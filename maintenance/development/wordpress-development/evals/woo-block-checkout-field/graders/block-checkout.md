---
type: llm
---

A store created in 2025 with the default checkout page uses the Checkout block, which does not render fields added through `woocommerce_checkout_fields`.

PASS if the reply's main diagnosis is that the checkout page is, or most likely is, the block-based Checkout and that the classic `woocommerce_checkout_fields` filter does not add fields there, and it gives the block-compatible way to add the field: the Additional Checkout Fields API (`woocommerce_register_additional_checkout_field`, registered on `woocommerce_init` or later). Explaining how to confirm which checkout the page uses, or mentioning the shortcode checkout as a fallback with its trade-off, is fine.

FAIL if the main diagnosis is hook priority, caching, the theme or a mistake in the array; if it recommends editing WooCommerce plugin files or templates; or if it never mentions the Checkout block.
