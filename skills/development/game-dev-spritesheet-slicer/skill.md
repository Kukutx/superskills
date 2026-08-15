---
name: game-dev-spritesheet-slicer
description: Production router for 2D/pixel-art animation strips and spritesheets: frame contracts, generated-strip planning, normalization, deterministic slicing, timing metadata, naming and engine handoff.
---

# Game Dev Spritesheet Slicer

把角色/动作素材变成 **可切、可预览、可导入游戏** 的 production asset。

## Scope

Use when the main problem is:

- sprite / animation strip planning;
- exact frame geometry;
- action/direction layout;
- generated animation consistency;
- scale/anchor normalization;
- slicing/naming/packing;
- timing/tag metadata;
- Godot SpriteFrames or other 2D-engine handoff.

如果核心问题是 Godot gameplay、combat、state 或 animation implementation，以 `development/godot-2d-game-development` 为主；本 Skill 只负责 asset contract/subtask。

## Progressive routing

| Need | Load |
| --- | --- |
| generate/plan new action strips, seed-frame consistency, directions | `references/generation.md` |
| slice/normalize/name/pack/import existing strips or sheets | `references/packaging.md` |
| generate then package | both, in that order |

不要因为出现 “spritesheet” 就自动加载两个 reference。

## Required contract

只在缺失会明显改变结果时询问，否则合理默认。

| Field | Default |
| --- | --- |
| perspective | side-view |
| frame size | 64x64 |
| anchor | bottom-center / feet |
| background | transparent |
| actions | infer from task |
| direction | 1 |
| output | PNG strips + optional packed sheet |
| filtering | pixel project -> nearest/point |

Frame count **按动作决定**，不要所有动作固定相同帧数。

## Core invariants

```text
exact frame contract
+ stable identity/proportions when generated
+ shared canvas/scale/anchor
+ explicit action/direction order
+ timing separate from geometry
+ deterministic slicing/naming
+ preview before production overwrite/import
```

## High-level workflow

### New generated animation

```text
approve seed
-> plan one action/direction
-> generate strip
-> normalize
-> preview
-> package/import
```

详细规则读 `references/generation.md`，然后按需读 `references/packaging.md`。

### Existing sheet/strip

```text
inspect geometry
-> define exact slice contract
-> normalize if needed
-> deterministic split/pack
-> preserve timing metadata
-> preview
-> engine handoff
```

只读 `references/packaging.md`。

## Output

按任务只输出需要的部分，通常包括：

1. Asset/frame spec
2. Action/direction plan when relevant
3. Generation prompt when relevant
4. Strip/sheet layout
5. Timing/loop metadata
6. Slice/pack config
7. Naming
8. Engine import notes
9. QA

不要为了填模板输出无关 section。

## Hard constraints

- 不把自由排版角色概念图冒充可切 spritesheet。
- 不默认巨型 multi-action sheet 是最佳生成方式。
- 不逐帧独立生成同一 action，除非明确接受 drift。
- 不让同一角色不同 frame 使用不一致 scale/anchor。
- 不把 labels/scenery/watermark 混入 production sheet。
- 不用 blank/duplicate frame 掩盖未知 layout。
- 不让 art sheet 自己决定 combat damage timing。
- 不在未预览/验证前覆盖唯一 approved source/production asset。

## Minimum QA

确认：

- exact frame count/geometry;
- stable anchor and apparent scale;
- correct action/direction order;
- clean transparency;
- deterministic names/files;
- timing metadata matches frames;
- action reads at actual game size;
- preview correct before engine import.
