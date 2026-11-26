---
name: conversion-review
description: Review a landing page, signup or checkout flow, popup or lead form for conversion problems, with ranked fixes and tests. Use when a page does not convert, not for SEO, ads or UI critique.
---

# Conversion Review

## Use

Use when visitors arrive and do not act: a landing, pricing or product page that does not convert, a signup or registration flow people abandon, a checkout, an email-capture popup or banner, and the offer behind a lead form (a checklist, template or free tool given in exchange for an email address).

A usability and accessibility critique of a screen belongs to `design/design-review`. Designing the experiment that settles a disputed change belongs to `marketing/ab-testing`. What happens after signup (activation, retention, cancel flows) belongs to `product/onboarding-and-retention`. Rewriting the whole page belongs to `writing/marketing-copy`; search visibility to `marketing/seo-audit`.

## Domain inputs and blockers

- **Three facts before judging anything**: the page type, the one conversion it exists for, and where its traffic comes from. The same page is right for one source and wrong for another.
- Useful when available: the current conversion rate and the target, what happens after the conversion, field-level drop-off for a form, recordings or heatmaps, what has already been tried, and the split between mobile and desktop.
- Pasted text, a screenshot or a description of the steps is enough to start. Without numbers, findings are judgements from principle and are labelled as hypotheses; the size of an improvement is never estimated.
- **Rule out the obvious first**: a broken form, a slow page, a tracking error. And when the real shortage is traffic, say that conversion work is the wrong lever.
- For a signup flow, which fields the business truly needs before first use, and any compliance requirement on what must be collected.

## Reviewing a page

Check in this order, which runs from the largest effect to the smallest:

1. **Value proposition**: can a new visitor say what this is and why it matters within five seconds?
2. **Headline**: does it state the benefit, and does it echo the ad, email or search result that brought the visitor?
3. **Call to action**: position, wording and visual priority; one primary action per page.
4. **Visual hierarchy**: does the eye reach the proposition, the proof and the action in that order?
5. **Trust signals**: placed next to the action and straight after benefit claims; testimonials that are specific, attributed and carry a photo.
6. **Objections**: are the main reasons not to act answered on the page?
7. **Friction**: too many form fields, an unclear next step, confusing navigation, fields marked required without need, mobile problems, slow loading.

By page type: a landing page matches its traffic source in four ways (the headline echoes the ad, the visual matches the creative, the offer is the one promised, and different audiences get different pages), has one action and can drop the navigation; a home page leads with the broadest value and then gives each kind of visitor a clear path; a feature page ties the feature to a benefit, shows it in use and has its own route to trial or purchase; a blog post uses in-line calls to action related to its topic.

**Pricing page.** When nobody chooses the middle plan, check three things: is the comparison clear, is a recommended plan marked, and does the visitor know which plan is theirs; then whether the plans differ enough to matter. Worth testing: the number of plans and their order, a "most popular" mark, how annual and monthly prices and the saving are shown, a calculator for usage pricing, a short quiz that picks a plan, an FAQ for pricing objections, and where the guarantee sits.

**Conversion fell after a redesign.** Go through what changed: a trust signal that disappeared, a weaker value proposition, a different hierarchy of actions, new friction, a broken match with the traffic source. Rank by likely effect, roll back the riskiest change first, and test the rest.

Signup and form rules are in [references/signup-and-forms.md](references/signup-and-forms.md).

Popup and banner rules are in [references/popups-and-banners.md](references/popups-and-banners.md).

Lead magnets and free tools are in [references/lead-magnets-and-tools.md](references/lead-magnets-and-tools.md); field, button and per-format detail is in [references/forms-and-lead-offers.md](references/forms-and-lead-offers.md).

## Output

Every review ends in the same four blocks:

1. **Quick wins**: changes to make today.
2. **High-impact changes**: larger work, in priority order.
3. **Test ideas**: disputed changes written as hypotheses worth an experiment.
4. **Copy alternatives**: two or three options for the key elements (headline, call to action), each with its reason.

Each finding states the issue, its effect on the visitor, the fix and a priority. A signup redesign adds the field set with the reason for each field, their order, and the labels, placeholders, button and error texts. A popup plan gives type, trigger, placement, frequency and copy. A lead-magnet plan gives format, topic, stage, effort, outline, gating, distribution and what to measure.

## Constraints

- Do not quote a conversion uplift, a benchmark rate or a "cost per extra field" figure; none of the circulating ones has a source, and the user's own data decides.
- Do not propose hidden close buttons, guilt-based decline text, fake scarcity or fake countdowns.
- Consent and privacy wording for email capture depends on where the visitors are; mark it for the user to check against the applicable law. This Skill does not give legal advice.
- Keep to the conversion problem; visual taste and full accessibility conformance are a separate review.
