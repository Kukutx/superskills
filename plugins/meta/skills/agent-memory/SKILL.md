---
name: agent-memory
description: Keep cross-session memory in plain files — capture, consolidate, retrieve, forget on request. Use for decisions and context that must survive between sessions.
---

# Agent Memory

## Use

Use when the same user works with an agent across sessions and the work depends on remembering: decisions already made, preferences, commitments, open threads, corrections, and who people are. Memory is a tool-independent method, not a product: plain files the user owns, readable on any host, with no service to install. The approach follows the published methodology of session-capture tools (claude-mem), memory layers (mem0) and temporal knowledge graphs (graphiti) — capture, consolidate, retrieve, forget — without bundling or requiring any of them.

Not for a live database, a search index, or a store for secrets. Never use memory to store passwords, tokens, keys, full private messages, or health and financial identifiers unless the user explicitly asks for that exact item — and even then, keep it in the user's own files, never in a shared repository.

## What to remember

- Decisions the user made, with the reasoning in one line.
- Preferences that change future behaviour (language, tools, scope, what to leave alone).
- Commitments: what was promised, to whom, by when, and whether it is done.
- Open threads: work started but unfinished, and the next step.
- Corrections: where the user corrected the agent, and what the right version is.
- People and groups: who someone is to the user, in one line, only what the user stated.

Do not record what the user did not state. Do not infer traits, motives, health or relationships from indirect signals, and do not write a profile the user never approved. A memory that cannot name its source is not a memory; it is a guess — leave it out.

## Capture

At the end of a session, or when a durable fact appears mid-session, write one line per fact: the fact, who said it, and when. Keep the curated file short; put raw detail in dated notes and let the curated file point at them. When a new fact replaces an old one, record the replacement in the curated file (old line struck or noted as replaced, with the date) instead of silently keeping both.

## Files

- One curated file holds the durable facts, grouped as facts, preferences, commitments and people. It is the only file a new session reads by default.
- Dated notes hold the raw session detail the curated file was distilled from.
- Both live in the user's own workspace. They are never copied into a shared repository, a skill, or a published bundle, and they are never sent to another person or service.

## Consolidate

Periodically, fold dated notes into the curated file: promote what still matters, drop what is superseded or no longer true, merge duplicates into one line. The curated file stays short enough to read at the start of a session; if it grows past that, split by topic and keep an index, not a longer file.

## Retrieve

- At the start of a session, read the curated file before acting.
- When the task touches an old thread, search the dated notes for it; do not rely on the curated file alone for detail.
- When acting on a memory, name its source (the date or the conversation) so the user can correct it.
- When a memory and the current request conflict, the current request wins; record the change as a new memory instead of arguing with the user.

## Forget

On request, remove the item from the curated file, the dated notes and any index, then confirm what was removed. Forgetting is complete only when no copy remains in the agent's files; a line left in a dated note is not forgotten. Never bring back a forgotten fact from another copy.

## Tooling

The method needs no tool: when a host offers a memory product, it may be used as the store, but the files above remain the portable fallback and the export format.
