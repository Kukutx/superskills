# Godot 2D behavioral evals

Maintenance-only. Verify the Agent chooses the **smallest useful reference set**, preserves ownership and avoids dependency/tool overreach.

## Routing matrix

| Prompt | Expected route | Must avoid |
| --- | --- | --- |
| “8 向移动” | `movement-physics.md` | loading camera/input refs without need |
| “8 向移动 + 顺滑 Camera2D” | `movement-physics.md` + `camera.md` | one giant movement/camera owner |
| “键鼠切手柄自动换提示并允许重映射” | `input-controls-accessibility.md` + optional `ui-ux.md` | rewriting movement controller |
| “dash 在 attack recovery 后吞输入” | input + movement/state as needed | installing an input addon first |
| “一刀有时扣三次血” | `combat-system.md` | tuning shake/VFX first |
| “攻击 active frame 和 hitbox 不一致” | `combat-system.md` + `animation-runtime.md` | independent timers guessing timing |
| “伤害正确，但打击感很软” | `game-feel.md` + optional audio/VFX | rewriting damage architecture |
| “大量 hit particles FPS 掉” | `performance.md` + rendering/VFX after profiling | optimization before evidence |
| “生成 6 帧 attack strip” | `development/sprite-animation-pipeline` | full Godot runtime for asset generation alone |
| “生成 strip 并导入 Godot 配置 runtime timing” | sprite pipeline + `asset-pipeline.md` + `animation-runtime.md` as needed | duplicating geometry/timing truth |
| “authored source 已有 tags/durations” | `asset-pipeline.md` + `animation-runtime.md` | flatten/rebuild metadata manually |
| “只调 Camera2D look-ahead/bounds” | `camera.md` | loading movement physics by default |
| “敌人 idle/chase/attack” | `ai-navigation.md` | installing a behavior framework by default |
| “seeded dungeon 要保证 start/goal 可达” | `procedural-generation.md` + optional world ref | mixing enemy AI/perception logic |
| “原生 terrain 已经够用” | `world-tilemap-level-design.md` | migrating to third-party terrain tooling |
| “旧存档升级后 item ID 全换了” | `save-persistence.md` | guessing by display name |
| “简单 stack/equip inventory” | `inventory-progression.md` | adding an inventory framework by default |
| “大量 branching + 多语言 dialogue” | `dialogue-localization.md` | putting story truth in UI callbacks |
| “Agent 改暂停菜单，验证手柄真的能操作” | `verification-testing.md` + `ui-ux.md` + optional input | static inspection only |
| “某场景 FPS 掉” | `performance.md` | optimization without profiler evidence |
| “GitHub Actions clean export” | `release-export-ci.md` | local cache dependence |
| “Godot 3D 第三人称” | outside this Skill | forcing 2D references |
| “Godot 2D rollback netcode” | Godot owns local gameplay only; networking architecture elsewhere | pretending current refs cover netcode |

## Pressure cases

### Correctness before feel

`一刀偶尔两次伤害，而且也没重量。` -> fix single-hit correctness first, then tune feel. Do not change damage, hit-stop, shake, audio and VFX simultaneously.

### Asset vs runtime ownership

Generated strip -> sprite pipeline owns generation/geometry/packaging. Godot asset/runtime references only join when import/runtime behavior is requested.

Authored editable source with tags/durations -> preserve source metadata; do not recreate a second timing truth manually.

### AI vs generation

`敌人追玩家，同时地图是 seeded dungeon。` -> `ai-navigation.md` owns enemy decisions; `procedural-generation.md` owns generated layout/seed validity; world ref joins only for materialization concerns.

### Save vs inventory

`背包 stack 正常，但 v2 存档迁移失败。` -> inventory logic stays untouched unless evidence points there; `save-persistence.md` owns migration.

### Dependency restraint

If native/current project patterns work, do not migrate merely because a more advanced addon exists. Evaluate third-party tooling only after recurring pain is demonstrated and current compatibility is re-verified.

### Runtime evidence

If live tooling exists, run the affected scene/flow and inspect visible behavior/errors. Otherwise state static vs runtime/visual verification boundaries.

## Regression rule

Before adding/splitting a reference, answer:

1. What decisions live there?
2. When should it load?
3. Which neighboring owner must not duplicate it?
4. Does the split reduce real runtime context or clarify ownership?
5. What eval case proves the boundary matters?

If the answer is unclear, keep the current structure.
