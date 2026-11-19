---
name: quote-and-proposal
description: Turn job notes, a call transcript, photos, drawings or a client brief into a priced quote, estimate, proposal or statement of work with scope and exclusions. Not for grants or contract review.
---

# Quote and Proposal

## Use

Use when the user has to tell a client what they will do and what it costs: a quote for a job, an estimate, a proposal after a discovery call, a statement of work for a freelance or agency project.

A grant application or a formal public tender belongs to `sales/grant-and-rfp-bidding`. The client's contract paper belongs to `legal/contract-review`. What to charge for a product in general belongs to `product/pricing-and-paywall`.

## Domain inputs and blockers

- The discovery material: notes, transcript, photos, drawings, the client's brief.
- **The user's own past quotes or price list.** Prices come from comparable work this user has done, not from general estimates or industry averages.
- The user's standard terms and the deadline.

What must never be invented: labour rates, material costs, lead times, quantities estimated from a photo, a subcontractor's price, a discount. With no comparable job and no price list, that line is left as a visible blank and everything else is completed; say which number is needed.

## Extracting the job

- Read a transcript to the end; the useful part is often in the middle. Capture the client's own words for the problem (they go into the proposal), constraints mentioned in passing ("we can only get in after six" is a cost), who decides, hints about budget, and what they disliked about the previous supplier. A budget hint is checked for what it covered before it is used as an anchor.
- In a voice note, a number corrected mid-sentence takes its last value; an inaudible number is marked for confirmation.
- A photo can establish make and model, visible condition, access and obvious obstacles. It cannot establish dimensions without a reference object, what is hidden, or compliance with a code. Area estimated from a photo is the classic way to lose money on a job.
- On drawings, check the revision, date and scale in the title block first, take quantities from the schedule rather than by measuring, and carry "by others" and "not in contract" items into the exclusions.

Every gap has exactly two outcomes: ask, when the answer is quick to get and changes the price; or write the assumption into the client-facing text with its consequence in money ("ladder access assumed; a lift adds 1,800"). No silent guessing.

## Pricing

1. Find two or three past jobs similar in type, size and client, and show the arithmetic from them to this price.
2. If the derived price differs from the price list by more than about 15%, say which was used and why.
3. Break the price into items the client can make a decision about (equipment, electrical work, access, permits), not into "materials" and "labour" and not down to the screws. A client can remove an item; faced with one number they can only say it is too much.
4. At most two or three options, with the recommended one marked and one sentence of reason. Do not include a cheap option the user would not want to deliver.
5. Terms come from the user's past proposals. Otherwise propose conservative defaults for confirmation: a deposit of 30% to 50% (higher when materials are heavy), payment in 15 or 30 days, validity of 30 days, changes approved in writing. Terms weaker than the user's usual ones are pointed out to the user.

## The document

Ten parts, two to four pages for an ordinary job and one page for routine work with a known client:

1. header with the validity date;
2. what you asked for, in the client's words;
3. what we will do;
4. **what is not included** — the most valuable section: list what a reasonable client might assume is included; a few lines here prevent a whole dispute;
5. assumptions, in neutral language;
6. the price;
7. timeline, with what it depends on;
8. terms;
9. the next step, as one instruction the client can act on;
10. signature block.

No mission statement and no "why choose us". Use the user's own template when they have one; improvements are proposed separately.

## Output

To the user, before the document: the client and job in a line, the total and how it was priced, the comparable jobs it rests on, the open assumptions each with its money consequence, and what to know before sending. Then the client document.

Risk is written twice and never mixed: neutral assumptions in the client document, the frank worry in the note to the user.

Afterwards, record the outcome — won, lost or no reply — with the final price and the reason. A lost bid teaches more than a won one.

## Constraints

- Price, discount, schedule and subcontractor figures are the user's decisions.
- A document containing prices is not placed at a public address to make sharing easier.
- Nothing goes to the client without the user's explicit yes, given with the recipient, the total and what acceptance triggers in view.
