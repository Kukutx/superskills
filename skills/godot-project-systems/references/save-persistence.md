# Save and Persistence Reference

Use for stable persistent IDs, save/load, schema migration, checkpoints, settings/profile boundaries and durable world/progression state. Runtime inventory/equipment mechanics are in `inventory-progression.md`.

## Stable identifiers

Persist stable IDs such as item, quest, NPC or checkpoint keys. Do not use translated display text, runtime instance IDs or fragile NodePaths as long-term primary keys.

## Save persistent truth only

A save schema may include:

```text
schema version
save/profile id
checkpoint/position when appropriate
stats/progression
inventory/equipment snapshot
quest/flag state
world mutations
procedural seed/version when required
```

Do not serialize the entire SceneTree.

## Versioned migration

Store a schema version from the first format:

```text
read raw data
-> validate shape
-> migrate N -> N+1 stepwise
-> validate migrated data
-> instantiate/apply runtime state
```

Migrations should be deterministic and diagnosable. Renamed IDs need explicit mapping; do not silently wipe unknown content. Keep old fixtures for important migration tests.

## Safe writing

Avoid corrupting the only save during partial writes:

```text
serialize
-> write temp
-> flush/close
-> optional read-back validation
-> replace final
-> optional backup/slot rotation
```

Use platform/Godot capabilities appropriate to the target.

## Autosave policy

Use meaningful triggers such as checkpoints, scene transitions, durable transactions, progression events, debounced intervals or lifecycle boundaries. Do not save every frame.

## Settings / profile / save boundaries

Conceptually distinguish:

- settings/preferences: audio, graphics, controls, accessibility;
- profile/meta progression: unlocks/meta state;
- save slot/world state: current run/world.

They do not need separate files, but should not become one unversioned mutable blob.

## Loading order

```text
load definitions/content
-> read + migrate save
-> create target world/scene
-> apply persistent state
-> emit ready/changed events
-> UI/presentation reacts
```

Avoid UI reading half-applied state.

## Missing/renamed content

Plan for removed checkpoints, item/quest ID changes, stat schema changes and dependency serialization changes. Prefer explicit migration over guessing by display name.

## Persistence boundary

Gameplay systems own runtime truth; persistence snapshots durable state after valid mutations. A disk-write failure should not leave UI and gameplay disagreeing silently.

## Validation

Cover no-save/new game, current and previous-version fixtures, corrupted/partial files, missing/renamed IDs, scene reload, settings/control persistence, procedural seed restore when used and safe failure behavior.
