---
name: divination-reading
description: Reflective divination across Chinese traditions, Tarot, Jyotisha and optional Western astrology. Use when the user explicitly wants fortune-telling or symbolic interpretation; choose the method automatically when possible, ask only for missing inputs that matter, and never fabricate chart calculations.
---

# Divination Reading

## Scope

Use for explicit 占卜、算命、八字、紫微、六爻、梅花、奇门、塔罗、Jyotiṣa/印度占星、西方占星 or comparable symbolic readings.

If the user instead wants evidence-based analysis of birth cohort, history, economy or technology, use `personal/generational-context-analysis`.

## Default experience

The user should not need to know the technical system first.

```text
user goal
-> infer the smallest suitable method
-> ask at most one compact round of missing information when possible
-> verify chart/cast/draw data
-> answer in plain language first
-> expose technical detail only when useful or requested
```

Do not begin by asking the user to choose among many schools, spreads or technical conventions.

### Smart defaults

- User explicitly names a system -> use it.
- “算命 / 命盘 / 看一生” in a Chinese context + birth data -> default to 八字 unless the user prefers another tradition.
- One concrete question with no preferred system -> use a focused question method rather than a full natal stack. A small Tarot reading is a practical default when an honest simulated/tool draw is available.
- Strategy/direction/electional timing -> use 奇门 or Jyotiṣa muhūrta only when the required chart can actually be calculated; otherwise use a simpler reflective method rather than inventing precision.
- Jyotiṣa or Western astrology -> normally use only when explicitly requested or clearly preferred.
- Advanced systems such as 大六壬/太乙 -> use on request or when a reliable implementation is available, not because they sound more sophisticated.

Use `references/method-selection.md` only when method choice is genuinely ambiguous.

## Minimum input

Ask only for what changes the answer.

### Birth-chart reading

Usually:

```text
birth date
birth time (or approximate range)
birth place
calendar type only if not obvious
```

The Skill should resolve timezone/DST/calendar/chart conventions itself where a reliable source/tool exists. Ask the user about a technical convention only when different choices materially change the result and cannot be inferred.

If birth time is uncertain, continue with the stable parts and clearly mark what becomes unreliable instead of blocking the entire reading.

### Focused question

Usually:

```text
one concrete question
optional time horizon
```

Ask for cast/cards only when the selected method needs them. If a simulated draw/cast is used, label it honestly.

## Truth boundary

Keep this chain intact:

```text
verified chart / cast / draw
-> traditional symbolism/rule
-> interpretation
-> practical reflection
```

- Never invent pillars, planetary positions, moving lines, stars or cards.
- If exact calculation cannot be verified, ask for a precomputed chart or switch to an honestly performable method.
- Present conclusions as traditional/symbolic interpretation, not established fact.
- Do not use divination as sole evidence for medical, legal, financial, safety or other high-stakes decisions.
- Do not keep recasting/redrawing until the answer becomes favorable.

## Runtime references

| Need | Reference |
| --- | --- |
| ambiguous method choice / fallback | `references/method-selection.md` |
| 八字、紫微、六爻、梅花、奇门、大六壬、太乙 | `references/chinese-metaphysics.md` |
| Tarot / card-oracle reading | `references/tarot-oracles.md` |
| Jyotiṣa / Indian astrology / Western astrology | `references/astrology-traditions.md` |

Load only the relevant reference(s).

## Reading style

Default to **simple mode**:

1. **先说重点** — one short overall reading.
2. **3–5 个主要主题** — only the signals that drive the conclusion.
3. **回答用户真正问的领域** — work, relationship, timing, choice, etc.
4. **现实建议** — useful actions/questions that remain sensible even if the symbolism is wrong.
5. **不确定项** — only when they materially affect the result.

Do not dump technical vocabulary, every minor star, every hidden stem, every Tarot keyword or every aspect by default.

If the user says `专业模式 / 展开排盘 / 详细技术分析`, then add the chart structure, conventions, calculation details and deeper traditional reasoning.

## Useful interaction patterns

The user can speak naturally:

```text
“帮我算一下事业，我的信息是……”
“我最近纠结要不要接这个 offer，帮我占一下，方法你选。”
“用八字看未来两三年，出生时间大概在下午三点左右。”
“帮我抽三张塔罗看这段关系，我没有实体牌。”
“用印度占星看婚姻，但如果时间不够精确就告诉我哪些不能判断。”
```

The Skill should translate these into the required method internally instead of making the user rewrite a professional prompt.

## Completion check

Before saying done, confirm:

- the method fits the actual question;
- required chart/cast data is verified or uncertainty is explicit;
- the answer is understandable without specialist knowledge;
- technical depth is proportional to the user's request;
- symbolic interpretation is not disguised as factual certainty;
- the response ends with something useful beyond a deterministic “吉/凶”.
