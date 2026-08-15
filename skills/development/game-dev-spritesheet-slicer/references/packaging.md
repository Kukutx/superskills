# Spritesheet Packaging Reference

用于已有 strips/sheets 的 normalization、deterministic slicing、metadata、naming、packing 和 engine handoff。需要生成新动作素材时配合 `generation.md`。

## Geometry contract

切图前必须知道：

```text
frameWidth
frameHeight
rows
columns
row/action order
direction order
valid frames per row
padding
spacing
anchor/baseline
```

未知 geometry 不要靠 blank/duplicate frames 猜。

## Normalize before final package

同一角色 set 统一：

- canvas size;
- apparent scale;
- anchor;
- baseline;
- transparent padding;
- direction convention.

Cropping 可以用于检测 bounds，但最终 frame canvas 应保持稳定，否则会造成 foot sliding / sprite jitter。

## Per-action strips vs combined grid

### Per-action strips

适合：

- actions frame count 不同;
- iteration frequent;
- engine/import pipeline 支持独立 animations;
- 希望 diff/re-export 更简单。

### Combined grid

适合：

- downstream tooling 明确要求 atlas;
- layout 已稳定;
- metadata 精确记录 row/action/direction/frame count.

不要为了“看起来像 spritesheet”强行合并所有素材。

## Timing metadata

Sheet geometry 与 animation timing 分开保存。

至少记录：

- frame duration or FPS policy;
- loop / ping-pong / one-shot;
- valid range/tag;
- intentional hold frames.

如果 source tool 有 tags/JSON/sidecar metadata，优先 deterministic 转换；不要靠人工记住 range。

## Naming

Prefer:

```text
{character}_{action}_{direction?}_{frame:02}.png
```

Examples:

```text
hero_idle_00.png
hero_attack_light_03.png
slime_hurt_01.png
knight_run_n_05.png
```

Names 应稳定、可排序、可由脚本生成。

## Example slice config

```json
{
  "frameWidth": 64,
  "frameHeight": 64,
  "anchor": "bottom-center",
  "padding": 0,
  "spacing": 0,
  "actions": {
    "idle": {"frames": 4, "loop": true},
    "run": {"frames": 6, "loop": true},
    "attack_light": {"frames": 6, "loop": false},
    "hurt": {"frames": 3, "loop": false}
  },
  "naming": "{character}_{action}_{frame:02}.png"
}
```

实际 config 要反映真实 sheet，不要用默认值覆盖未知信息。

## Deterministic operations

能程序化就不要人工重复：

- split by exact grid;
- crop detection + fixed-canvas padding;
- alpha cleanup;
- shared scale/anchor alignment;
- rename;
- pack atlas;
- generate metadata;
- preview GIF/contact sheet.

同一输入应产生同一输出。

## Godot handoff

确认：

- import filtering/mipmap policy;
- SpriteFrames animation names;
- loop policy;
- per-frame speed/duration;
- anchor/pivot;
- animation state names match gameplay convention;
- attack/hitbox event timing 由 gameplay/animation system 单独配置。

Art package 提供 frame/timing contract，但不自己决定 damage truth。

其他 2D engine 同理：把 geometry、timing、pivot 和 naming 显式交付，不依赖编辑器中的隐式人工状态。

## Packaging QA

- expected file count;
- correct rows/columns/action ranges;
- clean transparency;
- same frame canvas;
- same ground anchor;
- no crop-induced foot sliding;
- correct direction/order;
- naming deterministic;
- metadata matches files;
- loop/one-shot flags correct;
- preview looks correct before engine import;
- re-running slicer does not unexpectedly change approved output.

不要在未预览前直接覆盖唯一 production asset/source。
