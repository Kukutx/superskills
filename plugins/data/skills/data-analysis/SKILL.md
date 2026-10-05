---
name: data-analysis
description: Analyze a dataset, CSV, metric trend or A/B result and check the numbers before they are shared. Use to explore data, explain a change or review an analysis, not to write SQL or design a chart.
---

# Data Analysis

## Use

Use when the question is what the data says or whether a conclusion drawn from it holds: profiling a file, explaining a metric movement, comparing groups, reading an experiment, or reviewing an analysis before it goes to someone else.

Writing the query belongs to `data/sql-query-writing`; choosing and building the chart belongs to `data/data-visualization`. Checking a claim against outside sources belongs to `research/research-brief`.

## Domain inputs and blockers

Work from what was pasted or uploaded. Without the raw data, say which numbers were taken as given and not recomputed. Establish these four before computing anything, because each one silently changes every result:

- the grain (what one row is) and whether the stated key is really unique;
- the time range covered and when the data was last refreshed;
- the exact definition of each metric, including what the denominator is;
- the time zone of the timestamps.

Ask only when a definition cannot be read from the material and two reasonable readings give different answers.

## Checks that catch most wrong numbers

1. **Row counts after every join.** More rows than before means the relationship is not one-to-one; count entities with a distinct count.
2. **Subtotals add up to the total**, and the magnitude is plausible against a known reference.
3. **Complete periods only.** A partial week or month is not compared with a full one. The denominator keeps one definition across the periods being compared.
4. **Never average pre-aggregated averages.** Recompute from the underlying rows or weight by the group size.
5. **Who is not in the data.** Survivors, logged-in users or respondents only describe themselves. A segment is not defined by the outcome it is then used to explain.
6. **Missing values.** Report the share per field; treat more than about 5% missing as a caveat and more than about 20% as a reason not to rely on the field. Placeholder values (0, -1, 999999, "N/A", "TBD", "test") are missing values in disguise.
7. **Cleaning keeps the original.** Fix in a new column or a copy, report what will change (column, issue, count, proposed fix) before changing it, and confirm before removing duplicates or filling blanks.
8. **Red flags worth a second look**: a period-over-period change above 50%, suspiciously round totals, rates of exactly 0% or 100%, identical values across segments, and a result that confirms the hypothesis perfectly.

## Statistics

- Report the mean and the median for business metrics; a large gap means the distribution is skewed and the mean misleads.
- Classify an outlier before touching it: data error, real extreme, or a different population. Never drop outliers automatically, and say how many were excluded and why.
- A significant result is reported with its effect size, a confidence interval and what it means in business terms. Correlation is described as correlation.
- Pick the test from the data: two group means use a t-test (paired when the same units are measured twice), proportions use a z-test or chi-square, three or more groups use ANOVA, skewed or ordinal data use Mann-Whitney U. Below roughly 30 events per group, say that the test has little power.
- When many segments or metrics were tested, state how many, since some will look significant by chance. Check whether a trend reverses inside the segments (Simpson's paradox) before reporting the aggregate.
- A forecast is a range, not a point. Non-linear growth, several seasonal cycles, outside drivers or a decision that moves real budget are reasons to recommend a proper model built by a specialist.

## Output

Match the depth to the question:

- **Quick answer**: the number, its definition and period, and one caveat if any.
- **Full analysis**: the conclusion first, then the evidence, the method, the caveats and what to look at next.
- **Review of an existing analysis**: one verdict — ready to share, share with caveats, or needs revision — followed by the issues found, each with the check that exposed it, and the caveats the audience must be told.

State the data's as-of date and every metric definition used. Include the query or the calculation steps when they exist so the result can be reproduced.

## Constraints

- Do not present a number that was not computed from the supplied data as if it were; mark estimates and carried-over figures.
- Do not state a cause when the data only shows that two things moved together.
- Do not smooth over a failed check; a result that did not pass is reported with the reason.
- Keep the user's question as the scope; extra cuts of the data are offered, not silently added.
