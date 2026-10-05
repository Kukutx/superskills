---
name: nda-triage
description: Screen an incoming NDA or confidentiality agreement as safe to sign, needs changes or do not sign, checking carve-outs, term, residuals and hidden non-compete clauses. Not for full contracts.
---

# NDA Triage

## Use

Use when a non-disclosure agreement arrives and the question is whether to sign it as it is.

First check that it really is only an NDA. A document that also contains exclusivity, a non-compete, an IP assignment or commercial obligations is not an NDA whatever its title; it is a contract and goes to `legal/contract-review`.

This is a screen for a non-lawyer, based on common commercial practice. It does not replace a lawyer, and the result says so.

## Domain inputs and blockers

Which party the user is (disclosing, receiving or both) and why the NDA exists (a sales conversation, a hire, a partnership, an acquisition). An NDA with a competitor, in an acquisition context, or covering unusual data such as biometric data or data for model training is escalated to a lawyer regardless of how standard it looks.

## What a standard NDA looks like

- Mutual, when both sides will share information.
- A term of one to three years, with confidentiality surviving two to five years; trade secrets may be protected for as long as they remain secret.
- Confidential information is defined as what is marked or what a reasonable person would understand to be confidential.
- All five standard carve-outs are present: already public, already known to the receiver, independently developed, received lawfully from a third party, and disclosure required by law.
- Return or destruction at the end, with an exception for copies kept for legal, compliance or backup reasons.
- Injunctive relief is acknowledged; there are no liquidated damages.

## Classification

**Green — sign**: every point above holds.

**Yellow — sign after changes**:
- a definition that is too broad: narrow it to marked information, with oral disclosures confirmed in writing within 30 days;
- a term somewhat longer than usual;
- a missing carve-out that is easily added;
- a narrow residuals clause;
- small asymmetries, a non-preferred governing law, or return without the retention exception.

**Red — do not sign as written**:
- one-way when it should be mutual, or the wrong direction entirely;
- no independent-development carve-out (the other side could later claim the user's own product came from their information) or no compelled-disclosure carve-out;
- a non-solicit, non-compete, exclusivity or standstill clause. These do not belong in an NDA: delete them, and if the other side insists, limit a non-solicit to targeted solicitation for 12 months;
- a term of ten years or more, or perpetual. Replace with two to five years plus continued protection for trade secrets;
- a broad residuals clause. The floor is: general ideas retained in unaided memory only, excluding trade secrets and patentable material, and granting no licence;
- a hidden licence or assignment of IP, liquidated damages, audit rights without limits, or mandatory arbitration in an unfavourable venue.

Anything between the yellow and red examples is judged by what it exposes, and the reasoning is stated.

## Output

The classification, a screening table (item, what the document says, verdict), each issue as what it is, why it is a risk and the suggested fix, and the recommended action: sign, send back with the listed changes, or get a lawyer involved.

## Constraints

- Quote the clause being judged; do not characterize wording that was not read.
- Do not call an NDA standard when a carve-out is missing.
- Do not negotiate away the independent-development carve-out to close faster.
