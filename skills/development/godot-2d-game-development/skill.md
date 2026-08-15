---
name: godot-2d-game-development
description: Godot 4.x 2D/pixel-game production router. Use for architecture, movement/physics/camera, input, TileMapLayer worlds, animation, combat, game feel, VFX, UI, audio, AI, save/dialogue, assets, runtime validation, performance/testing and export. Load only the focused references needed.
---

# Godot 2D Game Development

## Scope

Use for Godot 4.x **2D-first** implementation and production workflows.

Route elsewhere when the main problem is:

- Godot 3D / 3D rendering;
- multiplayer/network protocol/server architecture;
- generic backend/frontend unrelated to Godot;
- pure game design/writing with no implementation concern.

If a mixed task contains Godot 2D work, this Skill owns only that part.

## Core invariants

1. **Inspect the real project first**: `project.godot`, Godot version, GDScript/C#, scene tree, autoloads, Resources, signals, InputMap, collision layers, addons and existing conventions.
2. **Gameplay truth before presentation**: physics/combat/data/state own gameplay facts; animation/VFX/audio/camera/UI react to them.
3. **One primary reference first**: normally load 1–3 references total, not every keyword match.
4. **Native/existing before new dependency**: reuse project patterns; add addons only for demonstrated complexity.
5. **Evidence before completion claims**: parse/build success is not proof of runtime, visual, input, save or export correctness.

## Routing precedence

When a request spans layers, locate the actual failure first:

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
- attack pose and active window disagree -> `combat-system.md` + `animation-pixel.md`
- gamepad cannot navigate pause menu -> `ui-ux.md` + input reference if needed
- particles cause frame drops -> profile first, then rendering/VFX

## Runtime references

| Need | Reference |
| --- | --- |
| ownership, scenes, Resources, signals, state/FSM | `references/core-architecture.md` |
| CharacterBody2D, movement, physics, jump/dash, Camera2D | `references/movement-physics-camera.md` |
| InputMap, keyboard/gamepad/touch, remap, device switching, accessibility | `references/input-controls-accessibility.md` |
| TileMapLayer, terrain/world layout, y-sort, collision, level design | `references/world-tilemap-level-design.md` |
| AnimatedSprite2D, AnimationPlayer/Tree, pixel timing | `references/animation-pixel.md` |
| hitbox/hurtbox, damage, i-frame, combo/cancel | `references/combat-system.md` |
| hit-stop, shake, flash, recoil, squash, impact feedback | `references/game-feel.md` |
| particles, CanvasItem shaders, 2D lighting/effects | `references/rendering-vfx-shaders.md` |
| HUD/menu, Control/Container/Theme, focus, safe area | `references/ui-ux.md` |
| SFX/music, buses, variation, ducking, positional audio | `references/audio.md` |
| enemy AI, NavigationAgent2D, behavior complexity, procedural generation | `references/ai-navigation-procedural.md` |
| inventory, stable IDs, save/load, migration, progression/settings | `references/save-inventory-progression.md` |
| branching dialogue, conditions/effects, localization | `references/dialogue-localization.md` |
| sprite/FX/map/tiles/UI production and Godot handoff | `references/asset-pipeline.md` |
| profiler, runtime debugging, automated tests | `references/performance-testing-debugging.md` |
| inspect -> edit -> run -> input/screenshot/errors -> verify | `references/runtime-agent-validation.md` |
| export presets, clean CI, toolchain pinning, artifacts | `references/release-export-ci.md` |
| optional MCP/addons/importers/templates | `references/companion-tools.md` |
| exact spritesheet geometry/slicing/naming | `../game-dev-spritesheet-slicer/skill.md` |

Maintenance-only material lives in `maintenance/` and should not be loaded for normal game tasks.

## Implementation workflow

### 1. Define the player-visible result

Prefer observable statements:

```text
press attack -> startup -> active hit -> enemy reacts -> recovery
```

not manager/class names.

### 2. Establish ownership

Typical direction:

```text
physical input -> action intent
state/controller -> action allowed + gameplay state
physics/combat/data -> result
explicit event -> animation/UI/audio/VFX/camera
save system -> persistent representation
```

Avoid two systems writing the same truth.

### 3. Synchronize from one authority

When timing must match, share an explicit event/timeline rather than independent timers guessing the same moment. Animation can author visual timing; combat/state still owns whether damage/action is valid.

### 4. Polish after correctness

Add feedback proportionally. Do not use strong hit-stop/shake/VFX to hide bad combat timing or unreadable telegraphs.

### 5. Validate the claim

Prefer the smallest executable surface:

```text
inspect
-> change
-> run affected scene/flow
-> reproduce exact behavior
-> inspect output/errors + visible result
-> fix/repeat
```

Without live tooling, clearly state what is static vs actually runtime-verified.

## Dependency rule

Consider an addon/tool only when:

- native/current project solution is demonstrably cumbersome;
- it supports the project's exact Godot version/language;
- it solves a named problem rather than adding architecture prestige;
- overlap with existing addons is understood;
- source-of-truth, upgrade and removal costs are acceptable;
- the user/project allows a new dependency.

`companion-tools.md` is a candidate index, not an install list.

## Output

For implementation/debug tasks, default to:

1. **结论 / 问题**
2. **修改位置**
3. **具体修改**
4. **原因**
5. **最小验证**

If the user asks for direct implementation, implement first rather than producing a long design document.

## Completion bar

Before saying done, check the relevant subset:

- existing project conventions preserved;
- API matches actual Godot version;
- gameplay truth and presentation ownership are clear;
- input responsiveness remains correct;
- assets/imports rebuild from source;
- runtime/visual behavior has evidence or an explicit unverified boundary;
- no unrelated 3D, dependency or architecture was added.
