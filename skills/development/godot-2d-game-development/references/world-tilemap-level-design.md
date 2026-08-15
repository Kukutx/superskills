# World, TileMap and Level Design Reference

用于 TileMapLayer、TileSet、terrain、top-down depth、parallax、collision/navigation、room/level structure、external level authoring 和 2D level design。

## Separate visual world from gameplay metadata

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

它们可以共享 authoring source，但不要让背景 PNG 成为 collision/spawn/trigger 的唯一真源。

## Native Godot first

优先沿用当前项目已有 `TileMapLayer` / `TileSet` workflow。

Tiles 适合 repeated ground/walls、terrain、simple decoration 和 tile metadata；doors/chests/NPC/enemy/breakables/pickups/complex hazards 更适合独立 scene。

不要为了 external editor/addon 重做已经可维护的 native pipeline。

## One authoring source of truth

### Godot-native

适合团队主要在 Godot 内工作且 TileMapLayer/TileSet 已满足需求。

### External level editor

如果项目已经明确使用外部 editor，则让它成为 layout/content truth，再 deterministic import 到 Godot：

```text
editable source
-> deterministic importer
-> generated Godot representation
-> gameplay-specific runtime integration
```

不要同时手改 editable source 和 generated Godot output。

需要 importer 时，按项目实际 editor + Godot version 重新验证当前 maintained option；不要在 runtime Skill 固定某个第三方插件。

## Terrain authoring

先使用当前 Godot TileSet terrain workflow。

只有 terrain painting/connection 已成为持续 production bottleneck 时，才评估额外 terrain tooling。

```text
native terrain works -> keep native
repeated authoring pain -> evaluate alternative tooling
project already has terrain tooling -> keep one source of truth
```

## Tileset production

定义：tile size、atlas grid、terrain edges/corners、collision、navigation、variants、animated tile rules、spacing/padding 和 palette/light direction。

QA 必须铺真实组合：corner、T-junction、corridor、isolated tile、terrain transitions。

## Collision simplification

Collision 服务 gameplay，不是逐像素描边。

- floor/wall silhouette 稳定；
- decorative bumps 不必全变 obstacle；
- top-down prop 使用清楚 footprint；
- 避免碎边造成 snag；
- imported/generated collision 必须实际走一遍。

## Top-down draw order

明确 y-sort、floor/actor/foreground layers、prop ground anchor 和 tall-prop occlusion。

ground-contact point 通常比图片中心更适合排序。

## Parallax

Parallax 只负责 presentation。检查 layer speed hierarchy、seam、camera bounds、repeat、filtering 和 motion comfort。

## Level design starts from gameplay

先 whitebox：

```text
goal
-> route
-> challenge
-> recovery
-> reward/variation
```

不要让高精美 art 过早锁死关卡结构。

## Readability and pacing

玩家要快速看清 walkable/blocked、hazard、interactable、exit/path、enemy telegraph 和 foreground occlusion。

常见节奏：

```text
teach -> test -> vary -> combine -> relief/reward
```

## Combat space

检查 player/enemy mobility、camera framing、projectile lanes、retreat space、obstacle readability、spawn fairness 和 telegraph visibility。

## Navigation handoff

如果使用 NavigationAgent2D：

- nav geometry 与地图同步；
- dynamic obstacle strategy 明确；
- spawn 不落不可达区域；
- agent radius 适合 corridor；
- re-import 后 nav 仍匹配。

导航细节见 `ai-navigation-procedural.md`。

## Generated maps

Generative art 可以做 visual concept、baked background、tileset/props source 或 reference layout。

生产 handoff 仍保留 editable collision、spawn/exit markers、trigger zones、navigation、y-sort anchors 和 separated interactive props。

## Chunking / streaming

只有规模真正需要时再做。先证明 active world size 或 scene load 已经是实际瓶颈。

## Generated-file rule

External importer 产生的 Godot files 要明确：

- 是否 commit derived output；
- clean checkout 是否能 regenerate；
- CI 是否需要 importer；
- generated file 是否允许手改。

不要依赖“某台电脑之前 import 过”的隐式状态。

## Level QA

实际跑：

- spawn -> exit / alternate route;
- movement extremes;
- edge/corner collision;
- camera limits;
- y-sort crossings;
- enemy paths;
- trigger re-entry;
- unreachable rewards;
- foreground visibility;
- terrain edge combinations;
- clean re-import when external authoring is used.
