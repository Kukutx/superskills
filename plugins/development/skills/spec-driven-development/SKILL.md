---
name: spec-driven-development
description: Start a feature from a written constitution and clarified spec, with a principles file and a specify then clarify gate. Use when direction is open, not for breaking decided work into tasks.
---

# Spec-Driven Development

## Use

Use when a feature or application is still direction-open and the team needs the direction written down before anything is planned: writing the project's constitution, writing a specification from a feature idea, and running the clarify gate that removes ambiguity before planning starts.

Once direction is set, task breakdown still goes to `development/implementation-plan`. Open architecture questions belong to `development/technical-design`. A PRD with MVP scope belongs to `product/prd-builder`. Fixing an observed failure belongs to `development/bug-diagnosis`, not to this Skill.

This Skill takes only two things from Spec Kit: the constitution principles file and the specify-then-clarify gate. It does not duplicate planning, task decomposition or implementation, which already have owners in this pack.

## The chain

```
constitution -> specify -> clarify -> (implementation-plan, then build)
```

Each step's output is the next step's input. Skipping a step is how a feature drifts: a spec written without a constitution has nothing to be checked against, and a plan written from an unclarified spec bakes the ambiguity into tasks.

## Constitution

A constitution is a short, ratified file of project-level principles that every later step is checked against. It lives in the project, not in a chat transcript, so it can be re-read by every step and amended deliberately.

Write one before the first spec. Keep it short: three to seven core principles, each a named rule with a one-paragraph description, plus the governance rule that the constitution supersedes other practices and that amendments need a recorded approval and a migration plan.

Principle shape, with examples of the kind of rule that belongs here:

- **Library-first.** Every feature starts as a standalone, independently testable unit with a clear purpose; no organisational-only units.
- **Test-first (non-negotiable).** Tests are written and approved before implementation; the red-green-refactor cycle is enforced, not aspirational.
- **Explicit interfaces.** Every unit exposes its functionality through a defined interface with text in and out and errors on a separate channel.
- **Simplicity.** Start simple; a more complex approach must be justified in writing.

Add sections only for constraints that genuinely bind later decisions: additional constraints, security requirements, performance standards, the development workflow. A principle that no step ever checks is decoration; delete it.

Version the file (semantic version, ratified date, last amended date). When a later step conflicts with the constitution, the constitution wins and the step is reworked, or the constitution is amended explicitly with a recorded rationale. Silent drift is the failure mode.

## Specify

Turn a feature idea into a written specification before any plan exists. The spec answers, in order:

1. **What and why.** The feature in two to four words as a short name, the problem it solves, and the outcome that proves it worked.
2. **Who and what for.** The users, their goal, and what is explicitly out of scope.
3. **Requirements.** Functional requirements as testable statements, each with a success criterion that can be checked without the author's help.
4. **Constraints.** What the constitution imposes, plus technical, data and interface constraints that bind the design.
5. **Open questions.** Anything unknown, listed explicitly rather than silently assumed.

Quality bar before the spec leaves this step:

- Every requirement has a stated success criterion; a requirement that cannot be checked is rewritten or dropped.
- Scope is explicit on both sides: what is in, and what is deliberately out.
- No requirement depends on a fact that only exists in someone's head. If it does, it goes in Open questions.
- The spec is consistent with the constitution. A conflict is resolved here, not deferred to implementation.

## Clarify gate

Clarify runs after specify and before any planning. It is a gate, not a discussion: the spec does not advance until the gate passes or its unresolved items are explicitly deferred with a rationale.

1. **Scan the spec for ambiguity and coverage** across functional scope, data, interfaces, edge cases, non-functional requirements and success criteria. Mark each category Clear, Partial or Missing.
2. **Ask at most five questions**, one at a time, highest-impact first. A question earns its place only if the answer would change the spec. Do not ask about a technology choice unless its absence blocks functional clarity.
3. **Integrate each accepted answer into the spec immediately**, updating the affected requirements and marking the coverage map again. Do not batch answers for the end.
4. **Stop conditions.** If no meaningful ambiguities are found, say so and suggest proceeding. If the user says stop, done or proceed, stop. If the question quota is reached with high-impact items unresolved, list them as Deferred with the reason each was deferred, and the plan carries them as risks.
5. **Re-validate** the spec quality checklist after the gate: every requirement still has a success criterion, scope is still explicit, and the constitution still holds.

Never invent an answer to a clarification question. An unanswered high-impact question is a deferred risk, not a default.

## Handoff

The clarified spec is the handoff artifact. It goes to `development/implementation-plan` for file-level tasks and tests, and to `development/technical-design` if an architecture decision is still open. The constitution stays with the project and is re-checked at review time: a change that violates it is sent back or amends the constitution explicitly.

## Output

1. **Constitution** — principles, governance, version and dates.
2. **Specification** — short name, problem and outcome, users, requirements with success criteria, constraints, open questions.
3. **Clarify record** — questions asked with answers integrated, items deferred with rationale, coverage summary.
4. **Handoff note** — what goes to implementation-plan, and any open architecture question for technical-design.

## Constraints

- Do not plan, decompose into tasks, or write implementation steps here. That is implementation-plan's job once direction is set.
- Do not write a spec without a constitution to check it against, and do not skip the clarify gate because the spec "looks clear".
- Do not ask more than five clarification questions, and do not ask a question whose answer would not change the spec.
- Do not resolve a constitution conflict silently. The constitution wins, or it is amended on the record.

## Source

Adapted and rewritten from `github/spec-kit` (constitution template, specify and clarify commands), https://github.com/github/spec-kit (MIT). Only the constitution principles file and the specify-then-clarify gate are taken; planning, task decomposition and implementation are intentionally not duplicated here.
