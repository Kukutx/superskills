# Code Review Prompt Template

## Standard request

```text
Use the Code Review Skill.

Language/framework:
Code or diff:
Expected behavior:
Risk area:
Output depth: brief / normal / deep
```

## Pull request request

```text
Use the Code Review Skill.

PR goal:
Diff:
Files changed:
Known risk areas:
Output: verdict, critical issues, suggested patch, validation checklist
```

## Minimal request

```text
帮我 review 这段代码，优先找真实 bug 和安全风险：

[code]
```
