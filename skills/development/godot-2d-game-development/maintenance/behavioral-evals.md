# Godot 2D behavioral evals

Maintenance-only. Verify the Agent chooses the **smallest useful 2D reference set**, preserves 2D ownership and hands dimension-neutral concerns to `development/godot-project-systems`.

## Routing matrix

| Prompt | Expected route | Must avoid |
| --- | --- | --- |
| “8 向移动” | `movement-physics.md` | loading camera/shared refs without need |
| “8 向移动 + 顺滑 Camera2D” | `movement-physics.md` + `camera.md` | one giant movement/camera owner |
| “dash 在 attack recovery 后吞输入” | 2D movement/state + shared input only if the binding/buffer layer is actually involved | installing an input addon first |
| “一刀有时重复结算” | `combat-system.md` | tuning feel/VFX first |
| “攻击 active frame 和 contact window 不一致” | `combat-system.md` + `animation-runtime.md` | independent timers guessing timing |
| “机制正确，但反馈很软” | `game-feel.md` + optional 2D VFX | rewriting interaction architecture |
| “大量 hit particles FPS 掉” | `performance.md` + rendering/VFX after profiling | optimization before evidence |
| “生成 6 帧 attack strip” | `development/sprite-animation-pipeline` | full Godot runtime for asset generation alone |
| “生成 strip 并导入 Godot 配置 runtime timing” | sprite pipeline + `asset-pipeline.md` + `animation-runtime.md` as needed | duplicating geometry/timing truth |
| “只调 Camera2D look-ahead/bounds” | `camera.md` | loading movement physics by default |
| “敌人 idle/chase/attack” | `ai-navigation.md` | installing a behavior framework by default |
| “seeded dungeon 要保证 start/goal 可达” | `procedural-generation.md` + optional world ref | mixing enemy AI/perception logic |
| “原生 terrain 已经够用” | `world-tilemap-level-design.md` | migrating to third-party terrain tooling |
| “按键重映射、菜单 focus、存档迁移、GitHub Actions export” | `development/godot-project-systems` | keeping those systems inside the 2D Skill |
| “Godot 3D 第三人称” | `development/godot-3d-game-development` | forcing 2D references |
| “Godot 2D rollback netcode” | 2D owns local runtime only; networking architecture elsewhere | pretending current refs cover netcode |

## Pressure cases

### Correctness before feel

If a gameplay result is wrong and the feedback also feels weak, fix correctness first, then tune presentation. Do not change interaction logic, shake, audio and VFX simultaneously.

### Asset vs runtime ownership

Generated strip -> sprite pipeline owns generation/geometry/packaging. Godot 2D asset/runtime references join only for import/runtime behavior.

### AI vs generation

`敌人追玩家，同时地图是 seeded dungeon。` -> `ai-navigation.md` owns enemy decisions; `procedural-generation.md` owns generated layout/seed validity.

### Shared systems boundary

`Godot 2D 的 pause menu gamepad focus 断了。` -> shared project-systems owns UI/input. Do not load movement/Camera2D because the project happens to be 2D.

### Runtime evidence

If live tooling exists, run the affected scene/flow and inspect behavior/errors. Otherwise state static vs runtime/visual verification boundaries using the shared verification owner.

## Regression rule

Before adding/splitting a 2D reference, answer:

1. Does 2D materially change the implementation?
2. What decisions live there?
3. When should it load?
4. Which neighboring owner must not duplicate it?
5. What eval case proves the boundary matters?

If the answer is unclear or the behavior applies equally to 3D, keep/use the shared project-systems owner instead.
