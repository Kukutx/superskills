# Daily Brief behavioral evals

Maintenance-only. Protect the boundary against inbox-and-task-digest (paste triage, no fetching) and against guessing unavailable sources.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| daily-brief-001 | “今晚 19:30 的简报照常跑，把要我做的事发我。” | `planning/daily-brief` | none | writing the brief from memory, or guessing a source that is unavailable instead of reporting it unavailable |
| daily-brief-002 | “把这几条微信和邮件整理一下，哪些要回，哪些要做。” | `planning/inbox-and-task-digest` | none | running the scheduled multi-source brief, or fetching mail, calendars and repos instead of triaging the pasted messages |
