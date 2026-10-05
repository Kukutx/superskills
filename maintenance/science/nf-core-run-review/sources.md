# nf-core Run Review maintenance sources

Maintenance-only. Do not load for normal tasks.

## Policy

- Each row is an official page that was opened and read when the Skill was written or last reviewed. Samplesheet columns and parameters change between releases; on review, re-open each page and change the Skill only where the page changed.
- The upstream plugin pinned older releases (rnaseq 3.22.2, sarek 3.7.1) and differs from the pages below in places: it treats ATAC-seq as paired-end only, while the usage page says the layout is detected from the sheet; it omits `auto` for strandedness. The Skill follows the pages.
- The ATAC-seq quality bands in the upstream plugin (alignment, mitochondrial share, duplication, fraction in peaks, enrichment) carried no source and differ from ENCODE's. The Skill carries ENCODE's published standards and gives no band for the mitochondrial share or the duplication rate, because ENCODE states none.
- The memory meaning of exit statuses other than 137 was not found on an official page and is written as "usually".

## Source register

| Source | Canonical URL | Used for | Last reviewed |
| --- | --- | --- | --- |
| nf-core/rnaseq usage (3.27.0) | https://nf-co.re/rnaseq/usage | samplesheet columns; strandedness values including `auto`; gzipped FASTQ; aligner options; retries with twice then three times the resources | 2026-10 |
| nf-core/sarek usage (3.10.0) | https://nf-co.re/sarek/usage | samplesheet columns; `status` 0 or 1 with normal as the default; pairing by patient; index columns for BAM and CRAM; target regions for exome data | 2026-10 |
| nf-core/atacseq usage (2.1.2) | https://nf-co.re/atacseq/usage | samplesheet columns; first replicate must be 1; merging of repeated runs; single- or paired-end detected from the sheet | 2026-10 |
| ENCODE, ATAC-seq data standards | https://www.encodeproject.org/atac-seq/ | replicates; usable reads per replicate; alignment rate; fraction of reads in peaks; NRF, PBC1 and PBC2; nucleosome-free region and mononucleosome peak; enrichment at transcription start sites by annotation; replicate concordance ratios | 2026-10 |
| nf-core docs, configuring Nextflow for your system | https://nf-core-docs.netlify.app/docs/running/configuration/nextflow-for-your-system | exit status 137 as a reason to raise resources; automatic retry with doubled requests; `resourceLimits` for recent pipelines and `--max_*` parameters for older ones | 2026-10 |
