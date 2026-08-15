# AI, Navigation and Procedural Generation Reference

用于 2D enemy AI、state decisions、NavigationAgent2D、steering/perception、wave/spawn logic 与 seeded procedural content。

## Start from behavior, not framework

先定义玩家能观察到的行为：

```text
idle/patrol
-> notice
-> chase
-> attack
-> recover/search
-> return
```

再决定 simple state、navigation、steering 或 behavior tree 是否真的需要。

## Ownership

```text
AI decision -> intent/state
movement -> actual CharacterBody2D motion
combat -> attack/damage truth
animation/VFX -> presentation
```

AI 不直接成为 movement、damage 或 animation truth。

## Perception

明确 detection range、LoS、reaction delay、target memory、lose-target rule 和 fairness policy。

Area2D 可做 broad detection；ray/query 可做 LoS。避免每帧执行所有昂贵 sensing。

## NavigationAgent2D

确认：

- navigation data ready;
- target reachable;
- radius/avoidance settings match level geometry;
- dynamic map update timing;
- path/steering data 与 CharacterBody2D 实际移动分离。

## State stability

避免 threshold 抖动，可使用 hysteresis、cooldown 或 explicit transition gate。

例如：

```text
enter attack <= 48
leave attack >= 60
```

## Complexity ladder

从最小可理解模型开始：

1. **handwritten state**：少量清楚状态和转换；
2. **reusable behavior tree/state abstraction**：condition/action/subtree 开始大量复用；
3. **hierarchical/parallel state model**：状态组合本身出现明显 explosion；
4. 更复杂 tooling 只有在当前模型已经成为维护瓶颈时才评估。

项目已有 state/AI framework 就沿用。不要同时引入多套高度重叠的状态系统。

需要第三方 framework 时，按主 Skill 的 dependency rule 重新验证当前版本、维护状态、license 和迁移成本；不要依赖静态工具名单。

## Decision frequency

昂贵 decision 不需要每 physics frame 执行：

- sensing lower frequency;
- stagger agent updates;
- path only when target/path meaningfully changes;
- cache stable data;
- cheap movement each physics tick, expensive reasoning less often.

先 profile，再优化。

## Attack handoff

AI 只表达 intent，例如：

```text
want_attack(target)
```

Combat 系统判断 cooldown/range/state 并执行实际 attack/damage。

## Spawn / waves

显式定义 budget、max active、spawn regions、no-spawn-near-player、pacing、elite/boss rules 和 cleanup。

不要每帧随机 spawn。

## Procedural generation

需要 debug/save 可复现时使用 seed：

```text
seed
-> abstract layout/data
-> validate connectivity/rules
-> materialize TileMap/scenes
-> spawn gameplay content
```

先验证结构，再生成最终场景。

至少检查：start/goal reachable、mandatory content reachable、spawn 不在 collision、navigation 匹配 layout、encounter 不超 budget。

## Debug visibility

开发时可显示 current state、target、ranges、LoS、nav path、cooldown 和 procedural seed；必须容易关闭，不变成 production dependency。

## Validation

覆盖：

- detection boundary / blocked LoS;
- unreachable or escaped target;
- many enemies;
- dead/stunned state;
- pause/time-scale;
- nav map changes;
- scene reload;
- same seed deterministic;
- different seeds still satisfy validity rules.
