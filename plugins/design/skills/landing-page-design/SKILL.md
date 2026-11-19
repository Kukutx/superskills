---
name: landing-page-design
description: Plan, write and build a single-goal landing or marketing page with section structure, conversion copy, SEO and a default visual system. Use for a new or restyled page, not copy-only edits.
---

# Landing Page Design

A landing page wins one intent: **one offer → one audience → one primary action**. A homepage serving many intents is a different job.

Adapted from `elayadesign/ai-design-skills` (MIT); see maintenance `sources.md`.

## Scope

Owns: landing and marketing pages, their sections, conversion copy and the visual defaults below.

Not this Skill:

- audience, value proposition or messaging that is still undecided -> `marketing/product-positioning` first;
- the words alone for an existing page, ad or post -> `writing/marketing-copy`;
- an existing page or flow that does not convert -> `marketing/conversion-review`;
- Shopify theme or Liquid implementation -> `ecommerce/shopify-dev` (use this Skill only for the page's structure and copy);
- app dashboards and product UI: borrow the visual system only if the user has no design system.

Precedence: the user's explicit request > an existing brand or design system > this Skill's visual defaults > framework defaults.

## Workflow

Strategy before visuals.

1. **Intake.** Primary action, the exact offer, what counts as a conversion, the audience and their problem, top three objections, traffic source and what visitors already know, proof and assets on hand, brand voice and design direction. Missing answers become stated assumptions; do not stall the build.
2. **Choose a layout** and say why:

   | Type | Use when |
   | --- | --- |
   | Classic hero + sections | the product reads from one hero screenshot (most common) |
   | Long-form story | visitors need education and skepticism handled |
   | Minimal conversion | high-intent traffic or a short offer (download, waitlist) |
   | Comparison | search intent is "X vs Y" or "best for" |

3. **Outline before code**: section order; hero copy (headline, subheadline, CTA, proof line); 3–5 benefits; how it works in 3 steps; 6–12 FAQ; index or noindex with title and meta; the layout choice.
4. **Build section by section**: hero, benefits, how it works, proof, FAQ, final CTA. Do not rebuild the whole page on every iteration.
5. **Apply** `references/visual-system.md` and `references/content-and-ship.md`, then run the checklist there.

## Page structure

- **Above the fold:** headline (outcome + audience), subheadline (how, with specifics), one primary CTA (verb + what they get), one proof signal, a hero visual.
- **Middle:** problem to solution, 3–5 outcome-driven benefits, how it works, social proof, and one large tagline section (see visual system).
- **Bottom:** FAQ, risk reversal (trial, cancel anytime, guarantee), final CTA identical to the top one.

## Conversion rules

- Match the hero to the traffic source: an ad's promise and tone carry into the headline.
- One primary CTA; no competing CTAs above the fold.
- Benefits before features; specific beats vague ("4 小时周报缩到 15 分钟", not "提升效率").
- At least one risk reversal.
- Put proof beside the claim it supports; treat objections as a section, move FAQ up for high-friction offers.
- CTA labels are verb + object ("Start free trial", "领取清单"), never "Learn more" or "Submit".
- Index evergreen pages whose search intent matches the promise; `noindex` ad-only or time-bound campaign pages.

## Proof honesty

Never present invented testimonials, customer logos, user counts or metrics as real. When real proof is missing, write clearly marked placeholders (for example `[客户评价：待替换]`) or realistic sample content labelled as sample, and list what the user needs to supply.

## References

| Need | Load |
| --- | --- |
| typography, spacing, radius, color, hero, icons, motion, tagline section | `references/visual-system.md` |
| sample content, interaction states, ship requirements, final checklist | `references/content-and-ship.md` |
