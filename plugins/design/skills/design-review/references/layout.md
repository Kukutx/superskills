# Layout Craft

Craft rules for grouping, alignment and responsive structure, adapted and rewritten from `jakubkrehel/skills` better-layout (MIT).

The numbers below apply only where the project has no spacing scale or density system; otherwise use its tokens. A finding needs a failure that can be shown, such as a clip, an overlap, a broken mirror or a misread group. A value that differs from these starting points is not one.

## Grouping and alignment

- **Group with space, not lines.** Space groups first, background shapes second, separator lines last and only where space alone cannot carry the structure. The gap between groups is at least twice the gap within one, so 8px inside a group means 16px or more between groups.
- **Keep controls distinct from content.** Every interactive element gets a background shape, a border, an underline, or a consistent placement zone such as a toolbar. A control styled like the static text beside it does not read as a control.
- **Align to shared edges.** Pick a small set of alignment edges and put everything on them. Use one project spacing step per level of nesting; 16px is a useful default.
- **Order by importance.** The most important content sits near the top and the leading edge. Within a row, identifying content leads and metadata and actions trail. Visual order matches DOM order, so never move content out of source sequence with `order`, `row-reverse` or grid placement.
- **One primary action per view.** Once a view has more than three secondary actions, put them behind a menu. Prefer a short view that links deeper over one long view that shows everything at the top level.

## Mirroring

Write direction-dependent layout as leading and trailing: `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`. Reserve physical left and right for physical geometry such as safe-area insets. `float: left` on mirrored UI becomes `float: inline-start`; `translateX` and `background-position: left` need an explicit RTL override, since neither has a logical form.

## Hidden content

Every piece of off-screen or collapsed content needs a visible cue: the project's established cue, the next item peeking 16–32px past the scroll edge, or a disclosure control. A truncated value the user needs has a way to the full text; truncation mechanics are in [typography.md](typography.md).

## Spacing

- **Borderless controls need more clearance.** Start with 12px between adjacent bordered or filled controls. Leave 24px between the visible glyphs of borderless text and icon controls, counting each button's own padding. Compact layouts may use less, as long as hit areas never overlap and the controls stay distinct.
- **Inset buttons from the edges.** In content layouts, keep full-width buttons inside the layout margins, starting near 16px inline on mobile. Edge-to-edge actions work when they follow established platform chrome, account for safe areas, and stay distinguishable from system UI.
- **Content bleeds, controls float.** Backgrounds and media extend to the viewport edges. Controls and text stay inside the layout margins and safe areas. Content scrolls beneath sticky chrome; set `scroll-padding-block-start` to the sticky header's height, so anchored targets and focused elements never land under it.

## Responsive structure

- **Breakpoints come from the content, not device presets.** Keep the expanded layout until it stops fitting, then collapse. Prefer container queries for component-level adaptation, and test the smallest and largest supported sizes first.
- **Plan for growth and clipping.** Translated strings grow, and short ones grow proportionally more, so a one-word button label is the riskiest thing on the screen. Size text containers with `max-width` and `min-height`, never a fixed width or height, and let rows wrap. Test with pseudo-localisation and one long-string locale such as German. Never park a critical action where resizing, zoom or scrolling clips it.
- **Sizing fixes.** A grid track holding long text or a wide table needs `minmax(0, 1fr)`; a flex child needs `min-width: 0`. `width: 100vw` includes the scrollbar and scrolls horizontally on desktop, so use `100%`. A full-height mobile pane uses `100dvh`, which tracks the toolbar. A box holding text uses `min-height`, not a fixed height.

## Common faults

| Pattern | Fix |
| --- | --- |
| A grid track with `1fr` holding long text or a wide table, overflowing its track | `minmax(0, 1fr)` on the track, `min-width: 0` on the flex child |
| `width: 100vw` | `width: 100%`; `100vw` includes the scrollbar |
| `height: 100vh` on a full-height mobile pane | `100dvh` tracks the toolbar; keep the bottom action in stable chrome, since the on-screen keyboard resizes only the visual viewport |
| A fixed `height:` on a box holding text | `min-height`, or `max-height` with `overflow-y: auto` |
| A media query inside a reusable component | A container query on the component's parent |
| `container-type: inline-size` on a flex item, inline-block or absolute element with no width | Give it a definite width; size containment collapses a shrink-to-fit box to zero |
| `env(safe-area-inset-*)` with no `viewport-fit=cover` in the viewport meta | Add it, or the insets resolve to zero |
| `inset-inline-*` combined with `safe-area-inset-left` or `-right` | Physical `left` or `right` with the matching inset, plus an RTL override |
| `float: left` on mirrored UI | `float: inline-start` |
| `translateX` or `background-position: left` on mirrored UI | An RTL override; neither has a logical form |
| Sticky header with no `scroll-padding-block-start` | Set it to the header height |

## Verification

Without a browser, check logical properties in place of physical ones, container and media queries against the supported viewport list, and DOM order against visual order. With one, check every supported width, 320px, 200% zoom and the RTL mirror. Report every check that could not be run as not verified.

Stress the layout three ways before calling it done: resize it from the smallest to the largest supported width and watch for clipping or overlap; switch it to a long-string locale and confirm the critical action is still reachable; and mirror it for RTL, confirming that leading and trailing edges, not left and right, carry the structure.

A layout that passes all three stresses is done. A layout that passes only the designer's viewport is not reviewed; it is assumed broken at some other size until the stresses prove otherwise.

## Source

Adapted and rewritten from `jakubkrehel/skills` skills/better-layout/SKILL.md, https://github.com/jakubkrehel/skills (MIT).
