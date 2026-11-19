---
name: conversion-review
description: Review a landing page, signup or checkout flow, popup or lead form for conversion problems, with ranked fixes and test ideas. Use when a page or flow does not convert, not for SEO, ads or UI critique.
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

## Signup and forms

- **Every field costs completions.** For each one ask: is it needed before first use, can it be collected later, can it be inferred? Needed: an email address or phone number, and a password or a passwordless method. Often needed: a name. Usually deferrable: company, role, team size, phone, address.
- **Value before registration** where the product allows it: let the visitor try first and create the account afterwards. For a store, guest checkout is the default and the account is offered after the purchase.
- **One step or several**: one step for three fields or fewer, simple consumer products and high-intent traffic. A registration flow moves to several steps beyond three or four fields, a general form beyond five or six; then show progress, ask the easy questions first, allow going back, and keep the data on refresh.
- When the form is already only an email and a password and still converts poorly, look outside it: the value proposition before the form, a "no card required" line if true, a privacy assurance, a testimonial beside it, the password rules, the button text and the error handling.
- **Email**: one field with no confirmation field, validated in line, with common typos caught ("gmial.com").
- **Password**: requirements visible before the first failure and updated as the user types, a show toggle, pasting allowed, a strength meter instead of rigid rules.
- **Social sign-in** placed prominently: Google, Apple or Facebook for consumers; Google, Microsoft or single sign-on for business users. Whether a platform obliges an app to offer a particular sign-in option is taken from that platform's current rules, not assumed.
- **Labels stay visible**; a placeholder shows an example only, because it disappears on typing. An error keeps what was typed, moves focus to the field, and "this email is already registered" offers the way back in.
- **Email verification can wait.** Let the user into the product while it is pending, and offer resend, a "check your spam folder" hint and a way to change the address.
- **Mobile**: touch targets of 44 px or more, the right keyboard for each field, autofill, a single column, a call to action that stays in view, and a test on a real device.
- Promises such as "no credit card required" appear only when true.
- Measure: start rate, completion rate, drop-off per field, time to complete, error rate per field, mobile against desktop, share using social sign-in.

## Popups and banners

| Decision | Working default |
| --- | --- |
| Trigger | never on page load; after 30–60 seconds, or a scroll depth of a quarter to a half (half to two thirds on a blog post, where a behavioural trigger beats a timer); exit intent on desktop; after a number of pages; on a behaviour such as leaving a cart. A click-triggered popup interrupts nobody |
| Mobile | exit intent cannot be detected, so the back button or an upward scroll stands in for it; a bottom slide-in instead of a full-screen overlay; larger tap areas |
| Frequency | once per session at most; remember a dismissal and wait 7–30 days; never to someone who already converted; never inside checkout |
| Closing | a visible close button at the top right, a plain "No thanks", and closing on a click outside. The decline text is polite; "No, I don't want to save money" is not used |
| Copy | a specific button in the first person ("Send me the guide"); an exit popup offers something different from the entry one |
| Consent and access | no pre-ticked boxes, a link to the privacy policy, keyboard operable, focus kept inside the dialog while open, readable contrast |

Google's guidance (Search Central, page dated December 2025) is not to cover the whole page with an interstitial and to use a banner that takes a small part of the screen; intrusive dialogs can lead to poor search performance, and legally required ones such as age gates are exempt. When several popups exist, state which one wins when two would fire. When conversions have to be traded against complaints, lower the frequency and move to a lighter form (a slide-in for a modal, a bar for an overlay) before testing triggers. An announcement bar states a short headline, one line of benefit and an action, can be dismissed, runs for a set time and addresses the visitors it concerns, not everyone.

Whether to lead with a discount is unsettled: a first-order discount is common practice, and customers won by a discount may leave sooner. Treat it as a test, never as the default, and any deadline or countdown shown must be real.

## Lead magnets and free tools

- **A lead magnet** solves one specific problem, matches the buying stage, can be used within about ten minutes (thirty at most), leads toward the product and comes in one format.
- Stage fit: early awareness suits a checklist, cheat sheet, guide or quiz; evaluation suits a comparison template, assessment or set of case studies; decision suits a template, trial, migration checklist or ROI calculator.
- Effort, as working defaults: checklist 1–2 hours, cheat sheet 2–4 hours, template 2–8 hours, ebook 1–3 weeks, email mini-course or quiz 1–2 weeks.
- Ask for the email address only; add fields only for a high-value exchange such as a demo. The page has a headline, a preview, three to five points on what is inside, proof, the form and an FAQ. Deliver on the thank-you page and by email, and use the thank-you page for the next step.
- **A free tool** must be useful on its own, sit next to the main product, stay simple, and pass this test: value of a lead × expected leads > cost to build and maintain. Score eight factors from 1 to 5: search demand, audience fit, uniqueness, path to the product, ease of building, low maintenance, link potential, shareability. As a working heuristic, 25 or more of 40 is a strong candidate, 15–24 is promising, below 15 is reconsidered.
- Gating has four settings: fully gated, partly gated, open with an optional email field, fully open for search and brand. The first version does the core job, works on a phone and collects an email; accounts, saved results and polish wait. Tools that scrape, call an API or accept user input decay and carry security work, so budget for it.

The handling of individual fields, button states, each lead-magnet format, lead quality and free-tool types are in [references/forms-and-lead-offers.md](references/forms-and-lead-offers.md).

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
