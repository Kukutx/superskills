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

## Domain inputs and blockers

List only domain-specific facts whose absence could materially change correctness, safety or final direction.

Before asking the user:

- inspect supplied files and context;
- obtain discoverable facts with available tools;
- use the smallest convention-aligned default for harmless, reversible choices;
- escalate only user-only decisions, truth-critical missing facts or consequential actions that are not already authorized.

Do not repeat the global autonomy/clarification policy here.

## Workflow

1. Inspect the relevant context and existing conventions.
2. Identify the smallest decision or implementation path that solves the requested task.
3. Load task-dependent references only when their decision boundary is reached.
4. Execute or produce all safe, reversible work already authorized by the request.
5. Validate at the level required by the completion claim and self-correct from failures.
6. Stop only at a true blocker or consequential final boundary that requires user input.

## Output

Default to the smallest useful structure for this domain. Put the requested result first and do not emit empty sections merely to satisfy a template.

## Constraints

- Do not invent missing facts or turn placeholders into claims.
- Do not ask for information already present in supplied material or connected context.
- Do not add unrelated alternatives or architecture.
- Do not stop at a plan when the user asked for execution and this Skill owns the work.
- Do not add generic permission, confirmation or tool-use rules that belong in project instructions.

## Validation

State what was actually checked. Distinguish static confidence from runtime, visual, external or production verification when relevant. Keep verification proportional to the change; broaden it only when failures or unresolved risk justify it.

<!--
Keep global autonomy/escalation/scope behavior in gpts/kukutx/project-instructions.md.
Add one-level references/ only when domain depth is genuinely task-dependent.
If a real ownership/routing/blocker boundary needs regression coverage, add maintenance/behavioral-evals.md.
Use maintenance/sources.md only for substantial source inventories; use decisions.md rarely.
Move ownership when splitting content; do not duplicate rules across files.
Do not create prompt-template.md, examples.md, changelog.md or compatibility stubs by default.
Run tests, python tools/validate_repo.py and the behavioral eval export check before completion.
-->
