# Data / Save / Dialogue Compatibility Index

旧版兼容入口。现在将 persistence 与 narrative 分开。

- Resource definitions、inventory、save/load、schema migration、settings/progression -> `save-inventory-progression.md`
- branching dialogue、conditions/effects、dialogue UI、localization -> `dialogue-localization.md`
- UI layout/focus -> `ui-ux.md`
- control bindings/settings -> `input-controls-accessibility.md`

示例：

```text
“旧存档升级后 inventory 丢了”
-> save-inventory-progression

“NPC 对话有条件分支和多语言”
-> dialogue-localization

“对话选择会给道具并永久保存”
-> dialogue-localization + save-inventory-progression
```

不要因为任务提到 Resource 就自动加载 dialogue/save 全套。