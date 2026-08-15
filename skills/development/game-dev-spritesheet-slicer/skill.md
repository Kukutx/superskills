---
name: game-dev-spritesheet-slicer
description: Production workflow for planning, generating, normalizing, slicing and naming 2D/pixel-art animation strips and spritesheets for Godot or other 2D engines. Use when exact frame geometry, action/direction layout, anchor consistency, timing metadata, export or slicing is the main task.
---

# Game Dev Spritesheet Slicer Skill

## Status

- Version: v0.2
- Category: `development`
- Maturity: `production-oriented`
- Owner: `Kukutx`
- Last updated: 2026-08-15

## Purpose

把角色/动作素材变成 **可切、可预览、可导入游戏** 的 spritesheet/animation strip。

重点不是“一张很酷的大图”，而是：

```text
consistent character
+ exact frame contract
+ stable scale/anchor
+ predictable timing
+ deterministic slicing
+ engine-ready output
```

## When to use

- sprite / animation strip；
- idle/walk/run/attack/hurt/death；
- 4/8-direction character；
- exact frame size；
- sheet row/column；
- slicing/naming；
- Aseprite tags/timing；
- Godot SpriteFrames import contract。

如果任务还包含 Godot gameplay/animation/combat implementation，以 `development/godot-2d-game-development` 为主。

## Core principle: approve one frame first

AI/generative workflow 优先：

1. approve one in-game seed frame；
2. lock identity/proportions/palette/outfit/weapon；
3. generate **one action strip at a time** when possible；
4. normalize all frames；
5. package sheets only after strips are stable。

不要默认一次生成“所有动作 × 所有方向”的巨型表。
巨型表更容易出现 identity drift、错格和 frame inconsistency。

## Required contract

只在缺失会明显影响结果时询问；否则合理默认继续。

| Field | Default |
| --- | --- |
| perspective | side-view |
| frame size | 64x64 |
| anchor | bottom-center / feet |
| background | transparent |
| actions | idle, walk/run, attack, hurt, death |
| direction | 1 |
| output | PNG strips + optional packed sheet |
| filtering | pixel project -> nearest/point |

Frame count **按动作决定**，不要所有动作固定 6 帧。

## Action planning

Typical ranges are starting points only:

| Action | Typical frames | Timing idea |
| --- | --- | --- |
| idle | 2–4 | slow / variable |
| walk | 4–8 | even rhythm |
| run | 4–8 | faster, larger poses |
| attack | 3–8 | anticipation -> impact -> recovery |
| hurt | 2–5 | fast impact + recover |
| death | 4–10 | readable one-shot |
| dash | 2–6 | strong direction/readability |

Quality depends more on strong key poses + timing than raw frame count.

## Direction policy

For top-down:

- define 4 or 8 directions；
- state which directions may be mirrored；
- asymmetric weapon/outfit may require unique art；
- keep anchor/apparent scale consistent across directions；
- naming includes direction。

Example:

```text
player_run_n_00.png
player_run_e_00.png
player_run_s_00.png
player_run_w_00.png
```

## Generation prompt contract

Every prompt must state:

- same character；
- same proportions；
- same outfit/equipment；
- same palette；
- same facing direction for this strip；
- transparent background；
- exact number of frames；
- fixed slots/frame size target；
- no labels/scenery/watermark；
- readable silhouette；
- crisp pixel clusters for pixel art；
- production game asset, not concept sheet。

## Whole-strip workflow

```text
approved seed
-> reference canvas/layout guide if needed
-> one full action strip generation
-> cleanup alpha
-> split frames
-> normalize shared scale
-> align shared anchor
-> optionally lock frame 1 to seed
-> preview GIF/sheet
-> approve
-> package/import
```

Independent frame-by-frame generation is fallback only.

## Normalization

All frames of one character set should share:

- frame canvas size；
- scale；
- anchor；
- baseline；
- direction convention；
- transparent padding policy。

Do not crop every frame tightly to different bounds and then expect stable animation.

## Timing metadata

Spritesheet geometry 与 timing 是两件事。

记录：

- frame duration；
- loop/ping-pong/one-shot；
- hold frames；
- animation tag/range。

如果工具支持 Aseprite tags/JSON，保留 metadata。
Godot import 时不要靠手工记忆 action range。

## Sheet packaging

当 individual strips 已批准后，再决定：

### Per-action strips

Best when:

- pipeline likes simple imports；
- actions have different frame counts；
- iteration frequent。

### Combined grid

Best when:

- engine/tooling expects one atlas；
- layout is stable；
- exact metadata exists。

Combined sheet must define:

```text
frameWidth
frameHeight
rows
columns
row/action order
direction order
frames valid per row
padding
spacing
anchor
```

不要用 blank/duplicate frame 隐藏未知 layout。

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

## Godot handoff

确认：

- import filter/mipmap policy；
- SpriteFrames animation names；
- loop policy；
- per-frame speed/duration；
- anchor/pivot；
- animation state names match gameplay convention；
- attack frame event/hitbox timing separately configured when needed。

Art sheet 不应该自己决定 combat damage timing；它提供可对齐的 frames/tags。

## QA

检查：

- identity stable；
- proportions stable；
- same ground anchor；
- no foot sliding caused by crop；
- weapon does not morph；
- correct direction；
- correct frame count；
- clean transparency；
- no text/watermark；
- action reads at actual game size；
- loop seam clean；
- impact pose clear；
- deterministic slicer produces expected files；
- preview looks correct before engine import。

## Output contract

默认：

1. Asset spec
2. Action/direction plan
3. Generation prompt
4. Strip/sheet layout
5. Timing/loop metadata
6. Slice config
7. Naming
8. Godot/engine import notes
9. QA

## Example slice config

```json
{
  "frameWidth": 64,
  "frameHeight": 64,
  "anchor": "bottom-center",
  "background": "transparent",
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

## Hard constraints

- 不输出无法切分的自由排版角色图当作 spritesheet。
- 不默认每个动作相同帧数。
- 不默认巨型多动作 sheet 是最佳生成方式。
- 不逐帧独立生成同一 action，除非接受 drift。
- 不让不同 frame 使用不同 scale/anchor。
- 不把 dynamic labels/background scene 混入 sheet。
- 不在未预览动画前直接覆盖 production asset。
- 不把 tool-specific capability 当作所有环境都存在。

## Source synthesis

核心吸收 OpenAI `sprite-pipeline` 的 seed/whole-strip/normalize/preview、Aseprite pixel animation 的 timing/tag concepts，以及 Agent Sprite Forge 的 deterministic cleanup/game-ready handoff。
