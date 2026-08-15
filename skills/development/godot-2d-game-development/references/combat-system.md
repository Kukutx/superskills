# Combat System Reference

用于 **战斗正确性**：attack state、startup/active/recovery、hitbox/hurtbox、damage payload、i-frame、multi-hit policy、combo/cancel、death/stagger。

“机制已经正确但不够爽”请读 `game-feel.md`。

## 1. Combat truth and presentation

Combat owns：

- attack allowed or not；
- attack phase；
- hitbox active window；
- hit confirmation；
- damage/status/crit/resistance result；
- i-frame / repeated-hit policy；
- gameplay knockback/stagger；
- death。

Animation/VFX/audio/camera 表现这些结果，不反过来决定伤害真值。

## 2. Baseline pipeline

常见清晰边界：

```text
Attack/Ability definition
-> attacker state/timeline
-> Hitbox(Area2D)
-> Hurtbox(Area2D)
-> structured attack/damage payload
-> Health/Damage receiver
-> result event: hit / health_changed / died
```

类名可以不同，ownership 要清楚。

避免：

```text
attacker detects target
-> target.health -= 10
```

这会绕过 i-frame、resistance、source、knockback、crit 等规则。

## 3. Attack phases

显式区分：

```text
startup -> active -> recovery
```

- startup: 起手/anticipation；
- active: hitbox 有效；
- recovery: hitbox 已关闭但动作尚未完全可取消。

Frame-perfect 游戏可以用 AnimationPlayer method/property tracks 或单一 authoritative timeline 同步 hitbox。不要多个 Timer 猜同一攻击窗口。

## 4. Hitbox / hurtbox

典型 2D action game：

- `Area2D` + `CollisionShape2D`；
- layer/mask 做 physics filtering；
- hitbox 默认 inactive，仅 active window 开启；
- physics callback 内切 shape 状态时遵循 Godot deferred-change 要求；
- hitbox 记录 attack instance / already-hit targets when needed。

不要把 groups 当主要 physics filter。

## 5. Repeated-hit policy

必须明确一击重叠多个 physics frame 时如何处理：

- once per attack instance；
- target i-frame；
- per-target tick cooldown；
- intentionally repeated DoT ticks。

Multi-hit attack 也要明确每段命中的 interval/target policy。

## 6. Damage payload

建议传递结构化数据，例如：

```text
source
base_damage
damage_type/tags
critical info
knockback intent
stagger/status
attack instance id
```

简单游戏可以更小，但不要把相关上下文拆成散落的全局变量。

Definitions 可用 Resource；mutable runtime hit instance 不要误用共享 Resource 导致实例串状态。

## 7. I-frames

I-frame 由 receiver/combat layer 统一决定，避免每个攻击方自己猜。

检查：

- invulnerable window 起止；
- 哪些 damage type 可绕过；
- overlap during i-frame；
- visual blink/flash 只是表现；
- hit-stop 不应意外延长/缩短规则，除非设计如此。

## 8. Gameplay knockback / stagger

Combat 产生 **knockback intent/result**；character controller 执行实际移动策略。

不要从 hitbox 直接给 CharacterBody2D 一个 impulse 然后下一帧 controller 又覆盖它。

常见策略：

- knockback state；
- external velocity channel；
- short movement override；
- stagger state with reduced/locked control。

Visual recoil 属于 `game-feel.md`。

## 9. Combo / cancel

Combo 系统需要显式：

```text
input buffer
combo window
next attack mapping
cancel window
resource/stamina rules
recovery/whiff policy
```

不要把 `animation_finished` 当唯一 combo logic。

动画可以发 timing event，但 gameplay state 决定能否 transition。

## 10. Projectiles

Projectile 要明确：

- owner/team；
- collision layers/masks；
- lifetime/range；
- piercing/bounce count；
- one-target repeated hit policy；
- spawn point/direction；
- cleanup/pooling only if profiling justifies。

视觉 projectile 与实际 hit shape 要保持可读一致，但不要求像素级形状完全相同。

## 11. Death

Death sequence 至少保证：

- 不再创建新攻击；
- hitbox 关闭；
- body/hurtbox 是否继续碰撞按设计处理；
- gameplay state 不再接受无效 input/AI action；
- death signal 只触发一次；
- animation/VFX/loot/score 监听明确事件。

## Debug order

出现“攻击判定错”时按顺序：

1. attack state 是否进入；
2. hitbox 是否在正确 window active；
3. layer/mask；
4. hitbox/hurtbox overlap callback；
5. repeated-hit / i-frame gate；
6. damage receiver；
7. state exit/cancel；
8. presentation sync。

先证明 combat truth，再调视觉。

## Validation

测试：

- one swing -> expected hit count；
- holding overlap；
- rapid repeated attacks；
- whiff；
- multi-target；
- target dies on hit；
- i-frame；
- combo timing；
- attack interrupted by hurt/death；
- pause/time-scale；
- collision disabled/enabled lifecycle。
