---
name: data-visualization
description: Choose the right chart and build clear, honest, accessible charts or a one-page KPI dashboard from data. Use for a chart, plot, graph or dashboard, not for deciding what the numbers mean.
---

# Data Visualization

## Use

Use when the deliverable is a chart, a set of charts or a dashboard, in any form: a description of what to draw, plotting code, or a single HTML page.

What the numbers mean and whether they are right belongs to `data/data-analysis`. Store screenshots belong to `design/app-store-assets`.

When the host provides its own charting or design system, follow its components and palette; the rules below still decide which chart to draw and whether it is honest.

## Choosing the chart

Pick from the relationship in the data, not from what looks impressive:

| The data shows | Use | Avoid |
| --- | --- | --- |
| change over time | line; bars for few discrete periods | a pie per period |
| comparison across categories | bars, sorted by value | bars in arbitrary order |
| ranking | horizontal bars | a table when there are many items to scan |
| part of a whole | stacked bar; a pie only below 6 slices | pies with many slices, donuts for comparison |
| distribution | histogram, box plot | averages alone |
| relationship between two measures | scatter | a dual-axis line |
| a few headline numbers | KPI tiles with the comparison stated | a chart per number |

No 3D charts. A dual axis suggests a relationship that may not exist; when it is unavoidable, label both axes and say so. Many categories in a stacked bar become unreadable; use small multiples.

## Honesty

- Bars start at zero. A line may use a non-zero baseline when the axis is labelled.
- Charts that will be compared share the same scale.
- Show uncertainty when it exists (a range, an interval, a sample size).
- Every axis has a label and a unit. Incomplete periods are marked.

## Reading at a glance

- The title states the finding ("Churn doubled after the price change"), the subtitle states the period, filters and source.
- Colour encodes data. Highlight the one series that matters and grey out the rest; keep categorical colours to about six.
- Never rely on colour alone: add direct labels, line styles or patterns, and prefer blue and orange to red and green. The chart should still read when printed in black and white, and the underlying values should be available as text or a table.
- Sort categories by value unless they have a natural order. Format numbers for reading: 45.2%, $1.2M, 2.3K.

## Dashboard

- Two to four KPIs on top, one to three charts beneath, a detail table only when someone needs to look things up.
- Aggregate before plotting: keep a line under roughly 500 points per series, bars under 50 categories, a scatter under 1,000 points, a table paginated at 100 to 200 rows.
- A page that loads its charting library from a CDN does not work offline; say so, or inline the library.
- Values from data are escaped before they are placed into HTML.
- A static page is a snapshot at a point in time. For live or frequently refreshed data, recommend a BI tool instead.
- With no data yet, build with sample data and label it as sample on the page.

## Output

The chart or dashboard, plus one line on why this chart type fits and anything the reader must know to read it correctly (baseline, excluded data, sample size).

## Constraints

- Do not plot numbers that were not supplied or computed; sample data is labelled.
- Do not pick a chart that hides the finding to look more sophisticated.
- Before delivery, check: readable without colour, text legible at the display size, title is the finding, axes have units, legend does not cover data, source and date present.
