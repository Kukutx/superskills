# AI, Navigation and Procedural Generation Reference

用于 2D enemy AI、FSM、NavigationAgent2D、steering/perception、wave/spawn logic 和 seeded procedural content。

## 1. Start from behavior, not algorithm

先定义 enemy 行为：

```text
idle/patrol
-> notice
-> chase
-> attack
-> recover/search
-> return
```

再决定需要：

- simple state logic；
- ray/area perception；
- NavigationAgent2D；
- steering；
- behavior tree-like structure。

不要默认上复杂 BT/GOAP。

## 2. State ownership

AI state owner 决定 intent。
Movement system 执行移动。
Combat system 执行 attack。
Animation/VFX 只表现。

不要把 `AnimationPlayer` 当敌人 AI state machine。

## 3. Perception

明确：

- vision range；
- line of sight；
- hearing/noise；
- aggro memory；
- lose-target condition；
- reaction delay。

Area2D 可做 broad detection。
精确 LoS 用 ray/query。

不要让敌人“既假装看不见又直接读取 player global position”除非设计就是作弊型 director。

## 4. NavigationAgent2D

使用前确认：

- navigation data 已生成；
- target reachable；
- agent radius/avoidance；
- map change 后 nav update；
- collision/navigation 区别。

Navigation path 给目标方向；actual body movement 仍遵循 CharacterBody2D controller。

## 5. Steering and local avoidance

简单追逐不需要复杂 flocking。
在以下情况加入 avoidance/steering：

- crowd；
- corridor；
- ranged spacing；
- surround behavior。

避免所有 enemy 堆到同一点。

## 6. Attack range and hysteresis

不要用一个 threshold 造成状态抖动。

例如：

```text
enter attack at <= 48
leave attack at >= 60
```

或使用明确 cooldown/state gate。

## 7. Offscreen AI

先从 gameplay fairness 出发：

- 是否允许 offscreen movement；
- 是否允许 offscreen attack；
- spawning distance；
- simulation simplification。

性能确实需要时再减少 offscreen update frequency / suspend expensive sensing。

## 8. Wave/spawn system

定义：

- spawn budget；
- max active；
- spawn region；
- no-spawn-on-player；
- pacing；
- elite/boss rule；
- cleanup。

不要每帧随机 spawn。

## 9. Procedural generation

必须 seeded/reproducible when debugging matters。

保存 seed 可复现：

- dungeon；
- loot；
- level layout；
- encounter。

Random generation 仍需规则验证，不是“随机就有 replayability”。

## 10. Generation pipeline

推荐：

```text
seed
-> abstract layout/data
-> validate connectivity/rules
-> materialize TileMap/scenes
-> spawn gameplay objects
```

不要直接在画面上随机画完才发现地图不可达。

## 11. Connectivity validation

Dungeon/map 至少检查：

- start -> goal reachable；
- mandatory rooms reachable；
- no isolated critical reward；
- spawn not inside collision；
- nav matches layout。

## 12. AI debug tools

开发时可显示：

- current state；
- target；
- path；
- detection range；
- attack range；
- ray/LoS；
- nav target；
- cooldown。

Debug visual 必须容易关闭，不进入生产 UI。

## 13. Performance

AI 常见成本：

- 每敌人每帧 path request；
- 高频 raycasts；
- large overlap scan；
- expensive decision every frame；
- crowd avoidance。

优化优先：

- lower decision frequency；
- stagger updates；
- cache stable data；
- request path only when target/path meaningfully changes；
- spatial limits。

先 profile。

## 14. When a plugin is justified

Default to project-native state logic first.

Consider an external AI/state plugin only when the problem is genuinely complex:

- **LimboAI**: useful for reusable Behavior Trees + hierarchical state machines, visual debugging, blackboards, and larger enemy behavior sets.
- **Godot State Charts**: useful when orthogonal/hierarchical states, guarded transitions, delayed transitions, or state explosion make a hand-written FSM hard to reason about.

Do not install either just to implement `idle -> chase -> attack`.
If the project already uses one, follow its model instead of creating a competing state framework.

## 15. AI QA

测试：

- target on/off edge；
- wall between player/enemy；
- target unreachable；
- player escapes；
- many enemies；
- pause/time-scale；
- scene reload；
- spawn near bounds；
- nav map change；
- dead enemy stops AI。

## Source synthesis

主要吸收 GD-Agentic-Skills navigation/state/procedural patterns、GodotPrompter `ai-navigation`/`procedural-generation`，以及 awesome-gamedev-agent-skills `game-ai`/`procedural-gen`。
