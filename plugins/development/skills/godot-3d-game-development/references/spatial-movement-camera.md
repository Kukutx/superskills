# Spatial Movement and Camera Reference

Use for `Node3D`/`Transform3D`, CharacterBody3D movement and first-/third-person Camera3D rigs. Collision/query semantics are in `collision-interaction.md`; imported model/rig concerns are in `animation-assets.md`.

## 1. Treat 3D transforms as spatial data

Keep these distinctions explicit:

```text
local transform != global transform
position != orientation != visual scale
body transform != model/camera presentation transform
```

For simple one-axis editor-style rotations, Euler properties can be fine. For repeated rotation, orientation composition or interpolation, prefer vectors, `Basis` or quaternions rather than repeatedly reading/modifying Euler angles and assuming rotation order does not matter.

Godot's conventional forward direction for many 3D nodes is `-Z`; verify the imported asset/controller convention instead of compensating with unexplained magic rotations.

## 2. Avoid hidden scale problems

Physics/manipulated transform roots are easier to reason about at unit scale. Prefer scaling visual mesh children or fixing source/import scale rather than carrying arbitrary non-uniform scale through movement, collision, rigging and camera math.

When scale is inherited from imported content, inspect the real node hierarchy before "fixing" it in code.

## 3. CharacterBody3D owns controlled movement

A typical controlled-body loop remains:

```text
consume input/AI intent
-> derive desired 3D direction
-> update velocity/state/gravity
-> move_and_slide()
-> inspect floor/wall/contact state
-> emit presentation events
```

Keep authoritative movement in `_physics_process()` unless the existing project has a deliberate alternative.

Do not drive the collision body by directly copying the animated model or camera transform every render frame.

## 4. Camera-relative movement

For third-person/top-down 3D controls, input often needs conversion from camera space to the gameplay movement plane:

```text
input vector
-> camera horizontal forward/right
-> flatten/project onto movement plane
-> normalize only when intended
-> desired movement direction
```

Do not accidentally include camera pitch in ground movement and send the character into the floor/air.

For free-flight/space movement, do not flatten the vector; define the intended six-degree-of-freedom rules explicitly.

## 5. First-person camera ownership

A simple FPS rig often separates:

```text
body yaw
-> camera/head pitch
```

Clamp pitch only as required by the game. Keep view rotation separate from collision/body rotation when doing so prevents unwanted tilt/roll.

Input sensitivity, capture and remapping remain InputMap/project concerns rather than camera state truth.

## 6. Third-person camera rig

A robust third-person camera normally separates:

```text
target/body
-> pivot/orbit rig
-> optional collision avoidance arm/query
-> Camera3D
```

`SpringArm3D` is a native option for camera collision/occlusion. Use it when it matches the desired behavior; do not add a third-party camera system before the native/project rig has shown a real limitation.

Camera smoothing/look-ahead/shoulder offsets are presentation. They should not move the CharacterBody3D or redefine its collision position.

## 7. Aim vs body orientation

Make the relationship explicit:

- movement direction may differ from aim direction;
- camera yaw may differ from model facing;
- upper-body aim may be animation/IK while locomotion remains physics-owned;
- lock-on can influence desired facing without making the camera the gameplay owner.

Avoid deriving gameplay truth from the rendered mesh's temporary recoil/animation transform.

## 8. Root motion handoff

If animation supplies root-motion displacement, treat it as motion input/delta that the controller reconciles with collision and state. Do not bypass CharacterBody3D collision by blindly applying the animated root transform to the world body.

Detailed import/AnimationTree ownership is in `animation-assets.md`.

## 9. Validation

Test the relevant extremes:

- local/global transform assumptions after reparenting;
- imported model facing/scale;
- slopes, walls, stairs and fast direction changes;
- camera-relative movement with large pitch/yaw changes;
- first-person pitch/yaw separation;
- third-person wall/ceiling camera occlusion;
- camera smoothing during fast body motion;
- animation/root-motion interaction with collision;
- pause/time-scale if the controller uses them.
