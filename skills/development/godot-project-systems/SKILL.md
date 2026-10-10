---
name: godot-project-systems
description: Godot 4.x dimension-neutral project systems for architecture, InputMap, Control UI, audio, persistence, inventory/progression, dialogue/localization, verification and export/CI. Use when the task applies similarly to both 2D and 3D projects.
---

# Godot Project Systems

## Scope

Use for Godot concerns where **2D vs 3D does not materially change the implementation**: scene/data ownership, Resources/signals/autoloads, input/remapping, Control UI, audio organization, persistence, inventory/progression, dialogue/localization, verification and export/CI.

Use `development/godot-2d-game-development` when CharacterBody2D, Camera2D, TileMapLayer, 2D animation/combat/VFX/navigation or other 2D runtime semantics matter.

Use `development/godot-3d-game-development` when Transform3D, CharacterBody3D, Camera3D, 3D collision/rendering/import/navigation or other spatial semantics matter.

Do not load a dimensional Skill merely because the project happens to be 2D or 3D when the current subproblem is dimension-neutral.

## Inspect first

Resolve only the relevant subset:

```text
Godot version + language
scene/autoload/resource conventions
InputMap and UI structure
data/save/content ownership
existing test/export/CI setup
target platform when it changes behavior
```

Preserve project conventions unless they are the source of the problem.

## Core invariants

1. **One owner per fact**: gameplay/data systems own state; UI/audio/animation present it; persistence stores durable representation.
2. **Semantic input before hardware**: gameplay consumes actions, not keyboard/gamepad/touch branches.
3. **UI displays domain truth**: Control trees should not reconstruct gameplay state from widget state.
4. **Stable IDs for durable data**: display text, runtime instance IDs and fragile NodePaths are not save/content identity.
5. **Source of truth survives iteration**: editable content/config -> deterministic handoff -> runtime representation.
6. **Evidence matches the claim**: parse/build, runtime, visual, save/load and export are different verification levels.
7. **Native/existing before dependency**: add frameworks only for demonstrated recurring complexity.

## Runtime references

| Need | Reference |
| --- | --- |
| scenes, ownership, Resources, signals, autoloads, state boundaries | `references/core-architecture.md` |
| InputMap, keyboard/gamepad/touch, remapping, prompts, control accessibility | `references/input-controls-accessibility.md` |
| Control/Container/Theme, HUD/menu flow, focus, safe area, responsive UI | `references/ui-ux.md` |
| SFX/music, buses, variation, ducking and positional/non-positional audio | `references/audio.md` |
| save/load, stable IDs, schema migration, settings/checkpoints | `references/save-persistence.md` |
| item definitions, inventory/equipment transactions and progression | `references/inventory-progression.md` |
| branching dialogue, conditions/effects and localization | `references/dialogue-localization.md` |
| reproduce/debug/test/runtime evidence and verification boundaries | `references/verification-testing.md` |
| export presets, clean CI, toolchain pinning and artifact checks | `references/release-export-ci.md` |

Normally load one reference first. Add a 2D/3D Skill only when the task crosses into dimensional runtime behavior.

## Routing examples

- remappable controls + controller glyph switching -> `input-controls-accessibility.md`
- pause/settings menu focus or responsive HUD -> `ui-ux.md`
- save v2 cannot migrate renamed item IDs -> `save-persistence.md` + inventory context only if the runtime transaction itself is wrong
- branching dialogue with localized choices -> `dialogue-localization.md` + UI/input only as needed
- clean Godot export in GitHub Actions -> `release-export-ci.md`
- prove a pause-menu controller fix really works -> `verification-testing.md` + UI/input as needed
- CharacterBody2D dash bug -> 2D Skill, not this Skill
- CharacterBody3D camera collision -> 3D Skill, not this Skill

## Dependency rule

Prefer:

```text
existing project pattern
-> native Godot capability
-> focused addon/tool only for demonstrated recurring pain
```

For current addons, APIs, platform/export requirements or version-sensitive behavior, verify the project's exact Godot version and current primary documentation instead of relying on static repository memory.

## Completion bar

Before saying done, confirm the relevant subset:

- ownership/state boundaries remain unambiguous;
- input/UI/audio are presentation or intent layers rather than hidden gameplay truth;
- durable IDs/schema/content ownership survive reload/re-import where relevant;
- the changed flow has evidence at the level claimed;
- export/release claims are based on the produced artifact, not only source/build success;
- no unnecessary 2D/3D subsystem or dependency was introduced.
