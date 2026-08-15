---
name: xtool-f1-engraving
description: Design engraving-ready concepts and production guidance for xTool F1 projects, with small-format geometry, material-aware artwork and SVG-friendly constraints.
---

# xTool F1 Engraving

## Core goal

Produce artwork that survives real engraving, not generic illustration.

Default when the user gives no different machine/material constraints:

- small-format xTool F1 workflow;
- design area up to about `110 × 110 mm`;
- keep `3–5 mm` margin where practical;
- high-contrast black/white or clearly separated engraving layers;
- SVG/DXF-friendly geometry or high-contrast raster suitable for tracing.

These are workflow defaults, not guarantees for every fixture/material.

## Material-aware direction

- **wood / slate**: bold silhouettes, line art, readable filled regions; avoid fragile micro-detail.
- **leather**: monograms, labels, stamp-like marks, clean typography.
- **coated metal**: compact icons, logos/text, line art, QR when tested at final size.
- **acrylic / glass-like surfaces**: simple high-contrast forms; verify the actual material/coating before production.
- **paper/card**: can tolerate finer illustration, but final scale still controls detail.

Do not give absolute laser power/speed values unless requested and supported by the exact material/process. Prefer a material test or verified machine/material preset.

## Artwork rules

Unless the user requests otherwise:

- avoid gradients, soft shadows and color-dependent meaning;
- keep negative space clear;
- avoid tiny text and excessively thin strokes;
- avoid fragile cut bridges;
- separate engraving/fill/cut intent explicitly;
- convert production text to outlines before final SVG export when appropriate;
- keep QR/barcode-like content large and clean enough to test after engraving.

Useful conservative starting constraints for small artwork are `>= 0.2 mm` important line width and `>= 3 mm` text height, but treat them as defaults to verify, not universal physical limits.

## Workflow

1. Confirm object/material/usable size when they materially affect the design.
2. Choose one clear visual hierarchy and simplify it for final physical scale.
3. Separate layers/processes:
   - engraving/fill;
   - optional lighter texture;
   - cut path only when needed.
4. Produce image-generation/vector direction that avoids effects impossible or wasteful to engrave.
5. Prepare SVG/tracing notes: stroke/fill ownership, text outline, closed cut paths, minimum detail.
6. Run a small material/detail test before the final object.

## Output

Default:

1. **Concept + intended material/size**
2. **Composition**
3. **Layer/process plan**
4. **Image/vector prompt** when useful
5. **SVG / production notes**
6. **Final checks**
7. Up to 3 variants only when they are meaningfully different

## Constraints

- Do not treat a beautiful generated image as engraving-ready without simplifying/validating it.
- Do not invent material safety or laser settings.
- Do not use huge filled areas without considering heat/time/appearance on the actual material.
- Cut lines must be unambiguous and must not rely on decorative color semantics alone in the final production file.
- If the user's actual machine/fixture/work area differs, their real setup overrides these defaults.