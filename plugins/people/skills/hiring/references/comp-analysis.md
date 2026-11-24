# Compensation Analysis

Rules for benchmarking pay and modelling equity, adapted and rewritten from `anthropics/knowledge-work-plugins` human-resources comp-analysis (Apache-2.0).

`people/hiring` writes the offer; this file decides what the offer should be worth.

## What is needed

Three ways in, depending on what the user has:

- **Single role.** "What should we pay a senior software engineer in this city?" Needs role, level and location.
- **Uploaded data.** A CSV of the company's bands or a paste of them, to analyse placement, find outliers and compare with the market.
- **Equity modelling.** "Model a refresh grant of 10,000 shares over four years at a $50 stock price."

## Framework

Total compensation has four components: base salary (cash), equity (RSUs, stock options or other equity), bonus (annual target bonus, signing bonus), and benefits (health, retirement, perks, harder to quantify). A comparison on base alone is not a comparison.

The variables that move the answer: role and specialisation, level (individual-contributor and management levels), location (geographic pay adjustments), company stage (startup, growth, public), and industry.

Data sources: with compensation data, pull verified benchmarks; without it, use web research, public salary data and user-provided context. Always note data freshness and source limitations. Compensation data is sensitive; results stay in the conversation.

## Output

Report percentile bands (25th, 50th, 75th, 90th) for base, equity and total compensation, with location adjustments and company-stage context, and name the sources.

| Percentile | Base | Equity | Total comp |
| --- | --- | --- | --- |
| 25th | | | |
| 50th | | | |
| 75th | | | |
| 90th | | | |

When company data is supplied, add band analysis per employee: current base against band minimum, midpoint and maximum, and position (below, at, above). Then recommendations: specific compensation recommendations, equity considerations, and retention risks.

## Band placement and outliers

- An employee below the band minimum is a pay-equity and retention risk, not a rounding error. Say so plainly.
- An employee above the band maximum is either mis-levelled or held in a band that no longer fits the role; the fix is a level review or a band revision, not a quiet freeze.
- A cluster of outliers at one level usually means the band, not the people, is wrong.
- Location matters: the same role in different cities is a different benchmark. Never compare a salary against a benchmark from another city without stating the adjustment.

## Equity modelling

Model the grant as the employee experiences it: total shares, vesting schedule, current stock price, and the value at vesting under stated assumptions. State the assumptions (price held flat, growth scenarios) rather than baking one into a single number. A refresh grant is judged against the unvested balance it replaces, not in isolation.

## Worked example

A senior engineer in Milan, five years' experience, at a growth-stage company. Benchmarks come from public salary data and the user's own context, with the source and the date named. The table shows the 25th, 50th, 75th and 90th percentiles for base, equity and total compensation, plus the location adjustment applied. The recommendation then states a band position (for example, 60th percentile for a strong hire in a hard-to-fill role) and the reason, the equity grant with its vesting, and the retention risk if the offer lands below the 50th percentile.

When the data is thin for a role or a city, say so and widen the band rather than inventing precision. A wide honest band beats a narrow invented one, and the offer letter states the numbers that were actually agreed, not the benchmark.

## Constraints

- Do not invent a market rate. A figure without a source is labelled an estimate with its basis, or left blank.
- Do not present a single percentile as "the market rate". The band is the answer.
- Do not share one employee's compensation with another; band analysis is reported per person to the requester only.

## Source

Adapted and rewritten from `anthropics/knowledge-work-plugins` human-resources/skills/comp-analysis/SKILL.md, https://github.com/anthropics/knowledge-work-plugins (Apache-2.0).
