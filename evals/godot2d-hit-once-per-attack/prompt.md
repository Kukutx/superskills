---
description: godot-2d-game-development fixes multi-hit with an explicit per-attack contact policy, not a blanket cooldown
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

Godot 4.3 做 2D 横版动作，玩家攻击判定是 Area2D（Hitbox），攻击动画里用 AnimationPlayer 把 monitoring 打开 0.15 秒。问题是一刀会扣敌人好几次血。代码：

```gdscript
# hitbox.gd (挂在 Area2D 上)
extends Area2D
@export var damage := 10

func _physics_process(_delta):
    if not monitoring:
        return
    for area in get_overlapping_areas():
        if area.is_in_group("hurtbox"):
            area.owner.take_damage(damage)
```

我们有三段连击，三刀之间间隔很短（大概 0.2 秒），要求每一刀都能正常各打中一次。怎么改？
