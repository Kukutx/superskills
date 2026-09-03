# Superskills repository instructions

When modifying this repository:

1. Read `docs/authoring-guide.md` before changing Skill structure or ownership.
2. Treat `skills/meta/skill-router/skill.md` `## Catalog` as the only complete Skill catalog; every non-Router Skill must appear there exactly once.
3. Prefer improving, renaming, splitting or merging an existing owner before creating a new Skill.
4. Default to one `skill.md`. Add one-level `references/` only for real task-dependent runtime depth.
5. Keep the global clarification/confidence policy in `gpts/kukutx/project-instructions.md`; domain Skills should add only domain-specific required facts and blockers.
6. Keep source inventories, behavioral regressions and rare design rationale in `maintenance/`; never load or copy them into normal runtime guidance.
7. Move ownership when splitting content; do not maintain the same rule in multiple references.
8. Do not create prompt-template, generic examples, changelog or compatibility files unless a current decision genuinely requires a separate artifact.
9. If a routing or ownership boundary changes, update the smallest relevant `maintenance/behavioral-evals.md` case set.
10. Preserve existing project conventions and avoid unrelated rewrites.
11. Before completion run:

```bash
python -m unittest discover -s tests -v
python tools/validate_repo.py
python tools/export_behavioral_evals.py --check
```

Fix errors. Treat size advisories as review prompts, not automatic reasons to split files.
