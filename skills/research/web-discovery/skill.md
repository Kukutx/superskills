---
name: web-discovery
description: Find and rank public web resources, media, examples, pages, accounts or platform content when the user wants the best usable results rather than an evidence-synthesis brief.
---

# Web Discovery

## Use

Use when the main task is to **find, shortlist or rank things on the web**: videos, images, examples, pages, accounts, creators, resources, tools, references or platform content.

Use `research/research-brief` instead when the main task is deciding what is true, comparing factual claims, weighing source quality, reconciling disagreement or establishing current policy/status.

Do not use this Skill for retail-product shopping or local-business discovery when a dedicated product/local tool owns the task.

## Workflow

1. Extract the user's explicit goal and stated filters.
2. Preserve those filters exactly. Fill only operational gaps that do not narrow or redefine the requested result set.
3. Search the sources and platforms that best match the request; prefer direct/original pages when the user asks for platform content.
4. Rank primarily by fit to the user's requested outcome, not by convenience, citation ease or an unstated risk proxy.
5. Return the smallest useful shortlist. When the user asks for the best options, do not dump a broad catalog.
6. Verify changeable properties only when they are requested or materially determine whether a candidate satisfies an explicit requirement.

## Constraint fidelity

The user's stated requirements are the selection criteria. Do **not** silently add new filters such as:

- free / paid;
- copyright or licensing status;
- commercial-use permission;
- watermark status;
- account/login requirements;
- platform policy preferences;
- source type or stock-site preference;
- geographic, format or quality restrictions the user did not state.

A possible concern is not automatically a selection criterion. Do not convert a caveat into a filter unless the user asked for it or the requested action cannot be completed correctly without resolving it.

If the user explicitly rejects a criterion, remove it from the search/ranking logic rather than repeating it as a warning.

## Source behavior

- If the user asks for TikTok, Instagram, YouTube or another named platform, search that platform/direct content first rather than substituting stock or aggregator sites because they are easier to verify.
- If the user asks for mainstream sources, prefer genuinely mainstream/direct sources; do not redefine “mainstream” as “most permissively licensed”.
- Source authority matters when making factual claims about a result. It is not a replacement for the user's relevance criteria when the task is media/resource discovery.
- Do not introduce legal, copyright, commercial-use or licensing discussion unless the user asked for it or it is necessary to answer the specific requested action.

## Output

Default to:

1. **Best matches** — a short ranked set.
2. **Why each fits** — only the user-relevant reason.
3. **Direct source/link** — when available.

Do not add generic caveat sections, licensing lectures or unrelated alternatives.