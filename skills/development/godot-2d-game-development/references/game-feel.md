# Game Feel Reference

用于“机制能用，但不够有重量/反馈/爽感”的问题：hit-stop、camera shake、recoil、squash/stretch、flash、impact FX、damage popup、rumble、audio-visual layering。

如果 hit detection/damage 本身不可靠，先读 `combat-system.md`。

## 1. Principle: feedback reacts to truth

```text
confirmed gameplay event
-> feedback bundle
```

不要：

```text
particle appeared
-> therefore deal damage
```

Hit、land、dash、pickup、death、button confirm 都应有清楚 event hook。

## 2. Layer from small to large

一个有力 hit 通常不是靠单个超强特效，而是几个很短的反馈对齐：

```text
impact sound
+ contact flash/FX
+ gameplay knockback or visual recoil
+ optional short hit-stop
+ optional small camera shake
+ optional popup/rumble
```

先加 2–3 层，实际玩，再决定是否继续。

## 3. Importance tiers

保持全局相对尺度：

| Tier | Typical use |
| --- | --- |
| small | footstep, light pickup, tiny hit |
| medium | normal melee/projectile hit |
| heavy | charged hit, explosion, elite enemy |
| critical/boss | authored high-impact moment |

不要每次普通攻击都使用最大 shake + 最长 hit-stop。

## 4. Hit-stop

Hit-stop 只在**确认命中**时触发，且很短。

原则：

- once per meaningful impact；
- recovery timer 要能在 slowed/frozen time 下恢复；
- 不用 blocking sleep；
- 保存/恢复正确的 time-scale ownership，避免多个系统互相覆盖；
- input buffer/polling 按游戏设计保持响应；
- repeated multi-hit 不应把游戏永久锁住。

起始调参可从几十毫秒量级试，不把数值当规则。

## 5. Camera shake

优先：

```text
event -> add bounded trauma/intensity -> smooth noise/oscillation -> decay to zero
```

不要每帧完全随机 offset，容易变成视觉噪声。

Shake 改 Camera2D offset/rotation 或 visual rig；不改 player/world physics transform。

提供 reduced shake 选项 when relevant。

## 6. Flash / shader feedback

短 white/bright flash 是高性价比 hit confirmation。

- confirmed hit -> set material/shader parameter -> short reset；
- retrigger 时 restart/replace，不无限叠 Tween；
- shared material 要注意实例间参数串联；
- pixel art 保持 silhouette 与 crisp edges。

## 7. Recoil and squash/stretch

Presentation recoil：

- weapon kick；
- sprite visual offset；
- squash/stretch；
- short rotation/punch。

Gameplay knockback 属于 combat/movement。

可重触发 Tween 时：

```text
store tween
-> kill/replace
-> start new tween
```

不要让两个 Tween 同时争同一个 property。

## 8. Particles / impact FX

特效应帮助玩家读懂：

- hit position；
- force direction；
- damage/element type；
- event importance。

保持短生命周期，避免盖住 enemy telegraph/pose。

常见：

- slash/spark burst；
- debris/blood/magic burst；
- trail；
- landing dust；
- death burst。

## 9. Sound is part of feel

必要时拆分：

```text
wind-up/whoosh
-> contact impact
-> target hurt/material response
```

高频 SFX 可使用少量受控 variation/pitch，避免机械重复。

Audio mix/ducking 深度问题读 `audio.md`。

## 10. Rumble

Rumble 只增加反馈：

- scale by importance；
- duration short；
- repeated triggers bounded；
- stop on scene change/disconnect when needed；
- respect rumble accessibility setting。

Input/device implementation 读 `input-controls-accessibility.md`。

## 11. Movement feel

同样原则用于：

- jump: launch pose/stretch；
- land: squash + dust + subtle sound；
- dash: trail + directional sound + optional tiny shake；
- pickup: pop + sparkle + SFX；
- UI confirm: focused press motion + sound。

Feedback 必须回到 rest state。

## 12. Failure modes

- hit-stop 太长，像 input lag；
- shake 不衰减；
- flash/Tween 重复叠加后无法恢复；
- VFX 比敌人攻击 telegraph 更抢眼；
- 所有事件都同样夸张；
- feedback 先于 confirmed gameplay event；
- polish 改坏 collision/aim/physics；
- 每个 hit 创建大量 node 而不清理，然后误以为必须先上复杂 pooling。

## Validation

在真实连续战斗中验证，而不是只看一次 staged hit：

- input 仍及时；
- hit-stop 总能恢复；
- shake 完全回到 neutral；
- flash/material/tween 回到 default；
- 多敌人同时受击仍可读；
- ordinary vs heavy hit 有明显层级；
- reduced shake/rumble/flash settings if implemented 确实生效。

## Source synthesis

核心来自 `game-feel` 跨引擎原则、Godot Tween/Camera2D/particles/shader/audio 实践和 action-game feedback patterns。默认用原生 Godot 能力；外部 juice addon 只在项目明确需要 designer-authored graph/large effect library 时考虑。