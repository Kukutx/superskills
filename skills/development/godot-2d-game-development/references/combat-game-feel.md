# Combat and Game Feel Reference

用于 hitbox/hurtbox、damage、combo、i-frame、stagger、knockback、hit-stop、camera shake、impact FX 与 action responsiveness。

## 1. Combat truth vs feedback

Combat truth owns：

- can attack；
- active hit window；
- target filtering；
- damage/resistance/crit；
- i-frame；
- stagger/knockback intent；
- death/combo state。

Presentation reacts：

- SFX；
- flash；
- particles；
- camera shake；
- hit-stop；
- damage number；
- visual recoil/squash。

不要让 particle/flash/camera 决定有没有造成伤害。

## 2. Hitbox / hurtbox baseline

典型 2D：

```text
Hitbox(Area2D)
-> Hurtbox(Area2D)
-> structured Attack/Damage payload
-> Health/Combat receiver
-> result/event
```

Physics filtering 用 layers/masks。

不要：

```text
target.health -= 10
```

因为会绕过 armor/i-frame/source/type/knockback 等规则。

## 3. Attack phases

明确：

```text
startup -> active -> recovery
```

Hitbox 只在 active window 有效。

Frame-critical action 优先共享 AnimationPlayer method/property track 或明确 attack timeline；不要几个独立 timer 猜同一时刻。

## 4. One hit policy

一个 visual swing overlap 多个 physics ticks 时，需要明确：

- one hit per attack instance；
- target i-frame；
- per-target multi-hit cooldown；
- intentional DOT ticks。

不要让 repeated overlap 的结果靠运气。

## 5. Combo / cancel

明确：

- input buffer window；
- next attack queue；
- cancel allowed states；
- recovery skip rules；
- hit-confirm-only branch if any；
- animation/hitbox timeline alignment。

Combo 系统不要靠 `if animation_name == ...` 四处分支。

## 6. Knockback

Gameplay knockback 与 visual recoil 分开。

如果 CharacterBody2D controller 每 physics tick 重写 velocity，外部 impulse 可能立刻被覆盖。让 controller/state 明确处理 knockback window 或 external velocity。

## 7. Hit-stop

Hit-stop 只强调 meaningful confirmed impact。

Rules:

- once per impact；
- very short；
- restore previous/global time state；
- recovery delay 必须能在 slowed/frozen time 下结束；
- no blocking sleep；
- important input 可按设计 buffer。

Starting points only:

```text
light  ~20–40 ms
medium ~40–70 ms
heavy  ~70–120 ms
```

高频战斗通常更短。

## 8. Camera shake

推荐：

```text
hit -> add bounded trauma/intensity
-> smooth/noise offset
-> decay to zero
```

避免每帧新 random offset 的“电视雪花感”。

只改 Camera2D visual offset/rotation/zoom，不改 physics body。

## 9. Impact hierarchy

按事件强度分 tier：

| Tier | Typical bundle |
| --- | --- |
| Small | sound + tiny contact FX |
| Medium | sound + FX + recoil/knockback + small shake |
| Heavy | stronger sound + flash + short hit-stop + shake |
| Boss/critical | authored bundle, still readable |

不要每个小怪 hit 都 max juice。

## 10. Flash / shader hit feedback

Confirmed hit：

```text
set flash parameter
-> brief hold/tween
-> reset
```

Repeated hit 时 restart/replace old effect，不要无限 stack Tween。

Pixel art 用 hard/clean flash，谨慎 blur/glow。

## 11. Particles / slash FX

FX 应表达：

- impact position；
- direction；
- damage type；
- importance。

Character attack animation 与大范围 slash/impact FX 最好可独立控制：body animation 不需要承担所有外部特效画面。

## 12. Audio layers

常见 attack：

```text
wind-up/whoosh
-> impact
-> target hurt
-> optional environment response
```

高频 sample 允许轻微 controlled variation，避免 machine-gun sameness。

## 13. Movement game feel

同原则也用于：

- jump launch stretch；
- landing squash + dust；
- dash trail/impact；
- pickup pop；
- interact feedback。

Feedback 必须回到 rest state。

## 14. Accessibility/readability

强反馈项目考虑：

- reduce screen shake；
- reduce flashes；
- damage feedback 不能只靠颜色；
- VFX 不盖住 enemy telegraph。

降低反馈不能移除必要 gameplay information。

## 15. Combat QA

重复真实操作：

- one swing -> intended hit count；
- hitbox active only intended frames；
- multi-hit policy correct；
- combo queue/cancel correct；
- hit-stop always restores；
- shake returns zero；
- flash resets；
- repeated hit does not stack runaway tweens；
- input remains responsive；
- crowded combat still readable；
- death disables further combat interaction as intended。

## Source synthesis

主要吸收 GD-Agentic-Skills `godot-combat-system`、awesome-gamedev `game-feel`、Godot animation/tween/camera patterns。核心原则是：combat truth first, feedback layered second。
