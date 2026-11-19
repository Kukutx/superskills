# Custom plugins and security

## Plugin shape

- The main file has the plugin header (`Plugin Name`, `Version`, `Requires at least`, `Requires PHP`, `Text Domain`), exits when `ABSPATH` is not defined, and only bootstraps: classes are namespaced and autoloaded with Composer, and hooks are registered from one place.
- Register custom post types and taxonomies on `init`. Flush rewrite rules once on activation, after registering them, never on every request.
- `uninstall.php` removes the plugin's options and tables only when the user deletes the plugin; deactivation keeps data.
- `mu-plugins` load before normal plugins, cannot be deactivated from the admin and have no activation hooks. Use them for behaviour the site must not lose when an editor deactivates something.
- Nothing runs at file load: no queries or remote calls before `plugins_loaded` or `init`.

## Storing data

| Data | Store |
| --- | --- |
| site setting | an option registered with the Settings API (`register_setting()` with a `sanitize_callback`) |
| large or rarely used option | an option that is not autoloaded; autoloaded options load on every request |
| value attached to a post or user | post or user meta, registered with `register_meta()` when REST or the editor needs it |
| many relational records (bookings, logs) | a custom table created with `dbDelta()` and versioned with a schema option |
| cache that can be rebuilt | a transient; it can vanish at any time and lives in memory when an object cache is present |

## Request handlers

- **Forms in the admin or front end** post to `admin-post.php` (`admin_post_<action>` and `admin_post_nopriv_<action>`), check `check_admin_referer()` and the capability, then `wp_safe_redirect()` and `exit`.
- **AJAX** through `wp_ajax_<action>` and `wp_ajax_nopriv_<action>` checks `check_ajax_referer()`. New endpoints prefer REST.
- **REST** routes are registered on `rest_api_init`:

```php
register_rest_route( 'myplugin/v1', '/bookings', [
    'methods'             => WP_REST_Server::CREATABLE,
    'callback'            => [ $this, 'create_booking' ],
    'permission_callback' => fn () => current_user_can( 'edit_posts' ),
    'args'                => [
        'date' => [ 'required' => true, 'validate_callback' => [ $this, 'is_valid_date' ], 'sanitize_callback' => 'sanitize_text_field' ],
    ],
] );
```

  The REST handbook requires a permission callback; without one WordPress raises a `_doing_it_wrong` notice since 5.5. `__return_true` is only for data that is genuinely public. Permission callbacks check what the user may do with `current_user_can()`, not merely that they are logged in.

## Security functions

- **Input**: `wp_unslash()` superglobals, then sanitise for the type (`sanitize_text_field()`, `sanitize_email()`, `absint()`, `sanitize_key()`, `sanitize_textarea_field()`), and validate against what the field may contain.
- **Output**: escape as late as possible, at the echo (developer handbook): `esc_html()`, `esc_attr()`, `esc_url()`, `esc_js()`, `esc_textarea()`, `wp_kses()` or `wp_kses_post()` for allowed HTML, and `esc_html__()`, `esc_attr_e()` and similar for translated strings.
- **SQL**: `$wpdb->prepare()` with placeholders for every value; `$wpdb->esc_like()` before adding LIKE wildcards.
- **Authorization**: capabilities, not role names, including meta capabilities such as `current_user_can( 'edit_post', $post_id )`. Custom capabilities are added to roles on activation.
- **Nonces** (`wp_nonce_field()`, `check_admin_referer()`, `check_ajax_referer()`, `wp_verify_nonce()`) prevent request forgery. They are tied to the user's session, last a day by default, and are never authentication or authorization.
- **Files**: uploads go through `wp_handle_upload()` with type checks (`wp_check_filetype_and_ext()`), never a bare `move_uploaded_file()`. Never `unserialize()` or `maybe_unserialize()` data a visitor controls.
- **Remote requests**: `wp_remote_get()` and `wp_remote_post()` with explicit timeouts; `wp_safe_remote_get()` when the URL comes from a user.
- **Translations**: literal text domains in `__()` and `_e()`; `wp_set_script_translations()` for JavaScript.

## Quality tools and tests

- WordPress Coding Standards 3 through Composer (`composer require --dev wp-coding-standards/wpcs:"^3.0"`, after allowing the `dealerdirect/phpcodesniffer-composer-installer` plugin), with the `WordPress` ruleset or `WordPress-Extra`, plus PHPCompatibilityWP with `testVersion` set to the plugin's `Requires PHP`.
- PHPStan with WordPress stubs, and the Plugin Check plugin for code meant for the wordpress.org directory.
- PHPUnit through `wp scaffold plugin-tests` (the WordPress test suite) or a `wp-env` environment; browser tests (Playwright) for checkout and forms, the flows a unit test cannot prove.
