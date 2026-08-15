# 2D Asset Pipeline Reference

用于生成、编辑、整理、导入 2D game assets：character sprites、animation strips、FX、tiles、maps、props、UI art。

核心原则：**先识别 source type，再选择 pipeline。** AI-generated PNG 与 `.aseprite`/Krita 等 authored source 不应走同一套流程。

## 1. Asset is a production contract

可用资产至少需要明确：

- dimensions / frame geometry；
- alpha/background policy；
- scale + anchor/pivot；
- source vs derived file；
- naming；
- timing/tags when animated；
- engine import settings；
- QA at actual in-game scale。

“看起来好看”不足以证明可用。

## 2. Identify source type

### A. AI-generated / rendered PNG

典型：single sprite、transparent strip、FX sheet、map image。

Pipeline：

```text
approved visual/reference
-> generate full useful unit (e.g. one action strip)
-> deterministic alpha cleanup
-> split/crop/pad
-> normalize shared scale/anchor
-> preview
-> Godot import
```

### B. Authored editable source

典型：`.aseprite`、LibreSprite、Krita、Pencil2D、Pixelorama 等。

优先保留：

- layers where useful；
- frame durations；
- animation tags；
- source canvas/anchor conventions；
- source file as truth。

不要先 flatten 成无 metadata PNG 再手工重建所有 timing，除非项目刻意选择这种 pipeline。

### C. Static production image

例如 icon、prop、portrait、background。只做当前用途需要的 cleanup/import，不强行转成 sprite-animation workflow。

## 3. Character animation

AI workflow：

1. approve one in-game seed frame；
2. lock silhouette/proportions/palette/outfit/weapon/facing；
3. generate one action strip at a time；
4. normalize shared frame size/scale/anchor；
5. preview motion；
6. import/package。

不要默认独立生成每帧。

Authored workflow：尽量从 source tags/timing 直接生成 Godot SpriteFrames/animation metadata，减少手工重复维护。

## 4. Aseprite / raster importer choice

如果项目有 authored source：

- Aseprite-centric -> 可评估 Aseprite Wizard；
- 多种 raster-animation editors -> 可评估 Importality；
- project 已有 importer -> 沿用它。

不要同时引入两个重叠 importer。

Importer 是 build/development pipeline dependency；升级 Godot 时要验证 importer compatibility 和 generated asset diffs。

## 5. Spritesheet contract

需要 conventional sheet 时定义：

```text
frame width/height
rows/columns
action order
direction order
frames per action
padding/spacing
anchor/baseline
timing metadata or sidecar source
```

具体切图/naming 用 `../game-dev-spritesheet-slicer/skill.md`。

## 6. Pixel-art rules

- crisp pixel clusters；
- consistent source resolution；
- readable silhouette at actual size；
- controlled palette/style；
- avoid accidental anti-alias blur；
- clean alpha；
- deliberate nearest/point filtering；
- consistent outline/lighting direction。

不要把高细节 AI illustration 伪装成低分辨率 production pixel sprite。

## 7. FX bundles

按 gameplay event 规划，而不是孤立漂亮图：

```text
cast/anticipation
projectile/trail
contact impact
residue/smoke if needed
UI icon only if gameplay needs one
```

每个 FX 有清楚 origin/anchor/direction policy。

## 8. Editable maps

把这些分开：

```text
ground/base
tiles
transparent props
collision
navigation/pathing
spawn points
triggers/zones
exits
foreground/occlusion
```

Generated map art 可以做 base/reference，但不要把 enemies/collision/triggers 永久烤进背景 PNG。

Godot 通常使用 TileMapLayer + reusable scenes/props + explicit gameplay metadata。

## 9. Tilesets

定义：

- tile size/atlas layout；
- terrain edges/corners；
- variants；
- animated tiles；
- collision/navigation policy；
- padding/spacing；
- lighting direction/palette。

必须测试真实组合；showcase sheet 好看不代表 tiles 能拼。

## 10. Props

- transparent PNG/source；
- stable ground anchor；
- consistent world scale；
- simplified collision；
- shadow policy；
- y-sort baseline for top-down；
- avoid huge empty transparent bounds。

## 11. UI art

拆分 reusable pieces：

```text
icons
panels/frames
buttons/states
badges
focus/cursor art
resource symbols
```

Dynamic/localized text 不烤进普通 UI artwork。

Pixel panels 考虑 9-slice/patch margins，不缩放破坏 corners。

## 12. Deterministic post-process

模型不擅长保证 exact geometry，能程序化就程序化：

- crop/pad；
- alpha cleanup；
- split/combine；
- shared scale；
- shared anchor；
- file naming；
- preview GIF/sheet；
- metadata extraction。

Creative generation 与 deterministic packaging 分工明确。

## 13. Source / derived folders

至少概念上区分：

```text
source/reference
raw generated/exported
normalized production
preview/debug
engine-consumed asset
```

不要覆盖唯一 approved source。

Git 是否提交 derived files 取决于项目 pipeline；不要无理由同时维护两套手工真源。

## 14. Godot handoff

验证：

- source/importer path correct；
- filtering/repeat settings；
- SpriteFrames/animation ranges；
- frame durations/tags preserved；
- scale/anchor；
- shared material/resource behavior；
- production scene 没引用 preview/raw temp file；
- clean checkout 能重新 import。

最后一条很重要：本机 import cache 正常不代表 CI/其他机器可重建。

## Asset QA

- art direction consistent；
- silhouette readable；
- scale/anchor stable；
- alpha clean；
- animation identity/timing stable；
- tiles connect；
- props y-sort correctly；
- FX 不盖 gameplay telegraph；
- UI art can scale/layout；
- clean Godot import succeeds；
- in-engine result matches preview。

## Source synthesis

结合 Agent Sprite Forge、OpenAI sprite-pipeline、Aseprite workflow、Aseprite Wizard/Importality 与 Godot import principles。关键不是绑定某个工具，而是根据 source type 走可重建、可验证的生产流程。