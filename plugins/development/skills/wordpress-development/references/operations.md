# Performance, operations and migrations

## Performance and caching

- **Layers**: a page cache (host or plugin) for anonymous visitors; a persistent object cache (Redis or Memcached) for logged-in users, the admin and WooCommerce; a CDN for static files. Run one page cache, not a host cache and a plugin cache competing.
- **Autoloaded options** load on every request. Find the large ones in `wp_options` and set rarely used options to not autoload before adding more caching.
- **Profiling**: Query Monitor on staging for slow queries, duplicate queries and slow hooks; fix the cause rather than caching around it.
- **Nonces in cached pages**: a nonce is valid for about a day by default. An anonymous page cached longer serves expired nonces and its forms fail; keep such pages' cache lifetime under that, or fetch the nonce with a request that is not cached.
- **Images**: register only the sizes the theme uses; after adding a size, regenerate with `wp media regenerate`.
- **Cron**: WP-Cron runs on page views. In production set `DISABLE_WP_CRON` to true and run `wp cron event run --due-now` from the system scheduler every few minutes; WooCommerce's Action Scheduler depends on it.

## Security and update hygiene

- Production sets `DISALLOW_FILE_EDIT`, keeps few administrators with strong passwords and two-factor login, and uses a database user with only the privileges WordPress needs.
- Remove plugins and themes that are not used: deactivated code is still on the server and still reachable.
- Core minor (security) releases update automatically by default. Decide plugin and theme auto-updates per site and write the decision down; a store's critical plugins update on staging first.
- `wp core verify-checksums` and `wp plugin verify-checksums --all` detect modified files of core and wordpress.org plugins after a suspected compromise.
- Follow a vulnerability feed for the installed plugins, and report abandoned plugins or premium plugins without working update licences.
- Backups cover the database and `uploads`, are stored off the server, and a restore has been tested.

## WP-CLI

Commands used most: `wp core update`, `wp plugin update --all --dry-run`, `wp db export` and `wp db import`, `wp search-replace`, `wp db search`, `wp cache flush`, `wp rewrite flush`, `wp cron event list`, `wp maintenance-mode activate`, `wp option get` and `wp option update`. Run them as the web server's user, with `--path` and `--url` on multisite or non-standard layouts.

## Environments

- `wp_get_environment_type()` returns `local`, `development`, `staging` or `production`; it defaults to production when `WP_ENVIRONMENT_TYPE` is not set (function reference, since 5.5). Debug output, payment test mode, outgoing email and search-engine visibility follow it.
- Staging never emails real customers and never charges cards: switch gateways to test mode and route mail to a catcher. Staging is password-protected and set to discourage indexing.

## Moving a site or changing its URL

1. On the source: `wp db export`; copy `wp-content/uploads`; code comes from Git or the deploy, not from the old server's files.
2. On the target: `wp db import`, then preview the change:

   ```bash
   wp search-replace 'https://staging.example.it' 'https://www.example.it' --all-tables-with-prefix --skip-columns=guid --dry-run
   ```

   Read the report, then run it without `--dry-run`. WP-CLI unserialises and reserialises PHP data, so serialised options and widgets keep valid string lengths; `--precise` forces PHP handling for every column. On multisite add `--network`, and select the site with `--url`.
3. Elementor stores page data as JSON with escaped slashes (`https:\/\/old`), which a plain search-replace misses. Run `wp elementor replace-urls <old> <new>`, or Elementor > Tools > Replace URL, then regenerate Elementor's CSS and data from Elementor > Tools.
4. `wp rewrite flush`, `wp cache flush`, purge the host cache and CDN.
5. `wp db search '<old domain>'` finds what is left; check menus, forms, media and checkout by hand.

Never run `sed` or SQL `REPLACE()` over a dump or table that holds serialised data: when the length of a string changes, PHP can no longer unserialise the value and the option or widget silently resets to its default.

## Going live over an existing production site

The production database contains orders, form entries, comments and users created since staging was copied. Do not overwrite it with the staging database. Deploy the code; recreate or import only the content that changed (export and import, a migration plugin's selective push, or rebuilding the pages on production); and schedule store changes when orders can be paused. When a full database replacement is unavoidable, put the store in maintenance mode first and reconcile the orders taken since the copy.
