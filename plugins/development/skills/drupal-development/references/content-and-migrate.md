# Content model, Views and Migrate

## Choosing the structure

| Content | Structure |
| --- | --- |
| has its own URL, revisions, author or workflow, and is listed elsewhere (servizio, ufficio, notizia, evento, luogo, documento, persona) | node bundle with fields |
| classifies items across bundles (topics, life events, audiences) | taxonomy vocabulary |
| file, image, video or remote media reused on several pages | Media entity, referenced from fields |
| ordered sections inside one page (accordion, gallery, callout, attachment list) | Paragraphs |
| an item linked from many pages | its own node, referenced, not a Paragraph copied into each page |

- Paragraphs belong to one host through Entity Reference Revisions: they are not shared, they are deleted with the host, and each nesting level multiplies revisions and storage. Keep nesting shallow, and do not use a Paragraph for something that needs its own URL or must be queried on its own.
- Layout Builder suits per-page layouts that editors compose. Where a design model fixes the page structure, as the Designers Italia comuni model does, fixed fields and Paragraphs keep pages conformant; free layout lets editors break the structure the validator checks.
- Reuse field storage across bundles only when the meaning is identical. Machine names are permanent: renaming a field means a migration, so decide them before content exists.
- Required fields and their order are part of the model. When a design standard requires sections in a given order, enforce it in the form display and the template, not in editorial guidelines.

## Views

- Views are configuration: built in development and exported.
- Never enable "Disable SQL rewriting" on a view users see: it bypasses node access and unpublished-content checks. Set access per display.
- Keep the default tag-based caching. Time-based caching is for expensive views where the delay is acceptable; "None" is for debugging.
- Use a pager, not "display all items", on anything that grows, and watch relationships that multiply rows before reaching for "Distinct".
- Complex filtering belongs in a Views filter, argument or field plugin; `hook_views_query_alter()` is brittle across updates.
- Faceted or full-text search uses Search API with a database or Solr backend. The core Search module is deprecated in 11.5 and removed from core in 12.0.

## Migrate

Every bulk import, whether from Drupal 7, another CMS, CSV, JSON or XML exports, or an external registry, is a migration in a custom module rather than a one-off SQL or PHP script, because migrations can be re-run, updated, rolled back and audited.

- Migrations are YAML (core migration plugins or `migrate_plus` config entities) with `migration_dependencies` setting the order: files, then media, then terms and users, then content that references them. `migration_lookup` resolves references, with stubs for forward references.
- Sources come from `migrate_source_csv`, the `migrate_plus` URL source with JSON or XML parsers, or a custom source plugin. Transformations happen in process plugins, not in SQL after the import.
- The ID map lets a re-run update instead of duplicate: `drush migrate:import <id> --update`, `migrate:rollback`, `migrate:status`, `migrate:messages`, and `migrate:reset-status` for a migration stuck in "Importing".
- Validate on a copy: compare source and destination counts, open a sample from every bundle and language, check files and links, and read the messages.
- Drupal 7 sources live in Migrate Drupal, which Drupal 12 removes without moving it to a contributed project; Drupal 12 keeps the migration API and destinations but not the Drupal 6 and 7 sources (deprecated extensions page, checked 2026-11). Drupal 7 sites are migrated onto Drupal 11 first and upgraded to 12 afterwards.
- A migration that will run again after launch (a nightly registry import) keeps `--update` semantics and never overwrites fields that editors own on the destination. Split editor-owned fields from imported ones in the model.
