# Input, Controls and Accessibility Reference

用于 InputMap、keyboard/mouse/gamepad/touch、remapping、active-device detection、input prompts、deadzone、rumble/haptics 与控制相关 accessibility。

Movement physics 请读 `movement-physics-camera.md`；菜单 focus/layout 请配合 `ui-ux.md`。

## Gameplay consumes actions, not physical buttons

Gameplay 优先读取稳定 action：

```text
move_left
move_right
jump
attack
interact
pause
```

```text
physical input
-> InputMap/action
-> gameplay intent
-> state decides whether action is allowed
```

不要把 keyboard/gamepad/touch 分成三套 gameplay logic。

## Binding != meaning

Action `interact` 是稳定语义；E、gamepad button 或 touch control 只是可替换 binding。

因此：

- UI prompt 根据当前 binding/device 显示；
- settings 持久化 binding；
- gameplay 不关心具体硬件 key code。

## Device coexistence

通常检测最近有效输入并切换提示，但避免 analog drift / tiny mouse movement 造成 prompt 抖动。

使用合适 deadzone/threshold/debounce。

## Gamepad

检查：

- analog deadzone;
- controller navigation focus;
- confirm/cancel mapping;
- disconnect/reconnect;
- multiple device IDs when relevant;
- glyph/prompt family;
- rumble optional and stoppable.

不要假设所有手柄布局一致。

## Remapping

```text
select action
-> listening state
-> capture allowed event
-> detect conflict
-> replace/swap/reject by explicit policy
-> update InputMap
-> persist settings
-> refresh prompts
```

Conflict policy 必须明确，避免静默覆盖。

保存可重建 binding 数据；加载时验证 action/event，非法配置回退安全默认值，并保证 menu confirm/back 可恢复。

## Input buffering

动作游戏中可对重要 action 使用短 buffer：

```text
press -> timestamp/expiry -> consume once when state becomes valid
```

只 buffer 设计允许的 action，过期输入不得延迟自动触发。

## Touch/mobile

Touch controls 仍产生同一 gameplay actions。

检查 touch target、safe area、virtual stick deadzone/radius、drag/cancel、多指输入、UI/gameplay touch 冲突和 orientation/aspect。

不要复制 mobile-only character logic。

## Input prompts

Prompt 从当前 action binding 推导，而不是硬编码文本/设备：

```text
Press [E] to interact
Press [X] to interact
Tap [Interact] to interact
```

项目已有 input abstraction 就沿用；简单项目优先使用 InputMap + 自有 mapping。

只有 repeated device/remap/prompt/rumble plumbing 已经成为真实复杂度时，才评估第三方 helper，并按主 Skill dependency rule 重新验证兼容性和维护状态。

## Rumble / haptics

Rumble 是 feedback，不是玩法真源。

- strength/duration 与事件重要性匹配；
- repeated hits 不无限延长强震动；
- scene change/pause/disconnect 时可停止；
- 提供 off/reduced intensity when relevant。

## Accessibility

按项目需求考虑：

- full remapping;
- hold vs toggle;
- sensitivity/deadzone settings;
- reduced rumble;
- reduced shake/flashes;
- keyboard-only / gamepad-only 完整路径;
- non-color-only status cues when relevant.

## Validation

实际检查：

- keyboard/mouse/gamepad only;
- unplug/replug gamepad;
- analog near deadzone;
- rapid device switching;
- remap conflict / restore defaults;
- restart and persistence;
- pause/menu navigation;
- touch multi-input if mobile;
- rumble stop/disable.
