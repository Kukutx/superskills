---
name: pricing-and-paywall
description: Set prices, tiers, free versus paid limits, paywall and upgrade moments, discounts and price increases for an app, SaaS or store. Use for monetization decisions, not unit economics or cancel flows.
---

# Pricing and Paywall

## Use

Use when the decision is what to charge and where the product asks for money: a first price, plan tiers, what stays free, when the paywall or upgrade prompt appears, a discount or guarantee, an offer that does not convert, a price increase, or a review of a pricing page.

The arithmetic of customer lifetime value, acquisition cost and payback belongs to `finance/unit-economics`. Cancel flows, save offers and failed payments belong to `product/onboarding-and-retention`. The wording on a store listing belongs to `writing/app-store-copy`. Designing a price test and reading its result belongs to `marketing/ab-testing`.

## Domain inputs and blockers

- **What is sold and to whom**: a consumer app, a tool for teams, a service, physical goods. The rules below lean on software subscriptions; say so when applying them elsewhere.
- **Who bills the customer.** When an app store bills the subscription, price points, trial and offer mechanics, what a paywall must disclose and what review accepts are set by the store. None of that is stated here: take it from the store's current documentation before finalising a price or a paywall.
- **The alternatives a buyer would use instead** and what they cost, including doing nothing.
- **Current numbers, if any**: price, conversion from free to paid, revenue per user, churn. Without them the output is a first price to learn from and the test that would improve it, labelled as such.
- **For a paywall**: the action after which users understand the product's value, and the points where they hit a real limit.

## Setting the price

1. **Three separate decisions**: packaging (what each plan contains), the value metric (what the customer is charged by) and the price point. A problem in one is not fixed by moving another.
2. **The price sits between the next-best alternative and the value the buyer perceives.** Cost is only the floor; a competitor's price is one data point, not the target.
3. **A first price is a price to learn from.** With no data, start from an order of magnitude and adjust quickly. As starting magnitudes per month for software: around 10 for an individual, around 100 for a small team, around 1,000 for something a mid-sized business depends on.
4. **The very low price is a trap.** It produces traction that is not real, the cheapest customers churn and complain the most, and raising a price several-fold later is very hard.
5. **Test of a value metric**: does the customer get more value as they use more of it? A good metric is also easy to understand, grows with the customer and is hard to game.
6. **Good, better, best.** The middle plan is the one to recommend and the anchor; the top plan at roughly two to three times the middle is a working default. The annual discount is set from the user's own cash needs and renewal data; published ranges differ widely and none is a rule.
7. **Price framing**: an ending in .99 signals value, a round number signals quality; a price restated per day makes a monthly figure smaller. Use each only where the signal is the one wanted.
8. **Research**, when there are customers to ask: four questions per respondent (at what price is it too expensive to consider, so cheap you doubt it, getting expensive but still considered, a bargain); how to read the four curves, and how to find which features belong in which tier, is in [references/offers-and-research.md](references/offers-and-research.md), together with the charging models, guarantees, bonuses and the detailed pricing page review.

**Raising a price.** Signals that the price is too low, as working signals and not thresholds: competitors raised theirs, prospects accept without hesitation, an unusually high share of trials convert (above roughly 40%, as a rough mark), churn is very low (under 3% a month), customers say it is cheap. Order: test the new price on new customers first; move existing customers in batches of 5 to 10%; announce months ahead and give existing customers a concession. Whether long-standing customers keep the old price for good or for a set period is the user's choice, made from their costs and contracts and then kept.

## Paywall and upgrade moments

**Value first, then the ask.** A paywall belongs after the user has understood the value and at a real limit. It does not appear during onboarding, in the middle of a task, or again and again after being dismissed.

| Trigger | What it must contain |
| --- | --- |
| Locked feature | Why it is paid, a preview of it, and a way to carry on free |
| Usage limit | A warning before the limit; never a sudden block |
| Trial ending | Reminders at 7, 3 and 1 days, a summary of the value already received, and what happens at expiry |
| Time-based prompt | A light reminder that is easy to close |

A paywall screen has: a headline about what the user gains, the value shown, a plan comparison with the current plan marked, clear monthly and annual prices, proof from real users, a specific call to action and a visible "not now".

Frequency: a cap per session, and a cool-off after a dismissal; start with days rather than hours and treat the length as something to test. Watch for signs of annoyance alongside the conversion figures: how often it is shown, clicks to upgrade, completed purchases, revenue per user, and churn after upgrading.

Not acceptable: a hidden close button, a confusing plan choice, wording that shames the user for declining, asking before any value was delivered, blocking a critical flow.

## Offers, discounts and guarantees

For a course, a service, consulting or a one-off product, "the copy is weak" often means the offer is weak. For a self-serve subscription, look at tiers and the value metric first.

- **Value rises with** the outcome the buyer wants and how likely they believe it is, **and falls with** the time until they get it and the effort it costs them. Many requests to lower the price are better answered by raising one of the first two or lowering one of the last two.
- **A complete offer has six parts**: the core deliverable, bonuses, a guarantee, a real limit on time or quantity, a name, and the price with its payment structure. Weak offers usually lack bonuses, a guarantee or a limit.
- **Diagnosis**: write the current offer down; score the four value levers from 1 to 10; the lowest is the constraint; change one lever per round and measure before changing another. Promise no uplift figure; a claim that one change multiplies conversion is not credible.
- Before touching the price, establish whether price is what stops the purchase: when the real obstacle is the effort of switching or of getting started, a discount does not remove it.
- **Discounts.** For subscriptions and services, do not discount to win new customers, on the reasoning that customers won by a discount leave sooner; discount for upgrades, cross-sells and real seasonal windows. For a shop, a first-order discount is common practice, and whether it pays is decided by the shop's own margin and repeat-purchase data, which the user supplies.
- **Percentage or amount.** Which one reads larger depends on the price. Work out both for the actual price, always show the real amount saved, and treat which one leads as something to test.
- **Scarcity and deadlines are used only when they are real.** A countdown that resets or "three places left" that is not true is a lie.
- **A guarantee** states its conditions and promises only what the business can pay.
- Bonus values are not inflated, and a serious product is not dressed in get-rich packaging.
- Pre-selecting the recommended plan is acceptable only when it honestly is the plan most buyers should have.

## Pricing page

Check two things: can a person tell within seconds which plan is theirs and what it costs, and can a machine read it. Paste the page's rendered text into an assistant and ask which plans and prices exist; a price that lives in an image or behind "contact us" is invisible to that reader. The recommended plan is visually obvious, and the page answers "which one fits me".

## Output

- **Price recommendation**: packaging, value metric and price points with the reasoning for each, the alternatives used as reference, what is assumed, and the first test to run.
- **Paywall design**: for each trigger, when it fires, the screen's components with draft text, frequency and cool-off, and what to measure.
- **Offer review**: the six parts as they stand, the four lever scores, the one change to make first and how to tell whether it worked.
- **Price increase plan**: the signals found, the new price, the rollout order with dates, and the notice to existing customers.

## Constraints

- Do not state an app store's price tiers, trial or disclosure rules; name the store's documentation as the place to confirm them.
- Do not quote a conversion or uplift benchmark as fact; figures here are defaults that the user's data replaces.
- Do not design false urgency, hidden renewal terms or a paywall without a visible way to decline; beyond the ethics, consumer-protection rules on pricing claims and automatic renewal differ by country and are confirmed for the user's market.
- Tax treatment of prices (inclusive or exclusive, by country) is outside this Skill; flag it for the user's accountant.
