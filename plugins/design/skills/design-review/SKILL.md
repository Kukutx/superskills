---
name: design-review
description: Critique a UI screen, mockup or screenshot for usability, visual hierarchy, consistency and WCAG accessibility, with severity-ranked fixes. Use for interface reviews, not for generated artwork.
---

# Design Review

## Use

Use when the user shows an interface (screenshot, mockup, live page or a description of one) and wants to know what is wrong with it or whether it is accessible.

A generated or illustrated image judged against its purpose belongs to `design/image-review-refiner`. Store screenshots as marketing assets belong to `design/app-store-assets`.

## Domain inputs and blockers

- **Stage.** Feedback on an early exploration is about direction; feedback on a near-final screen is about defects. When the stage is not stated, read it from the fidelity of what was shown and say which one was assumed.
- **Who it is for and what they are trying to do on this screen.** Usability is judged against that task.
- **Colour values.** A contrast ratio is computed from the actual foreground and background values. From a screenshot alone, a suspicious pair is reported as "to be measured", never with an invented ratio.

## Review order

1. **First impression**: where the eye lands in the first two seconds, whether that is the right place, and whether the screen's purpose is obvious.
2. **Usability**: can the task be completed, is the next step clear, are errors and empty states handled.
3. **Visual hierarchy**: reading order, emphasis, competing elements.
4. **Consistency**: the same thing looks and is named the same everywhere.
5. **Accessibility**: the checks below.

Each finding is specific ("the secondary button competes with the primary one" rather than "the layout is cluttered"), gives the reason in terms of the user's task, and proposes a change. Say what already works, so it is not lost in the redesign.

## Accessibility checks

Start with contrast and keyboard, since they are the most common failures and block the most people.

| Check | Requirement | WCAG |
| --- | --- | --- |
| text contrast | at least 4.5:1, or 3:1 for large text | 1.4.3 (AA) |
| contrast of UI components and graphics | at least 3:1 against adjacent colours | 1.4.11 (AA) |
| keyboard | every function is operable by keyboard, with no trap | 2.1.1, 2.1.2 (A) |
| focus | order follows the visual order and the focus indicator is visible | 2.4.3 (A), 2.4.7 (AA) |
| text resize | usable at 200% without loss of content or function | 1.4.4 (AA) |
| target size | at least 24×24 CSS pixels; 44×44 is the enhanced level | 2.5.8 (AA), 2.5.5 (AAA) |
| images | meaningful images have a text alternative | 1.1.1 (A) |
| forms | inputs have labels; errors are identified and described in text | 3.3.2, 3.3.1 (A) |
| components | custom controls expose name, role and value | 4.1.2 (A) |

Also look for auto-playing media without controls and time limits that cannot be extended.

An automated scan finds only a minority of accessibility problems. A review from a picture is a starting point; keyboard-only navigation and a screen reader pass on the real build are still needed, and the report says so.

## Output

- **Overall impression**, one or two sentences.
- **Findings**, ordered by severity: Critical (blocks the task or excludes a group of users), Major, Minor. Each with location, why it matters, the fix, and the WCAG criterion when it is an accessibility finding.
- **What works well.**
- **Top three changes**, with the reason for the order.

A dedicated accessibility audit adds a contrast table (element, foreground, background, ratio, required, pass) and the keyboard walk-through.

## Constraints

- Do not report a measured ratio, size or timing that was not measured.
- Do not redesign the screen when the request is to review it; alternatives are attached to findings.
- Keep taste separate from defects: a preference is labelled as a preference.
- Conformance is claimed against a named WCAG version and level, and only for what was checked.
