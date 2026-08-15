---
name: generational-context-analysis
description: Evidence-led personal context analysis anchored on birth cohort, place and historical conditions. Use for childhood background, cohort/worldview, career, relationship, financial-mindset and life-stage questions that explicitly avoid astrology or fortune-telling.
---

# Generational Context Analysis

## Scope

Use when the user wants to understand how **historical period, geography, technology, economy, institutions and life stage** may have shaped people born around a given date.

This is not astrology and does not infer a person's character from a date of birth alone. If the user explicitly wants 命理、占星、塔罗 or another divinatory system, use `personal/divination-reading` instead.

## Core model: age, period, cohort

Do not collapse three different effects:

```text
age effect    = changes associated with life stage
period effect = events/conditions affecting many age groups at the same time
cohort effect = different exposure because people encountered the same period at different ages
```

A birth date is mainly an **anchor for exposure timing**. It is not a causal personality variable.

Generational labels such as Gen Z or Millennial are optional shorthand, not scientific personality types. Prefer narrower birth cohorts, formative-event windows or local historical context when they explain the question better.

## Inputs

Minimum:

```text
birth date or year
country/region where childhood/adolescence occurred
```

Useful when relevant:

```text
migration history
urban/rural environment
education path
family socioeconomic context
career-entry location/year
major personal disruptions
```

Do not interrogate for all of these before starting. If only a birth date is available, give a broad cohort-level analysis and state what cannot be individualized.

## Evidence discipline

For concrete historical/economic/social claims, prefer:

1. official statistics and institutions;
2. longitudinal or peer-reviewed research;
3. reputable historical/academic sources;
4. high-quality journalism for event context.

Search current/historical sources when the answer depends on country-specific labor markets, housing, education, technology adoption, recessions, policy or other factual context.

Separate confidence levels:

- **well supported** — directly backed by historical/statistical evidence;
- **plausible cohort hypothesis** — reasonable exposure pattern but not an individual fact;
- **individual unknown** — requires the user's actual history.

Never convert a population-level association into “you are X”.

## Seven analysis modes

These absorb the earlier prompt-library ideas into one reusable workflow.

### 1. Childhood background decoder

Map the environment during childhood/adolescence:

- major local/global events;
- household technology and media transition;
- education norms;
- economic security/insecurity;
- dominant social expectations;
- changes in mobility, migration or globalization.

Focus on **shared exposures**, then explain several ways people could respond differently to the same environment.

### 2. Personality / worldview development map

Do not infer stable traits from birth date.

Instead describe:

```text
formative pressures
-> plausible learned expectations / coping styles
-> alternative responses
-> what personal history would distinguish them
```

When comparing earlier/later cohorts, compare similar life stages where possible rather than comparing today's 25-year-olds with today's 55-year-olds and calling the difference generational.

### 3. Career compass

Analyze the environment around education and labor-market entry:

- dominant industries and occupations;
- credential expectations;
- automation/digital-platform shifts;
- recessions/booms;
- remote/global work;
- entrepreneurship barriers/opportunities.

Recommend **career environments and transferable strengths**, not destiny based on birth year.

### 4. Relationship-pattern analysis

Use evidence about social norms and cohort exposure, for example:

- age at partnership/marriage;
- online dating/social media adoption;
- gender-role change;
- geographic mobility;
- work/family pressures.

Do **not** infer attachment style, fidelity, compatibility or conflict behavior from date of birth alone. Those require individual relationship history.

### 5. Financial mindset matrix

Anchor money behavior to real exposures such as:

- inflation/deflation;
- housing affordability;
- recessions and labor-market shocks;
- interest-rate regimes;
- pension/social-security expectations;
- financial technology and investing access.

Distinguish “people exposed to X may become more cautious/risk-seeking” from “you are cautious/risk-seeking”.

### 6. Hidden-struggle detector

Identify plausible blind spots created by an environment, not hidden flaws supposedly encoded by birth year.

For each hypothesis:

```text
formative condition
-> possible adaptive behavior
-> when that adaptation becomes costly
-> practical experiment to update it
```

Examples might include overvaluing credentials after a competitive education system or excessive job-security focus after recession exposure, but only when the historical context actually supports the hypothesis.

### 7. Life roadmap

Build a **scenario roadmap**, not a fortune forecast.

Use current age, location and likely structural transitions to organize:

- near-term opportunities;
- foreseeable constraints;
- skills/capital/relationships worth building;
- decisions with high option value;
- risks that deserve monitoring.

Do not claim that a certain event “usually happens to people born on this date”.

## Default output

For a full analysis:

1. **Cohort + formative context** — where/when the user came of age.
2. **Strongest documented exposures** — evidence-backed events/trends.
3. **Likely adaptations** — explicitly framed as hypotheses.
4. **Adjacent-cohort comparison** — only where useful and evidence permits.
5. **Seven-domain implications** — include only domains requested.
6. **Individual unknowns** — what could materially change the interpretation.
7. **Practical next steps** — decisions/experiments rather than labels.

For a single mode, answer that mode directly instead of generating all seven sections.

## Quick request patterns

```text
童年背景：我出生于 [date]，主要在 [place] 长大。结合当地和全球事件，分析我成长阶段最重要的共同环境；区分证据、合理推测和个人未知。

职业指南针：我出生于 [date]，在 [place] 接受教育/进入职场。结合当时经济、技术和劳动力市场，分析哪些职业环境可能更适合这一经历背景，不要用星座或代际刻板印象。

关系模式：分析我这个出生年代在 [place] 经历的约会、婚姻、性别角色和数字媒体变化。不要从出生日期推断依恋类型。

财务心态：结合我成长和进入职场时期经历的住房、通胀、衰退、利率和投资渠道，分析可能形成的金钱观假设，并告诉我哪些需要用个人经历校正。

人生路线图：基于我的年龄、地区和现实结构条件做未来阶段规划。用情景和决策重点，不要把出生年份当成命运预测。
```

## Constraints

- no astrology/divination unless the user explicitly switches tasks;
- no personality diagnosis from DOB;
- no invented “generation traits” without evidence;
- no single-country evidence generalized globally;
- no age-vs-cohort confusion when the comparison can be avoided;
- no deterministic career, relationship or financial prediction.

## Completion check

A strong answer should make clear:

```text
what happened historically
what people in that exposure window may have learned
what remains unknown about this individual
what practical decision follows
```

If the response could have been written for anyone sharing the same generational label without using place, timing or evidence, it is probably too generic.
