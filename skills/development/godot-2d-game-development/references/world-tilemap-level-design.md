# World, TileMap and Level Design Reference

Use for TileMapLayer, TileSet, terrain, top-down depth, parallax, collision/navigation, room/level structure, external level authoring and 2D level implementation.

## Separate visual world from gameplay metadata

Keep concepts such as ground, decoration, foreground/occlusion, collision, navigation, interactables, spawn points, triggers and exits explicit. They may share an authoring source, but a baked background image should not be the only truth for gameplay metadata.

## Native Godot first

Prefer the project's existing TileMapLayer/TileSet workflow when it is adequate. Tiles are good for repeated ground/walls/terrain/simple metadata; complex doors, NPCs, enemies, pickups and hazards are often clearer as scenes.

## One authoring source of truth

Godot-native authoring is appropriate when the team works primarily in Godot. If an external level editor is already the source of truth, use a deterministic import pipeline:

```text
editable source
-> deterministic importer
-> generated Godot representation
-> runtime integration
```

Do not hand-edit both source and generated representation.

## Terrain and tileset production

Start with current TileSet terrain capabilities. Evaluate extra tooling only when authoring is a demonstrated recurring bottleneck.

Define tile size, atlas grid, terrain edges/corners, collision/navigation, variants, animated-tile rules and spacing/padding. QA real combinations: corners, T-junctions, corridors, isolated tiles and terrain transitions.

## Collision simplification

Collision serves gameplay, not pixel tracing. Keep floor/wall silhouettes stable, prop footprints clear and decorative bumps from creating snaggy geometry.

## Top-down draw order

Make y-sort/layering, prop ground anchors and tall-prop occlusion explicit. Ground-contact points are often better sort anchors than image centers.

## Parallax

Parallax is presentation. Check layer-speed hierarchy, seams, camera bounds, repeat, filtering and motion comfort.

## Level flow

Whitebox gameplay before high-fidelity art:

```text
goal -> route -> challenge -> recovery -> reward/variation
```

Walkable/blocked space, hazards, interactables, exits and enemy telegraphs should remain readable.

## Navigation handoff

Keep nav geometry synchronized with level layout, agent radius compatible with corridors and dynamic obstacle strategy explicit. Enemy navigation behavior is in `ai-navigation.md`.

## Generated worlds

For seeded/generated layouts, use `procedural-generation.md`. Materialized maps still need editable collision, spawn/exit markers, triggers, navigation, y-sort anchors and interactive props.

## Chunking / streaming

Only add it when world size/load measurements justify the complexity.

## Generated-file rule

For imported/generated Godot files, define whether derived output is committed, whether clean checkout can regenerate it, whether CI needs the importer and whether generated files may be hand-edited.

## Level QA

Run spawn-to-exit paths, movement extremes, collision edges, camera limits, y-sort crossings, enemy paths, trigger re-entry, unreachable rewards, foreground visibility, terrain combinations and clean re-import when external authoring is used.
