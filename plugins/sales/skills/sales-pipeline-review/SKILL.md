---
name: sales-pipeline-review
description: Review a sales pipeline or CRM export for stale, stuck and slipping deals, coverage against a target, a commit forecast and win-loss patterns, or set up a spreadsheet CRM. Not for one deal's health.
---

# Sales Pipeline Review

## Use

Use when the subject is the whole book of deals: finding the ones that have gone quiet, checking whether there is enough pipeline for a target, writing a forecast, modelling what happens if a deal slips, learning from closed deals, cleaning up records, or starting a lightweight CRM.

A single deal belongs to `sales/deal-review`. Recording one call belongs to `sales/sales-call-prep-and-recap`. A KPI report across the business belongs to `data/metrics-review`.

## Domain inputs and blockers

A pipeline export or a pasted list with, per deal: name, stage, amount, close date, created date, next step, last activity and contacts. The target or quota for coverage and slip scenarios; without one, ask, because a scenario with no target has no meaning. The previous export, if changes since last time are wanted.

Thresholds below are defaults for a sales cycle of a few months. Two weeks of silence means something different in a 30-day cycle than in a year-long one: adjust to the user's cycle and state the thresholds used.

## Risk flags

| Flag | Definition |
| --- | --- |
| stale | no activity for 14 days or more |
| slipped | close date already passed, or moved back twice or more |
| no next step | the field is empty, or unchanged for 14 days or more |
| stuck | in its stage for more than twice that stage's median time |
| single-threaded | only one contact has any activity |
| incomplete | amount empty or zero; stage with no evidence that its exit criteria were met |

Every open deal needs an owner, a next step and a date. A deal missing any of the three is the one that dies quietly. A good next step reads as date, verb, what, with whom.

Sort flagged deals by amount, then by length of silence. For each, draft the next contact, referring specifically to the last interaction rather than "following up on our conversation".

## Coverage and forecast

- Coverage = weighted open pipeline ÷ the remaining gap to target. Three times the gap is the customary comfort level; below it, say so.
- Forecast buckets: closed won, commit, best case, pipeline. When the user's records carry their own forecast category, use it rather than inferring from stage.
- For each commit and best-case deal, one line: where it stands, what must still happen, and the risk. If the commit total is above the stage-weighted total, the stages are optimistic.
- **A deal that was in the last export and is missing from this one is "closed or removed, outcome not in the file".** It is never assumed won.
- Narrative: the numbers, what changed since last time, risks to commit with mitigation, and what help is needed.

## If a deal slips

Model three cases: it moves to the next period, it shrinks, it is lost. Recompute commit, the gap and coverage for each. Then list what could realistically replace it: best-case deals with activity in the last two weeks and a close date inside the period. A deal that would need to advance more than one stage with under two weeks left is not a realistic replacement. End with one verdict: still on plan, at risk, or not recoverable this period without new pipeline.

## Win-loss review

State the sample size first. Cut win rate by source, deal size, industry and new versus existing customer; show at which stage losses happen, and the median cycle and size of wins against losses. From the largest wins and losses, pull the stated loss reasons, the objections that appear only in losses, and what wins have in common. Lead with the single most important pattern in one or two sentences, with its numbers. Recommendations are of three kinds: change the process, coach a skill, or start recording something that is suspected but not yet provable.

## Record hygiene

For each proposed correction show current value → proposed value with its evidence (the email or note and its date), and let the user approve item by item. Stage and amount are only ever suggested: "we are moving forward" is not a won deal. Contradictory notes are resolved by adding a new note, not by editing history. Nothing is deleted.

## Lightweight CRM

With no CRM, a spreadsheet with four tabs is enough: Contacts, Deals, Activity and a follow-up Queue. Deals use four stages — new, quoted, won, lost — and the next-step column is the one that matters. Activity is append-only: three to five lines per entry with the decision, the numbers and the next step, dated when the event happened. Suggest a real CRM once, when open deals pass roughly 150 or several people edit at the same time.

## Output

Summary (open count and amount, weighted amount, coverage, count and amount at risk); table by stage; flagged deals with the flag and the suggested action; where to focus first. Lead with what needs the user, then what is merely recorded. When nothing crossed a threshold, say so in one line: a quiet review is a good result.

## Constraints

- Data that was not in the export (activity history, emails) is reported as not available, not shown as zero.
- A personal view that comes back empty is questioned, not silently widened to everyone's deals.
- No record is changed, and no message is sent, from here.
