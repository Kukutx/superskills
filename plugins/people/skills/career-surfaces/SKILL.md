---
name: career-surfaces
description: Keep facts consistent across a resume, LinkedIn, GitHub profile and personal website, each with its own audience and source of truth. Not for writing a resume alone.
---

# Career Surfaces

## Scope

Use for any change to a person's public career surfaces: usually a resume, LinkedIn, a GitHub profile and a personal website. Each surface has its own audience, language and source of truth; they are independent and refer to each other, never one shared text. The facts, settled choices and per-surface rules live in configuration the user supplies; they win over the general rules below. Writing a resume on its own stays with `writing/resume-writing`.

## Writing copy

Scope:

- "Change the content" means the person's own content only (intro, story, timeline, project texts). Template copy, template code and the other surfaces stay untouched unless the user names them.
- Change only what was asked. Keep existing sentences that already work; when asked to improve, improve, and do not quietly fall back to the old text.
- Background the user mentions is context for tone, not a theme. Never repeat or expand a personal detail they did not ask to see on the page.

Lasting:

- Past facts with dates are fine. Present status is a judgement call: a badge, a "Present" range or a store link may state today's truth; a sentence in an intro, story or timeline should prefer wording that does not depend on today. Never flag or change existing present-status text unless asked.
- Never name things that may disappear (specific repositories, side projects, internal tools, what a page happens to show). Describe them generically or leave them out.
- Write so a sentence stays true if a product is sold, renamed or refactored: past tense for what the person built, not ownership or state.

Tone:

- Plain, calm and specific. No idioms or slang that translate badly, no drama, no self-praise. When the user reads the copy through a translation, check each sentence by imagining that translation.
- Short sentences, concrete nouns, at most one reflective line per paragraph.
- Reference sites are for structure and feel only; never copy their wording, milestones or anecdotes.

Before showing anything, reread every new sentence against these rules, then show each change as original to new in plain words (with a gloss in the user's language when they read the surface's language with effort). Mark which lines are yours.

## Facts

- Facts come only from the user's repositories, resume, own profile text, or what they say. Read the material before asking anything it can answer. Facts about jobs come from the user; never question them.
- Never invent, inflate, delete or merge facts. Never add content that was not asked for. Reviewer or "best practice" advice never overrides the user's wording or reference layout.
- Assets the user uses (images, music, reference-site details) are theirs to use; do not question or replace them.
- Private planning notes found in their folders are never mentioned on any surface.

## When a fact changes

One change reaches every surface that states it, each through its own rules, but only the surfaces the user asks for:

1. Confirm the fact from the user's material (repository, store listing, their words).
2. Resume: edit its source of truth, build, archive (follow the resume repository's own skill when it has one).
3. Website: content file and project media.
4. GitHub: the repository's README and description, then the profile README when it names it.
5. LinkedIn: draft the text for the user to paste.

Finish with a consistency pass: titles, dates, company and product names read the same everywhere. Report differences; change only what the user approves.

## Per surface

- Resume: one source file, one build pipeline; never hand-edit generated outputs. Touch it only when the user names it; a website wording change does not extend to the resume.
- LinkedIn: About introduces a person, not a CV. No automation of any kind (no scraping, cookie tools or third-party LinkedIn integrations): automated access puts the account at risk. Read the profile from pasted text or the data export; write by drafting section by section; fill fields in a browser only when asked, and never press Save without explicit OK for that edit.
- GitHub: developers are the audience; concrete, short, in the user's tone, no recruiter phrasing. Repository descriptions match the product names used elsewhere.
- Website: ship through the site repository's own release process. Check motion and layout in a real browser over time and at several widths, not from static screenshots alone.

## Working style

- Do exactly what the user describes. "Click X to do Y" means X does Y: no new buttons, labels or controls. Anything visible they did not name is a proposal: ask first.
- Before anything ships, list every visible change and mark the ones nobody asked for.
- Be thorough the first time; when asked to rewrite, rewrite everything affected, not a patch.
- Do not ask questions the material can answer; when a real decision is the user's, give one recommendation and ask once.
- Never roll back the user's explicit choices.
- Nothing is committed, pushed, published or saved to the user's accounts without their explicit OK in the current conversation. Once they approve a release, carry it through to the live result without stopping at intermediate states.

Source: fused from the author's Notion skill `career-surfaces` (2026-11), generalized; the skill's personal references folder (surface list, facts, settled choices) was not used.
