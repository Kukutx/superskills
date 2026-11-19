---
name: cash-flow-forecast
description: Forecast cash for the next 30, 60 and 90 days from receivables, payables, payroll and fixed costs, with a low and high case and runway risks. Use for can I make payroll, not bookkeeping or tax.
---

# Cash Flow Forecast

## Use

Use when the question is whether the money will be there: a 30/60/90-day forecast, runway, whether payroll or a large bill can be met, what a late-paying customer does to the month.

Getting the books right first belongs to `finance/books-close-and-reconciliation`. Deciding which bills to pay belongs to `finance/bills-and-payables`. Chasing the late invoices belongs to `finance/invoice-collections`.

## Domain inputs and blockers

- **Opening cash balance with its date.** Without it the forecast is titled "net change only" and makes no claim about cash on hand. A balance is never assumed.
- Open receivables with due dates, open payables, payroll dates and amounts, and known fixed costs. A bank or ledger export works; confirm which column is which before computing, since a silent mis-mapping gives a confident wrong answer.
- Payment history per customer, if available: the last six to twelve paid invoices.
- For a store or app: the payout schedule of the payment processor or app store. Ask; do not infer it.

A forecast built on books that are not closed inherits their errors. If the month has unreconciled or unclassified items, say so and name them.

## Method

1. **Inflows arrive when customers actually pay, not when invoices fall due.** For each customer, expected receipt = due date + that customer's average days late. Count only invoices with a balance still due.
2. **Platform revenue arrives on the payout date**, not the order date. Modelling on the order date makes the forecast optimistic by exactly the settlement delay.
3. **Fixed costs** are more than the entries labelled recurring: a payable to the same supplier for three or more consecutive months within about 10% of the same amount is treated as fixed, and the list is shown for confirmation.
4. **Known outflows not yet in the books**, such as card spending and approved expense claims, are added, with the amount the forecast would be overstated without them.
5. **Payroll** uses the payroll system's dates and amounts when it disagrees with the ledger.
6. One ledger is the source of totals. The same item is never added across two systems.

## Uncertainty

- The spread of each customer's payment delay sets the band: the more erratic the customer, the wider it is. With fewer than three paid invoices for a customer, use a default of ±30%.
- A band that would exceed ±50% means the history is too thin to model; say that instead of presenting a range.
- The low and high cases move the uncertain inflows; committed outflows such as payroll stay where they are.

## Risks

List at most five, largest amount first, each naming the party, the amount and the dates:

- **Payroll before receipts**: payroll falls due before the receivable that was meant to cover it arrives. This is the one that matters most, and money arriving in 45 days does not solve Friday's payroll.
- A customer who habitually pays late and holds a large balance.
- A window where the low case goes negative.
- Thin data: few paid invoices, or a forecast built from a single export.

## Output

Headline with the sources used and the opening balance and its date; a table of window (0–30, 31–60, 61–90 days), expected, low and high, in the business's currency; the risks; then what was not available this time and whether its absence makes the forecast too high or too low.

## Constraints

- Do not present the expected case without the low case.
- Do not reclassify or remove a suspected duplicate transaction to tidy the forecast; show it.
- A summary total that disagrees with its detail lines is replaced by the sum of the lines, and the difference is mentioned.
- This is a planning aid, not accounting advice; a borrowing or investment decision is checked with the bookkeeper or accountant first.
