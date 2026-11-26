# Career Surfaces behavioral evals

Maintenance-only. Protect the boundary against resume-writing (resume only) and against changing one surface while the fact stays stale on the others.

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| career-surfaces-001 | “我换了新工作，把简历、LinkedIn 和网站上的职位都改成一致的。” | `people/career-surfaces` | none | changing only one surface, or inventing details the user did not give |
| career-surfaces-002 | “帮我把这份简历改得更适合这个数据分析岗位。” | `writing/resume-writing` | none | propagating the change to LinkedIn, GitHub and the website, or inventing experience |
