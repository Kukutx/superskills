---
name: crisis-communications
description: Handle a public crisis such as a data breach, outage backlash, billing error or viral complaint by tiering it, deciding who hears first and writing the holding statement. Not for the technical fix.
---

# Crisis Communications

## Use

Use when something has gone wrong and people outside the company know or are about to: a breach, a long outage that customers are angry about, a billing or pricing mistake, a customer's bad experience spreading online, a marketing claim called out as false, news leaking early.

Running the technical incident, its internal updates and the postmortem belongs to `operations/incident-response`. A reply to one customer belongs to `support/customer-support-replies`. A reply to a public review belongs to `support/review-replies-and-winback`.

This prepares wording and sequence. It does not decide what the company may legally say.

## Domain inputs and blockers

What is confirmed, as opposed to suspected; who is affected and how many; what has already been said, by whom and where; who can approve a statement. A statement is built only from confirmed facts. A fact that is not yet known is not guessed at to fill the page.

## Tier it first

| Tier | Example | Response |
| --- | --- | --- |
| 1 contained | a bug in one feature, an isolated complaint | support answers directly; no public statement |
| 2 visible | degraded service, complaints gathering, a claim called out | public acknowledgement on the status page or social account, owned by the support or marketing lead |
| 3 significant | a full outage, a widespread billing error, a customer's story spreading widely | a formal statement reviewed by leadership, with one named spokesperson |
| 4 severe | a data breach or security incident, misconduct by a leader, a safety problem, a regulator's inquiry | a statement reviewed by a lawyer, an executive spokesperson, a dedicated incident page, and possibly a legal duty to notify |

When unsure between two tiers, take the higher: under-reacting to a tier 3 looks worse than over-reacting to a tier 2.

## Who hears, in what order

1. The people affected, directly, by email or inside the product; staff are told in parallel.
2. The status or incident page: the one place the company controls and can link to.
3. The company's own social accounts, as a short post linking to the full statement, because a statement squeezed into a post reads as evasive.
4. The press last, unless a journalist is already asking, in which case they get a direct answer.

The press never learns before affected customers do. Getting the order wrong creates a second crisis.

## Writing the statements

**A holding statement**, when the facts are still coming in: acknowledge the specific problem, say that it is being investigated, and give a specific time for the next update. It says nothing about cause, scope or who is affected, and it goes out with no placeholders left in it. "No new information; next update at four" beats silence.

**The full statement** says what happened first, then what it meant for customers, then what is being done, in plain language. Long background before the event reads as defence.

- An apology has no "but". Before a lawyer has cleared it, the company can acknowledge the problem and its effect; it does not assign a cause it cannot yet prove.
- The legal position and the public statement are two documents. The lawyer decides what may be said; the statement says it the way a person would. Phrases such as "the company denies any wrongdoing" stay out of a message to customers.
- Not done: silence; deleting criticism, which gets screenshotted and becomes a story about a cover-up; the non-apology ("we are sorry if anyone was affected"); speculation.

## First move by kind of crisis

| Crisis | First move | Trap |
| --- | --- | --- |
| data breach | bring in the lawyer before saying what was or was not exposed | "no sensitive data was affected" is the sentence most often taken back; wait for the security team to confirm it |
| outage | update the status page within minutes | a promised fix time that was a guess; give the time of the next update instead |
| misconduct by a leader | legal and the board first | speed; being right matters more here |
| a customer's story spreading | contact the customer privately before replying in public | arguing facts in a comment thread |
| billing or pricing error | establish how many customers and how much, then refund or credit before being asked | a refund extracted by public pressure reads as defeat |
| news leaking early | bring the internal announcement forward | letting staff learn from outside |
| a marketing claim called out | name the sentence, correct it, say how it is being fixed | defending the intention |

## Afterwards

Tier 3 and 4 get a public review: what happened, the root cause, and specific changes that can be checked; "we take this seriously" says nothing. The internal review is a separate document. Every repair, credit or policy change promised in a statement is tracked and reported back when done. Watch the conversation for another week or two, since a new detail can start a second wave.

## Output

The tier with its reason; the order of audiences with who sends what; the holding statement; the full statement and its short social version; the questions that must be answered before the next update; and the list of promises to track.

## Constraints

- Notification duties after a data incident, and their deadlines, differ by jurisdiction and kind of data. No deadline is stated here; a lawyer confirms what applies.
- Nothing about cause, scope or affected people is written before it is confirmed.
- Do not draft a statement that shifts blame to a customer, a supplier or an employee.
- A statement is a draft until the person with authority has approved it.
