# Animation Runtime Reference

Use for Godot 2D runtime animation: `AnimatedSprite2D`, `SpriteFrames`, `AnimationPlayer`, `AnimationTree`, Tween, state synchronization and timing events.

Sprite generation/slicing/packing belongs to `development/sprite-animation-pipeline`; editable source/import belongs to `asset-pipeline.md`.

## Choose one authority per property/timeline

| Need | Prefer |
| --- | --- |
| frame-by-frame sprite animation | `AnimatedSprite2D` + `SpriteFrames` |
| property/audio/method/event tracks | `AnimationPlayer` |
| locomotion/state blending | `AnimationTree` backed by animations |
| dynamic one-shot presentation effect | `Tween` |

Do not let code, AnimationPlayer, AnimationTree and Tween fight over the same property.

## Gameplay owns intent

```text
input / AI intent
-> gameplay state allows action
-> animation selected
-> explicit timeline event when needed
-> owning gameplay/presentation systems react
```

Animation names should not become the only state machine.

## Timeline events

Use one authoritative timeline/event when presentation and gameplay must align. Animation events may request hitbox windows, projectile release, footsteps, SFX or particles, but combat/state still decides whether gameplay truth changes.

Do not let an animation track bypass combat ownership and directly mutate target HP.

## Attack timing

Think in:

```text
startup -> active -> recovery
```

Visual contact and active windows should agree, while cancel/input/damage rules remain gameplay-owned. Interrupted attacks must not leave delayed active events or hitboxes alive.

## Frame timing

Equal frame geometry does not imply equal duration. Intentional holds, impact emphasis and one-shot recovery may use different per-frame timing.

## Loop / transition semantics

Define loop vs one-shot, exit condition, interruption policy, restart/resume and AnimationTree transition behavior. Do not wait for a non-loop-style “finished” signal to exit a looping state.

Rapid transitions should not produce one-frame wrong poses or stale timeline events.

## Tween lifecycle

For repeatedly triggered presentation effects, store and replace/kill the previous Tween when it owns the same property. Visual Tween logic must not silently alter physics truth.

## Time domains

Under pause/hit-stop, define which runtime animations/Tweens continue, which input remains buffered and which timers use game vs real time. Helpers should not privately reset global time scale.

## Asset handoff

Runtime animation expects stable action names, frame ranges, timing metadata, loop policy, anchor/pivot and direction naming. If those are unstable, fix the asset pipeline instead of adding magic runtime indices/offsets.

## Validation

Test relevant transitions (idle/move/attack/hurt/death), rapid switching, loops, one-shots, attack-event alignment, interruption, repeated Tweens and pause/hit-stop behavior.
