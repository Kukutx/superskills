---
name: financial-modeling
description: Build or audit a spreadsheet financial model such as a three-statement projection, revenue build or budget, and find why a balance sheet will not balance. Not for valuation judgement.
---

# Financial Modeling

## Use

Use when the deliverable is the model itself or a review of one: a projection with linked income statement, balance sheet and cash flow; a revenue and cost build for a startup or product; a model that does not balance, has circular references or gives an implausible answer.

What the output means for value belongs to `finance/company-valuation`. Explaining actuals against plan belongs to `finance/variance-analysis`. Analysing a dataset that is not a model belongs to `data/data-analysis`.

## Domain inputs and blockers

- For a build: historical statements for three to five years or, for a new business, the drivers the user actually knows (prices, volumes, headcount, costs). Currency and unit (thousands or millions) are fixed first.
- For an audit: the file, since hidden rows, overwritten formulas and broken links are invisible in pasted values. With only pasted cells, check the logic and say what could not be inspected. Calculations done by macros cannot be audited from formulas.
- The scope of an audit: a selection, a sheet, or the whole model.

Without spreadsheet output available, deliver the structure as tables with the formulas written out.

## Building

1. **Revenue is the part that matters most.** Build it from drivers (units × price, customers × revenue per customer) and split it the way the business is managed: by product, by region, by channel. Every split adds up to the same total.
2. **Costs from drivers, then checked as a share of revenue.** People cost is headcount × cost per head; cost of sales links to the margin assumption; depreciation links to the capital expenditure schedule. Operating leverage means the share of revenue falls as the business scales; a flat or rising share needs a reason.
3. **Inputs live in one place.** A forecast cell contains a formula; the only typed numbers are historical actuals and labelled assumptions. Blue for inputs, black for formulas and green for links from other sheets is the common convention.
4. **Working capital in days.** Receivable days = receivables ÷ revenue × 365; inventory days and payable days use cost of sales. An increase in an asset is a cash outflow, an increase in payables an inflow.
5. **Sign conventions stated once.** Depreciation and share-based pay are added back in operating cash flow; capital expenditure, debt repayment and dividends are negative; borrowing is positive.
6. **Interest circularity.** Interest depends on debt, debt on cash, cash on interest. Break the loop by charging interest on the opening balance, or enable iteration deliberately with a switch that turns it off.
7. **Scenarios.** Bear, base and bull selected by one switch, each changing several assumptions, each with its rationale.

## Integrity checks

These hold in every period or the model is wrong:

- assets = liabilities + equity;
- change in cash = operating + investing + financing cash flow, and closing cash equals the balance sheet's cash;
- net income on the income statement is the starting line of the cash flow;
- opening retained earnings + net income − dividends = closing retained earnings, with any other movement shown explicitly;
- fixed assets roll forward with capital expenditure and depreciation; debt rolls forward with borrowing and repayment.

After a scenario switch the checks still pass, and the ordering makes sense: profit and cash are higher in the upside than in the base, leverage is lower.

Tax losses: a new business starts with none; they arise only in loss years; how much can offset later profit is set by the tax rules of the jurisdiction, so take the limit from the user or a tax adviser.

Auditing a model is in [references/auditing.md](references/auditing.md).

## Output

- **Build**: the model or its table layout, the assumptions list with sources, and the result of each integrity check.
- **Audit**: one line of overall status (clean, minor issues, major issues, with counts), then a findings table of sheet, cell or range, severity, category, issue and suggested fix. Critical means the output is wrong; warning means a hard-coded value, an inconsistency or a failure at an edge; info is style.

## Constraints

- Report findings first; change someone's model only when asked, and never before the plan of changes is accepted.
- Do not force a model to balance with a plug; an unexplained difference is shown as one.
- Credit and margin thresholds differ by industry; any used as a flag is labelled a generic default.
- A model is a set of assumptions, not a forecast to rely on; this is not financial advice.
