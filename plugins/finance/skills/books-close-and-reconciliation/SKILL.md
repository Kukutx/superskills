---
name: books-close-and-reconciliation
description: Prepare journal entries and accruals, reconcile bank, ledger and payment records, and run a month-end close with a plain P&L summary. Use for bookkeeping and close, not tax or forecasts.
---

# Books Close and Reconciliation

## Use

Use for the work of getting a period's books right: drafting an accrual, depreciation, prepaid or revenue entry; reconciling two records that should agree; finding duplicates and missing receipts; ordering a month-end close; summarizing the month's P&L.

Explaining why actuals differ from budget belongs to `finance/variance-analysis`. Forecasting cash belongs to `finance/cash-flow-forecast`. Paying or coding supplier bills belongs to `finance/bills-and-payables`.

Everything produced here is a draft for the person who keeps or signs off the books. Entries are proposed, never posted, and the accounting framework is the user's: the conventions below follow US GAAP practice, so say so and ask when the user reports under another standard or on a cash basis.

## Domain inputs and blockers

- **Both sides at the same date.** A reconciliation needs the two balances and their detail lines as of the same day. Processor exports must include the fee column.
- **The period, and whether it is still open.** A period that has been filed or locked is not reconciled again; differences found later are reported for the accountant.
- **Where each number comes from.** State which sources were used and which were not available, because a missing source makes the result too high or too low. A source that returns nothing is a gap in the data, not a clean zero.
- Summary rows of an export are not trusted over its detail lines; sum the lines.

## Journal entries

| Entry | Debit | Credit |
| --- | --- | --- |
| expense accrual | expense (or asset when capitalizable) | accrued liability |
| depreciation | depreciation expense | accumulated depreciation |
| prepaid amortization | expense | prepaid asset |
| payroll accrual | wages, benefits, employer taxes | accrued payroll liabilities |
| revenue earned from deferred | deferred revenue | revenue |
| cash received in advance | cash or receivable | deferred revenue |

- A period-end accrual is the part of the cost that belongs to the period minus what is already booked: base × days in period ÷ days the base covers, less prior accruals and invoices already posted. A line that comes to zero gets no entry.
- Accruals reverse at the start of the next period; a missing reversal is the usual cause of a cost counted twice.
- Estimates use the same method each period and record their basis (order value, contract term, run rate). Suspiciously round estimates and accruals that never clear are reviewed.
- A customer deposit is not revenue until the goods or service are delivered.
- Every entry carries: a description, the calculation, the source document, the period, who prepared it, and whether it reverses. Debits equal credits or the entry stops; a difference is never parked in a suspense account.
- Before proposing an entry, check it against the common errors: wrong or closed period, flipped sign, duplicate of an existing entry, similar-looking wrong account, cut-off, capitalized versus expensed.

Reconciliation is in [references/reconciliation.md](references/reconciliation.md).

## Month-end close

Order follows dependency: first cash, payroll, accruals, depreciation and prepaid entries; then bank and subledger reconciliations and revenue recognition; then the full balance-sheet reconciliation and a trial balance; then tax and review; then lock the period. Nothing closes over an unexplained difference. A soft close is reviewable numbers; a hard close locks the period.

Close faster by reconciling during the month, automating recurring entries and setting cut-off dates, not by skipping reconciliations.

## Output

- **Entry**: a table of account, debit, credit and memo with totals, the supporting calculation, and the reversal date if any.
- **Reconciliation**: the statement in the fixed shape, the list of open items with age, category and likely cause, and the match rate.
- **Close summary**: what needs attention, settlement differences, duplicates, missing receipts, then a P&L note of 150 to 250 words that leads with the result and its currency, explains revenue and margin, names expense lines that moved more than about 10%, and lists up to three things to watch. Items the user postponed stay on the action list.

## Constraints

- Do not alter, void or reclassify the user's ledger data; show the finding and the proposed correction side by side.
- Payroll is checked in totals only; no individual's pay, tax identifier or bank details appear in the output.
- Approval limits, materiality and escalation thresholds are the user's; any figure used as a default is labelled as one.
- This is preparation, not accounting or tax advice; a qualified person reviews before posting, reporting or filing.
