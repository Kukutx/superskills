# AI and Navigation Reference

Use for enemy behavior/state decisions, perception, steering and `NavigationAgent2D`. Seeded world generation and spawn/wave generation are in `procedural-generation.md`.

## Start from observable behavior

Define the behavior first:

```text
idle/patrol
-> notice
-> chase
-> attack
-> recover/search
-> return
```

Then decide whether simple state logic, reusable behavior abstraction or a heavier model is justified.

## Ownership

```text
AI decision -> intent/state
movement -> CharacterBody2D motion
combat -> attack/damage truth
animation/VFX -> presentation
```

AI should not become a second movement, damage or animation authority.

## Perception

Define detection range, line of sight, reaction delay, target memory, lose-target rules and fairness. Area2D can provide broad detection; ray/query checks can refine LoS. Avoid expensive sensing for every agent every physics frame.

## NavigationAgent2D

Confirm navigation data readiness, target reachability, radius/avoidance vs geometry, dynamic map update timing and separation between path/steering output and actual CharacterBody2D movement.

## State stability

Prevent threshold oscillation with hysteresis, cooldown or explicit gates when appropriate.

## Complexity ladder

1. handwritten states for a small understandable graph;
2. reusable behavior/state abstraction when conditions/actions/subtrees repeat;
3. hierarchical/parallel state model when state composition itself explodes;
4. heavier tooling only after current complexity is a demonstrated maintenance problem.

Keep an existing project framework when it is adequate; do not introduce overlapping state systems.

## Decision frequency

Cheap movement can run every physics tick; expensive perception/path/reasoning can run less often, staggered or only when inputs change materially. Profile before adding complexity.

## Attack handoff

AI expresses intent, e.g. `want_attack(target)`. Combat validates cooldown/range/state and owns the actual attack/damage result.

## Debug visibility

Development overlays may expose current state, target, ranges, LoS, nav path and cooldowns, but they should be easy to disable.

## Validation

Test detection boundaries, blocked LoS, unreachable/escaped targets, many agents, dead/stunned states, pause/time-scale, nav changes and transition stability.
