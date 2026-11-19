---
name: sms-marketing
description: Plan SMS or WhatsApp marketing such as cart recovery and promo texts with consent, opt-out, quiet hours and message-length checks. Use for text-message marketing, not for email sequences.
---

# SMS Marketing

## Use

Use when a shop or app wants to market by text message: deciding whether SMS is the right channel, cart-recovery and browse-recovery texts, promotional sends, post-purchase and win-back texts, the opt-in wording, WhatsApp campaigns, and checking a planned message for length and compliance gaps.

Email flows belong to `marketing/email-sequences`. Privacy law in general (data rights, policies, processors) belongs to `legal/privacy-compliance-check`.

Text marketing is regulated and mistakes are expensive. Every answer starts with the compliance check and only then turns to strategy. This Skill is an orientation for a non-lawyer; the rules differ by country and by state, and a lawyer confirms compliance before the first send.

## Domain inputs and blockers

- **Where the recipients are.** This picks the legal regime and is asked first.
- **How people opted in**: the exact wording they saw, where, and whether a record exists. A list with no provable opt-in for marketing texts blocks the plan; say so and design the opt-in instead.
- **The sending platform and number type**, and for US ten-digit numbers whether the brand and campaign are registered.
- **Business type, margin and list size**, which decide the flows and whether discounts are affordable.

Registration status, deliverability and real opt-in data cannot be checked from here; they are reported as stated by the user, not verified.

## Compliance gate

**United States.** Read from the FCC's rule at 47 CFR 64.1200 in the Code of Federal Regulations edition revised 1 October 2025; confirm against the current text on eCFR before relying on it.

- Advertising or telemarketing sent to a mobile number with an automatic dialing system requires the recipient's **prior express written consent**. Whether a given platform counts as such a system is a legal question; plan for written consent unless a lawyer says otherwise.
- That consent is a signed written agreement that clearly authorises the seller to send marketing by such a system, and it must state that agreeing is **not a condition of buying** anything.
- **Quiet hours**: no solicitation before 8 a.m. or after 9 p.m. in the recipient's local time, and the rule applies these limits to text messages to mobile numbers. Whether the recipient's state sets a narrower window is checked separately; 9 a.m. to 8 p.m. recipient time is a safer working default.
- **Opt-out**: consent can be withdrawn by any reasonable method. A reply of "stop", "quit", "end", "revoke", "opt out", "cancel" or "unsubscribe" counts by definition. The request is honoured within a reasonable time that may not exceed ten business days; in practice, process it immediately and automatically.
- One text confirming the opt-out is permitted if it only confirms.
- The sender identifies itself: the name of the business and a phone number or address where it can be reached.

**Practices to confirm with the sending platform**, because they come from carrier and industry requirements rather than from the regulation: the opt-in disclosure usually names the programme, the expected message frequency, how to stop and get help, that message and data rates may apply, and links the terms; a "help" reply returns the brand name, how to stop and a support contact; every promotional message carries the opt-out instruction.

**Keep for every subscriber**: the time of consent, where it was given (the page), and the exact wording shown.

**Consent in practice.** The disclosure sits next to the phone field and the submit button, not in a footer, and matches both the sample messages registered with the carriers and what is actually sent. A phone number given at checkout covers messages about that order; it is not consent to marketing, and a transactional message carries no promotion. When sending to several countries, apply the strictest standard, record where each consent was given, and identify the sender in every message.

**Ten-digit numbers in the US (10DLC).** The Campaign Registry describes 10DLC as a channel in which brands and their messaging providers are verified before they are allowed to send, with registration done through the provider. Take the registration steps, the consequences of sending unregistered and the rule on sample messages from the provider's and the registry's current pages.

**Other countries.** Not stated here. For each market, find out from the regulator's own pages: what form of opt-in is required and whether a pre-ticked box counts, what sender identification each message needs, whether every message must carry an unsubscribe route, and whether consent implied by an existing customer relationship expires.

**WhatsApp.** From Meta's WhatsApp Business messaging policy and pricing pages (policy last updated 23 September 2026):

