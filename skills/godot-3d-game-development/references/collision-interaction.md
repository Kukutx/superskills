# Collision and Interaction Reference

Use for `CollisionShape3D`, PhysicsBody3D/Area3D contact, ray/shape queries, interaction targeting and 3D combat contact. Movement/camera ownership is in `spatial-movement-camera.md`.

## 1. Choose collision by role, not visual fidelity

For moving/dynamic actors, prefer simple primitive shapes when they approximate gameplay well:

- `CapsuleShape3D` / `BoxShape3D` / `SphereShape3D` / `CylinderShape3D`;
- convex shapes when a primitive is insufficient;
- multiple simple/convex shapes only when the extra accuracy has gameplay value.

Do not make a detailed render mesh the collision shape merely because it exists.

## 2. Concave/trimesh is static-world collision

Concave/trimesh collision can represent complex level geometry but is not a valid dynamic CharacterBody3D/RigidBody3D shortcut. Use it with static world bodies where its accuracy is actually useful.

For moving props/characters, simplify the collision or use convex decomposition as appropriate.

## 3. Keep collision geometry stable

Prefer fixing source shape/size over repeatedly rotating/scaling collision shapes to compensate for a bad hierarchy. Keep the number of shapes as low as the gameplay permits, especially for moving bodies.

Visual details such as small bevels, foliage, trim and decorative mesh noise usually do not deserve matching collision.

## 4. Layer and mask first

Before changing logic, inspect:

```text
body/area type
collision layer
collision mask
shape enabled state
shape transform
monitoring/monitorable when Area3D is involved
expected query/callback
physics timing
```

Groups/tags may classify objects, but they should not replace physics filtering when layer/mask semantics solve it cleanly.

## 5. Overlap vs ray vs volume query

Choose the primitive that expresses the gameplay question:

| Question | Typical tool |
| --- | --- |
| what entered/stays inside a volume? | `Area3D` |
| what is directly along a line? | `RayCast3D` or direct-space ray query |
| can a volume move/fit along this path? | `ShapeCast3D` / shape query |
| what did this moving physics body contact? | body collision result/callback |

Do not choose a query API because of unverified performance folklore. Use the clearest semantic tool, then profile if query volume becomes material.

## 6. Camera/player interaction ray

For center-screen or cursor interaction, define:

```text
ray origin
ray direction / projected screen point
max interaction distance
collision mask
occlusion policy
accepted target type
```

The visible crosshair and the physics query must represent the same interaction rule. Do not allow UI highlighting to become the source of interaction truth.

## 7. 3D hitboxes / hurtboxes

The same ownership rule applies as in other combat systems:

```text
attack/state authorizes hit window
-> 3D hitbox/query detects candidate
-> combat receiver validates repeated-hit/i-frame/team rules
-> gameplay result
-> animation/VFX/audio/camera react
```

Use `Area3D` or explicit shape/ray queries according to weapon semantics. Keep active windows explicit; do not leave melee hit volumes permanently damaging everything they overlap.

Projectile visuals and collision shapes should be readable and consistent, but do not need pixel-perfect mesh matching.

## 8. Physics-callback mutation

When enabling/disabling/replacing collision state from inside physics callbacks, respect the engine's safe/deferred-change requirements for the exact node/property/version. Do not "fix" a callback error by adding arbitrary delays without understanding the ownership/timing issue.

## 9. Validation

Test:

- layer/mask matrix with intended and unintended targets;
- wall/floor/edge/corner contact;
- fast motion where tunneling could matter;
- camera interaction through/behind occluders;
- close-range ray origin edge cases;
- multi-target melee overlap and repeated-hit policy;
- shape enable/disable lifecycle;
- imported/static level collision at stairs/doorways/small details;
- performance only under a representative query/contact load.
