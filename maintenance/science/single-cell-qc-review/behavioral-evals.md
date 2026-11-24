# Single-Cell QC Review behavioral evals

Maintenance-only. Protect the boundary against single-cell-model-guide (choosing the model, not judging QC cutoffs).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| single-cell-qc-review-001 | “这是单细胞 RNA-seq 的 QC 指标和图，帮我看下过滤标准定得对不对。” | `science/single-cell-qc-review` | none | choosing a scvi-tools model or clustering the cells |
| single-cell-qc-review-002 | “单细胞整合用 scVI 还是 totalVI？训练日志在这里。” | `science/single-cell-model-guide` | none | re-judging QC cutoffs instead of choosing the model |
