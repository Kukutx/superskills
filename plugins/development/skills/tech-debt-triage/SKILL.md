---
name: tech-debt-triage
description: Inventory and rank technical debt by impact, risk and effort, decide what to refactor first and which tests to add, and plan remediation alongside feature work. Not for reviewing a single diff.
---

# Tech Debt Triage

## Use

Use when the question is what to fix in a codebase and in what order: a debt audit, a refactoring backlog, "what should we clean up before it hurts", or which kinds of tests a system is missing.

Reviewing one change belongs to `development/code-review`. Deciding the target architecture belongs to `development/technical-design`. Turning a chosen refactor into file-level tasks belongs to `development/implementation-plan`.

## Domain inputs and blockers

The code or a description of the system, and the pain the team actually feels: where changes are slow, what breaks, what nobody dares to touch. Read the repository when it is available; an inventory built from assumptions about a codebase that could have been inspected is not an audit. Items that could not be verified in the code are marked as reported, not confirmed.

## Categories

| Debt | Examples | What it costs |
| --- | --- | --- |
| code | duplicated logic, poor abstractions, magic numbers | bugs, slow changes |
| architecture | a monolith that should be split, the wrong data store | a ceiling on scale |
| test | low coverage, flaky tests, no integration tests | regressions reach users |
| dependency | outdated or unmaintained libraries | security exposure |
| documentation | missing runbooks, stale README, knowledge in one head | slow onboarding, slow recovery |
| infrastructure | manual deploys, no monitoring, nothing as code | incidents and slow recovery |

## Scoring

Rate each item 1 to 5 for **impact** (how much it slows the team now), **risk** (what happens if it is left) and **effort** to fix. Priority = (impact + risk) × (6 − effort), so cheap fixes to painful or dangerous things rise to the top.

The score orders the list; it does not replace judgement. An item that blocks planned feature work, or carries a known security exposure, is pulled forward whatever its score, and the reason is written next to it.

Each item also gets a rough effort estimate and a business reason in plain terms: what becomes possible, faster or safer once it is fixed.

## Tests worth adding

Choose by the kind of component:

- **API**: unit tests for business logic, integration tests at the HTTP layer, contract tests for consumers.
- **Data pipeline**: input validation, correctness of each transformation, idempotency on re-run.
- **Front end**: component and interaction tests, visual regression, accessibility.
- **Infrastructure**: smoke tests, load tests, failure injection.

Cover first the business-critical paths, error handling, boundaries, security boundaries and data integrity. Skip trivial accessors, framework code and one-off scripts. Many fast unit tests, fewer integration tests, few end-to-end tests.

## Remediation plan

Phase the work so it runs alongside features instead of waiting for a rewrite window. As a default split of capacity, about 70% planned features, 20% technical health and 10% buffer for the unplanned; a mature product or one that just had incidents shifts towards health, a new product towards features.

## Output

The ranked inventory (item, category, impact, risk, effort, priority, estimate, business reason), the gaps in test coverage, and the phased plan with what each phase unlocks.

## Constraints

- Do not recommend a rewrite where a contained refactor removes the risk.
- Do not list style preferences as debt.
- An estimate is labelled an estimate, with what it assumes.
