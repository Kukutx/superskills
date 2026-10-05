---
name: stock-research
description: Research one listed company, covering business and moat, earnings results and previews against consensus, guidance and a falsifiable thesis. Use for 财报分析 or a stock thesis, not screening.
---

# Stock Research

## Use

Use for work on a single listed company: understanding the business, reading a quarter's results, preparing for an upcoming report, updating estimates after news, or writing down and maintaining the reasons for holding it.

What the company is worth belongs to `finance/company-valuation`. Comparing an industry or finding candidates belongs to `finance/sector-and-stock-screening`. A general fact check with no investment question belongs to `research/research-brief`.

The output informs the user's own decision. It carries no rating, no price target presented as a forecast and no instruction to buy or sell, and it says that it is not investment advice.

## Domain inputs and blockers

Results, guidance, consensus and prices are current facts and are never recalled. Each one comes from a document the user supplies or a source opened in this session, with its date. In order of authority: audited filings, the earnings release and call, the company's presentations, broker research, industry reports, news.

Before analysing a quarter:

- Write down today's date and confirm the release is the latest one. A release more than about three months old is probably the wrong quarter.
- Learn the company's fiscal year; the label of a quarter follows the company's calendar, not the calendar year.
- Check that the release, the filing and the call transcript all belong to the same quarter.
- Consensus must be the figure from **before** the release, with its source and as-of date. Without it, say that the result cannot be judged against expectations; do not estimate what consensus was.

## Understanding the business

- What is sold, how it is priced, who pays and the typical size of a sale; the split of customers and the concentration in the largest ten; the route to market.
- Unit economics where disclosed. Where they are not, say so.
- Management: the chief executive and finance chief at least — their record in previous roles, tenure, ownership and how they are paid.
- Competitors of three kinds: direct, substitutes, and new entrants. The company's own annual report lists who it considers a competitor; start there.
- The moat, judged on four sources with strong, moderate or weak for each: network effects, switching costs, scale, and intangibles such as brand, data, licences or patents. Write the vulnerabilities as carefully as the strengths.
- The market in three layers (total, serviceable, obtainable) with the method behind the number and the current penetration.
- Risks in four groups: company-specific, industry, financial (path to profit, funding need, debt terms, cash burn) and macro. Each with its impact, how likely it is, and what mitigates it.

## Reading results

1. Lead with the verdict — beat, in line or miss — and the size of the gap in money and percent.
2. For every beat or miss answer: what caused it, whether it is one-off or will persist, and what it does to the thesis. A miss is separated into company-specific and industry-wide.
3. Break revenue down by segment, region or product and name what over- and under-performed. Explain margin movements by price, mix, cost and scale.
4. Guidance: new against old, and new against consensus. Weigh it by management's record of guiding conservatively or aggressively. If none was given, say so.
5. From the call: tone, the themes management pushed, what analysts kept asking about, anything unexpected.
6. Estimates are revised from the reported actuals forward, each change written as old → new with its reason, stating whether figures are reported or adjusted and what one-off items and share count changes were involved. Separate the signal from a noisy quarter before changing a long-term assumption.

## Before a report

List the three to five things that will decide the reaction, each as a metric against expectations and why it matters. Use the operating metrics of the industry: recurring revenue, retention and backlog for software; comparable sales and traffic for retail; orders and book-to-bill for industrials; net interest margin and credit quality for banks. Build bull, base and bear cases with the figures and the management language that would confirm each.

## Thesis

- One or two sentences, three to five pillars, the risks that would break it, the catalysts with dates, and the condition under which the user would exit.
- A thesis must be falsifiable. If nothing could disprove it, it is not a thesis.
- Contrary evidence is tracked as strictly as supporting evidence. Each new fact is logged with date, what it was, which pillar it strengthens or weakens, and the resulting confidence.
- Review at least quarterly. The web chat keeps nothing between sessions, so the user brings the thesis text back.

Catalysts fall into four kinds: financial (results, investor days, refinancing), corporate (launches, regulatory decisions, contract renewals, lock-up expiries), industry (conferences, data releases, rulings) and macro. Dates move; every date is confirmed on the company's investor page before it is relied on.

## Output

Numbers first: "revenue rose 15% to 1.2bn", not "strong growth". Only what is new; no company description in a results note. Every figure with its source and date, matching the filing exactly, with A for actual and E for estimated years.

## Constraints

- Do not state a result, a consensus figure, a date or a price from memory.
- Do not turn the analysis into a recommendation or a target; give the reasoning and what would change it.
- Short ideas need a higher bar of evidence, since timing is harder and losses are not capped; say so when the user is considering one.
- This is research support, not investment advice.
