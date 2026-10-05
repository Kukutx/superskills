# Godot Verification and Testing Reference

Use for runtime bugs, behavior verification, automated tests, visual/runtime QA and evidence-driven validation after Agent changes in either 2D or 3D projects.

## Core loop

```text
reproduce exact behavior
-> inspect relevant state/errors
-> isolate subsystem
-> make smallest change
-> rerun the same reproduction
-> compare with expected result
-> regression check
```

Do not change several plausible causes at once, and do not treat parse/build success as proof that interaction or visual behavior is fixed.

## Match evidence to the claim

| Claim | Evidence |
| --- | --- |
| scene/resource loads | no relevant parse/resource errors |
| button/input works | actual input causes expected transition |
| collision/movement fixed | controlled runtime reproduction |
| animation/VFX correct | runtime observation / frame preview |
| save fixed | write -> restart/load -> compare state |
| performance fixed | profiler/frame-time evidence |
| export fixed | clean export + artifact smoke check |

Evidence should verify the user's actual result, not an easier proxy.

## Smallest executable surface

Prefer an isolated test scene, affected level, focused UI screen or minimal reproduction. Only run the complete game flow when the bug genuinely depends on it.

## Test layers

### Logic tests

Useful for formulas, inventory rules, save migration, state transitions, procedural invariants and pure data logic.

### Scene / integration tests

Useful for signal wiring, collision, spawned-scene setup, UI flow and save/load application.

### Runtime / playtest

Required for movement/camera feel, animation timing, combat feel, spatial interaction, visual readability, controller focus and other behavior that cannot be established statically.

Use the project's existing framework/harness when present. Do not install a test framework merely for formal completeness.

## Runtime automation

If the environment already supports run/input/screenshot/error capture:

- reuse it;
- prefer semantic/project actions over fragile coordinates where possible;
- make press/hold/release reflect real behavior;
- verify keyboard/gamepad focus/confirm/back for UI;
- remember a screenshot proves visible state, not physics/combat correctness by itself.

Do not modify gameplay logic only to make automation tooling easier.

## Error capture

After changes, check relevant parse/runtime errors, invalid get/set/call, missing nodes/resources, shader/import/addon failures and newly introduced relevant warnings.

A visually plausible result does not excuse new runtime errors.

## Stable reruns

Return to a predictable state before repeated tests: reload the scene, restart the game, use an existing debug reset or load a controlled fixture. Do not rely on residue from the previous run.

## Without live tooling

Use the strongest available evidence:

```text
Godot editor/CLI checks
+ existing tests
+ targeted manual reproduction steps
+ user-provided screenshot/log when required
```

Keep completion language precise:

- `implemented`
- `static checks passed`
- `runtime checks passed`
- `visual checks passed`
- `not verified: <reason>`

Tests that could not run must not be described as passed.

## Domain handoff

When the reproduction is dimension-specific, use the matching domain Skill for the actual invariant:

- Godot 2D -> movement/Camera2D/combat/2D rendering/navigation rules;
- Godot 3D -> spatial movement/Camera3D/collision/rendering/import/navigation rules;
- project systems -> input/UI/audio/save/inventory/dialogue/export rules.

Verification owns the evidence loop, not the domain truth itself.

## Completion rule

The claimed verification level must match the evidence collected. Avoid “应该好了” and do not package static confidence as runtime confirmation.
