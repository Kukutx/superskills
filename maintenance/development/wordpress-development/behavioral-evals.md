# WordPress Development behavioral evals

Maintenance-only. Protect the reference split, the WordPress/Drupal/Shopify boundary, and the decisions a plain model gets wrong: block checkout fields, HPOS-safe order code, serialisation-safe migrations and code that lives outside core and parent themes.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| wp-001 | “WooCommerce 店铺 2025 年新开的，用默认结账页，我用 woocommerce_checkout_fields 加了一个 SDI 编码字段，前台不显示。” | `woocommerce.md` | none | debugging hook priority or caching while missing that the Checkout block ignores that filter |
| wp-002 | “我们插件用 get_post_meta 读订单的自定义字段，店铺开了 HPOS 以后全是空的。” | `woocommerce.md` | none | switching the store back to post storage as the fix, or querying the order tables with raw SQL |
| wp-003 | “staging.example.it 做好了要换成 www.example.it 正式上线，页面都是 Elementor 做的。” | `operations.md` | none | sed or SQL REPLACE on the dump, or skipping Elementor's URL replacement and CSS regeneration |
| wp-004 | “父主题更新以后，我们之前改过的 header.php 被覆盖了。” | `themes-and-builders.md` | none | editing the parent theme again |
| wp-005 | “员工在后台的预约管理页要改预约状态，帮我写这个 REST 接口，预约存在自定义表里。” | `plugins-and-security.md` | none | a route without a capability-checking permission_callback or argument validation, or a nonce treated as the authorization |
| wp-006 | “后台和前台都很慢，Query Monitor 显示自动加载的 options 有 8MB。” | `operations.md` | none | adding another caching plugin before fixing the autoloaded options |
| wp-007 | “线上店铺每天都有订单，staging 改了很多页面，直接把 staging 数据库覆盖到正式站吧。” | `development/wordpress-development` | none | overwriting a production database that holds orders created since the copy |
| wp-008 | “Shopify 的 Dawn 主题商品卡片加一个新品角标。” | `ecommerce/shopify-dev` | none | invoking wordpress-development for a Shopify theme |
| wp-009 | “Drupal 10 的新闻列表要按区过滤。” | `development/drupal-development` | none | invoking wordpress-development for a Drupal site |

## Pressure cases

### Code that belongs in a plugin

Prompt: `把这段注册自定义文章类型的代码加到主题的 functions.php 里。`

Pass: a post type that holds content must survive a theme change, so it goes in a site plugin or a must-use plugin; a child theme is for presentation.

### Template override drift

Prompt: `WooCommerce 更新后，状态页说我们覆盖的模板过期了。`

Pass: compare each override with the new core template, port the changes or replace the override with a hook; do not just bump the version comment.

## Regression rule

Add a case only when it protects a real ownership boundary or a decision a plain model gets wrong. Version facts are re-verified at execution time, not frozen into cases.
