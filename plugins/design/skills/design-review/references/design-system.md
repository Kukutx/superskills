# Design System

Rules for auditing, documenting and extending a design system, adapted and rewritten from `anthropics/knowledge-work-plugins` design-system (Apache-2.0).

## What a design system is

Three layers, each with its own owner:

- **Design tokens** — the named values (colour, type, spacing, radius, elevation) that carry every visual decision. One token, one role; a token never carries two jobs.
- **Components** — the reusable pieces, each with a defined API, variants, states and accessibility behaviour.
- **Patterns** — the compositions: how components combine into flows, layouts and recurring screens.

A system is judged by whether a new screen can be built from it without inventing a value, not by how many components it lists.

## Principles

- Tokens before components: a component that invents its own values is not part of the system.
- One component, one job: a component that serves two purposes splits.
- Variants are explicit: every variant, state and size is named and documented, not discovered by reading code.
- The system is the default: deviating from it needs a reason written down at the point of deviation.

## Audit

When auditing an existing system, report in this order:

1. **Summary** — what the system covers, what it does not, and the one-line verdict.
2. **Naming consistency** — the same concept named the same way everywhere; synonyms and near-duplicates listed.
3. **Token coverage** — which decisions have tokens and which are still hard-coded values in components. A hard-coded value that appears in more than one place is a missing token.
4. **Component completeness** — for each component: does it have all its variants, states and sizes, and does its documentation match what it renders.
5. **Priority actions** — ranked by how many future screens each fix unblocks.

## Documenting a component

| Section | What it holds |
| --- | --- |
| Description | What the component is for, in one sentence |
| Variants | Each variant and when it is used |
| Props | Each prop, its type, and its default |
| States | Default, hover, focus, disabled, error, loading |
| Accessibility | Keyboard behaviour, focus, names, contrast |
| Do's and don'ts | One correct use and one incorrect use, each shown |
| Code example | The minimal correct usage |

## Extending the system

A new component starts from the problem, not from a sketch: what task it serves, which existing patterns it reuses, the proposed API and props, its variants and states, the tokens it uses, and its accessibility behaviour. Open questions are listed, not silently decided. The proposal is checked against the existing system first: if a component already covers the job, it is extended, not duplicated.

## Common faults

| Pattern | Fix |
| --- | --- |
| A component inventing its own colour, spacing or type values | Give the decision a token first, then point the component at it |
| Two components doing the same job under different names | Merge them under one name; keep the better API |
| A variant that exists only in code, undocumented | Document every variant, state and size, or remove it |
| A token that carries two jobs | Split it; one token, one role |
| A new screen that invents values instead of using the system | Build from the system and record the deviation with its reason |
| Documentation that does not match what renders | Treat the mismatch as a defect in one of the two, and fix the wrong one |
| A component with no keyboard or focus behaviour documented | Document it; accessibility is part of the component, not an add-on |

## Source

Adapted and rewritten from `anthropics/knowledge-work-plugins` design/skills/design-system, https://github.com/anthropics/knowledge-work-plugins (Apache-2.0).
