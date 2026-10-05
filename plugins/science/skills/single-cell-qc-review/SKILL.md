---
name: single-cell-qc-review
description: Review single-cell RNA-seq quality control from pasted metrics, plots or code, including MAD cutoffs and mitochondrial percent. Use for judging cell filtering, not clustering or model choice.
---

# Single-Cell QC Review

## Use

Use when someone has run, or is about to run, quality control on single-cell RNA-seq data and wants the thresholds, the plots or the filtering code judged: are the cutoffs reasonable for this tissue, why did so many cells disappear, why is the mitochondrial share zero, what should happen before and after filtering.

General outlier handling in tabular data belongs to `data/data-analysis`. A failed pipeline run belongs to `science/nf-core-run-review`.

Nothing is computed here unless the user uploads the data and it is actually processed in the session. Otherwise every judgement rests on the summary figures the user pastes, and the answer says which numbers came from them.

## Domain inputs and blockers

Species; tissue or cell type; the protocol; the number of cells; whether the matrix holds raw counts; whether there are several samples or batches; and the QC summary: for each metric the median, the cutoff used and the share of cells removed, plus cell counts before and after. With some of these missing, answer with the defaults below and say that they are defaults.

## Rules

1. **Three metrics per cell**: total counts, number of genes detected, and the share of counts from mitochondrial genes. Low counts and few genes with a high mitochondrial share suggest a dying or broken cell; judge the three together, since each alone can remove a valid cell type.
2. **Adaptive cutoffs instead of fixed ones.** The median absolute deviation is `MAD = median(|x − median(x)|)`, and a cell is an outlier when it lies more than n MADs from the median. A widely used published starting point is 5 MADs for total counts and for genes detected, both on the log-transformed values, and 3 MADs for the mitochondrial share combined with a hard ceiling of 8%. These are deliberately permissive defaults, not rules.
3. **Say on which scale the MAD was computed.** The published practice applies it to log-transformed counts and genes; some scripts apply it to raw values, which gives different cutoffs on a skewed distribution. When the user's code and the description disagree, point it out.
4. **The MAD bound is two-sided.** Applied as written to the mitochondrial share, it also removes cells with an unusually low share. If only the high side should be cut, use the upper bound alone.
5. **A cell passes when it is an outlier on none of the metrics**; for mitochondria the effective cutoff is the stricter of the MAD bound and the hard ceiling. In a tissue whose normal mitochondrial share is high, the pair can be far too strict.
6. **Adjust for the biology.** Metabolically active cells such as heart muscle and neurons carry a higher mitochondrial share, and the ceiling is raised for them; what value fits is taken from the literature for that tissue or from the data's own distribution, and stated as a choice.
7. **Be permissive first.** Removing fewer cells protects rare populations, and the filter is re-assessed after cells are annotated. Tightening later is easier than recovering what was dropped.
8. **Gene name prefixes decide whether the metric exists.** Human mitochondrial genes start with `MT-`, mouse with `mt-`; ribosomal genes with `RPS` and `RPL` (lower case after the first letter in mouse); other species use other names. A prefix given as a regular expression to code that expects plain prefixes matches nothing, and the mitochondrial share silently becomes zero. "Found 0 mitochondrial genes" or a share of exactly zero everywhere means the prefix is wrong, not that the cells are perfect.
9. **Different cell groups may need different cutoffs**, each applied to its own group and then combined into one mask. Computing two masks and using neither is a common unfinished step.
10. **Per sample or pooled.** Whether the MAD is computed over the whole dataset or per sample changes the result when samples differ in depth. Ask which was done and treat it as an open choice.
11. **Genes are filtered after cells**: a common default drops genes detected in fewer than 20 cells; lower it when rare populations matter.
12. **Reading the plots.** Total counts against genes detected should rise together; cells with high counts and a high mitochondrial share are suspect; vertical bands suggest batches. In a histogram or violin, two peaks may be mixed cell types or a quality problem, a long tail is normal, and an abrupt edge means the data was filtered before or carries an artefact.
13. **What this step does not do**, to be said at the end: correction for ambient RNA, detection of doublets (recommended for droplet-based data), cell-cycle effects and batch correction. In the published order, low-quality cells are filtered first, then ambient RNA is corrected, genes are filtered, and doublets are detected.

## Output

- The verdict on the filter: reasonable, too strict or too loose, with the metric that shows it.
- A table: `Metric | Median | Cutoff used | Scale | Share removed | Comment`.
- Cells before and after and the share kept.
- What to change, as specific parameter changes, and what to paste back after rerunning.
- The steps still to do, and every assumption made for missing inputs.

## Constraints

- No statistic is described as computed when it was only read from what the user pasted.
- A cutoff is never presented as a standard for all tissues.
- Tool names are examples; the user's own pipeline decides.
- Which cells are biologically valid is the researcher's judgement; this review informs it.
