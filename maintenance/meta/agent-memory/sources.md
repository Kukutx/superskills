# Agent Memory sources

Maintenance-only.

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| thedotmack/claude-mem | https://github.com/thedotmack/claude-mem | Session capture: what to record so context survives across sessions | 2026-11 |
| mem0ai/mem0 | https://github.com/mem0ai/mem0 | Extract and consolidate memory from conversation | 2026-11 |
| getzep/graphiti | https://github.com/getzep/graphiti | Temporal knowledge graphs: facts carry time, newer facts supersede older ones | 2026-11 |
| Author's Notion skill `owner-workspace` | https://app.notion.com/p/41d1494ce8fd8158a369e9c9843c1ed9 | Session-ownership map, leaving other sessions' work alone, outbound actions wait for explicit OK, owner-only steps go to the single hand-off place, no temp files/branches/reminders left behind | 2026-11 |
| Author's Notion inbox note "小红书三篇内容提炼" | https://app.notion.com/p/41d1494ce8fd81cbac65c7702f8bfb53 | Long-horizon handoff pattern: per-handoff state files plus an append-only log | 2026-11 |

The two Notion rows above feed only `references/multi-session-coordination.md`, fused and generalized 2026-11-24; the skill's personal references folder was not consulted and none of it entered the pack.

Upstream licenses (apply to the adapted methodology only): all three Apache-2.0; see the upstream repositories for the full license text. Methodology only — no code was copied and no tool is required or bundled. The skill is a plain-file method that works on any host.
