---
name: marketing-attribution
description: Judge which marketing drove revenue with attribution models, MMM, incrementality tests and self-reported attribution. Use when channels disagree on credit, not for paid-ads reconciliation.
---

# Marketing Attribution

## Use

Use when the question is which marketing actually caused a conversion or revenue: which channel deserves the credit, whether a channel is really working, which numbers to trust when platforms disagree, how to credit podcasts and dark social, or whether to cut or grow a budget line.

Reconciling one paid-ads account's spend against its own reported results belongs to `marketing/paid-ads`. Designing an experiment on a page or product belongs to `marketing/ab-testing`. Checking whether a metric is computed correctly belongs to `data/metrics-review`. Tracking setup (events, UTMs, pixels) is a precondition, not this Skill.

## First rule

Attribution is directional, not truth. It is a model of causality built from incomplete data: cookies expire, sessions fragment, offline touches vanish, people research on one device and buy on another. Deliver a defensible, consistent read with confidence levels, never a single objective number.

## Attribution models

Every model is an opinion about whose story to believe. Say so when you pick one.

| Model | Credit rule | Best for | How it lies |
| --- | --- | --- | --- |
| First-touch | 100% to the first known touch | Top-of-funnel and demand-gen valuation, short cycles | Ignores everything that closed the deal |
| Last-touch | 100% to the last touch before conversion | Direct response, quick e-commerce | Over-credits bottom-funnel, branded search and direct |
| Last non-direct | Last touch, skipping direct | A cheap fix for direct pollution | Still single-touch, only moves the blind spot |
| Linear | Equal credit to every touch | Long multi-touch journeys | Treats a throwaway visit like a demo |
| Time-decay | More credit nearer conversion | Longer cycles where recency matters | Under-credits the top of funnel |
| Position-based | 40% first, 40% last, 20% middle | B2B with clear created and closed moments | The 40/40/20 split is arbitrary |
| Data-driven | Credit from modelled marginal contribution | High-volume accounts with enough conversions | A black box that needs volume and cannot see touches it was never fed |

Rules of thumb:

- Never report a single model in isolation for a long sales cycle. Show first-touch and last-touch side by side; the gap between them is the insight.
- Data-driven attribution needs volume. Below roughly 200 conversions and 2,000 ad interactions in 30 days it often collapses toward last-click priors, noise dressed as science. When thin, prefer last-click, or compute position-based or first-plus-last side by side on first-party or CRM data.
- Google Ads and GA4 no longer offer first-click, linear, time-decay or position-based as selectable reporting models. Teach the full table as concepts you can compute on your own event path, CRM or warehouse, not as dropdown options.
- The model matters far less than being consistent and pairing it with an out-of-model sanity check.

## The three measurement paradigms

Models split credit inside tracked data. Paradigms get at causality, and they get more rigorous and more expensive in this order:

| Paradigm | What it is | Answers | Needs | Watch out |
| --- | --- | --- | --- | --- |
| MTA (multi-touch attribution) | Stitch user-level touches, apply a model | Which touchpoints appear on converting journeys | Clean cross-device user-level tracking | Cookie loss and privacy gut user-level data; click paths over-weight search and direct |
| MMM (media mix modelling) | Top-down regression of spend against outcomes over time | Each channel's aggregate contribution, including offline and brand | Two to three years of weekly data with real spend variation | Correlational, slow to react, needs budget swings to learn |
| Incrementality (geo holdout, PSA, ghost ads, on/off) | Controlled experiment, exposed against withheld | Did this channel cause lift that would not have happened anyway | Ability to withhold, enough volume for significance | The gold standard, but only a few things can be tested at a time |

How to choose: small budget or short cycle, good UTMs plus last-non-direct plus a self-reported survey beats a fancy model. Mid budget with several channels, MTA day to day plus periodic incrementality tests on the biggest line items. Large budget with offline and brand spend, MMM for the portfolio plus incrementality to validate MMM's coefficients. Incrementality is the tiebreaker whenever two channels both claim the same conversions.

## Self-reported attribution

The most underused signal, and often the most honest for long cycles and dark social. A post-conversion "How did you hear about us?" catches what tracking structurally cannot: podcasts, word of mouth, Slack communities, a founder's post, a friend's recommendation.

- Ask at the moment of conversion (signup, first purchase, demo request), when recall is highest.
- Open-ended wording captures dark social; a short pick-list is easier to quantify but pre-biases the answer. Best practice is a pick-list of known channels plus a free-text "other, tell us more".
- Treat it as a triangulation input, not gospel. Recall is fuzzy and people credit the memorable touch, not the first. Discount survey share before turning it into credit: 22% recall of a channel is evidence of awareness, not a claim it deserves 22% of conversions. Pair it with incrementality or platform deltas before writing an allocation rule.
- If a large share of journeys shows up as direct, there is a self-reported-shaped hole.

## Reconciling conflicting sources

"Google says 50, Meta says 40, GA says 60, the CRM says 35 — who is right?" Nobody is.

