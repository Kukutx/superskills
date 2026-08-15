---
name: generational-context-analysis
description: Evidence-led life-context analysis anchored on birth cohort, place and historical conditions. Use for childhood background, worldview, career, relationships, money and life-stage questions that explicitly avoid astrology or fortune-telling.
---

# Generational Context Analysis

## Scope

Use when the user wants to understand how **historical period, geography, economy, technology, institutions and life stage** may have shaped people born around a given time.

This is not astrology. A birth date is an exposure-timing anchor, not a personality cause. If the user explicitly wants 命理、占星、塔罗 or symbolic fortune-telling, use `personal/divination-reading`.

## Default experience

The user should be able to ask in normal language.

```text
user question
-> infer the relevant life-context mode
-> use birth date/year + place as anchors
-> search/verify factual context when needed
-> separate evidence from plausible cohort hypotheses
-> answer only the requested domains
```

Do not force a seven-section report when the user only asks about career, relationships or money.

## Minimal inputs

Usually enough to start:

```text
birth year/date
where the user mainly grew up
```

Useful only when they materially change the answer:

- migration history;
- urban/rural context;
- education or career-entry place/year;
- family socioeconomic background.

If place is missing and geography would strongly change the answer, ask one compact follow-up. Otherwise start broadly and state the limitation.

## Core reasoning

Keep three effects separate:

```text
age   -> life-stage change
period -> events affecting many people at once
cohort -> different exposure because the same event was experienced at a different age
```

Generational labels such as Gen Z/Millennial are optional shorthand, not personality types.

For factual historical/economic claims, prefer official statistics, longitudinal/peer-reviewed research and reputable historical sources. Search current or historical evidence when country-specific labor, housing, education, technology or policy matters.

Use three confidence levels naturally:

- **documented context** — directly supported by evidence;
- **plausible cohort pattern** — reasonable but not an individual fact;
- **personal unknown** — requires the user's real history.

Never turn “people exposed to X may…” into “you are X”.

## Auto-selected modes

| User asks about | Analyze |
| --- | --- |
| childhood / upbringing | major events, media/technology, education, economy, social norms during formative years |
| personality / worldview | plausible learned expectations and coping patterns, with alternative responses |
| career | labor market at education/career entry, industries, technology shifts, credentials, work norms |
| relationships | dating technology, marriage norms, mobility, gender roles, work/family pressure |
| money | housing, inflation, recessions, interest rates, job security, pensions and investing access |
| blind spots / struggles | adaptations that once helped but may now become costly |
| life roadmap | current age + structural opportunities/constraints + high-value next decisions |

These are modes, not separate prompt templates.

## Quality rules by mode

### Childhood / worldview

Start with shared exposures, then explain several possible responses. Do not claim that everyone from the same cohort develops the same trait.

### Career

Recommend **work environments, skills and opportunity directions**, not destiny from birth year.

### Relationships

Cohort evidence may describe dating norms or marriage timing. It cannot infer attachment style, fidelity or compatibility without individual history.

### Money

Link possible attitudes to real exposure such as housing affordability or recession experience. Keep personal risk tolerance as unknown unless the user provides it.

### Blind spots

Use:

```text
formative condition
-> possible adaptive behavior
-> when it becomes costly
-> one practical experiment
```

### Life roadmap

Use scenarios and decision priorities rather than “people born in this year usually experience X at age Y”.

## Default output

Keep it compact:

1. **最重要的时代背景** — only the context that matters for this question.
2. **可能形成的影响** — hypotheses, not personality verdicts.
3. **与你个人情况最可能不同的地方** — one or two important unknowns.
4. **实际建议** — choices, experiments or questions worth acting on.

For a broad “完整分析”, expand across the relevant modes. For a focused question, stay focused.

## Natural request examples

```text
“我 1994 年出生，在中国长大，为什么我们这一代这么看重稳定？”
“结合我成长和进入职场的时代，分析适合我的职业环境，不要占星。”
“我这个年代的人为什么对买房这么焦虑？区分数据和推测。”
“根据我的年龄和现实环境做未来五年的路线图，不要命运预测。”
```

The user does not need to know terms such as age–period–cohort before asking.

## Constraints

- no astrology/divination unless the user switches tasks;
- no personality or attachment diagnosis from DOB;
- no unsupported generation stereotypes;
- no single-country pattern generalized globally;
- no deterministic career, relationship or financial prediction;
- do not confuse today's age difference with a true cohort difference when the comparison can be made more carefully.

## Completion check

A strong answer makes clear:

```text
what happened
-> what adaptation it could plausibly encourage
-> what remains unknown about this person
-> what useful decision follows
```

If the answer could be pasted onto anyone with the same generation label without using place, timing or evidence, it is too generic.
