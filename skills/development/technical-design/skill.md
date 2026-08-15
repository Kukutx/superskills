---
name: technical-design
description: Design the simplest robust technical solution for a general software feature or system when no more specific domain skill owns the architecture.
---

# Technical Design

## Workflow

1. Inspect the current stack and existing boundaries before inventing new architecture.
2. Define the requirements that materially affect design: data ownership, consistency, auth, scale, latency, failure modes, compatibility.
3. Prefer the smallest design that fits current needs and has a clear upgrade path.
4. Specify interfaces and data contracts where ambiguity would cause implementation errors.
5. Make migration, rollback and failure behavior explicit for risky changes.
6. Compare alternatives only when the tradeoff is real enough to affect the decision.

## Output

Default:

- **Recommended design**
- **Key components / ownership**
- **Data + interface contracts** when relevant
- **Important flows / failure behavior**
- **Migration / rollout** when relevant
- **Tradeoffs / risks**
- **Validation plan**

Do not include sections that are irrelevant to the task.

## Constraints

- Existing project conventions beat generic architecture preferences unless they are the problem.
- Do not add queues, microservices, event buses, caches or new storage layers without a demonstrated need.
- Do not ignore authorization, data integrity or rollback on sensitive changes.
- Do not hide assumptions about scale or consistency.
- A technical design should be implementable; avoid diagrams/terms with no concrete ownership or interface.