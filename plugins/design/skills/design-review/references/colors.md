# Colour Craft

Craft rules for building and judging a colour system, adapted and rewritten from `jakubkrehel/skills` better-colors (MIT).

## A system is ramps, not colours

One neutral ramp, one accent ramp, and only the status ramps the product actually renders. A warning ramp nothing imports is maintenance for zero pixels. A second accent hue earns its place only when two things must be distinguishable at a glance; otherwise use more steps of the one accent ramp.

Each ramp step exists because a role needs it: page background, component hover, border, solid fill, body text. Do not generate a step no role consumes.

## Naming

Primitives name a value (`--blue-600`) and are never applied in a component. Semantic tokens name a job (`--color-text-secondary`), point at a primitive, and are the only tier components reference. That seam is what lets a theme repoint colours without touching components.

Rules:

- Never borrow a token because its value is right today. A separator used as text colour works until borders get lighter, and then the text goes with them. If a role has no token, add the token.
- A semantic name never contains a hue or a component (`--color-blue-button`); rename it for its role (`--color-accent-solid`).
- Do not define both `--color-primary` and `--color-text-primary`; rename the brand token `accent`.
- A `border` token never goes inside `color:`, and a `text` token never goes inside `background:`.

## Building a ramp

A ramp holds one hue end to end, peaks in vividness mid-ramp, and steps more finely at the light end (about 0.04–0.05 OKLCH lightness per step at the light end). Build it with a colour library, never by eye. Perceived lightness throughout means OKLCH `L`, from 0 to 1.

- Match the project's colour system and notation. A consistent hex system beats hex with `oklch()` scattered through it. For a new system, `oklch()` is the best default, because its numbers behave the way these rules describe.
- Use the same proportion of each hue's own maximum chroma; one chroma number copied across every hue is wrong.
- A status hue within 15° of the accent hue moves at least 15° away, or the destructive action gets a distinct treatment.
- Dark tokens are not the light ramp in reverse step order: lower the accent's chroma, widen the dark end, and remeasure every pair.
- Pick one theme-switching mechanism (`prefers-color-scheme` or a `.dark` class) and use it throughout.

## One colour, one meaning

Use a colour for one purpose across the whole interface, treating anything within 15° of OKLCH hue as the same colour. Never let colour be the only carrier of meaning; pair it with an icon or a label. Colour as sole meaning is an accessibility failure, owned by [accessibility.md](accessibility.md).

## Emphasis

When filled colour encodes primary emphasis, one primary action per view gets it and peers stay neutral. Put the colour on the background, not the label: a filled button reads as primary across the room, while accent-coloured text on a neutral button reads as a link. Several coloured backgrounds are fine when they encode distinct states or categories rather than competing peers.

## Measuring

- Measure a foreground against the background it actually renders on, not the page background. Measure the rendered result for text on a colour with alpha.
- Never report a contrast value that was not measured, and never estimate a colour that could be computed. Whether a pair is required to pass belongs to [accessibility.md](accessibility.md).
- When a pair fails, report the pair, its measured value and the threshold it misses, then leave the colours alone. They are a design decision; change them only when asked, and remeasure after.
- A contrast fix changes lightness, the channel contrast responds to, not hue.
- White on most `500` fills and several `600` fills fails 4.5:1; measure and report it.
- Gradients: default to interpolation `in oklab`; reach for `in oklch` when a two-hue gradient goes grey in the middle. The space is a look, not a correctness setting.

## Common faults

| Pattern | Fix |
| --- | --- |
| A hex, `rgb(` or `oklch(` literal in a component file where a token exists | Reuse or add the role token, in the project's notation |
| One `oklch(` value in a codebase otherwise written in hex | Write it in the established notation unless a migration is in scope |
| `var(--blue-600)` or `bg-blue-600` in a component file | Point a semantic token at the primitive and use that |
| A semantic name containing a hue or a component | Rename it for its role |
| `--color-primary` and `--color-text-primary` both defined | Rename the brand token `accent` |
| A `border` or `separator` token inside `color:`, or a `text` token inside `background:` | Add a token for the missing role |
| `hsl(` ramp values that differ only in lightness | Rebuild with a constant perceived hue, in the project's notation |
| Light-end steps as far apart in OKLCH `L` as mid-ramp steps | Tighten the light end to about 0.04–0.05 per step |
| One chroma or saturation number copied across every hue's ramp | Use the same proportion of each hue's own maximum |
| A status hue within 15° of the accent hue | Move it at least 15° away, or give the destructive action a distinct treatment |
| Dark tokens equal to the light ramp in reverse step order | Lower the accent's chroma, widen the dark end, remeasure every pair |
| Colour tokens set under both `prefers-color-scheme` and a `.dark` class | Pick one switching mechanism and use it throughout |
| Text on a colour with alpha, such as `/50`, `rgba(` or `color-mix(` with `transparent` | Measure the rendered result, or use a solid token |
| `oklch()` chroma beyond sRGB with no sRGB value declared before it | Declare the sRGB value first, then the vivid one inside `@media (color-gamut: p3)` |

## Verification

Without a browser, check token values, the gamut of every declared colour, and that both theme blocks are present, with contrast computed from the declared token pair. With one, check the background actually rendered behind the text, including opacity and any image beneath it, measured in both light and dark. Report every check that could not be run as not verified.

## Source

Adapted and rewritten from `jakubkrehel/skills` skills/better-colors/SKILL.md, https://github.com/jakubkrehel/skills (MIT).
