---
name: bills-and-payables
description: Process supplier bills and invoices, catching duplicates, coding them to accounts, matching against orders and proposing which to pay this week against cash. Not for chasing money owed to you.
---

# Bills and Payables

## Use

Use when the user has bills to deal with: a stack of supplier invoices to read and code, "who do we owe", "what should I pay this week", "have we been billed twice", or a supplier statement to check.

Money owed to the user belongs to `finance/invoice-collections`. The cash forecast belongs to `finance/cash-flow-forecast`. Month-end reconciliation belongs to `finance/books-close-and-reconciliation`.

Nothing is paid from here. Coding a bill into the books and approving a payment are two separate decisions, each the user's.

## Domain inputs and blockers

Bills as PDFs, photos or forwarded emails; the chart of accounts or past coding; purchase orders and delivery notes if the business uses them; the current cash balance, the cash floor the user wants to keep, and upcoming payroll. Without cash data, the payment proposal is headed "not checked against cash" and makes no claim that the money is there.

## Reading a bill

- Extract supplier, invoice number, invoice date, due date or terms, subtotal, tax, shipping, total, order reference, line items, and payment details when they differ from what is on file. An empty field is a valid result; an invented one is not.
- Lines + tax + shipping must equal the total. When they do not, report both numbers; a cropped photo is the usual cause.
- An amount that cannot be read is reported as unreadable, with what was legible. "1,84" is not completed to 1,847.00.
- A notification from a billing portal is a link, not a bill. A card or expense transaction is already paid: it is coded, never queued for payment.
- Supplier names are matched loosely to existing records before a new one is proposed; a duplicate supplier record splits the history.

## Duplicates, before coding

Flag as a possible duplicate: the same supplier and invoice number; the same supplier and total within five days when one copy has no number; the same supplier and total already recorded or paid in the last 90 days. Show the pair with both sources and let the user decide, since some suppliers do bill the same amount every month.

A supplier statement is used to find gaps, not to create entries: on the statement but not in the books means a bill never arrived; in the books but not on the statement is usually already paid; a different amount is usually a credit or part-payment.

## Coding

Use the strongest single piece of evidence and stop: this supplier's history in these books, then the job or order reference, then the line items, then a rule the user has stated, then ask. Stacking weak signals produces confident nonsense.

- Code automatically only when at least three past bills agree and nothing on this one contradicts them. The rest go on a short "needs your decision" list, each with a suggested account and one sentence of reasoning.
- One invoice covering several jobs is split by the references on its lines or by the split the user gives. It is never split evenly by default; when the split is unknown, code it to the most likely job and mark it unsplit.
- Traps: equipment above the capitalization threshold is an asset (ask the threshold once); a deposit or prepayment is a prepaid, not an expense; freight on job materials belongs to the job; a credit note is a negative bill for the same supplier, never netted silently into an unrelated invoice.
- A recurring bill can be coded from its history, but an amount more than about 10% different from last time is flagged, and recurrence is never consent to pay.

## Matching to orders and deliveries

Many small businesses have no purchase orders; a missing one is not an exception unless the user requires it. Where they exist, default tolerances are: unit price off by more than 2% or 25 in the business's currency, whichever is larger; any quantity billed above what was received; unordered freight or surcharges above 50; total off by more than 1% of the order. The asymmetry is deliberate: a small price drift is often the market, an over-billed quantity is always an error.

Name each exception with supplier, invoice number, both figures and the difference, and say who has to resolve it: the user (accept a price rise, pay short), the supplier (shortage, missing invoice), or the bookkeeper (a correction to a closed period).

## Payment proposal

Order: overdue; early-payment discounts worth taking, stated in money (2% for paying 20 days early on 10,000 is 200); due within the run window; everything else waits. Exclude and list with the reason: bills with an open exception, unreadable totals, bills already paid by card, disputed bills.

Read the aged payables by bucket before ranking. A negative amount in any bucket is a credit, and a supplier's net total hides it: show gross owed, credits and net, and do not treat a supplier whose net is zero or negative as owed.

State the result in one sentence with the numbers: total going out, the date, the balance afterwards, and how that compares with the next payroll. If the run would take cash below the floor, offer a reduced run and say who is held back.

## Constraints

- **Changed payment details are a fraud signal.** Bank details on a bill that differ from those on file, or any message asking to change them, are flagged for the user to confirm by phone on a number they already have. Supplier records are never updated from a bill or an email.
- No payment is initiated, scheduled or described as made. The list can only be reduced by the user, not extended on the assistant's initiative.
- A part-payment records what was paid, what was withheld and why, and the disputed balance stays visible.
- Corrections to a closed period go to the bookkeeper. This is not accounting or tax advice.
