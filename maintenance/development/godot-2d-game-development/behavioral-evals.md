# Godot 2D behavioral evals

Maintenance-only. Verify the Agent chooses the **smallest useful 2D reference set**, preserves 2D ownership and hands dimension-neutral concerns to `development/godot-project-systems`.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| godot2d-001 | “8 向移动” | `movement-physics.md` | none | loading camera/shared refs without need |
| godot2d-002 | “8 向移动 + 顺滑 Camera2D” | `movement-physics.md` | `camera.md` | one giant movement/camera owner |
| godot2d-003 | “dash 在 attack recovery 后吞输入” | `movement-physics.md` | shared input only if the binding/buffer layer is actually involved | installing an input addon first |
| godot2d-004 | “一刀有时重复结算” | `combat-system.md` | none | tuning feel/VFX first |
| godot2d-005 | “攻击 active frame 和 contact window 不一致” | `combat-system.md` | `animation-runtime.md` | independent timers guessing timing |
| godot2d-006 | “机制正确，但反馈很软” | `game-feel.md` | optional `rendering-vfx-shaders.md` | rewriting interaction architecture |
| godot2d-007 | “大量 hit particles FPS 掉” | `performance.md` | rendering/VFX after profiling | optimization before evidence |
| godot2d-008 | “生成 6 帧 attack strip” | `development/sprite-animation-pipeline` | none | full Godot runtime for asset generation alone |
| godot2d-009 | “生成 strip 并导入 Godot 配置 runtime timing” | `asset-pipeline.md` | `animation-runtime.md` + sprite pipeline as needed | duplicating geometry/timing truth |
| godot2d-010 | “只调 Camera2D look-ahead/bounds” | `camera.md` | none | loading movement physics by default |
| godot2d-011 | “敌人 idle/chase/attack” | `ai-navigation.md` | none | installing a behavior framework by default |
| godot2d-012 | “seeded dungeon 要保证 start/goal 可达” | `procedural-generation.md` | optional `world-tilemap-level-design.md` | mixing enemy AI/perception logic |
| godot2d-013 | “原生 terrain 已经够用” | `world-tilemap-level-design.md` | none | migrating to third-party terrain tooling |
| godot2d-014 | “按键重映射、菜单 focus、存档迁移、GitHub Actions export” | `development/godot-project-systems` | none | keeping those systems inside the 2D Skill |
| godot2d-015 | “Godot 3D 第三人称” | `development/godot-3d-game-development` | none | forcing 2D references |
| godot2d-016 | “Godot 2D rollback netcode” | `development/godot-2d-game-development` | networking architecture elsewhere | pretending current refs cover netcode |

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
