# Themes and page builders

## Choosing the build

| Build | Where layout and styles live | Fits when |
| --- | --- | --- |
| Block theme | `theme.json`, `templates/*.html`, `parts/*.html`, `patterns/`, and Site Editor changes in the database | structured content, editors working in the block editor, performance and long-term maintainability matter |
| Classic theme | PHP templates, `functions.php`, the Customizer | an existing classic site, or PHP-driven templates that blocks do not fit |
| Elementor | page JSON in the `_elementor_data` post meta, a global kit (colours, fonts), Theme Builder templates in Elementor Pro | the client or editors need visual control of layouts and the site already runs it |

Decide with these trade-offs stated: page weight and DOM size, per-site licence costs for Pro, the lock-in of content stored as builder JSON (changing builder means rebuilding pages), and what editors can safely change. Do not let two systems own the same area, such as an Elementor Theme Builder header and a block theme header part.

## Block themes

- `theme.json` schema version 3 works with WordPress 6.6 and later (block editor handbook, checked 2026-11); the schema lives at `https://schemas.wp.org/trunk/theme.json`, or the versioned `https://schemas.wp.org/wp/<version>/theme.json`. It owns the palette, typography, spacing and layout widths, so design tokens are set there, not repeated in CSS.
- Templates and parts edited in the Site Editor are saved in the database and take precedence over the theme's files. A code change to a template that someone customised in the editor does not appear until that customisation is reset, so check for one before debugging "my change does nothing".
- Patterns in `patterns/*.php` with header comments, and style variations in `styles/`, give editors choices without free-form CSS.

## Child themes

- Classic: `style.css` with `Template: <parent-folder>`. Enqueue the parent stylesheet only when the parent does not already do it. `get_stylesheet_directory()` points to the child, `get_template_directory()` to the parent.
- Block: the child's `theme.json` merges over the parent's, and a child template replaces the parent template of the same name.
- The common Elementor setup is the Hello Elementor theme with a child theme for code and global CSS.

## Assets

- Enqueue with `wp_enqueue_style()` and `wp_enqueue_script()` on `wp_enqueue_scripts`, conditionally where the asset is used, and with a version from the file's modification time or a build hash so caches refresh.
- Data reaches JavaScript through `wp_add_inline_script()` or `wp_localize_script()`. Calls to the site's REST API with cookie authentication send the `wp_rest` nonce in `X-WP-Nonce`.

## Custom blocks

- Each block has a `block.json` and is registered with `register_block_type()` on that folder; `@wordpress/scripts` builds it.
- A block whose output depends on data that changes renders on the server (`render` in `block.json`). A static block saves HTML into the post: changing its `save()` output turns existing posts into "unexpected or invalid content" unless the old version is kept as a deprecation, so plan markup before content exists.

## Elementor

- Custom widgets live in a plugin: a class extending `\Elementor\Widget_Base` (name, title, icon, categories, controls, `render()`), registered on the `elementor/widgets/register` action with `$widgets_manager->register( new My_Widget() )`. Elementor 3.5 replaced the old `elementor/widgets/widgets_registered` hook and `register_widget_type()` (developer documentation, checked 2026-11).
- `render()` escapes like any template. Scripts and styles are registered separately and declared through the widget's dependency methods; the widget does not enqueue them itself.
- Global colours and fonts belong to the kit (Site Settings), global CSS to the child theme. Per-widget custom CSS spreads styles across post meta where nobody finds them again.
- Elementor writes generated CSS per post under `uploads/elementor/`. After a URL change or migration, run Elementor's replace-URL tool and regenerate its CSS (see `operations.md`).
- Builder output is not accessible by default: check heading order, link and button text, form labels and contrast on each template.
