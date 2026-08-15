# Godot 2D routing regression tests

Maintenance-only. Goal: verify the Agent selects the **smallest useful reference set** and avoids dependency/tool overreach.

## Pass criteria

- correct domain route;
- normally 1–3 references;
- correctness before polish;
- gameplay truth ownership remains clear;
- no automatic addon/MCP/test-framework installation;
- version-sensitive behavior uses the actual project version;
- source/generated ownership is explicit;
- completion claim has matching evidence.

## Routing matrix

| Prompt | Expected route | Must avoid |
| --- | --- | --- |
| “8 向移动 + 顺滑 Camera2D” | `movement-physics-camera` | loading input/combat refs without need |
| “键鼠切手柄自动换提示并允许重映射” | `input-controls-accessibility` + optional `ui-ux` | rewriting movement controller |
| “dash 在 attack recovery 后吞输入” | input + movement/state as needed | installing an input addon first |
| “一刀有时扣三次血” | `combat-system` | tuning shake/VFX first |
| “攻击动画 active frame 和 hitbox 不一致” | `combat-system` + `animation-pixel` | independent timers guessing timing |
| “伤害正确，但打击感很软” | `game-feel` + optional audio/VFX | rewriting damage architecture |
| “大量 hit particles FPS 掉” | `performance` + rendering/VFX after profiling | ECS/MultiMesh before measurement |
| “AI 生成 6 帧 attack strip 并导入 Godot” | `asset-pipeline` + slicer + animation as needed | rebuilding each frame independently |
| “authored animation 已有 tags/timing” | `asset-pipeline` + animation | flattening metadata and recreating manually |
| “原生 terrain 已经够用” | `world-tilemap-level-design` | migrating to third-party terrain tooling |
| “外部 level editor 是团队唯一编辑源” | world reference | editing generated Godot map as second truth |
| “敌人 idle/chase/attack” | `ai-navigation-procedural` | installing a behavior framework by default |
| “很多行为 subtree/state 开始重复” | AI reference, then evaluate complexity | jumping to the heaviest framework |
| “简单 stack/equip inventory” | `save-inventory-progression` | adding an inventory framework by default |
| “旧存档升级后 item ID 全换了” | save reference | guessing by display name |
| “大量 branching + 多语言 dialogue” | `dialogue-localization` | putting story truth in UI callbacks |
| “Agent 改暂停菜单，验证手柄真的能操作” | `verification-testing` + `ui-ux` + optional input | static code inspection only |
| “某场景 FPS 掉，找瓶颈” | `performance` | optimization without profiler evidence |
| “GitHub Actions clean export” | `release-export-ci` | unpinned latest / local cache dependence |
| “只切 64x64 spritesheet” | spritesheet slicer | loading full Godot domain |
| “Godot 3D 第三人称” | route outside this Skill | forcing 2D references |
| “Godot 2D rollback netcode” | Godot owns 2D gameplay only; networking architecture elsewhere | pretending existing refs cover netcode |

## Pressure tests

### Existing-project respect

Prompt: `项目已有简单 enum FSM，可以跑。只加 dash。`

Pass: keep the enum FSM; use movement/input only; no new state framework; validate cooldown/collision/state exit.

### Correctness before feel

Prompt: `一刀偶尔两次伤害，而且也没重量。`

Pass: fix and reproduce single-hit correctness first; only then tune feel. Do not change damage, hit-stop, shake, audio and VFX simultaneously.

### Authored vs generated assets

A. Editable source already contains tags/durations -> preserve metadata and source ownership.

B. Generated transparent strip -> deterministic normalize/slice/anchor/preview; do not require an authored-source importer.

### Level source ownership

Prompt: `美术在外部 editor 改地图，程序也在 Godot 里改生成的 TileMap。`

Pass: identify double-truth risk; choose editable source; generated representation is regenerated or has an explicit patch boundary.

### Dependency restraint

Prompt: `原生方案能用，但网上有一个更高级的 addon。`

Pass: no migration unless there is demonstrated recurring pain; re-verify current compatibility/maintenance only if evaluation becomes necessary.

### Save migration

Prompt: `v3 把 item id 全换了，v2 存档继续能开。`

Pass: explicit ID mapping + versioned migration + old fixture; failure must not silently erase save.

### Runtime evidence

Prompt: `我改了 HUD，确认修好了吧？`

Pass: if live tooling exists, run the affected flow and inspect visible result/errors; otherwise state static vs unverified runtime/visual boundaries.

### Performance evidence

Prompt: `感觉 node 太多，改成对象池和 MultiMesh 吧。`

Pass: profile first; identify actual bottleneck; only introduce complexity if measurements justify it.

### Clean CI

Prompt: `本地 export 正常，CI 说资源不存在。`

Pass: compare exact Godot/templates, source assets/LFS/submodules, case-sensitive paths, clean import and export preset before reinstalling everything.

## Distribution tests

### Domain precedence

Prompt: `Godot 2D 攻击重复扣血，帮我 debug。`

Pass: `godot-2d-game-development` primary -> `combat-system`; generic bug skill does not replace domain routing.

### Router is the single catalog

Pass:

- `skills/meta/skill-router/skill.md` is the only maintained full Skill catalog;
- Project Instructions point to the Router instead of duplicating its table;
- no `knowledge-pack.md` or parallel routing manifest is required.

### Runtime knowledge hygiene

Pass:

- `maintenance/` is not normal runtime context;
- source/tool inventories do not live under `references/`;
- no compatibility stubs are preserved merely for old names;
- routing does not depend on loading every file.

## Regression rule

Before adding a reference/source/dependency rule, answer:

1. What specific decision is currently missing?
2. Why can the existing reference not own it?
3. Does it create routing overlap/context bloat?
4. Is it runtime knowledge or maintenance-only information?
5. What regression prompt proves the new boundary matters?

If the answer is unclear, do not add it.
