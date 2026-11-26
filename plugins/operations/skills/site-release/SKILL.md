---
name: site-release
description: Ship a site change end to end through shared and personal branches, checks by change kind, local preview, CI gates and live verification. Not for a generic go or no-go gate.
---

# Site Release

## Scope

Use to take a change to a personal or site repository from the author's machine to the live site: branching, checks, local preview, CI and reviews, through to live verification. What the site may say belongs to `people/career-surfaces` when installed. A generic go or no-go gate with no project release workflow stays with `operations/release-checklist`. The repository's own skills and docs stay the reference for that repository; this Skill adds the release pipeline across its branch model.

## Configuration the user supplies

Branch names, repository paths, hosting, preview ports and script names differ per site; read them from the repository, not from this Skill. What this Skill fixes is the shape of the pipeline: which changes share a branch line and which stay personal, which checks run for which kind of change, and what must be true before a merge and after it goes live.

## Branches

- A shared change (source, scripts, checks, docs, schemas, CI, shared skills) branches from the shared integration branch, merges there, then travels integration to main, then main merges into the personal branch, which deploys.
- Personal content only (content files, personal baselines) branches from the personal branch and merges back into it.
- Personal work that needs a shared change waits for main: the personal check fails the branch boundary until main has the shared commits; rerun it after main merges.
- Bring shared work into personal by merging, never by cherry-picking. When a merge conflicts on shared files whose personal side equals the integration branch's previous version, take the integration side and confirm the staged diff shows nothing outside the personal baselines.
- Several independent changes can travel together through one integration to main to personal round; each CI round costs real time, so batch deliberately.
- Dependency updates: merge their branches into one dated branch from the integration branch and open one pull request; their own pull requests show as merged when it lands.
- After a merge that changes the lockfile, stop the local server (the OS may lock installed modules), reinstall from the lockfile, then build.

## Editing safely

- Edit text with a small script (read as UTF-8, replace an exact string after checking it exists, write) or the file-write tool. Never use a shell text command that re-encodes UTF-8 files: it corrupts non-ASCII text such as accented letters and CJK characters. When that happens, restore the file from version control and redo the edit.
- Redirect command output through a form that preserves encoding; never through a shell redirect that writes UTF-16.
- Keep scratch files only in the repository's scratch folder (commit messages there, used with `git commit -F`); delete them at the end, keeping the files the repository itself owns.
- No worktrees. No checkout or restore of the user's files, except to undo damage of your own.
- Images for your own eyes go in a temporary folder the user can see, staged and read; remove the folder at the end.

## Checks by kind of change

- Always: the repository's full check (lint, branch boundary, content tests, build). Without the build: lint, boundary check, content tests.
- Visible change: build the content; look at phone, tablet and desktop widths with motion on and over time, and with reduced motion. Then, after a build, run the visual comparison; update baselines only for an intended change, opening every replaced image.
- Behaviour: run the functionality checks against a running build, plus a probe script for the exact thing changed.
- Resume: the repository's resume skill when it has one.
- CI files: run the CI-impact tests. External actions are pinned to a full commit SHA with the version in a comment; a local action is written with an id line then a path.
- Probe scripts live in the scratch folder, use the repository's browser helper to resolve the browser path, and disable the headless scrollbar hiding when scrollbars matter.

## Local preview

- One preview server serves the last build on a fixed port. Rebuild on the branch the user should see and restart it after switching branches; a build of another branch replaces what they are looking at.
- For side checks use a development server on a different port, which leaves the build alone, and stop it afterwards.

## CI, reviews and merging

- The required checks on the main and personal branches also require every review conversation resolved. Review comments block the merge: fix the finding (here or in the next round), then reply and resolve them only with the user's OK.
- Wait on pull-request checks and prepare the next branch meanwhile. A job stuck in setup: cancel the run, wait until it completes, then rerun the failed jobs. When setup is slow again, check that workflow's last run first; it can be started by hand from the hosting's actions view.
- Merge with a merge commit, in order. After the personal merge, wait for the deploy status on the merge commit, then check the live site with a probe of the changed behaviour, not just a status code.

## Reporting

- One line per step while it runs.
- At the end: what is live, what the user can try, anything pending or decided for them. List every visible change and mark the ones they did not ask for.

Source: fused from the author's Notion skill `folioweave-release` (2026-11), generalized; all FolioWeave-specific paths, branch names, hosting and script names were stripped to placeholders and examples.
