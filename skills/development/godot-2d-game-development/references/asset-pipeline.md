# 2D Asset Pipeline Reference

Use this reference when the task includes generating, cleaning, organizing or importing 2D game assets: sprites, animation strips, FX, tiles, maps, props or UI art.

## 1. Treat art as production assets

The goal is not merely “a good-looking image”. A usable game asset needs:

- known dimensions;
- transparent/background policy;
- stable scale and anchor;
- predictable naming;
- repeatable export format;
- engine import settings;
- QA at actual game scale.

Always design the asset around how the game will consume it.

## 2. Decide the asset type before generating

Common types:

```text
character sprite / animation strip
enemy / boss sprite
projectile
impact FX
spell / attack FX
tileset
map base
transparent prop
UI icon / HUD art
portrait / dialogue art
```

Do not ask one image to serve incompatible purposes. A decorative full map illustration is not automatically an editable gameplay map; a concept sheet is not automatically a spritesheet.

## 3. Character and animation pipeline

For animated characters:

1. establish one approved in-game seed frame;
2. lock silhouette, proportions, palette, outfit, weapon and facing direction;
3. define exact animation/action requirements;
4. generate a whole strip per action when possible;
5. normalize frames to one shared size, scale and anchor;
6. preview the animation;
7. only then import/update the game asset.

For detailed sheet layout and slicing, use `development/game-dev-spritesheet-slicer`.

Avoid independent per-frame generation because identity, proportions and equipment drift easily.

## 4. FX bundles

When generating combat effects, think in bundles rather than isolated pretty images.

Example fire attack bundle:

```text
cast / anticipation
projectile or weapon trail
impact burst
optional ground residue / smoke
small HUD/icon asset if the ability needs one
```

Keep related effects consistent in palette, shape language and scale.

At runtime, each asset should have a clear origin/anchor so the engine can place it at a muzzle, hand, hit point or target center.

## 5. Pixel-art constraints

When the project is pixel art:

- use crisp pixel clusters;
- keep a consistent source resolution;
- preserve readable silhouettes;
- use a controlled palette appropriate to the project;
- avoid accidental anti-alias blur;
- keep transparent backgrounds clean;
- check outlines and highlights at actual display size;
- do not mix highly detailed AI illustration pixels with deliberately low-resolution game sprites.

The visual style should match existing shipped/project assets, not whatever style the generator prefers.

## 6. Map workflow

For editable 2D maps, separate concerns:

```text
ground/base visual
repeatable tiles
transparent props
collision
navigation/pathing
spawn points
interactive zones
exits/doors
foreground/occlusion layers
```

Generated map art can be used as a visual reference or base, but gameplay metadata should remain editable in Godot.

For Godot handoff, prefer reusable game structures such as:

- `TileMapLayer` for editable tile layers;
- `Sprite2D` or reusable scenes for props;
- `StaticBody2D` / collision shapes for blocking geometry;
- `Area2D` for encounter/trigger zones;
- explicit spawn/exit markers;
- y-sort strategy for top-down depth.

Do not bake enemies, collision and triggers irreversibly into a background PNG.

## 7. Tileset rules

A tileset needs more than a nice texture sheet.

Define:

- tile size;
- atlas dimensions;
- terrain/edge/corner requirements if used;
- collision policy;
- variants;
- animated tiles if needed;
- transparent padding/spacing;
- palette and lighting direction.

Test real tile combinations. A tileset that only looks correct in its showcase sheet is not ready.

## 8. Props

For reusable props:

- export transparent PNGs;
- keep consistent ground contact and scale;
- separate shadow when the project needs dynamic placement;
- keep collision simpler than visual silhouette where appropriate;
- preserve enough transparent padding for effects without creating huge empty textures.

For top-down games, identify the ground anchor explicitly so y-sorting and placement remain stable.

## 9. UI art

UI art should be designed for scalable layout rather than baked screenshots.

Prefer separate:

```text
icons
frames/panels
buttons
badges
cursor/focus states
resource symbols
```

Do not bake normal dynamic labels, values or localized text into the art unless that text is intentionally part of the artwork.

For scalable pixel panels, plan stretchable center/edge regions so corners remain crisp.

## 10. Cleanup and normalization

After generation, perform deterministic cleanup where possible:

- remove unwanted background/chroma residue;
- crop or pad to exact frame sizes;
- normalize shared scale;
- align to shared anchor;
- split strips/sheets predictably;
- verify alpha edges;
- export PNG for sprites/tiles when lossless transparency is needed;
- create preview sheets/GIFs for human inspection.

Do not rely on prompts alone to guarantee exact frame geometry if a deterministic post-process can enforce it.

## 11. Naming and folders

Use names that reflect game semantics, not generation history.

Example:

```text
player/
  idle/
  run/
  attack_light/
  attack_heavy/
  hurt/
  death/
fx/
  sword_hit_small.png
  sword_hit_heavy.png
  dash_trail.png
ui/
  icon_health.png
  icon_coin.png
```

Avoid names such as `final_v2_new_fixed_03.png` inside production asset paths.

## 12. Godot import handoff

When assets enter Godot, verify:

- filtering appropriate to pixel/non-pixel art;
- repeat mode if tiles require it;
- frame layout / SpriteFrames setup;
- scale and anchor/pivot;
- material/shader assignment;
- collision remains separate from art;
- scenes reference the intended production file, not a preview/export intermediate.

Do not change global import settings without checking how existing assets rely on them.

## 13. Asset QA

Before accepting an asset, check:

- does it match existing game art direction?
- is silhouette readable at game scale?
- are scale and anchor consistent with neighboring assets?
- is transparency clean?
- does animation preserve identity and proportions?
- do tiles actually connect in multiple combinations?
- do props sit correctly on the ground/y-sort line?
- are FX readable without covering gameplay telegraphs?
- are files named and exported predictably?
- does the asset look correct in-engine, not only in an image viewer?

## 14. Source vs derived files

Keep a distinction between:

- approved source/reference art;
- raw generated output;
- normalized production frames;
- previews/GIFs;
- engine-ready imported assets.

Do not overwrite the only approved source frame with a processed derivative.

## Upstream inspiration

Condensed from `0x0funky/agent-sprite-forge`, `openai/plugins` sprite pipeline and the existing `development/game-dev-spritesheet-slicer` skill in this repository. The retained principle is: generate creatively, then use deterministic cleanup/normalization and in-engine QA to make the result production-ready.