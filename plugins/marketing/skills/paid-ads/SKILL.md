---
name: paid-ads
description: Plan and review paid ad campaigns on Google, Meta or TikTok, judge spend, cost per result and ROAS, and reconcile conflicting attribution numbers. Not for writing ad copy or organic content.
---

# Paid Ads

## Use

Use for "are my ads working", "should I pause this campaign", "can I raise the budget", planning a first campaign, retargeting, and "the ad platform says 50 sales, analytics says 30, which is right".

The ad text itself belongs to `writing/marketing-copy`. A recurring report across all business metrics belongs to `data/metrics-review`. The page the ads lead to belongs to `marketing/conversion-review`, and the wider channel plan to `marketing/marketing-plan`.

## Domain inputs and blockers

- **For a review**: an export of the last 30 days by campaign (90 days for a trend question), with spend, results, cost per result and frequency. For the real return, the leads and sales recorded in the user's own system for the same period.
- **For a plan**: the goal (installs, sales or leads), the target cost per result or return, the budget, the landing page, whether conversion tracking exists, and past results. A ceiling for cost per acquisition needs the customer's lifetime value or margin from the user.
- There is no access to the ad account. Work from pasted exports; every change is carried out by the user in the ad manager, so proposals are written as current state, change, expected effect and how to undo it.
- **No conversion tracking means no verdict.** Say plainly that nobody can tell what these ads produced, compare cost per click only, and put "install tracking" ahead of any budget change.
- Reading an export: "Results" can mean a different event in each campaign. Check the result-type column; if it is absent, say the rows are not comparable and do not add them. Currency strings are converted to numbers first. A missing conversion column is named, together with the export setting that adds it.

## Is there enough data, and what state is it in

