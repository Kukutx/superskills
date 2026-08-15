# Pixel Animation Reference

Use this reference for 2D sprite animation, pixel-art consistency, AnimatedSprite2D, AnimationPlayer, AnimationTree and animation-to-gameplay synchronization.

## 1. Choose one animation authority

Pick the simplest tool that fits the job:

| Need | Prefer |
| --- | --- |
| Pure frame-by-frame sprite animation | `AnimatedSprite2D` + `SpriteFrames` |
| Animate properties, audio, hitbox windows, method calls, shader values | `AnimationPlayer` |
| Complex locomotion/state blending | `AnimationTree` over `AnimationPlayer` |
| Dynamic one-shot scale/position/color effects | `Tween` |

Do not let code, AnimatedSprite2D and AnimationPlayer all fight over the same sprite property.

## 2. Gameplay state owns intent

Animation should represent gameplay state:

```text
idle
run
jump
fall
attack
hurt
dash
death
```

Do not use a pile of animation-name checks as the only gameplay state machine.

A useful flow is:

```text
input/gameplay state -> select animation -> animation events -> presentation/hit windows
```

## 3. Frame-perfect events

Use explicit animation events for things that must align visually:

- enable/disable hitbox;
- spawn projectile;
- play impact/whoosh SFX;
- footstep;
- spawn particles;
- change weapon trail;
- trigger shader flash.

Prefer one authoritative animation timeline over independent timers.

For looping animations, use loop-aware signals/events; do not assume a non-looping completion signal will fire for loops.

When changing animation and another sprite property in the same frame, be aware that engine update timing can create a one-frame mismatch. If exact same-frame synchronization matters, use the Godot API appropriate to the project version to advance/apply the new pose immediately.

## 4. Tween lifecycle

Procedural animation such as squash/stretch is useful for:

- landing;
- jump launch;
- pickup pop;
- recoil recovery;
- UI response.

If the same effect can trigger again before the previous Tween finishes:

```text
store tween -> kill/replace old tween -> start new tween
```

Do not stack multiple Tweens on one property.

## 5. Pixel-art asset consistency

For AI-generated or manually assembled animation, preserve these invariants across all frames:

- same character identity;
- same proportions;
- same facing direction per strip;
- same outfit / weapon design;
- same palette family;
- stable silhouette;
- stable scale;
- stable anchor, usually bottom-center/feet;
- transparent background;
- exact frame count and slot layout.

The animation must read at **actual in-game scale**, not only when zoomed in.

## 6. Approved seed frame workflow

For generated animation, prefer this production sequence:

1. Create or choose one approved in-game seed frame.
2. Lock its silhouette, palette, outfit, proportions and facing direction.
3. Generate the **whole animation strip in one pass** when possible.
4. Normalize all frames to one frame size.
5. Apply one shared scale across the strip.
6. Align all frames to one shared anchor.
7. Optionally replace frame 1 with the exact approved seed if continuity requires it.
8. Preview the strip as an animation before importing it into the game.

Do **not** independently generate every frame unless the user accepts higher visual drift.

This is especially important for pixel art because small shape changes are obvious in motion.

## 7. Animation timing

Frame count alone does not determine feel. Tune frame duration and holds.

Typical principles:

- idle: subtle, slower loop;
- run: clear contact/passing poses and even rhythm;
- anticipation: often longer than the fastest action frames;
- attack impact: strong readable key pose, sometimes held briefly;
- hurt: fast reaction with a clear recoil silhouette;
- death: readable progression, then stable final pose if needed.

Do not force every animation to the same FPS.

## 8. Attack animation structure

For action games, think in gameplay phases:

```text
startup -> active -> recovery
```

Example visual planning:

```text
frames 1–2: anticipation/startup
frames 3–4: active strike
frames 5–6: follow-through/recovery
```

The exact numbers depend on combat speed. The important part is that hitbox timing and visuals agree.

## 9. Squash and stretch

Use subtle procedural deformation to reinforce force:

- jump: brief vertical stretch;
- landing: brief horizontal squash;
- heavy impact: compress then recover;
- pickup/UI: overshoot then settle.

For pixel art, keep deformation small enough that pixels remain intentional. Strong subpixel scaling can cause shimmering or blurry sampling.

## 10. Pixel rendering rules

For crisp pixel art:

- use point/nearest filtering where appropriate;
- avoid unintended texture filtering and mip blur;
- prefer integer display scales when the art direction requires strict pixel fidelity;
- keep camera/subpixel movement strategy consistent with the project;
- do not mix multiple incompatible source resolutions without a deliberate scale policy.

If the game intentionally uses smooth camera motion with pixel art, validate the final look in motion rather than blindly enforcing integer-only movement everywhere.

## 11. Spritesheet structure

When producing a conventional sheet, define:

```text
frame width
frame height
rows
columns
action order
frames per action
padding
spacing
anchor/baseline
```

For slicing/naming/export details, use `development/game-dev-spritesheet-slicer` rather than duplicating that workflow here.

## 12. Animation QA

Before approval, inspect the animation as a loop and as gameplay:

- identity/proportions stay stable;
- feet/anchor do not unintentionally slide;
- frame size does not drift;
- weapon does not change shape or hand unexpectedly;
- silhouette clearly communicates the action;
- no accidental extra limbs/props;
- action reads at game scale;
- first/last frames loop cleanly when intended;
- attack event and hitbox timing match;
- hurt/death one-shots exit or stop correctly;
- repeated state changes do not cause visible one-frame flashes.

## Upstream inspiration

Condensed from `godot-2d-animation` in `thedivergentai/GD-Agentic-Skills` and `sprite-pipeline` in `openai/plugins`. The approved-seed + whole-strip + shared scale/anchor workflow is intentionally retained because independent frame generation causes visible drift.