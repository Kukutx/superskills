---
name: unit-economics
description: Work out LTV, CAC, payback, churn, net and gross retention, cohorts and an ARR bridge for a subscription app, SaaS or recurring-revenue business. Use to judge revenue quality, not to set prices.
---

# Unit Economics

## Use

Use when the question is whether a recurring-revenue business makes money per customer and how durable its revenue is: the user's own app or store, or a business being evaluated.

Choosing prices and tiers belongs to `product/pricing-and-paywall`. Reducing churn belongs to `product/onboarding-and-retention`. Valuing the whole company belongs to `finance/company-valuation`.

## Domain inputs and blockers

- **The revenue model**, because it decides which metrics mean anything: subscription (ARR, retention, cohorts), recurring services (contract value, renewal rate), usage or transactional (revenue per transaction, volume trend, take rate), or a mix analysed stream by stream. A usage business is read from consumption trends, not from ARR.
- **Customer-level revenue by month** when it exists. Aggregates hide problems; when only aggregates are available, compute what they allow and say what cannot be seen.
- **Sales and marketing spend and gross margin** for the same periods.
- For a store-billed app, whether revenue figures are before or after the store's commission.

## Formulas

- CAC = sales and marketing spend ÷ new customers acquired in the same period.
- LTV = (average revenue per customer × gross margin) ÷ churn rate. Revenue per customer and churn must be on the same period: monthly revenue with annual churn is wrong by a factor of twelve.
- CAC payback in months = CAC ÷ monthly gross profit per customer. Some reports leave the margin out; say which version was used.
- Gross retention excludes expansion; net retention includes it. Logo churn counts customers; revenue churn counts money. Report each pair together, because net retention above 100% can sit on top of heavy gross churn, and losing many small customers looks different from losing one large one.
- ARR bridge: opening → new → expansion → contraction → churn → closing.
- Rule of 40 = growth rate + profit margin. Magic number = net new ARR ÷ the previous period's sales and marketing spend.

## Reading the numbers

Working benchmarks from investor practice for software subscriptions; they are not laws and differ by segment and price point, so use the user's own history first:

| Metric | Strong | Acceptable | Concerning |
| --- | --- | --- | --- |
| net revenue retention | above 120% | above 110% | below 100% |
| gross revenue retention | above 95% | above 90% | below 85% |
| LTV to CAC | above 5 | above 3 | below 2 |
| CAC payback | under 12 months | under 18 | over 24 |

Rule of 40 above 40 and a magic number above 0.75 are read as healthy on the same footing.

The cohort table is the most informative view of revenue quality: one row per start period, one column per period since start, shown both in money and indexed to 100% at the start. A steep early drop points at activation, a curve that keeps falling points at engagement, and a curve that flattens shows a stable retained base.

## Revenue quality

- Contracted ARR is not recognized revenue. Recurring, non-recurring and services revenue are separated; services are lower margin and not recurring.
- Concentration: the share held by the top 10, 20 and 50 customers.
- Contract structure: spread of contract values, share on multi-year terms, share that renews automatically.
- Margin waterfall: revenue → gross profit → contribution after acquisition cost → operating profit, with gross margin split by revenue stream.
- For a summary score, rate six factors from 1 to 5 — recurring share, net retention, concentration, cohort stability, growth durability, margin structure — and show the factor scores, not only the total.

## Output

The metric table with each definition, period and source; the ARR bridge and cohort table when the data allows; the three or four findings that matter; and what could not be computed and which data would allow it.

## Constraints

- Every ratio states its numerator, denominator and period.
- A benchmark is quoted as a benchmark, with the caveat that it comes from larger software companies.
- Do not fill a missing input with an industry average and present the result as the user's number.
- This informs a decision; it is not investment advice.
