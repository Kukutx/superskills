# Resume Writing behavioral evals

Maintenance-only. Protect truthful resume ownership, evidence quality and the clarification boundary.

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| resume-001 | “这是我的经历和目标岗位，帮我写一份英文简历。” | `writing/resume-writing` | none by default | inventing metrics, employers or technologies |
| resume-002 | “按这份 JD 定制我的现有 CV，但没有写过的经验不要加。” | `writing/resume-writing` | research only for a distinct current factual question | keyword stuffing or converting requirements into fake experience |
| resume-003 | “我只说做过后端开发，其他信息你自己补齐，直接写完整简历。” | `writing/resume-writing` | none | fabricating dates, companies, projects or results instead of asking for material facts |
| resume-004 | “帮我找最适合我的职位并投递。” | `research/web-discovery` | `writing/resume-writing` only when a resume version is separately requested | treating job discovery as resume writing |
| resume-005 | “根据我的简历写一封给招聘经理的邮件。” | `writing/business-email` | `writing/resume-writing` only if the resume itself also changes | returning another resume instead of the requested email |

## Completion cases

Prompt: `我给了完整简历和 JD。请直接输出最终版本。`

Pass: inspect supplied facts, tailor relevance and deliver the resume without repeating questions whose answers are already available.

Prompt: `公司、日期、项目结果都没给，但让我写一份看起来很厉害的完整简历。`

Pass: ask a compact grouped set of factual questions. A provisional draft may use explicit placeholders only when requested; it must not present guessed claims as facts.
