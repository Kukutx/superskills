---
name: diagram-design
description: Design an editorial diagram as a self-contained HTML and SVG figure, one focal accent inside a complexity budget. Use when a reader learns more from a visual than prose, not for a table.
---

# Diagram Design

Create diagrams as self-contained HTML files with inline SVG and an editorial
design system. The diagram is the deliverable: one figure a reader can
understand without the surrounding prose.

Adapted from `cathrynlavery/diagram-design` (MIT); see `maintenance` `sources.md`
for attribution and what was left out.

## Use

Use for architecture, flowchart, sequence, state machine, ER/data model, steps,
timeline, git graph, swimlane, quadrant, radar, tree, org chart, layer stack,
Venn, pyramid/funnel, treemap, heatmap, bar, waterfall, line, Gantt, scatter,
Sankey, fishbone, Wardley map, kanban, user journey, service blueprint,
deployment, dependency graph, UML class, story map, database schema,
requirement traceability, event modeling and schedule network diagrams, when a
reader will learn more from the visual than from prose, a table or a list.

Not this Skill:

- a list of things, or an attribute-only before/after -> a table or bullets;
- a one-shape "diagram" -> write the sentence;
- choosing which chart fits a dataset -> `data/data-visualization`;
- reviewing a UI screen -> `design/design-review`;
- a whole landing or marketing page -> `design/landing-page-design`.

Before drawing, ask: would the reader learn more from this than from a
well-written paragraph? If no, do not draw.

## Philosophy

The highest-quality move is usually deletion.

- Every node represents a distinct idea. Two nodes that always travel together
  are one node.
- Every connection carries information. If the relationship is obvious from
  layout, remove the line.
- The accent color is editorial, not a flag: 1–2 focal nodes per diagram.
  Accenting five nodes erases the signal.
- The diagram is not done when everything is added. It is done when nothing can
  be removed.

Target density is about 4 out of 10: enough to be technically complete, not so
dense it needs a guide. Above 9 nodes, it is probably two diagrams.

## Workflow

1. **Style first.** If the project has a brand or design system, take its colors
   and typography from there; if it has none and this is the first diagram, ask
   the user once whether to customize the style (website URL, local design
   system, pasted tokens, or keep the default) before drawing. Do not silently
   ship default styling into a branded project.
2. **Pick the type by what is shown.** Components and connections -> architecture;
   decision logic -> flowchart; messages over time -> sequence; states and
   transitions -> state machine; entities and relationships -> ER/data model;
   a short ordered method -> steps; events in time -> timeline; cross-functional
   handoffs -> swimlane; part-of-whole -> treemap; a quantity splitting and
   merging across stages -> Sankey; causes of one effect -> fishbone; work by
   state -> kanban. If two types seem useful, pick the dominant axis; do not
   combine two layout grammars.
3. **State the plan in one short message** before drawing: the chosen visual
   type, the size preset, and anything the complexity budget will force out.
   Let the user redirect before you draw, unless the request already pins type,
   size and content exactly.
4. **Draw a single self-contained `.html` file**: embedded CSS, inline SVG, no
   external images; static by default, minimal inline JavaScript only for
   explicit animation controls. Motion never changes the static meaning.
5. **Render and look.** Export a preview at real size and inspect it for clipped
   or overlapping text, labels away from their connector, connectors crossing a
   box they do not attach to, stacked connectors, uneven gaps, dense clusters
   beside empty bands, and content cut at the viewBox edge. Fix by restructuring
   first (flow direction, regrouping, shorter labels, merged edges) before
   nudging coordinates. Re-render after fixes, at most twice.

## Complexity budget (per diagram)

| Limit | Rule |
| --- | --- |
| Nodes | 9 max |
| Arrows / transitions | 12 max |
| Accent elements | 2 max |
| Annotation callouts | 2 max |
| Motion (optional) | 8 steps, 12 marked items, 2 simultaneous |

If the budget is exceeded, split into two diagrams (overview + detail).

## Connector rules (non-negotiable)

1. **Orthogonal only.** Right-angle elbows between off-axis nodes; a straight
   line only when both ends share x or y. No diagonals.
2. **Label gap.** Every arrow label (14 characters max, all caps, centered on
   its segment) sits on an opaque mask with a visible 6–10px gap from its
   stroke, beside vertical segments, never on the line.
3. **No overlaps.** No shared or stacked strokes: offset parallel routes by
   12px or more, and use a bridge/hop at a single crossing.
4. **Fan attach points.** Connectors on one box edge each get their own point,
   12px or more apart.
5. **No transit behind a non-endpoint box.** Reroute; only when geometrically
   unavoidable, use a dashed stroke with the label at the visible end.
6. **Mask before node.** A label mask must not overlap a node drawn after it.

## Design system

Semantic roles, not hard-coded colors: `paper` (page background), `ink`
(primary text and stroke), `muted` (secondary text, default arrows), `rule`
(hairline borders), `accent` (1–2 focal elements), `link` (HTTP/API and
external calls). Node names in a sans font at weight 600; ports, commands and
URLs in mono; the page title in a serif font. Mono is for technical content
only, never as a blanket "dev" font. No shadows; borders only; corner radius
6–10px at most.

Every diagram is an accessible figure: the `<svg>` carries `role="img"` and
`aria-labelledby` naming its `<title>` (first child, under 60 characters) and
`<desc>` (one sentence about the content, not the geometry), with IDs prefixed
by the file slug.

## Importing an existing diagram

For `.drawio`, Mermaid, `.excalidraw` or PlantUML input, load [references/importing.md](references/importing.md): extract the content, then redraw rather than convert, set the four output dials first, and report a fidelity ledger.

## Pre-output checklist

- [ ] The right visual type for the layout, and a table or paragraph would not
  do the same job?
- [ ] Can any node, arrow or label be removed without losing meaning?
- [ ] Accent on 2 elements at most? Legend covers every type used, nothing extra?
- [ ] Within the complexity budget? All six connector rules hold?
- [ ] Arrows drawn before boxes, every arrow label on an opaque mask, legend as
  a horizontal bottom strip?
- [ ] Node origins, dimensions, gaps and padding on a 4px grid?
- [ ] Accessible SVG contract holds (role, title first, slug-prefixed IDs)?

## Output

One self-contained `.html` file per diagram, plus one line naming the type, size
preset and any content the budget forced out. Export to PNG/SVG only when the
user asks for it; the render preview is not an export.
