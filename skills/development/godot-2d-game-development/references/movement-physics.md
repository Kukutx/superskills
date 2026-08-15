# Movement and Physics Reference

Use for `CharacterBody2D`, top-down/platformer movement, jump/dash, collision response, moving platforms and knockback interaction. Camera behavior is in `camera.md`; device/remap concerns belong to `development/godot-project-systems`.

## Physics owns movement truth

Keep authoritative movement in `_physics_process()`:

```text
consume intent
-> update movement/state
-> update velocity
-> move_and_slide()
-> inspect floor/wall/collision result
```

Animation/FX may represent movement but should not become the hidden source of physical displacement.

## Top-down movement

Make explicit only what the game needs:

- diagonal normalization;
- instant vs accelerated velocity;
- facing independent from travel direction;
- dash/knockback override or additive behavior;
- y-sort/depth applied to presentation rather than corrupting physics truth.

## Platformer feel

Add coyote time, jump buffer, variable jump, rise/fall gravity, apex tuning, acceleration/deceleration and floor/slope behavior only when they serve the intended feel. They are not a mandatory checklist.

## Dash contract

Define:

```text
direction source
duration or distance
speed profile
cooldown
collision behavior
invulnerability yes/no
cancel rules
control lock degree
```

Do not let animation duration silently define dash gameplay.

## Knockback

If the controller rewrites velocity every tick, a one-off external impulse can disappear immediately. Choose an explicit model:

- temporary knockback state;
- additive external velocity;
- controlled override;
- reduced/locked control window.

Visual recoil belongs on visual children when it should not move the collision body.

## Collision debugging order

Check body/area type, layer, mask, enabled shape, Area monitoring, transforms/scale, expected callback/query and physics timing before assuming an engine bug.

## Moving platforms / external motion

Define how platform/conveyor/push motion combines with player intent, whether departure inherits velocity, and how floor snap/slopes/corners behave. Avoid render-tick teleporting of physics bodies.

## Time scale / hit-stop

Confirm movement behavior, input buffering and timer time domains under pause/slowdown. Movement scripts should not privately reset global time scale.

## Validation

Test the relevant extremes: cardinal/diagonal changes, wall/corner/slope, jump edge cases, repeated dash, action/knockback transitions, moving platforms and pause/time-scale transitions.
