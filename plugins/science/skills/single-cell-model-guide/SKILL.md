---
name: single-cell-model-guide
description: Choose and sanity-check scvi-tools models such as scVI, scANVI or totalVI and read their training logs, integration metrics and errors. Use for single-cell integration, not general data analysis.
---

# Single-Cell Model Guide

## Use

Use when someone works with deep generative models for single-cell data from the scvi-tools family and wants to know which model fits their data, whether the data is fit to train on, what a training curve or an integration metric says, how far to trust transferred labels, or what an error means.

Filtering cells before modelling belongs to `science/single-cell-qc-review`. A pipeline run that failed belongs to `science/nf-core-run-review`. Tables and business metrics belong to `data/data-analysis`.

Training needs the user's own machine. Nothing here is trained or verified in the conversation: conclusions rest on what the user pastes, such as the printed data object, key values, the loss curve, metric tables and error text.

## Domain inputs and blockers

The printed summary of the data object (cells, genes, layers, the batch and label columns); the modalities measured; whether the matrix holds raw counts; the number and size of batches; the library version; and for a problem, the metric values or the exact error.

Class names, function signatures and defaults differ between library versions. A call the user's version does not have is checked in the documentation for that version, not asserted.

## Is the data fit to train on

1. **Raw integer counts.** These models expect them. Non-integer values, negative values or a maximum below about ten mean the matrix was normalized or log-transformed: look for a counts layer or the raw slot, and if neither exists say that the model cannot be used on this object.
2. **Protein counts for a joint RNA and protein model are raw too.** Decimals, negatives or a minimum that is not zero mean they were already transformed, and they are exported again as raw counts.
3. **Chromatin accessibility input is binarized**, with sparse peaks and cells filtered first.
4. **Variable genes** are selected with a method that works on counts and takes the batch into account. A couple of thousand genes is the usual starting point and several thousand for multimodal or strongly different datasets; far fewer or far more deserves a question.
5. **Size**: with few cells a deep model has little to learn from; a very small batch is merged with a neighbour; a label with very few cells will not be learned; with a single batch, ask whether correction is needed at all.

## Which model

| Data | Model |
| --- | --- |
| RNA, no labels | scVI |
| RNA, some or all cells labelled | scANVI, preferably initialized from a trained scVI model, with unlabelled cells given one placeholder label |
| RNA and surface protein from the same cells | totalVI |
| chromatin accessibility only | PeakVI |
| RNA and accessibility, paired or partly unpaired | MultiVI |
| spatial spots plus a single-cell reference | DestVI |
| spliced and unspliced counts, for velocity | veloVI |
| RNA datasets with substantial batch effects, such as different technologies or studies | sysVI |

For moderate differences such as chemistry versions of one platform, the plain model with the batch as a covariate is usually enough.

## Reading training

- Look at the training and validation loss together. Validation rising while training falls is overfitting: stop earlier, add dropout, or make the model smaller.
- A loss that becomes undefined is first a data problem: cells or genes with no counts at all, or a filter that left them in.
- There is no universal number that means "converged"; say that the curve has flattened, not that a threshold was met.
- Running out of memory: smaller batches, a smaller model, fewer genes, then the processor instead of the graphics card.
- Scale the settings to the data: a small dataset wants a smaller latent space, fewer layers, more dropout and more passes; a very large one wants bigger batches and fewer passes. The values are choices to report, not constants.

## Judging integration

- Measure both sides: how well batches mix, and how well biology is preserved (agreement of clusters with known labels, separation of cell types). A plot in which batches overlap proves nothing about over-correction.
- Each metric has a direction, and similarly named ones from different packages can point opposite ways; state which implementation was used before reading a value.
- **Batches not mixing**: check shared genes and batch sizes first, then more variable genes, longer training or a larger latent space.
- **Over-correction**, where distinct cell types merge: use labels with the semi-supervised model, shrink the latent space, or reconsider which variable is treated as the batch.
- **One batch dominating**: look at the distribution, down-sample to the smallest batch if needed, or use labels to protect rare types.

## Transferring labels from a reference

- Query and reference must use the same genes and the same gene identifiers; unify identifiers first. When less than about half of the reference genes are present in the query, the mapping is unreliable. How missing genes are filled depends on the function used, so check it instead of assuming zeros.
- The library version should match the one the reference was trained with.
- Report the distribution of confidence, taking the highest predicted probability per cell. Cells under one half are low confidence; a stricter analysis uses a higher bar, and the bar used is stated. Many low-confidence cells mean a cell type absent from the reference or a mismatched reference, not a failure to be thresholded away.
- Check the transferred labels against known marker genes.

## Other checks

- **Differential expression**: say which thresholds defined a marker (the false-discovery cut and the effect size), and whether only up-regulated genes were kept.
- **Spatial deconvolution**: the reference comes from matching tissue, contains every expected cell type and shares enough genes with the spatial data. Every spot receiving the same type suggests over-smoothing; undefined proportions suggest a missing type.
- **Velocity**: confirm the spliced and unspliced layers exist. Evaluation is qualitative: do the streamlines follow the known direction of differentiation, does latent time agree with marker genes. No signal is first a question of unspliced depth; a reversed direction is corrected by setting the root cells.
- **Errors**: a complaint that the matrix should contain integers points at the counts layer; a key that is not found points at a column name; a setup function that cannot be found usually means code written for another major version, where it was called differently.

## Output

The model recommended and why; a pass or fail on each data check with the value it rests on; the reading of the curve or metrics; the specific change to make; what to run and paste back; and which statements depend on a version that was not checked.

## Constraints

- Nothing is described as trained, computed or verified here.
- No function signature, class location or default is stated as fact for an unchecked version.
- No numeric pass line is invented for convergence or integration quality.
- The biological interpretation is the researcher's.
