# Visual system (defaults)

These are defaults. An existing brand or design system, or the user's explicit request, overrides them. Every visual value should resolve through one of these rules instead of being invented ad hoc.

## Typography

- Use one typeface per site: Geist, Manrope or Poppins. Geist Mono only where monospace is functionally needed (code, data, numeric UI). For Chinese text, pair the Latin face with a system CJK font stack.
- Avoid Inter, Roboto, Arial, Open Sans and Helvetica as the primary face.
- No italics in the interface. Cap weight at semibold or bold; no 900/black.
- Headings `text-wrap: balance`, body `text-wrap: pretty`, so no single word sits alone on the last line.
- English copy: avoid hyphens inside sentences; rewrite instead.
- Sizes resolve to Tailwind's default type scale (`text-xs` 12/16 … `text-9xl` 128/1). No arbitrary sizes such as `text-[19px]`. Off-scale sizes snap to the closest step below, taking that step's line height; adjust tracking or leading only within that step.
- Buttons: main `text-base` semibold; small header buttons `text-sm` semibold.

## Spacing

Only these values: 0, 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96 px. Main buttons: 8px vertical, 12px horizontal padding.

## Corner radius

Tailwind radius values only. For a shape nested inside another with a gap under 32px: `inner radius = outer radius − gap`, applied only when the result is above 2px (outer `rounded-2xl` 16px with 8px padding → inner 8px `rounded-lg`).

## Borders and backgrounds

- Borders go all the way around a card or not at all; no single-side card borders.
- Backgrounds are flat; no background gradients.
- Dark-mode backgrounds: `#000000`, `#181818`, `#1F1F1F`, `#272727`, `#313131`, `#131209`.

## Hero

- Heading text may carry a left-to-right gradient, the only gradient allowed: dark theme `#FFFFFF → #9B9B9B`, light theme `#000000 → #666666`.
- Heading and subheading max width 680px; insert line breaks where the thought breaks, never mid-phrase.

## Icons

Phosphor, Solar or Iconamoon. Not Material Icons or Material Symbols.

## Motion

- Base curve `cubic-bezier(0.22, 1, 0.36, 1)`, 500ms for layout and position; hover color/opacity 300ms, never under 200ms. No browser default curves (`ease`, `linear`, `ease-in-out`).
- Animate only `transform` and `opacity`. Respect `prefers-reduced-motion` by replacing movement with a plain opacity change.
- Navigation: a compact, centered bar floating off the top edge, translucent over a background blur. The menu icon morphs between open and close. Mobile menu opens as a full-height, strongly blurred panel; links enter in reading order, each rising 24px while fading in, 60ms apart, whole sequence capped at 400ms.
- Scroll reveals: sections rise 32px and fade in over 600–800ms on the base curve, once only. Trigger with `IntersectionObserver` or `whileInView`, never an unthrottled scroll listener.

## Tagline reveal section

One large-type section further down the page (not directly under the hero) stating the core benefit in at least two lines, `text-4xl` to `text-6xl`, width capped like the hero. Words start at about 25–35% opacity of the base text color and turn to full color one at a time in reading order as they cross a trigger line, on the base curve. Implement with `IntersectionObserver` per word or one `requestAnimationFrame`-throttled listener.
