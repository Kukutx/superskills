# Save, Inventory and Progression Reference

用于 persistent IDs、Resource definitions、runtime inventory、save/load、schema migration、settings、checkpoint/progression 与复杂 inventory architecture。

对话结构和本地化见 `dialogue-localization.md`。

## Definition != runtime state

例如：

```text
ItemDefinition(Resource)
- id
- display_name_key
- icon
- max_stack

InventoryEntry(runtime/save)
- item_id
- quantity
- durability / rolled stats / unique state
```

不要把共享 Resource definition 当成每个实例的 mutable state。

## Stable IDs

持久化使用稳定 ID，例如：

```text
iron_sword
npc_mira
quest_intro
checkpoint_forest_02
```

不要把 translated display name、fragile NodePath 或 runtime instance ID 当长期主键。

## Save only persistent truth

常见 schema：

```text
version
profile/save id
checkpoint or world position when appropriate
stats/progression
inventory/equipment
quest/flag state
world state
procedural seed if required
```

不要序列化整个 SceneTree。

## Versioned migration

从第一版就保存 schema version：

```text
read raw data
-> validate shape
-> migrate N -> N+1 stepwise
-> validate migrated data
-> instantiate/apply runtime state
```

迁移应 deterministic、stepwise、可诊断；旧 ID mapping 显式，不静默清空 save。

重要升级保留旧版 fixture 做 migration test。

## Safe writing

避免写一半破坏唯一存档：

```text
serialize
-> write temp
-> flush/close
-> optional read-back validate
-> replace final
-> optional backup/slot rotation
```

具体原子替换能力以目标平台/Godot API 为准。

## Autosave

明确触发点：checkpoint、scene transition、inventory transaction、quest/progression event、timed debounce 或必要的 app lifecycle。

不要每帧保存；高频事件 coalesce/debounce。

## Inventory truth is data, not UI

```text
inventory transaction
-> validate
-> mutate inventory data
-> emit inventory_changed
-> UI updates
```

不要通过 GridContainer children 反推 inventory truth。

明确 stacking、capacity、unique state、equipment slots、transfer/split/merge、use/remove transaction 和 missing definitions。

## Complexity boundary

简单 inventory（少量 item、stack/equip）通常项目自有 Resource/data structure 更透明。

只有 container/transfer/equipment/stacking 等通用 mechanics 已经大量重复并成为真实维护成本时，才评估第三方 inventory system。

采用外部系统也不改变：

- stable project IDs 由项目定义；
- save schema/migration 是项目责任；
- UI 不成为 truth；
- plugin-specific transient state 不进入长期 save contract。

第三方选择必须按主 Skill dependency rule 重新验证当前兼容性和维护状态，不依赖静态插件名单。

## Settings / profile / save-game boundaries

概念上区分：

- settings/preferences：volume, graphics, controls, accessibility;
- profile/meta progression：unlocks/meta state;
- save slot/world state：当前 run/world.

不一定必须三个文件，但不要混成无法演进的大对象。

Input bindings 见 `input-controls-accessibility.md`。

## Loading order

```text
load content definitions
-> load/migrate save
-> create target scene/world
-> apply persistent state
-> emit ready/changed events
-> UI/presentation reacts
```

避免 UI 在 save 未完成 apply 时读取半初始化数据。

## Missing/renamed content

长期项目考虑 item/quest ID rename、scene/checkpoint 删除、stat schema 变化和 dependency serialization changes。

优先 migration 显式映射旧 ID；不要通过 display name 猜。

## Transaction + persistence

```text
validate
-> mutate gameplay truth
-> emit domain event
-> schedule/save persistent snapshot
```

写盘错误策略按游戏重要性设计，避免 UI/gameplay 半更新。

## Validation

覆盖：

- no save/new game;
- current + previous-version save;
- corrupted/partial file;
- missing/renamed IDs;
- empty/full inventory;
- stack split/merge boundary;
- unique/equipment state;
- scene reload;
- save after transaction;
- restart/settings/control persistence;
- procedural seed restore when used;
- migration after dependency changes when relevant.
