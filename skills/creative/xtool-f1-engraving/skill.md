---
name: xtool-f1-engraving
description: Design engraving-ready concepts and production guidance for xTool F1 projects, with small-format geometry, material-aware artwork and vector/raster constraints. Verify current machine/material guidance when exact capability or safety matters.
---

# xTool F1 Engraving

## Goal

Produce artwork that survives real engraving, not generic illustration.

Standard F1 working-area baseline: `115 × 115 mm`. Actual usable area depends on the object, fixture/accessory and framing, so do not hard-code a universal inner margin.

## Start from the real setup

Clarify only what changes production:

```text
machine/setup
material/coating
object shape + usable area
engrave/mark/cut intent
final physical size
text/QR readability needs
```

Unknown capability/material facts should stay unresolved until verified from current xTool guidance or a real material test.

## Material rule

Artwork detail must follow the **actual material response**.

- favor bold silhouettes, clear line art and readable filled regions for small-format work;
- coated/bare metals, leather, acrylic/glass-like materials and other formulations must be treated according to the exact material/process, not visual appearance alone;
- verify laser-safe material compatibility before processing unknown materials;
- do not provide absolute power/speed/frequency settings unless the exact machine + material + process supports them.

Use a material test/preset as the starting point, then adjust artwork if fine details fail.

## Artwork rules

Unless the design requires otherwise:

- strong contrast and clear negative space；
- avoid gradients/soft shadows when the process cannot reproduce them reliably；
- important text/strokes stay comfortably above the failure threshold found in testing；
- avoid fragile bridges/tiny isolated shapes for cut work；
- separate engrave/fill/cut intent explicitly；
- outline production text when appropriate；
- QR/barcode-like content must be tested after engraving at final size；
- do not use decorative color as the only process indicator。

There is no universal minimum line width/text height across all materials and settings.

## Vector vs raster

Prefer vector for:

- logos / typography；
- line art / borders；
- geometric shapes；
- exact cut paths。

Use raster for photos, dither/halftone or tonal artwork.

Do not auto-trace a complex raster into thousands of nodes unless that actually improves production.

## Workflow

1. Confirm setup, material, object and usable size.
2. Simplify composition for final physical scale.
3. Separate process layers: primary engraving/marking, optional secondary detail, cut only when verified supported.
4. Prepare vector/raster artwork with unambiguous process ownership.
5. Frame/preview on the real object.
6. Run a representative material/detail test before the final object.
7. Adjust artwork first when detail fails; only then fine-tune decorative complexity.

## Output

Default:

1. **Object / material / usable area**
2. **Concept + composition**
3. **Process/layer plan**
4. **Vector/raster direction**
5. **Prompt** when generation is useful
6. **Test + final checks**

## Constraints / validation

- generated image != engraving-ready file；
- do not invent material safety/settings；
- full machine area is not guaranteed usable on every object；
- avoid huge fills without considering heat/time/material response；
- cut contours must be unambiguous/closed when required；
- check physical-size readability, framed fit, hidden/duplicate paths and raster threshold/dither；
- when failure would waste the object, require a representative test before final production。