- A business may message a person only after that person gave their number and opted in to receive messages from it.
- A conversation is started only with an approved message template. Free-form replies are allowed inside the 24-hour customer service window, which opens and resets with each message from the user.
- Templates fall into marketing, utility and authentication. Plan cart reminders and promotions as marketing unless Meta's current template guidelines place them elsewhere. Marketing templates are charged per delivered message; current rates are on Meta's pricing page.
- Every request to stop is respected.
- Whether marketing templates are delivered to numbers in a given country is checked in Meta's current documentation before planning a WhatsApp campaign for that country.
- A template that mixes an order update with a promotion counts as marketing, and so does a cart reminder the customer asked for. Consent for order messages and for promotions is collected separately or named as two categories in one consent. Variables in a template need realistic sample values; vague samples are a common reason for rejection.
- Each marketing template offers a way to stop promotions; a person who uses it is marked at once and receives one confirmation and no further marketing, while order messages they separately agreed to may continue. Where blocking is the only way to stop, the sender's quality rating suffers.
- A new number is warmed up: verify the business, send first to recent buyers and people who wrote in, raise volume over a week or two and spread large sends over hours. One or two marketing messages a month per person is a sensible ceiling.

## Channel fit and flows

**If the message can wait 24 hours, send an email.** Text fits abandoned carts, shipping updates, time-limited promotions, codes and post-purchase offers. A welcome series is led by email with a text in support; education and newsletters are email; win-back uses both.

Working timings, to be replaced by the user's own results:

| Flow | Timing |
| --- | --- |
| Abandoned cart | 30 minutes: reminder, no discount. 4 hours: gentle urgency and proof. 24 hours, optional: a discount, only if the margin allows |
| Abandoned browse | 1 hour |
| Post-purchase | Order confirmation at once (transactional); two days after delivery, a review request and a related product |
| Win-back | At 60 to 90 days; 14 days later an offer; 14 days later a last message |
| Promotion | One or two texts per campaign, on different days from the campaign emails |

A discount in the first cart message teaches customers to abandon carts on purpose.

**Every flow states who leaves it and who never enters.** A cart flow stops on purchase, on opt-out or after about two days; low-value carts and people who abandon repeatedly to collect discounts are excluded; a browse flow needs real browsing behind it and stops if the person buys something else. Someone inside a flow receives no promotional send on top of it, and a customer who just bought with a discount is left alone for a couple of weeks. A replenishment text goes out shortly before a consumable is due to run out.

**Unsubscribes rising** is diagnosed in order: frequency, relevance (was the whole list sent the same message), then segment by engagement, recency of purchase and source of the subscription. Subscribers silent for two months get one soft message and then a "reply YES to stay" message; no answer means suppression. After a full win-back attempt with no response, stop sending.

The number type (a registered ten-digit number, a toll-free number or a short code) follows from the throughput the list needs and the cost, which the provider quotes; a short code is for large, steady volumes. Before choosing a platform, confirm how it handles brand and campaign registration, whether sample messages must match what is sent, the description of the consent flow given to carriers, stop and help keywords, quiet hours by the recipient's time zone, the suppression list, and how long timestamped consent records are kept. Registrations are commonly rejected for samples that differ from real messages, a consent screenshot without the disclosure, and a vague campaign description.

## Writing the message

- Start with the brand name, so the recipient knows who is writing.
- One call to action and one short link carrying campaign tags. At most one emoji, and only when it is worth the extra segments; text pasted from a word processor brings curly quotes and long dashes that silently switch the whole message to the shorter encoding.
- **Length**: a message in the basic GSM character set fits 160 characters in one segment; beyond that it is billed as more than one. A single emoji, accented letter or curly quotation mark switches the whole message to an encoding with 70 characters per segment. State the character count and the segment count of every draft, and tell the user to confirm with the platform's own counter.
- A picture message is priced above a text; get the provider's current rate before planning one.

## Output

Six parts, in this order:

1. **Compliance check**, with blockers first: consent basis, opt-in wording, opt-out handling, quiet hours, registration, and what could not be verified.
2. **Strategy**: which flows to build first and why.
3. **Sequences**: trigger, delay, the text with its character and segment count, the call to action, the segment it goes to.
4. **Number type and platform questions** to settle with the provider.
5. **Measurement**: opt-in rate from the email list, click rate, conversions per message and opt-outs per message, compared with the user's own earlier sends. Published benchmarks for these have no reliable source.
6. **Compliance texts**: the opt-in disclosure, the opt-out confirmation and the help reply, marked for legal review.

## Constraints

- Do not call a plan compliant. State what was checked, against which source, and that a lawyer confirms it.
- Do not treat a purchased list, an email opt-in or an existing customer relationship as consent for marketing texts.
- Do not state a legal requirement for a country or state that was not checked on an official page in this conversation; write it as a question to confirm.
- Do not quote carrier fees, throughput limits or message prices; they change and are the provider's to quote.
- Do not draft a text that hides the sender, omits the way to stop, or is timed outside the recipient's quiet hours.
