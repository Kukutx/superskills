# Data, Save, Inventory, Dialogue and Localization Reference

用于 Resource-driven content、runtime data、inventory、save/load versioning、dialogue 和 localization。

## 1. Separate definition from runtime state

Example：

```text
ItemDefinition(Resource)
- id
- display_name_key
- icon
- max_stack
- value

InventoryEntry(runtime)
- item_id/reference
- quantity
- durability/instance state
```

不要直接把共享 definition 当每个实例的 mutable runtime state。

## 2. Stable IDs

Persistent data 使用 stable ID：

- `iron_sword`
- `npc_mira`
- `quest_intro`

不要保存：

- translated display name；
- fragile node path；
- arbitrary runtime instance id。

## 3. Resource-driven content

适合：

- items；
- attacks；
- abilities；
- enemy archetypes；
- quests；
- dialogue；
- loot；
- level metadata。

内容多、迭代频繁时才体现价值。

## 4. Inventory

Inventory truth 是数据结构，不是 UI child list。

UI：

```text
inventory changed
-> rebuild/update visible slots
```

不要通过 GridContainer children 反推真实 inventory。

明确：

- stacking；
- capacity；
- unique item state；
- equipment；
- remove/use transaction；
- save format。

## 5. Save schema

保存的是必要 gameplay state，不是整个 SceneTree snapshot。

常见：

```text
version
player position/checkpoint
stats
inventory
quests/flags
world state
settings/profile references
procedural seed if needed
```

## 6. Version migration

Save format 一开始就有 `version`。

加载流程：

```text
read
-> validate
-> migrate old version stepwise
-> apply to runtime
```

不要因为 v1 简单就假设永远不变。

## 7. Atomic/safe writing

避免写一半破坏唯一存档。

可采用：

- write temp；
- validate/flush；
- replace final；
- backup/slot according to platform needs。

实际实现跟随 Godot/platform capability。

## 8. Autosave

Autosave trigger 必须有明确时机：

- checkpoint；
- scene transition；
- inventory transaction；
- timed interval；
- app lifecycle event。

不要每帧保存。
高频状态变化可 debounce/coalesce。

## 9. Dialogue model

Dialogue truth 与 UI 分开。

Data 可表达：

- speaker；
- text key；
- choices；
- conditions；
- effects；
- next node。

UI 负责：

- portrait；
- typewriter；
- choice rendering；
- input/focus；
- skip/advance。

不要把 story branching 逻辑硬写进 Label/Button callback。

## 10. Dialogue side effects

Choice/action side effect 要走明确 gameplay API：

```text
set_flag
grant_item
start_quest
change_relationship
```

避免任意字符串直接执行未知脚本。

## 11. Localization

从一开始分离：

```text
stable content key
!= displayed translated text
```

UI containers 允许 longer translation。
不要把正常文本烤进 UI sprite。

## 12. Settings vs save game

分开概念：

- settings/preferences；
- profile/meta progression；
- per-save world state。

不要一个 JSON 混全部然后任何改动都重写整个文件。

## 13. Loading order

加载时明确依赖：

```text
load definitions
-> load save data
-> create world/scene
-> apply persistent state
-> notify UI/presentation
```

避免 UI 在数据未 ready 时读取半初始化状态。

## 14. External dialogue systems

For dialogue-heavy games, a mature addon can be better than inventing a parser/editor.

**Dialogue Manager** is a strong optional choice for branching dialogue, conditions/mutations, translations and editor/runtime integration.

Use it only when the project needs those capabilities or already depends on it. Keep these boundaries:

```text
dialogue addon/resource -> dialogue flow/evaluation
gameplay API -> side effects
project UI -> visual presentation/input
save system -> persistent flags/state
```

Do not let plugin-specific dialogue strings become the only representation of core inventory/quest state.

Always match the addon release to the project's Godot version.

## 15. Save/data QA

测试：

- new game no file；
- corrupted/partial file；
- old version；
- empty inventory；
- max stack；
- unique item state；
- scene reload；
- save immediately after transaction；
- localization switch；
- dialogue choice re-entry；
- procedural seed restore。

## Source synthesis

主要吸收 GodotPrompter `resource-pattern`/`inventory-system`/`save-load`/`dialogue-system`/`localization`，GD-Agentic-Skills Resource/save/dialogue patterns，以及 awesome-gamedev-agent-skills save/dialogue disciplines。
