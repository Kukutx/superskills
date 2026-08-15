# 2D Asset Pipeline Reference

用于生成、编辑、整理、导入 2D game assets：character sprites、animation strips、FX、tiles、maps、props、UI art。

核心原则：**先识别 source type，再选择 pipeline。** AI-generated PNG 与 authored editable source 不应走同一套流程。

## Asset is a production contract

至少明确：

- dimensions / frame geometry;
- alpha/background policy;
- scale + anchor/pivot;
- source vs derived file;
- naming;
- timing/tags when animated;
- engine import settings;
- QA at actual in-game scale.

“看起来好看”不足以证明可用。

## Source types

### AI-generated / rendered PNG

```text
approved visual/reference
-> generate full useful unit
-> deterministic alpha cleanup
-> split/crop/pad
-> normalize shared scale/anchor
-> preview
-> Godot import
```

### Authored editable source

例如 pixel/raster editor source。优先保留 layers、frame durations、animation tags、canvas/anchor conventions，并让 editable source 保持 truth。

不要 flatten 后再手工重建 metadata，除非项目刻意采用这种 pipeline。

### Static production image

Icon、prop、portrait、background 只做当前用途需要的 cleanup/import，不强行转成 animation workflow。

## Character animation

AI workflow：

1. approve one in-game seed frame;
2. lock silhouette/proportions/palette/outfit/weapon/facing;
3. generate one action strip at a time;
4. normalize shared frame size/scale/anchor;
5. preview motion;
6. import/package.

不要默认独立生成每帧。

Authored workflow：尽量保留 source tags/timing 并 deterministic 导出，减少手工重复维护。

如果项目需要 importer，优先沿用已有 pipeline；新增 importer 前按主 Skill dependency rule 验证当前 Godot/source-editor compatibility 和 generated-file ownership。不要同时维护两套重叠 importer。

## Spritesheet contract

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

具体切图/naming 使用 `../../game-dev-spritesheet-slicer/skill.md`。

## Pixel-art rules

- crisp pixel clusters;
- consistent source resolution;
- readable silhouette at actual size;
- controlled palette/style;
- clean alpha;
- deliberate nearest/point filtering;
- consistent outline/lighting direction.

不要把高细节 illustration 仅靠缩小伪装成 production pixel sprite。

## FX bundles

围绕 gameplay event 规划：

```text
cast/anticipation
projectile/trail
contact impact
residue/smoke if needed
```

每个 FX 明确 origin/anchor/direction policy。

## Editable maps

分开：

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

## Tilesets / props / UI

Tileset 定义 tile size、atlas、terrain rules、variants、collision/navigation、padding/spacing 和 lighting direction，并测试真实组合。

Props 保持 transparent source、stable ground anchor、consistent world scale、simple collision 和合理 bounds。

UI art 拆成 reusable pieces；dynamic/localized text 不烤进普通 artwork；pixel panel 需要明确 9-slice/patch margins。

## Deterministic post-process

模型不擅长保证 exact geometry。能程序化就程序化：

- crop/pad;
- alpha cleanup;
- split/combine;
- shared scale/anchor;
- file naming;
- preview;
- metadata extraction.

Creative generation 与 deterministic packaging 分工明确。

## Source / derived ownership

至少概念上区分：

```text
source/reference
raw generated/exported
normalized production
preview/debug
engine-consumed asset
```

不要覆盖唯一 approved source，也不要无理由维护两套手工真源。
