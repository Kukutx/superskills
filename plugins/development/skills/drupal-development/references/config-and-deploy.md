# Composer, configuration and deployment

## Composer

- Layout follows `drupal/recommended-project`: docroot in `web/`, `vendor/` and `config/` outside it. Core comes from `drupal/core-recommended`, which pins core's own dependencies to tested versions, plus `drupal/core-composer-scaffold` and `drupal/core-project-message`; `drupal/core-dev` goes in `require-dev`.
- Production runs `composer install --no-dev` from the committed lock file. `composer update` runs in development, and its lock diff is reviewed like code.
- Recent Composer releases refuse to resolve packages affected by a security advisory ("not loaded, because they are affected by security advisories"). Do not set `audit.block-insecure` to false to get past an update: update the affected package, or list that one advisory under `audit.ignore` with the reason.
- Drush is a project dependency (`composer require drush/drush`), run as `vendor/bin/drush`. Drush 13 supports Drupal 10.2 and later, Drush 14 supports 11.3 and later (drush.org, checked 2026-11).

### Patches

- `cweagans/composer-patches`, defined in `extra.patches` or `patches.json`. Download the issue's merge-request diff into `patches/` and reference the local file: the content behind a merge-request URL changes whenever someone pushes to it (plugin documentation).
- Version 2 of the plugin writes `patches.lock.json`; commit it and update it whenever patch definitions change.
- Each patch description carries the issue URL. On every update, check whether the fix has been released and drop the patch when it has; a patch that no longer applies fails the install, which is the intended signal.

### Scaffold files

Core updates rewrite scaffold files such as `.htaccess`, `robots.txt` and `default.settings.php`. Customise them through `extra.drupal-scaffold.file-mapping` (append, prepend or exclude) instead of editing the copied file, and list the customisations; the official upgrade guides warn that every core file, `.htaccess` included, changes on a major upgrade.

## Configuration management

- `$settings['config_sync_directory']` points outside the docroot (for example `../config/sync`).
- Before changing configuration, bring the local site in line with the branch (`drush deploy` or `updatedb` plus `config:import`). Then change, `drush config:export`, review the diff and commit config and code together. Exporting from an out-of-date database reverts colleagues' work.
- Every environment is a copy of one site: `system.site` UUIDs must match or the import is refused. A new environment is installed from configuration with `drush site:install --existing-config`.
- **Config Split** (2.x) holds per-environment sets: development modules (devel, stage_file_proxy), verbose logging, test API endpoints. A split is activated per environment in that environment's settings file, for example `$config['config_split.config_split.dev']['status'] = TRUE;`. Version 2 uses core's config API and no longer needs Config Filter, and can split individual keys through config patches (project page, checked 2026-11).
- **Config Ignore** excludes items that editors legitimately own on production. Ignored items are also not deployed from code, so decide per item who owns it. Webforms are the usual case on municipal sites: editors build them on production while developers ship them as config. Settle which side owns each one before the first deploy rather than after a lost form.
- Secrets, API keys and per-host values are read in `settings.php` from environment variables or a secrets store, never set in configuration.
- `settings.php` is committed and includes an uncommitted `settings.local.php` per environment. Production also sets `trusted_host_patterns`, a private file path outside the docroot, and a `hash_salt` that does not live in Git.

## Deploy

`drush deploy` runs `updatedb`, `config:import`, `cache:rebuild`, `deploy:hook` and, on Drupal 11.2 and later, `cache:warm` (drush.org 13.x deploy command). A deploy for one environment is therefore:

1. back up the database (and files when the release touches them);
2. put new code in place with `composer install --no-dev`;
3. enable maintenance mode (`drush maint:set 1`) when update hooks rewrite data that users are writing at the same time;
4. `drush deploy`;
5. leave maintenance mode, then smoke-test the pages and forms the release touched;
6. `drush config:status` lists no differences. A difference means someone changed config on that environment or the import did not finish, and the next import will overwrite it.

Rolling back code does not roll back the database: update hooks and imported config have already run. The rollback is the backup from step 1 plus the previous release.

The configuration imported is always the one exported from the code being deployed. Never import a config directory exported from another branch.
