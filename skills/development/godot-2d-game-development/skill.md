---
name: godot-2d-game-development
description: Godot 4.x 2D/pixel-game production router for architecture, movement/physics, camera, input, worlds, runtime animation, combat, game feel, VFX, UI, audio, AI, procedural content, persistence, inventory, dialogue, assets, verification, performance and export.
---

# Godot 2D Game Development

## Scope

Use for Godot 4.x **2D-first** implementation and production. Route elsewhere when the main task is Godot 3D, networking/server architecture, unrelated backend/frontend, or pure game design/writing without implementation concerns.

## Core invariants

1. **Inspect the real project first**: Godot version, `project.godot`, language, scene tree, autoloads, Resources, signals, InputMap, collision layers, addons and existing conventions.
2. **Gameplay truth before presentation**: physics/combat/data/state own facts; animation/VFX/audio/camera/UI react to them.
3. **Smallest reference set**: load one primary reference first, then add only the focused neighbors required by the current subproblem.
4. **Existing/native before dependency**: add tooling only for demonstrated recurring complexity.
5. **Evidence before completion claims**: parse/build success is not runtime, visual, input, save or export proof.

## Routing precedence

```text
correctness / gameplay truth
-> input / interaction
-> presentation synchronization
-> game feel / polish
-> measured performance
-> release / CI
```

Examples:

- one swing deals damage three times -> `combat-system.md`
- damage is correct but hit feels weak -> `game-feel.md`
- attack active frame disagrees with hit window -> `animation-runtime.md` + `combat-system.md`
- smooth follow/look-ahead/bounds problem -> `camera.md`
- generate/slice/package a new attack strip -> `../sprite-animation-pipeline/skill.md`
- authored sprite metadata must survive import -> `asset-pipeline.md` + animation runtime as needed
- seeded dungeon/layout generation -> `procedural-generation.md` + world reference when materializing tiles/scenes
- save migration failure -> `save-persistence.md`
- stack/equip/transfer logic -> `inventory-progression.md`

## Runtime references

| Need | Reference |
| --- | --- |
| scenes, ownership, Resources, signals, state/FSM | `references/core-architecture.md` |
| CharacterBody2D, movement, jump/dash, collisions, knockback | `references/movement-physics.md` |
| Camera2D follow, bounds, look-ahead, pixel camera | `references/camera.md` |
| InputMap, keyboard/gamepad/touch, remap, device switching, accessibility | `references/input-controls-accessibility.md` |
| TileMapLayer, terrain/world layout, y-sort, collision/navigation, level authoring | `references/world-tilemap-level-design.md` |
| AnimationPlayer/Tree, SpriteFrames, Tween, runtime timing/events | `references/animation-runtime.md` |
| hitbox/hurtbox, damage, i-frame, combo/cancel | `references/combat-system.md` |
| hit-stop, shake, flash, recoil, squash, impact feedback | `references/game-feel.md` |
| particles, CanvasItem shaders, 2D lighting/effects | `references/rendering-vfx-shaders.md` |
| HUD/menu, Control/Container/Theme, focus, safe area | `references/ui-ux.md` |
| SFX/music, buses, variation, ducking, positional audio | `references/audio.md` |
| enemy behavior, perception, state complexity, NavigationAgent2D | `references/ai-navigation.md` |
| seeded generation, waves/spawn rules, generated-layout validity | `references/procedural-generation.md` |
| save/load, stable IDs, schema migration, settings/checkpoints | `references/save-persistence.md` |
| item definitions, inventory/equipment transactions, progression | `references/inventory-progression.md` |
| branching dialogue, conditions/effects, localization | `references/dialogue-localization.md` |
| editable asset source, import, FX/map/tiles/UI handoff | `references/asset-pipeline.md` |
| reproduce/debug/test/runtime evidence | `references/verification-testing.md` |
| profiling, frame-time, memory and measured optimization | `references/performance.md` |
| export presets, clean CI, toolchain pinning, artifacts | `references/release-export-ci.md` |
| sprite-strip generation, exact frame geometry, slicing, timing metadata, naming/packing | `../sprite-animation-pipeline/skill.md` |

Maintenance material lives in `maintenance/` and is not normal runtime context.

## Cross-system ownership

```text
physical input -> action intent
state/controller -> action allowed + gameplay state
physics/combat/data -> result
explicit events -> animation/UI/audio/VFX/camera
save system -> persistent representation
```

When timing must match, share one explicit event/timeline rather than independent timers guessing the same moment. Asset production and runtime integration remain separate:

```text
editable/generated source
-> deterministic production package
-> Godot import
-> runtime gameplay/presentation
```

## Dependency rule

Only evaluate an addon/tool when the current project/native approach is demonstrably cumbersome. Before adoption, verify current compatibility, maintenance, license, overlap, source-of-truth impact and removal cost. Do not keep a static runtime plugin catalog.

## Completion bar

Check the relevant subset before saying done:

- project conventions and actual Godot version respected;
- one clear owner per gameplay/presentation fact;
- affected runtime/visual/input/save/export flow has matching evidence, or the unverified boundary is explicit;
- assets/derived outputs rebuild from their intended source;
- no unrelated dependency, 3D system or architecture was introduced.
