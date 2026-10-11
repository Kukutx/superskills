---
type: llm
---

PASS if the fix makes "one hit per target per attack instance" explicit: e.g. keep a set/array of already-hit targets (or an attack id) that is cleared/renewed when each new swing (each combo stage) starts, and skip targets already hit in the current swing; so each of the three combo hits can still land once on the same enemy.
FAIL if the only fix is a time-based gate that would block the next combo hit or is unrelated to the attack instance, such as giving the enemy an invincibility timer / damage cooldown longer than ~0.2s, a global hit cooldown, or disabling monitoring after an arbitrary await delay; or if the hit-set is never reset between combo stages (so the 2nd and 3rd hits cannot damage the same enemy).
