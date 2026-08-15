# Godot Core Architecture Reference

Use for scene ownership, signals, Resources, state, autoloads, composition and dimension-neutral project structure.

## Start from ownership

First ask: **who owns this fact?** Exact classes can differ by project, but the conceptual boundary should stay clear.

```text
action/state controller -> can/cannot act + state transitions
movement controller -> physical movement execution
combat/attack resolver -> attack instance, hit validity, damage calculation, repeated-hit policy
Health/Vitals -> current HP, invulnerability state, alive/dead result
animation/audio/VFX/UI -> presentation and feedback
save/persistence -> durable representation
```

A small project may combine several roles in one node. The important rule is one authoritative truth, not one class per concept.

## Scene composition

Godot works well with scene/node composition, but do not turn every line of logic into a component.

Useful independent components may include Health/Vitals, Hitbox/Hurtbox, InteractionArea or a state machine when their state/lifecycle is genuinely reusable or complex.

Avoid trivial wrappers that have no independent state, lifecycle or reuse value.

## Direct call vs signal

Use a direct call when:

- the owner deliberately knows the target;
- the relationship is stable one-to-one;
- a synchronous result matters.

Use a signal/event when:

- one event has multiple listeners;
- the emitter should not know listeners;
- UI/audio/VFX react to gameplay;
- scene replacement/lifecycle benefits from decoupling.

Do not replace ordinary calls with a global event bus by default.

## Autoload

Use autoloads for truly cross-scene services with clear global lifetime, such as settings/profile, save coordination, scene transitions or project-wide audio when needed.

Do not put Player, Combat, Inventory or UI into autoload merely for convenient access.

## Resources

Resources are useful for definitions/config such as items, attacks/abilities, stat templates, loot tables, enemy archetypes and dialogue/quest data.

Resources may be shared. For mutable runtime instance data, make the duplicate/local-to-scene/instance strategy explicit so several actors do not accidentally share HP, durability or rolled state.

## State machines

Simple state does not require a framework. Start with the project's existing explicit state representation.

Escalate when transitions are scattered, impossible boolean combinations proliferate, enter/exit lifecycle matters, states are reused, or hierarchical/parallel behavior is real.

State owns gameplay permission/transition truth. Animation names or AnimationTree state should not become the only gameplay state authority.

## Dependency direction

Prefer:

```text
data/config
-> gameplay/domain systems
-> explicit events
-> presentation/UI/audio
```

Avoid presentation mutating unrelated domain internals merely because it has a reference to them.

## Node references

Follow the project convention: cached stable children, exported typed references/NodePaths when designer wiring helps, and groups only for genuinely group-based relationships.

Avoid repeated tree searches in hot loops for objects whose ownership is already stable.

## Lifecycle

Make relevant lifecycle ownership explicit:

- `_ready()` wiring;
- signal connect/disconnect;
- timers/tweens cleanup;
- node free/reuse;
- scene transition reset;
- autoload/profile/new-game reset.

Many ghost bugs are stale scene/global state rather than algorithm errors.

## Architecture escalation rule

Add abstraction only when at least one is real now:

- duplication already exists;
- multiple consumers need the same mechanism;
- current coupling blocks testing/maintenance;
- an approved roadmap requires the extension;
- bugs come from unclear ownership.

Do not build layers only for hypothetical future use.

## Minimum validation

After architecture changes, verify the relevant subset:

- scene loads;
- signals connect once;
- state transitions exit correctly;
- mutable Resources do not leak across instances;
- scene reload/new game has no stale global state;
- presentation listeners can fail/disappear without corrupting gameplay truth;
- combined roles still preserve one authoritative owner per fact.
