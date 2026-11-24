# Importing an existing diagram

For `.drawio`, Mermaid, `.excalidraw` or PlantUML input: extract the content
(nodes, edges, containers), then **redraw, never convert** — source coordinates,
colors, fonts and shape quirks are discarded; only the content is kept. Set four
dials before drawing: format (`html` default), size (`doc-inline` default),
detail (`balanced` default: 12 nodes max; `faithful` up to 24, zoned;
`simplified` up to 7), audience (`mixed` default). Report a fidelity ledger:
what was merged, collapsed or dropped. An import is bounded by its source:
never invent a component to fill a layout, and never silently drop one.

