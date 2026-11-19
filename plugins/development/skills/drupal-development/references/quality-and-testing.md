# Quality gates and tests

## Static checks

- **PHPCS** with `drupal/coder` (installed by `drupal/core-dev`), standards `Drupal` and `DrupalPractice`, over custom code only, with Drupal's file extensions (`php,module,inc,install,test,profile,theme,info,yml`). A `phpcs.xml.dist` in the repository fixes paths and standards so CI and editors agree.
- **PHPStan** with `mglaman/phpstan-drupal`, which pulls in `phpstan/phpstan-deprecation-rules`; with `phpstan/extension-installer` its configuration loads automatically. It flags `\Drupal` static calls inside classes and checks plugin attributes and form alters on the core versions that support them. Drupal 11.2 moved to PHPStan 2; the 1.x line of phpstan-drupal is supported until Drupal 10 loses security support (project README, checked 2026-11).
- Start at the level the code passes and raise it over time. A baseline file records existing debt only; new code never goes into it.
- Deprecation findings are upgrade work. Upgrade Status and Drupal Rector are covered in `upgrades.md`.

## PHPUnit test types

| Base class | Boots | Use for |
| --- | --- | --- |
| `UnitTestCase` | nothing | pure logic with mocked services |
| `KernelTestBase` | the listed modules, a database, no HTTP | services, entities, access, config, queue workers; the default for custom module logic |
| `BrowserTestBase` | a full install, HTTP through Mink without JavaScript | routes, forms, permissions, rendered output; set `$defaultTheme` |
| `WebDriverTestBase` | a full install with a real browser | JavaScript and AJAX behaviour only; slowest |

- Kernel tests install only what they list (`$modules`, `installEntitySchema()`, `installConfig()`), so missing dependencies show up as test failures instead of passing by accident on a full site.
- Run with the core configuration and environment variables: `vendor/bin/phpunit -c web/core web/modules/custom/<module>` with `SIMPLETEST_DB`, `SIMPLETEST_BASE_URL` and `BROWSERTEST_OUTPUT_DIRECTORY` set.

## Existing-site tests

Drupal Test Traits (`composer require --dev weitzman/drupal-test-traits`) run against an installed copy of the real site, with its configuration, theme and content:

- `ExistingSiteBase` for HTTP-level checks without JavaScript (`tests/src/ExistingSite`); `ExistingSiteSelenium2DriverTestBase` for JavaScript (`tests/src/ExistingSiteJavascript`), which needs `behat/mink-selenium2-driver`.
- The database already holds content: never assert a total count or the absence of something. Create your own entities with random names; the creation traits delete them at the end of each test.
- Limit them to the site's custom behaviour, never core or contrib, and never point them at production.

Use kernel tests for module logic and existing-site tests for "does this site's configuration plus custom code still work", such as a smoke suite on staging after `drush deploy`.

## CI

A pipeline for a site repository runs, in order of cost: `composer validate` and `composer audit`; PHPCS and PHPStan on custom code; unit and kernel tests; then, on a sanitised copy of production (`drush sql:sanitize`), `drush deploy` followed by existing-site tests. The deploy step catches config import errors and failing update hooks before production does.
