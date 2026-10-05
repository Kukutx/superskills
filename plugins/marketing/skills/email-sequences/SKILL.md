---
name: email-sequences
description: Design automated email sequences such as welcome, onboarding, nurture, re-engagement, win-back and launch flows with timing, branching, exit rules and full copy. Not for one-off emails or SMS.
---

# Email Sequences

## Use

Use when the deliverable is a series of emails sent automatically after a trigger: welcome, onboarding, lead nurture, re-engagement, win-back, product launch, event follow-up, upgrade, an educational drip, or the emails of a referral programme.

A single email to a person belongs to `writing/business-email`. What happens inside the product after signup, and the cancel flow, belong to `product/onboarding-and-retention`. Text messages belong to `marketing/sms-marketing`. A newsletter issue or other one-off broadcast belongs to `writing/marketing-copy`.

## Domain inputs and blockers

- **The trigger** that puts someone in the sequence, and **the conversion** that takes them out. Without a definition of "converted" there is no exit rule, so settle it first; when the user has not said, propose one and mark it as an assumption.
- What the reader already knows and which stage they are in; what other emails they receive in the same weeks; how past emails performed.
- Optional: number of emails, cadence, brand voice, an offer, assets, product features to show.
- There is no connection to an email tool. Deliver copy that can be pasted, plus the build order: create the automation, set the entry trigger, add each email with its delay, configure branches and exits, set up tracking. Segment sizes, deliverability and live results were not checked unless the user pasted them.

## Sequence design

Decide the architecture before writing any email: the narrative arc across the series, the stage each email serves (awareness, consideration, decision, activation, expansion), how the ask escalates, and what success is.

Working defaults for size and span; start at the low end and add an email only when it has a job no other email does:

| Sequence | Emails | Span |
| --- | --- | --- |
| Welcome | 3–7 | first email immediately, then 1–2 days apart |
| Onboarding | 5–7 | 14–21 days |
| Lead nurture | 4–6 | 3–4 weeks |
| Re-engagement | 3–4 | 10–14 days, triggered after 30–60 days of inactivity |
| Win-back | 3–5 | 30 days |
| Product launch | 4–6 | 2–3 weeks |
| Event follow-up | 3–4 | 7–10 days |
| Upgrade | 3–5 | 2–3 weeks |
| Educational drip | 5–8 | 4–6 weeks |

A re-engagement series runs in this order: a check-in, a reminder of the value, an offer, and a last email that asks the reader to stay or unsubscribe.

**Logic every sequence defines:**

1. **Branches.** At least: opened but did not click gets a softer variant; clicked the main action skips ahead.
2. **Exit.** Converting removes the reader immediately; nobody is sold something they just bought.
3. **Re-entry.** For example, a customer who lapses again after 90 days may enter win-back once more.
4. **Suppression.** Do not send to someone who is in another active sequence, has unsubscribed from marketing, or contacted support in the last 48 hours.

Onboarding emails support the in-product onboarding and do not repeat it: the email sends the reader back to the step they have not finished.

**Referral emails.** Ask at a moment of proven value: after the first success with the product, after a milestone, after a good support experience, after a renewal or upgrade. Pay the reward when the referred person reaches their own first success or milestone, not at signup, and verify and cap rewards so the programme does not pay for fake accounts. A two-sided reward (both people get something) is the starting hypothesis, and whether to state the reward as an amount or a percentage is something to test. A working shape is an announcement followed by reminders around days 7, 30 and 60.

## Each email

- **One job and one primary action**, stated in a sentence before the copy. Value comes before the ask.
- **Timing**: a delay from the previous email or an event, and the condition under which it is sent.
- **Two or three subject lines** from different angles (curiosity, benefit, urgency, personal, question). Keep them under about 50 characters; clear beats clever; each must make sense to someone who reads nothing else.
- **Preview text** that adds to the subject instead of repeating it. Recommended lengths vary from 40 to 140 characters, so put the point first and check how the user's tool renders it.
- **Body**: hook, substance, action; paragraphs of two or three sentences; scannable. Length by purpose, as working defaults: transactional 50–125 words, educational 150–300, story-led 300–500.
- **Segment and exit conditions** for this email.

Wording to keep out, because readers recognize it as automated: a fake "Re:" or "Fwd:"; "I hope this email finds you well"; "Just checking in"; a closing "let me know if you have any questions"; "It's not X, it's Y" contrasts; "no X, no Y, no Z" stacks (one true "no card required" is fine); a question answered by the next sentence or a reveal after a colon; "Say goodbye to" and "Unlock the power of"; dashes in the subject or preview.

## Measuring and testing

Definitions, stated in the plan because tools differ: open rate = unique opens ÷ delivered; click rate = unique clicks ÷ delivered; click-to-open rate = clicks ÷ opens; plus unsubscribe rate, bounce rate and delivery rate. Each email is judged on its own job, and the sequence on the conversion that defines its exit.

No benchmark table is given: the published ones are unsourced and contradict each other. Compare an email with the rest of its sequence and with the user's earlier sends. Two working alarm lines for onboarding and nurture mail are an unsubscribe rate above about 0.5% and a bounce rate above about 2%. Re-engagement and win-back series run higher unsubscribe rates (1% to 3% as a working allowance), which is partly the list cleaning itself.

Propose two or three tests, each with what changes, how the audience is split and what decides the winner. One variable per test, the metric chosen first, the sample size worked out first, and at least one full business cycle before reading it.

## Law and consent

For commercial email to recipients in the United States, the FTC's CAN-SPAM compliance guide (read October 2026) requires: accurate "From", "To" and routing information; a subject line that is not deceptive; identification of the message as an advertisement; a valid physical postal address; a clear way to opt out that works for at least 30 days after sending; opt-outs honoured within 10 business days, with no fee and no information demanded beyond the email address; and responsibility for anything a third party sends on the sender's behalf. It makes no exception for business-to-business email. Transactional and relationship messages are exempt from most of it. Penalties are counted per email; take the current amount from the FTC guide.

Other countries have their own rules, including on whether prior consent is needed; they were not verified here. Before a sequence goes live, the user checks the law where the recipients are. Every draft carries an unsubscribe line and a postal-address placeholder.

## Output

1. **Overview table**: number, subject line, purpose, timing, primary action, condition.
2. **Every email in full**: subject options, preview, body, action and its destination.
3. **Flow as text**: trigger, branches, exits, re-entry and suppression.
4. **Tests**, **metrics to track** with a review date, and **the build order** for the user's tool.
5. Assumptions made and the legal checks left to the user.

## Constraints

- Do not invent discounts, deadlines, features, customer results or quotations; an offer that was not supplied is a placeholder.
- A deadline or "last chance" in the copy matches a real one.
- Do not present an open-rate or conversion benchmark as an industry fact.
- This is not legal advice. A statement that a sequence "is compliant" is not made; the checks above are listed for the user or their counsel.
- Do not write a sequence that makes unsubscribing hard to find or keeps mailing people who opted out.
