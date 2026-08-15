# Save, Inventory and Progression Reference

用于 persistent IDs、Resource definitions、runtime inventory、save/load、schema migration、settings、checkpoint/progression 与数据恢复。

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

不要试图序列化整个 SceneTree 作为存档。

## 4. Schema version from day one

```text
read raw data
-> validate basic shape
-> migrate version N -> N+1 stepwise
-> validate migrated data
-> instantiate/apply runtime state
```

不要只写一个“如果缺字段就补默认值”的永久兼容泥团。

## 5. Migration

迁移函数应：

- deterministic；
- stepwise；
- idempotence/one-time behavior 明确；
- 保留未知但可安全保留的数据 only when design requires；
- migration failure 给出可诊断错误，而不是静默清空存档。

重要升级至少保留旧版 fixture 做 migration test。

## 6. Safe writing

避免写一半破坏唯一存档：

```text
serialize
-> write temp
-> flush/close
-> optional validate/read-back
-> replace final
-> optional backup/slot rotation
```

具体原子替换能力以目标平台/Godot API 为准。

## 7. Autosave

明确触发点：

- checkpoint；
- scene transition；
- inventory transaction；
- quest/progression event；
- timed debounce；
- app lifecycle event if platform requires。

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
- use/remove transaction；
- item definition missing after update 的处理。

## 9. Settings / profile / save-game boundaries

区分：

- settings/preferences：volume, graphics, controls, accessibility；
- profile/meta progression：unlocks, achievements-like meta state；
- save slot/world state：当前 run/world。

不一定必须三个文件，但概念不要混成一个无法演进的大对象。

Input bindings 的具体编码/恢复与 control safety 读 `input-controls-accessibility.md`。

## 10. Loading order

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

## 11. Missing/renamed content

长期项目必须考虑：

- item/quest ID 被删除；
- item definition rename；
- scene/checkpoint 不再存在；
- stat shape changed。

优先通过 migration 显式映射旧 ID；不要依赖 display name 猜。

## 12. Save ownership and gameplay transactions

关键 transaction（购买、装备、获得重要物品）先完成 gameplay truth，再触发 save。

```text
validate transaction
-> mutate runtime truth
-> emit domain event
-> schedule/save persistent snapshot
```

不要让写磁盘失败把一半 UI/一半 gameplay 状态留在奇怪中间态；错误处理策略按游戏重要性设计。

## Validation matrix

至少覆盖：

- no save/new game；
- normal current-version save；
- previous-version save；
- corrupted/partial file；
- missing field；
- removed content ID；
- empty/full inventory；
- stack boundary；
- unique item state；
- scene reload；
- save immediately after transaction；
- restart and settings/control persistence；
- procedural seed restore if used。

## Source synthesis

吸收 Godot Resource/save patterns、GodotPrompter data/save guidance、跨引擎 save-versioning practices。精确 filesystem/API behavior 必须按项目 Godot 版本和目标平台确认。