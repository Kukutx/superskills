---
name: skill-name
description: What this Skill owns and when an agent should use it.
---

# Skill Name

## Use

Use for:

- ...

Do not use for:

- ...

## Required context

List only domain-specific facts whose absence could materially change correctness or direction. Inspect supplied context first; group necessary questions instead of guessing or repeatedly asking one at a time.

## Workflow

1. Inspect the relevant context before proposing changes.
2. Resolve direction-changing or factual unknowns; use reversible assumptions for harmless gaps.
3. Identify the smallest decision or implementation path that solves the task.
4. Preserve existing conventions unless they block the goal.
5. Execute or produce the requested deliverable.
6. Validate the result at the level required by the claim.

## Output

Default to the smallest useful structure for this domain. Do not emit empty sections merely to satisfy a template.

## Constraints

- Do not invent missing facts or turn placeholders into claims.
- Do not ask for information already present in supplied material or context.
- Do not add unrelated alternatives or architecture.
- Prefer a usable, reversible first version when the user explicitly requests best effort before every detail is known.

## Validation

State what was actually checked. Distinguish static confidence from runtime, visual, external or production verification when relevant.

<!--
Keep global clarification/scope behavior in gpts/kukutx/project-instructions.md.
Add one-level references/ only when domain depth is genuinely task-dependent.
If a real ownership/routing boundary needs regression coverage, add maintenance/behavioral-evals.md.
Use maintenance/sources.md only for substantial source inventories; use decisions.md rarely.
Move ownership when splitting content; do not duplicate rules across files.
Do not create prompt-template.md, examples.md, changelog.md or compatibility stubs by default.
Run tests, python tools/validate_repo.py and the behavioral eval export check before completion.
-->
