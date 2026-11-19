# Upgrades and platform requirements

Dates and versions below were read on drupal.org and drush.org on 2026-11-19. They move every release; re-check the linked pages before giving a client a date.

## Support

| Major | Released | End of life |
| --- | --- | --- |
| 9 | — | 1 November 2023 |
| 10 | 15 December 2022 | 9 December 2026; 10.6 is the last minor |
| 11 | 2 August 2024 | early December 2028 |
| 12 | scheduled for the week of 7 December 2026 (RC1 week of 9 November) | early December 2030 |

- Drupal 11.4 is current (released week of 29 June 2026) with security support until 21 April 2027. Drupal 11.5 ships with 12.0. Security support for 11.3 and 10.6 ends that same week.
- Each minor is supported for about eight months; the final minor of a major gets twelve months of security fixes (release process overview).

## PHP and databases

| Core | PHP | MySQL | MariaDB | PostgreSQL | SQLite |
| --- | --- | --- | --- | --- | --- |
| 10.4 to 10.6 | 8.1 to 8.4 | 5.7.8+ | 10.3.7+ | 12+ | 3.26+ |
| 11.1 and 11.2 | 8.3, 8.4 | 8.0+ | 10.6+ | 16+ | 3.45+ |
| 11.3 and 11.4 | 8.3 to 8.5 | 8.0+ | 10.6+ | 16+ | 3.45+ |
| 12.0 | 8.5 only, compiled with argon2 | 8.0+ | 10.11+ | 18+ | 3.45+ |

No Drupal version supports PHP 8.6 yet, although PHP released it on 19 November 2026. PHP 8.2 security support ends on 31 December 2026 (php.net). Hosting is often what blocks an upgrade, so check the server's PHP and database versions before estimating.

## Path

- One major at a time, from the latest minor of the current one. Upgrade Status checks only the next major, and update hooks for old minors are removed: 9.4 or 9.5 before 10; 10.3 or later before 11; 11.3 or later before 12, because Drupal 12 removes all core updates older than 11.3.0.
- A Drupal 9 site goes 9.5, then 10.6, then the newest Drupal 11 minor, with database updates and a config export after each step. With Drupal 10 ending on 9 December 2026, 10 is a stepping stone, not a destination.
- A Drupal 7 site is migrated, not upgraded, and onto Drupal 11, because Drupal 12 removes the Drupal 7 migration sources (see `content-and-migrate.md`).
- Target: as of this check, the newest Drupal 11 minor, unless every contrib project the site uses already has a Drupal 12 release and the host offers PHP 8.5. Drupal 11 is supported until December 2028, so 12.0 is not urgent on its release day.

## Removed modules and themes

Before the core upgrade, either stop using each removed extension or `composer require` its contributed project while still on the old major; Drupal then uses the contributed copy automatically (deprecated and obsolete extensions page, checked 2026-11).

- **Removed in 10**: among others the CKEditor 4 module and the Seven theme. Switch editors to CKEditor 5 on Drupal 9, before the upgrade, rather than carrying CKEditor 4 forward as a contributed module.
- **Removed in 11**: Actions UI, Activity Tracker, Book, Forum, Statistics, Tour. Single Directory Components and Help Topics became obsolete because core absorbed them. Custom Statistics rules in `.htaccess` should be removed.
- **Removed in 12**: Ban, Contact, Field Layout, History, Search, Settings Tray, Shortcut, Telephone, Text with Summary, Toolbar, and the Claro and Olivero themes (12 adds a new default admin theme). Migrate Drupal and Migrate Drupal UI are removed with no contributed replacement.
- Text with Summary is the field type of the default `body` field on most sites, and Contact and Search are common on municipal sites: check `drush pm:list --status=enabled` and the field storage list before assuming a site is unaffected.

## Steps for each major

1. **Prepare**: confirm the host meets the target's requirements; update to the latest minor of the current major; note customised scaffold files; resolve every removed extension.
2. **Contrib**: on a development copy, install Upgrade Status (5.x runs on `^10.4 || ^11 || ^12`; run it on 10 for 11 and on 11 for 12), run `drush upgrade-status:analyze` (alias `us-a`) on the projects to check, and update each contrib project to a release that supports both majors.
3. **Custom code**: `composer require --dev palantirnet/drupal-rector`, copy its `rector.php`, run `vendor/bin/rector process web/modules/custom --dry-run`, review, apply, then fix what remains by hand and widen `core_version_requirement`.
4. **Core** (official upgrade guides): `composer require 'drupal/core-recommended:^N' 'drupal/core-composer-scaffold:^N' 'drupal/core-project-message:^N' --no-update`; `composer remove drupal/core --no-update` if it is required directly; update `drush/drush` and `drupal/core-dev` the same way; `composer update --dry-run`, then `composer update`. When the solver blocks, `composer update "drupal/core-*" drush/drush --with-all-dependencies`.
5. **Database and config**: `drush updatedb`, then `drush config:export`, because core updates change configuration, and commit it.
6. **Verify**: PHPCS, tests, a manual pass over editing, forms, search and listings, cron; then deploy as in `config-and-deploy.md`. Uninstall and remove Upgrade Status afterwards.

## Reporting

Give the client the end-of-life date, what stops (security releases), what the upgrade involves for their modules and hosting, and which removed extensions affect them. For an end-of-life site, the exposure is current, not hypothetical: the highly critical core advisory of May 2026 shipped no release for Drupal 9.
