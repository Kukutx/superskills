---
name: project-planner
description: Turn a broad multi-step goal into a realistic cross-workstream roadmap with deliverables, dependencies, risks and immediate next actions. Use for project sequencing, not file-level software implementation.
---

# Project Planner

## Use

Use when the user needs sequencing, prioritization or a roadmap across multiple deliverables/workstreams.

Do not use for a single fix, a file-level software execution plan, or a domain task that already has a more specific planning workflow. For unresolved software architecture use `development/technical-design`; for an approved software direction that needs concrete files/tasks use `development/implementation-plan`.

## Workflow

1. Define the outcome and current starting point.
2. Identify hard constraints: deadline, people, budget, tools and external dependencies.
3. Split work by concrete deliverable/workstream, not generic project-management phases.
4. Order work by dependency and risk.
5. Put uncertain/high-risk work early enough to invalidate bad assumptions cheaply.
6. Identify blocking decisions separately from executable tasks.
7. End with the smallest executable next actions.

If no deadline exists, use phases rather than inventing dates.

## Output

Default:

- **Goal / done state**
- **Workstreams / deliverables**
- **Sequence + dependencies**
- **Main risks / blocking decisions**
- **Next 3 actions**

Add timeline, owners or sprint structure only when useful.

## Constraints

- Do not invent unrealistic deadlines.
- Do not turn every item into vague “research / implement / test” language.
- Keep dependencies and blocking decisions visible.
- Prefer fewer concrete deliverables over a long checklist.
- Do not drift into file-by-file implementation when another Skill owns that level of detail.
- Domain-specific implementation details should stay in the relevant domain Skill.
