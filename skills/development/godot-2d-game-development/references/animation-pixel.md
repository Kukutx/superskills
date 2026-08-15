# Pixel Animation Runtime Reference

用于 Godot 2D runtime animation：`AnimatedSprite2D`、`SpriteFrames`、`AnimationPlayer`、`AnimationTree`、Tween、状态同步、事件 timing 和 pixel rendering。

**不负责生成/切分 spritesheet。** 新动作 strip、frame geometry、shared anchor、切图、naming 请用 `development/game-dev-spritesheet-slicer`；source/import pipeline 读 `asset-pipeline.md`。

## 1. One authority per property or timeline

按需求选最简单的工具：

| Need | Prefer |
| --- | --- |
| pure frame-by-frame sprite animation | `AnimatedSprite2D` + `SpriteFrames` |
| property/audio/method/event tracks | `AnimationPlayer` |
| locomotion/state blending | `AnimationTree` backed by animations |
| dynamic one-shot scale/position/color effect | `Tween` |

不要让 code、AnimationPlayer、AnimationTree 和 Tween 同时写同一个 property。

## 2. Gameplay owns intent

Animation 表现 gameplay state，不替代它：

```text
input / AI intent
-> gameplay state decides action
-> animation selected
-> explicit timeline event when needed
-> combat/physics/presentation reacts according to ownership
```

不要用大量 `animation == "attack"` 判断来充当唯一 state machine。

## 3. Timeline events and gameplay boundaries

当视觉和玩法必须精确同步时，使用一个 authoritative timeline/event，而不是多个 Timer 猜同一时刻。

适合 animation event/track 的内容：

- request hitbox active/inactive window;
- projectile release moment;
- footstep;
- whoosh/impact SFX trigger;
- particles/trail toggle;
- visual property changes.

边界仍然是：

```text
animation says "timing event now"
-> combat/state system decides whether/how gameplay truth changes
```

Animation track 不直接绕过 combat receiver 修改目标 HP。

## 4. Attack animation timing

动作通常可表达为：

```text
startup -> active -> recovery
```

视觉 key pose 与 active window 应一致，但 frame count/FPS 不是 gameplay rule 本身。

检查：

- startup 是否给足 anticipation/readability;
- active event 是否落在真正接触帧附近;
- recovery 是否和 cancel/input rules 一致;
- interruption/hurt/death 时旧 active event 不会继续生效.

具体 repeated-hit / i-frame / combo correctness 读 `combat-system.md`。

## 5. Frame timing is not uniform by default

同一 animation 可以有不同 frame durations/holds。

例如：

- idle 可以慢;
- anticipation 可以 hold;
- impact pose 可以短暂强调;
- recovery 可以按手感调整;
- hurt/death 通常 one-shot.

不要因为 spritesheet 每格一样大，就默认每帧播放时间也一样。

## 6. Loop and transition semantics

明确每个 animation：

- loop / one-shot;
- exit condition;
- interruption policy;
- restart vs resume;
- blend/transition rule when using AnimationTree.

不要依赖一个只适用于 non-loop animation 的 finished signal 去结束 looping state。

快速切换状态时检查一帧闪错 pose、旧 animation event 延迟触发和 transition 未 reset 的问题。

## 7. Tween lifecycle

Tween 适合 presentation-only one-shot：

- squash/stretch;
- recoil recovery;
- pickup/UI pop;
- short color/scale/offset response.

同一个 effect 可能在前一次结束前再次触发时：

```text
store tween
-> kill/replace previous tween
-> start new tween
```

不要让多个 Tween 争同一个 property，也不要让 visual Tween 偷偷改变 physics truth。

## 8. Pixel runtime policy

项目应明确自己的 pixel rendering policy：

```text
base render resolution
filtering policy
integer display scale yes/no
camera/subpixel policy
stretch policy
```

通常要避免意外 linear filtering、mipmap blur 和不受控 fractional scale；但不要把“所有物体必须整数坐标”当成通用规则。

如果 smooth camera/subpixel motion 是设计的一部分，必须看实际运动中的 shimmer/blur，而不是只看静态截图。

## 9. Asset handoff boundary

Runtime animation 只应依赖清楚的 asset contract：

- animation/action names;
- frames/ranges;
- timing metadata;
- loop policy;
- stable anchor/pivot;
- direction naming.

如果这些信息本身还没稳定，先回到 spritesheet/asset production，而不是在 runtime code 里补大量 magic indices。

## 10. Pause / hit-stop / time scale

确认 animation 与 gameplay time policy 一致：

- 哪些 animation/tween 随 game pause;
- hit-stop 时 input 是否仍需要采集/缓冲;
- UI animation 是否继续;
- recovery timer/tween 是否使用正确的 time domain.

不要让某个 animation helper 私自重置全局 time scale。

## Validation

实际验证 relevant cases：

- idle/move/attack/hurt/death transitions;
- rapid state switching;
- looping animations;
- one-shot completes/exits once;
- attack event aligns with visible contact;
- interrupted attack cannot leave hitbox active;
- repeated Tween trigger returns to rest state;
- pause/hit-stop behavior;
- no one-frame wrong pose/flash;
- pixel art remains crisp/readable in actual camera motion and target resolution.
