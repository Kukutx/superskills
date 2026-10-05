---
name: user-research
description: Plan user research and turn interviews, surveys, usability tests, reviews or support tickets into themes, segments and ranked recommendations. Use for research about users, not facts or the market.
---

# User Research

## Use

Use for two jobs: planning a study (what method, how many people, which questions) and synthesizing what came back (transcripts, survey exports, usability notes, app reviews, support tickets, NPS comments).

Establishing external facts belongs to `research/research-brief`. Turning the findings into a specification belongs to `product/prd-builder`.

## Planning a study

Choose the method from the question:

| Question | Method | Typical size |
| --- | --- | --- |
| why people do something, what they need | interviews | 5–8 people |
| whether people can use this design | usability test | 5–8 people |
| how common something is | survey | 100 or more responses |
| how people group and name things | card sort | 15–30 people |
| how behaviour unfolds over time | diary study | 10–15 people |
| which version performs better | A/B test | enough traffic for a significant result |

The sizes are working conventions, not guarantees; state the limits of whatever sample was reached.

An interview guide for about 50 minutes runs: warm-up 5, background 10, the core topic 20, reactions to a concept or prototype 10, wrap-up 5. Questions ask about what the person did last time, not what they would do. A question that contains the answer ("Would it help if…") is rewritten.

## Synthesizing

1. **Prevalence is a count.** "5 of 8 participants", never "most users". Without the number of participants, ask for it or mark it as not stated.
2. **Observation and interpretation are written separately.** "5 of 8 tapped the wrong button" is an observation; "the button placement is confusing" is an interpretation of it.
3. **Every theme carries evidence**: a quotation with the participant's identifier, or the count behind it.
4. **Segments** are described by their traits, their needs and a rough share of the sample, not invented as personas beyond the data.
5. **Insights become opportunities**, each rated for impact and effort, so the result can be acted on.
6. **Say what the study cannot tell**: who was not recruited, leading questions, small samples, and the questions still open.

Reviews and tickets over-represent people with problems; say so when they are the only source.

7. **What people did outweighs what they say they want.** Note where the two conflict. A workaround someone built is an unmet need in disguise.
8. **Rank findings by frequency and impact together**: frequent and severe first, then rare but severe, then frequent but mild. Five to eight strong findings beat twenty weak ones, and something heard in two interviews is a hypothesis.
9. **Each finding states its confidence** (strong evidence, suggestive, early signal) and how many sources stand behind it. Evidence from about the last year outweighs older material.
10. **Surveys**: read the shape of the distribution, not only the mean; check the response rate and who did not answer; code open answers like short interviews and count them. When numbers and interviews disagree, check whether they describe the same people before choosing one.

## Output

For a plan: goal and questions, method and why, participants and recruiting criteria, the guide or survey, and the schedule.

For a synthesis: a summary of three or four sentences; the themes with prevalence, evidence and implication; the segments when they differ; the opportunities table (insight, opportunity, impact, effort); the recommendations in priority order; open questions and method limits.

## Constraints

- Do not invent quotations, participants or counts.
- Do not generalize from a handful of interviews to all users; qualitative findings say what exists, not how often.
- Keep participants unidentifiable in anything meant to be shared.
