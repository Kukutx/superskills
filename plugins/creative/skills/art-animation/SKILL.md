---
name: art-animation
description: Animate art with code using 35 art styles, nine narration-animation grammars, shot lists and framing checks. Use for explainer and art-history video, not for script-only video.
---

# Art Animation

## Use

Use when the picture itself must move: an art-history or explainer video rendered in a recognisable art style, a narration-driven animation built from a voiceover script, a breakdown and code recreation of an existing animation, or a scene that passes through several art styles.

A script package with no rendered film belongs to `creative/knowledge-video`. A marketing video belongs to `creative/promo-video`. A still image or a prompt for one belongs to `creative/image-prompt-director`. Laser engraving belongs to `creative/xtool-f1-engraving`.

This Skill is written in English but its source is a Chinese repository; the art-style names and shot-list practice below follow the source. Work in the user's language for the script and on-screen text.

## First decision: lock the look before a single frame

One film, one art style, one colour palette, from the first frame to the last. A clean, slightly slideshow-like film beats a collage that changes style every shot.

- **Style** in one sentence, used for the whole film.
- **Palette** of three to six colours from one set; no blue-purple gradients, deep-purple starfields or neon violet light unless the user explicitly asks for them.
- **Characters.** Either AI-generated frames that pass a quality check, or hands and backs of heads only. Never substitute generic code-drawn cartoon people, and never put a face on a coin, a ball or an ion. A flat-cartoon style may use original semantic SVG characters only when that style is explicitly chosen.
- **Real material first.** Screenshots, photos, footage and source documents go full-frame; code explains, labels and moves the camera. Only a section with genuinely no material is drawn entirely in code or AI-generated.
- **Three directions first.** A new character interpretation or style direction is shown as three options with different compositions, not three recolourings, and the user picks before production.

## Shot list

Write the shot list before building. One row per shot:

| Time | What is on screen (nouns) | What it does (verbs) | Camera | On-screen text (8 words or fewer) | How it is made |
| --- | --- | --- | --- | --- | --- |

Rules for the list:

- The first three seconds are a concrete small scene (a pair of hands, one object doing one relevant thing), not a title card.
- One concrete example runs through the whole film.
- One shot lasts 2–6 seconds; a single parameterised segment holds at most 8 seconds, longer is split.
- Text-led shots are at most 30% of the film.
- Adjacent shots change composition, never the art style.
- Every row names a concrete object and its action. A row with no object is not built yet.

## Camera

The camera is punctuation, not decoration for every line. Before moving it, answer three questions: what should the viewer look at now, is this a transition or an accent, and what did the previous shot do.

- **If it is already readable, do not move.** When the picture itself moves (a line being drawn, a curve growing, footage playing) or the viewer is reading text, hold still. Long still stretches in an explainer are correct, not a fault.
- **Transitions are slow, accents are fast.** Slow push to guide the eye to a detail, lateral move to walk between things, pull back to show the whole or close a section. Fast push, smash-in and whip are accents, reserved for reveals, reversals, key numbers and jokes, and countable in one film.
- **Come back out.** After pushing in, pull out, move sideways, or cut to a different framing. Never push in three shots in a row.
- **One rhythm per film is a failure.** The same slow push every shot reads as slides; a fast push every shot reads as frantic. The camera follows the section's mood: steady for plain exposition, faster at turns and climaxes.
- **Still does not mean empty.** A rejected cut was described as "background too plain, nothing to watch". Something must always be happening: an object moving, material moving, something new being revealed, the camera guiding the eye.
- **Art-style footage is always alive.** One main action per scene plus two repeating motifs, camera allowed to drift slowly. A film that is only still images with transitions between them is not a finished film.

## Nine narration-animation grammars

Pick the grammar by what must be explained, not by what looks impressive:

| Grammar | For |
| --- | --- |
| Whiteboard | Mechanisms and derivations |
| 3b1b-style | Mathematical explanation |
| Storytime | Experience and personal narrative |
| Finance charts | Numbers and trends |
| Vox-style investigation desk | Evidence, documents, real material |
| Kurzgesagt-style | Big ideas with a consistent visual system |
| Art-style scenes | Art and eras |
| Presenter explainer | A host-led explanation |
| Release and keynote | Announcements and product reveals |

At most two segment grammars per film, and every segment uses the same theme and palette. For a new style or a style seen for the first time, study several original works, extract the visual language (brushwork, colour, light, form, space) and validate it on the new subject before building; do not treat a studio name as a single filter.

## The 35–36 art styles

The source holds 35–36 implemented styles plus research cards for further styles, each with its parameters and known pitfalls. Treat a style card as a starting point, not the only way to paint: the same room rendered in many styles is a mechanism demonstration, not a composition. Compose for the new subject, and when a style is attempted, beat its recorded shortcoming first.

When the task is "one scene in many styles" or "one character walking through painting after painting", the mechanism is a long scroll: one segment per world, the character walking left to right, the style changing at each boundary, the crossing itself made into the character's action.

## Delivery checklist (text only)

This Skill keeps a written delivery checklist; no scripts are bundled.

1. **Shot list written and locked** — one style, one palette, first three seconds a concrete scene, every row with an object and an action.
2. **Stills check** — pull frames at two or three timestamps per shot and lay them in a row against the shot list. Any frame that looks borrowed from another film is remade in the film's style.
3. **Normal-speed watch** — watch the whole film at normal speed. Camera smoothness cannot be judged from stills.
4. **Six failure modes, checked before delivery:**
   - Slide-deck film: fixed header, page numbers, bullet points fading in, the same camera move every shot, ending on a centred quote card.
   - Copied demo: composition, character or material lifted from a demo film or sample.
   - No concrete object: an abstract concept rendered only as words and icons.
   - Dead background: large flat colour or starfield that never changes, the subject absent from the frame.
   - Real material redrawn in code instead of shown full-frame.
   - Obvious AI look: blue-purple gradients, a style collage, code-drawn cartoon people, faces on objects.
5. **Independent review** — someone who did not make the film watches only the finished film and writes the problems down before delivery.
6. **Determinism** — every random value uses a seed, so the same moment renders identically twice.

## Constraints

- Do not change art style or palette mid-film.
- Do not use a demo film's composition, character or material in the finished film; demos teach method only.
- Do not deliver a film that is only still images with transitions.
- Do not put a face on an object, and do not use generic code-drawn people as characters.
- Do not claim a film is finished without the normal-speed watch and the independent review.

## Source

Adapted and rewritten from `alchaincyf/huashu-art-motion`, https://github.com/alchaincyf/huashu-art-motion (MIT, v1.3.1). The source's delivery scripts are not copied; only the written delivery checklist above is kept.
