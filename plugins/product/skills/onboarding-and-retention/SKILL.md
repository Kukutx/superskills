---
name: onboarding-and-retention
description: Design onboarding and activation, cancel flows with save offers, failed-payment recovery and churn warning signs for an app or subscription. Use for activation and churn, not pricing or signup forms.
---

# Onboarding and Retention

## Use

Use for the two ends of a customer's life in the product: getting a new user to the first real value (first-run flow, checklist, empty states, the moment to ask for a referral), and keeping a subscriber who is about to leave (cancel flow, save offers, pause, failed payments, warning signals).

The signup form and the landing page before it belong to `marketing/conversion-review`. The copy of the emails in a lifecycle sequence belongs to `marketing/email-sequences`. Tiers, price points and the paywall belong to `product/pricing-and-paywall`. Winning back shop customers who stopped ordering belongs to `support/review-replies-and-winback`.

## Domain inputs and blockers

- **Who bills the subscription. Ask this before any cancel-flow or payment-recovery work.** If the app store bills it, the store owns the cancellation screen, the payment retries and the billing messages; the cancel flow and retry schedule below do not apply as written. What the app is allowed to do around cancellation and billing problems is taken from that store's current documentation, and the output says which parts were left to the store.
- **Activation**: the action that best predicts a user staying, what happens right after signup, and where users drop out. Without behavioural data the output is a proposed flow and hypotheses to test; it cannot say what the activation moment is.
- **Churn**: monthly churn, number of subscribers and revenue per subscriber, whether pause and downgrade exist, any cancellation reasons already collected, consumer or business customers. Missing figures do not block a draft flow.
- **What the user can actually offer** to a leaving customer: a discount, a pause, a downgrade, help.

## Activation

1. **Choose the activation model first** (free plan, free trial, paid trial, money-back guarantee, guided setup with a person), because it decides the whole first-run flow. How to choose, and how to cut the path to first value step by step, are in [references/cancel-and-payment-recovery.md](references/cancel-and-payment-recovery.md).
2. **Judge activation by conversion to paying customer and retention at 90 days, not by signups.** The activation moment is the action most strongly associated with staying; find it by comparing what retained users did with what churned users did.
3. **Every step must be needed to reach the core value**; anything else moves later. Let the user do the thing instead of watching a tour, and give each session one goal.
4. **Checklist**: three to seven items, ordered by value, starting with a quick win, showing progress, dismissible. Starting with one item already ticked is a tactic worth testing.
5. **Empty states** say what the area is for, show what it looks like with data, offer the main action, and can be pre-filled with an example.
6. **Tours** are three to five steps, closable at any point, and not shown again to returning users.
7. **Mobile apps**: permissions, then a quick win, then notification settings, then the habit loop.
8. **Email supports the product instead of repeating it**: a reminder at 24 and 72 hours when setup is unfinished, a note when the user activates, feature discovery around days 3, 7 and 14.

**Asking for a referral** belongs at a moment of earned goodwill: right after the first real result, after a milestone, after a good support experience, after a renewal or upgrade. Sharing built into the product works better than a personal link, which works better than an email invite, a social post or a code. The reward is given when the referred person reaches value, not when they sign up; a reward for both sides converts better than for one. Do not force referral mechanics onto a product people have no natural reason to share.

## Cancel flow and save offers

Churn is voluntary (the customer cancels) or involuntary (the payment fails). Measure the split in the user's own data; involuntary churn is usually the cheaper one to fix.

The flow has five steps: the cancel entry, one reason question, an offer matched to the reason, a clear confirmation that says when access ends, and a path afterwards that makes coming back easy.

- **Reason question**: one single-choice question with five to eight options, the common ones first, plus optional free text; framed as "help us improve". Review the options every quarter.
- **Match the offer to the reason.** The same offer for every reason is the standard mistake. The figures are starting points:

| Reason | First offer | Fallback |
| --- | --- | --- |
| Too expensive | 20 to 30% off for two to three months | A cheaper plan |
| Not using it enough | A pause of one to three months | Free guided setup |
| Missing a feature | What is coming and when, if it is true | A workaround |
| Moving to a competitor | An honest comparison plus a discount | None |
| Technical problem | Hand over to support immediately | None |
| Needed it only for a while | A pause | None |
| Business closing | No offer | None |

- **Keep a save discount to about 30% at most**, for two or three months; larger ones teach customers to cancel in order to get the offer. Show the amount saved in money, not only the percentage.
- **A pause lasts one to three months at most**; longer pauses rarely end in a return.
- **One main offer and one fallback**, never a stack; the fallback may be a lower plan or a second, slightly larger discount, and nothing follows it. The "continue to cancel" option stays visible at every step, with no wording that shames the customer.
- **Route by the customer's state as well as the reason**: a new customer never activated, a dormant one is already gone, a heavy user leaving for a competitor points at a product gap. Each needs a different response, set out with pauses, downgrades, grace periods and the messages after cancellation in [references/cancel-and-payment-recovery.md](references/cancel-and-payment-recovery.md).
- **A save is counted only if the customer is still there 30 days later.** Track what the retained customers are worth afterwards.

## Failed payments

Applies when the user's own billing system charges the card. Where the billing provider runs retries itself, read its settings first and do not add a second schedule on top.

- **Retry by decline type.** A soft decline (insufficient funds, timeout) is retried, as a default at 24 hours, then days 3, 5 and 7, about four attempts. A hard decline (lost card, closed account) is not retried: ask for a new card. A decline that needs customer authentication sends the customer to complete it or update the payment method.
- **Emails on days 0, 3, 7 and 10** as a default: plain text, no blame, with a link that opens the payment update page directly.
- **Before it fails**: remind customers 30, 15 and 7 days before a card expires, offer a backup payment method, and announce an annual renewal about a week ahead, with the amount and the date; some places require notice of an automatic renewal, so check the rule for the market.

## Warning signals

Signs that come before a cancellation: logins falling by half or more, a key feature no longer used, more visits to the billing page, and a data export, which is the urgent one because cancellation follows within days.

A health score can weight these; one illustrative weighting is login frequency 30%, feature use 25%, support sentiment 15%, billing health 15%, engagement 15%, with bands at 80, 60 and 40. Treat both the weights and the bands as an example to calibrate against which customers really left.

Measure: churn split by voluntary and involuntary, the share of cancel attempts saved, offer acceptance by reason, and the share of failed payments recovered. Benchmarks for these circulate without sources; compare the user's figures with their own earlier periods.

## Output

- **Onboarding review or design**: the activation goal, the flow step by step, checklist items, empty-state text, email triggers, and what to measure; an audit lists finding, effect, recommendation and priority.
- **Cancel flow**: each screen in order with its text, the reason options, the offer per reason, and the confirmation wording.
- **Payment recovery**: the retry schedule by decline type, the email schedule with the purpose of each message, and the pre-expiry reminders.
- For store-billed subscriptions, state at the top which parts were not designed because the store controls them.

## Constraints

- Do not make cancelling hard to find or hard to finish. Laws on how easy cancellation must be differ by country and change; the current rule is confirmed for each market the user sells in (for the United States, the FTC's page on its Negative Option Rule) before any legal claim is made, and this Skill states none.
- Do not promise a roadmap item to keep a customer unless the user confirmed it.
- Do not apply the retry and email schedules to subscriptions billed by an app store.
- Do not present the offer sizes, retry timings or health-score weights as industry standards.
