# Security

## Access

- Routes declare access in `*.routing.yml` (`_permission`, `_entity_access`, `_custom_access`). A controller that checks access inside its body still exposes the route to anyone the requirement lets through.
- Entity access goes through `$entity->access('view', $account, TRUE)`, which returns an `AccessResult` with cacheability; pass it on instead of collapsing it to a boolean.
- Content entity queries call `accessCheck()` explicitly (Drupal 10 throws otherwise). Views respect node access through the query tag, so "Disable SQL rewriting" stays off on anything users see.
- Fine-grained node visibility (per office, per section) uses node grants or a maintained access module, not checks scattered through templates, because grants also apply to listings, search and Views.
- Dangerous custom permissions set `restrict access: true` in `*.permissions.yml`. Grant permissions to roles, never check role names in code.

## Output and input

- Twig and render arrays escape by default. Plain text goes in `#plain_text`; `#markup` is filtered for admin-level HTML, which is not a licence to concatenate user input into it.
- `t()` placeholders: `@name` escapes, `%name` escapes and emphasises, `:url` is for URLs and filters dangerous protocols. Never build a translatable string by concatenation.
- User HTML is stored raw and rendered through a text format. Formats for untrusted roles allow a restricted tag list, and "Full HTML" goes only to roles that need it.
- Database: query builders (`select()`, `->condition()`) or placeholders in `query()`; `escapeLike()` for LIKE patterns; never interpolate a variable into SQL.
- Redirects to a URL taken from the request use `LocalRedirectResponse`, or validate the host before a `TrustedRedirectResponse`.

## CSRF

- The Form API adds a token to every form.
- A route that changes state without a form (approve, delete, toggle links) adds the requirement `_csrf_token: 'TRUE'`. The value is a string, not a boolean; URLs generated with `Url::fromRoute()` then carry and validate the token (routing documentation, checked 2026-11). A confirmation form is the alternative.
- REST or JSON:API writes with cookie authentication send the `X-CSRF-Token` header from `/session/token`.

## Files

- File fields allow a narrow extension list. Documents that are not meant to be public use the private file system (`private://`, path outside the docroot), so field and entity access apply to downloads.
- SVG uploads can carry scripts: allow them only with sanitising, or from trusted roles.

## Site hardening

- Production sets `trusted_host_patterns`, keeps `update_free_access` false, and has no development modules enabled (devel, webprofiler, kint); Config Split keeps them on development only.
- Secrets never enter exported configuration or Git.
- Before adding a contrib project, check that its stable release is covered by the security advisory policy (the shield on its project page). Uncovered and dev releases receive no advisories.

## Update policy

- Security release windows (drupal.org "Security release numbers and release timing", checked 2026-11): contributed projects any Wednesday, core one Wednesday a month (usually the third), between 16:00 and 22:00 UTC. Highly critical core releases are pre-announced by a PSA, as on 18 May 2026 for a release on 20 May.
- Stay on the latest patch release of a supported minor, so a security release is a small update. The PSA of May 2026 told sites to update to the latest patch release beforehand for exactly this reason.
- `composer audit` checks the whole project, including PHP libraries; drupal.org's Composer update guide calls `drush pm:security` the legacy equivalent, and Drush 13 no longer lists it. Run `composer audit` in CI and act on advisories from the drupal.org security feed.
- An end-of-life core gets no security releases: Drupal 9 since 1 November 2023, Drupal 10 after 9 December 2026. For the May 2026 highly critical issue, Drupal 9.5 received only an unofficial patch to apply by hand. Report an end-of-life site as an open security risk with the upgrade as the remedy; do not present a patched end-of-life site as secure.
