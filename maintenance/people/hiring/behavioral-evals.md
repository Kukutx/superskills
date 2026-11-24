# Hiring behavioral evals

Maintenance-only. Protect the boundary against resume-writing (the user's own application, not hiring others).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| hiring-001 | “招一个后端工程师，帮我写招聘贴、筛简历的标准和面试题。” | `people/hiring` | none | writing the user's own resume |
| hiring-002 | “帮我改一下简历，投这个后端岗位。” | `writing/resume-writing` | none | treating the user's own job application as hiring |
