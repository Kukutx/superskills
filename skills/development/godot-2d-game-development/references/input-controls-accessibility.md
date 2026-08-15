# Input, Controls and Accessibility Reference

用于 Input Map、keyboard/mouse/gamepad/touch、remapping、active-device detection、input prompts、deadzone、rumble/haptics 与控制相关 accessibility。

Movement physics 请读 `movement-physics-camera.md`；菜单 focus/layout 请配合 `ui-ux.md`。

## 1. Gameplay consumes actions, not physical buttons

Gameplay 代码优先读取：

```text
move_left
move_right
jump
attack
interact
pause
```

不要把 `KEY_SPACE`、Xbox A、触屏按钮分别写成三套 gameplay logic。

```text
physical input
-> InputMap/action
-> gameplay intent
-> state decides whether action is allowed
```

## 2. Separate binding from meaning

Action `interact` 是稳定语义；键盘 `E`、gamepad `X` 或 touch button 是可替换 binding。

因此：

- UI prompt 根据当前 binding/device 显示；
- save/settings 持久化 binding；
- gameplay 不关心具体硬件 key code。

## 3. Device coexistence

不要要求玩家先在设置里声明“现在使用键盘/手柄”。常见体验是检测最近有效输入并切换提示。

但避免 analog stick 微小 drift 导致提示在 keyboard/gamepad 间闪烁：

- analog input 需要 deadzone/meaningful threshold；
- mouse movement 可设置合理 threshold；
- device switch 要 debounce when needed。

## 4. Gamepad

确认：

- analog deadzone；
- controller navigation focus；
- confirm/cancel mapping；
- disconnect/reconnect；
- multiple device IDs if multiplayer/local co-op matters；
- glyph/prompt family when available；
- rumble optional and stoppable。

不要假设所有手柄布局/名称一致。

## 5. Remapping

Remap flow 至少定义：

```text
select action
-> enter listening state
-> capture allowed event
-> detect conflict
-> replace/swap/reject according to explicit policy
-> update InputMap
-> persist settings
-> refresh prompts
```

不要把 remap UI 直接修改 gameplay variables。

### Conflict policy

必须清楚选择：

- reject duplicate；
- replace existing binding；
- swap bindings；
- allow duplicates for selected actions。

避免静默覆盖。

## 6. Persistent bindings

保存可重建的 binding 数据，不要保存脆弱 UI state。

加载后：

1. validate action still exists；
2. validate event type/data；
3. apply mapping；
4. fall back to safe defaults if invalid；
5. guarantee menu confirm/back remains recoverable。

最好提供 restore defaults。

## 7. Input buffering

动作游戏中，hit-stop/recovery/transition 可能吞掉合理输入。

可对重要 action 使用短 buffer：

```text
press -> timestamp/expiry -> consume once when state becomes valid
```

只 buffer 设计允许的 action；不要让过期输入突然自动执行。

## 8. Touch/mobile

Touch controls 仍应产生相同 gameplay actions。

检查：

- touch target 大小；
- safe area；
- virtual stick deadzone/radius；
- drag/cancel behavior；
- 多指同时移动+攻击；
- UI 与 gameplay touch 区域冲突；
- orientation/aspect changes if supported。

不要复制一套 mobile-only character logic。

## 9. Input prompts

Prompt 显示的是**当前 action binding**，不是硬编码文本：

```text
Press [E] to interact
Press [X] to interact
Tap [Interact] to interact
```

如果项目已有输入提示 addon，复用它。否则简单项目可直接从 InputMap + 自有 icon mapping 实现。

## 10. Rumble / haptics

Rumble 是 feedback，不是玩法真源。

- strength/duration 与事件重要性匹配；
- repeated hits 不应无限延长强震动；
- scene change/pause/controller disconnect 时能停止；
- 提供 rumble off / reduced intensity when relevant。

## 11. Accessibility controls

按项目需求考虑：

- full remapping；
- hold vs toggle options；
- aim sensitivity；
- deadzone settings；
- reduced rumble；
- reduced screen shake/flashes 在表现层对应设置；
- keyboard-only / gamepad-only 完整路径；
- non-color-only prompts/status where relevant。

不要把 accessibility 当最后才补的 UI 文案问题。

## 12. Optional Input Helper

`nathanhoad/godot_input_helper` 是成熟的可选 Godot 4 addon，适合项目需要：

- active input device detection；
- query/change action bindings；
- joypad differentiation；
- rumble；
- GDScript/C# helper workflow。

选择规则：

```text
native InputMap already enough -> stay native
need repeated device/remap/prompt/rumble plumbing -> consider Input Helper
project already has another input abstraction -> do not add a second one
```

新增依赖前检查项目 Godot 版本和当前 addon release。

## Validation

实际检查：

- keyboard only；
- mouse + keyboard；
- gamepad only；
- unplug/replug gamepad；
- analog stick near deadzone；
- rapid keyboard/gamepad switching；
- remap conflict；
- restore defaults；
- restart and persistence；
- pause/menu navigation；
- touch multi-input if mobile；
- rumble stop/disable。

## Source synthesis

基于 Godot InputMap/input-event 官方实践、Godot official demos、game UI/input disciplines，以及 `nathanhoad/godot_input_helper` 提供的设备/映射/rumble workflow。