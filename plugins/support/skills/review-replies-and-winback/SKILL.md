---
name: review-replies-and-winback
description: Reply to public reviews, turn reviews and order history into themes, and rank and message customers who have gone quiet. Use for reputation and win-back, not for answering a support ticket.
---

# Review Replies and Win-back

## Use

Use when the question is what customers are saying in public and who has silently left: summarising reviews into themes, drafting replies to good, bad, mixed or false reviews, explaining a falling rating, finding customers who stopped ordering, and writing the messages that invite them back.

A ticket, complaint or question sent directly to the business belongs to `support/customer-support-replies`. Cancel flows and save offers for a subscription belong to `product/onboarding-and-retention`.

## Domain inputs and blockers

- **Reviews**: an export from each platform is the best source, because it carries dates and ratings and includes what the public page hides. Text copied from a public page is partial (pages paginate, truncate and reorder); label it "web, partial" and ask for an export once.
- **Order or service history** per customer with dates and amounts. Without it, quiet customers cannot be ranked.
- **What the user can honour** for a returning customer: a discount, a credit, priority booking, a new service, or nothing but a sincere note. Ask before drafting; "nothing" is a valid answer and often the stronger first message.
- **A sample of the owner's own writing**, so replies sound like them.

A source that returns zero reviews is a valid result: record zero, name the source and continue. It is neither an error nor good news. When searching the user's inbox exports for feedback, search wide: customers write "took forever" and "never again", not "disappointed".

## Reading the reviews

- **Default window: 90 days.** Thirty days is empty for a business that gets six reviews a quarter.
- **Three to five themes.** Each has a one-line label, the number of signals behind it and two or three quotations with their source. Order themes by signal count, not by how loud one complaint is.
- **Quotations are verbatim.** A paraphrase cannot be traced and costs the report its credibility.
- **Ratings from different platforms are never averaged.** They come from different populations; a blended figure exists nowhere, and the owner may repeat it to customers. List each platform's rating separately and mark them "not averaged".
- **Behaviour changes weeks before reviews do.** From order data, look at: fulfilment time rising (give the figure for two periods), repeated refunds for the same product or the same time slot (three refunds on one product is a product problem, not three unhappy people), more split shipments, and the share of first-time buyers who never return. If refund reasons were not recorded, say they are unavailable.
- An open payment dispute has an evidence deadline set by the payment processor; it goes into this week's actions.

## Public replies

Readers of a reply are the next customers, not the reviewer.

- **Under 60 words.** Longer reads as arguing.
- **A negative review, in four moves**: name the specific thing that happened; say what has changed, only if something really has; give a real offline contact (a person's name and a phone number); stop. No defence, no quoting of policy, no "sorry you feel that way".
- **A positive review** gets a specific, human reply that thanks the customer for the particular thing they mentioned. A run of identical thank-yous shows readers the replies are automatic.
- **A mixed review** is answered on both halves; replying only to the praise looks like dodging the complaint.
- **A false or malicious review**: calmly correct one fact and stop.
- **Removal requests** are made only for a clear breach of the platform's own rules (wrong business, no transaction, a personal attack, a conflict of interest), checked against the platform's current policy. Tell the user that most requests are refused and that the platform decides.
- **Timing**: reply to a negative review within days; after a month it reads as damage control. A review the owner already answered gets no new draft.
- When the owner rewrites a draft to make it truer, keep their wording as a voice note for later replies.

## Quiet customers

1. **Check the date field before computing anything.** If a date filter returns nearly every order or none, or the dates cluster on one or two days, a bulk import stamped the import date on old orders. Use the processing date or the customer-level order history, and say which field was used.
2. **Quiet is measured against the customer's own rhythm.** With three or more orders, the normal gap is the median gap between that customer's orders. Quiet means the current gap exceeds twice that; lost means three times. With fewer than three orders, use the median across the business and mark the result as an estimate.
3. **Rank by past value, not by length of silence**: lifetime spend, then order frequency, then size of the latest order, using whichever the data supports and saying which. Fifteen names the owner will really contact are worth more than two hundred.
4. **A customer who left a bad review and then stopped ordering goes to the top regardless of value.** The cause is known, which makes them the most recoverable.
5. **A quiet customer with an unresolved ticket** is not a mystery; they go on the owner's phone list, not into a message sequence.

## Win-back messages

One message is the default, and follow-ups are earned by value.

| Customer | Approach |
| --- | --- |
| High value, left a bad review | A phone call from the owner. No offer first; the apology is the offer |
| High value, no complaint | A personal note from the owner that mentions their last order. If there is no reply, up to two follow-ups within four weeks |
| Medium value, seasonal buyer | One well-timed reminder, no discount |
| Low value, bought once | One low-cost offer, then stop |

The reason for the tiers: a second and third unanswered message cost goodwill and deliverability, which is acceptable only where a single returning customer is worth a great deal; a complaint is never answered with a sequence at all.

When a sequence is used: the first message does not sell, it acknowledges the gap and asks what happened; the second says what has changed since; the third gives one specific, time-limited reason to return, and any offer appears only there. Each message stays under 90 words.

**Any reply ends the sequence**, including a complaint and an out-of-office notice (resume only after its return date). A complaint goes to a person at once and is never followed by a pitch.

## Output

1. **Header**: date range, each platform's rating and direction, review counts, from pulled data only.
2. **Sources**: each source with its count, including zeros and failures by name.
3. **Themes**: label, signal count, quotations.
4. **Reviews awaiting a reply**, oldest first, each with its draft and the choice send, edit or skip.
5. **Quiet customers**: a table of customer, normal gap, current gap, lifetime value, note and suggested approach, then the message drafts as copyable blocks, with the offer and tone stated once above them.
6. **Three things to do this week**, tied to the largest theme.

A request for only one of these gets only that part.

## Constraints

- A public reply cannot be taken back, so each one is approved individually by the user; approving several at once is how a wrong reply goes live.
- Approving the first win-back message does not approve the later ones; each send is confirmed with its count, recipients and sending account.
- Do not promise a refund, discount or credit the user has not confirmed, and do not promise that a review will be removed.
- Do not invent a policy change to make a reply sound better.
- Win-back messages are marketing messages: consent and unsubscribe requirements depend on the customer's country and are confirmed by the user before sending.
