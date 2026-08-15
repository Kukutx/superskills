---
name: skill-name
description: What this skill does and when an agent should use it.
---

# Skill Name

## Use

Use for:
- ...

Do not use for:
- ...

## Workflow

1. Inspect the relevant context before proposing changes.
2. Identify the smallest decision or implementation path that solves the task.
3. Preserve existing conventions unless they block the goal.
4. Execute or produce the requested deliverable.
5. Validate the result at the level required by the claim.

## Output

Default to the smallest useful structure for this domain. Do not emit empty sections merely to satisfy a template.

## Constraints

- Do not invent missing facts.
- Do not add unrelated alternatives or architecture.
- Ask only when missing information would materially change the result.
- Prefer a usable first version over generic explanation.

## Validation

State what was actually checked. Distinguish static confidence from runtime, visual, external, or production verification when relevant.

<!--
Add one-level references/ only when domain depth is genuinely task-dependent.
If a real ownership/routing boundary needs regression coverage, add maintenance/behavioral-evals.md.
Use maintenance/sources.md only for substantial source inventories; use decisions.md rarely.
Move ownership when splitting content; do not duplicate rules across files.
Do not create prompt-template.md, examples.md, changelog.md, or compatibility stubs by default.
Run python tools/validate_repo.py before completion.
-->