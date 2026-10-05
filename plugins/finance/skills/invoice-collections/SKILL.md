---
name: invoice-collections
description: Chase overdue invoices by ranking who owes what, checking for recent payments first, and drafting reminders matched to each customer's payment history. Not for bills you owe.
---

# Invoice Collections

## Use

Use when customers owe the user money: "who owes me", an aged receivables list to work through, payment reminders to write, or a decision on how firm to be with a late payer.

Bills the user owes belong to `finance/bills-and-payables`. Forecasting when the money lands belongs to `finance/cash-flow-forecast`. A dispute about the work itself is a customer conversation and belongs to `support/customer-support-replies`.

## Domain inputs and blockers

The list of open invoices with customer, invoice number, amount, due date and contact; recent receipts from every channel the business is paid through; and, if available, twelve months of each customer's payment history. Reminders go only to customers on the supplied receivables list, never to names recalled from the conversation.

## Before drafting anything

1. **Check whether it was already paid.** Look for a receipt from that customer in the last two weeks in every payment channel supplied. A possible match is marked "possibly paid — verify" and gets no draft. Say which channels were checked; cheques and bank transfers do not appear in a card processor's export, so state that they were not verified.
2. Match customer to payment on email address when both sides have one. A match on name alone is marked as such and held for the user.
3. Remove internal and test accounts (the user's own domain, names containing test or demo), and voided invoices.
4. An invoice that appears in two systems is one invoice: match on invoice number, then on amount and due date. When unsure, one reminder, not two.
5. Several overdue invoices for one customer become one message.

## Tone from payment history

Score a customer only with at least three invoices in the past twelve months:

| History | Tone |
| --- | --- |
| paid on time at least 75% of the time | gentle: it has probably been overlooked |
| late 25% to 50% of the time, or fewer than three invoices | neutral: the facts and the request |
| late more than half the time | firm: a specific date, no warmth and no accusation |

The tone follows the customer's record, not the age of the oldest invoice.

Every reminder contains the invoice number, the total owed, the original due date, the number of days overdue, and how to pay, and asks for one thing. Firm is not threatening: no capitals, no consequences the user has not decided on.

## Prioritizing

Sort by amount, then by age, and name invoices more than 30 days overdue individually rather than as a count. Whether to change a habitual late payer's terms is the user's call; raise it, do not write it into a reminder.

## Output

A summary table (customer, amount due, days late, tone, channel), the draft for each, and the list of those held back with the reason: possibly paid, name-only match, disputed, or missing contact. After the user approves, the approval covers that batch only; a customer added later is a new approval.

## Constraints

- Nothing is sent from here, and nothing is described as sent.
- Do not add late fees, interest, a deadline or a threat of collection or legal action unless the user states them; what may be charged and how debts may be pursued depends on the contract and the law where the customer is.
- The ledger is not modified.
- A reminder never includes another customer's details or the user's internal notes.
