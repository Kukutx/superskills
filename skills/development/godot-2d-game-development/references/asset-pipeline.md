# 2D Asset Pipeline Reference

Use for Godot 2D source -> production -> import across sprites, FX, tiles, maps, props and UI art.

Sprite animation generation/geometry/slicing/naming/packing belongs to `development/sprite-animation-pipeline`; Godot runtime animation belongs to `animation-runtime.md`.

## Production contract

Before import, define the relevant source, size/world scale, alpha/background, anchor/pivot, naming, source-vs-derived ownership, filtering/import policy and metadata.

“Looks good” is not the same as production-ready.

## Choose pipeline by source type

### Generated/raster output

```text
approved visual
-> generate useful unit
-> deterministic cleanup/normalize
-> preview
-> import
```

Use models for visual content; exact crop/pad/alpha/scale/naming/packing should be deterministic when practical.

### Authored editable source

For Aseprite/Krita/Pixelorama-style sources, preserve valuable layers, tags, durations, palette and anchor metadata. Do not flatten metadata and then rebuild a second manual truth in Godot.

### Static image

Icons, portraits, props and backgrounds only need the cleanup/import relevant to their actual use; do not force them through animation workflows.

## One editable source of truth

```text
editable source
-> deterministic export/import
-> Godot-consumed derived asset
```

Do not hand-edit source and generated derivatives as competing truths.

Before adding an importer, confirm project compatibility, ownership of generated files, clean-checkout reproducibility and whether it really removes recurring work.

## Asset-specific rules

### Pixel/raster

Keep deliberate source resolution/scale, clean alpha, readable game-scale silhouettes, filtering and reasonable transparent bounds.

### FX

Organize around gameplay events with explicit origin, direction, scale, lifetime and loop/one-shot policy. Runtime readability is in `rendering-vfx-shaders.md`.

### Maps / tiles

Keep visual layout separate from collision/navigation/spawn/trigger/exit truth. Map ownership is in `world-tilemap-level-design.md`.

### Props

Keep consistent world scale, ground/y-sort anchors and clean bounds; collisions/interactions remain Godot-side gameplay data.

### UI art

Prefer reusable icons/panels/states, keep dynamic/localized text out of generic artwork and use suitable scalable UI techniques instead of arbitrary image stretching.

## Deterministic post-process

Automate crop/pad, alpha cleanup, explicit resize/scale, split/combine, naming, metadata conversion and preview when practical. Never overwrite the only approved source.

## Godot handoff

Confirm import type, filtering/mipmap/compression, scale/pivot/region, atlas/subresource ownership, re-import safety, case-correct paths/names and clean import.

## Validation

Check final size/scale/anchor, alpha/bounds, source reproducibility, absence of duplicate truths, preserved metadata, tile/map composability, editable gameplay metadata, localization-ready UI and actual target-resolution appearance.
