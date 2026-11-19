---
name: wordpress-development
description: WordPress themes, child and block themes, Elementor, custom plugins, WooCommerce, REST, WP-CLI, caching, security and migrations. Use for WordPress sites, not Drupal or Shopify stores.
---

# WordPress Development

## Scope

Owns code and site work on WordPress: block, classic and child themes; Elementor builds and custom widgets; custom plugins and REST endpoints; WooCommerce customisation; performance and caching; security and update hygiene; WP-CLI; moving sites between environments.

Drupal belongs to `development/drupal-development`, Shopify to `ecommerce/shopify-dev`. An Italian municipal site on the Designers Italia model built with WordPress starts from the model's official WordPress theme (`italia/design-comuni-wordpress-theme`, installed with a child theme); the model's conformity criteria and accessibility obligations are not CMS-specific and are checked on designers.italia.it and with the official validator.

## Support status

Checked 2026-11-19 on wordpress.org, make.wordpress.org and woocommerce.com; re-check before quoting.

- WordPress 7.1 was released on 19 August 2026; the latest release is 7.1.5 (18 November 2026). WordPress 7.0 raised the minimum PHP to 7.4; 7.1 runs on PHP 7.4 to 8.5, with 8.4 or 8.5 recommended for new installs and 7.4 to 8.1 kept only for backward compatibility.
- WooCommerce 11.3.1 (19 November 2026) asks for WordPress 6.9 or later, PHP 8.3 or later (tested to 8.4; 7.4 is legacy), MySQL 8.0 or MariaDB 10.6 or later and a 256 MB memory limit. WooCommerce states that only its latest version is considered fully secure.
- New stores default to HPOS order storage (since 8.2) and to the Cart and Checkout blocks (since 8.3). Older stores can be on either side, so order and checkout code starts from what the store actually runs.

## Inspect first

```text
wp core version; PHP and database versions per environment; WP_ENVIRONMENT_TYPE on each
wp plugin list / wp theme list: active theme, its parent, must-use plugins
theme type: block (theme.json, templates/*.html), classic (PHP templates) or Elementor-built pages
where customisations live today: child theme, site plugin, mu-plugins, snippet plugins, builder custom code
WooCommerce: version, HPOS on or off, Checkout block or shortcode, gateways, overridden templates (WooCommerce > Status)
cache layers (host page cache, plugin, object cache, CDN) and how code reaches production (Git, SFTP, host deploy)
```

## Invariants

1. **Customisations live in code the site owns.** Core, parent themes and third-party plugins are never edited: their updates overwrite the change. Presentation goes in a child theme; behaviour that must survive a theme change goes in a site plugin or `mu-plugins`. Logic sitting in snippet plugins or builder custom-code boxes moves into versioned files when it is touched.
2. **Hooks before overrides.** Behaviour changes through actions and filters. A template (theme or WooCommerce) is copied only when no hook exists, and its version is kept in step after each update.
3. **Nothing that crosses a request boundary is trusted.** Input is sanitised and validated on the way in; output is escaped at the moment it is printed; every query with variables goes through `$wpdb->prepare()`; every state change checks `current_user_can()` and a nonce, and the nonce is never the authorization. REST routes always declare a real `permission_callback`.
4. **WooCommerce data goes through WooCommerce APIs.** Orders and products are read and written with `wc_get_order()`, `wc_get_orders()`, `wc_get_product()` and their getters, setters and `save()`. Post meta functions and `WP_Query` on orders break under HPOS.
5. **The database holds content and settings together.** There is no configuration export, so a staging database is never pushed over a live one that takes orders, comments or form entries. Code moves through Git or the deploy, content moves deliberately, and URLs change only through serialisation-safe tools.
6. **Everything registered is prefixed or namespaced**: functions, hooks, options, post types, script handles, text domain. A name clash with a plugin fails silently.
7. **Updates are routine and reversible**: backup, update on staging, test the flows that make money or collect data (checkout, forms, login), then production. An abandoned plugin, or a premium plugin whose licence no longer delivers updates, is a security finding to report.

## References

| Need | Load |
| --- | --- |
| block, classic and child themes, theme.json, custom blocks, block editor versus Elementor, Elementor widgets | `references/themes-and-builders.md` |
| plugin structure, hooks, post types, options, AJAX, REST, sanitising and escaping, quality tools, tests | `references/plugins-and-security.md` |
| WooCommerce hooks and templates, HPOS, checkout blocks, products and orders, payments, emails, accessibility law for shops | `references/woocommerce.md` |
| performance and caching, cron, WP-CLI, updates and backups, staging and production migrations | `references/operations.md` |

Load the reference the subproblem needs; a WooCommerce change that touches caching or a migration also needs `operations.md`.

## Completion bar

Confirm the subset that applies and name what was not run:

- no file changed in core, a parent theme or a third-party plugin, and the custom code is under version control;
- `php -l`, PHPCS with the WordPress standard and PHPStan pass on the changed code where the project has them;
- each new form, AJAX, REST or admin-post handler was exercised logged out and as a low-privilege role, and rejects a missing or wrong nonce;
- for WooCommerce, a full checkout in the gateway's test mode on the checkout type the store uses; custom plugins that touch orders declare HPOS compatibility;
- after a migration, the old domain is gone from the database (`wp db search`), Elementor URLs and CSS were regenerated, permalinks flushed, and media and forms work;
- every cache layer that served the old version was purged.
