# Core Architecture Reference

用于 scene ownership、signals、Resources、state、autoload、composition 与项目结构。

## 1. Start from ownership

先回答：谁拥有这个事实？

```text
Player/controller -> input intent + movement request
Character state -> can/cannot act
Health -> HP/i-frame/death truth
Combat -> hit/damage resolution
Animation -> visual timeline
UI -> display only
Save -> persistent representation
```

一个状态尽量只有一个权威 owner。

## 2. Scene composition

Godot 适合通过 scene/node composition 拆职责，但不要把每一行逻辑都拆成 node。

适合独立 component 的例子：

- HealthComponent
- Hitbox/Hurtbox
- InteractionArea
- StateMachine when behavior complexity justifies it
- Audio/VFX controller when reused

不适合：只被一个 parent 调一次、没有独立状态/生命周期的 trivial wrapper。

## 3. Direct call vs signal

Use direct call when:

- owner 明确知道 target；
- relationship 是稳定的一对一；
- synchronous result 有意义。

Use signal/event when:

- one event has multiple listeners；
- emitter 不应知道 listeners；
- UI/audio/VFX react to gameplay；
- scene replacement/lifecycle needs decoupling。

不要把所有函数调用都换成 global event bus。

## 4. Autoload

Autoload 只放真正跨场景、全局生命周期清楚的内容，例如：

- settings/profile service；
- save coordinator；
- scene transition coordinator；
- global audio service when project needs it。

不要把 Player、Combat、Inventory、UI 都因为“方便访问”塞进 autoload。

## 5. Resources

Resource 适合定义数据：

- items；
- attacks/abilities；
- character stats templates；
- loot tables；
- enemy archetypes；
- dialogue/quest data。

注意 Resource 默认可共享。运行时要修改实例数据时：

- 明确 duplicate/local-to-scene strategy；
- 不要意外让多个 enemy 共用一份 mutable HP/stats。

## 6. State machines

简单状态不需要 framework。

可以从 enum + match/explicit methods 开始：

```text
IDLE
MOVE
ATTACK
HURT
DEAD
```

当出现以下问题再升级：

- transitions scattered everywhere；
- nested/parallel behavior；
- reusable states；
- state-specific enter/exit lifecycle；
- many bools encode impossible combinations。

FSM 管 gameplay intent；AnimationTree/animation names 不应成为唯一 gameplay state truth。

## 7. Dependency direction

Prefer:

```text
data/config
-> gameplay systems
-> events
-> presentation/UI
```

Avoid:

```text
HUD -> mutate player internals
particles -> decide damage
animation name -> decide inventory/save state
```

## 8. Node references

沿用项目 convention：

- `@onready` cache stable child references；
- exported NodePath/typed node reference when designer wiring is useful；
- group lookup only where relationship is genuinely group-based。

不要在 hot loop 每帧 `get_node()`/tree search 找稳定对象。

## 9. GDScript clarity

Prefer:

- typed variables/functions where useful；
- `StringName` for repeated action/state/signal identifiers where project already uses it；
- small functions with one responsibility；
- explicit names over generic `Manager`/`Helper`。

不要为了类型系统把简单 Godot code 写成 enterprise boilerplate。

## 10. Lifecycle

明确：

- `_ready()` wiring；
- signal connect/disconnect ownership；
- timers/tweens cleanup；
- node free/reuse；
- scene transition reset；
- autoload state reset between new game/load。

常见 ghost bug 来自旧 scene/global state 没清理，而不是算法错误。

## 11. Architecture escalation rule

只有下面至少一个成立才加抽象：

- 当前重复已经真实存在；
- 同一机制有多个消费者；
- 测试/维护被当前耦合阻塞；
- feature roadmap 已明确需要扩展；
- bug 来源就是 ownership 不清。

不要为“以后可能”建立五层抽象。

## 12. Minimum validation

架构改动后至少验证：

- scene loads；
- signals connect once；
- state transitions reach expected exit；
- shared Resource has no cross-instance mutation；
- scene reload/new game has no stale global state；
- presentation listeners missing时 gameplay 仍正确。
