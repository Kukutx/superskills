# Typography Craft

Craft rules for judging and setting type, adapted and rewritten from `jakubkrehel/skills` better-typography (MIT).

## Exact values, not preferences

Some values are exact findings when missed: unitless line-height, weight 400 or heavier below 18px, a 60–75 character measure, 16px inputs on iOS, and tabular numbers on changing values.

Letter-spacing, pairing and scale ratios are heuristics. Report them only where they break the project's own scale. Never propose a new typeface, paid or free, unless the task asks for a type change.

## Fewer fonts, sizes and weights

Rarely use more than three fonts; marketing pages can carry more than apps. Weight and size carry hierarchy, so each extra weight or size dilutes it. Pair for contrast: a serif headline over a sans body reads as deliberate, two near-identical sans-serifs read as a mistake.

Below 18px, use weight 400 or heavier. Weights 100–300 belong at 28px and up, checked against the background even there.

## Scale and hierarchy

Define a small set of sizes and deviate from it as little as possible. Pair each size with its line-height and weight, so a role is one decision instead of three. On a team, name sizes by use (`text-body-sm`) so the rules survive other people.

Heading levels map to descending steps of the scale, so a subordinate heading never overpowers its parent. Deep levels may share a size where the scale runs out, as long as weight or letter-spacing keeps them distinct. A heading is never smaller than body text unless it is a deliberate overline.

## Line-height, spacing and measure

- Display text 1.1, headings 1.2–1.3, body copy 1.5–1.6. Use unitless values so line-height scales with the font size. Tight line-height is for short text; anything wrapping to three or more lines needs at least 1.4.
- Headings at 24px and up take −0.01em to −0.02em letter-spacing. Uppercase labels at 14px or smaller take 0.05em. Body copy stays at 0. Use `em` so tracking scales with the size.
- Cap long-form text at 60–75 characters per line, in any unit, as long as a cap exists and the line length lands in range.

## Wrapping and numbers

- `text-wrap: balance` evens out headings and short descriptions, never paragraphs. `text-wrap: pretty` keeps a lone word off the last line and is safe on any paragraph.
- `overflow-wrap: break-word` where a long word, link or ID could escape the container. `white-space: nowrap` on labels and badges where a line break looks broken.
- Keep interface text at `text-align: start`. Justified text belongs only in specific editorial layouts.
- Apply tabular numbers (`font-variant-numeric: tabular-nums`) to timers, counters, prices and numeric table columns, so every digit keeps one width and nothing shifts. Leave figures in prose proportional.

## Truncation

For one line: `overflow: hidden`, `text-overflow: ellipsis`, `white-space: nowrap`. For several lines: a clamped box with `-webkit-line-clamp`. A truncated value the user needs always has a way back to the full text: an expand control, a detail view, or a tooltip that is also keyboard-reachable.

## Details

- Store text in natural case and set case with `text-transform`, so a redesign never means rewriting copy. Rendered text uses typographic characters (curly quotes, en dashes, the ellipsis character), never keyboard stand-ins; code keeps straight quotes.
- Underlines come from the font (`text-underline-position: from-font`); a dotted underline hints that a word carries extra information, such as an abbreviation.
- Inputs at 16px on mobile: iOS Safari zooms the whole page when an input's text is smaller than 16px. Either size the input up on mobile or keep `font-size: 16px` and render the intended size with a scale transform.
- Size floors: long-form body starts at 16px; inputs and menus at 14px, captions at 13px, rarely below 12px. Set `font-size` in `rem` so the reader's browser font size still applies.
- Load every face the design uses; browsers synthesise a missing weight or style and distort the face. Prefer CSS properties over raw font tags (`font-weight: 650`, not a variation-settings string).
- Apply font smoothing once on the root, never per component. Set `lang` and `dir` so browsers and assistive technology pick the right quotes, hyphenation and pronunciation.
- Decorative text (drop caps, gradient text, outlines) is built in CSS, not images, so the text stays selectable and searchable. Keep useful text selectable by default.

## Common faults

| Pattern | Fix |
| --- | --- |
| Weight 100–300 below 28px | Use weight 400 or heavier below 18px; light weights belong at 28px and up |
| A fixed `24px` line-height | Use unitless line-height so it scales with the font size |
| `text-wrap: balance` on a paragraph | Balance is for headings and short descriptions; use `pretty` on paragraphs |
| Numbers that shift as they change | Apply tabular numbers to timers, counters, prices and numeric columns |
| Truncated text with no way back | Add an expand control, a detail view, or a keyboard-reachable tooltip |
| Input text below 16px on iOS | Size up on mobile or render the intended size with a scale transform |
| `font-feature-settings: "tnum" 1` | Use the property `font-variant-numeric: tabular-nums`, which survives fallback rendering |
| `font-kerning: none` as a fix | Kerning is built into the font and on by default; never turn it off to fix spacing |
| `user-select: none` across the interface | It belongs only on draggable or gesture-driven surfaces |
| Straight quotes in rendered text | Use typographic characters; keep straight quotes in code only |
| A heading smaller than body text | Map heading levels to descending scale steps; a smaller heading must be a deliberate overline |

## Source

Adapted and rewritten from `jakubkrehel/skills` skills/better-typography/SKILL.md, https://github.com/jakubkrehel/skills (MIT).
