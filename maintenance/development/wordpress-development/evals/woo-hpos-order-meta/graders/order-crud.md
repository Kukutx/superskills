---
type: llm
---

Under HPOS, orders are not posts: post meta functions and the posts-screen hooks no longer reach them. The plugin has to use WooCommerce's order API.

PASS if the reply rewrites the storage through the order object for both writing and reading (`wc_get_order()`, `update_meta_data()` or `add_meta_data()` followed by `save()`, and `get_meta()` to read), and does not present switching back to post storage as the fix; it may mention compatibility mode only as a temporary measure while the plugin is fixed. Declaring HPOS compatibility, pointing out that the column hooks belong to the old posts screen, and escaping the echoed value are welcome but not required.

FAIL if the reply's main recommendation is to switch the store back to WordPress posts storage; if the rewritten code still calls `update_post_meta()` or `get_post_meta()` on the order ID; or if it reads or writes the order tables with raw SQL.
