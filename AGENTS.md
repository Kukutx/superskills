# Superskills repository instructions

When modifying this repository:

1. Read `docs/authoring-guide.md` before changing Skill structure, ownership or a `description`.
2. A Skill lives at `plugins/<category>/skills/<skill>/SKILL.md`; its evals, sources and rare design rationale live at `maintenance/<category>/<skill>/` and are never linked from or copied into runtime files.
3. Treat `plugins/meta/skills/skill-router/SKILL.md` `## Catalog` as the only complete Skill catalog; every non-Router Skill must appear there exactly once.
4. `plugins/<category>/plugin.json` is the only authored copy of a plugin's name, version and description. After adding or removing a category or editing a `plugin.json`, run `python tools/build_manifests.py`; never hand-edit the two generated marketplace files.
5. Prefer improving, renaming, splitting or merging an existing owner before creating a new Skill.
6. Default to one `SKILL.md`. Add one-level `references/` only for real task-dependent runtime depth.
7. A `description` is the only thing most hosts see before triggering: capability first, then when to use it, then the nearest task it must not take; 200 characters at most, plain text without `: `.
8. Skill bodies must stand on their own. `gpts/kukutx/project-instructions.md` holds the global autonomy, escalation and scope policy for ChatGPT only; hosts with a native Skill registry never load it, so domain Skills add domain-specific decision inputs, blockers and validation rules without depending on it.
9. Move ownership when splitting content; do not maintain the same rule in multiple references.
10. Do not create prompt-template, generic examples, changelog or compatibility files unless a current decision genuinely requires a separate artifact.
11. If a routing, ownership, autonomy or blocker boundary changes, update the smallest relevant `behavioral-evals.md` case set under `maintenance/`.
12. When tuning for a newer model, remove duplicated generic process instructions before adding new ones. Domain Skills should encode durable decisions, not generic plan/ask/confirm loops.
13. Preserve existing project conventions and avoid unrelated rewrites.
14. Before completion run:

```bash
python -m unittest discover -s tests -v
python tools/validate_repo.py
python tools/export_behavioral_evals.py --check
```

Fix errors. Treat size advisories as review prompts, not automatic reasons to split files.

These checks are structural. When a `description`, route or reference boundary changes, replay only the affected cases with `python tools/build_live_evals.py` and `claude plugin eval dist/live-evals --ablation none --runs 1 --case <glob>`. Each case is a real model session billed to whoever runs it, so never replay the whole suite as a routine check; without a replay, report the behavior as unverified.
