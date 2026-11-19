# Caching

## Cacheability metadata

| Part | Question it answers | Examples |
| --- | --- | --- |
| tags | which data does this output depend on? invalidated when that data changes | `node:12`, `node_list`, `taxonomy_term:3`, `config:system.site`, `user:7`, a custom `comune_prenotazioni:user:7` |
| contexts | what does the output vary by? one cached copy per value | `user`, `user.permissions`, `user.roles`, `url.path`, `url.query_args:page`, `route`, `languages:language_interface`, `session`, `theme`, `timezone` |
| max-age | how long is it valid without an invalidation? | `Cache::PERMANENT` (default), seconds, `0` |

- Take tags from the objects you used: `$entity->getCacheTags()`, `$config->getCacheTags()`, or `$renderer->addCacheableDependency($build, $object)`, which also adds that object's contexts and max-age. `CacheableMetadata::createFromObject()` and `->applyTo($build)` do the same in preprocess and services.
- Custom data gets its own tags, invalidated where it changes: `Cache::invalidateTags(['comune_prenotazioni:user:7'])` after saving a booking.
- Choose the narrowest context that is correct. `user` makes one copy per account; when output only differs by role or permission, `user.roles` or `user.permissions` is right and far cheaper.
- Access results carry cacheability too: `AccessResult::allowedIfHasPermission($account, 'view bookings')->addCacheableDependency($node)`. Returning a bare boolean from custom access code loses it.
- Metadata bubbles from child render arrays to the page. Code that renders to a string and returns the string, instead of returning the render array, cuts the chain.
- Block plugins merge their values with the parent's in `getCacheContexts()`, `getCacheTags()` and `getCacheMaxAge()`.

## Cache layers

- **Internal Page Cache**: whole responses for anonymous users, keyed by URL. Contexts beyond the URL and render max-age do not reach it; the cache-max-age documentation (checked 2026-11) states that max-age does not work for anonymous users with this module, Varnish or CDNs.
- **Dynamic Page Cache**: responses for all users, varied by the bubbled contexts. Elements built through a lazy builder (blocks are) whose contexts include `user` or `session`, or whose max-age is 0, are turned into placeholders automatically, so they do not make the whole page uncacheable.
- **BigPipe**: streams those placeholders after the cached page for authenticated users.
- **Render cache**: individual elements, keyed by `#cache['keys']` plus contexts.

## Patterns

- **Personalised piece on a shared page** (a greeting, a basket count, "my bookings"): a `#lazy_builder` callback with `#create_placeholder => TRUE`. The callback is a service method declared trusted (`TrustedCallbackInterface`) and returns its own render array with its own contexts and tags, so the rest of the page stays cached.
- **Time-dependent output for anonymous visitors** ("events today", an opening-hours badge): invalidate a custom tag from cron when the period changes, or use the Cache Control Override module. `page_cache_kill_switch` disables caching for the whole response, so it is the last resort for a page that truly cannot be cached.
- **Sessions**: anything that starts a session for an anonymous visitor, such as storing a value in the session or a status message, makes their pages uncacheable. Keep anonymous flows sessionless where possible.
- **Reverse proxy or CDN**: with Varnish, Fastly or Cloudflare in front, install the Purge module with a tag-based purger so invalidations reach the proxy. Without it, the only lever is a short `page_cache_maximum_age`, and editors see stale pages.

## Diagnosing

- Locally, set the container parameter `http.response.debug_cacheability_headers: true` in `development.services.yml` to get `X-Drupal-Cache-Tags`, `X-Drupal-Cache-Contexts` and `X-Drupal-Cache-Max-Age`. Not on production: with many tags the headers can exceed server limits.
- `X-Drupal-Cache` shows HIT or MISS for the page cache and `X-Drupal-Dynamic-Cache` shows HIT, MISS or UNCACHEABLE for the dynamic page cache.
- A cache bug is fixed by finding the missing tag or context, never by `drush cache:rebuild` on a schedule or by setting max-age 0 on the parent.

## Proof

Request the page as anonymous and as two different users, and on two different URLs where the output should differ; then edit the underlying entity and reload without clearing caches. All of these must show the right output.
