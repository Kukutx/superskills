# Save, Inventory and Progression Reference

用于 persistent IDs、Resource definitions、runtime inventory、save/load、schema migration、settings、checkpoint/progression 与复杂 inventory addon selection。

对话结构和本地化请读 `dialogue-localization.md`。

## 1. Definition != runtime state

例如：

```text
ItemDefinition(Resource)
- id
- display_name_key
- icon
- max_stack
- base value

InventoryEntry(runtime/save)
- item_id
- quantity
- durability / rolled stats / unique state
```

不要把共享 Resource definition 当成每个实例的 mutable state。

## 2. Stable IDs

持久化使用稳定 ID：

```text
iron_sword
npc_mira
quest_intro
checkpoint_forest_02
```

不要把 translated display name、fragile NodePath、runtime instance ID 当长期主键。

## 3. Save only persistent truth

常见 save schema：

```text
version
profile/save id
checkpoint or player world position when appropriate
stats/progression
inventory/equipment
quest/flag state
world state
procedural seed if required
```

不要序列化整个 SceneTree 作为存档。

## 4. Schema version from day one

```text
read raw data
-> validate basic shape
-> migrate version N -> N+1 stepwise
-> validate migrated data
-> instantiate/apply runtime state
```

不要永久堆“字段不存在就补默认值”的兼容泥团。

## 5. Migration

迁移应：

- deterministic；
- stepwise；
- old ID mapping explicit；
- failure 可诊断；
- 不静默清空 save。

重要升级保留旧版 fixture 做 migration test。

## 6. Safe writing

避免写一半破坏唯一存档：

```text
serialize
-> write temp
-> flush/close
-> optional read-back validate
-> replace final
-> optional backup/slot rotation
```

原子替换能力以目标平台/Godot API 为准。

## 7. Autosave

明确触发点：

- checkpoint；
- scene transition；
- inventory transaction；
- quest/progression event；
- timed debounce；
- app lifecycle when needed。

不要每帧保存。高频事件 coalesce/debounce。

## 8. Inventory truth is data, not UI

```text
inventory transaction
-> validate
-> mutate inventory data
-> emit inventory_changed
-> UI updates
```

不要通过 GridContainer children 反推真实 inventory。

明确：

- stacking；
- capacity；
- unique item state；
- equipment slots；
- transfer/split/merge；
- use/remove transaction；
- missing definition after game update。

## 9. When an inventory addon is justified

简单 inventory（几十个 item、stack + equip）通常自有 Resource/data structure 更透明。

如果项目需要较多通用 inventory mechanics、反复实现容器/stack/transfer/equipment 等功能，可以评估 `peter-kish/gloot` 这类成熟 Godot inventory addon。

选择规则：

```text
simple project-native inventory is clear -> keep it
inventory domain itself is becoming large/repetitive -> evaluate GLoot
project already uses an inventory addon -> keep one source of truth
```

即使使用 addon：

- stable project item IDs 仍由项目定义；
- save schema/migration 仍是项目责任；
- UI 不应成为 inventory truth；
- 不让 plugin-specific transient node path 成为长期 save contract。

## 10. Settings / profile / save-game boundaries

区分：

- settings/preferences：volume, graphics, controls, accessibility；
- profile/meta progression：unlocks/meta state；
- save slot/world state：当前 run/world。

不一定必须三个文件，但概念不要混成一个无法演进的大对象。

Input bindings 读 `input-controls-accessibility.md`。

## 11. Loading order

常见顺序：

```text
load content definitions
-> load/migrate save
-> create target scene/world
-> apply persistent state
-> emit ready/changed events
-> UI/presentation reacts
```

避免 HUD 在 save 还没 apply 时读取半初始化数据。

## 12. Missing/renamed content

长期项目考虑：

- item/quest ID 删除或 rename；
- scene/checkpoint 不再存在；
- stat schema 改变；
- addon version changed serialization details。

优先 migration 显式映射旧 ID；不要通过 display name 猜。

## 13. Transactions and save timing

关键 transaction：

```text
validate
-> mutate gameplay truth
-> emit domain event
-> schedule/save persistent snapshot
```

写盘错误策略按游戏重要性设计，避免 UI/gameplay 半更新。

## Validation matrix

覆盖：

- no save/new game；
- current-version save；
- previous-version save；
- corrupted/partial file；
- missing field；
- removed/renamed item ID；
- empty/full inventory；
- stack split/merge boundary；
- unique/equipment state；
- scene reload；
- save after transaction；
- restart/settings/control persistence；
- procedural seed restore if used；
- addon upgrade migration if inventory plugin is used。

## Source synthesis

吸收 Godot Resource/save patterns、GodotPrompter data/save guidance、跨引擎 save versioning，并将 `peter-kish/gloot` 作为复杂 inventory 的可选成熟 companion，而不是默认架构。