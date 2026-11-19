---
name: multilingual-docs
description: Keep docs, articles or site copy in several languages in step with one source language at native quality, with parity checks and native review. Not for one-off chat translations or microcopy.
---

# Multilingual Docs

## Use

Use when the same text has to live in more than one language and stay correct over time: a set of articles, a README, notes, a landing page or a portfolio published in two or more languages, or a single important text being translated for publication.

A one-off translation of a message in chat does not need this process. Interface microcopy, store listings and resumes have their own owners (`writing/ux-copy`, `writing/app-store-copy`, `writing/resume-writing`); apply the language rules below inside those owners when they need several languages.

## Inputs and blockers

Establish from the material or the repository before asking:

- the languages to maintain, and which one is the source;
- the audience and register of each version;
- the spelling variety where it matters (for example British or American English);
- existing terminology, file layout and the repository's own language rule for code, comments, commits and READMEs.

Ask only when the source language or the set of languages cannot be inferred and the choice would change the work. Do not add languages nobody asked for.

## Source of truth

- One language is the source. A change starts there and reaches every other version in the same change, never "later".
- When translating exposes a problem in the source (a wrong fact, an ambiguous sentence, a claim the author never made), fix the source as well and carry the fix to every version.
- Keep facts, numbers, dates, names, links and structure identical across versions. Wording may differ; meaning may not.
- Repository texts with their own language rule (code, comments, commit messages, technical READMEs) follow that rule and are not translated.

## Layout

- One folder per language (`zh/`, `en/`, `it/`, …) with the same file names in every folder, so a path differs only by its language folder.
- Under each title, a language switch line linking the same file in the other languages; the current language is plain text, not a link.
- Cross-references between documents point to the same language's file.
- An index at the root that lists the languages; each language folder has its own index in that language.

## Native quality

Translate meaning and register, not words. Rebuild sentences the way a native writer in that field would write them; keep technical terms the way native practitioners actually use them (often the English term: merge, fork, pattern, major version).

Patterns that mark a text as translated or machine-written, to remove in review:

- **Scaffolding from the source language**: "There are two reasons. First… Second…", "One more point:", sentence fragments that open with a colon ("The reason:", "Il motivo:"), lists whose items do not match grammatically.
- **Calques**: words that look right but are not what natives say in that context (Italian "scala" for scale, "capacità" for capability, "confini" for boundaries, "lungo la strada" for along the way).
- **Stock connectors and headings**: "Moreover", "In summary", "Inoltre", "In sintesi" used by reflex.
- **Repetition** of the same word inside one sentence; dangling modifiers; scare quotes around ordinary phrases; "actually" and "really" used as filler.
- **Slogans and uplift**: aphoristic closing lines, rhetorical parallels and statements of how meaningful something was, unless the source is genuinely written that way.

## Meaning drift

Check every sentence where a small wording change flips the meaning:

- modality: "need not" vs "must not";
- scope of negation: "is not always the same" vs "is never the same";
- quantities and comparisons: "24 times longer" is not "an order of magnitude longer";
- states vs events: "no error was raised" is not "nothing broke";
- who did something, and whether it happened once or as a rule.

## Review

- For text that will be published, have each language reviewed by a reviewer who did not write it and who reads that language natively, sentence by sentence, against the source.
- Judge each suggestion: accept what fixes meaning, grammar, idiom or consistency; reject what contradicts the author's facts or own words, and say why.
- Keep a short terminology list per project when terms recur, and apply it to all versions.

## Completion

The work is done when:

- every language version carries the same change;
- a structural comparison shows the same headings, list items, tables, numbers and links in every version (a short script that counts these per file is enough);
- important public text has had the independent review, or the reply says plainly that it has not.

Report what changed in each language and anything left for the author to decide.
