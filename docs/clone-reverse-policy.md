# Clone / reverse-engineering policy

Decided 2026-11-24 (deep-dive round 3). This is the pack's standing policy; a future
request to add a clone or reverse skill is judged against it, not re-argued from scratch.

## Verdict

**Forbidden as Skills: cloning or reverse-engineering third-party apps.**
**Allowed, defensive subset only: detecting clones of the user's own work, and
authorized review of the user's own code.** No defensive skill is added in this round:
authorized review of the user's own code is already owned by
`development/security-audit`, and clone detection of the user's own work has no
source material in the pack yet.

## What was reviewed and rejected

All three are MIT-licensed and starred by the pack author, which is why they were
considered rather than ignored:

| Repo | Stars (2026-11-24) | Claim | Why it stays out |
| --- | --- | --- | --- |
| `morluto/rea` | 476,840 | "Reverse engineer anything with agents, from app behavior down to native binaries" | Unbounded "anything" framing: app behaviour, binaries, third-party IP |
| `Jakeschincariol/replica-skill` | 10,526 | "Eleven free Claude skills that clone any app: reverse-engineer it, rebuild it" | Cloning an app is the purpose, not a side effect |
| `zhaoxuya520/reverse-skill` | 45,205 | "Reverse Engineering / Authorized Penetration Testing / Security Research" | The "authorized" qualifier is a label on a general capability; a generic Skill cannot verify authorization, so the capability ships unbounded |

Jailbreak and red-team material (`yueliu1999/Awesome-Jailbreak-on-LLMs`,
`e2sy/jailbreak-archives`) was already excluded and stays excluded.

## Reasoning

1. **The pack is distributable.** It ships under MIT to any host. A Skill whose
   purpose is "clone any app" hands every installer an infringement vector the
   pack cannot bound: the Skill cannot check who owns the target, what license
   it carries, or whether the user has permission.
2. **"Authorized" does not bound a generic Skill.** The reverse-skill repo
   labels itself authorized, but a Skill file has no way to verify authorization
   for a target it has never seen. A label is not a check.
3. **The legitimate uses are already owned.** Authorized security review of the
   user's own code is `development/security-audit`. Interoperability research
   on a named, licensed target is a one-off task with its own legal basis, not
   a reusable Skill.
4. **Star count is not a license.** `rea` is the most-starred repo in the
   author's whole star list; popularity does not change the IP analysis.

## What a future request must show

A clone/reverse Skill is reconsidered only when the request names all three:

- the target, and proof the user owns it or has written permission for it;
- the legal basis (own code, an explicit license, a bug-bounty scope);
- the defensive outcome (detect a clone, fix the user's own code, document an
  interface) — not "rebuild the app".

Without all three, the answer is no, and the refusal points here.
