---
name: metrics-review
description: Turn business, product or marketing metrics into a KPI report or health check with a scorecard, trends and next actions. Use for weekly or monthly reviews, not for exploring a raw dataset.
---

# Metrics Review

## Use

Use when someone has a set of numbers and wants to know how things are going: a weekly or monthly review, a business snapshot, a campaign wrap-up, "is growth working", or the definition of a report that will be run again.

Exploring or verifying a raw dataset belongs to `data/data-analysis`. Explaining a gap against budget line by line belongs to `finance/variance-analysis`. Drawing the charts belongs to `data/data-visualization`. Reporting progress on work rather than on numbers belongs to `operations/status-report`.

## Domain inputs and blockers

The numbers, the period, and something to compare with: the previous period, the same period last year, or a target. Known events in the period (a launch, an outage, a campaign, a holiday). Without a comparison, say that only a snapshot is possible.

With no data at all, four spoken answers are enough for a small-business snapshot: cash now and roughly a week ago, what is overdue in either direction, this week's sales against a normal week, and what is already worrying the owner. Label the result as supplied by the owner, not measured.

## Numbers that can be trusted

1. **One source of revenue.** The same sale appears in the store, the payment processor and the ledger; adding them can triple it. Choose one (the ledger when there is one), name it, and use the others only for detail such as channel or product split.
2. **Forecast is not revenue.** Deal values in a pipeline are reported separately from what was invoiced or received.
3. **Missing is not zero.** A source that returned nothing is "not available", named once at the end. A zero that would be implausible for a healthy business is read as unknown. An empty date is the worst case, not the newest.
4. **Detail over summary.** When a summary row and its detail lines disagree, sum the lines, and drop "total" rows before ranking.
5. **Complete periods.** Month to date is compared with the same days of the previous month, not with the whole month.
6. **Totals reconcile.** When groups do not add up to the total, say what the difference is. A group with nothing this period shows 0 rather than disappearing.
7. Every ratio states its numerator, denominator and period.

## Reading them

- A metric hierarchy keeps the review short: one north-star metric, five to seven health metrics (acquisition, activation, engagement, retention, revenue, satisfaction), then diagnostic metrics only where something moved.
- Each number carries its comparison and direction. A direction is a trend after about four periods in the same direction; one move is noise.
- A flat total can hide one segment growing and another shrinking; look inside before calling it stable.
- Retention curves: a steep early drop is an activation problem, a steady decline is an engagement problem, a flattening curve is a retained base. A ratio of daily to monthly active users above 0.5 indicates a daily habit, below 0.2 occasional use.
- Read metrics together. Spend up and cost per lead up means the channel is saturating, not scaling. More leads with a falling win rate points at lead quality or response speed, not at marketing. Growth carried by one product is fragile: check the trend without it. Falling satisfaction with steady revenue is an early warning.
- A stage that loses more than about 70% of what enters it is the headline, whatever revenue did.
- Correlation is reported as correlation. Attribution that is not available is stated as not available; revenue is not assigned to campaigns by guesswork. A forecast from fewer than about twelve data points is low confidence and given as a range.

## Status thresholds

Defaults to start from and to retune after a few weeks; the owner's own targets replace them:

| Measure | Green | Yellow | Red |
| --- | --- | --- | --- |
| revenue month over month | flat or up | down up to 5%–10% | down more |
| cash runway | 6 months or more | 3 to 6 | under 3 |
| receivables | nothing past 30 days | something 31 to 60 days late | anything past 60 |
| share of revenue from one channel | under 60% | 60% to 80% | over 80% |
| return on ad spend | 3 or more | 1.5 to 3 | under 1.5 |

The overall status is the worst section's. A named customer, amount and deadline within a week turns the whole report red regardless of the colours.

## Output

- **Review**: a summary a reader gets in thirty seconds (the headline, one win, one concern); the scorecard with metric, current, previous, change, target and status; what is working; what is not, with a hypothesis; then at most three actions ranked by impact, each with what to do, the number that motivates it and what it is worth. When nothing needs doing, say the period was stable instead of inventing actions.
- **Report definition** for a recurring report: name, frequency, period, comparison, grouping, and each metric with its formula and source. One report serves one purpose; eight unrelated metrics are two reports.

Numbers come before adjectives, and specific names before categories: "three invoices past 60 days, the largest 4,100 from one customer", not "collections need attention".

## Constraints

- Do not estimate, round towards a guess or carry forward last period's value for a missing number.
- Do not report vanity totals with no comparison.
- A review that leads to no decision is unfinished; one whose data cannot support a decision says so.
