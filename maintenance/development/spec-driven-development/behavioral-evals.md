# Spec-Driven Development behavioral evals

Maintenance-only. Protect the boundary: direction-open work starts here, decided work goes to implementation-plan.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| spec-driven-development-001 | “我们要做一个新功能，方向还没定，先帮我把项目原则写下来，再写一份规格，然后把含糊的地方问清楚。” | `development/spec-driven-development` | none | jumping to a file-level task breakdown before the spec is clarified |
| spec-driven-development-002 | “方向已经定了，帮我把这个功能拆成文件级任务和测试。” | `development/implementation-plan` | none | invoking spec-driven-development for task breakdown on decided work |
| spec-driven-development-003 | “这个规格里有几处含糊的地方，问我最多五个问题，问完就别再问了。” | `development/spec-driven-development` | none | inventing answers to clarification questions, or asking more than five |
