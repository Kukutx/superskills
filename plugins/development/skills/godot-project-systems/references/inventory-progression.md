# Inventory and Progression Reference

Use for item definitions, runtime inventory/equipment state, stacking/capacity, transfer/use transactions and progression/unlock mechanics. Durable serialization/migration is in `save-persistence.md`.

## Definition != instance state

Example:

```text
ItemDefinition(Resource)
- id
- display_name_key
- icon
- max_stack

InventoryEntry(runtime)
- item_id
- quantity
- durability / rolled stats / unique state
```

Do not mutate shared Resource definitions as if they were per-instance state.

## Stable domain IDs

Items, quests, unlocks and progression nodes need stable project-defined IDs. UI labels and translated names are presentation, not identity.

## Inventory truth is data, not UI

```text
inventory transaction
-> validate
-> mutate inventory data
-> emit domain event
-> UI reacts
-> persistence snapshots when appropriate
```

Do not reconstruct inventory truth from GridContainer children.

## Transaction rules

Make the relevant semantics explicit:

- stacking/max stack;
- capacity/weight/slots;
- unique state/durability;
- equipment slots and conflicts;
- transfer/split/merge;
- use/remove/grant atomicity;
- missing definitions;
- rollback/failure behavior for multi-step transactions.

## Progression ownership

Progression/unlock state should be explicit data with stable IDs and clear prerequisites/reward application. Presentation (skill tree UI, badges, animations) reacts to that state rather than owning it.

## Complexity boundary

Small inventories usually remain clearer as project-owned Resources/data structures. Evaluate a framework only when reusable container/transfer/equipment/stacking mechanics have become demonstrated recurring complexity.

External tooling does not change project responsibilities: IDs, save schema/migration, gameplay truth and UI separation remain explicit.

## Persistence handoff

Save only durable inventory/progression state; transient UI selection, drag state and derived caches should not enter the long-term contract. Coordinate schema/version changes with `save-persistence.md`.

## Validation

Test empty/full inventory, stack boundaries, split/merge, unique/equipment state, invalid transactions, missing definitions, repeated reward application, save/reload and renamed IDs when relevant.
