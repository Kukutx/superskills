# Custom modules, hooks and core APIs

## Module shape

- Split custom code by feature (`comune_servizi`, `comune_prenotazioni`), not one catch-all site module: a feature can then be disabled, tested and upgraded on its own.
- `*.info.yml` declares `core_version_requirement` for the cores the site really runs; during an upgrade custom code must run on both (`^10.3 || ^11`, later `^11 || ^12`). Dependencies use `project:module` (`drupal:node`).
- Every config object a module adds has a schema in `config/schema/*.schema.yml`. Kernel and functional tests check schemas strictly, and config translation needs them.
- `config/install` is read once, when the module is installed. Changing it later does nothing on existing sites; ship the change through the site's config sync or an update hook.
- Keep `.module` thin: hooks that are still procedural delegate to services.

## Routes, controllers and forms

- Every route declares access: `_permission`, `_entity_access: 'node.update'`, `_custom_access`, or `_access: 'TRUE'` only for something genuinely public. Avoid `_role`; role names are site configuration.
- Parameters such as `{node}` are upcast to entities automatically; pair them with `_entity_access` instead of loading and checking by hand.
- Controllers return render arrays, not strings, so theming, cache metadata and BigPipe apply. JSON that may be cached is a `CacheableJsonResponse` with cache metadata added.
- Dependencies are injected through `create()` or autowiring. `\Drupal::service()` inside a class hides dependencies from tests, and PHPStan with phpstan-drupal flags it.
- Forms extend `FormBase` or `ConfigFormBase`: checks in `validateForm()`, side effects in `submitForm()`. The Form API adds a CSRF token to every form, so a hand-written HTML form posting to a controller loses that protection.

## Services, plugins and events

- Services are declared in `*.services.yml`, with autowiring or explicit arguments, behind an interface when something else may replace them.
- Plugins (blocks, field formatters and widgets, Views handlers, queue workers, conditions) use PHP attribute discovery, available since 10.2. Annotations still work, but a plugin type without an attribute class is deprecated since 11.2, attribute classes are required in 12.0 and annotation support is removed in 13 (change record 3522776). New code uses attributes.
- Block plugins implement `blockAccess()` and return their cacheability through `getCacheContexts()`, `getCacheTags()` and `getCacheMaxAge()`, merging the parent's values.
- Use the mechanism the subsystem dispatches: entity CRUD, forms and rendering expose hooks; kernel request and response, config save and import, and Migrate dispatch Symfony events handled by an `event_subscriber` service.

## Hooks

Object-oriented hooks exist since Drupal 11.1 (change record "Support for object oriented hook implementations using autowired services"):

- A class in the `Drupal\<module>\Hook` namespace (`src/Hook/`) is registered automatically as an autowired service. Methods carry `#[Hook('form_alter')]`, keep the procedural signature, can have any name, and one method may carry several attributes.
- Still procedural as of that record: `hook_install`, `hook_uninstall`, `hook_schema`, `hook_requirements`, `hook_update_N`, `hook_post_update_NAME`, `hook_update_dependencies`, `hook_update_last_removed`, `hook_removed_post_updates`, install tasks, `hook_hook_info` and `hook_module_implements_alter`. Module preprocess functions can be OOP since 11.2 and themes can implement OOP hooks since 11.3.
- Code that must also run on 10.x keeps a procedural function marked `#[LegacyHook]` that calls the service method; 11.1 and later skip the shim, so the hook does not run twice.
- Hook implementations defined conditionally, and procedural hook functions placed in `src/`, are not supported. Procedural hook support is expected to be removed no earlier than Drupal 13.
- Drupal Rector's `HookConvertRector` converts procedural hooks. Run it as a separate pass after deprecation fixes and review the diff.

## Entities

- Content entity queries call `->accessCheck(TRUE)` for anything shown to a user and `->accessCheck(FALSE)` only for system processing whose results are not exposed. Drupal 10 throws an exception when the call is missing (change record 3201242).
- Load in bulk with `loadMultiple()`. A query plus a load inside a loop over hundreds of IDs belongs in a batch or a queue.
- Read fields through the field API (`->get('field_x')->value`, `->target_id`, `->entity`, `->isEmpty()`) and respect translations (`hasTranslation()`, `getTranslation()`).
- Editorial content with its own URL, revisions and workflow is a node bundle with fields: access, Views, revisions and moderation come with it. A custom content entity is for high-volume or non-editorial records (bookings, submissions, logs) and needs its own access handler, Views data and admin routes.
- Derived values are set in `hook_ENTITY_TYPE_presave()`. Saving the same entity again inside its own presave or update hook recurses.

## Long-running work

- Work that does not fit one request goes to the Queue API (a `QueueWorker` plugin with a cron time limit) or, when a user starts it from the UI, the Batch API. Cron hooks enqueue items rather than process everything.
- Production cron runs from the system scheduler (`drush cron`), not from page requests.

## Update code

`drush deploy` runs them in this order: `hook_update_N`, then `hook_post_update_NAME`, then config import, then Drush `hook_deploy_NAME`.

| Hook | File | Use for |
| --- | --- | --- |
| `hook_update_N` | `.install` | schema and low-level changes; the full API is not guaranteed here |
| `hook_post_update_NAME` | `.post_update.php` | data fixes through the entity API that do not depend on new config |
| `hook_deploy_NAME` | `.deploy.php` | anything that needs configuration imported in the same deploy, such as filling a field whose storage arrives with the config |

- `N` encodes the major version and a sequence (`11001`). Large data sets use `$sandbox` to run in batches.
- Each runs once per site. An update that already ran on production is never edited; a correction is a new update.
- Menu links created in the UI (`menu_link_content`), taxonomy terms and custom block content are content entities, not config, so `drush config:export` does not carry them. A required menu tree or vocabulary ships with a deploy hook or a migration.

Log through a logger channel service. Debug output (`dpm()`, `var_dump()`, `kint()`) does not reach a commit.
