---
name: xtool-f1-engraving
description: Design engraving-ready concepts and production guidance for xTool F1 projects, with small-format geometry, material-aware artwork and SVG/raster production constraints. Verify current machine/material guidance when exact capability or safety matters.
---

# xTool F1 Engraving

## Core goal

Produce artwork that survives real engraving, not generic illustration.

For the standard xTool F1, treat `115 × 115 mm` as the machine working-area baseline. The actual object, fixture, rotary/extension setup and framing result determine the usable design area, so do not hard-code a universal inner margin.

When exact machine capability, accessory behavior or material compatibility matters, verify current official xTool guidance rather than relying on remembered specs.

## Start from the real object

Before detailed design, identify the facts that materially change production:

```text
machine/setup
material/coating
object shape + usable area
engrave vs mark vs cut intent
final physical size
required text/QR readability
```

If any of these are unknown, make only reversible artwork decisions and leave process settings for a real material test.

## Material-aware direction

Use the actual material response to control detail density.

- wood / slate-like engraving surfaces: bold silhouettes, line art and readable filled regions usually survive small-scale production better than fragile micro-detail;
- leather or coated surfaces: keep typography/marks clean and verify that the exact material/coating is laser-safe and suitable;
- coated/anodized or bare metals: artwork may be appropriate for marking/engraving, but the exact laser/material interaction must be verified rather than inferred from the visual design;
- acrylic/glass-like or unknown formulations: do not generalize from appearance alone; verify the exact material and supported process first;
- paper/card: fine illustration may be possible, but heat response and final physical scale still control usable detail.

Do not provide absolute power/speed/frequency values unless requested and supported by the exact machine + material + process. Prefer a material test matrix or verified preset as the starting point.

## Artwork rules

Unless the user requests otherwise:

- favor high-contrast geometry and clear negative space;
- avoid gradients/soft shadows when they do not survive the intended engraving process;
- keep text and important strokes comfortably above the failure threshold demonstrated by the material test;
- avoid fragile bridges or tiny isolated shapes in cut work;
- separate engrave/fill/cut intent explicitly;
- convert production text to outlines before final vector export when appropriate;
- keep QR/barcode-like content simple enough to test after engraving at final size;
- do not use decorative color alone as the only indicator of process ownership in the final production file.

Do **not** treat one fixed minimum line width or text height as universal across wood, metal, coated surfaces, different lasers and different engraving settings.

## Workflow

1. Confirm machine/setup, object, material and usable size when they affect the design.
2. Choose one clear visual hierarchy and simplify it for the final physical scale.
3. Separate process layers:
   - primary engraving/marking;
   - optional secondary texture/detail;
   - cut path only when the verified material/setup supports cutting.
4. Produce vector/image direction that avoids detail the chosen process cannot reproduce reliably.
5. Prepare production notes: stroke/fill ownership, text outlines, closed cut paths, image threshold/dither intent when raster is used.
6. Frame/preview on the real object.
7. Run a small material/detail test before committing the final object.
8. Adjust the artwork from the test result before tuning decorative micro-detail.

## Vector vs raster

Prefer vector when the design depends on:

- logos;
- typography;
- line art;
- geometric borders;
- exact cut paths.

Raster is appropriate for:

- photos;
- halftone/dithered tonal artwork;
- textured illustration whose appearance depends on image processing.

Do not auto-trace a complex raster and assume the resulting thousands of vector nodes are production-improved.

## Output

Default:

1. **Object / material / usable area**
2. **Concept + composition**
3. **Process/layer plan**
4. **Vector/raster production direction**
5. **Image/vector prompt** when useful
6. **Test plan**
7. **Final checks**

Provide variants only when they are meaningfully different production directions.

## Constraints

- Do not treat a beautiful generated image as engraving-ready without simplifying and testing it.
- Do not invent material safety, compatibility or laser settings.
- Do not assume the full machine work area is usable on every object/fixture.
- Do not use huge filled areas without considering time, heat and the actual material response.
- Cut lines must be unambiguous and closed where the downstream process requires it.
- Unknown material/process facts should trigger verification, not confident fabrication.
- The real machine/fixture/material setup overrides repository defaults.

## Validation

Before final production, check the relevant subset:

- design fits the framed usable area;
- important text/details are readable at physical size;
- vector paths/fills represent the intended process unambiguously;
- raster threshold/dither is previewed at real size when used;
- material compatibility is verified;
- a representative detail/material test has been run when failure would waste the object;
- final output contains no unintended hidden shapes, duplicate paths or open cut contours.
