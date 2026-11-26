---
name: agent-accounts
description: Manage accounts per AI CLI tool, recognise quota limits, ask once before switching and offload helper tasks to a free-quota agent. Use when a tool hits its limit, not for choosing models.
---

# Agent Accounts

## Scope

Use when an AI command-line tool stops work with a usage or rate limit, or when a self-contained helper task can run on a free-quota agent instead of the paid session. The accounts, tools, sign-out and sign-in commands, and what shares a sign-in live in configuration the user supplies; this Skill holds the decision rules, not that inventory.

## Tell a quota limit from other failures

- A quota or rate limit is what the tool itself says: usage or rate limit reached, quota exhausted, HTTP 429, or a reset time. A network error or an expired session is not a quota problem; fix that instead.
- When the message gives a reset time within about an hour and the work can wait, keep doing other work and retry after the reset. Do not ask.
- Otherwise ask the user once, in one line, naming the tool, the account in use (from its status command), when it resets, and a recommendation. Switching accounts is one of the few decisions worth asking about; the question itself is the escalation.
- On yes, run the sign-out command, then the sign-in command, which opens the browser for the user. Wait until the status command shows a different account, say which account is now active, and continue the interrupted work.
- Never type a password or a verification code, never read or copy credential files, never store an account's details anywhere.
- Check what shares a sign-in before switching. When one login is shared by every session of that tool on the machine, switch only when all of them are blocked by the same limit, and say so when asking.

## Spend scarce quota where it shows

- Quota is counted per account and per model, so route scarce or premium models to the work where their quality shows, and mechanical work to the free tier.
- Everyday coding, integration and review use the session's default model.
- Visual and page design, where the result is judged by look, is where a premium model earns its quota; mechanical edits, merges and waiting on CI never are.
- Scheduled runs use a deterministic script wherever the decision can be written down, and a model only where judgement is needed.

## Hand side work to a free-quota agent

- Hand self-contained helper tasks to an agent running on a free quota: a second, independent review of a diff or document; research or a summary of long material; first drafts of mechanical changes in a personal repository, on a separate branch.
- Run it non-interactively from the folder the task is about, with a brief written as for any delegate: goal, files, constraints, what to return.
- Treat its output as material to verify, never as a finished result: read the changes yourself before using them.
- Never hand it secrets, production or store actions, employer or client code or data, or decisions the user's rules reserve.

## Completion

- The interrupted work continues on the new account, or resumes after the reset, with the user told which account is active.
- Helper output is verified before it is used; unverified output is not merged, sent or published.

Source: fused from the author's Notion skill `agent-accounts` (2026-11), generalized; the skill's personal references folder (account inventory, machine paths, sign-in commands) was not used.
