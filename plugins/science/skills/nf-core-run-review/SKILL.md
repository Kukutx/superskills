---
name: nf-core-run-review
description: Review an nf-core pipeline run from pasted samplesheets, logs and QC tables for rnaseq, sarek or atacseq, covering sheet errors, exit codes and metrics. Use for checking a run, not for running one.
---

# nf-core Run Review

## Use

Use when someone is preparing or debugging a run of an nf-core pipeline and pastes the samplesheet, the command, the error or the QC summary: is the sheet valid, why did a task die, why is the alignment rate low, did the run actually finish, do the metrics look usable.

A defect in the user's own software belongs to `development/bug-diagnosis`. Quality control of single-cell data belongs to `science/single-cell-qc-review`. Interpreting downstream statistics belongs to `data/data-analysis`.

Nothing is executed here. No environment check, test profile or download is described as having been run.

## Domain inputs and blockers

The pipeline and **its version**, the command line, the samplesheet, the failing task's name with its exit status and the last lines of its log, and the QC table when the question is about quality.

Columns, parameters and defaults change between releases. The facts below were read on the pipelines' usage pages and are checked against the usage page for the user's version before being relied on; when the version is unknown, say that first.

## Choosing the pipeline

Bulk RNA-seq goes to `rnaseq`; ATAC-seq to `atacseq`; whole-genome, exome and targeted DNA for variant calling to `sarek`. Other assays have their own pipelines and their own sheets.

Before a run the user confirms the reference genome and that it matches the species and the build of any annotation or target file; the aligner; for `sarek` the variant-calling tools and, for exome or targeted data, the file of target regions.

## Samplesheets

| Pipeline | Columns | What goes wrong |
| --- | --- | --- |
| rnaseq | `sample`, `fastq_1`, `fastq_2`, `strandedness` | strandedness is one of `unstranded`, `forward`, `reverse`, `auto`; files must be gzipped FASTQ; the same `sample` on several rows is merged as repeated sequencing of one library |
| sarek | `patient`, `sample`, `lane`, `fastq_1`, `fastq_2`, optional `status` | `status` is 0 for normal and 1 for tumour and **defaults to normal when left out**; a pair is the same `patient` with different `sample` and `status`; starting from aligned files needs the index column beside the BAM or CRAM |
| atacseq | `sample`, `fastq_1`, `fastq_2`, `replicate` | the first replicate of a group must be 1; rows sharing sample and replicate are merged as repeated sequencing; single- or paired-end is detected from the sheet |

- Give full paths. "No such file" is first a path problem: a relative path, a typo, or a file not visible from where the tasks run.
- **Tumour or normal is confirmed by the user for every sample.** A helper that guesses it from file names, or leaves it blank, silently turns a tumour into a normal, and a somatic caller then reports nothing. Empty somatic output is checked against `status` and pairing before anything else.
- A sheet that a helper script validated is still read by eye; the pipeline's own schema is the authority.

## Failures

- **Exit status 137** means the task was killed for memory; 143 and similar kill signals usually mean memory or time. Pipelines retry such tasks with a larger request, so a task that still fails has hit the ceiling: raise the limit for that process, or cap requests to what the machine has. Recent releases cap with a `resourceLimits` block in the configuration; older ones used `--max_memory`, `--max_cpus` and `--max_time`. Which applies depends on the version.
- **Exit status 1** is a general error: read the task's own error output and the run log, starting from the first error, not the last.
- A container that cannot be pulled is a network, registry or disk-space problem, not a pipeline bug.
- A low alignment rate is first a mismatch between genome and species, then adapter or contamination. An index-building failure is usually memory or a truncated reference file.
- Use the resume option after fixing the cause, so finished tasks are reused. Deleting the work directory throws that cache away and is suggested only when the user wants a clean restart.

## Did it work

A finished run has the pipeline's completion message in the log and a MultiQC report. Then check the outputs that matter: for RNA-seq a count matrix that is not empty and has every sample; for variant calling a file per sample or pair with a plausible number of calls; for ATAC-seq peaks and signal tracks for every replicate.

Reading ATAC-seq quality against the ENCODE consortium's published standards, which is the reference to name when a band is quoted:

| Measure | ENCODE standard |
| --- | --- |
| replicates | two or more biological replicates |
| usable reads per replicate | 50 million non-duplicate, non-mitochondrial aligned reads for paired-end, 25 million for single-end |
| alignment rate | above 95%; above 80% may be acceptable |
| fraction of reads in peaks | above 0.3; above 0.2 is acceptable |
| library complexity | NRF above 0.9, PBC1 above 0.9, PBC2 above 3 |
| fragment lengths | a nucleosome-free region and a mononucleosome peak must both be present |
| enrichment at transcription start sites | depends on the annotation: for GRCh38 RefSeq below 5 is concerning, 5 to 7 acceptable, above 7 ideal; for mm10 RefSeq below 10, 10 to 15, above 15 |
| replicate concordance | rescue and self-consistency ratios both below 2 |

These describe a consortium's bar for deep, reference-quality data; a smaller experiment can be usable below the read depth, and each sample is also judged against the others in its batch. The mitochondrial share and the duplication rate have no ENCODE band: report them and compare across samples. Low fraction in peaks points to library complexity; high duplication is common with little starting material; fewer than two replicates leaves consensus peaks unsupported.

For public data: an accession showing no runs may hold only processed files; a series with several data types needs the user to choose the subset first.

## Output

The diagnosis first; the evidence line from the sheet or log; the specific change (the corrected rows, the parameter or configuration block); what to rerun and what to paste back; and what could not be judged from the material.

## Constraints

- No parameter name or default is asserted for a version that was not checked.
- No command that deletes data, changes system settings or installs software is given without saying what it removes or changes.
- Clinical interpretation of variants is outside this review.
- Results are the user's to validate; publications cite the pipeline as its own citation file directs.
