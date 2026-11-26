# Reconciliation

1. Align both sides on the finest shared key and normalize dates, amounts (two decimals) and identifiers so equality is exact. Default tolerance is 0.01 on amounts.
2. Classify every difference:
   - **timing** (outstanding cheque, deposit in transit, trade date versus settlement date) needs no entry and should clear within days;
   - **needs an adjustment** (unrecorded bank fee or interest, a posting error, a misclassification);
   - **needs investigation** (unexplained, disputed, old, or recurring).
3. A bank reconciliation has a fixed shape: bank balance + deposits in transit − outstanding cheques ± bank errors = adjusted bank balance; book balance + unrecorded interest − unrecorded charges ± book errors = adjusted book balance; the two must be equal.
4. Age open items. As a default: watch under 30 days, investigate from 31, escalate from 61, and decide on write-off or adjustment past 90.
5. A likely cause attached to a break is a hypothesis for whoever resolves it. To trace one, compare the two records attribute by attribute (posting date, rate used, account mapping, sign of quantity and amount); the attribute that differs is usually the cause, written as one sentence: which side did what, and why.
6. Sort breaks by absolute amount. A roll-forward (opening + additions − reversals − payments ± adjustments = closing) must foot; what does not is listed as unexplained.

**Payment processors.** Compare net with net: the ledger holds the payout after fees, the processor report shows gross, so gross against net is off on every line. Match on the deposit date, not the sale date. Refunds are negative lines that match a credit or refund entry. For a store, reconcile payouts to the bank and orders to revenue as two separate exercises.

**Duplicates.** Flag when amount, counterparty and a five-day window all match; split lines of one transaction are not duplicates, and a regular weekly bill is the usual false alarm. Say what window was scanned, since a second payment three weeks later falls outside it.

**Receipts.** List expenses above the user's threshold that have no supporting document.
