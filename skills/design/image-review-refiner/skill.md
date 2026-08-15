---
name: image-review-refiner
description: Review an existing generated or designed image against its intended use, preserve what works, prioritize visible defects, and produce precise next-round changes or a refined prompt.
---

# Image Review Refiner

## Workflow

1. Judge the image against its actual purpose and target size, not abstract aesthetics.
2. Separate:
   - what already works and must stay;
   - high-impact problems;
   - low-priority polish.
3. Diagnose problems concretely: hierarchy, anatomy, geometry, lighting, consistency, text/UI, cropping, artifacts, style drift.
4. Change as little as needed to fix the current failure. Do not restart from scratch when the composition is already working.
5. Convert the diagnosis into explicit edit instructions or a refined generation prompt.

## Output

Default:

- **Keep**
- **Fix first** — prioritized
- **Remove / avoid** only when needed
- **Refined edit/generation instruction**
- **Final production checks**

Do not force a separate negative prompt if the target tool/workflow does not benefit from one.

## Constraints

- Preserve user-approved identity, composition and brand elements unless they cause the problem.
- Do not hide the main issue inside a long list of minor defects.
- For product/UI visuals, flag invented or misleading interface content.
- For people/characters, distinguish stylistic choices from actual anatomy/consistency errors.
- Review at intended display size when readability or pixel/detail density matters.
- If the image itself is not available, clearly distinguish review of the user's description from direct visual inspection.