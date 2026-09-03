# Sprite Animation Pipeline behavioral evals

Maintenance-only. Protect the boundary between **generation**, **deterministic packaging**, and **engine runtime integration**.

## Routing cases

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| sprite-001 | “用这个角色 seed 做 6 帧 attack strip” | `generation.md` | none | loading packaging/runtime details before geometry exists |
| sprite-002 | “已有 64x64 sheet，只切成 attack_00..05” | `packaging.md` | none | regenerating the artwork |
| sprite-003 | “生成 8 向 run，再按稳定 anchor 导出” | `generation.md` | `packaging.md` | one giant uncontrolled all-action sheet |
| sprite-004 | “Aseprite 已有 tags/durations，导出到引擎” | `packaging.md` | none | rebuilding timing by hand as second truth |
| sprite-005 | “只改 Godot AnimationTree，不改 sprite source” | matching Godot runtime animation owner | none | changing asset geometry unnecessarily |
| sprite-006 | “attack frame 看起来对，但一刀扣两次血” | gameplay/combat owner | none | treating art timing as damage truth |

## Pressure cases

### Generated frames drift

Prompt: `六帧 attack 每帧角色大小和脚底位置都在漂。`

Pass: fix shared scale/anchor and generation consistency first; do not hide the defect with engine-side per-frame offsets.

### Unknown sheet geometry

Prompt: `这张 sheet 有几个空格，我不确定哪些是有效帧，直接帮我切。`

Pass: inspect/resolve the real geometry or metadata; do not invent missing ranges from blank/duplicate cells.

### Source metadata ownership

Prompt: `源 .aseprite 已经有 animation tags 和 durations，但 Godot 里也手工维护了一套。`

Pass: identify double-truth risk; keep one authoritative timing source and deterministically hand it off where practical.

### Art timing vs gameplay truth

Prompt: `把 active frame 改了，所以 damage 应该自动跟着变吧？`

Pass: the asset/runtime timeline may expose the event moment, but combat/state remains responsible for whether damage is valid and how often it applies.

### Minimal context

Prompt: `已有完整 strip，只需要重新命名和打包。`

Pass: load packaging only. Generation guidance adds no value.

## Regression rule

Add a new case only when it protects a real ownership or production failure. Do not turn this file into an example library.
