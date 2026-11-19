---
name: help-center-article
description: Write a help-center, knowledge-base or FAQ article such as a how-to, troubleshooting guide or known-issue notice customers can find by search. Use for support docs, not store copy or internal SOPs.
---

# Help Center Article

## Use

Use when a solved problem, a repeated question or an ongoing incident should become an article that customers read on their own.

An internal procedure for the people doing the work belongs to `operations/sop-builder`. A reply to one customer belongs to `support/customer-support-replies`.

## Domain inputs and blockers

Exact interface paths, button names and error text come from the user or the product, never from memory; a step that cannot be confirmed is left as a marked placeholder. Say which product version or plan the article applies to when it matters. When a list of existing articles is available, decide between updating one and writing a new one before drafting.

## Choose the type first

| Type | Opens with | Shape |
| --- | --- | --- |
| How-to | "This guide shows how to…" | prerequisites, numbered steps, how to verify it worked, common problems |
| Troubleshooting | "If you are seeing [symptom]…" | symptom, then the fixes from most to least likely, then where to get help |
| FAQ | the customer's own question | the answer in the first sentence |
| Known issue | "Some users are experiencing…" | status, who is affected, workaround, updates |
| Reference | what the thing is | tables and definitions to look up |

An answer that needs steps is a how-to, not an FAQ.

## Being found

- The title uses the customer's words and contains the symptom, the tool name or the verbatim error: "Fix: dashboard shows a blank page", not "Dashboard issue".
- Include the exact error message as text; people paste it into search.
- Use the words customers use ("can't log in") rather than internal terms ("authentication failure"), and mention common synonyms once (delete/remove, export/download).

## Writing

- A step starts with a verb, names the exact path (Settings > Integrations > API keys) and says what the reader should see afterwards.
- One topic per section, paragraphs of two to four sentences, numbered lists for sequences, code formatting for commands, values and error text.
- Troubleshooting explains the cause in one plain sentence; the detailed root cause stays out unless the reader needs it to choose a fix.
- Link how-to and troubleshooting articles to each other where a reader would naturally move between them.

## Known issues

A known-issue notice always shows: the status (investigating, workaround available, fix in progress, resolved), who is affected, the date of the last update, the workaround or an explicit "no workaround yet", and a dated update log. An out-of-date notice damages trust more than none, so it is updated on a fixed rhythm while open and kept for about a month after resolution.

## Update or create

Update the existing article when the product changed, a detail is missing or readers report a confusing section. Write a new one for a new feature, a gap that tickets revealed, or when one article has grown to cover several topics or audiences.

## Output

The article, with its title, type and the audience or plan it applies to, followed by publishing notes: what must be verified by someone who knows the product, existing articles that need a matching edit, and a suggested review date.

## Constraints

- A wrong article is worse than no article: steps are followed once from start to finish, or the article is marked as not verified.
- Do not promise fix dates or describe unreleased features.
- Do not include customer names, account details or internal ticket links.
