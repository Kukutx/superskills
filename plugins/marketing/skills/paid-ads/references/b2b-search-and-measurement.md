# B2B, Search and Measurement

Read for a business that sells through leads and a sales process, for a search campaign's structure, or for a question about incrementality or which attribution model to use. The thresholds are practitioner starting points: recalibrate them on the account's own first 30 days.

## Break-even and kill rules

- Break-even cost per lead = average deal value × lead-to-close rate. Break-even cost per click = target cost per lead × landing-page conversion rate. The working target sits below both to leave a margin.
- Two spend-based stop rules, which are repeatable rather than statistically rigorous: a new ad that has spent two to three times the target cost per lead with no lead is stopped; an ad older than one to two weeks whose cost per lead runs at one and a half to two times the target is stopped.
- A producing ad is never paused before its replacement is ready. When the pipeline of new creative is empty, move the budget to proven ads.

## Optimize for quality, not form fills

- Send sales stages back to the ad platform (qualified, opportunity, closed), so automated bidding learns from revenue rather than from cheap form submissions. For a lead-based business this is usually the single most valuable change.
- Until that exists, read the job titles and companies of new leads every week, not only the cost per lead. Reconcile platform conversions with the CRM monthly; the CRM wins.
- Lead-quality score: urgency, budget and fit, each 0 to 3, given by whoever takes the sales call and recorded against the ad it came from. After about twenty scored calls, rank ads by average score, not by cost per lead.
- Low-friction lead forms that autofill produce leads who do not remember submitting. Ask for a work email, add one to three choice questions from easy to hard, and say what happens next. A landing page suits demos and trials; a form suits content and webinars.

**Before scaling**, rate measurement on five points from 1 to 3: a view of the whole pipeline, a view per channel, conversion tracking (3 only when offline conversions are sent back), site analytics, and an agreed written attribution process. A low total means visibility comes before budget, starting with the weakest point.

## Fatigue by campaign type

Frequency lines differ by audience, so one number for the whole account misreads retargeting:

| Campaign | Safe | Warning | Severe |
| --- | --- | --- | --- |
| cold audience | up to about 2.5 | 2.5–4 | above 4 |
| retargeting | 2–4 | 4–6 | above 6 |
| small named-account audience | 2–5 | 5–8 | above 8 |

A rising cost per thousand impressions over two weeks usually moves before the click rate does. A click rate well below its peak, or frequency in the severe band, retires the concept instead of tweaking the execution. Editing the creative of a running ad restarts its learning; launch the new version beside it. Pausing does not restart learning.

When spend will not grow although cost per result is stable, look at unique reach month over month. Flat reach on the same spend means the same people are being shown the ads again: that is a reach problem, and conversion work will not fix it.

## Search campaigns

- **Intent ladder**, opened one rung at a time and only after the rung below has produced pipeline: brand, high-intent non-brand, competitor terms, problem-aware terms, demand generation.
- Brand, non-brand, competitor and retargeting each have their own budget; a shared budget is swallowed by brand, the cheapest and best converting. Whether brand needs paying for at all is settled by pausing it and watching total brand conversions, paid and organic together.
- Ad groups by theme: five to fifteen keywords of one intent with two or three responsive ads. Campaigns too small to gather conversions are merged.
- Start with phrase and exact match and mine the search terms weekly. Broad match waits for steady conversion volume, automated bidding and a strict negative list.
- Bidding follows monthly conversion volume: manual or untargeted while it is low, a target cost only once volume is stable, a target return only with real revenue sent back. Change a target by small steps and wait one to two weeks.
- Impression share lost to budget and impression share lost to rank are different problems: money, or the quality of the ad and page.
- **Negatives.** A broad-match negative needs every word present, so negating "free trial" does not block "free" alone; a phrase negative blocks the words in order; an exact negative blocks only that query. Weekly, three passes: waste (several clicks, no conversion), winners (converting terms not yet keywords), drift (close in wording, wrong in meaning). Negate only what is plainly wrong; ambiguous terms gather data first. A starter list of generic negatives is for building a new campaign and is labelled as a starter, not as evidence.

## Named-account campaigns

Worth it with a list of roughly a thousand accounts or more, large deals, sales cycles of two months or longer, and sales and marketing agreeing on the list. With a small list, no first-party data, a small budget or a short cycle, ordinary profile targeting does better. Measure movement of accounts (share of the list reached, cost per engaged account, accounts becoming opportunities), not cost per lead, and hold out about a fifth of the list for three weeks or more to see the lift.

## Incrementality

- Lift = conversion rate of the exposed group − rate of the control group. With 4.2% exposed and 3.6% control the lift is 0.6 points; the rest would have converted anyway, which is why last-click return is almost always overstated.
- Read the interval: "a 5% lift, between −2% and +12%" has taught nothing yet.
- Check for contamination: a control group that was reached, or spill-over between regions, can make a working channel look flat.
- Incremental cost per acquisition = spend ÷ incremental conversions. It is usually worse than the platform's figure and is the number that should move budget.
- Designs: regional hold-out, a random hold-out for retargeting or email, and a plain on-off test, which is especially useful for brand search.
- A high platform return with flat revenue is the signature of low incrementality, most often in retargeting.

## Attribution by business type

| Business | Source of truth | Default |
| --- | --- | --- |
| B2B with a long cycle | the CRM | first touch and a position-based view side by side; the "how did you hear about us" answer weighs most; attribute to pipeline stage, at account level |
| store or direct-to-consumer | the order count in the store's own back end | platform conversions are deduplicated against it, never added; a question on the order confirmation page catches podcasts, organic video and word of mouth; platform return is for optimizing inside the platform only |
| self-serve plus sales | both, reported separately | do not blend a small self-serve signup and a large enterprise deal into one figure |

Model choice: a short cycle with few touches uses last non-direct click plus the customer question; a long cycle uses a position-based split with first and last touch shown alongside; high volume online can use a data-driven model, validated by lift tests; offline and brand-heavy businesses rely on lift tests and aggregate modelling instead of any user-level model. A time-decay model with a short half-life behaves almost like last click. Choose one model, keep it, and pair it with a check from outside the model; switching models to flatter a channel is the fastest way to lose trust. When several lines of evidence agree that a channel is undercounted, write a bounded adjustment in the reporting layer, limited to the period the evidence covers, with the raw table kept.
