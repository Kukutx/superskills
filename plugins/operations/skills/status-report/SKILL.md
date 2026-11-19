---
name: status-report
description: Write a weekly or monthly status report, stakeholder update or release announcement with honest status, risks and decisions needed, for executives, the team or customers. Not for KPI analysis.
---

# Status Report

## Use

Use when progress has to be reported to someone: a regular update to a manager, client or investor, a project status, an escalation of a risk, a release announcement, or the same news rewritten for a different audience.

Analysing the numbers themselves belongs to `data/metrics-review`. A one-to-one email with a negotiating position belongs to `writing/business-email`. Updates during an outage belong to `operations/incident-response`.

## Domain inputs and blockers

Four facts are needed and come only from the user: what was completed since the last update, what is in progress or blocked, the risks, and what is needed from the reader. Add the audience and the period. A metric with no value supplied is marked as missing, not estimated.

## Status

Use three states and mean them:

- **Green — on track.** On plan with no significant risk. It is a claim, not the default.
- **Yellow — at risk.** Behind plan or a risk has appeared and mitigation is under way with an uncertain outcome. Turn yellow at the first sign, not when it is certain; yellow is not a failure.
- **Red — off track.** Significantly behind with no clear mitigation, or the writer has run out of options and needs help.

Back to green only when the risk is resolved, not postponed. Every change of colour states its reason.

## What each audience needs

| Audience | Lead with | Leave out |
| --- | --- | --- |
| executives, investors, clients | the conclusion, status, progress against goals, risks with mitigation, the specific ask, the next milestone | activity counts and process detail |
| the team | what shipped, what is in progress and who owns it, blockers, decisions pending with options, changes of priority | restating what everyone knows |
| partner teams | what is coming that affects them, what is asked of them and by when | internal debate |
| customers | what is new in terms of benefit, what is coming, known issues with workarounds, how to give feedback | internal names, ticket numbers, anything not yet committed |

## Rules

1. The first three lines carry the message; a busy reader stops there.
2. Bad news comes first and early. A risk buried under good news, or reported late, costs more trust than the risk itself.
3. A risk is communicated in five parts: what it is, its impact in numbers, how likely it is, what is being done, and what is asked of the reader. Only list risks the reader can do something about or must know.
4. An ask is specific: "a decision on X by Friday", not "we need support". Each decision needed comes with the background and a recommendation, so it is easy to make.
5. Outcomes, not activity: "checkout conversion up from 2.1% to 2.6%" instead of "held 14 meetings and closed 23 tickets".
6. An executive update fits in about 200 to 300 words.

## Output

A regular report: summary in three or four sentences; overall status; key metrics with target, actual and trend; accomplishments; work in progress; risks and issues; decisions needed with deadline and recommendation; priorities for the next period.

A release announcement for customers: what changed and why it matters to them, how to use it, known limits, where to ask.

## Constraints

- Do not choose a brighter colour than the facts support, and do not soften a risk the user stated.
- Do not announce a date, a feature or a number the user has not confirmed.
- Confidential figures and internal names stay out of any version meant for outside readers.
