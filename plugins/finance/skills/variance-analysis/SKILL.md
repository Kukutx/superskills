---
name: variance-analysis
description: Explain budget versus actual or period-over-period differences by splitting them into price, volume and mix drivers, with commentary and a bridge that ties out. Not for building the budget.
---

# Variance Analysis

## Use

Use when two sets of numbers differ and someone needs to know why: actual against budget or forecast, this month against last, this year against the same period last year. The deliverable is the decomposition and the commentary.

Getting the books themselves right belongs to `finance/books-close-and-reconciliation`. A recurring KPI report belongs to `data/metrics-review`. Checking whether an analysis of raw data holds belongs to `data/data-analysis`.

## Domain inputs and blockers

- Both sets of numbers at the same level of detail, and which one is the baseline.
- Volume and price (or headcount and rate) where they exist. Without them only a categorical breakdown is possible; say so instead of inventing a split.
- The materiality threshold. When none is given, use the defaults below and label them.

Decide the direction first: revenue above the baseline is favourable, cost above it is unfavourable.

## Which baseline answers which question

| Compare | Answers |
| --- | --- |
| actual vs budget | did we deliver the annual plan |
| actual vs latest forecast | are operations on track, is forecasting accurate |
| forecast vs budget | how expectations have moved |
| vs prior period | trend |
| vs same period last year | growth without seasonality |

## Decomposition

- **Price and volume.** Volume effect = (actual volume − baseline volume) × baseline price. Price effect = (actual price − baseline price) × actual volume. The two add up to the total variance; if they do not, the split is wrong.
- **Mix.** When segments have different margins, a shift between them moves the blended margin even if no segment changed. Separate it as a third effect.
- **People cost** splits into headcount, rate, mix of levels, timing of hires, and attrition net of backfill.
- **Operating expenses without a volume** fall into six kinds, each with a different outlook: headcount-driven, volume-driven, discretionary, contractual or fixed, one-off, and timing.

## What to investigate

Default thresholds, to be replaced by the user's own: 10% against budget, 15% against the prior period, 5% against forecast, 20% month over month, with a money floor around 0.5% to 1% of revenue. Large lines deserve a lower percentage, volatile lines a higher one. Revenue, people cost and cash are explained whatever their size.

Work in this order: largest absolute amount, largest percentage, unexpected direction, newly appearing deviations, deviations that grow each period.

A consistently favourable variance suggests a soft budget; a consistently unfavourable one suggests an aggressive budget or an execution problem; one that widens each period needs action before year end.

## Commentary

Each note is two to four sentences that state the amount and direction, the cause, whether it will continue, and what follows. The cause says why, not what: "cloud spend rose 1.2M because GPU capacity was reserved for the May launch", not "cloud spend rose 18%".

Reject these on sight:

- a circular explanation ("revenue is above budget because sales were higher");
- "timing" without what moved and when it reverses;
- "one-off" without naming the item;
- "various small items" for a material amount;
- only the largest driver, with the offsetting ones left out.

When the data cannot show the cause, write that the driver is unclear and who should be asked. A plausible invented cause is worse than a gap.

## Bridge

Start value, then each driver with its sign, then the end value, and it must foot. Keep five to eight drivers and group the rest as "other". Order from largest positive to largest negative or in business sequence. A companion table lists each driver's amount, its share of the total variance and the running total; a share above 100% is normal when drivers offset.

## Output

For each material line: `line — favourable/unfavourable variance of amount (percent) against baseline for period`, then the driver, the outlook (one-off, continuing, improving, deteriorating) and the action (none, monitor, investigate, update the forecast). Add the bridge when the total needs explaining, and three to five sentences on the largest movements at the top.

## Constraints

- Percentages use the absolute value of the baseline as the denominator; margins and ratios are compared in percentage points or basis points.
- Do not present a driver as fact when it is an assumption; mark it.
- Partial periods are not compared with full ones.
- This explains numbers; it is not financial advice, and anything reported outside the business is reviewed by a qualified person.
