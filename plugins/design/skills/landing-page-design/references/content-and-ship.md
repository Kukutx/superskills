# Content, states and ship checklist

## Sample content

- Write real draft copy in the product's voice; no lorem ipsum or "Your headline here".
- Testimonials, customer logos, user counts and metrics: use the user's real proof. When none is supplied, use clearly marked placeholders or sample content labelled as sample, never figures or quotes that read as real claims. If the user wants realistic mockup content, keep names and numbers plausible (varied dates, non-round figures, region-appropriate names, industry-appropriate company names) and label the block as sample.
- Avoid filler: "revolutionize", "supercharge", "cutting edge", "effortless", "transform your workflow", "next level", "harness the power", "world class", and Chinese equivalents such as 「颠覆」「赋能」「一站式」「极致」. Say what the product does.
- Sentence case for English headings and buttons.
- System messages are calm and specific: "Invoice sent to Dana"; "Upload failed. The file is over 20 MB." No exclamation marks.

## Interaction states

Every interactive element has hover (background shift, slight scale or translate), active (`scale(0.98)` or `translateY(1px)`), a visible focus ring, skeleton loading shaped like the real layout, a composed empty state and inline specific errors (never `window.alert()`). No dead links: a `#` button is either linked or visibly disabled. Navigation marks the current page.

## Ship requirements

Privacy and terms links; a branded 404; client-side validation for email and required fields; skip-to-content link; cookie consent where the jurisdiction requires it; favicon; `<title>`, meta description, `og:image` and social tags; alt text on meaningful images; semantic `<nav>`, `<main>`, `<section>`; a way back from every page.

## Checklist

**Strategy**
- [ ] One offer, one audience, one primary action; no competing CTAs above the fold
- [ ] Specific outcomes instead of vague verbs; at least one risk reversal
- [ ] Proof sits beside the claim; no invented proof presented as real
- [ ] Layout type chosen and justified

**Visual**
- [ ] One approved typeface, no italics, no ultra bold; balanced headings
- [ ] Sizes on the type scale; spacing from the spacing table; nested radii follow the formula
- [ ] No single-side card borders, no background gradients
- [ ] Hero text capped at 680px with meaningful breaks
- [ ] Icons from Phosphor, Solar or Iconamoon
- [ ] Motion on the base curve, transform/opacity only, reduced-motion respected
- [ ] Tagline reveal section present

**Content and ship**
- [ ] Real draft copy; samples labelled; no filler words
- [ ] All interaction states present; no dead links
- [ ] 404, legal links, validation, favicon, meta tags, alt text
