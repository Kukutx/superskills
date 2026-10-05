# Single-Cell Model Guide maintenance sources

Maintenance-only. Do not load for normal tasks.

## Policy

- Each row is an official page that was opened and read when the Skill was written or last reviewed.
- The upstream plugin this Skill was distilled from contradicts itself on class locations, setup calls, missing-gene handling, the number of variable genes and several thresholds, and marks parts of its own code as version-dependent. The Skill therefore names models and decisions only, carries no code, and tells the reviewer to check calls against the documentation for the user's version.
- Not verified on an official page: the "about ten" maximum used to spot transformed data, the one-half confidence bar and the one-half gene-overlap line. They come from the upstream scripts and are written as approximate.

## Source register

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| scvi-tools user guide, model index | https://docs.scvi-tools.org/en/stable/user_guide/index.html | which model serves which data type and task, including SysVI for datasets with substantial batch effects; the page lists more models than the Skill names | 2026-10 |
