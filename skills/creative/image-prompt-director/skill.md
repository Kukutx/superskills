---
name: image-prompt-director
description: Turn a visual goal into a coherent image direction and production-ready generation prompt. Use when the user wants image concepts, prompts, art direction or generation planning.
---

# Image Prompt Director

## Use

Use for illustration, product visuals, characters, marketing imagery, mockup direction, visual concepts and image-generation prompts.

If the user wants an existing image critiqued/refined, use `design/image-review-refiner`. If another domain Skill owns production constraints (for example xTool or game assets), that domain Skill stays primary.

## Workflow

1. Identify the image's **use**, audience and required format before styling it.
2. Preserve explicit user references and visual intent; do not silently redesign the concept.
3. Define only the visual controls that matter:
   - subject / action;
   - composition / camera;
   - environment;
   - lighting / color;
   - material / rendering language;
   - text/UI policy;
   - aspect ratio / production constraints.
4. Make foreground/background hierarchy and focal point explicit.
5. Add avoid rules only for likely failure modes; do not produce a generic negative-prompt dump.
6. When consistency across a series matters, lock the reusable invariants separately from scene-specific instructions.

## Output

Default:

- **Visual direction** — 2–5 concrete decisions.
- **Main prompt** — copy-ready.
- **Avoid / constraints** — only meaningful failure prevention.
- **Composition / production notes** — only when needed.
- **Variants** — max 3 and only when they represent genuinely different directions.

When the user asks to generate the image directly, treat the prompt as internal production guidance rather than forcing the user to copy it.

## Quality rules

- Describe observable visual properties, not vague adjectives like “premium”, “stunning” or “modern” without visual meaning.
- Avoid contradictory instructions such as simultaneously demanding minimal composition and many focal elements.
- Do not bake dynamic/localized copy into artwork unless explicitly required.
- For UI/product screenshots, do not invent product features or misleading interface states.
- For character/series consistency, preserve identity, silhouette, proportions, palette and recurring props.
- Match detail density to final display size; do not optimize only for zoomed-in beauty.

## Validation

Before approval, check: intended use, focal hierarchy, legibility at target size, unwanted text/logos/artifacts, consistency with references, and whether the prompt contains any instruction that does not help the final image.