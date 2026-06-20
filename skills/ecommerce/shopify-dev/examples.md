# Shopify Development Examples

## Example 1: Product page trust badge

### Input

```text
Use the Shopify Development Skill.

Theme: Dawn
Goal: Add a small trust badge under Add to Cart on product pages
Constraints: no paid app
Output: implementation steps, code, placement, validation
```

### Expected output pattern

```text
Direct answer:
Use a small Liquid snippet or custom block in the product information section.

Recommended implementation:
Start with theme customizer if the theme supports custom liquid blocks. If not, add a snippet and render it in main-product.liquid.

Code/configuration steps:
1. Online Store > Themes > Customize > Product template.
2. Add Custom Liquid block if available.
3. Paste minimal HTML/CSS.

Risks/limitations:
- Theme update may overwrite direct code edits.
- Badge claims should be accurate.

Validation checklist:
- Desktop/mobile layout.
- Product variants still work.
- Add to Cart remains visible.
```

## Bad output

```text
Install a trust badge app.
```

Why bad:

- App-first answer.
- No native option.
- No placement guidance.
