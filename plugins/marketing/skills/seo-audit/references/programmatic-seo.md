# Programmatic SEO

Rules for producing SEO pages at scale from a template and a dataset, adapted and rewritten from `coreyhaines31/marketingskills` programmatic-seo (MIT).

`marketing/seo-audit` audits pages; this file is the build side, used only when a set of pages is being produced from one pattern.

## Before designing

Understand three things first: the business context (product, audience, conversion goal for these pages), the opportunity (what search patterns exist, how many potential pages, how the search volume is distributed), and the competition (who ranks for these terms now, what their pages look like, whether the site can realistically compete).

## Core principles

- **Unique value per page.** Every page must provide value specific to that page, not just swapped variables in a template. The more differentiated, the better. Better 100 great pages than 10,000 thin ones.
- **Proprietary data wins.** Data defensibility runs: proprietary (created by the business), product-derived (from users), user-generated (from the community), licensed (exclusive access), public (anyone can use, weakest).
- **Clean URL structure.** Prefer subfolders to subdomains: a subfolder inherits the main site's internal links and structure, while a subdomain needs its own.
- **Genuine search-intent match.** Pages must actually answer what people are searching for.
- **No penalties.** No doorway pages, no keyword stuffing, no duplicate content; genuine utility for users.

## The 12 playbooks

| Playbook | Pattern | Example |
| --- | --- | --- |
| Templates | "[Type] template" | "resume template" |
| Curation | "best [category]" | "best website builders" |
| Conversions | "[X] to [Y]" | "$10 USD to GBP" |
| Comparisons | "[X] vs [Y]" | "webflow vs wordpress" |
| Examples | "[type] examples" | "landing page examples" |
| Locations | "[service] in [location]" | "dentists in austin" |
| Personas | "[product] for [audience]" | "crm for real estate" |
| Integrations | "[product A] [product B] integration" | "slack asana integration" |
| Glossary | "what is [term]" | "what is pSEO" |
| Translations | Content in multiple languages | Localised content |
| Directory | "[category] tools" | "ai copywriting tools" |
| Profiles | "[entity name]" | "stripe ceo" |

Choosing: proprietary data points to directories and profiles; a product with integrations to integrations; a design or creative product to templates and examples; a multi-segment audience to personas; a local presence to locations; a tool or utility to conversions; content or expertise to glossary and curation; a competitor landscape to comparisons. Playbooks layer: "best coworking spaces in San Diego" is curation plus locations.

## Implementation

1. **Keyword pattern research.** Identify the repeating structure, its variables, and how many unique combinations exist. Validate demand: aggregate search volume, head-versus-long-tail distribution, trend direction.
2. **Data requirements.** What populates each page, whether it is first-party, scraped, licensed or public, and how it is updated.
3. **Template design.** Header with the target keyword, a unique intro (not just variables swapped), data-driven sections, related pages and internal links, and calls to action matched to intent. Uniqueness comes from conditional content driven by the data and original insights per page.
4. **Internal linking.** Hub-and-spoke: a main category page as hub, programmatic pages as spokes, cross-links between related spokes. No orphan pages; every page reachable from the main site, in the XML sitemap, with breadcrumbs and structured data.
5. **Indexation.** Prioritise high-volume patterns, noindex very thin variations, manage crawl budget, separate sitemaps by page type.
6. **Build platform.** It must hold the page count, refresh the data, render server-side HTML, branch on data for conditional sections, and control indexation per page. Prefer the existing site's CMS when it can; otherwise serve the set on a subpath of the main domain.

## Quality checks

Pre-launch: each page provides unique value and answers search intent; unique titles and meta descriptions, proper heading structure, schema markup, acceptable page speed; connected to the site architecture with related pages linked and no orphans; in the XML sitemap, crawlable, no conflicting noindex.

Post-launch, track indexation rate, rankings, traffic, engagement and conversion. Watch for thin-content warnings, ranking drops, manual actions and crawl errors.

## Common mistakes

- Thin content: only swapping city names in identical content.
- Keyword cannibalisation: several pages targeting the same keyword.
- Over-generation: creating pages with no search demand.
- Poor data quality: outdated or incorrect information.
- Ignoring UX: pages built for Google, not for users.

## Source

Adapted and rewritten from `coreyhaines31/marketingskills` skills/programmatic-seo/SKILL.md, https://github.com/coreyhaines31/marketingskills (MIT).
