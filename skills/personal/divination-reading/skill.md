---
name: divination-reading
description: Reflective divination and traditional astrology across Chinese systems, Tarot, Jyotisha and optional Western astrology. Use when the user explicitly wants a symbolic/fortune-telling reading; choose the appropriate method, verify chart conventions, and never fabricate calculations.
---

# Divination Reading

## Scope

Use when the user explicitly asks for 占卜、命理、八字、紫微、六爻、梅花、奇门、塔罗、Jyotiṣa/印度占星、西方占星 or a comparable symbolic reading.

This Skill treats these as **traditional interpretive systems**, not empirically established forecasting. If the user instead wants evidence-based analysis of how birth cohort, historical events or economic conditions may shape experience, use `personal/generational-context-analysis`.

## Truth boundary

Keep four layers separate:

```text
verified chart / cast / card data
-> traditional rule or symbolism
-> interpretation
-> practical reflection
```

- Say “按此体系/传统解释” rather than presenting a prediction as certain fact.
- Do not turn symbolic language into a diagnosis of personality, health, fertility, legal outcome, investment return or another high-stakes fact.
- A reading may support reflection or option generation; it should not replace professional evidence for medical, legal, financial or safety decisions.
- **Never invent a chart, pillar, planetary position, moving line or card draw.** If exact computation requires a calendar/ephemeris/charting tool that is not available or verified, ask for a precomputed chart or clearly limit the answer to method-level interpretation.

## Input gate

Ask only for information that changes the chosen method.

### Natal / birth-chart methods

Usually need:

```text
birth date
birth time + precision/uncertainty
birth place
civil calendar used
historical timezone / DST when relevant
sex/gender only if the chosen tradition actually uses it
```

If the birth time is approximate, say which conclusions become unstable instead of silently treating it as exact.

### Question-based divination

Usually need:

```text
one concrete question
time horizon if relevant
important known constraints
the cast/draw data, or explicit permission to generate/simulate it
```

Do not keep redrawing/recasting until the answer becomes favorable.

## Choose one primary method

Use `references/method-selection.md` when the user has not specified a system or when several systems could apply.

Do **not** stack 八字 + 紫微 + 六爻 + 奇门 + 塔罗 + Jyotiṣa by default. One coherent method is usually clearer than a “majority vote” across unrelated traditions.

## Runtime references

| Need | Reference |
| --- | --- |
| choose a method, decide required data, cross-method discipline | `references/method-selection.md` |
| 八字、紫微斗数、易经/六爻、梅花、奇门、大六壬、太乙 | `references/chinese-metaphysics.md` |
| Tarot and comparable card/oracle readings | `references/tarot-oracles.md` |
| Jyotiṣa/Indian astrology and optional Western astrology | `references/astrology-traditions.md` |

Load only the relevant reference(s).

## Reading workflow

1. **Clarify the real question.** Separate curiosity, self-reflection, timing, compatibility, decision support and a request for a full natal reading.
2. **Choose the method.** Respect the user's requested tradition; otherwise select the smallest method that fits the question and available data.
3. **State the convention.** Calendar, time correction, school, spread, reversal policy, ayanāṁśa/house system or casting method matters when applicable.
4. **Verify the base data.** Chart/cast/draw first; interpretation second.
5. **Interpret hierarchically.** Start with the few dominant themes, then supporting details. Do not dump every symbol or technical term.
6. **Translate into usable language.** Explain what a symbol traditionally points toward, plausible manifestations, and what would contradict that interpretation.
7. **End with grounded reflection.** Give questions, options or practical actions that remain useful even if the divinatory interpretation is wrong.

## Default output

For a substantial reading:

1. **Method + assumptions** — tradition, chart/cast convention, uncertain inputs.
2. **Base structure** — only verified pillars/positions/cards/hexagrams relevant to the reading.
3. **Core themes** — 3–6 strongest signals.
4. **Requested domains** — e.g. character, work, relationships, timing.
5. **Tensions / alternative readings** — where the symbolism is mixed or school-dependent.
6. **Practical reflection** — non-deterministic implications and useful next questions.

For a focused question, answer the question first and keep the technical apparatus proportional.

## Quick request patterns

These are usage shortcuts, not separate prompt files.

```text
完整命盘：这是我的出生日期、时间、地点。请先判断还缺什么，再选择我指定的体系做完整解读；明确排盘约定和不确定项。

单一问题：我的问题是 [...]. 时间范围是 [...]. 如果我没指定体系，请选最适合的一种，不要多体系堆叠。

八字：请以子平八字为主。先核对公历/农历、时区、出生地和是否采用真太阳时，再排盘；不要用“缺什么补什么”代替格局分析。

塔罗：问题是 [...]. 请选最小够用的牌阵。若没有真实抽牌工具，请明确标注模拟抽牌；不要为了得到好答案重复抽牌。

印度占星：请用 Jyotiṣa。先说明使用的星历/ayanāṁśa 和出生时间精度；如果无法可靠计算命盘，不要猜行星或宫位。
```

## Completion check

Before saying the reading is complete, check:

- the chosen method actually fits the question;
- required chart/cast data was verified or uncertainty is explicit;
- school/convention differences are not hidden;
- interpretation is separated from factual claims;
- technical jargon is translated rather than piled up;
- no high-stakes decision is being justified solely by divination;
- the answer gives the user something useful beyond deterministic “吉/凶” labeling.
