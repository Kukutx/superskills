---
name: company-valuation
description: Value a company or stock with a DCF, WACC, terminal value, comparable multiples, scenarios and sensitivity tables, and sanity-check the result. Use for what a business is worth, not trade timing.
---

# Company Valuation

## Use

Use when the question is what a company, a stock or a stake is worth, or whether someone else's valuation holds up: a discounted cash flow, comparable multiples, precedent deals, or a check of an existing number.

Researching the company and its results belongs to `finance/stock-research`. Building or debugging the spreadsheet belongs to `finance/financial-modeling`. Returns on a specific acquisition belong to `finance/deal-diligence`.

A valuation is the consequence of its assumptions. The output is a range with the assumptions that drive it, never a buy or sell call, and it says so.

## Domain inputs and blockers

- Three to five years of financial statements, the current share price, **diluted** share count, debt and cash.
- Growth and margin assumptions, or a consensus the user supplies with its date.
- For the discount rate: the current yield on a long-dated government bond in the company's currency, a beta, and an equity risk premium. These are market data with a date; take them from the user or a source checked in the session, and state the source. They are never recalled.
- For multiples: the peers' market value, net debt and the same profit measures over the same period.

A missing input is listed as assumed, with the value used, so the reader can replace it.

Comparable multiples do not work for a company with no listed peers, a conglomerate, a distressed business or one with no revenue yet; say so and use another method.

## Discounted cash flow

1. **Free cash flow to the firm**: operating profit → less tax on it → plus depreciation and amortization → less capital expenditure → less the increase in working capital. No interest in it; interest belongs to the discount rate. Net income is not a substitute.
2. **Forecast period**: five years by default, shorter for a stable business, longer for a fast-growing one. Growth fades towards the terminal rate over the period, and growth needs matching investment in capital expenditure and working capital, otherwise it is counted twice. A cyclical business is valued on mid-cycle margins.
3. **Discount rate**: cost of equity = risk-free rate + beta × equity risk premium; cost of debt after tax; weights at market value, not book value. As a rough orientation, large stable companies fall around 7% to 9%, growing ones 9% to 12%, high-risk ones 12% to 15%; a result outside those bands is rechecked before it is used.
4. **Terminal value**: final-year cash flow × (1 + g) ÷ (discount rate − g). The growth rate g must be below the discount rate and no higher than the long-run growth of the economy; 2% to 3% is the usual range for a developed-market currency. An exit multiple taken from current peer multiples is the alternative and suits cyclical industries.
5. **Discounting**: choose end-of-year or mid-year timing and apply it to every cash flow and to the terminal value. Mixing conventions, or leaving the terminal value undiscounted, is a classic error.
6. **From enterprise value to a share**: enterprise value − net debt − minority interests − preferred equity + non-operating assets = equity value, divided by diluted shares.

## Checks that catch a wrong DCF

- The terminal value's share of enterprise value. Around 50% to 70% is ordinary; above roughly 75% the result rests almost entirely on the terminal assumptions, and the forecast period may be too short.
- The multiple the DCF implies, against peers. A DCF implying 25 times profit when peers trade at 12 needs a reason.
- What growth the current price already implies.
- If the value looks too high: terminal share, g too close to the discount rate, margins or growth too optimistic. If too low: the sign of net debt, a discount rate that is too high, a terminal growth that is too low.

## Comparable companies

- Four to ten companies that really share the business model, size, sector and geography, each with a reason for inclusion. Three good peers beat six doubtful ones.
- Numerator and denominator cover the same period for every company; note different year ends and the exchange rate and date used.
- Summarize ratios with maximum, upper quartile, median, lower quartile and minimum, and reason from the median. Size measures are not averaged.
- Choose the multiple by the business: revenue multiples for unprofitable or fast-growing companies, enterprise value to EBITDA for mature ones, price to earnings where capital structure is stable, price to book for banks. EBITDA and gross margin mean little for a bank. A company with negative EBITDA is not valued on an EBITDA multiple.
- Deal multiples include a control premium and are not directly comparable with trading multiples.
- Explain where the target should sit against the median and why: growth, margins, scale, position.

## Scenarios and sensitivity

- Bear, base and bull change several drivers together (growth, margin, discount rate, terminal growth, investment), not growth alone. Each has a stated trigger and, when weighted, a probability.
- A sensitivity table is symmetric around the base case with an odd number of steps, and its centre cell equals the model's own result; that equality proves the table is wired correctly. Discount rate against terminal growth is the standard pair; revenue growth against margin is the second.
- When several methods are combined, state the weights and why. More weight on the DCF when the forecast is well founded, on comparables for a mature company.

## Output

The assumptions table with sources and dates; the calculation in steps; the range (low, base, high) per share and in total; the sensitivity table; the checks above with their results; and the three assumptions the value depends on most.

## Constraints

- Every input carries its source and date; an estimate is marked as an estimate.
- Do not present a single point as the answer, and do not attach a rating or a recommendation to trade.
- Do not carry worked numbers from an example into a real valuation.
- This is an analytical tool, not investment advice.
