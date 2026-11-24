---
name: revops
description: Design revenue operations with lifecycle stages, MQL/SQL definitions, lead scoring, handoff, routing and CRM automation. Use when sales and marketing disagree on leads, not for outreach.
---

# RevOps

## Use

Use when the work is the revenue system itself: lifecycle stages, MQL and SQL definitions, lead scoring, routing and the marketing-to-sales handoff, pipeline stages, CRM automation, deal-desk rules, or the metrics that show where revenue leaks.

Writing outbound emails belongs to `sales/sales-outreach`. Reviewing the health of an existing pipeline belongs to `sales/sales-pipeline-review`. A marketing plan belongs to `marketing/marketing-plan`. Which marketing drove revenue belongs to `marketing/marketing-attribution`.

## Before starting

Work with whatever the user gives; do not block on missing inputs, and note what would strengthen the solution. Gather what is available:

1. **Go-to-market motion** — product-led, sales-led, or hybrid.
2. **Average contract value** and **sales cycle length** (first touch to closed-won).
3. **Current stack** — CRM, marketing automation, scheduling, enrichment.
4. **Current state** — how leads are managed today, what works, what does not.
5. **Goal** — more conversions, faster speed-to-lead, fixing handoff leaks, or building from scratch.

## Core principles

- **Single source of truth.** One system of record for every lead and account. If data lives in several places it will conflict. Pick a CRM as canonical and sync everything to it.
- **Define before automating.** Stage definitions, scoring criteria and routing rules are agreed on paper before any workflow is built. Automating a broken process creates broken results faster.
- **Measure every handoff.** Marketing-to-sales, SDR-to-AE, AE-to-customer-success: each handoff is a potential leak and needs an SLA, a tracking mechanism and someone accountable for follow-through.
- **Revenue-team alignment.** Marketing, sales and customer success must agree on definitions. If marketing calls something an MQL but sales will not work it, the definition is wrong.

## Lead lifecycle

| Stage | Entry criteria | Exit criteria | Owner |
| --- | --- | --- | --- |
| Subscriber | Opts in to content | Provides company info or shows engagement | Marketing |
| Lead | Identified contact with basic info | Meets minimum fit criteria | Marketing |
| MQL | Passes fit plus engagement threshold | Sales accepts or rejects within SLA | Marketing |
| SQL | Sales accepts and qualifies in conversation | Opportunity created or recycled | Sales (SDR/AE) |
| Opportunity | Budget, authority, need and timeline confirmed | Closed-won or closed-lost | Sales (AE) |
| Customer | Closed-won deal | Expands, renews, or churns | Customer success |
| Evangelist | High NPS, referral activity, case study | Ongoing programme participation | Customer success / Marketing |

Outbound contacts follow their own stages (targeted, in sequence, replied, positive, meeting booked, meeting held, opportunity), with fields for signal, tier, sequence and channel so meetings can be attributed.

### MQL definition

An MQL requires both fit and engagement. Neither alone is sufficient: a perfect-fit company that never engages is not an MQL, and a student downloading every ebook is not an MQL.

- **Fit score** — does this person match the ideal customer profile (company size, industry, role, tech stack)?
- **Engagement score** — have they shown buying intent (pricing page, demo request, repeated visits)?

### MQL-to-SQL handoff SLA

- MQL alert sent to the assigned rep.
- Rep contacts within 4 hours in business hours.
- Rep qualifies or rejects within 48 hours.
- Rejected MQLs go to recycling nurture with a reason code.

## Lead scoring

### Scoring dimensions

- **Explicit (fit)** — who they are: company size, industry, revenue, job title, seniority, department, tech stack, geography.
- **Implicit (engagement)** — what they do: page visits (pricing, demo and case-study pages weigh most), content downloads, webinar attendance, email engagement, product usage for product-led motions.
- **Negative (disqualifying)** — competitor email domains, student or personal email, unsubscribes and spam complaints, title mismatches such as intern or student.

### Building a scoring model

1. Define ideal-customer attributes and weight them.
2. Identify high-intent signals from a cohort with won and lost outcomes, using only features available at the qualification decision.
3. Set point values for each attribute and behaviour.
4. Set the MQL threshold, typically 50–80 points on a 100-point scale.
5. Freeze the rule and test a later, fully observed holdout against the current routing baseline; report precision, recall, missed wins, false positives and workload.
6. Pilot with monitoring and rollback; tune on development cohorts and keep an untouched holdout for each promotion.

### Common scoring mistakes

- Weighting content downloads too heavily (research is not buying intent).
- No negative scoring, so bad leads pass through.
- Set and forget: buyer behaviour changes, so recalibrate quarterly.
- Scoring all page visits equally (a pricing page is not a blog post).

## Lead routing

| Method | How it works | Best for |
| --- | --- | --- |
| Round-robin | Distributed evenly across reps | Equal territories, similar deal sizes |
| Territory-based | Assigned by geography, vertical or segment | Regional teams, industry specialists |
| Account-based | Named accounts go to named reps | Account-based motions, strategic accounts |
| Skill-based | Routed by deal complexity, product line or language | Diverse product lines, global teams |

Routing rules:

- Route to the most specific match first, then fall back to general.
- Include a fallback owner. Unassigned leads go cold fast and waste pipeline.
- Round-robin accounts for rep capacity and availability (time off, quota attainment).
- Log every routing decision for audit and optimisation.