Why each source systematically lies:

| Source | Biased toward | Because |
| --- | --- | --- |
| Ad platforms | Over-counts itself | Claims view-through and click conversions in its own window; every platform counts the same sale |
| Web analytics | Last non-direct click | Loses cross-device and cookie-blocked users, dumps the unknown into direct |
| CRM | Whatever the rep typed or the form captured | Human entry, lead-source overwrites, offline deals with no digital trail |
| Self-reported survey | The memorable touch | Recall bias; under-counts boring-but-real touches like retargeting |

Triangulate:

1. Pick one source of truth for the conversion count, usually the CRM or backend, the system where money is real. Everything else explains where those conversions came from; it does not get to redefine how many there were.
2. Never sum across platforms. If Google and Meta both claim a conversion, that is one conversion with two claimants, not two conversions. De-duplicate against the source-of-truth total.
3. Read directional agreement, not absolute match. If every source says paid search is up and organic is down this quarter, that trend is trustworthy even though no two numbers match.
4. Use self-reported attribution as the tiebreaker when platforms fight over the same conversions, and incrementality when the stakes justify a test. Do not turn a platform-versus-analytics gap into a multiplier rule.
5. Expect and budget for the gap. Report "platforms claim N; we can verify M; the delta is over-claiming plus view-through plus untracked, here is our best allocation."

## The blind spots

- **Direct** is the junk drawer: bookmarks and typed URLs, but also stripped referrers, app-to-web, dark social and dropped tracking. Investigate its composition before treating it as a tracking defect.
- **Branded search** is people who discovered the product elsewhere and searched its name. Last-touch hands the credit to branded search; the real driver was whatever made them search. Segment branded against non-branded or the top of funnel gets defunded.
- **Dark social** is sharing that carries no referrer: direct messages, Slack and Discord, podcasts, newsletters, screenshots. Structurally invisible to tracking; self-reported attribution is the only way to see it.
- **AI traffic** increasingly influences buyers, then sends them via branded search or direct, so the AI touch is invisible in analytics. Name it as a blind spot; deeper AI-search visibility work belongs to `marketing/seo-audit`.

When direct and branded search dominate, the most common explanation is a top of funnel that works while attribution hides it. Rule out existing customers, lost referrers and offline discovery first, then check self-reported attribution or run an incrementality test.

## Business-type fork

- **B2B SaaS, long cycle, sales-assisted.** Journeys span weeks to months and several people, so single-touch models mislead badly. Anchor on the CRM as source of truth, use first-touch and position-based side by side, lean hard on self-reported attribution at demo or signup, and treat pipeline and revenue attribution as the real scoreboard.
- **E-commerce and DTC, short cycle, self-serve.** Fast journeys, high volume, spend concentrated in paid social and search. Anchor on platform ROAS but distrust it, validate with MMM once spend is material and geo-holdouts on the biggest channels, and use a post-purchase survey to catch what pixels miss. Last-touch is defensible for quick-turn SKUs; MMM plus incrementality is how the real budget gets allocated.

## First-party attribution, in brief

When the user controls the site or app and wants to own attribution instead of renting platform numbers, the whole idea is one join: anonymous browsing joined to the eventual conversion.

1. Analytics assigns an anonymous id at first visit and stamps first-touch properties on events.
2. At conversion (signup, booking, purchase), `identify()` with a stable id (email or user UUID) merges the anonymous history into a known person, so first-touch survives to the conversion.
3. Every conversion event can now be broken down by first-touch channel, and joined to revenue.

Two failure modes to check first: nothing ever calls `identify()`, so conversions never join to browsing history; and redirects overwrite the true first touch, so exclude OAuth and checkout referrers, own subdomains and dev hosts from referrer classification. A conversion that completes on a domain the user does not control (a booking tool, a hosted checkout) needs the anonymous id passed through that tool's metadata passthrough and returned in its webhook, then merged on receipt. Only ever pass the anonymous id, never an email or UUID, into a third-party URL.

## Output

An attribution readout, not a data dump:

1. **The question** — what decision this informs.
2. **Source of truth** — which system defines the conversion count, and why.
3. **What each source says** — platform-reported, analytics, CRM and self-reported side by side, de-duplicated against the source of truth, never summed.
4. **Model comparison** for long cycles — first-touch against last-touch, the gap stated as the insight.
5. **Confidence and gaps** — the attribution gap, the blind spots, what cannot be seen.
6. **Recommendation** — the allocation call with confidence levels, and the tiebreaker test worth running.

## Constraints

- Do not present a single model's output as the truth.
- Do not sum conversion counts across platforms.
- Do not turn a platform-versus-analytics gap into a multiplier.
- Do not claim a channel is failing when the evidence is consistent with an attribution blind spot; say which reading the evidence supports.
- Do not set up tracking, pixels or UTMs here; that work belongs to the analytics and conversion-tracking owners.

## Source

Adapted and rewritten from `coreyhaines31/marketingskills` skills/attribution, https://github.com/coreyhaines31/marketingskills (MIT).
