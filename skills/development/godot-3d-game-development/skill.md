---
name: godot-3d-game-development
description: Godot 4.x 3D game runtime and production guidance for spatial transforms, CharacterBody3D/physics, Camera3D, collisions/interactions, rendering/lighting/worlds, animation/rigging/import, and NavigationAgent3D. Use when the task is materially 3D-specific.
---

# Godot 3D Game Development

## Scope

Use for Godot 4.x work where the **3D dimension changes the implementation**: transforms, CharacterBody3D/physics, Camera3D, 3D collision/query semantics, spatial rendering, imported 3D assets/rigging or NavigationAgent3D.

Use `development/godot-2d-game-development` for 2D/pixel runtime work.

Do not recreate dimension-neutral Godot knowledge here merely for completeness. UI with `Control`, InputMap, Resources/signals, save/inventory/dialogue data and ordinary release/process concerns should follow the real project's conventions; pair a generic development/operations Skill only when it owns a distinct subproblem.

## Inspect first

Before changing a 3D project, resolve the relevant subset:

```text
Godot version + renderer + target platform
scene/root/body types + language
global/local transform conventions
collision layers/masks + shape ownership
camera rig + input/aim model
3D source assets + import settings + skeleton/animations
navigation regions/maps/agents
the actual runtime or performance symptom
```

Do not impose a starter architecture on an existing project.

## Core invariants

1. **Spatial math is explicit**: distinguish local/global transforms, visual scale and gameplay orientation. For repeated 3D rotation/interpolation, reason with vectors/Basis/Quaternion rather than casually accumulating Euler angles.
2. **Physics owns physical truth**: CharacterBody3D/RigidBody3D/StaticBody3D and their controller rules own motion/collision; camera/model/VFX children represent it.
3. **Collision follows body role**: prefer simple primitive/convex shapes for moving bodies; concave/trimesh collision is static-world territory, not a shortcut for dynamic actors.
4. **One asset source of truth**: imported meshes/rigs/animations must have a reproducible source -> import -> runtime handoff. Do not hand-maintain competing source and imported states.
5. **Rendering advice is target-dependent**: renderer, hardware, scene scale and measured bottleneck decide lighting/GI/LOD/occlusion choices. Avoid copied numeric budgets as universal rules.
6. **Navigation output is not movement ownership**: NavigationAgent3D supplies path/avoidance information; the parent movement/controller applies valid motion.
7. **Evidence matches the claim**: import success, runtime collision, camera behavior, animation, visuals and performance require their own evidence.

## Runtime references

| Need | Reference |
| --- | --- |
| Node3D/Transform3D, CharacterBody3D movement, first/third-person Camera3D rigs | `references/spatial-movement-camera.md` |
| CollisionShape3D, Area3D, ray/shape queries, interaction and 3D combat contact | `references/collision-interaction.md` |
| materials, lights, Environment/GI, world rendering, LOD/occlusion and measured performance | `references/rendering-lighting-world.md` |
| glTF/Blender import, Skeleton3D, AnimationPlayer/Tree, root motion and re-import safety | `references/animation-assets.md` |
| NavigationAgent3D, nav geometry, perception and AI movement handoff | `references/navigation-ai.md` |

Normally load one reference first and add a neighboring reference only when the problem genuinely crosses the boundary.

## Common routing examples

- third-person controller + wall-clipping camera -> `spatial-movement-camera.md`
- moving character uses trimesh collision -> `collision-interaction.md`
- crosshair ray selects the wrong object -> `collision-interaction.md` + camera context only if needed
- imported Blender character has broken scale/rig/animations -> `animation-assets.md`
- root motion visually moves through walls -> `animation-assets.md` + `spatial-movement-camera.md`
- scene looks correct but shadows/GI tank frame time -> `rendering-lighting-world.md`
- NavigationAgent3D jitters near the target -> `navigation-ai.md`

## Dependency rule

Prefer:

```text
existing project pattern
-> native Godot capability
-> focused addon/tool only for demonstrated recurring pain
```

Before adopting a current addon/importer/controller framework, re-check exact Godot compatibility, maintenance, license, overlap, source-of-truth impact and removal cost. Do not keep a static plugin catalog in runtime guidance.

## Completion bar

Check the relevant subset before saying done:

- actual Godot version/renderer/project conventions were respected;
- transforms/scale and physics ownership are unambiguous;
- collision/query choice matches the object's role;
- imported assets can be reproduced from their intended source;
- camera/animation/navigation do not silently bypass gameplay physics;
- visual/performance claims were checked on the relevant renderer/target or explicitly remain unverified;
- no 2D-only assumptions or unrelated framework were introduced.
