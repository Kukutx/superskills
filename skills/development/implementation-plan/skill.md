---
name: implementation-plan
description: Convert an approved technical direction or feature requirement into concrete implementation tasks, file-level changes, tests and rollout steps.
---

# Implementation Plan

## Workflow

1. Inspect the actual repository/file structure when available.
2. Identify the smallest coherent implementation sequence.
3. Separate schema/data migrations from application changes.
4. Order tasks so contracts and risky assumptions are validated early.
5. Include tests with the task that creates the behavior, not as an afterthought.
6. Include rollout/rollback only when the change has deployment or data risk.

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
- Avoid vague tasks such as “implement backend” or “add tests”.
- Prefer incremental, reversible changes.
- Domain-specific implementation should follow the relevant domain Skill rather than generic patterns.