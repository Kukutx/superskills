---
name: company-tear-sheet
description: Write a one or two page company profile tailored to its reader (investor, deal team, acquirer or salesperson) from supplied financials, with arithmetic checks. Use for 公司一页纸, not a stock thesis.
---

# Company Tear Sheet

## Use

Use when the deliverable is a compact profile of one company for a particular reader: an investor's snapshot, a profile for a deal team, a briefing on an acquisition target, or a sheet to read before approaching a customer.

A thesis on a listed company and its results belongs to `finance/stock-research`. What it is worth belongs to `finance/company-valuation`. Deciding whether to buy it belongs to `finance/deal-diligence`. The plan for a specific meeting belongs to `sales/sales-call-prep-and-recap`.

## Domain inputs and blockers

- **The reader.** Investor, deal team, acquirer or salesperson. If the user has not said, ask: it decides what stays on the page.
- **The data**: filings, the latest results and call, peers' figures, deals. Everything comes from what the user supplies or a source opened in the session, with its date. What is not there is written "N/A" or "Not disclosed", never filled from memory and never silently dropped.
- What the user sells, only if they mention it.

## Rules for every sheet

1. State the fiscal year end and do not assume it is the calendar year. A market value carries its "as of" date. Fiscal-year and last-twelve-month figures are not mixed in one column.
2. Take four years to show three: the fourth exists only to compute the earliest year's growth, which otherwise shows as a gap.
3. Use a figure the source already reports (net debt, EBITDA, free cash flow) before calculating one. The same data point is identical across every sheet made for the company.
4. **Check the arithmetic before publishing**: gross margin is gross profit over revenue; growth is the change over the earlier period; segments add up to total revenue, and if they do not, leave out the total row; shares add up to about 100%; a quoted multiple agrees with the value and the metric shown beside it. A figure that fails the check is replaced by "N/A".
5. A segment's share is measured against consolidated revenue, not the sum of segments, which is often larger because of internal sales.
6. Derived measures: free cash flow conversion is free cash flow over EBITDA; net debt is total debt less cash; then net debt to EBITDA, and research and capital spending as shares of revenue.
7. Multiples are labelled by period, last twelve months or next twelve months, and both appear when the forward data exists.
8. A known deal value is never written as "Undisclosed"; that word is only for a value the source really lacks. Deal values get their own column.
9. Executives are listed only when the source lists them.
10. The description is rewritten for the reader, not pasted from a database, and the same results call yields different points for different readers.
11. The sections of judgement are where the value is: connect the data into an argument instead of listing names.
12. An announced disposal is marked in the segment table, with revenue and mix restated without it.
13. **A private company** has no share price, trading range, consensus or trading multiples: say "Private company" at the top and give the space to the business, its relationships and its ownership.
14. Format: units in the column heading and no currency sign in the cells; negatives in brackets; percentages to one decimal; real year labels ("FY2023"), not relative ones.

## By reader

**Investor.** One page; density is the standard. A valuation table with both periods (earnings, enterprise value to EBITDA and to revenue, price to free cash flow, dividend yield). Guidance, when given, is the first result line. A beat or miss is stated only when a consensus figure was supplied; otherwise give the absolute figure and growth. Attribute views to management ("management highlighted…"). Capital structure sits in its own small table. Share-price performance is the least valuable part and the first cut.

**Deal team.** The business overview reads like a pitch: how revenue is earned (recurring or transactional), the scale of customers, the named source of defensibility. Add a last-twelve-months column to the three years. Comparable valuation carries a row per peer, the peer median and the operating measures (growth, margin) beside the multiples. Each relationship carries a note saying what it is; a bare name is useless. When over two pages cut in this order: ownership, comparable deals, business relationships, capital structure folded into the financial summary, peers reduced to three. Never cut the overview, the segments, the core financials or the company's own acquisitions.

**Acquirer.** The one-line strategic relevance says what a buyer would get, not what the target is ("a dominant benchmark business with a regulatory moat and high margins", not "a leading data provider"). Customer concentration is the first signal: ask what share the five largest customers represent. Strategic fit in three groups (customer overlap, complementary product or technology, competitive substitution), two or three sentences each. Research spending shows whether the value is in intellectual property or in services; cash conversion hints at how hard integration will be; if research is not reported separately, say "not separately disclosed", which is itself information. Leverage is described in the buyer's terms. Integration considerations are three or four items a diligence team can act on: regulatory approvals and where, change-of-control clauses in key contracts, retention of key people, whether customer contracts transfer, ownership of intellectual property, pending litigation. Mark these as analysis, not sourced fact. Cut ownership first, then customers, valuation, precedent deals and capital structure; never the overview, the core financials or the integration considerations.

**Salesperson.** A briefing, not a data sheet. Three to five sentences on the company in plain language. Strategic priorities are three to five themes with labels and supporting figures, not a recap of results. Financials shrink to revenue, gross margin and headcount. Relationships in four groups (customers, suppliers and technology, partners, competitors), each with a note. Recent news starts with the latest results and ends with what is coming up, since an upcoming event is a reason to make contact. Two or three conversation openers, each citing a specific figure, date, product or initiative from the page and naming the role it suits; an opener that would fit any company in the industry fails. Tie the priorities to the user's product only when the user said what it is.

## Output

The sheet at one page for an investor and one to two for the others: a header with identifiers on one side and market data on the other, the sections for the reader, tables for financial data only, and a footer naming the data sources and stating that it is for information and not investment advice. Then, outside the sheet, the list of figures that failed a check or were missing.

## Constraints

- No figure, executive, customer, deal or multiple from memory.
- A precedent deal with no data is "not available"; a multiple is never made up.
- No rating or recommendation.
- This is a summary of supplied information, not investment advice.
