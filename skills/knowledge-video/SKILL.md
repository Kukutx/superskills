---
name: knowledge-video
description: Turn one knowledge point into a narrated, source-backed short explainer video package (45 s to 5 min) — topic hook, script template, duration tier, fact list with sources, narration, storyboard, visual style and publish copy. Use when the user wants a 知识短片 / 科普短视频 / 知识大赏-style video, or to turn a concept, history story or principle into a short narrated explainer.
---

# Knowledge Video

One episode = **one knowledge point → one narrated short film** where every fact on screen has a source.

Adapted from `andyhuo520/vibe-knowledge` (MIT); see maintenance `sources.md` for attribution and what was left out.

## Scope

Owns topic shaping, script template choice, duration, fact sourcing, narration, storyboard, style choice and the publish pack.

Not this Skill:

- evidence synthesis as its own deliverable -> `research-brief`;
- a single still image prompt -> `image-prompt-director`;
- a course series, finance talking-head or brand promo: use this Skill's method only if the user still wants a knowledge short.

## Two output levels

| Level | When | Output |
| --- | --- | --- |
| **Script package** (default) | any host, including claude.ai web | facts list, narration by beat, storyboard, style card, publish copy; optionally a one-file HTML animatic of the cold open |
| **Rendered film** | the user runs Claude Code with the upstream render pipeline installed | the package above, then voice, code-rendered 1080p60 film and QA; see `references/rendering.md` |

Do not claim a rendered video exists unless a render actually ran. Do not ask the user to install the pipeline when a script package answers the request.

## Workflow

```text
topic -> template + duration + style (pick defaults, say which)
-> facts list -> narration by beat -> self-review
-> storyboard -> publish copy
-> (rendered level only) voice -> film -> QA
```

1. **Shape the topic.** Check three things: can the viewer guess or choose something in the first 3 seconds; is there one prop that can carry the whole film; is there a reversal. If the topic fails all three, propose 2–3 sharper angles and pick the best one.
2. **Pick template, duration and style** from `references/templates.md`, `references/duration.md` and `references/styles.md`. Choose the recommended option, state it in one line with the reason, and continue; the user can redirect.
3. **Facts first.** Build the fact list before writing narration (`references/script.md`). Every number, name, year and quotation gets a row with its source and tier. Without web access, mark each row `待核实` and name where to check; never fill a source from memory as if verified.
4. **Write narration by beat** following the template skeleton and the word budget for the chosen duration.
5. **Self-review** against the checklist in `references/script.md`: hook in 3 s, title delayed, one prop throughout, no unsourced claim on screen, on-screen text ≤8 characters per group, ending question answerable in one word.
6. **Storyboard** each beat: background layer, motion layer, information layer; mark which shots are code-drawn and which would need generated imagery.
7. **Publish copy** from `references/publish.md`.

## Non-negotiables

- No source, no screen. Disputed facts show both versions ("一说……").
- AI-generated people and scenes are labelled 「AI 示意」; never generate a living real person's face.
- Open on something the viewer can guess, choose or recognise within 3 seconds; the title comes after the hook.
- Close by returning to the opening and handing the viewer a question answerable in one word or a binary choice (搬 / 不搬, A / B); an open essay question does not count.
- Narration tells the story; the screen carries keywords, numbers and sources only.
- Narration budget: about 5.5 Chinese characters per second of film (2:00 ≈ 660 characters).
- Paid generation (image/video/music credits) needs a listed quote and the user's explicit yes before it is submitted.
- Voice cloning only from the user's own voice or one they have explicit permission to use.
- Defaults over questions: only the paid-generation and voice-consent points above wait for the user.

## References

| Need | Load |
| --- | --- |
| choose and write a script template | `references/templates.md` |
| pick duration and word/beat budget | `references/duration.md` |
| fact list, narration rules, sync rules, review checklist | `references/script.md` |
| choose a visual style | `references/styles.md` |
| title, tags, description, cover | `references/publish.md` |
| full render pipeline in Claude Code | `references/rendering.md` |
