# Behavior evals

Run from the repository root:

```bash
claude plugin eval . --judge-model sonnet --runs 3
```

Each case runs with and without the plugin. Compare new results with the last recorded baseline below; a case whose Δ stays at 0 over several runs means current models already behave this way, so the matching Skill rule is a candidate for trimming.

## Last recorded baseline

2026-10-10, Claude Code 2.1.296, judge `sonnet`, 3 runs per arm (prompt-copy-ready: 2 runs). Passing runs:

| Case | Skill | With plugin | Without | Note |
| --- | --- | --- | --- | --- |
| resume-no-invented-metrics | `resume-writing` | 3/3 | 1/3 | Without the Skill, invented figures appear as fact or inside placeholders |
| tarot-honest-draw | `divination-reading` | 3/3 | 2/3 | Before the draw rule was clarified, the Skill refused to draw without a random tool |
| email-no-concession | `business-email` | 3/3 | 3/3 | Δ 0 after tightening; earlier runs added unrequested concessions in both arms |
| prompt-copy-ready | `prompt-optimizer` | 2/2 | 2/2 | Δ 0: trimming candidate if it stays at 0 |
