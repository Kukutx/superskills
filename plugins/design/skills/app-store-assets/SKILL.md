---
name: app-store-assets
description: App Store and Google Play visual assets such as screenshot sequences, feature graphics and promo imagery built from real UI. Use for store visuals, not listing wording.
---

# App Store Assets

## Workflow

1. Identify platform, asset type, target audience and the single message each asset must communicate.
2. Verify current platform dimensions/rules when exact compliance matters; do not rely on remembered store specifications.
3. Build a visual hierarchy for **thumbnail/mobile viewing first**.
4. Use real product UI/features, captured from the product at high resolution. Simplify presentation if needed, but do not fabricate functionality, and do not have an image model draw the interface: it invents UI that will not match the app.
5. Keep headline copy short; route deeper wording work to `writing/app-store-copy` when needed.
6. Design a screenshot **sequence**, not isolated posters: value -> key use cases -> trust/proof/control as relevant.
7. Export and review at actual store preview size.

## Visual rules

- one focal message per frame, with a caption of about five to seven words;
- lead with the screens that show the core value; settings and onboarding screens do not take the first slots;
- readable typography and strong contrast;
- safe margins for devices/cropping;
- consistent device mockup, lighting and visual system across the set;
- UI must remain plausible and legible;
- avoid overcrowded compositions, fake ratings/reviews, invented notifications or impossible UI;
- do not bake unnecessary localized text into background artwork;
- generated imagery is for backgrounds and atmosphere only: no interface, no logo and no readable text in it; arrows, callouts, logos and captions are added afterwards in a design tool;
- for a consistent set, settle the style on three or four trial images, keep the exact prompt as the template, and crop and label afterwards instead of regenerating;
- an icon carries no text and has a strong, recognizable shape.

## Output

Default:

- **Asset goal / sequence**
- **Layout direction** per asset
- **Headline/copy placeholders or options**
- **Visual elements / UI treatment**
- **Image-generation prompt** where external imagery is needed
- **Production / compliance checks**

If the user supplied an exact asset size, use it. Otherwise verify the current platform spec before giving precise dimensions.

## Production checks

- final canvas and file format match current platform requirements;
- text remains readable at store preview scale;
- no private/sensitive data in screenshots;
- screenshots show the current UI, and are redone after a redesign;
- no misleading feature, fake social proof or unsupported claim;
- App Store review (guidelines section 2.3, read October 2026): screenshots show the app in use, not only title art, a login page or a splash screen; a preview uses only screen capture of the app, with narration and overlays allowed; screenshots and previews make clear which featured items need an in-app purchase; icons, screenshots and previews suit a 4+ audience even when the app is rated higher; no names, icons or imagery of other mobile platforms; account data shown is fictional; the rights to every element are held;
- a store preview may autoplay without sound, so it has to make sense muted;
- Google Play restricts what a title, icon and graphics may claim; read its current metadata and preview-asset policy before adding a ranking, a price, a promotion or a call to action to an asset;
- localized variants have enough layout flexibility;
- exported assets are checked on both large and small displays when relevant.

## Boundaries

Use `creative/image-prompt-director` only as a visual-generation subtask. Use `design/image-review-refiner` for reviewing an existing generated asset. Use `writing/app-store-copy` when the main problem is copy rather than composition.