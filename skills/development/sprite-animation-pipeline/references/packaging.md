# Sprite Packaging Reference

Use for normalization, deterministic slicing, metadata, naming, packing and engine handoff of existing strips/sheets. Pair with `generation.md` only when new animation content must also be generated.

## Geometry contract

Before slicing, know the relevant values:

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

Do not infer unknown geometry from blank or duplicate frames.

## Normalize before final package

A character set should share:

- canvas size;
- apparent scale;
- anchor/baseline;
- transparent padding policy;
- direction convention.

Cropping may detect bounds, but final frame canvases should stay stable to avoid sprite jitter/foot sliding.

## Per-action strips vs combined grid

Prefer per-action strips when action lengths vary or iteration is frequent. Use a combined atlas/grid when downstream tooling explicitly benefits from it and metadata records exact layout.

Do not combine assets merely to make them “look like a spritesheet.”

## Timing metadata

Geometry and animation timing are separate. Preserve or generate:

- frame duration / FPS policy;
- loop / ping-pong / one-shot;
- valid range/tag;
- intentional holds.

When source tools provide tags/JSON/sidecars, convert them deterministically instead of recreating ranges by hand.

## Naming

Prefer stable sortable names such as:

```text
{character}_{action}_{direction?}_{frame:02}.png
```

Names should be scriptable and consistent with engine animation/state conventions.

## Deterministic operations

Automate repeatable transformations when practical:

- exact-grid split;
- bounds detection + fixed-canvas padding;
- alpha cleanup;
- shared scale/anchor alignment;
- rename;
- atlas packing;
- metadata generation;
- preview GIF/contact sheet.

The same approved input should produce the same output.

## Engine handoff

Deliver explicit:

- filtering/mipmap/compression policy;
- animation names;
- loop policy;
- per-frame timing;
- anchor/pivot;
- action/direction naming;
- source vs derived ownership.

For Godot, these feed SpriteFrames/runtime animation, but combat/state remains the authority for gameplay validity and damage.

## Packaging QA

Check expected file count, layout/ranges, clean alpha, stable canvas/anchor, direction order, deterministic naming, metadata/file consistency, loop flags and preview motion. Re-running the pipeline should not unexpectedly change approved output.

Never overwrite the only approved source before preview/validation.
