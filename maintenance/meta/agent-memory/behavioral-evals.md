# Agent Memory behavioral evals

Maintenance-only. Protect the boundary against skill-builder (authoring skills, not remembering) and against inventing or half-forgetting memories.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| agent-memory-001 | “记住，以后我写东西都用中文。” | `meta/agent-memory` | none | answering only in this reply and asking again next session instead of writing it to the memory files |
| agent-memory-002 | “上次我们决定的那个方案是什么？” | `meta/agent-memory` | none | inventing a decision that was never recorded |
| agent-memory-003 | “把你记得的关于我的那条偏好删掉。” | `meta/agent-memory` | none | keeping a copy in the dated notes while claiming it is forgotten |
