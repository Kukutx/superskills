---
name: godot-3d-game-development
description: Godot 4.x 3D-specific runtime and production guidance for spatial transforms, CharacterBody3D/physics, Camera3D, 3D collision/interaction, rendering/lighting/worlds, animation/rigging/import and NavigationAgent3D.
---

# Godot 3D Game Development

## Scope

Use for Godot 4.x work where the **3D dimension materially changes implementation**: transforms, CharacterBody3D/physics, Camera3D, 3D collision/query semantics, spatial rendering, imported 3D assets/rigging or NavigationAgent3D.

Use `development/godot-project-systems` for dimension-neutral Godot architecture, InputMap/remapping, Control UI, audio, save/inventory/dialogue, verification and export/CI.

Use `development/godot-2d-game-development` for 2D/pixel runtime work.

Do not recreate shared project-system knowledge here merely for completeness.

## Inspect first

Resolve the relevant subset:

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
2. **Physics owns physical truth**: CharacterBody3D/RigidBody3D/StaticBody3D and controller rules own motion/collision; camera/model/VFX children represent it.
3. **Collision follows body role**: prefer simple primitive/convex shapes for moving bodies; concave/trimesh collision belongs to static-world use.
4. **One asset source of truth**: imported meshes/rigs/animations need a reproducible source -> import -> runtime handoff.
5. **Rendering advice is target-dependent**: renderer, hardware, scene scale and measured bottleneck decide lighting/GI/LOD/occlusion choices.
6. **Navigation output is not movement ownership**: NavigationAgent3D supplies path/avoidance information; the parent controller applies valid motion.
7. **Shared systems stay shared**: do not fork UI/save/input/export architecture into a 3D variant without a real dimensional reason.
8. **Evidence matches the claim**: use the shared verification owner when completion depends on runtime/visual/export evidence.

## Runtime references

| Need | Reference |
| --- | --- |
| Node3D/Transform3D, CharacterBody3D movement, first/third-person Camera3D rigs | `references/spatial-movement-camera.md` |
| CollisionShape3D, Area3D, ray/shape queries, interaction and 3D contact | `references/collision-interaction.md` |
| materials, lights, Environment/GI, world rendering, LOD/occlusion and measured performance | `references/rendering-lighting-world.md` |
| glTF/Blender import, Skeleton3D, AnimationPlayer/Tree, root motion and re-import safety | `references/animation-assets.md` |
| NavigationAgent3D, nav geometry, perception and AI movement handoff | `references/navigation-ai.md` |
| architecture/input/UI/audio/save/inventory/dialogue/verification/export | `../godot-project-systems/skill.md` |

Normally load one 3D reference first. Add the shared Skill only when the task genuinely crosses into a dimension-neutral project-system concern.

## Routing examples

- third-person controller + wall-clipping camera -> `spatial-movement-camera.md`
- moving character uses trimesh collision -> `collision-interaction.md`
- imported Blender character has broken scale/rig/animations -> `animation-assets.md`
- root motion visually moves through walls -> `animation-assets.md` + `spatial-movement-camera.md`
- shadows/GI cause a measured frame-time problem -> `rendering-lighting-world.md`
- NavigationAgent3D jitters near target -> `navigation-ai.md`
- pause/settings focus, save migration or export CI -> `../godot-project-systems/skill.md`

## Dependency rule

Prefer existing project pattern -> native Godot capability -> focused addon/tool only for demonstrated recurring pain. Re-check current compatibility, maintenance, license, overlap and removal cost before adoption.

## Completion bar

Check the relevant subset before saying done:

- exact Godot version/renderer/project conventions were respected;
- transforms/scale and physics ownership are unambiguous;
- collision/query choice matches object role;
- imported assets reproduce from their intended source;
- camera/animation/navigation do not silently bypass gameplay physics;
- visual/performance claims were checked on the relevant target or remain explicitly unverified;
- dimension-neutral concerns use the shared owner;
- no 2D-only assumption or unrelated framework was introduced.
