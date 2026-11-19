---
name: drupal-development
description: Drupal 10/11 modules, hooks, config, Composer, Twig, Views, Migrate, caching, security, tests and 9-to-12 upgrades, plus Italian PA sites on Bootstrap Italia. Use for Drupal work, not WordPress.
---

# Drupal Development

## Scope

Owns code and site work on Drupal 9 to 12: custom modules and themes, Composer, configuration and deployment, content modelling with Views, Paragraphs and Migrate, caching, security, quality gates and tests, major-version upgrades, and Italian public-sector sites built on Bootstrap Italia and the Designers Italia municipal model.

WordPress and WooCommerce belong to `development/wordpress-development`.

## Support status

Checked 2026-11-19 against the drupal.org release schedule; re-check before quoting dates to anyone.

- Drupal 11.4 is the current release. Drupal 12.0 and 11.5 are scheduled for the week of 7 December 2026.
- Drupal 10 reaches end of life on 9 December 2026. Drupal 9 ended on 1 November 2023 and receives no releases, even for highly critical core advisories. Drupal 11 is supported until early December 2028.
- A site on Drupal 9 or 10 therefore has an upgrade problem before anything else; say so when it changes the advice. New custom code targets Drupal 11 and stays free of deprecations, so moving to 12 is a constraint change rather than a rewrite.

## Inspect first

These decide the answer, and the repository and running site reveal them:

```text
drupal/core-recommended version in composer.lock; PHP version on every environment
composer.json: patches, extra repositories, scaffold overrides, drupal/core-dev
config sync directory, Config Split sets and which are active per environment (settings*.php)
custom code under modules/custom and themes/custom; the base theme of the active theme
contrib projects in use and whether each has a release for the target core
how deploys run (pipeline, drush deploy or hand-run commands); existing tests, phpstan.neon, phpcs.xml
```

## Invariants

1. **Composer owns the code.** Modules are added, updated and removed with Composer and `composer.lock` is committed. Core and contrib are never edited in place: a fix ships as a patch file applied by `cweagans/composer-patches`, with the drupal.org issue in its description, so the next update cannot silently drop it.
2. **Configuration is code, content is data.** Content types, fields, views, block placement, roles and permissions change in development, are exported with `drush config:export`, reviewed as a diff and committed; deploys import them. Configuration edited on production is overwritten by the next import unless it is deliberately excluded, so when someone edits config on production, say so before it is lost. Environment differences go into Config Split or `settings.php`; secrets come from the environment, never from exported config, which lives in Git.
3. **Every render array carries its cacheability.** Tags name the data it shows, contexts what it varies by, max-age when it expires. A missing context serves one user's or one page's output to everyone. `max-age: 0` hides that bug, costs performance and is ignored by the anonymous page cache.
4. **Access is declared and output is escaped.** Every route has an access requirement; content entity queries call `accessCheck()` explicitly; user text reaches the browser through Twig autoescaping, render arrays or `t()` placeholders; a link that changes state carries a CSRF token.
5. **Write against the target core's current API.** Services are injected in classes (`\Drupal::` only in procedural code); plugins use PHP attributes; hooks live in `src/Hook` classes on 11.1 and later. Every deprecation added now is upgrade work later.
6. **Data changes ship as update code.** Schema and data changes are `hook_update_N`, `hook_post_update_NAME` or Drush `hook_deploy_NAME`, chosen by whether they run before or after config import; a manual SQL step on production is not a deploy.

## References

| Need | Load |
| --- | --- |
| module skeleton, routes, controllers, forms, services, plugins, hooks, events, entities, queues, update hooks | `references/modules-and-hooks.md` |
| Composer, patches, config export and import, Config Split and Ignore, settings per environment, `drush deploy` | `references/config-and-deploy.md` |
| Twig templates, preprocess, suggestions, libraries, components, base and sub-themes | `references/theming.md` |
| content types versus Paragraphs and Media, Views, Search API, Migrate and Drupal 7 imports | `references/content-and-migrate.md` |
| cache tags, contexts and max-age, lazy builders, BigPipe, page cache and reverse proxies | `references/caching.md` |
| access, sanitising, SQL, CSRF, files, security advisories and update policy | `references/security.md` |
| PHPCS, PHPStan, PHPUnit test types, Drupal Test Traits, CI | `references/quality-and-testing.md` |
| 9 to 10 to 11 to 12 upgrades, PHP and database requirements, removed modules, Upgrade Status, Rector | `references/upgrades.md` |
| Italian municipal and PA sites: Bootstrap Italia, the comuni model and its criteria, the validator, AgID accessibility, PNRR 1.4.1 | `references/italian-public-sector.md` |

Load the reference the subproblem needs. Code that renders output usually needs `caching.md` as well.

## Completion bar

Confirm the subset that applies and name what was not run:

- `composer validate` passes, `composer.lock` is committed, nothing under core or contrib was edited;
- the exported config diff contains only the intended changes;
- `drush deploy` on a copy of the production database runs without errors and `drush config:status` is clean afterwards;
- PHPCS (Drupal, DrupalPractice) and PHPStan are clean on the changed code, and tests exist at the level of the claim;
- changed output was viewed as anonymous, as two different users (cache leaks) and as a role without the permission (access);
- on a public-sector site, the validator and accessibility checks in `references/italian-public-sector.md` were run on the changed pages.
