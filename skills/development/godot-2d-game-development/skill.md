---
name: godot-2d-game-development
description: Godot 4.x 2D-specific runtime and production guidance for CharacterBody2D physics, Camera2D, TileMapLayer/worlds, runtime animation, gameplay interaction, game feel, 2D VFX, AI/navigation, procedural content, 2D assets and measured performance.
---

# Godot 2D Game Development

## Scope

Use for Godot 4.x work where **2D semantics materially change implementation**: CharacterBody2D physics, Camera2D, TileMapLayer/world layout, 2D runtime animation/interaction/VFX/navigation, procedural 2D worlds and 2D asset handoff.

Use `development/godot-project-systems` for dimension-neutral Godot architecture, InputMap/remapping, Control UI, audio, save/inventory/dialogue, verification and export/CI.

Use `development/godot-3d-game-development` for materially 3D/spatial work.

## Core rules

1. Inspect the real project first: exact Godot version, `project.godot`, language, scene tree, collision setup, renderer/import settings and existing conventions.
2. Gameplay/state systems own facts; animation/VFX/camera present them.
3. Load one primary 2D reference first, then only focused neighbors required by the subproblem.
4. Do not recreate shared input/UI/save/export architecture inside a 2D reference.
5. Prefer existing/native patterns before dependencies.
6. Match completion claims to actual runtime/visual evidence; use the shared verification guidance when needed.

## Runtime references

| Need | Reference |
| --- | --- |
| CharacterBody2D, movement, jump/dash, collisions, knockback | `references/movement-physics.md` |
| Camera2D follow, bounds, look-ahead, pixel camera | `references/camera.md` |
| TileMapLayer, terrain/world layout, y-sort, collision/navigation, level authoring | `references/world-tilemap-level-design.md` |
| AnimationPlayer/Tree, SpriteFrames, Tween, runtime timing/events | `references/animation-runtime.md` |
| hitbox/hurtbox, attack resolution, repeated-contact policy, combo/cancel | `references/combat-system.md` |
| hit-stop, shake, flash, recoil, squash, impact feedback | `references/game-feel.md` |
| particles, CanvasItem shaders, 2D lighting/effects | `references/rendering-vfx-shaders.md` |
| enemy behavior, perception, state complexity, NavigationAgent2D | `references/ai-navigation.md` |
| seeded generation, waves/spawn rules, generated-layout validity | `references/procedural-generation.md` |
| editable 2D asset source, import, FX/map/tiles handoff | `references/asset-pipeline.md` |
| profiler, frame-time, memory and measured 2D optimization | `references/performance.md` |
| architecture/input/UI/audio/save/inventory/dialogue/verification/export | `../godot-project-systems/skill.md` |
| sprite-strip generation, exact frame geometry, slicing, timing metadata, naming/packing | `../sprite-animation-pipeline/skill.md` |

## Routing examples

- CharacterBody2D movement/collision -> `movement-physics.md`
- Camera2D framing/bounds -> `camera.md`
- runtime animation timing -> `animation-runtime.md`
- gameplay contact/interaction correctness -> `combat-system.md`
- feel/feedback after correctness is established -> `game-feel.md`
- generate/slice/package a sprite strip -> `../sprite-animation-pipeline/skill.md`
- remapping/menu focus/save migration/export CI -> `../godot-project-systems/skill.md`

## Ownership

Use the shared project-systems Skill for dimension-neutral state/data ownership. For 2D-specific physical/presentation behavior, keep movement, interaction rules and presentation synchronized through explicit state/events rather than multiple systems independently writing the same fact.

Asset production and runtime integration remain separate:

```text
editable/generated source
-> deterministic production package
-> Godot import
-> runtime integration
```

## Dependency rule

Evaluate an addon/tool only when the current project/native approach has demonstrated recurring pain. Re-check compatibility, maintenance, license, overlap and removal cost before adoption.

## Completion bar

Confirm the relevant subset:

- project conventions and exact Godot version were respected;
- the affected 2D runtime/visual flow has matching evidence or an explicit unverified boundary;
- assets/derived outputs rebuild from their intended source;
- dimension-neutral concerns use the shared owner rather than duplicated 2D rules;
- no unrelated dependency or 3D system was introduced.
