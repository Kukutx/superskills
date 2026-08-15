# Movement, Physics and Camera Reference

用于 CharacterBody2D、platformer/top-down movement、jump/dash、collision response、knockback interaction、Camera2D 与 pixel-camera behavior。

输入设备、remap、rumble、keyboard/gamepad/touch UX 请读 `input-controls-accessibility.md`。

## 1. Physics owns movement truth

关键移动放 `_physics_process()`：

```text
consume intent
-> update movement/state
-> update velocity
-> move_and_slide()
-> inspect floor/wall/collision result
```

Animation/FX 可以表现移动，但不要偷偷成为实际位移真源。

## 2. Top-down movement

明确这些设计，而不是复制固定公式：

- diagonal input 是否 normalize；
- instant velocity 或 acceleration/deceleration；
- analog deadzone 由 input 层处理；
- facing 与 movement direction 是否独立；
- dash/knockback 如何覆盖或混合普通移动；
- top-down depth/y-sort 是否影响 visual root，而非 physics root。

## 3. Platformer feel

按游戏需要选用：

- coyote time；
- jump buffer；
- variable jump height；
- different rise/fall gravity；
- apex tuning；
- acceleration/deceleration；
- floor snap / slope handling。

不是 mandatory checklist。简单游戏不需要就不要加。

## 4. Dash

显式定义：

```text
direction source
duration or distance
speed profile
cooldown
collision behavior
i-frame yes/no
cancel rules
control lock degree
```

Dash gameplay 不应只由“动画播放多久”决定。

## 5. Knockback

如果 controller 每帧自己写 velocity，直接施加一次外部 impulse 往往会被下一 physics tick 覆盖。

选择清楚：

- temporary knockback state；
- additive external velocity；
- controlled velocity override；
- reduced/locked control window。

Visual recoil 可以独立作用在 sprite/weapon visual child，不移动 collision body。

## 6. Collision debugging order

优先检查：

1. body/area 类型；
2. collision layer；
3. mask；
4. CollisionShape 是否 enabled；
5. Area monitoring/monitorable；
6. world transform/scale；
7. expected callback/query type；
8. physics tick timing。

不要先假设是引擎 physics bug。

## 7. Camera framing and feedback are separate

Framing:

- follow；
- smoothing；
- dead zone；
- look-ahead；
- bounds/room limits；
- zoom。

Feedback:

- shake；
- impact offset；
- zoom punch。

Game-feel 反馈只改 camera/visual presentation，不移动 player physics body。

## 8. Top-down camera

通常关注：

- soft/centered follow；
- optional aim/cursor look-ahead；
- world/room limits；
- scene transition behavior；
- boss/arena framing only when needed。

## 9. Platformer camera

可考虑：

- horizontal look-ahead；
- vertical dead zone；
- landing/jump framing；
- room transitions；
- camera bounds。

Camera 不应追随每个小幅 sprite deformation 或 shake noise。

## 10. Pixel camera

明确项目自己的 pixel policy：

```text
base render resolution
nearest/point filtering
integer display scale yes/no
camera subpixel policy
stretch policy
```

“pixel-perfect”不是统一答案。严格整数坐标可能清晰但造成运动阶梯感；smooth camera 可能更自然但产生 shimmer。必须在实际运动中验证。

## 11. Moving platforms / external motion

如果游戏有 moving platform、conveyor、push zone：

- 明确 world motion 与 player input velocity 的组合顺序；
- 避免在 render tick 手动 teleport body；
- 检查离开平台时是否继承速度；
- 检查 corner/slope/floor snap interaction。

## 12. Time scale / hit-stop

Movement 系统需要确认 global slowdown/hit-stop 时：

- physics behavior 是否符合设计；
- input 是否仍被采集/缓冲；
- unscaled timers 是否只用于确实需要 real-time 的恢复逻辑。

不要在 movement script 内私自重置全局 `Engine.time_scale`。

## Validation

至少实际测试：

- cardinal + diagonal；
- rapid direction changes；
- wall/corner/slope；
- jump edge/coyote/buffer if implemented；
- repeated dash；
- attack/hurt/knockback during movement；
- moving platforms if used；
- camera world bounds；
- pixel shimmer during camera/player motion；
- pause/time-scale transitions。

## Source synthesis

基于 Godot CharacterBody2D/physics/camera 官方模式、Godot official demos，以及 Godot-specific agent skills 的 movement/camera lessons。精确 API 以项目对应 Godot 版本为准。