### Speed-to-lead

Response time is the largest single factor in lead conversion. Contact within 5 minutes is far more likely to qualify than contact after 30 minutes, and after 24 hours the lead is effectively cold. Build routing that prioritises speed, alert reps immediately, and escalate when an SLA is missed.

## Pipeline stages

| Stage | Required fields | Exit criteria |
| --- | --- | --- |
| Qualified | Contact info, company, source, fit score | Discovery call scheduled |
| Discovery | Pain points, current solution, timeline | Needs confirmed, demo scheduled |
| Demo / Evaluation | Technical requirements, decision makers | Positive evaluation, proposal requested |
| Proposal | Pricing, terms, stakeholder map | Proposal delivered and reviewed |
| Negotiation | Redlines, approval chain, close date | Terms agreed, contract sent |
| Closed Won | Signed contract, payment terms | Handoff to customer success complete |
| Closed Lost | Loss reason, competitor if any | Post-mortem logged |

Stage hygiene:

- **Required fields per stage.** Reps cannot advance a deal without them.
- **Stale-deal alerts.** Flag deals sitting in a stage beyond the average time (about twice the average days).
- **Stage-skip detection.** Alert when deals jump stages, for example Qualified straight to Proposal.
- **Close-date discipline.** Pushed dates carry a reason; no silent pushes.

### Pipeline metrics

| Metric | What it tells you |
| --- | --- |
| Stage conversion rates | Where deals die |
| Average time in stage | Where deals stall |
| Pipeline velocity | Revenue per day through the funnel |
| Coverage ratio | Pipeline value against quota (target 3–4x) |
| Win rate by source | Which channels produce real revenue |

## CRM automation

Essential automations: lifecycle stage updates when criteria are met; a follow-up task when an MQL is assigned; SLA alerts to the manager when response time is missed; deal-stage triggers that send proposals, update forecasts and notify customer success on close.

Marketing-to-sales automations: instant MQL alert to the assigned rep with lead context; notification when a prospect books a meeting; a daily digest of high-intent actions by active leads; a re-engagement alert when a dormant lead returns to the site.

Scheduling: round-robin meeting distribution; routing by criteria (enterprise leads to senior reps, SMB to junior reps); pre-meeting enrichment of the CRM record; automatic follow-up on no-shows.

## Deal desk

A deal desk is needed when the average contract value is above the non-standard threshold (about $25K, or the user's own threshold), for non-standard payment terms, multi-year contracts with custom pricing, volume discounts beyond published tiers, or custom legal terms and SLAs.

| Deal size | Approval required |
| --- | --- |
| Standard pricing | Auto-approved |
| 10–20% discount | Sales manager |
| 20–40% discount | VP Sales |
| 40%+ discount or custom terms | Deal desk review |
| Multi-year / enterprise | Finance plus Legal |

Document every exception. Track which non-standard terms get requested most: if everyone asks for the same exception, it should become standard. Review quarterly.

## Data hygiene and enrichment

- **Dedup.** Match on email domain plus company name plus phone; the CRM record wins over marketing automation, and the most recent activity wins for fields. Run scheduled dedup weekly with manual review for edge cases.
- **Required fields.** Enforce them at each lifecycle stage and block stage advancement when they are empty. Use progressive profiling instead of demanding everything upfront.
- **Quarterly audit.** Merge duplicates, validate deliverability on stale emails, archive contacts with no activity in 12 months, audit lifecycle-stage distribution for bottlenecks, and verify enrichment accuracy on a sample.

## RevOps metrics

| Metric | Definition | Benchmark |
| --- | --- | --- |
| Lead-to-MQL rate | MQLs / total leads | 5–15% |
| MQL-to-SQL rate | SQLs / MQLs | 30–50% |
| SQL-to-Opportunity | Opportunities / SQLs | 50–70% |
| Pipeline velocity | (deals × average deal size × win rate) / average sales cycle | Varies by ACV |
| CAC | Total sales plus marketing spend / new customers | LTV:CAC above 3:1 |
| LTV:CAC ratio | Customer lifetime value / CAC | 3:1 to 5:1 healthy |
| Speed-to-lead | Time from form fill to first rep contact | Under 5 minutes ideal |
| Win rate | Closed-won / total opportunities | 20–30% (varies) |

Build three dashboard views: a marketing view (lead volume, MQL rate, source attribution, cost per MQL), a sales view (pipeline value, stage conversion, velocity, forecast accuracy), and an executive view (CAC, LTV:CAC, revenue against target, pipeline coverage).

## Output

Deliver as standalone documents the user can implement directly:

1. **Lifecycle stage document** — stage definitions with entry and exit criteria, owners and SLAs.
2. **Scoring specification** — fit and engagement attributes with point values and the MQL threshold.
3. **Routing rules document** — decision tree with assignment logic and fallbacks.
4. **Pipeline configuration** — stage definitions, required fields and automation triggers.
5. **Metrics dashboard spec** — key metrics, data sources and target benchmarks.

Include platform-specific guidance when the CRM is known.

## Constraints

- Do not automate a process whose definitions are not yet agreed on paper.
- Do not call a lead an MQL on fit or engagement alone.
- Do not route without a fallback owner.
- Do not report pipeline metrics without naming the source system and the period.

## Source

Adapted and rewritten from `coreyhaines31/marketingskills` skills/revops, https://github.com/coreyhaines31/marketingskills (MIT).
