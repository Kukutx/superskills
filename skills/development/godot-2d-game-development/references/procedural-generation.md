# Procedural Generation and Spawning Reference

Use for seeded procedural layouts/content, spawn rules, waves and validity checks. Tile/world authoring lives in `world-tilemap-level-design.md`; enemy decision logic lives in `ai-navigation.md`.

## Deterministic pipeline

When reproducibility matters:

```text
seed
-> abstract layout/data
-> validate rules/connectivity
-> materialize TileMap/scenes
-> place gameplay content
-> runtime integration
```

Validate structure before decorating or instantiating the final scene graph.

## Separate generation from materialization

Prefer an abstract/data representation that can be inspected and tested before it becomes Nodes/TileMapLayer content. This makes seeds reproducible and failures diagnosable.

## Validity rules

Define only rules the game actually requires, such as:

- start/goal reachable;
- mandatory rooms/items reachable;
- no spawn inside collision;
- navigation matches generated layout;
- critical route/door/key constraints hold;
- encounter budget remains within design bounds.

Generation that merely “looks random” is not enough.

## Spawn / wave ownership

Make explicit:

```text
spawn budget
max active
spawn regions
minimum player distance / fairness
pacing/cooldown
elite/boss rules
cleanup/despawn
```

Do not perform uncontrolled random spawning every frame.

## Seed persistence

If save/replay/debug depends on reproducibility, persist the seed and any non-derivable mutations. Do not save a seed and assume it reproduces the same world after generator logic has changed without a version/migration policy.

## Performance

Generate expensive content at appropriate boundaries, cache stable data and avoid rebuilding whole worlds for small runtime changes. Profile before introducing chunking/streaming.

## Debug visibility

Expose seed, generation stage, rejected constraints and connectivity/spawn diagnostics during development. Failure should identify which invariant could not be satisfied.

## Validation

Test same-seed determinism, diverse seeds, connectivity, spawn validity, collision/navigation alignment, save/reload policy and failure behavior when constraints cannot be satisfied.
