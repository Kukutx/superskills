# Multi-Session Coordination

Use when several agent sessions work for the same user at once, or when one long-running job hands off to the next session. This reference covers who owns what and how a handoff carries state; capturing and retrieving memories stays with the main Skill.

## Session ownership

- Work that belongs to another session, as listed in the user's session-ownership map, is left to that session; report what was noticed instead of changing it.
- Anything that sends, publishes, pushes or saves to the user's accounts waits for their explicit OK in the current conversation, unless their rules say otherwise.
- Anything only the user can do (sign-ins, approvals, scripts they must run themselves) goes to the single hand-off place named in the ownership map, with an entry in its list, never anywhere else.
- A step the host's safety checks will not let this session do on the user's accounts goes to a session that can do it; only a step that needs the user's own sign-in becomes a one-click script in the hand-off place.
- Leave no temporary files, branches or open reminders behind.
- The session-ownership map, the hand-off place and the rules are configuration the user supplies; look them up in the material and the repositories before asking the user.

## Long-horizon handoff

- Split a long-running job into per-handoff state files plus an append-only log, so the next session resumes from files instead of from memory.
- Each state file covers one handoff: what is done, what is open, the next step, and the decisions made in that handoff. The log records events in order and is never rewritten.
- A new session reads the latest state file and the log tail before acting, then writes its own state file when it hands off again.

Source: the session-ownership core of the author's Notion skill `owner-workspace` (2026-11), generalized, and the per-handoff state-file pattern from the inbox note "小红书三篇内容提炼" (2026-11-20 evaluation, 待做 item); the skill's personal references folder was not used.
