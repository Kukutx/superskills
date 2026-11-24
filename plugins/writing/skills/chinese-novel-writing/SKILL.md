---
name: chinese-novel-writing
description: Write a Chinese novel of 10 to 50 chapters with outline, character and foreshadowing memory, suspense hooks and self-checks. Use when the user asks for a Chinese novel, not for business copy.
---

# Chinese Novel Writing

Write a complete Chinese long-form novel, 10–50 chapters, from premise to a
checked final draft. The Skill owns the outline, the chapter plan, the
continuity memory, the writing itself and the final validation.

Adapted from `PenglongHuang/chinese-novelist-skill` (MIT); see `maintenance`
`sources.md` for attribution and what was left out.

## Use

Use when the user asks to write a novel, a story in chapters, a serial, or to
continue or validate an unfinished novel project. All genres: 悬疑, 言情, 奇幻,
科幻, 历史 and others.

Not this Skill:

- business, marketing or UX copy -> `writing/marketing-copy`,
  `writing/business-email`;
- a short story under one chapter -> write it directly, without the full
  pipeline;
- a screenplay or video script -> `creative/knowledge-video` or
  `creative/promo-video` for the video form.

## Three golden rules

1. **展示而非讲述**: show through action and dialogue, do not state it directly.
2. **冲突驱动剧情**: every chapter must contain a conflict or a turn.
3. **悬念承上启下**: every chapter ends on a hook into the next.

## Workflow

### 1. Ask in three layers

Ask in rounds, and do not start the outline until the layers below are settled.
Keep each round short; merge follow-ups instead of asking one question at a time.

- **Core positioning** (must ask): premise and genre, protagonist, core conflict.
- **Depth and specification**: world and setting, point of view and tone, core
  theme, intended reader, chapter count, words per chapter. Confirm the
  specification back to the user in one message.
- **Title**: propose candidate titles from the premise elements; the user picks
  one or supplies their own.

### 2. Plan, then confirm once

Create the project folder (for example `./.chinese-novelist/<timestamp>-<小说名称>/`)
with three files, and wait for the user's confirmation before writing Chapter 1:

- `01-大纲.md`: premise, chapter-by-chapter outline (goal, conflict, hook per
  chapter), ending, and the伏笔 (foreshadowing) list with where each one pays off;
- `人物档案.md`: each main character's goal, flaw, relationships, voice, and
  what they do not know;
- `写作计划.json`: chapter count, word budget per chapter, status per chapter.

### 3. Write chapter by chapter

Once the plan is confirmed, write without asking for confirmation between
chapters; the user is the reader, and the job is a finished novel. Before each
chapter, re-read its outline entry and write strictly to it. Keep the chapter
word count inside the plan's budget.

- **Serial mode** (default): write chapters one by one in order.
- **Parallel mode** (optional, for long novels): split chapters into batches and
  hand each batch to a worker with the outline, character sheets and plan as its
  only context; the lead merges and checks continuity afterwards.

### 4. Continuity memory

After each chapter, update the memory in the project folder: what each character
knows and does not know, which伏笔 are planted and which have paid off, timeline
and location of every scene, and any promise made to the reader. A chapter that
contradicts the memory is rewritten, not patched with an explanation. If the
session is interrupted, resume from the plan file: find the first chapter whose
status is not done and continue from there.

### 5. Validate and repair

After the last chapter, check every chapter and repair what fails, up to three
rounds; what still fails is marked `needs_attention` and reported, not silently
accepted:

- word count per chapter within budget;
- every chapter has a conflict or turn, and ends on a hook;
- every伏笔 in the outline is planted and paid off, or explicitly cut;
- no character knows something they should not know yet;
- names, timeline and locations are consistent across chapters;
- the ending resolves the core conflict set up in Chapter 1.

## Output

- The finished novel, one file per chapter in the project folder, plus the
  outline, character sheets and plan kept up to date.
- A short completion report: chapters written, total words, validation result,
  and anything marked `needs_attention`.

## Constraints

- Do not invent the user's premise, genre or protagonist: the three core
  questions are asked before any outline exists.
- Do not start Chapter 1 before the plan is confirmed.
- Do not explain the plot to the reader inside the novel; the hooks and reveals
  do the work.
- Do not resolve a伏笔 by narration alone; it must pay off in a scene.
- Do not pad chapters to reach a word count; a short chapter that keeps its
  conflict and hook is better than a padded one.
