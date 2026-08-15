# 2D Asset Pipeline Reference

用于 Godot 2D asset 的 source -> production -> import：sprites、FX、tiles、maps、props、UI art。

**不要在这里重复 spritesheet 生产。** 动作 strip、frame geometry、timing、anchor、切图/naming/packing -> `development/game-dev-spritesheet-slicer`；Godot runtime animation -> `animation-pixel.md`。

## 1. Production contract

进入游戏前明确相关项：

```text
editable source
size / world scale
alpha/background
anchor/pivot
naming
source vs derived ownership
import/filtering policy
animation metadata if applicable
```

“看起来好看”不等于 production-ready。

## 2. Choose pipeline by source type

### Generated/raster output

```text
approved visual
-> generate useful unit
-> deterministic cleanup/normalize
-> preview
-> import
```

模型负责视觉内容；exact crop/pad/alpha/scale/naming/packing 尽量程序化。

### Authored editable source

例如 `.aseprite` / Krita / Pixelorama：优先保留有价值的 layers、tags、durations、palette 和 anchor metadata。

不要先 flatten 掉 metadata，再在 Godot 手工维护第二份相同真源。

### Static image

Icon、portrait、prop、background 只做当前用途需要的 cleanup/import，不强行套 animation pipeline。

## 3. One editable source of truth

推荐：

```text
editable source
-> deterministic export/import
-> Godot-consumed derived asset
```

Generated side 如果可重建，不要同时和 source editor 双边手改同一事实。

引入 importer 前只问：

- 项目已有方案是否足够；
- Godot version 是否兼容；
- generated files 谁拥有；
- clean checkout 能否 re-import；
- 是否真的减少重复工作。

不要同时引入两个重叠 importer。

## 4. Asset-specific rules

### Pixel/raster

- consistent source resolution / scale policy；
- clean alpha；
- readable silhouette at actual size；
- deliberate filtering；
- avoid huge transparent bounds / accidental blur。

### FX

按 gameplay event 组织，明确 origin、direction、scale、lifetime、loop/one-shot。Runtime readability -> `rendering-vfx-shaders.md`。

### Maps / tiles

Visual 与 gameplay metadata 分开：collision、navigation、spawn、trigger、exit 不要永久烤进唯一背景图。地图 source ownership -> `world-tilemap-level-design.md`。

Tileset 要实际测试 corner、junction、terrain transition；showcase atlas 好看不代表能拼。

### Props

保持 world scale、ground anchor/y-sort baseline、合理 transparent bounds；collision/interactions 保持 Godot-side 明确。

### UI art

拆 reusable icons/panels/buttons/states；dynamic/localized text 不烤进普通 artwork；需要时使用合适 9-slice/StyleBox，而不是任意拉伸。

## 5. Deterministic post-process

能程序化就不要人工重复：

```text
crop/pad
alpha cleanup
explicit resize/scale
split/combine
naming
metadata conversion
preview/contact sheet
```

同一 approved source 应产生可预测 output。

概念上区分：

```text
editable source/reference
raw export/generated
normalized production
preview/debug
engine-consumed derived asset
```

不要覆盖唯一 approved source。

## 6. Godot handoff

确认 relevant subset：

- expected import type；
- filtering/mipmap/compression；
- scale/pivot/region；
- atlas/subresource ownership；
- re-import 不会破坏必要人工状态；
- paths/names case-correct；
- clean import succeeds。

## Validation

- final size/scale/anchor correct；
- alpha/bounds clean；
- source can regenerate derived output；
- no duplicate source of truth；
- animation metadata preserved when relevant；
- tiles/maps combine correctly；
- gameplay metadata remains editable；
- UI remains localization-ready；
- actual game resolution 下观感正确。
