# Animation and 3D Asset Reference

Use for DCC -> Godot 3D import, glTF/Blender/FBX source choices, scale/pivot/orientation, Skeleton3D/skin, AnimationPlayer/AnimationTree, root motion and re-import safety.

## 1. One editable source of truth

A durable 3D handoff is:

```text
editable DCC/source asset
-> deterministic export/import settings
-> Godot imported scene/resources
-> gameplay wrapper/integration
```

Do not hand-edit an imported/generated scene and the DCC source as competing truths. Prefer an inherited/wrapper scene, import settings or a deliberate post-import step when Godot-side gameplay nodes must survive re-import.

## 2. Format choice

Godot's official 3D pipeline recommends glTF 2.0 (`.gltf`/`.glb`) as the general scene format.

Direct `.blend` import can be convenient because Godot invokes Blender's glTF export path, but it makes Blender part of the import environment. That can add team/CI/editor friction; use it only when that tradeoff is acceptable.

FBX/OBJ/other formats can be valid for existing pipelines, but do not switch formats merely for preference. Verify current importer support and what metadata the format can actually carry.

## 3. Scale, orientation and pivots

Before compensating in runtime code, inspect:

- source unit scale;
- imported root scale;
- forward/up convention;
- object origin/pivot;
- skeleton/rest pose;
- animation root;
- collision and attachment scale.

Fix systemic scale/orientation problems at the source/import boundary when practical. Avoid scattering corrective rotations/scales across gameplay scripts.

## 4. Imported scene ownership

Separate visual/imported hierarchy from gameplay ownership where useful:

```text
CharacterRoot (gameplay/physics)
├── imported visual/rig scene
├── collision
├── gameplay components
└── camera/interaction anchors as needed
```

Do not make fragile imported bone/mesh names the only gameplay API without a stable convention or explicit binding layer.

## 5. Skeleton and attachments

Use Skeleton3D/bone attachment mechanisms for visual equipment or effects that genuinely follow bones. Gameplay collision/weapon reach should still have a clear gameplay owner rather than depending on an arbitrary animated mesh vertex.

Check retarget/rest-pose assumptions when animations come from a different source rig.

## 6. AnimationPlayer vs AnimationTree

Use AnimationPlayer to store/edit authored animation timelines. Use AnimationTree when the project needs state/blend-space/blending control over those animations.

When AnimationTree is active and linked to an AnimationPlayer, let the tree own playback/transitions rather than driving the same playback independently from both systems.

Gameplay/state decides whether an action is allowed; animation represents and synchronizes it. Do not use an animation name as the only source of gameplay state.

## 7. Root motion

Root motion can supply movement deltas from animation. For a collision-driven character:

```text
animation/root motion delta
-> controller interprets desired displacement/velocity
-> CharacterBody3D applies collision-aware motion
-> visual rig stays synchronized
```

Do not blindly teleport the world collision body to the animated root transform when walls/slopes/gameplay collision matter.

Define rotation root motion separately from translation if the game needs only one of them.

## 8. Animation events

Footsteps, attack-release points, VFX/SFX and similar events can be synchronized from an authoritative animation/timeline, while gameplay systems still validate the actual state/result.

Interrupted/transitioned animations must not leave delayed gameplay-affecting events alive unexpectedly.

## 9. Import-time optimization

Use import options such as animation clip extraction, mesh/material settings, LOD or compression only when they serve the project. Keep the raw editable source and re-import path reproducible.

Do not bake destructive one-off fixes into imported outputs with no documented source path.

## 10. Validation

Verify:

- clean re-import produces the expected scene/resources;
- model scale/facing/pivots are stable;
- skeleton/skin/rest pose are correct;
- animation clips/ranges/loops are correct;
- AnimationTree transitions do not fight code/AnimationPlayer;
- attachments follow intended bones;
- root motion respects collision/state;
- source changes do not delete gameplay wrapper nodes;
- clean checkout/import works when the pipeline is expected to be reproducible.
