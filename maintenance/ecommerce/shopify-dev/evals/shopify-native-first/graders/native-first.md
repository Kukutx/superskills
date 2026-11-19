---
type: llm
---

Both needs can be met without an app: Dawn has a built-in announcement bar section, and a "新品" badge can be added with a small Liquid change (for example checking `product.tags contains 'new'` in the card snippet).

PASS if the primary recommendation for BOTH needs is a Shopify-native or theme-level approach (announcement bar in the theme editor; a small Liquid/snippet change for the badge), and the reply says where to make the badge change (which file/snippet or a duplicated theme). Mentioning an app as an optional alternative is fine.
FAIL if the primary recommendation for either need is installing an app (free or paid), or if the reply only lists apps without offering the native/theme route.
