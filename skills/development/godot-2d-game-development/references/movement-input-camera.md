# Movement, Input and Camera Reference

用于 CharacterBody2D、input、platformer/top-down movement、dash/jump、physics feel 与 Camera2D。

## 1. Input expresses intent

使用 Input Map named actions：

```text
move_left/right/up/down
jump
attack
dash
interact
pause
```

Input 层表达“玩家想做什么”；character/state 决定当前能否执行。

不要把完整伤害/AI/scene logic 塞进 `_input()`。

## 2. Physics tick owns movement

CharacterBody2D 关键 movement/collision 在 `_physics_process()`：

```text
read/consume intent
-> update velocity/state
-> move_and_slide()
-> inspect collision/floor result
```

不要把 physics motion 放 `_process()`。

## 3. Top-down movement

明确：

- normalize diagonal input or intentionally not；
- acceleration/deceleration vs instant velocity；
- facing policy；
- collision response；
- analog stick deadzone；
- dash interaction。

不要把 visual facing 与 physics direction 混成一个不清楚的变量。

## 4. Platformer feel

按需要加入：

- coyote time；
- jump buffer；
- variable jump height；
- fall gravity multiplier；
- apex tuning；
- acceleration/deceleration；
- floor snap/slope handling。

这些不是 mandatory checklist。游戏不需要就不要加。

## 5. Input buffer

动作游戏在 recovery/hit-stop/animation transition 中容易吞输入。

可为重要 action 记录短 buffer：

```text
pressed_at
expires_at
consume when state becomes valid
```

Buffer 不等于自动执行所有旧输入。只保留明确设计允许的 action。

## 6. Dash

定义：

- direction source；
- duration/distance；
- cooldown；
- collision policy；
- invulnerability yes/no；
- cancel rules；
- input lock degree；
- visual trail separate from real hitbox/body。

不要靠“播放 dash 动画多久”隐式决定 dash 真值。

## 7. Knockback interaction

如果 character controller 自己控制 velocity，外部 raw physics impulse 可能立刻被 controller 覆盖。

明确选择：

- controller-owned knockback state/velocity；
- additive external velocity；
- temporary control lock/reduced control。

presentation recoil 与 gameplay knockback 分开。

## 8. Collision layers/masks

高频 physics filtering 用 layer/mask。

Debug 顺序：

1. body/area type；
2. layer；
3. mask；
4. CollisionShape enabled；
5. monitoring/monitorable；
6. world transform/scale；
7. expected signal/query type。

不要先怀疑 Godot physics bug。

## 9. Camera framing vs feedback

Camera framing owns：

- follow；
- smoothing；
- look-ahead；
- dead zone；
- bounds；
- zoom。

Game feel owns：

- shake；
- impact offset；
- zoom punch。

不要用 camera shake 改 player/body 真位置。

## 10. Camera follow

Camera 参数由游戏类型决定：

Top-down:

- usually centered/soft follow；
- optional cursor/aim look-ahead；
- strict room/world limits。

Platformer:

- horizontal look-ahead；
- vertical dead zone；
- landing/jump framing；
- room transitions。

不要让 camera 追每个像素噪声。

## 11. Pixel camera

Pixel art 需要明确：

- nearest/point sampling；
- base resolution；
- integer scaling policy；
- camera subpixel policy；
- viewport stretch strategy。

“pixel-perfect”不是一条固定规则。如果 smooth subpixel camera 更符合视觉目标，就在实际运动中验证 shimmer/blur 后决定。

## 12. Touch/mobile

仅目标平台需要时：

- virtual controls 不遮关键画面；
- touch target 足够大；
- analog drag/deadzone；
- safe area；
- input action abstraction 与 desktop/gamepad 共用 gameplay intent。

不要复制一套 mobile-only gameplay logic。

## 13. Movement validation

测试：

- cardinal + diagonal；
- rapid direction change；
- wall/corner；
- low/high FPS perception；
- repeated dash；
- attack/hurt during movement；
- pause/time-scale；
- controller deadzone；
- camera at world bounds；
- pixel shimmer while moving。

## Source synthesis

主要吸收 Godot CharacterBody2D/2D physics/input/camera patterns、awesome-gamedev 的 input/camera/physics-tuning principles，以及 game-feel 的 responsiveness 要求。
