---
name: deal-review
description: Review one B2B deal or customer account for health, qualification gaps, stakeholders, what blocks the next stage and renewal or churn risk. Use to judge will this deal close, not a whole pipeline.
---

# Deal Review

## Use

Use when the subject is one deal or one account: is it real, what is missing, who is involved, what would move it, whether a customer is healthy or likely to leave at renewal.

Many deals at once belong to `sales/sales-pipeline-review`. Preparing the next call belongs to `sales/sales-call-prep-and-recap`. Buying a company belongs to `finance/deal-diligence`. Researching a company with no sales judgement belongs to `research/research-brief`.

## Domain inputs and blockers

The deal as the user knows it: stage, amount, expected close date, who has been involved, and the notes, emails or transcripts they can paste. The qualification framework they use, if any; otherwise budget, authority, need and timing serve as the default and are named as such.

The review is limited to signals that can be seen in the material. Say which were not visible instead of scoring them as absent.

## Qualification

Mark each element confirmed, assumed or unknown, with specific evidence: "the finance lead confirmed the budget on the call of the 12th", not "budget seems fine". Assumed is not confirmed, and most optimistic deals are built on assumed.

## Probability

Start from the stage's usual probability and adjust for what the evidence shows. A working set of adjustments, in percentage points:

| Signal | Adjust |
| --- | --- |
| champion recently active | +10 |
| executive sponsor identified and met | +10 |
| mutual close plan agreed | +10 |
| three or more contacts engaged | +5 |
| no activity for two weeks | −10 |
| champion silent for two weeks | −15 |
| single contact only | −10 |
| a competitor is present | −10 |
| close date already slipped twice or more | −10 |
| a pricing gap between ask and position | −10 |
| an open dispute or withheld payment on the account | −10 |
| a new stakeholder appearing late | −5 |

Keep the result between 5% and 95%, show the sum, and treat the weights as defaults: the user's own win history overrides them, and two weeks of silence means less in a long sales cycle than in a short one.

Then check the stage against reality: matches the evidence, ahead of the evidence (stage says proposal, but no proposal exists and price was never discussed), or understated.

## Stakeholders

- A champion is someone who has done something for the deal: made an introduction, shared internal information, pushed a meeting. Enthusiasm on a call is not championship.
- Name the roles that are missing: the economic buyer, security or legal, an executive sponsor.
- Count the people actually engaged in the last 30 days and how each was reached.

## What blocks the next stage

List only the gaps that block progress, not every unknown: a missing champion blocks; an unconfirmed budget figure in early discovery may not. For each: who owns it (the customer, the user, someone else inside), what it blocks, and the evidence.

Sequence them: what can run in parallel, what is strictly serial, and the one action that unlocks the most downstream. If the earliest credible close date from that path is later than the stated one, say so. Items already in motion are not requested again.

A close plan works backwards from the signature date and includes the real turnaround of the customer's internal approvals; a step that makes the date impossible is flagged.

## Existing customers

Health on five dimensions, each green, yellow or red or "not visible": relationship, engagement trend, commercial, support, and value delivered.

Renewal risk rises with no activity for 30 days, a change of champion or buyer, an unresolved escalation, or falling usage; it falls with an expansion conversation in progress or a multi-year or auto-renewing term. Start the renewal conversation at least 90 days ahead. A contractual notice date within 45 days is flagged whatever the close date says.

An expansion idea needs at least one piece of evidence and is one of four kinds: another product, another team, another region or entity, or more volume. Sizes are not invented.

## Output

Health verdict in one line; the numbers (stage and its reality label, amount, close date, age, usual and adjusted probability with the adjustments); the qualification table with evidence; strengths; risks with evidence and mitigation; what is missing; next steps, most important first, with who and when.

## Constraints

- Do not present an inference about the customer's priorities as something they said.
- Do not score a dimension that the material does not show.
- The review proposes updates to the user's records; it changes nothing.
