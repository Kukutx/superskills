# Prompt Optimizer Examples

## Example 1: Stop generic answers

### Input

```text
把这个想法优化成可复用提示词：
我想让 ChatGPT 帮我做 xTool F1 雕刻图案，不要废话，要能直接拿去做。
```

### Expected output pattern

```text
Optimized prompt:
You are my xTool F1 engraving design assistant...

Reusable template:
Use this skill.
Use case:
Material:
Size:
Text:
Style:
...

Why it works:
- Defines role
- Defines constraints
- Defines output layers
- Prevents generic inspiration
```

## Bad output

```text
你可以告诉 ChatGPT：请帮我设计一个好看的雕刻图案。
```

Why bad:

- No role.
- No constraints.
- No output format.
- Not reusable.
