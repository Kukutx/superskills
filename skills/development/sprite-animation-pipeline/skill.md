---
name: sprite-animation-pipeline
description: Produce game-ready 2D/pixel-art sprite animations from seed/reference assets or existing sheets, with stable frame contracts, deterministic slicing/normalization, timing metadata and engine handoff.
---

# Sprite Animation Pipeline

Use when the main problem is **sprite animation asset production**, not engine gameplay/runtime logic.

## Scope

Owns:

- seed/reference -> action strip planning;
- identity/proportion consistency across generated frames;
- exact frame geometry, scale and anchor;
- direction/action layout;
- deterministic slicing, naming and packing;
- timing/tag metadata;
- preview and engine-ready handoff.

Godot gameplay/state/combat/runtime animation remains owned by `development/godot-2d-game-development`.

## Progressive routing

| Need | Load |
| --- | --- |
| create/plan a new action strip or directional set | `references/generation.md` |
| normalize/slice/name/pack an existing strip or sheet | `references/packaging.md` |
| generate then package | both, in that order |

Do not load both references merely because the word “spritesheet” appears.

## Asset contract

Only ask for missing details when they materially change the result. Reasonable defaults are acceptable.

```text
perspective
frame size
anchor/baseline
background/alpha
actions
directions
output layout
filtering/import target
```

Frame count is action-dependent; do not force every action to the same count.

## Invariants

```text
stable identity/proportions
+ exact frame geometry
+ shared scale/anchor
+ explicit action/direction order
+ timing separate from geometry
+ deterministic outputs
+ preview before production overwrite/import
```

## Workflow

### New animation

```text
approve one seed/reference
-> plan one action/direction
-> generate a coherent strip
-> normalize shared scale/anchor
-> preview motion
-> package/import
```

### Existing sheet

```text
inspect real geometry
-> define slice contract
-> normalize only if needed
-> deterministic split/pack
-> preserve timing/tags
-> preview
-> engine handoff
```

## Boundaries

- Art assets can expose frame/timing events; gameplay systems still own damage/state truth.
- If editable source already owns tags/durations, preserve that metadata instead of rebuilding a second truth manually.
- If the visual style/concept itself is unresolved, a visual-direction Skill may assist, but this pipeline owns production geometry and consistency.
- Do not patch a bad source contract with engine-side magic offsets.

## Hard constraints

- Do not present a concept sheet/free layout as a sliceable production sheet.
- Do not default to one giant all-actions/all-directions generation request.
- Do not independently generate every frame of one action unless drift is explicitly acceptable.
- Do not vary apparent scale/anchor across frames of the same character set.
- Do not mix labels, scenery or watermark into production frames.
- Do not guess unknown layout using blank/duplicate frames.
- Do not overwrite the only approved source before preview/validation.

## Minimum QA

Verify the relevant subset:

- exact frame count and geometry;
- stable identity, apparent scale and ground anchor;
- correct action/direction order;
- clean transparency;
- deterministic names/files;
- timing metadata matches frame ranges;
- action reads at actual game size;
- preview is correct before engine import.
