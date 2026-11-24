# Diagram Design behavioral evals

Maintenance-only. Protect the diagram/table boundary and the complexity budget.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| diagram-design-001 | “把这个系统架构画成一张图，要能放进技术文档。” | `design/diagram-design` | none | a table or prose instead of a diagram, or more than 9 nodes in one figure |
| diagram-design-002 | “帮我选一张图来展示这组季度销售数据。” | `data/data-visualization` | none | invoking diagram-design for dataset chart selection |
