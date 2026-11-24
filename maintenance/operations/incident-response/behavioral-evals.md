# Incident Response behavioral evals

Maintenance-only. Protect the boundary against bug-diagnosis (one bug, not an outage) and crisis-communications (the public statement, not the incident itself).

## Routing matrix

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| incident-response-001 | “网站挂了，500 错误，先帮我处理这次故障，写个状态更新和事后复盘。” | `operations/incident-response` | none | diagnosing it as a single code bug, or writing the public statement as the whole job |
| incident-response-002 | “帮我看看这段代码为什么报空指针。” | `development/bug-diagnosis` | none | opening an incident response for one bug |
