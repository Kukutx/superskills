# Skill Router decisions

Scope decisions that were considered and not added, with reasons, so they are not
re-litigated without new evidence. See also `docs/clone-reverse-policy.md`.

## Decided 2026-11-24 (deep-dive round 3)

- **Clone / reverse skills (rea, replica-skill, reverse-skill): forbidden.**
  Only a defensive subset is allowed (detecting clones of the user's own work,
  authorized review of their own code); no defensive skill was added this round.
  Full reasoning in `docs/clone-reverse-policy.md`.
- **agent-memory: added** (`meta/agent-memory`). Tool-independent cross-session
  memory in plain files, methodology from claude-mem, mem0 and graphiti, no tool
  required or bundled.
- **social-publish and social-engagement: added** (`marketing/social-publish`,
  `marketing/social-engagement`). Generic rewrites of the author's own local
  skills (v3.4 and v1.0). The deterministic check scripts and platforms.yaml
  were not ported: the pack has no script convention. LinkedIn engagement routes
  through the browser here; the author's personal li-* skills stay separate.
- **Unity skill: not added.** No star source and no author custom skill provide
  real material; Godot coverage is not a substitute. Reconsider when a Unity
  source appears.
- **MCP as a skill: not added.** The starred MCP items are servers (tools), not
  skills: whatsapp-mcp, GhidraMCP, mcp-for-blender. A skill that teaches "use
  MCP" has no durable decision to encode; individual MCP servers are set up
  through the custom-connector flow when needed.
- **Model-selection skill: not added.** No star source and no author custom skill
  provide real material; model capability changes faster than a Skill can track.
- **Fitness / travel skills: not added.** No star source and no author custom
  skill provide real material, and both are out of scope for a work pack.
- **Italy-admin skill: not added.** No source material yet; the existing
  drupal-development note on Italian PA sites is the only toehold. Reconsider
  if the user asks for it with material.
- **Core bundle membership for the 3 new skills: not changed.** `gpts/core/`
  is a curated most-used set; the new skills have no usage evidence yet.
  Reconsider after they are used.
- **Codex manifest descriptions and CODING_CATEGORIES mapping: unchanged.**
  No verifiable schema or source exists in the repo; adding an unverified field
  risks breaking the Codex install. (Carried from round 1 and round 2.)
- **Live eval replays: not run.** They cost model usage. Routing claims in this
  round are structurally verified only. Highest-value first replay when budget
  allows: security-audit vs code-review, then the new social-publish vs
  social-content boundary.
