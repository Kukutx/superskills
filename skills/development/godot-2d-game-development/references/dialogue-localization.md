# Dialogue and Localization Reference

用于 branching dialogue、conditions/choices/effects、dialogue UI、localization keys、translated layout 与 narrative tooling boundaries。

Inventory/save persistence 见 `save-inventory-progression.md`。

## Dialogue truth and UI are separate

Dialogue data/flow 表达：

```text
speaker
text/localization key
choices
conditions
mutations/effects
next node / end
```

UI 负责 portrait/name、text rendering/typewriter、choices、focus/input、skip/advance 和 presentation。

不要把 branching story logic 塞进 Label/Button callback。

## Stable content identifiers

Dialogue/quest flags 使用稳定 key/ID，不使用翻译后的文本作为逻辑条件。

Displayed text 可以变化，逻辑 ID 不应跟着翻译或文案调整改变。

## Conditions and side effects

Choice condition 只读取允许的 gameplay state；side effect 通过明确 API，例如：

```text
has_item(id)
get_flag(id)
set_flag(id, value)
grant_item(id, amount)
start_quest(id)
change_relationship(id, delta)
```

不要允许 dialogue text 任意执行未知脚本/string command。

## Persistence boundary

```text
dialogue evaluates condition
-> gameplay API applies effect
-> save/progression state owns persistent result
```

Narrative tooling 的局部变量不要成为 inventory/quest 的唯一真源。

## Localization

```text
stable content key != displayed translated string
```

UI 使用 containers，允许更长 translation；避免固定宽度只适合英文；dynamic text 不烤进 UI sprite；font/fallback 覆盖目标字符。

只有目标语言需要时再处理 RTL/CJK/特殊 line breaking。

## Layout stress

翻译完成前可以用膨胀文本/伪本地化检查：

- button clip;
- dialogue overflow;
- choice list height;
- HUD fixed width;
- missing glyphs.

## Typewriter

Typewriter 是 presentation：

- 不改变完整 text truth；
- skip/advance policy 明确；
- voice/audio timing 明确；
- rich text/Unicode 不按错误 byte index 截断。

## Choice focus

Keyboard/gamepad 下确认默认 focus、上下导航、confirm/cancel 和 text still typing 时的 input policy。

配合 `ui-ux.md` 与 `input-controls-accessibility.md`。

## Complexity boundary

简单线性 dialogue 用项目自有 Resource/JSON + 小 UI 足够时，不增加大型 narrative framework。

只有大量 branching、conditions/mutations、editor workflow、translation 或 content-heavy iteration 已经构成真实复杂度时，才评估专门 tooling。

已有 narrative framework 就沿用，不并行引入第二套。

第三方选择按主 Skill dependency rule 重新验证当前 Godot compatibility、maintenance、license、data ownership 和 migration cost；runtime reference 不固定具体插件名单。

## Dialogue QA

检查：

- every branch reachable as intended;
- invalid/missing next node;
- condition true/false paths;
- side effect once vs repeatable;
- save/reload mid-conversation policy;
- re-enter NPC conversation;
- missing/long translations;
- gamepad choices;
- skip/typewriter;
- changed/removed quest/item IDs.
