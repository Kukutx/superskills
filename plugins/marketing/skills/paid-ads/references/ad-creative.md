# Ad Creative

Rules for writing and judging ad creative, adapted and rewritten from `coreyhaines31/marketingskills` ad-creative (MIT), compressed from 474 lines.

`marketing/paid-ads` plans and reviews campaigns; this file is the creative production side, used only when headlines, descriptions or visuals are being written or iterated.

## Before starting

Gather: the platform and format, the product and offer, the audience and their intent, performance data when iterating, and the constraints (character limits, brand voice, claims that need evidence). The ad text for an existing page belongs to `writing/marketing-copy`; this file covers ads.

## Four modes

1. **Generate from scratch** — a full set of creative from product context, audience insight and platform practice.
2. **Iterate from performance data** — analyse what works, identify patterns in top performers, and generate variations that build on winning themes while testing new angles. Loop: pull data, identify winning patterns, generate variations, validate specs, deliver.
3. **Scaled static batches** — recurring production at volume from a grounded inputs corpus (below). Every concept traces to real source material.
4. **Creative strategy loop** — decide which ads are worth making before making them, from account performance, customer language and external organic signals, with a capacity-checked roadmap and a monthly retro.

## Grounded inputs

Most AI ad generation fails on input grounding, not output quality. For scaled production, maintain a durable corpus: 10–20 screenshots of the highest-performing ads from the last 90 days; 50–100 customer reviews; top comments from existing campaigns; the brand voice document, colours, logo and product assets.

Why each matters: winning ads carry the hooks, structures and angles already proven for the brand; reviews carry the exact language buyers use for pain, transformation and unexpected benefits, so pull copy from them verbatim rather than paraphrasing; ad comments are the most-skipped and highest-value input, because objections become FAQ-style ads and unprompted praise surfaces angles nobody wrote.

Grounding rules: every concept cites its source (which review, winning ad or comment it traces to); no invented claims, stats or testimonials, ever; if the winning-ads or reviews input is empty, stop and ask the user to populate it before generating, and do not generate ungrounded concepts as a fallback. Inputs decay: refresh winning ads as new ads scale, reviews and comments monthly.

## Platform specs

Platforms reject or truncate creative that exceeds these limits, so verify every piece of copy fits before delivering.

| Platform | Element | Limit |
| --- | --- | --- |
| Google Ads (responsive search) | Headline / description / display path | 30 chars (up to 15) / 90 chars (up to 4) / 15 chars each (2 paths) |
| Meta (Facebook/Instagram) | Primary text / headline / description | 125 chars visible (up to 2,200) / 40 chars / 30 chars |
| LinkedIn | Intro text / headline / description | 150 chars (600 max) / 70 chars (200 max) / 100 chars (300 max) |
| TikTok | Ad text / display name | 80 chars (100 max) / 40 chars |
| X | Tweet text / headline / description | 280 chars / 70 chars / 200 chars |

Responsive search ads: headlines must make sense independently and in any combination, since the platform combines them freely. Pin headlines to positions only when necessary. Include at least one keyword-focused, one benefit-focused and one call-to-action headline.

## Angles first, then variations

Before writing individual headlines, establish three to five distinct angles, each tapping a different motivation: pain point, outcome, social proof, curiosity, comparison, urgency, identity, contrarian.

For each angle, generate several variations, varying word choice, specificity (numbers against general claims), tone (direct, question, command) and structure (short punch against full benefit statement). Then validate every piece against the platform limits, flag anything over with a trimmed alternative, and organise the output for upload.

Present creative organised by angle with character counts, so an over-limit headline is visible at a glance. At scale (10 or more variations), offer a CSV for direct upload.

## Iterating from performance data

1. **Analyse winners** — top performers by CTR, conversion rate or ROAS (ask which metric matters most). Identify winning themes, structures, word patterns and character utilisation.
2. **Analyse losers** — themes that fall flat, and patterns in low performers (too generic, too long, wrong tone).
3. **Generate new variations** — double down on winning themes with fresh phrasing, extend winning angles, test one or two new angles, and avoid underperformer patterns.
4. **Document the iteration** — round, date, top and worst performers with metrics, winning patterns, new variations and angles, retired angles.

Fatigue is the signal for new creative, not more budget: when frequency rises and click rate falls, change the angle. Allow 1,000 or more impressions before judging a creative, and change one variable per test cycle.

## Writing quality

- **Headlines that click.** Specific over vague ("Cut reporting time 75%", not "Save time"), benefits over features, active voice over passive, numbers when possible. Avoid jargon the audience will not recognise, unspecific superlatives ("Best", "Leading"), all caps, clickbait the landing page cannot deliver, and shortened product names (use the exact product name from the brief in every field).
- **Test hypotheses that can lose.** "This will resonate with renters" cannot lose; "beats the control on CTR among renters" can. Name the metric and the comparison, state the expected direction and a magnitude when a baseline exists.
- **No AI tells.** Never write contrast reveals ("It's not X, it's Y"), negation lists ("No X, no Y, no Z"), trailing pile-ons that restate the claim after a comma, self-answered questions and colon reveals ("The result? 3x faster"), or stock phrases ("Say goodbye to", "Unlock the power of", "Take it to the next level"). No em dashes in headlines, descriptions or primary text. No hook slop ("Stop scrolling", "Here's what nobody tells you") unless the hook is hyper-specific to the viewer. No CTA slop ("Get started today"); name the action and what they get. Across a batch, vary the sentence shapes: ten variations that all open the same way read as generated.
- **Descriptions that convert.** Descriptions complement headlines, not repeat them: add proof points (numbers, testimonials, awards), handle objections ("No credit card required"), reinforce the call to action, and add urgency only when genuine.

## Batch production

Generate in waves: core angles first (three to five angles, five variations each), then extended variations on the top two angles, then wild-card angles (contrarian, emotional, specific). Quality filter: remove anything over the character limit, remove duplicates or near-duplicates, flag anything that might violate platform policies, and check that headline and description combinations make sense together.

For scaled static batches, save to a dated folder with an index listing every concept with its template type and grounding source, so a reviewer can scan it in two minutes and pick the best five to ten for testing. Picking five winners from fifty concepts yields better creative than picking five from ten.

## Common mistakes

- Headlines that only work together (responsive search headlines combine randomly).
- Ignoring character limits; platforms truncate without warning.
- All variations sounding the same; vary angles, not just word choice.
- No call-to-action headlines in responsive search ads.
- Generic descriptions that waste the slot.
- Iterating without data; gut feeling is less reliable than metrics.
- Generating without grounding, and skipping the comments input.
- Testing too many things at once, and retiring creative too early.

## Source

Adapted and rewritten from `coreyhaines31/marketingskills` skills/ad-creative/SKILL.md, https://github.com/coreyhaines31/marketingskills (MIT). Compressed from 474 lines: the per-format template library, video-ad references, tool integrations and review-page template are not carried over.
