# Superskills repository instructions

When modifying this repository:

1. Read `docs/authoring-guide.md` before changing Skill structure or ownership.
2. Treat `skills/meta/skill-router/skill.md` as the only full Skill catalog; do not duplicate it elsewhere.
3. Prefer improving, renaming, splitting or merging an existing owner before creating a new Skill.
4. Default to one `skill.md`. Add one-level `references/` only for real task-dependent runtime depth.
5. Keep source inventories and behavioral regressions in `maintenance/`; do not load/copy them into runtime guidance.
6. Move ownership when splitting content; do not maintain the same rule in multiple references.
7. Do not create prompt-template/example/changelog/compatibility files unless a current decision genuinely requires a separate artifact.
8. If a routing/ownership boundary changes, update the relevant `maintenance/behavioral-evals.md`.
9. Preserve existing project conventions and avoid unrelated rewrites.
10. Before completion run:

```bash
python tools/validate_repo.py
```

Fix validator errors. Treat size advisories as review prompts, not automatic reasons to split files.
