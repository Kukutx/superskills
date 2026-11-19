---
name: change-management
description: Write a change request or rollout plan with impact analysis, a risk register, communication plan and rollback triggers, or optimize a slow process. Not for a release go/no-go check.
---

# Change Management

## Use

Use when something that people or systems depend on is about to change and the change needs to be assessed, approved, communicated and reversible: a migration, a new tool, a price or policy change, a reorganized process. Also use for a risk register on its own, and for finding what makes an existing process slow.

The checklist on the day of a software release belongs to `operations/release-checklist`. A document for a procedure that already runs the same way each time belongs to `operations/sop-builder`. A schedule across workstreams belongs to `planning/project-planner`.

## Domain inputs and blockers

What is changing, who and what it touches, when, and who must approve. An approver that is not known is left as pending in the document, not guessed.

## Impact

"Everyone" is not an impact assessment; "the 200 users of the billing team" is. State the impact on four faces — users, systems, process, cost — each as high, medium, low or none, with the number of people or the systems named.

Size the change (low, medium, high) and say where resistance is expected and why.

## Risk register

Rate each risk for likelihood and impact:

| Likelihood \ Impact | Low | Medium | High |
| --- | --- | --- | --- |
| High | medium | high | critical |
| Medium | low | medium | high |
| Low | low | low | medium |

A catastrophic outcome is escalated whatever its likelihood. Each entry has a description, the rating, a specific mitigation, an owner and a status (open, mitigated, accepted, closed). Keep to the risks that matter and can be influenced; a register of thirty generic risks is read by no one.

## Rollback

Every change has one, however confident the author is, and it is agreed before the change starts:

- the **trigger**, as an observable condition (an error rate, a failed critical flow, a missed checkpoint), not "if things go badly";
- the **steps**;
- how to **verify** that the rollback worked.

A change that cannot be rolled back says so explicitly, so the approver knows what they are accepting.

## Communication

- Explain why before what.
- Say what people are losing, not only what they gain; unacknowledged losses turn into resistance.
- Early and more than once, through more than one channel, with a named place for questions.
- Each audience hears what changes for them and what they need to do by when.

## Process optimization

Map the current state first: each step, decision and hand-off, who does it and how long it takes, marking manual steps, approvals and waiting.

Look for five kinds of waste: waiting, rework, hand-offs (each is a point of delay or loss), steps that add no value, and manual work that could be automated.

Design the future state by removing steps, automating, reducing hand-offs, running independent steps in parallel, and using checkpoints instead of gates wherever work does not have to stop for an approval.

## Output

- **Change request**: description, justification, impact table, risk register, implementation plan (step, owner, time, dependency), communication plan, rollback, approvals required.
- **Risk register** alone when that is the request, sorted by rating.
- **Process review**: current and future flow side by side, each improvement with its estimated effect and how it will be measured.

## Constraints

- Do not invent approvers, dates, user counts or measured durations; unknowns are marked.
- Do not present a change as low risk because its rollback is untested.
- Estimated savings are labelled as estimates with their basis.
