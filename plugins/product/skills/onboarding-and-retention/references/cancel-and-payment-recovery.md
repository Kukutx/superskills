# Cancel Flows and Payment Recovery

Read when designing the detail of a cancel flow, a pause, a grace period or failed-payment recovery for a subscription the user bills themselves. A subscription billed by an app store follows the store's own flow and none of this applies to it as written.

## Route by the customer's state, not only the stated reason

| Customer | What it means | What helps |
| --- | --- | --- |
| new, under a month | never activated | onboarding help, a setup call, a longer trial; ask what they were trying to achieve |
| active but price-sensitive | value seen, price in question | a discount, annual billing, a lower plan |
| dormant for a month or more | already gone | a pause; ask what changed; the aim is to learn the reason |
| heavy user leaving for a competitor | a product gap | an honest comparison, a feedback call |

Someone who answers "too expensive" is asked a follow-up, since that answer often covers "I did not see the value" or "I did not use it enough". Check the billing period and whether this customer was already saved once.

## Offers

- **Discount ladder**: at most two discounts in one cancel session, the smaller first, capped at about 30% and limited to two or three months before the normal price returns. A customer who accepted a discount and cancels again at full price is not offered the same one.
- **Downgrade** is the strongest save for a product with several plans: show what is kept and what is lost, keep the data, and show no upgrade prompt for at least a month afterwards. When a free plan exists, offer it before the cancellation completes; keeping the user matters more than keeping the payment.
- **Pause**: one, two or three months with one as the default; data kept, access removed, automatic resumption announced a week ahead and the day before; once per year.
- **Annual plans**: first pause the remaining term, then adjust the plan with a credit at renewal, then a personal contact, then a partial refund with a downgrade. Be generous with refunds; a bad refund experience becomes a public review.
- **Team accounts**: only an owner can cancel; show the effect on the team ("your eight members lose access").

## After cancellation

The confirmation says when access ends, how long data is kept and how to come back, with a reactivation button. If the save flow breaks, the cancellation still completes and a receipt is emailed. Afterwards: confirmation at once, nothing the next day, a short survey after a week, what is new after a month, a message at two months only when the stated reason has been fixed, and one last offer at three months.

## Failed payments

- **By decline type**: insufficient funds is retried after two to three days; a network or processing error within a day; an unspecific refusal once more and then a new card is requested; a lost card or closed account is never retried; a decline that needs authentication sends the customer to complete it. Retry timing worth testing: the day of the month of the last successful charge, shortly after common paydays, weekday mornings.
- **Grace period** of one to two weeks after the last retry, during which retries and reminders continue and a banner shows in the product. Business accounts keep full access and individuals read-only; locking at once is for very cheap plans only. At the end the account is suspended, not deleted. A successful payment stops every reminder and restores access immediately.
- **Reminder emails** state the amount, the card type and last four digits, the reason when known, and a link that opens the update page directly. The first is calm and says access is unaffected for now; the one a week later names the suspension date and what will be lost; the last gives the data retention period and adds that no action is needed if cancelling was the intention.
- **In the product**: a banner on every page during recovery, dismissible but back in the next session, one click from the update page, never blocking use; a modal with "remind me later" for the final warning.
- **Prevention**: a banner a few days before a card expires; an offer to add a backup payment method right after a recovered failure, when its value is obvious; an email about a week before an annual or expensive renewal stating amount and date; and a check that the payment provider's automatic card-update service is on.
- **Measure**: recovery rate = recovered payments ÷ failed payments, by decline type; days to recover; money recovered against money lost to involuntary churn each month.

## Activation detail

- **Choosing the model**: a free plan needs real value in the free tier and a limit users run into naturally; it should hook, not satisfy. A trial needs a length that fits how long the value takes to show, and the choice to require a card trades volume for intent, so state the trade-off. A paid trial filters the undecided. A money-back guarantee needs the value to arrive inside the refund window. Guided setup suits expensive, complex products and does not scale. Price, buyer sophistication, complexity, time to value and what competitors do decide which model can hold.
- **The shortest path to value**, in three passes: list every screen, field, click, confirmation, permission and empty state between signup and the first value; ask of each whether it is unavoidable to reach that value now, and cut, defer, prefill or make skippable what is not (configuration, profile completion and nice-to-know education usually are not); reorder so value comes first, then measure completion per step and time to value. The first reordering is a hypothesis.
- **Measure**: activation rate, time to activate, completion per step, where users drop, return rate, retention at days 1, 7 and 30, and support requests during onboarding.

## Referral detail

- Products that are collaborative, used for communication or produce something others see spread naturally: build the sharing into the product. Back-end tools and anything users would rather not reveal do not, and a reward-based referral, content or partners serve better.
- Ceiling for a reward = customer lifetime value × gross margin − target acquisition cost.
- Against abuse: verify the email, pay when the referred person activates, claw back on a refund or chargeback, cap referrals per period, prefer product credit to cash.
- Reduce friction: a link already generated, one tap to share, a message already written, the entry point at the moment of success rather than in settings.
- Each inviter's invitations × the rate at which they convert gives the viral coefficient; above 1 the product grows by itself, below 1 referrals amplify other acquisition.
