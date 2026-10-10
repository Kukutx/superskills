---
name: technical-design
description: Decide general software architecture, ownership, interfaces and failure behavior when key technical decisions are still unresolved. Use before file-level implementation planning; prefer a domain-specific design skill when available.
---

# Technical Design

## Use

Use when the implementation direction still depends on decisions such as ownership, data model, interfaces, consistency, security, failure handling or migration strategy.

Do not use when the architecture is already agreed and the user mainly needs concrete files/tasks; use `development/implementation-plan`. For sequencing a broader multi-workstream project, use `planning/project-planner`.

## Workflow

1. Inspect the current stack and existing boundaries before inventing new architecture.
2. Define only the requirements that materially affect design: data ownership, consistency, auth, scale, latency, failure modes and compatibility.
3. Prefer the smallest design that fits current needs and has a clear upgrade path.
4. Specify interfaces and data contracts where ambiguity would cause implementation errors.
5. Make migration, rollback and failure behavior explicit for risky changes.
6. Compare alternatives only when the tradeoff is real enough to affect the decision.
7. End with the decisions an implementation plan can safely treat as fixed.

## Output

Default:

- **Recommended design**
- **Key components / ownership**
- **Data + interface contracts** when relevant
- **Important flows / failure behavior**
- **Migration / rollout** when relevant
- **Tradeoffs / risks**
- **Validation plan**
- **Decisions fixed for implementation** when useful

Do not include sections that are irrelevant to the task.

## Constraints

- Existing project conventions beat generic architecture preferences unless they are the problem.
- Do not add queues, microservices, event buses, caches or new storage layers without a demonstrated need.
- Do not ignore authorization, data integrity or rollback on sensitive changes.
- Do not hide assumptions about scale or consistency.
- Do not expand into a file-by-file task list unless the user also asks for implementation planning.
- A technical design should be implementable; avoid diagrams/terms with no concrete ownership or interface.
