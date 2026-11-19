---
name: rates-fx-vol-analysis
description: Read pasted market data on bond spreads, yield and swap curves, real rates, currency carry and option implied versus realized volatility. Use for rates, FX or volatility questions, not stock research.
---

# Rates, FX and Volatility Analysis

## Use

Use when the user pastes market data and wants it read: whether a bond looks rich or cheap, what the shape of a curve says, where an economy stands in its rate cycle, whether carrying a currency pays for its risk, or whether options are expensive against how the market has actually moved.

A portfolio of bonds reported for a period belongs to `finance/portfolio-reporting`. One company's shares belong to `finance/stock-research`. The discount rate inside a valuation belongs to `finance/company-valuation`.

## Domain inputs and blockers

Every rate, yield, spread, forward point and volatility comes from what the user pastes, with its date; none is recalled. These are professional markets with their own conventions for quoting and day counts; when the pasted data does not say which convention applies, ask instead of assuming.

No level here has a fixed threshold. "Rich", "cheap", "tight" or "elevated" is always a comparison with the instrument's own history or with its peers, so ask for the history, and without it give the calculation and say that the judgement cannot be made.

## Bonds

- Split the yield into its parts. The spread over the government curve is the bond's yield less the government yield interpolated to the same maturity. Take off the spread of the matching credit curve; what remains is the residual, which is the real rich-or-cheap signal: positive leans cheap, negative leans rich.
- A credit curve describes a class of issuer, so the residual also contains whatever is particular to this issuer. Say so instead of calling it all liquidity.
- State the conclusion with how many basis points the spread would have to move for it to flip.
- A bond with an embedded option, such as a callable one, needs option-adjusted spread and effective duration; a plain spread misleads.
- Scenario table: parallel moves of −100, −50, 0, +50 and +100 basis points, with the price change per 100 of face value, computed from the duration and convexity supplied and labelled as an approximation.

## Curves and the macro picture

- Swap spread is the swap rate less the government yield at the same maturity. Real rate is the nominal rate less breakeven inflation.
- Slope measures: two-year to ten-year, three-month to ten-year, five-year to thirty-year, and a butterfly across three points; ask which butterfly definition the user's desk uses. Classify the shape as normal, flat, inverted or humped.
- Order of reading an economy: where it is in the cycle (growth, jobs, surveys), what the central bank is doing, what the bond market signals (slope, real rates), then financial conditions (swap spreads). Wide first, then deep. Prefer seasonally adjusted series, and say whether an inflation figure is headline or core.
- Open with two or three sentences: cycle position, policy outlook, financial conditions, main risk.
- Any curve position described has both legs sized so their sensitivity to a one-basis-point move offsets, with the carry and roll-down over three months, the move that breaks even, and the levels at which the view is wrong.

## Currency carry

- Carry-to-volatility is annualized carry divided by at-the-money implied volatility: the attraction per unit of risk.
- Look at carry along the whole forward curve, overnight to one year, to find the tenor that pays best.
- A carry position is short volatility by nature. Rising implied volatility is the first warning.
- The 25-delta risk reversal shows which direction the market pays to protect against; the 25-delta butterfly shows how much it pays for extreme moves. The bid-offer spread indicates liquidity.
- Place today's level in the one-year range and say which way it has been moving.

## Options

- Start from the surface: at-the-money volatility by expiry, risk reversal and butterfly. A single option's price follows from it.
- The volatility premium is implied less realized. Compute realized volatility from daily closing prices over 20, 60 and 90 trading days and set them against one-, three- and six-month implied volatility; state the annualization used. A positive premium leans expensive.
- Describe the regime (low, normal, elevated, crisis) only against the instrument's own history.
- For a specific option give premium, delta, gamma, vega and theta when supplied.

## Output

The conclusion first with its evidence; then the tables (spread decomposition, curve with spreads and real rates, carry by tenor, implied against realized); the scenario table; what would change the conclusion; and the data that was missing.

## Constraints

- No market level from memory, and no threshold presented as a standard.
- A formula not given by the user's data or stated above is asked for, not improvised.
- Observations are not instructions to trade; position size and suitability are the user's and their adviser's.
- This is analysis support, not investment advice.
