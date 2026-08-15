# Chinese Metaphysics Reference

Use for 八字、紫微斗数、Yijing/六爻、梅花易数、奇门遁甲、大六壬、太乙神数.

These traditions contain multiple schools and calculation conventions. State the convention actually used instead of presenting one school as universal.

## 八字 / Four Pillars

### Input and chart integrity

For an exact natal chart, resolve:

```text
birth date + calendar
birth time + precision
birth place
historical timezone / DST
whether any local/apparent-solar-time correction is being used
```

A common 子平/Four-Pillars workflow uses solar-term boundaries for calendrical structure rather than treating lunar-month labels as month pillars. Near year/month/hour boundaries, small time or convention differences can change the chart, so expose the boundary instead of hiding it.

“真太阳时” is a **method choice**, not an automatic universal correction. If used, state how civil time, longitude and apparent-solar-time effects were handled. Do not silently alter the user's birth time.

### Interpretation order

Do not reduce 八字 to “五行缺什么就补什么”. A more coherent traditional reading considers, in order:

1. verified four pillars and hidden stems;
2. season/month command and overall qi distribution;
3. 日主 strength/condition under the chosen school;
4. stems/branches interactions, combinations, clashes, harms or punishments when materially relevant;
5. 十神 and structural pattern as relational language, not isolated labels;
6. 喜用/忌 only after the chart logic is established;
7. 大运/流年 as timing layers, using a stated calculation convention.

Do not assign a “lucky color/industry/direction” merely from a missing element. If giving such traditional correspondences, derive them from the stated interpretation and label them as symbolic suggestions.

### 大运 / timing

Direction and 起运 calculation can vary by lineage/convention. When exact timing matters:

- state the rule used;
- show the resulting start age/date;
- flag uncertainty near a boundary;
- do not fabricate a precise 大运 table from memory.

For 1–3 year readings, distinguish natal structure from 运/年 triggering. Avoid interpreting every annual stem/branch as a guaranteed event.

## 紫微斗数

Use when the user wants a palace/star-based natal reading and a reliable chart is available.

Exact charting can depend on lunar-calendar conversion, birth hour, sex/gender rules and school-specific placement/四化 conventions. Therefore:

- prefer a verified chart or charting tool;
- state the school/convention when known;
- interpret major palace structure and dominant stars first;
- do not dump every minor star;
- do not merge 八字 and 紫微 terminology as if they share one calculation system.

If the birth time is uncertain enough to change the 时辰, treat the affected palace/star placements as unstable.

## Yijing / 六爻

For an actual 六爻 reading, preserve the cast data:

```text
original hexagram
moving line(s)
changed hexagram
casting time when the chosen school uses it
```

If using a coin/yarrow/randomized cast, state how it was produced. If no real random/casting tool exists, either ask the user to cast or label a model-generated cast as simulated.

Interpret the question before technical detail. Traditional 六爻 schools may use 纳甲、世应、六亲、用神、月日旺衰 and other layers; do not invoke all of them unless the required chart data and method are actually available.

For a general Yijing reading, the hexagram/line imagery can be used as a structured reflection on change, alternatives and timing without pretending that the text supplies certain future facts.

## 梅花易数

Useful for quick symbolic readings derived from a stated time/number/event method.

Because different derivation recipes exist, always state the algorithm or input that produced the upper trigram, lower trigram and moving line. Do not reverse-engineer a convenient hexagram after seeing the desired answer.

Keep the result proportional: main/relating trigrams, moving relation, dominant image, then practical interpretation.

## 奇门遁甲

Best suited to a time-specific strategic/choice question when an actual 奇门 chart can be produced reliably.

Before interpreting, resolve the charting convention/school. Different systems can vary in 局、排盘 and placement methods. Do not mix rules from several schools in one chart simply to create more signals.

Interpret around the **specific question**: actors/positions, timing, constraints, direction/strategy where the chosen system supports them. Do not turn generic “吉门/凶门” labels into guaranteed outcomes.

## 大六壬 / 太乙神数

Treat these as advanced specialized systems, not automatic upgrades over simpler methods.

Use only when:

- the user explicitly asks for the system, or
- a reliable chart/method implementation is available and it clearly fits the question.

If the exact charting procedure cannot be verified, do not imitate the vocabulary and invent a result. Prefer 六爻、梅花、Tarot or another method that can be performed honestly.

## Cross-system discipline

Chinese systems can complement one another, but they do not share one universal source of truth.

If the user asks for a combined reading:

```text
primary system -> finish coherent interpretation
secondary system -> answer one defined cross-check question
compare -> agreements / contradictions / different lenses
```

Do not use “three systems agree” as a numerical confidence claim.

## Reading quality

Good interpretation should:

- explain the few structural signals that actually drive the conclusion;
- translate technical terms immediately;
- distinguish natal tendency, current timing and the user's real-world choices;
- describe both favorable and difficult manifestations of the same symbol;
- avoid fatalistic claims about death, illness, marriage failure, wealth or another irreversible outcome.
