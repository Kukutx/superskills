---
description: godot-project-systems saves stable item IDs, not display names, and migrates old saves
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

Godot 4.3 GDScript 项目，已经上线了 Steam 抢先体验，有玩家存档了。现在要做英文/日文本地化，策划还想把几个物品改名（比如"小血瓶"改成"初级治疗药水"）。

现在的存档代码：

```gdscript
func save_inventory() -> Dictionary:
    var items := []
    for item in inventory.items:   # item 是 ItemData (Resource)，有 display_name、icon、max_stack
        items.append({"name": item.display_name, "count": item.count})
    return {"items": items}

func load_inventory(data: Dictionary) -> void:
    for entry in data["items"]:
        var item := ItemDB.find_by_name(entry["name"])
        inventory.add(item, entry["count"])
```

改名和本地化之后读档应该怎么改？
