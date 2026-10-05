# Reading Ad Data

Read for an account audit, a judgement on search terms or small samples, or any statement that will be shown to a client or partner.

## Audit states

Each check ends in exactly one of four states: pass, fail, unknown (no evidence was seen) or not applicable. Report two figures and keep them apart:

- **Health** = passes ÷ checks that could be verified.
- **Coverage** = checks that could be verified ÷ checks that apply.

With coverage of 80% or more the audit is rated. Between 60% and 79% it is provisional: say so beside every score and list what was not verified. Below 60% report findings only, with no health figure.

Never counted against health: an unknown; a feature the account is not eligible for (record it as an opportunity to look into); not having adopted a new feature; a gap against a broad benchmark, which is a question, not a failure. A platform that could not be read is left out of the totals and named: "Google and Meta audited; LinkedIn not audited, no access".

## Benchmarks

Compare from narrow to broad, and stop at the first that exists: the same account, objective and window in the previous comparable period; the account's own experiments; revenue or CRM cohorts tied to spend; a peer sample whose method is disclosed; a broad industry benchmark, for direction only. Label a figure from a platform's or vendor's own marketing as vendor-supplied. Numbers under different attribution windows, conversion definitions or currencies are not combined unless normalized first, with the method stated.

## What zero conversions can prove

At 95% confidence, clicks with no conversion rule out only conversion rates above these levels:

| Clicks with zero conversions | Rates ruled out |
| --- | --- |
| 5 | none |
| 10 | 26% and above |
| 30 | 10% and above |
| 50 | 6% and above |
| 100 | 3% and above |

Before calling a keyword or an ad a failure, compute the break-even conversion rate = cost per click ÷ target cost per acquisition. If that rate is below what the clicks so far can rule out, the item is untested, not failed: say how many more clicks it needs and, at the current pace, by what date. "Let it run" always carries a date. One click with one conversion proves no more than five clicks with none.

## Search-terms reports

The report shows only part of the clicks, and the visible terms are a biased sample that favours common searches. For every conclusion compute the disclosure: disclosed clicks = clicks summed in the report; total clicks = campaign clicks in the same window; hidden = total − disclosed. Write "of the 33 clicks whose terms were disclosed, 13 were…", never "most searches were junk". Hidden terms cannot be recovered from site analytics. Pull the report unfiltered, since filtering on clicks drops the impression-only terms.

## Traps before any verdict

- Conversions are dated to the click, so "a sale came in today" and "the data shows the 11th" can both be true.
- A 30-day window is one slice of a longer history; ask how long the campaign has run and report both.
- If bids, keywords, budget, ads or targeting changed inside the window, it is not one experiment.
- A bid strategy that is still learning is not judged.
- A campaign or ad group name is a label; read the keywords.
- A "conversions" column may mix page views, trial signups and booked demos; split it by action.
- Change history fades with age; when an old change cannot be explained from the record, say so.

## Statements for someone else

Label each as **verified** (pulled in this conversation, unfiltered and reconciled to the total), **inferred** (reasoned from verified data) or **stale** (from a document, an earlier session or what the client said, with its date). Before sending, ask whether the client could disprove the sentence from their own account in a minute. State the limits first: disclosure share, sample size, configuration changes. When the client is right about an error, accept it once and plainly.

## Tracking before launch

A purchase event fires on confirmed payment, not on the button click; browser and server events share an identifier so they are counted once; internal traffic is excluded; test amounts are removed; where consent is required, it is collected before any tag fires; a pixel with no conversion action defined gives the platform nothing to optimize for. Always excluded from targeting: existing customers unless the campaign is an upsell, recent converters, visits of a few seconds, staff, and visitors to careers or support pages. A lookalike audience is seeded with the best customers, not all of them.
