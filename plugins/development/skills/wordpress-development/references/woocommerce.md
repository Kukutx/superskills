# WooCommerce

## Customising without editing WooCommerce

- First choice: actions and filters (`woocommerce_*`) in a site plugin. WooCommerce's own documentation prefers hooks because templates stay untouched and survive updates.
- Classic themes: override a template by copying it to `<child-theme>/woocommerce/`, keeping the path without `templates/` (`plugins/woocommerce/templates/emails/admin-new-order.php` becomes `<child-theme>/woocommerce/emails/admin-new-order.php`). WooCommerce > Status lists overrides that fall behind the core version; review them after every WooCommerce update.
- Block themes use block templates for the shop, product, cart and checkout pages, edited in the Site Editor. PHP template overrides do not apply to them.

## Orders and HPOS

High-Performance Order Storage keeps orders in WooCommerce's own tables and is on by default for stores created since 8.2. Code that must work on any store:

- reads and writes orders only through the order object: `$order = wc_get_order( $id ); $order->get_meta( 'key' ); $order->update_meta_data( 'key', $value ); $order->save();`;
- queries with `wc_get_orders()` or `WC_Order_Query`, never `WP_Query`, `get_posts()` with `shop_order`, `get_post_meta()` on an order ID, or SQL against `wp_posts`;
- declares compatibility in the plugin's main file, because an undeclared plugin blocks enabling HPOS:

```php
add_action( 'before_woocommerce_init', function () {
    if ( class_exists( \Automattic\WooCommerce\Utilities\FeaturesUtil::class ) ) {
        \Automattic\WooCommerce\Utilities\FeaturesUtil::declare_compatibility( 'custom_order_tables', __FILE__, true );
    }
} );
```

- branches on storage only where unavoidable, with `OrderUtil::custom_orders_table_usage_is_enabled()`; order-screen meta boxes use the screen ID from `wc_get_page_screen_id( 'shop-order' )` under HPOS.
- Compatibility mode syncs both storages while a store migrates (`wp wc cot sync` forces a sync). Turning HPOS off is not a fix for a plugin that reads order post meta; the plugin is fixed.

Products follow the same rule: `wc_get_product()`, setters and `save()`, so lookup tables, caches and hooks stay consistent.

## Checkout

- Find out which checkout the store uses before writing code: the Checkout page contains either the Checkout block (the default for stores created since 8.3) or the `[woocommerce_checkout]` shortcode.
- Classic checkout hooks do not carry over to the block. Fields added through `woocommerce_checkout_fields` do not appear there, editing core fields is not supported, and `woocommerce_form_field` is not supported (WooCommerce hook alternatives table, checked 2026-11). A new field on the block checkout is registered with the Additional Checkout Fields API: `woocommerce_register_additional_checkout_field()` on `woocommerce_init` or later, with the `contact`, `address` or `order` location; the documented types were select, text, checkbox and date.
- Other block integrations use the Store API extension points and the checkout's extensibility slots. Moving a store back to the shortcode checkout to keep a legacy plugin working is a real option with a cost (it leaves the maintained default path); state it rather than choose it silently.

## Payments, emails and money

- Use maintained gateway extensions; build a custom gateway only when none exists. Test in the gateway's sandbox on staging, with its own webhook endpoint, never with real cards on production.
- Email changes use the `woocommerce_email_*` hooks or overrides under `woocommerce/emails/`. Transactional mail goes through an SMTP or API provider, not PHP `mail()`.
- Prices and taxes come from WooCommerce's tax settings, never hard-coded rates. Italian stores usually need tax codes and electronic invoicing data (codice fiscale, partita IVA, SDI code or PEC). That requirement was not verified for this Skill: confirm it with the client's accountant and use a maintained invoicing integration.

## Caching and background work

- Cart, checkout and my-account pages, and requests carrying WooCommerce session cookies (`woocommerce_items_in_cart`, `wp_woocommerce_session_*`), bypass the page cache in every layer.
- Scheduled work runs through Action Scheduler (WooCommerce > Status > Scheduled Actions). A growing backlog of pending or failed actions points to broken cron or a failing extension.

## Accessibility law for shops

Online shops are within the European Accessibility Act, which applies to services placed on the market after 28 June 2025; service businesses with fewer than 10 employees and under EUR 2 million turnover are exempt (Your Europe, checked 2026-11). Italy transposed it with D.Lgs. 82/2022, and AgID supervises private digital services under it (AgID accessibility page, checked 2026-11). For an in-scope client, an inaccessible theme or checkout is a legal problem, not only a usability one: say so when it applies.

## Updates

Update WooCommerce and its extensions together on staging, read the release's developer advisories, review overridden templates, and place a test order in the gateway's test mode before production.
