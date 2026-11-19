# Drupal Development maintenance sources

Maintenance-only. Do not load for normal Drupal tasks.

## Policy

- Every row is an official page that was opened and read on 2026-11-19 when the Skill was written. The Skill states only what the page said; anything a page did not confirm is written in the Skill as something to check, or left out.
- Release dates, support windows, PHP and database requirements, removed modules, theme and validator versions, and the comuni model's criteria change. On review, re-open each page and change the Skill only where the page changed. The support box in `SKILL.md` and the tables in `references/upgrades.md` and `references/italian-public-sector.md` carry the check date and must be updated with it.
- The project's own `composer.lock`, hosting and configuration are the source of truth for a given site; these pages are the source of truth for what Drupal and the Italian administration require.

## Source register

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| drupal.org, core release schedule | https://www.drupal.org/about/core/policies/core-release-cycles/schedule | 11.4 current; 12.0 and 11.5 week of 7 Dec 2026; Drupal 10 EOL 9 Dec 2026; Drupal 9 EOL 1 Nov 2023; Drupal 11 to early Dec 2028; 11.4 security to 21 Apr 2027 | 2026-11 |
| drupal.org, release process overview | https://www.drupal.org/about/core/policies/core-release-cycles/release-process-overview | minors supported about eight months; final minor twelve months; monthly patch releases | 2026-11 |
| drupal.org, PHP requirements | https://www.drupal.org/docs/getting-started/system-requirements/php-requirements | PHP support per minor; 12.0 requires PHP 8.5 with argon2 | 2026-11 |
| drupal.org, database server requirements | https://www.drupal.org/docs/getting-started/system-requirements/database-server-requirements | MySQL, MariaDB, PostgreSQL and SQLite minimums for 10, 11 and 12 | 2026-11 |
| drupal.org, deprecated and obsolete extensions | https://www.drupal.org/node/3223395 | modules and themes removed in 11 and 12; Migrate Drupal not moved to contrib; Text with Summary, Claro, Olivero, Toolbar | 2026-11 |
| drupal.org, upgrading from Drupal 9 to 10 | https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-or-later/how-to-upgrade-from-drupal-9-to-drupal-10 | 9.4 or 9.5 first; CKEditor 4 and Seven removal; upgrade steps | 2026-11 |
| drupal.org, upgrading from Drupal 10 to 11 | https://www.drupal.org/docs/upgrading-drupal/upgrading-drupal/how-to-upgrade-from-drupal-10-to-drupal-11 | 10.3 first; PHP 8.3; removed and obsolete extensions; Composer commands | 2026-11 |
| drupal.org, upgrading from Drupal 11 to 12 | https://www.drupal.org/docs/upgrading-drupal/upgrading-drupal/how-to-upgrade-from-drupal-11-to-drupal-12 | updates before 11.3.0 removed; PHP 8.5; Composer commands; post-upgrade steps | 2026-11 |
| drupal.org, Upgrade Status | https://www.drupal.org/project/upgrade_status | 5.x on ^10.4, ^11 and ^12; checks the next major only; Drush commands | 2026-11 |
| Drupal Rector | https://github.com/palantirnet/drupal-rector | install, dry run, per-version rule sets, HookConvertRector pass | 2026-11 |
| drupal.org change record, OOP hooks | https://www.drupal.org/node/3442349 | `#[Hook]` in `src/Hook` since 11.1; hooks that stay procedural; LegacyHook; procedural removal no earlier than 13 | 2026-11 |
| drupal.org change record, plugin attribute classes | https://www.drupal.org/node/3522776 | attribute class required in 12.0; annotations removed in 13 | 2026-11 |
| drupal.org change record, entity query access | https://www.drupal.org/node/3201242 | explicit `accessCheck()`; Drupal 10 throws without it | 2026-11 |
| drupal.org, CSRF access checking | https://www.drupal.org/docs/8/api/routing-system/access-checking-on-routes/csrf-access-checking | `_csrf_token: 'TRUE'` as a string; token added by `Url::fromRoute()`; forms already protected | 2026-11 |
| drupal.org, cache max-age | https://www.drupal.org/docs/drupal-apis/cache-api/cache-max-age | max-age ignored by the page cache, Varnish and CDNs for anonymous users; Cache Control Override; cron-invalidated tags | 2026-11 |
| api.drupal.org, development.services.yml (11.x) | https://api.drupal.org/api/drupal/sites%21development.services.yml/11.x | `http.response.debug_cacheability_headers: true` as a development container parameter | 2026-11 |
| drupal.org, security release timing | https://www.drupal.org/node/1173280 | contrib windows every Wednesday, core usually the third Wednesday, 16:00 to 22:00 UTC | 2026-11 |
| drupal.org, PSA-2026-05-18 | https://www.drupal.org/psa-2026-05-18 | highly critical core release; no release for Drupal 9; update to the latest patch beforehand | 2026-11 |
| drupal.org, updating modules with Composer | https://www.drupal.org/docs/updating-drupal/updating-modules-and-themes-using-composer | `composer audit` for the whole project; `drush pm:security` as the legacy equivalent | 2026-11 |
| Drush, deploy command | https://www.drush.org/13.x/deploycommand/ | `drush deploy` order including `cache:warm` on 11.2+; update, post-update and deploy hooks | 2026-11 |
| Drush, install and compatibility | https://www.drush.org/13.x/install/ | Drush 13 for 10.2+, Drush 14 for 11.3+; site-local install | 2026-11 |
| Drush, command list | https://www.drush.org/13.x/commands/all/ | `maint:set`, `config:status`, `deploy:hook`, `cache:warm`, `sql:sanitize`; no `pm:security` in 13 | 2026-11 |
| Config Split | https://www.drupal.org/project/config_split | 2.x uses core's config API; key-level splits; activation per environment in settings | 2026-11 |
| Composer Patches, defining patches | https://docs.cweagans.net/composer-patches/usage/defining-patches/ | local patch files instead of changing merge-request URLs; `patches.lock.json` | 2026-11 |
| phpstan-drupal | https://github.com/mglaman/phpstan-drupal | deprecation rules dependency; `\Drupal` call rule; PHPStan 2 from Drupal 11.2; 1.x support window | 2026-11 |
| Drupal Test Traits | https://git.drupalcode.org/project/dtt/-/raw/2.x/README.md | package name, base classes, existing-content caveats, custom code only | 2026-11 |
| php.net, supported versions | https://www.php.net/supported-versions.php | PHP 8.2 security to 31 Dec 2026; PHP 8.6 released 19 Nov 2026 | 2026-11 |
| Designers Italia, comuni model | https://designers.italia.it/modelli/comuni/ | what the model provides; CMS themes for WordPress and Drupal | 2026-11 |
| Designers Italia, adopting the comuni site model | https://designers.italia.it/modelli/comuni/adotta-il-modello-di-sito-comunale/ | adoption steps; conformity criteria; evaluation app | 2026-11 |
| design-comuni-docs, site conformity criteria | https://docs.italia.it/italia/designers-italia/design-comuni-docs/it/versione-corrente/conformita/conformita-modello-sito.html | C.SI criteria, recommendations, EU emblem rule | 2026-11 |
| design-comuni-docs, services conformity criteria | https://docs.italia.it/italia/designers-italia/design-comuni-docs/it/versione-corrente/conformita/conformita-servizi-digitali.html | C.SE criteria for digital services | 2026-11 |
| design-comuni-docs, practices for the asseverazione | https://docs.italia.it/italia/designers-italia/design-comuni-docs/it/versione-corrente/conformita/buone-pratiche-asseverazione.html | header and footer consistency, breadcrumbs, capitals, required content types and attributes | 2026-11 |
| Evaluation app, technical requirements for comuni | https://docs.italia.it/italia/designers-italia/app-valutazione-modelli-docs/it/versione-attuale/requisiti-e-modalita-verifica-comuni.html | `data-element` attributes the validator reads; href checks | 2026-11 |
| pa-website-validator-ng | https://github.com/italia/pa-website-validator-ng | current validator CLI, options and requirements | 2026-11 |
| pa-website-validator (archived) | https://github.com/italia/pa-website-validator | archived December 2024 and deprecated | 2026-11 |
| Bootstrap Italia releases | https://github.com/italia/bootstrap-italia/releases | v2.18.3 latest stable; v3.0.0 betas | 2026-11 |
| drupal.org, Bootstrap Italia theme | https://www.drupal.org/project/bootstrap_italia | 2.17.7, core compatibility, security coverage | 2026-11 |
| Bootstrap Italia Drupal theme repository | https://github.com/italia/design-drupal-theme | install steps, `italiagov` starter kit, library loading, UI Patterns | 2026-11 |
| AgID, accessibilità e usabilità | https://www.agid.gov.it/it/ambiti-intervento/accessibilita-usabilita | declaration by 23 September; objectives by 31 March; AgID supervises D.Lgs. 82/2022 | 2026-11 |
| AgID news, accessibility declaration 2026 | https://www.agid.gov.it/it/notizie/dichiarazione-di-accessibilita-pubblicazione-o-aggiornamento-entro-il-23-settembre | `form.agid.gov.it`, RTD access, footer link, art. 9 Legge 4/2004 | 2026-11 |
| AgID accessibility guidelines, technical requirements | https://docs.italia.it/AgID/documenti-in-consultazione/lg-accessibilita-docs/it/stabile/requisiti-tecnici-accessibilita-strumenti-informatici.html | WCAG 2.1 AA equals UNI EN 301549:2018 points 9.1 to 9.4 and 9.5 | 2026-11 |
| AgID accessibility guidelines, introduction | https://docs.italia.it/AgID/documenti-in-consultazione/lg-accessibilita-docs/it/stabile/introduzione.html | references update automatically with a newer EN 301 549 | 2026-11 |
| PA digitale 2026, measures | https://padigitale2026.gov.it/misure/ | measure 1.4.1 scope; no deadline stated there | 2026-11 |

## Not verified

- Which Drupal theme the comuni model recognises for criterion C.SI.1.4; the model's pages do not name it.
- Current deadlines and any extension for PNRR 1.4.1 avvisi; only third-party minutes and decrees were found.
- The exact list of everything removed in Drupal 10 beyond CKEditor 4 and Seven; the 9 to 10 page names only those.
