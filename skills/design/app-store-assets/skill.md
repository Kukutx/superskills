---
name: app-store-assets
description: Design App Store and Google Play visual assets such as screenshot sets, feature graphics and promotional imagery with clear hierarchy, credible UI and platform-aware production checks.
---

# App Store Assets

## Workflow

1. Identify platform, asset type, target audience and the single message each asset must communicate.
2. Verify current platform dimensions/rules when exact compliance matters; do not rely on remembered store specifications.
3. Build a visual hierarchy for **thumbnail/mobile viewing first**.
4. Use real product UI/features. Simplify presentation if needed, but do not fabricate functionality.
5. Keep headline copy short; route deeper wording work to `writing/app-store-copy` when needed.
6. Design a screenshot **sequence**, not isolated posters: value -> key use cases -> trust/proof/control as relevant.
7. Export and review at actual store preview size.

## Visual rules

- one focal message per frame;
- readable typography and strong contrast;
- safe margins for devices/cropping;
- consistent device mockup, lighting and visual system across the set;
- UI must remain plausible and legible;
- avoid overcrowded compositions, fake ratings/reviews, invented notifications or impossible UI;
- do not bake unnecessary localized text into background artwork.

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
- no misleading feature, fake social proof or unsupported claim;
- localized variants have enough layout flexibility;
- exported assets are checked on both large and small displays when relevant.

## Boundaries

Use `creative/image-prompt-director` only as a visual-generation subtask. Use `design/image-review-refiner` for reviewing an existing generated asset. Use `writing/app-store-copy` when the main problem is copy rather than composition.