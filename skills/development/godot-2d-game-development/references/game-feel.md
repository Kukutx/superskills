# Game Feel Reference

Use when mechanics are already correct but lack weight/readability: hit-stop, camera shake, recoil, squash/stretch, flash, impact FX, popups, rumble and audio-visual layering.

If interaction/contact correctness is unreliable, use `combat-system.md` first. Shared audio/input/accessibility concerns belong to `development/godot-project-systems`.

## Feedback reacts to truth

```text
confirmed gameplay event
-> feedback bundle
```

Presentation must not become the authority that decides whether the gameplay event happened.

## Layer from small to large

A strong impact usually comes from a few aligned short signals rather than one exaggerated effect:

```text
impact sound
+ contact flash/FX
+ gameplay knockback or visual recoil
+ optional short hit-stop
+ optional small camera shake
+ optional popup/rumble
```

Start with 2–3 useful layers, play the game, then decide whether more helps.

## Importance tiers

Keep a relative hierarchy between ordinary, strong and authored high-impact events. Do not give every event maximum shake, stop and screen FX.

## Hit-stop

Use only on a confirmed meaningful event and keep it proportional to the game. Important rules:

- it must always recover;
- do not use blocking sleep;
- define time-scale ownership;
- input/timers must use the intended time domain;
- repeated triggers must remain bounded.

Tune by playtesting rather than treating a fixed duration as universal.

## Camera shake

Prefer bounded intensity/trauma with smooth noise/oscillation and decay. Avoid completely random per-frame offsets.

Shake modifies Camera2D presentation, not the player/world physics transform. Reduced-shake settings belong to the shared project-systems accessibility path.

## Flash / shader feedback

A short material/shader flash can provide inexpensive confirmation. Re-triggered effects should restart/replace rather than stack indefinitely. Check shared-material ownership so one actor does not unintentionally alter every instance.

## Recoil and squash/stretch

Presentation recoil can affect weapon/sprite visual offset, scale or rotation. Physical knockback belongs to gameplay movement/interaction owners.

When repeatedly triggering a Tween on the same property:

```text
store current tween
-> kill/replace
-> start new tween
```

## Particles / impact FX

Effects should clarify position, direction, type and event importance without hiding important poses or telegraphs. Keep lifetimes controlled and clean up one-shot effects.

Detailed 2D rendering/shader concerns are in `rendering-vfx-shaders.md`.

## Sound / rumble

Sound and rumble reinforce feedback but remain presentation. Shared bus/mix/device/accessibility behavior belongs to `development/godot-project-systems`; this reference only decides how strongly an event should feel.

## Movement / UI feel

The same rule applies to jump, land, dash, pickup and UI confirmation: add only feedback that makes the state/change easier to perceive, and always return presentation properties to a stable resting state.

## Common failure modes

- hit-stop feels like input lag;
- shake never returns to neutral;
- flash/Tween stacks do not reset;
- effects obscure gameplay readability;
- every event has the same intensity;
- feedback fires before the underlying event is confirmed;
- polish changes collision/aim/physics truth;
- performance problems trigger premature pooling/framework work without measurement.

## Validation

Test during real repeated play, not only one staged event. Verify responsiveness, complete recovery to neutral, readable simultaneous events, clear hierarchy between ordinary/strong moments and any implemented reduced-feedback settings.
