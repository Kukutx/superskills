# AI, Navigation and Procedural Generation Reference

用于 2D enemy AI、state decisions、NavigationAgent2D、steering/perception、wave/spawn logic 与 seeded procedural content。

## 1. Start from behavior, not framework

先写玩家能观察到的行为：

```text
idle/patrol
-> notice
-> chase
-> attack
-> recover/search
-> return
```

再决定需要的是 simple state、navigation、steering 还是 behavior tree。不要关键词一出现就装 BT/GOAP addon。

## 2. Ownership

```text
AI decision -> intent/state
movement -> actual CharacterBody2D motion
combat -> attack/damage truth
animation/VFX -> presentation
```

不要把 AnimationPlayer 当 enemy AI truth。

## 3. Perception

明确：

- detection range；
- line of sight；
- hearing/noise if used；
- reaction delay；
- target memory；
- lose-target rule；
- fairness/cheating policy。

Area2D 适合 broad detection；ray/query 适合 LoS。

## 4. NavigationAgent2D

使用前确认：

- navigation data 存在并 ready；
- target reachable；
- agent radius/avoidance settings；
- dynamic map update timing；
- path target 与 actual physics movement 分离。

NavigationAgent2D 给 path/steering data；CharacterBody2D controller 仍负责实际移动。

## 5. Steering / crowd

只有需要时加入：

- local avoidance；
- separation；
- ranged spacing；
- surround slots；
- corridor handling。

简单追逐不需要 flocking system。

## 6. State hysteresis

避免 range threshold 抖动：

```text
enter attack <= 48
leave attack >= 60
```

或用 cooldown/explicit transition gate。

## 7. Decision frequency

AI 不需要所有 expensive decision 每 physics frame 执行。

常见优化：

- sensing lower frequency；
- stagger updates；
- path only when target/path meaningfully changes；
- cache stable data；
- cheap movement every physics tick, expensive decision less often。

先 profile，再优化。

## 8. Behavior-complexity ladder

优先选择能清楚表达当前行为的最小模型：

### Level 1 — handwritten state

适合：

```text
idle -> chase -> attack
patrol -> alert -> return
```

最透明、最少依赖。

### Level 2 — Beehave

当行为开始出现可复用 condition/action/subtree，但仍主要是 Behavior Tree 问题时，可考虑 `bitbrain/beehave`。

适合：

- Godot-native scene/tree authoring；
- reusable BT nodes；
- visual/debug workflow；
- 中等复杂 enemy behavior。

### Level 3 — LimboAI

当项目同时真正需要：

- larger behavior-tree library；
- hierarchical state machines；
- blackboard；
- richer debugger/tooling；

再考虑 LimboAI。

### Parallel/hierarchical gameplay state — Godot State Charts

如果难点不是“AI behavior tree”，而是 gameplay state 本身出现 hierarchical + parallel/orthogonal state explosion，可考虑 State Charts。

### Rule

已有项目使用其中一个就沿用。不要 Beehave + LimboAI + State Charts 一起上。

## 9. Attack handoff

AI state 只请求：

```text
want_attack(target)
```

Combat 系统判断 cooldown/range/state 是否允许并执行真正 attack。这样 AI 不直接修改目标 HP。

## 10. Offscreen behavior

从 gameplay fairness 先决定：

- offscreen enemy 是否继续移动；
- 能否 offscreen attack；
- spawning distance；
- 是否简化 sensing/update。

优化 offscreen simulation 前先定义玩法规则。

## 11. Spawn / waves

显式：

- budget；
- max active；
- spawn regions；
- no-spawn-near-player；
- pacing；
- elite/boss rules；
- cleanup/despawn。

不要每帧随机 spawn。

## 12. Procedural generation

Debug/存档需要复现时使用 seed。

推荐：

```text
seed
-> abstract layout/data
-> validate rules/connectivity
-> materialize TileMap/scenes
-> spawn gameplay content
```

不要直接把随机 tiles 画到最终 scene 后才检查可达性。

## 13. Connectivity / validity

至少检查：

- start -> goal reachable；
- mandatory rooms reachable；
- critical reward not isolated；
- spawn not inside collision；
- navigation matches generated layout；
- generated encounter respects gameplay budget。

## 14. Debug visibility

开发时可显示：

- current AI state/BT node；
- target；
- detection/attack ranges；
- LoS ray；
- nav target/path；
- cooldown；
- procedural seed。

Debug overlay 要易于关闭，不变成 production HUD dependency。

## Validation

测试：

- player just inside/outside detection；
- wall blocks LoS；
- target unreachable；
- target escapes；
- many enemies；
- dead/stunned enemy；
- pause/time-scale；
- nav map changes；
- scene reload；
- deterministic generation with same seed；
- different seed still passes connectivity rules。

## Source synthesis

结合 Godot NavigationAgent2D/native state patterns、GodotPrompter/GD-Agentic-Skills AI guidance、`bitbrain/beehave`、LimboAI 和 Godot State Charts 的适用边界。原则是先选择最小可理解模型，再按真实复杂度升级。