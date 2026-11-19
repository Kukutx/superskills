# Multilingual Docs behavioral evals

Maintenance-only. Protect the single source language, same-change sync across versions and native quality over literal translation.

| ID | Prompt | Primary | Secondary | Must avoid |
| --- | --- | --- | --- | --- |
| multilingual-001 | “我改了中文版第 3 篇的两段，英文和意大利语也更新一下。” | `writing/multilingual-docs` | none | updating only one target language, or changing facts and numbers while rewording |
| multilingual-002 | “把这篇 README 翻成意大利语，要像意大利开发者自己写的。” | `writing/multilingual-docs` | none | word-for-word calques, reflex connectors such as "Inoltre" or "In sintesi", or adding content the source does not have |
| multilingual-003 | “翻译时发现中文原文这句和事实对不上。” | `writing/multilingual-docs` | none | silently fixing only the translation instead of fixing the source and every version |
| multilingual-004 | “把这句话翻成英文发给同事。” | none | none | invoking `writing/multilingual-docs` and running its multi-version sync and review process for a one-off chat translation |
