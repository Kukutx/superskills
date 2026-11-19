# WordPress Development maintenance sources

Maintenance-only. Do not load for normal WordPress tasks.

## Policy

- Every row is an official page that was opened and read on 2026-11-19 when the Skill was written. The Skill states only what the page said; anything a page did not confirm is written in the Skill as something to check, or left out.
- WordPress and WooCommerce versions, PHP and database requirements, WooCommerce defaults and Elementor hooks change. On review, re-open each page and change the Skill only where the page changed. The support box in `SKILL.md` carries the check date and must be updated with it.
- The site's own versions (`wp core version`, `wp plugin list`) are the source of truth for a given site.

## Source register

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| WordPress releases | https://wordpress.org/download/releases/ | 7.1.5 latest (18 Nov 2026); 7.1 on 19 Aug 2026; 7.0 on 20 May 2026 | 2026-11 |
| WordPress requirements | https://wordpress.org/about/requirements/ | PHP 8.3+ recommended; MariaDB 10.11+ or MySQL 8.4+ recommended; 7.4 legacy floor | 2026-11 |
| Hosting handbook, WordPress 7.1 compatibility | https://make.wordpress.org/hosting/handbook/compatibility/version/7-1/ | PHP 7.4 to 8.5 supported; 8.4 and 8.5 recommended; database minimums | 2026-11 |
| Make WordPress Core, dropping PHP 7.2 and 7.3 | https://make.wordpress.org/core/2026/01/09/dropping-support-for-php-7-2-and-7-3/ | minimum PHP 7.4 from WordPress 7.0 | 2026-11 |
| WooCommerce server requirements | https://woocommerce.com/document/server-requirements/ | WordPress 6.9+, PHP 8.3+ (tested to 8.4), MySQL 8.0+ or MariaDB 10.6+, 256 MB | 2026-11 |
| WooCommerce releases | https://developer.woocommerce.com/releases/ | 11.3.1 latest (19 Nov 2026); only the latest version is considered fully secure | 2026-11 |
| WooCommerce HPOS overview | https://developer.woocommerce.com/docs/features/high-performance-order-storage/ | default for new installs since 8.2; compatibility mode and sync; `wp wc cot sync` | 2026-11 |
| WooCommerce HPOS recipe book | https://developer.woocommerce.com/docs/features/orders/high-performance-order-storage/recipe-book/ | compatibility declaration, `OrderUtil` detection, order CRUD, order screen ID, legacy hooks to review | 2026-11 |
| WooCommerce `wc_get_orders()` | https://developer.woocommerce.com/docs/extensions/core-concepts/wc-get-orders | order queries instead of `WP_Query`, `get_posts()` or SQL; meta queries only on HPOS | 2026-11 |
| WooCommerce hook alternatives for blocks | https://developer.woocommerce.com/docs/block-development/reference/hooks/hook-alternatives/ | `woocommerce_checkout_fields` cannot edit core fields in the Checkout block | 2026-11 |
| WooCommerce additional checkout fields | https://developer.woocommerce.com/docs/block-development/extensible-blocks/cart-and-checkout-blocks/additional-checkout-fields/ | `woocommerce_register_additional_checkout_field` on `woocommerce_init` or later; types select, text, checkbox, date; contact, address and order locations | 2026-11 |
| WooCommerce, customizing the cart and checkout pages | https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/ | blocks are the default for stores started after 8.3; hook-based extensions need integration work; how to tell block from shortcode | 2026-11 |
| WooCommerce template structure | https://developer.woocommerce.com/docs/theming/theme-development/template-structure/ | override path, outdated-template notice, hooks preferred, block themes differ | 2026-11 |
| Block editor handbook, theme.json reference | https://developer.wordpress.org/block-editor/reference-guides/theme-json-reference/theme-json-living/ | schema version 3 for WordPress 6.6+; schema URLs | 2026-11 |
| REST API handbook, custom endpoints | https://developer.wordpress.org/rest-api/extending-the-rest-api/adding-custom-endpoints/ | required permission callback, `_doing_it_wrong` since 5.5, `__return_true` for public data, argument callbacks | 2026-11 |
| Common APIs, nonces | https://developer.wordpress.org/apis/security/nonces/ | nonces are not authorization; one-day lifetime; session binding; functions | 2026-11 |
| Common APIs, escaping | https://developer.wordpress.org/apis/security/escaping/ | escape late; escaping functions; localisation helpers | 2026-11 |
| Function reference, `wp_get_environment_type()` | https://developer.wordpress.org/reference/functions/wp_get_environment_type/ | values, production default, constant or variable, since 5.5 | 2026-11 |
| WP-CLI, search-replace | https://developer.wordpress.org/cli/commands/search-replace/ | serialised data handling, `--dry-run`, `--precise`, table scope, `--skip-columns=guid`, multisite | 2026-11 |
| WordPress Coding Standards | https://github.com/WordPress/WordPress-Coding-Standards | 3.x via Composer, rulesets, PHPCompatibilityWP | 2026-11 |
| Elementor developers, registering widgets | https://developers.elementor.com/docs/managers/registering-widgets | `elementor/widgets/register` and `register()` | 2026-11 |
| Elementor developers, widget registration change | https://developers.elementor.com/docs/deprecations/advanced-example | 3.5 replaced `widgets_registered` and `register_widget_type()` | 2026-11 |
| Elementor developers, replace-urls CLI | https://developers.elementor.com/docs/cli/replace-urls | `wp elementor replace-urls <old> <new>` | 2026-11 |
| Design Comuni Italia WordPress theme | https://github.com/italia/design-comuni-wordpress-theme | official comuni theme for WordPress; child theme recommended | 2026-11 |
| Your Europe, accessibility of goods and services | https://europa.eu/youreurope/business/selling-in-eu/selling-goods-services/accessibility/index_en.htm | applies after 28 June 2025; online shops covered; service microenterprise exemption | 2026-11 |
| AgID, accessibilità e usabilità | https://www.agid.gov.it/it/ambiti-intervento/accessibilita-usabilita | D.Lgs. 82/2022 transposes the European Accessibility Act; AgID supervises | 2026-11 |

## Not verified

- Italian electronic-invoicing fields for WooCommerce stores; the Skill says to confirm them with the client's accountant.
- The exact PHPStan WordPress stubs package and the Plugin Check plugin's current behaviour; named as tools only.
- Whether `wp elementor replace-urls` also regenerates CSS; the Skill keeps regeneration as a separate step.
