# Bug Diagnosis Prompt Template

## Standard request

```text
Use the Bug Diagnosis Skill.

Symptom:
Expected behavior:
Actual behavior:
Error logs:
Relevant code:
Recent changes:
Environment:
```

## Minimal request

```text
帮我诊断这个 bug，给我最可能原因、验证步骤和修复建议：

[bug details]
```

## Production issue request

```text
Use the Bug Diagnosis Skill.

Production symptom:
Affected users:
Error logs:
Recent deployments:
Environment differences:
Rollback possible: yes / no
Output: likely cause, fast checks, mitigation, fix, prevention
```
