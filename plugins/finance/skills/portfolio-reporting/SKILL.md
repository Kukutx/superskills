---
name: portfolio-reporting
description: Write a periodic portfolio or investment report with returns after fees against an agreed benchmark, attribution, allocation drift and commentary. Use for family or client reports, not stock research.
---

# Portfolio Reporting

## Use

Use when the performance of a portfolio or fund has to be reported for a period: a quarterly or annual report, the pack for a review meeting, a summary for a family or for outside investors, or a proposal that sets out an allocation and its costs.

Research on one company belongs to `finance/stock-research`. A KPI report on a business belongs to `data/metrics-review`. A proposal for services belongs to `sales/quote-and-proposal`.

This arranges and explains numbers the user supplies. It gives no advice on what to buy or sell, and a report sent to clients by a regulated adviser needs that firm's compliance review.

## Domain inputs and blockers

- Holdings and values at the start and end of the period, cash in and out with dates, income, fees and transactions.
- **The returns, or the method.** Returns can be calculated in more than one way and the choice changes the figure when money moved in or out. Use the returns the user's platform reports and state the method it names; if they must be computed, ask which method is wanted and show the working. Never present a return without saying how it was calculated.
- **The benchmark agreed in advance**, from the investment policy or the original plan, and the target allocation with its tolerance.
- Who will read it, since that decides the vocabulary.

Prices, index levels and benchmark returns are market data: they come from the user's statements or a source checked in the session, with dates.

## Rules that keep a report honest

1. **Returns are after fees** unless the reader has asked for the figure before fees; say which is shown.
2. **The benchmark is the one set beforehand.** Choosing afterwards whichever index looks kindest is the commonest way a report misleads.
3. **The same periods every time**: the quarter, year to date, one year, and three years, five years and since inception as annualized figures, for the portfolio, the benchmark and the difference. A period shorter than a year is not annualized.
4. **Attribution**: which asset classes or holdings drove the result, the three largest contributors and the three largest detractors, and whether one position is doing too much of the work.
5. **Allocation**: target, current and drift. Action is flagged only when the drift passes the agreed tolerance; a few percentage points is the usual band.
6. **Poor performance is stated plainly and early.** A weak period explained up front keeps trust; one found in a table loses it.
7. **Commentary** in two parts: what happened in the markets in two or three sentences, then what it meant for this portfolio and how it is positioned. Written at the reader's level, with no jargon for a non-specialist.
8. **Activity**: purchases and sales, money in and out, income received, fees charged, rebalancing.

## A review meeting

Open with what the reader cares about most. A workable half-hour: markets in a few minutes, performance, allocation, changes in the person's life and plans (income needs, large expenses, tax and estate questions as topics to raise, not to rule on), then actions. End with dated actions and record any change to the plan or the policy.

## A proposal

Restate the person's goals in their own terms to show they were heard; set out the allocation as class, share, instrument and reason; show three outcomes (cautious, central, optimistic) rather than one projection, each labelled hypothetical; list every layer of cost; and describe the transition and the first three months, since the effort of moving is what holds people back. Stress the process, not past results.

## Output

Summary on one page; the performance table; allocation against target; holdings; commentary; activity; notes on goals and the next review date; and the disclosures: how returns were calculated, that past performance does not predict future results, and that projections are hypothetical.

## Constraints

- No return, price or benchmark figure that was not supplied or computed with the method shown.
- No change of benchmark between reports without saying so and showing both.
- No recommendation to buy, sell or switch; observations are stated as observations.
- Tax, legal and estate matters are flagged for the relevant professional.
- This is reporting support, not investment advice.
