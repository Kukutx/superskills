# Input, Controls and Accessibility Reference

Use for InputMap, keyboard/mouse/gamepad/touch, remapping, active-device detection, prompts, deadzones, rumble/haptics and control-related accessibility.

Movement/physics is in `movement-physics.md`; menu focus/layout pairs with `ui-ux.md`.

## Gameplay consumes actions, not physical buttons

```text
physical input
-> InputMap/action
-> gameplay intent
-> state decides whether action is allowed
```

Keep stable actions such as move, jump, attack, interact and pause; do not create separate gameplay logic for keyboard, gamepad and touch.

## Binding != meaning

`interact` is the stable semantic action; a key/button/touch control is a replaceable binding. UI prompts derive from current binding/device, settings persist bindings and gameplay stays hardware-agnostic.

## Device coexistence

Switch prompt families from meaningful recent input, with deadzone/threshold/debounce so analog drift or tiny mouse motion does not cause prompt flicker.

## Gamepad

Check deadzones, navigation focus, confirm/cancel mapping, disconnect/reconnect, device IDs when relevant, glyph families and rumble stop/disable behavior. Do not assume all controller layouts are identical.

## Remapping

```text
select action
-> listening state
-> capture allowed event
-> resolve conflict by explicit policy
-> update InputMap
-> persist
-> refresh prompts
```

Conflict policy should explicitly replace/swap/reject. Invalid persisted bindings need safe fallback, especially for menu confirm/back.

## Input buffering

For action games, a short expiry-based buffer can preserve responsiveness:

```text
press -> expiry -> consume once when state becomes valid
```

Only buffer actions the design allows; expired input must not fire later.

## Touch/mobile

Touch controls should emit the same gameplay actions. Check target size, safe area, virtual-stick deadzone/radius, drag/cancel, multi-touch, UI/gameplay conflicts and orientation/aspect changes.

## Prompts

Derive prompts from current action binding rather than hard-coded hardware text. Reuse the project's existing input abstraction when present.

## Rumble / haptics

Rumble is presentation, not gameplay truth. Match intensity/duration to event importance, prevent endless accumulation, stop on relevant pause/scene/device changes and support reduced/off settings when appropriate.

## Accessibility

As required by the project, consider remapping, hold/toggle choices, sensitivity/deadzones, reduced rumble/shake/flashes, complete keyboard/gamepad paths and non-color-only cues.

## Validation

Test relevant devices independently, unplug/replug, analog near deadzone, rapid device switching, remap conflicts/default restore, restart persistence, pause/menu navigation, touch multi-input and rumble stop/disable.