Minimum data before a verdict (working defaults; the account's own volume may justify others). Below these the answer is "not enough data yet", plus what is needed:

| Decision | Minimum |
| --- | --- |
| pause a campaign | 30 days or 50 results, whichever comes first |
| name a winning creative | 1,000 impressions and 15 results per variant |
| call a cost trend | three consecutive weeks in the same direction |
| judge a new campaign | at least 7 days |
| move budget between two campaigns | both have run 30 days |

Status is judged against the account's own trailing 90-day average, not an industry benchmark:

| Status | Rule |
| --- | --- |
| Working | cost per result within 15% of the average or better, volume steady |
| Watch | 15–40% worse, or frequency past the warning line for its audience (about 2.5 for a cold audience, about 4 for retargeting), or volume down two weeks running |
| Problem | more than 40% worse, or spend with no results for 14 days or more |
| No verdict | no conversion tracking, or below the minimum data |

Lead with cost per result, or cost per closed sale when the user's records allow it. Impressions never come first.

A stop rule can also be written in spend instead of days: a new ad that has spent two to three times the target cost per result with nothing to show is stopped. In an audit, a check that could not be verified is reported as unknown and lowers coverage, never the health score. How to grade an audit, what zero conversions can and cannot prove, how to read a search-terms report and how to label statements for a client are in [references/reading-ad-data.md](references/reading-ad-data.md).

| Signal | Reading |
| --- | --- |
| spend up and cost per result up | the audience is exhausted (the signal most often misread) |
| frequency up and click rate down | creative fatigue: new creative, not more budget |
| click rate high, conversion low | the landing page or the offer; leave the ads alone |
| cost per result jumps suddenly | check sample size, delayed conversions and the learning phase before deciding anything |
| cost per thousand impressions high | the audience may be too narrow |
| one campaign delivers over 70% of results | the account is fragile; say so before touching that campaign |
| results flat, cost creeping up | usually auction pressure |
| "everything looks fine but the phone is quiet" | believe the phone: check whether the form works, where leads are delivered, and whether tracking counts twice |

Two weeks of movement is not a trend.

## Budget, targeting and structure

- **Raise** only when cost is stable or improving, frequency is below the warning line and there are 30 days of history. Step by about 20% and wait three to five days between steps on social platforms; on search, move a bid target by 10–15% and wait one to two weeks. If cost per result rises to one and a half times the target after a raise, cut back by 20–30% and let it settle before trying again. Larger jumps are reported to send a campaign back into its learning phase; treat that as a hypothesis and check the platform's current guidance.
- **Lower** when cost per result is 40% or more worse than the account's average, or frequency is in the severe band for its audience with a falling click rate. Below the minimum data, the right move most weeks is none.
- Pausing the only working campaign is never proposed without saying that it is the only one, and that a restart will perform worse for some days. A producing ad is not paused until its replacement is ready.
- Keep most of the budget, 70% to 80% as a default, on what is proven and the rest on tests with their own protected budget.
- **Scale against payback, not a lifetime-value ratio.** Payback in months = acquisition cost ÷ monthly revenue per customer, worked out per plan, since a blended average hides that a cheap plan may never pay for its ads. Divide by the annual retention rate to allow for customers who leave. As a working gate, paid acquisition is for plans that pay back within about a year; cheaper plans are acquired organically. Recompute monthly, because acquisition cost rises with volume, and watch net cash, not the return of a single campaign.
- **Return uses the revenue the ads can reach.** Dividing whole-company revenue by ad spend inflates the figure many times over; state both numbers used. A return an order of magnitude better than plausible means the denominator is wrong.
- **Targeting.** Narrow the geography to where the business can actually serve; exclude existing customers; when frequency passes 4, widening the audience beats swapping the creative. Stacking narrow interest filters does not rescue weak creative; several creatives aimed at different segments with broad targeting usually does better.
- **Retargeting windows** (working defaults): cart or trial visitors 1–7 days, visitors to key pages 7–30 days, any visitor 30–90 days, each with a frequency cap. Exclude recent buyers for 7–14 days, visits under ten seconds and irrelevant pages. Show a different offer, not the same ad again: an answer to an objection, testimonials, another product, or something useful first.
- **Search.** Brand and non-brand keywords are separate campaigns. Brand search is demand that already existed, so a low brand cost is not a win; report the blended return, but set targets on the non-brand one. A search-terms report is a partial, biased sample: state how many of the clicks had their terms disclosed, compute the break-even conversion rate before calling spend wasted, and never invent negative keywords without the report.
- **Links** carry UTM parameters in lowercase with one separator style and specific names, recorded in a single sheet. The landing page repeats the best-performing ad headline as its main heading.

For a business that sells through leads and sales calls, for the structure of a search campaign, for fatigue thresholds by campaign type and for incrementality tests, read [references/b2b-search-and-measurement.md](references/b2b-search-and-measurement.md).

Single-author claims about platform behaviour are hypotheses to test in the account, not rules: that static images beat produced video, that the algorithm rewards a large volume of fresh creative, that a given share of effort belongs to creative over targeting, that automated bidding should wait for about 50 conversions.

## Reconciling attribution

1. **Name one source of truth for the number of conversions**, normally the system where the money or the signed-up account actually lands.
2. **Platform numbers are never added together.** A sale claimed by two platforms is one sale, and conversions counted under different attribution windows are not summed.
3. **Report both figures and name the gap.** Platforms count more because of view-through conversions, cross-device matching, their attribution window and several touches claiming one sale. Internal records count less because the source field is blank, calls and walk-ins carry no digital trace, and some forms never become records.
4. **Decide on the internal cost per sale**; the platform's figure is the optimistic ceiling. Do not produce one blended ROI, because it gets forwarded to partners and lenders as fact.
5. Look for agreement in direction, not in value. "The platform claims twice what analytics shows" is not turned into "halve the platform"; check the windows and view-through settings first, and settle a real dispute with a holdout test.
6. **Blind spots.** Direct traffic is a catch-all; brand search is often demand created elsewhere; private messages, group chats and podcasts cannot be tracked at all, and visits prompted by AI assistants often arrive as direct or brand. A large direct-and-brand share often means something upstream is working unseen.
7. **Ask customers.** "How did you hear about us?" at the moment of conversion, with listed options and "other, please specify". It favours the most memorable touch, so it cross-checks and is not turned into exact shares.
8. **Models.** Last touch suits direct response and first touch suits prospecting; for a long sales cycle show both side by side, since the difference is the insight. With a small budget, clean UTMs, last non-direct click and the customer question beat a complex model. Media-mix modelling needs two to three years of weekly data. Take the data volume that data-driven attribution needs from the platform's current help page.

## Output

- **Account read**: one line for the account and one per campaign (spend, results, cost per result, frequency, status), then a one-sentence summary.
- **Attribution readout**: the question, the source of truth, what each source says (deduplicated, not summed), the gap explained, confidence and blind spots, the recommendation and the test that would settle it.
- **Change proposals**, one at a time: what changes (by name), why (the number), the effect in money per month, what is given up (pausing saves the spend and also loses its leads), what to watch after a week, and whether it can be undone. A percentage never stands alone.
- **Campaign plan**: goal and break-even, structure, budget split, retargeting tiers, tracking and UTM plan, and the date and data at which each part will be judged.
- **Before any new ad goes live**: the landing link works and matches the promise; every claim (price, guarantee, response time, credentials) is true; nothing was invented on the owner's behalf.

## Constraints

- Do not judge a campaign below the minimum data, and do not present "no verdict" as bad performance.
- Do not state a platform's policy, attribution setting or learning-phase rule as current fact; point to the platform's own page.
- Prices, guarantees and credentials in an ad are the advertiser's legal responsibility, and platforms restrict claims about health, personal attributes and before-and-after images; flag these for the user to check.
- A figure produced here is for managing the ads, not a financial statement.
