# Design Handoff

Rules for handing a design to engineering, adapted and rewritten from `anthropics/knowledge-work-plugins` design-handoff (Apache-2.0).

## What a handoff contains

A handoff is a spec an engineer can build from without guessing, and a reviewer can check against without re-reading the design file.

- **Visual specifications** — layout, spacing, typography, colour tokens, radius, elevation, icons, and the exact values for each, taken from the design system where one exists.
- **Interaction specifications** — states (default, hover, focus, disabled, error, loading), transitions, and what happens on each action.
- **Content specifications** — the exact copy, its source, and what varies by state or by data.
- **Edge cases** — empty states, long strings, missing data, error states, and the smallest and largest supported sizes.
- **Accessibility** — keyboard order, focus behaviour, names, contrast pairs, and reduced-motion behaviour.

## Principles

- Values, not pictures: a screenshot is not a spec. Every value an engineer needs is written down.
- One source of truth: tokens and components are referenced by name from the design system, not re-described in the handoff.
- States are specified, not implied: if a state is not listed, it is not built. The default state alone is never a complete handoff.
- Edge cases are part of the handoff, not a follow-up: empty, loading, error and overflow are specified with the happy path.

## Handoff spec shape

1. **Overview** — the feature or screen, its purpose, and its primary action.
2. **Layout** — structure, spacing, and the responsive behaviour at each breakpoint.
3. **Design tokens used** — the named tokens, not raw values.
4. **Components** — each component, its variant, and its props.
5. **States and interactions** — every state and the transition into and out of it.
6. **Responsive behaviour** — what changes, what collapses, and what is hidden at each size.
7. **Edge cases** — empty, error, long content, missing data.
8. **Animation and motion** — durations, easing, and reduced-motion fallbacks.
9. **Accessibility notes** — keyboard, focus, names, and contrast.

## Before the handoff is accepted

The engineer can build it without asking a question that the spec should have answered; the reviewer can check the build against the spec alone; and the spec names its source (the design file and the system version) so a later change can be traced.

## Common faults

| Pattern | Fix |
| --- | --- |
| A screenshot handed over as the spec | Write every value down; a picture is not a spec |
| Only the default state specified | Specify every state: hover, focus, disabled, error, loading |
| Values re-described instead of referenced by token name | Reference tokens and components from the design system |
| Empty, loading and error states missing | Specify them with the happy path, not as a follow-up |
| Long strings and small sizes untested | Specify the smallest and largest supported sizes and the overflow behaviour |
| Motion described as "animate it" | Give durations, easing and reduced-motion fallbacks |
| No source named for the spec | Name the design file and the system version so changes trace |

## Reviewing a handoff

When reviewing a handoff someone else wrote, check it in this order: does it name every value the build needs, or does the engineer have to open the design file to find one; does every component state its variant and its states; are the edge cases present; and does the responsive behaviour say what collapses, in what order, and what is hidden. A handoff that passes those four checks is accepted; one that fails the first is sent back, because the missing value will be invented on the build side.

The reviewer also checks the handoff against the built result, not against the design file. The design file is the intent; the handoff is the contract; the build is judged against the contract.

A handoff is versioned with the design it came from. When the design changes after handoff, the handoff is updated in the same change, with the changed values marked, so the engineer never builds from a stale spec while the designer reviews a new one.

## Source

Adapted and rewritten from `anthropics/knowledge-work-plugins` design/skills/design-handoff, https://github.com/anthropics/knowledge-work-plugins (Apache-2.0).
