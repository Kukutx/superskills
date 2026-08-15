# Dialogue and Localization Reference

用于 branching dialogue、conditions/choices/effects、dialogue UI、localization keys、translated layout 与 dialogue-heavy addon selection。

Inventory/save persistence 请读 `save-inventory-progression.md`。

## 1. Dialogue truth and UI are separate

Dialogue data/flow 表达：

```text
speaker
text/localization key
choices
conditions
mutations/effects
next node / end
```

UI 负责：

- portrait/name display；
- text rendering/typewriter；
- choices；
- focus/input；
- skip/advance；
- accessibility/presentation。

不要把 branching story logic 塞进 Label/Button callback。

## 2. Stable content identifiers

Dialogue/quest flags 使用稳定 key/ID，不使用翻译后的文本作为逻辑条件。

```text
flag_met_blacksmith
quest_intro_completed
dialogue_mira_first_meeting
```

Displayed text 可以变化，逻辑 ID 不应跟着翻译或文案调整改变。

## 3. Conditions and side effects

Choice condition 只读取允许的 gameplay state；side effect 通过明确 API：

```text
has_item(id)
get_flag(id)
set_flag(id, value)
grant_item(id, amount)
start_quest(id)
change_relationship(id, delta)
```

不要允许 dialogue text 任意执行未知脚本/string command。

## 4. Persistence boundary

Dialogue system 可以决定 flow，但持久 truth 应由 save/domain system 持有：

```text
dialogue evaluates condition
-> gameplay API applies effect
-> save/progression state owns persistent result
```

插件自己的局部变量不要成为整个 inventory/quest 的唯一真源。

## 5. Localization

从一开始区分：

```text
stable content key != displayed translated string
```

UI：

- 使用 containers；
- 允许更长 translation；
- 避免固定宽度只适合英文；
- dynamic text 不烤进 UI sprite；
- font/fallback 覆盖目标语言字符；
- right-to-left/CJK/line breaking only when target languages require。

## 6. Pseudolocalization / layout stress

在真正翻译完成前，可以用膨胀文本/伪本地化检查：

- buttons clip；
- dialogue box overflow；
- choice list height；
- HUD fixed width；
- missing glyphs。

Godot official demos/docs 可作为 native localization behavior 的优先参考。

## 7. Typewriter effect

Typewriter 是 presentation：

- 不应改变实际完整 text truth；
- skip 一次通常完成当前 line，再次 input 才 advance（按设计）；
- voice/audio timing 需明确；
- rich text/Unicode 不要按错误 byte index 切断。

## 8. Choice focus

Keyboard/gamepad 下：

- choices 出现时有默认 focus；
- up/down navigation 清楚；
- confirm/cancel behavior 明确；
- text still typing 时 input policy 清楚。

具体 focus 规则配合 `ui-ux.md` 和 `input-controls-accessibility.md`。

## 9. When to use an addon

简单线性 dialogue：自有 Resource/JSON + 小 UI 足够时，不增加大型插件。

复杂项目有：

- 大量 branching；
- conditions/mutations；
- authoring/editor workflow；
- translation；
- narrative designers/content-heavy iteration；

可评估成熟 addon。

### Dialogue Manager

强项是 Godot-native dialogue resources、branching、conditions/mutations、translation/editor/runtime workflow。

重要：**按 Godot 版本选择兼容 release，不把 preview/next-major 自动当默认。**

### Dialogic

如果目标更接近 visual novel / character-heavy timeline authoring、需要更完整的 narrative UI/tooling，可以评估 Dialogic；它比简单 dialogue parser 更重。

已有项目使用其中一个时优先沿用，不并行引入第二个 narrative framework。

## 10. Dialogue data QA

检查：

- every branch reachable as intended；
- invalid/missing next node；
- condition true/false paths；
- side effect only once vs repeatable；
- save/reload mid-conversation policy；
- re-enter NPC conversation；
- missing translation；
- long translation；
- gamepad choices；
- skip/typewriter；
- changed/removed quest/item IDs。

## Source synthesis

基于 Godot localization/signals/UI patterns、Dialogue Manager/Dialogic 的成熟 authoring 思路，以及 save/dialogue domain separation。插件只作为可选工具，核心 gameplay state 仍保持项目自己的明确 ownership。