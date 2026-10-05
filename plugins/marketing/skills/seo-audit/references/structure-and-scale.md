# Structure and Scale

Read for a site with several languages, pages generated at scale, a navigation or URL restructure, or one of the common diagnostic scenarios.

## Languages

- Canonical and hreflang must agree: every URL in an hreflang set is canonical to itself. An annotation that points at a URL canonicalized elsewhere sends two conflicting instructions, and so do two methods (HTML, header, sitemap) that give different URLs for the same language and region.
- Regional versions in one language (two English markets, for instance) that differ only in currency or spelling may be treated as duplicates and only one shown; they need a real difference in content to earn separate places.
- A page whose template is translated while the main content stays in the original language is a duplicate, not a translation.
- For a language that cannot be served well, the best page is none: neither noindex nor a canonical to another language repairs a thin page, and a large share of unhelpful pages weighs on the whole site.
- At many languages, carry hreflang in the sitemap rather than in every page head, split sitemaps by content type rather than by language, and check that the generated output really contains the self-reference. Start with the pages that receive visitors in the wrong language.
- Crawl budget is a finding for very large or very fast-changing sites only; do not raise it for a small one.

## Pages generated at scale

Each kind has its own test of real value:

| Page type | Has value when |
| --- | --- |
| location | real local data, providers or prices; not the town name swapped in |
| audience or industry | content, features, proof and use cases specific to that group |
| integration | real details, setup steps and combined use cases, for an integration that works |
| comparison | honest, balanced, current, with a recommendation by scenario |
| glossary | more depth than a dictionary, with examples and links |
| list of the best | real criteria and testing, a visible date, not an affiliate ranking |
| directory | broad coverage, filters, detail per entry |
| template | usable as it is |

What the business owns decides the play: proprietary data suits statistics, directories and profiles; an integration ecosystem suits integration pages; several audiences suit audience pages; a local business suits location pages.

"Five hundred pages, eighty indexed" is diagnosed in this order: do the pages really differ beyond a template with swapped words; can they be reached through internal links; are they in the sitemap; does robots.txt allow them; are they duplicates or near-duplicates. A search engine may decline to index thin pages whatever else is done.

## Navigation

- A large menu has two to four logically grouped columns and no dropdown inside a dropdown. A footer has three to five themed columns, not fifty unsorted links; comparison and location pages can live there.
- Avoid: eight or more header items, icon-only navigation, the main navigation hidden behind a menu button on desktop, navigation that differs from page to page, breadcrumbs that disagree with the URL, and navigation that exists only in script, since crawlers need real links.
- On a phone the main action is visible without opening the menu. A documentation site has a fixed, collapsible sidebar, search at the top and previous and next links.

## Restructuring a site

Inventory every existing page first, then regroup and show before and after. Mark each page as kept, new, removed or redirected, or moved; every moved page gets a redirect. Pages generated at scale sit under their own hub (an integrations hub, a comparison hub) with links between hub and pages, not in the main navigation. A small business site stays flat.

## Diagnostic scenarios

- **Traffic fell after a migration**: the redirect map, canonicals on the new pages, robots.txt, the sitemap, preserved titles and descriptions, redirect chains and loops, soft 404s, lost internal links, URLs changed without a redirect. Recovery takes weeks.
- **"Why do we not rank for this term"**: whether the title, main heading and URL match the term; depth against the pages that rank; two of the site's own pages competing; indexing and canonical; evidence of experience and expertise on the page.
- **Large store**: filter combinations creating duplicate URLs, pagination, parameters and session identifiers in URLs, thin category pages, repeated product descriptions, pages for discontinued products.
- **Blog**: stale posts, posts competing with each other, topic clusters, internal links, author pages.
- **Local business**: name, address and phone identical on the site and its listings, a page with unique content per location, a complete business profile, replies to reviews.

## Structured data detail

Commonly included beyond the minimum, where the information is on the page: for an article, the modified date and an author with a profile; for a product, identifier, brand, price with currency, availability and a current validity date; for an organization, logo, profiles elsewhere and a contact point; for a local business, coordinates, opening hours, phone and full address; for an event, end date, attendance mode, status and organizer. Entities in one graph refer to each other by identifier instead of being repeated. Content on health, money or law shows a reviewed date, the author's credentials and, for law, the jurisdiction. None of this is a promise of a search feature; eligibility is decided by the search engine's own page for each type.
