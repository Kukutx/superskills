---
name: contract-review
description: Review a contract, agreement or terms clause by clause, flag risky terms, and propose redlines with fallbacks before signing. Use for vendor, client, SaaS or freelance contracts, not for an NDA alone.
---

# Contract Review

## Use

Use when the user has an agreement to sign or negotiate and wants to know what is risky, what to push back on and what to ask for instead.

A stand-alone confidentiality agreement goes to `legal/nda-triage`. Whether a feature or data practice is lawful goes to `legal/privacy-compliance-check`. Writing the email that carries the redlines goes to `writing/business-email`.

This is a first-pass review for someone who is not a lawyer. It does not replace advice from a qualified lawyer in the governing jurisdiction, and every review ends by saying so.

## Domain inputs and blockers

- **Which side the user is on** (customer or supplier, licensor or licensee). The same clause is good for one side and bad for the other; when it cannot be read from the document, ask before judging.
- **What the deal is worth and how long it runs**, because exposure is judged against it.
- **Governing law.** Default positions below follow common commercial practice, mostly from US contracts; say so, and treat any other jurisdiction as a reason to flag for local advice.

Read the whole document before flagging anything: clauses change each other's meaning (an indemnity can sit outside the liability cap, a survival clause can extend a term).

## Clauses to check

Limitation of liability, indemnification, intellectual property, data protection, confidentiality, warranties, term and termination, governing law and disputes, insurance, assignment, force majeure, payment.

The traps that matter most:

- **Liability**: a cap far below the contract value; carve-outs that apply to one side only; "breach of section X" exclusions that swallow the cap; indirect damages excluded for one party only.
- **Indemnity**: covers "any breach" rather than third-party claims; one-way although both sides contribute IP; no right to control the defence; survives without end. Check whether it is inside or outside the cap.
- **IP**: an assignment broad enough to take pre-existing work; "work for hire" reaching beyond the deliverables; a perpetual, irrevocable licence to feedback.
- **Data**: personal data without a data processing agreement; no notice of subprocessors; breach notice slower than the law allows; no deletion at the end.
- **Term**: auto-renewal with a short notice window; a long term without termination for convenience; termination without a cure period; payment terms that slip (late fees, price increases on renewal).

- **Money**: convert a liability cap into an amount before judging it ("three months of fees" may be a few hundred), and treat payment terms much longer than 30 days as a negotiating point.

## Flagging

- **Green**: standard, acceptable as written.
- **Yellow**: outside the user's interest but negotiable. Give the redline, a fallback position and the business impact of accepting it.
- **Red**: unusual or dangerous. Explain the risk, what is normal in the market, the exposure, and that it needs a decision from someone with authority or a lawyer.

To rank the issues, rate each for severity and likelihood from 1 to 5 and multiply: 1–4 low, 5–9 medium, 10–15 high, 16–25 critical. A catastrophic outcome stays on the list whatever its likelihood.

A redline is written in a fixed shape so it can be sent on: the clause, the current wording, the proposed wording, a rationale the other side can read, its priority, and the fallback. Keep redlines balanced; demands that ignore the counterparty's position slow the deal down.

A clause that should be there and is not is flagged as missing. Standard boilerplate is not flagged, since noise hides the real issues. Work out the date by which an automatic renewal must be cancelled and give it to the user. Pitch the redlines to the counterparty's size: against a large company's standard paper, propose the compromise most likely to be accepted and mark what was conceded.

Negotiate in tiers: must-haves first, trade the nice-to-haves for the important ones, and never give up a must-have silently.

## Output

1. **Summary**: what the agreement is, which side the user is on, the overall verdict, and the three issues that matter most.
2. **Clause table**: clause, flag, issue, proposed change.
3. **Redlines** for the yellow and red items.
4. **Before signing**: final version has no open markups, all exhibits are attached, the legal names of the parties are correct, dates and signature blocks match the authorized signers. A wrong legal entity name is the most common mistake.
5. **What needs a lawyer.**

A long contract gets the key clauses first, then the full pass. Ask whether a translation is needed before reviewing a contract in another language.

## Constraints

- Litigation in progress, a government inquiry, possible criminal exposure, securities matters and anything the board must approve go to a lawyer, not into a redline.
- Do not state that a clause is enforceable or unenforceable; say what it would mean if enforced.
- Do not invent terms the document does not contain; quote the wording being discussed.
- Do not soften a red flag because the user wants to sign.
