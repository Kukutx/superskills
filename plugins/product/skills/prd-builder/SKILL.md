---
name: prd-builder
description: Turn a product or feature idea into a narrow, buildable PRD with MVP scope, out-of-scope, user flows and testable acceptance criteria. Use for PRDs and feature specs, not technical architecture.
---

# PRD Builder

## Workflow

1. Define the user problem before listing features.
2. Identify the smallest behavior change that solves it.
3. Separate MVP from later ideas.
4. Write acceptance criteria that can be observed or tested.
5. Surface dependencies, risky assumptions and unresolved product decisions.
6. Hand technical design to a domain/development Skill rather than embedding speculative architecture in the PRD.

## Scope and quality rules

- A requirement is must-have only if the feature no longer solves the core problem without it. When everything is must-have, nothing is.
- Goals describe outcomes ("halve the time to first value"), not outputs ("build an onboarding wizard").
- Out of scope lists the things a reader might expect, each with the reason it is left out.
- A user story names a specific user, a capability and the benefit, and does not prescribe the solution. A refactor is a task, not a story.
- Acceptance criteria cover the normal path, errors, edge cases and what must not happen, each testable on its own.
- A success metric has a target, a way to measure it and a date on which it is judged. Leading signals (adoption, completion) are kept apart from lagging ones (retention, revenue).
- Adding scope means removing scope or moving the date. An open question names who can answer it and whether it blocks; one the context already answers is not listed.

## Output

Default:

- **Problem / target user**
- **MVP outcome**
- **In scope**
- **Out of scope**
- **Key user flows / stories**
- **Acceptance criteria**
- **Risks / open decisions**
- **Success signal** when a meaningful metric is available

## Constraints

- Do not inflate a small feature into a product strategy document.
- Do not invent user research, traction or metrics.
- “Easy”, “fast”, “intuitive” are not acceptance criteria by themselves.
- Keep implementation detail out unless it materially constrains product behavior.
- If the user already has a clear spec, refine gaps instead of rewriting everything.
- A PRD meant for other readers is ready when someone without this conversation's context can answer, from the document alone, what is being built, for whom, and how to tell it is done.