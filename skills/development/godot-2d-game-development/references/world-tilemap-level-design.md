# World, TileMap and Level Design Reference

用于 TileMapLayer、tileset、top-down depth、parallax、collision/navigation、room/level structure 和 2D level design。

## 1. Separate visual world from gameplay metadata

地图至少区分：

```text
ground/background
decorative tiles
foreground/occlusion
collision
navigation
interactables
spawn points
triggers
exits
```

它们可以共享 authoring source，但不要让一张背景 PNG 成为 collision/spawn/trigger 的唯一真源。

## 2. TileMapLayer usage

优先沿用当前 Godot 4 项目的 `TileMapLayer` / `TileSet` workflow。

适合 tiles 的：

- repeated ground/walls；
- terrain/autotile；
- simple decorations；
- tile collision/navigation metadata。

更适合独立 scene 的：

- doors；
- chests；
- NPC/enemy；
- breakables；
- animated gameplay props；
- pickups；
- complex hazards。

## 3. Tileset production

定义：

- tile size；
- atlas grid；
- terrain edge/corner rules；
- collision；
- navigation；
- variants；
- animated tile rules；
- spacing/padding；
- palette/light direction。

QA 不只看 atlas，要在真实组合里铺：

- corner；
- T-junction；
- corridor；
- isolated tile；
- transition between terrains。

## 4. Collision simplification

Collision 服务 gameplay，不是逐像素描边比赛。

- floor/wall silhouette 尽量稳定；
- decorative bumps 不必全部变 physics obstacle；
- top-down prop 可用简单 blocking footprint；
- floor collision 尽量避免细碎边缘造成 snag。

## 5. Top-down draw order

明确 depth policy：

- y-sort；
- separate floor/actor/foreground layers；
- prop ground anchor；
- tall prop foreground/occlusion。

角色在树/墙前后移动时，ground contact point 才是排序关键，不是图片中心。

## 6. Parallax

Parallax 用于增加深度，不负责 gameplay truth。

检查：

- layer speed hierarchy；
- seamless edges；
- camera bounds；
- texture repeat；
- pixel art filtering；
- 运动速度不会产生眩晕/过度噪声。

## 7. Level design starts from gameplay

先白盒/简单 tile：

```text
goal
-> route
-> challenge
-> recovery
-> reward/variation
```

不要先用高精美地图锁死关卡结构。

## 8. Readability

玩家需要看清：

- walkable vs blocked；
- hazard；
- interactable；
- exit/path；
- enemy telegraph；
- foreground that can obscure player。

用 shape/value/color/animation 建立层级，不只靠文字提示。

## 9. Pacing

常见节奏：

```text
teach
-> test
-> vary
-> combine
-> relief/reward
```

动作关卡避免持续最大强度。
探索关卡避免长时间没有决策或信息。

## 10. Combat space

检查：

- player/enemy mobility；
- camera framing；
- projectile lanes；
- retreat space；
- obstacle readability；
- spawn fairness；
- telegraph visibility。

狭窄空间 + 大量敌人 + 强屏幕特效会显著降低可读性。

## 11. Navigation handoff

如果敌人使用 NavigationAgent2D：

- nav geometry 与视觉地图同步；
- dynamic obstacle strategy 明确；
- spawn 不落在不可达区域；
- agent radius/avoidance 适合 corridor width。

导航细节转 `ai-navigation-procedural.md`。

## 12. Generated maps

AI/generative art 可用于：

- visual concept；
- baked background；
- tileset/props source；
- reference layout。

生产 handoff 仍要保留：

- editable collision；
- spawn/exit markers；
- trigger zones；
- navigation；
- y-sort anchors；
- separated props when interaction requires。

## 13. Chunking / streaming

只有世界规模真的需要时再 chunk。

先问：

- 同时可见 tile/node 数是否已经成为瓶颈？
- scene load 是否明显卡顿？
- 是否需要开放世界/大地图？

小型 2D 游戏不要预先造 streaming framework。

## 14. Level QA

实际跑：

- 从出生点到出口；
- 所有路线；
- dash/jump extremes；
- edge/corner collision；
- camera limits；
- y-sort crossings；
- enemy path；
- trigger once/re-entry；
- no accidental unreachable reward；
- no foreground permanently blocking important action。

## Source synthesis

主要吸收 Agent Sprite Forge 的 editable map handoff、GD-Agentic-Skills 的 TileMap mastery、GodotPrompter 2D essentials，以及 awesome-gamedev-agent-skills 的 level-design principles。
