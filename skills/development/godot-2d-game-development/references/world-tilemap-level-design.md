# World, TileMap and Level Design Reference

用于 TileMapLayer、TileSet、terrain、top-down depth、parallax、collision/navigation、room/level structure、external level authoring 和 2D level design。

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

## 2. Native Godot first

优先沿用当前项目已有 `TileMapLayer` / `TileSet` workflow。

适合 tiles：

- repeated ground/walls；
- terrain/autotile；
- simple decorations；
- tile collision/navigation metadata。

更适合独立 scene：

- doors/chests；
- NPC/enemy；
- breakables；
- animated gameplay props；
- pickups；
- complex hazards。

不要为了 external editor/addon 而把已经可维护的 native map pipeline 重做。

## 3. Choose one level-authoring source of truth

常见选择：

### Godot-native

适合：

- 团队主要在 Godot 内工作；
- TileMapLayer/TileSet 已满足需求；
- gameplay scene 与 map authoring 紧密结合。

### External level editor

例如项目已经使用 LDtk。此时 external source 可以是 level layout/content truth，再通过 importer 生成 Godot-side representation。

原则：

```text
editable source
-> deterministic importer
-> generated Godot map/scene
-> gameplay-specific runtime integration
```

不要同时手改 source editor 和 generated Godot representation，形成双真源。

`heygleeson/godot-ldtk-importer` 是 Godot 4 的可选 LDtk importer 候选；只有项目明确选择 LDtk 时才考虑，并先检查当前 Godot/LDtk compatibility。

## 4. Terrain authoring

先尝试当前 Godot TileSet terrain workflow。

如果 terrain painting/connection workflow 已成为持续且明确的制作瓶颈，可以评估 `Portponky/better-terrain` 这类 Godot 4 terrain addon。

选择规则：

```text
native terrain works -> stay native
terrain authoring is repeated production pain -> evaluate Better Terrain
project already has terrain addon -> keep one system
```

不要因为 addon 名字叫 “better” 就默认替换原生 terrain。

## 5. Tileset production

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

QA 不只看 atlas，要铺真实组合：

- corner；
- T-junction；
- corridor；
- isolated tile；
- terrain transitions。

## 6. Collision simplification

Collision 服务 gameplay，不是逐像素描边比赛。

- floor/wall silhouette 稳定；
- decorative bumps 不必全变 obstacle；
- top-down prop 用清楚 footprint；
- 避免细碎边缘造成 snag；
- generated/imported collision 必须实际走一遍，不盲信 importer。

## 7. Top-down draw order

明确：

- y-sort；
- floor/actor/foreground layers；
- prop ground anchor；
- tall prop foreground/occlusion。

角色在树/墙前后移动时，ground-contact point 比图片中心更适合作排序依据。

## 8. Parallax

Parallax 增加深度，不负责 gameplay truth。

检查：

- layer speed hierarchy；
- seamless edges；
- camera bounds；
- repeat；
- pixel filtering；
- motion noise/comfort。

## 9. Level design starts from gameplay

先 whitebox/simple tile：

```text
goal
-> route
-> challenge
-> recovery
-> reward/variation
```

高精美 art 不应过早锁死关卡结构。

## 10. Readability

玩家要快速看清：

- walkable/blocked；
- hazard；
- interactable；
- exit/path；
- enemy telegraph；
- foreground occlusion。

通过 shape/value/color/animation 建层级，不只靠文字。

## 11. Pacing

常见节奏：

```text
teach
-> test
-> vary
-> combine
-> relief/reward
```

动作关卡避免持续最大强度；探索关卡避免长时间无决策或信息。

## 12. Combat space

检查：

- player/enemy mobility；
- camera framing；
- projectile lanes；
- retreat space；
- obstacle readability；
- spawn fairness；
- telegraph visibility。

狭窄空间 + 大量敌人 + 强全屏 FX 会显著降低可读性。

## 13. Navigation handoff

如果使用 NavigationAgent2D：

- nav geometry 与地图同步；
- dynamic obstacle strategy 明确；
- spawn 不落不可达区域；
- agent radius 适合 corridor；
- imported/generated maps 更新后 nav 仍匹配。

导航细节读 `ai-navigation-procedural.md`。

## 14. Generated maps

AI/generative art 可做：

- visual concept；
- baked background；
- tileset/props source；
- reference layout。

生产 handoff 仍保留 editable：

- collision；
- spawn/exit markers；
- trigger zones；
- navigation；
- y-sort anchors；
- separated interactive props。

## 15. Chunking / streaming

只有世界规模真的需要再做。

先证明：

- simultaneously active node/tile count 是瓶颈；
- scene load 有可感知问题；
- 游戏确实需要 large-world/chunk lifecycle。

小型 2D 游戏不要预先造 streaming framework。

## 16. Source-control / generated map rule

External importer 产生的 Godot files 要明确：

- 是否 commit derived output；
- clean checkout 是否能 regenerate；
- CI 是否需要 importer/addon；
- generated file 是否允许手改。

不要出现“某个人电脑 import 过所以项目能开”的隐式依赖。

## Level QA

实际跑：

- spawn -> exit；
- alternate routes；
- dash/jump extremes；
- edge/corner collision；
- camera limits；
- y-sort crossings；
- enemy paths；
- triggers once/re-entry；
- unreachable reward；
- foreground visibility；
- terrain edge combinations；
- clean re-import if external authoring is used。

## Source synthesis

基于 Godot TileMapLayer/TileSet 与 official demos、Agent Sprite Forge editable-map handoff、Godot-specific skills/level-design principles，并加入 Better Terrain 与 LDtk importer 的明确适用边界。