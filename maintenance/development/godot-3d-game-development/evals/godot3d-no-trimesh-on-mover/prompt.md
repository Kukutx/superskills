---
description: godot-3d-game-development flags concave/trimesh collision on a moving body
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

Godot 4.2，第三人称 3D 游戏。玩家是 CharacterBody3D，碰撞形状是我在角色模型的 MeshInstance3D 上点「Mesh > Create Trimesh Collision Sibling」生成的，再把那个 CollisionShape3D 挪到 CharacterBody3D 下面用。地图是 GridMap + StaticBody3D。

现在的问题：角色走到台阶和墙角经常卡住或者抖，偶尔还会穿进墙里。移动用的是 velocity + move_and_slide()，physics ticks 是默认 60。我试过把 physics ticks 调到 120，好一点但还是有。怎么彻底解决？
