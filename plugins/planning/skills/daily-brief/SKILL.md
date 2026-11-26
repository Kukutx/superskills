---
name: daily-brief
description: Scheduled unattended multi-source digest that syncs the hub, backs up memory, collects what needs the owner and writes a short structured brief. Not for triaging pasted messages.
---

# Daily Brief

## Scope

Use for the scheduled, unattended daily run that produces the one brief telling the owner what needs them, and keeps the shared hub current so every agent works from the same context. Sources are configurable slots the user supplies: hub and rules, memory, hand-off list, mail, calendars, job tracker, repositories, health snapshots, production log, material inbox. Triaging pasted messages or notes stays with `planning/inbox-and-task-digest`, which fetches nothing; this Skill fetches from the configured sources.

## Boundaries

- Read-only on mail, repositories, calendars and production logs: never send, reply, archive, label, merge, push to a project repository or write to production.
- Writes go only to the configured hub pages and databases, the memory backup location, the run's own state files, and the brief page itself.
- Never copy secrets, verification codes or employer or client material into the hub or the backup.
- An unavailable source (connector missing, host unreachable, no network) is reported as unavailable in one line. Never guess its content.

## 1. Sync the hub

- Keep a state file with the hash of the rules source and, per skill, of its packaged archive.
- Rules: when the hash changes, replace only the rules section of the hub's entry page, then store the new hash.
- Skills: when a skill's packaged hash changes, upload the new package to its hub page (creating it when there is none), enable the skill, and store the new hash. A hub skill page with no matching packaged skill is reported, not deleted.

## 2. Back up memory

- For each memory edited since the last run (all of them on the first run), write a backup file: first line its type, last-edited date and last editor, then the body.
- Remove backup files whose memory no longer exists.
- Memories that copy another source and were edited in the hub are listed under system improvements, so the source can be updated.

## 3. Collect what needs the owner

Look back to the previous brief, or 24 hours on the first run.

- Hand-off list: the open items in the owner's single hand-off place, plus any new file placed there. The hand-off list is the only source for what the owner must do: quote its items and recommendations as they stand, never one of your own that differs. When an item's recommendation looks wrong, say so under system improvements instead.
- Mail: threads that expect a reply or action from the owner; skip promotions, social mail, newsletters and notifications handled elsewhere. One line each: who, what they want, the suggested reply or action.
- Job and life: tracker rows whose next step falls today or tomorrow, or whose status changed; calendar events today and tomorrow. When an email gives a clear outcome a tracker row does not show yet (interview date, offer, rejection, the owner declining), update that row and list the change under what this run did. An unclear email changes nothing; mention it under mail.
- Repositories: open pull requests, not bot-opened, that wait for the owner; default-branch CI failures in repositories pushed in the last 30 days. Dependency updates come from the maintenance run's state file: report what it merged under what this run did, and the pull requests it left open per repository with its reason, under projects. When that file is older than a day, say the maintenance run did not run.
- Machines, sites and scheduled runs: read the health snapshot written by the scheduled health check (sites, machines, runners, disk, expiry dates, quotas, renewals, alerts, uncommitted work). When it is stale, run the health check first. Report its bad and warn items in its own words, so the brief and the health banner above every session agree; a host-side pause or billing block goes under what only the owner can do, with the recommendation.
- Production: the last entry of the production patrol log (its conclusion line, or that it could not run). Production alerts belong to the production session; report, do not act.
- Material inbox: pages added since the last run, not yet in the evaluated-pages state file. Read each in full and judge it against how the owner works today: what would remove work or make their agents better, what does not fit and why, and how it would be added (rule, skill, automation, change, tool). Do not count an idea as new when the system already does it; name where. Append a dated evaluation note at the end of the page, never changing what is above it, record the page in the state file, and put the strongest one or two points under system improvements. Adopting them is for the next working session, not this run.

## 4. Write the brief

- Replace the whole brief page, in the owner's language, plain words, no code. At most about 300 words; leave out empty sections.
- Fixed sections: what only the owner can do; today and tomorrow; mail; projects; what this run did; system improvements.
- What only the owner can do holds only that (sign-in, payment, device, permanent deletion, a decision their rules reserve), each with the recommendation.
- Projects holds one line per project (each active repository, the job, any commercial project), status and next step.
- What this run did holds what the run synced or backed up.
- System improvements holds at most two suggestions this run's evidence supports, each with why. Skip it rather than pad it.
- On Mondays, before writing system improvements: read the last week's release notes for the AI tools in use and check the official MCP or server registry for a service the owner uses. Name at most two new features that would remove work the owner or their agents do today, with what each would replace. Never adopt one from the brief.
- On Mondays the prompt also carries last week's guard-rule statistics. Under system improvements, name a rule that stopped work more than five times and, after reading its log lines, say whether it caught real mistakes or misfired; name an observe-mode rule that hit without misfiring as ready to enforce. Change nothing yourself.

## Completion

- Fetch the brief page once to confirm it saved; the final reply is the same brief as plain text.

Source: fused from the author's Notion skill `daily-brief` (2026-11), generalized; its personal references folder was not used.
