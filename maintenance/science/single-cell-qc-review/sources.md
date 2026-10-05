# Single-Cell QC Review maintenance sources

Maintenance-only. Do not load for normal tasks.

## Policy

- Each row is a page that was opened and read when the Skill was written or last reviewed. The Skill states only what the page said.
- The upstream plugin this Skill was distilled from contradicts itself on the scale of the MAD (its guide says log-transformed, its script uses raw values) and gives tissue-specific ranges without a source. The Skill follows the published chapter for the defaults, tells the reviewer to ask which scale was used, and carries no tissue-specific numbers.

## Source register

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| Single-cell best practices, Quality Control chapter | https://www.sc-best-practices.org/preprocessing-visualization/quality-control/ | the MAD formula; 5 MADs on log-transformed total counts and genes detected; 3 MADs and an 8% ceiling for the mitochondrial share; gene name prefixes; genes detected in fewer than 20 cells removed; the order of cell filtering, ambient RNA correction, gene filtering and doublet detection; being permissive and re-assessing after annotation | 2026-10 |
