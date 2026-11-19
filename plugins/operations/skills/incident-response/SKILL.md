---
name: incident-response
description: Run a production incident from severity triage through status updates to a blameless postmortem with timeline, root cause and action items. Use for an outage or its write-up, not one bug.
---

# Incident Response

## Use

Use when a live service is broken or degraded and the work is to manage it: decide how serious it is, tell people what is happening, keep the timeline, and afterwards write what happened and what will change.

Finding the technical cause of one failure belongs to `development/bug-diagnosis`. The check before a release belongs to `operations/release-checklist`. Replying to one affected customer belongs to `support/customer-support-replies`. The public side of a serious incident, such as a breach statement or an apology, belongs to `operations/crisis-communications`.

## Domain inputs and blockers

Which stage this is — a new incident, an update during one, or the postmortem — is usually clear from the message; ask only when it is not. Work from the alerts, logs and chat the user pastes. Start writing with whatever is known: a first update that says little but is on time beats a complete one that is late.

There is no paging, no war room and no monitoring here. Say what the user has to trigger themselves.

## Severity

| Level | Situation | Respond |
| --- | --- | --- |
| SEV1 | service down, all users affected | immediately, everyone available |
| SEV2 | a major function degraded, most users affected | within 15 minutes |
| SEV3 | a minor function affected, some users | within an hour |
| SEV4 | cosmetic or low impact | next working day |

The response times suit a team with on-call cover; a solo developer keeps the levels and sets times they can actually meet. An incident that exposed or lost personal data adds a question the team may be legally required to answer: whether users or a regulator must be notified, and by when. That question goes to whoever owns privacy or legal, at once.

## During the incident

- Every update has four parts: what happened, who is affected, what is being done, and when the next update comes. Then it comes at that time, even if nothing changed.
- Status is one of: investigating, identified, monitoring, resolved. Resolved is declared only after recovery has been confirmed, not when a fix has been deployed.
- Updates state what is known and what has been done. A suspected cause is labelled as suspected or left out.
- Internal updates and customer-facing messages are separate texts. The customer version has no internal names, no blame and no promise of a time that has not been confirmed.
- Keep a running timeline with times in UTC: detection, each action, each change of status. It is the raw material of the postmortem and cannot be rebuilt reliably from memory.
- Roll back when a rollback condition that was agreed before the deploy is met. If none was agreed, decide on user impact now, not on how close the fix feels.

## Postmortem

Blameless: it describes how the system and the process allowed the failure, not who made it.

1. Summary in two or three plain sentences.
2. Impact: who, for how long, and what it cost in measurable terms.
3. Timeline in UTC.
4. Root cause, reached by asking why until the answer is a condition that can be changed, not a symptom or a person.
5. What went well and what went poorly, including detection and communication.
6. Action items, each with an owner, a priority and a due date. An item without an owner will not happen.
7. What was learned.

## Output

- **New incident**: severity with the reason, the first status update, the immediate actions, and what to watch.
- **Update**: the status message in the four-part form, plus the timeline so far.
- **Postmortem**: the document above. Gaps in the supplied timeline are marked as gaps.

## Constraints

- Do not state a cause, a number of affected users or a recovery time that the evidence does not show.
- Do not name an individual as the cause.
- Do not write "resolved" for the user to send before they have confirmed recovery.
- Legal notification duties after a data incident are confirmed with a lawyer, not inferred here.
