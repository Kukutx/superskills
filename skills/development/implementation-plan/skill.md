---
name: implementation-plan
description: Turn decided behavior and an approved technical direction into concrete file-level changes, ordered tasks, tests and rollout steps. Use after key architecture/ownership decisions are settled.
---

# Implementation Plan

## Use

Use when the user knows what should be built and the main technical direction is already decided, but needs a concrete execution sequence.

If ownership, data contracts or architecture are still materially unresolved, use `development/technical-design` first. If the plan spans multiple non-code workstreams or a broad project roadmap, use `planning/project-planner`.

## Workflow

1. Inspect the actual repository/file structure when available.
2. Restate only the technical decisions the plan depends on; do not redesign them silently.
3. Identify the smallest coherent implementation sequence.
4. Separate schema/data migrations from application changes.
5. Order tasks so risky assumptions and contracts are validated early.
6. Put tests/validation next to the task that creates the behavior, not as an afterthought.
7. Include rollout/rollback only when the change has deployment or data risk.

If a new architectural blocker appears while planning, surface it explicitly rather than hiding a design decision inside a task list.

## Output

Default:

1. **Implementation summary**
2. **Files/components to change**
3. **Ordered tasks**
4. **Data/API/interface changes** when relevant
5. **Tests / validation**
6. **Migration / rollback** when relevant
7. **Open blockers** only when unresolved

## Constraints

- Do not invent exact file paths when the repository has not been inspected; label suggested paths as suggestions.
- Do not repeat the PRD or technical design in full.
- Do not reopen settled architecture without evidence that it blocks implementation.
- Avoid vague tasks such as “implement backend” or “add tests”.
- Prefer incremental, reversible changes.
- Domain-specific implementation should follow the relevant domain Skill rather than generic patterns.
