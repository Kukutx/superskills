# Theming

## Base theme and sub-theme

- The site's theme is a custom sub-theme of a maintained base theme (on public-sector sites, `bootstrap_italia` with its `italiagov` starter kit; see `italian-public-sector.md`). The base theme is updated through Composer and never edited, so a fix to it is a template override in the sub-theme or a patch.
- A new theme without such a base starts from core's starterkit generator (`php core/scripts/drupal generate-theme`), which copies markup instead of inheriting it.
- Olivero and Claro leave core in Drupal 12 (see `upgrades.md`). A sub-theme of either needs the contributed project before that upgrade.

## Templates

- Find the template and its suggestions with Twig debugging: the development settings page (`/admin/config/development/settings`) or `twig.config: debug: true` in `development.services.yml`. Never on production.
- Copy the template from the base theme into the sub-theme's `templates/`, keep the suggestion naming (`node--servizio--full.html.twig`, `paragraph--accordion.html.twig`, `views-view-unformatted--notizie--block-1.html.twig`), and change only what the task needs. Diff it against the base template after base-theme updates.
- Add suggestions in `hook_theme_suggestions_HOOK_alter()` rather than branching inside one template.
- Print render arrays, not raw values: `{{ content.field_data }}` keeps the formatter, field access, attributes and cache metadata. `{{ node.field_data.value }}` skips field access and drops the field's cacheability, and when `content` is never printed the tags of referenced entities never reach the page. When a template prints fields one by one, also print `{{ content|without('field_a', 'field_b') }}` or render `content` once, so the remaining metadata still bubbles.
- Keep logic in preprocess and Twig declarative. Anything computed in preprocess adds its own cacheability, for example `CacheableMetadata::createFromObject($term)->applyTo($variables);` or a cache context such as `url.path`.

## Escaping

- Twig autoescapes. `|raw` is only for markup Drupal has already filtered (a formatted text field rendered through its text format, a render array output), never for user input or a field's `.value`.
- Strings use `{{ 'Text'|t }}` or `{% trans %}` with placeholders, so translators see whole sentences.
- Attributes are built with `attributes.addClass()` or `create_attribute()`, not by concatenating strings.

## Assets

- Libraries are defined in `*.libraries.yml` and attached where the markup appears: `{{ attach_library('mytheme/card') }}` in the template or `#attached` in the render array. Only assets every page needs go in the theme's `.info.yml`.
- JavaScript runs as `Drupal.behaviors` and uses `once()`, so it works again on markup that AJAX or BigPipe insert later.
- A front-end build (npm, Sass) lives in the custom theme. The deployed artifact never requires Node on the production server: commit the built files or build them in CI, following the project's existing pipeline.

## Components

- Single Directory Components are part of core (the separate SDC module is obsolete in Drupal 11). A component directory holds `name.component.yml` with its props and slots schema, the Twig file and its CSS and JS; it is included with `{{ include('mytheme:card', {...}, with_context = false) }}` or embedded with slots.
- On a project whose base theme already provides components (bootstrap_italia uses UI Patterns), reuse and extend those before writing parallel ones: two components for the same UI element drift apart.

## Views and Paragraphs output

- Views select data; templates own markup. Prefer a Views template override over long field rewrites in the Views UI, which hide markup inside configuration.
- Paragraph types render through `paragraph--TYPE--VIEW-MODE.html.twig`. View modes, not template conditionals, decide which fields a context shows.

## Accessibility in templates

Semantic elements and one `h1` per page, heading levels that do not skip, visible focus, labelled form controls and image alt text taken from the media entity. Templates that hide content visually use `visually-hidden`, not `display: none`, when screen readers still need it. Public-sector accessibility obligations are in `italian-public-sector.md`.
