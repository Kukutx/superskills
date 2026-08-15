# 2D Asset Pipeline Reference

用于生成、编辑、整理和导入 Godot 2D assets：sprites、FX、tiles、maps、props、UI art，以及 editable source -> engine asset 的 handoff。

**Exact animation-strip generation/slicing 不在这里重复维护。** 角色动作 strip、frame geometry、timing、shared anchor、naming/packing 请用 `development/game-dev-spritesheet-slicer`；Godot runtime animation 读 `animation-pixel.md`。

## 1. Asset is a production contract

可用资产至少需要明确相关项：

- source type / editable source;
- dimensions / world scale;
- alpha/background policy;
- anchor/pivot;
- naming;
- source vs derived ownership;
- import/filtering settings;
- metadata when animated;
- QA at actual in-game scale.

“看起来好看”不足以证明能进入游戏。

## 2. Identify the source type first

### Generated/raster output

例如 transparent PNG、FX sheet、map concept、prop/icon。

```text
approved visual intent
-> generate/render useful unit
-> deterministic cleanup
-> normalize production geometry
-> preview
-> import
```

模型负责创意像素/图像，程序化步骤负责 exact crop/pad/alpha/naming/packing。

### Authored editable source

例如 `.aseprite`、Krita、LibreSprite、Pixelorama 等。

尽量保留 source 中真正有价值的信息：

- layers;
- tags;
- frame durations;
- palette/source resolution;
- anchor conventions.

不要先 flatten 掉 metadata，再在 Godot 手工维护第二份相同真源，除非项目明确选择这种 pipeline。

### Static production image

例如 icon、portrait、prop、background。只做当前用途需要的 cleanup/import，不强行转成 animation workflow。

## 3. Choose one editable source of truth

明确哪一侧允许人工编辑：

```text
editable source
-> deterministic export/import
-> Godot-consumed derived asset
```

如果 derived Godot file 可以重新生成，通常不要同时在 source editor 和 generated side 手改同一事实。

需要 external importer 时先检查：

- 项目是否已经有 importer;
- 当前 Godot version compatibility;
- generated-file ownership;
- clean checkout/re-import behavior;
- 是否真的减少手工重复.

不要同时引入两个重叠 importer。

## 4. Pixel/raster production rules

- consistent source resolution and scale policy;
- clean alpha;
- readable silhouette at actual size;
- deliberate nearest/point filtering where appropriate;
- avoid accidental anti-alias blur;
- stable palette/light direction when the art style depends on them;
- avoid huge transparent bounds.

不要把高细节 illustration 仅靠缩小/nearest filtering 就当成 production pixel art。

## 5. FX assets

按 gameplay event 组织，而不是孤立生成漂亮图：

```text
cast / anticipation
projectile / trail
contact impact
residue / smoke when needed
```

每类 FX 明确：

- origin/anchor;
- direction;
- scale;
- loop/one-shot;
- expected lifetime;
- whether color/tint is runtime-driven.

VFX runtime/readability 读 `rendering-vfx-shaders.md`。

## 6. Editable maps/world art

把 visual layer 与 gameplay metadata 分开：

```text
ground/base
decoration
foreground/occlusion
collision
navigation
spawn points
triggers/exits
interactive props
```

Generated map art 可以做 base/reference，但 enemies、collision、triggers 不要永久烤进唯一背景 PNG。

地图 authoring/source-of-truth 细节读 `world-tilemap-level-design.md`。

## 7. Tilesets

定义并实际测试：

- tile size / atlas layout;
- terrain edges/corners;
- variants;
- animated tiles if used;
- collision/navigation policy;
- spacing/padding;
- palette/lighting direction.

Showcase sheet 能看不代表真实 corner/T-junction/transition 能拼。

## 8. Props

- stable ground anchor;
- consistent world scale;
- transparent bounds kept reasonable;
- simplified collision footprint;
- shadow policy;
- top-down y-sort baseline when relevant;
- interaction/collision stays explicit in Godot rather than hidden in art.

## 9. UI art

拆成 reusable pieces：

```text
icons
panels/frames
buttons/states
badges
focus/cursor art
resource symbols
```

Dynamic/localized text 不烤进普通 UI artwork。

Pixel panel/corners 需要时使用合适的 9-slice/StyleBox policy，而不是任意缩放破坏边缘。

## 10. Deterministic post-process

能稳定程序化的步骤尽量不要靠人工重复：

- crop/pad;
- alpha cleanup;
- resize under explicit scale policy;
- split/combine;
- naming;
- metadata extraction/conversion;
- atlas/contact sheet/preview generation.

同一 approved source 应能产生可预测的 derived output。

## 11. Source / derived folders

至少概念上区分：

```text
editable source/reference
raw generated/exported
normalized production
preview/debug
gine-consumed derived asset
```

不要覆盖唯一 approved source。是否 commit derived files 由项目 pipeline 决定，但必须能说明 clean checkout 如何恢复 engine-consumed assets。

## 12. Godot import handoff

相关资产进入 Godot 后确认：

- expected import type;
- filtering/mipmap/compression policy;
- scale/pivot/region settings;
- atlas/subresource ownership;
- source re-import does not silently destroy required manual state;
- file names/paths are stable and case-correct;
- clean project import succeeds.

## Validation

按资产类型检查 relevant subset：

- final size/scale/anchor correct;
- alpha/bounds clean;
- source can regenerate derived asset;
- re-import works from clean state;
- no duplicate source of truth;
- animation metadata preserved when applicable;
- tiles/maps combine correctly;
- collision/navigation/spawns remain editable gameplay data;
- UI text/layout remains localization-ready;
- asset looks correct at actual game resolution, not only zoomed-in preview.
