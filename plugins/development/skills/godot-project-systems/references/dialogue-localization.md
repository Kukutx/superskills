# Dialogue and Localization Reference

Use for branching dialogue, conditions/choices/effects, dialogue UI, localization keys, translated layout and narrative-tooling boundaries.

Persistent flags/save schema are in `save-persistence.md`; item/progression gameplay state is in `inventory-progression.md`.

## Dialogue truth and UI are separate

Dialogue data/flow expresses speaker, text/localization key, choices, conditions, effects and next-node/end. UI owns portrait/name rendering, typewriter, choices, focus/input, skip/advance and presentation.

Do not embed branching story logic inside Label/Button callbacks.

## Stable content identifiers

Use stable dialogue/quest/content keys; translated display strings are never logic identifiers.

## Conditions and effects

Expose explicit allowed gameplay APIs such as item/flag/quest operations. Do not let dialogue text execute arbitrary unknown script/string commands.

## Persistence boundary

```text
dialogue evaluates condition
-> gameplay API applies effect
-> owning gameplay data changes
-> persistence snapshots durable result
```

Narrative-tool local variables should not become the only truth for inventory/quest state.

## Localization

Stable key != displayed translation. Use flexible Containers, allow longer translations, keep dynamic text out of artwork and provide needed font/fallback coverage. Handle RTL/CJK/special line breaking only for target languages that require it.

## Layout stress

Before final translations, expanded/pseudo-localized text can expose button clipping, dialogue overflow, choice-height problems, fixed-width HUD issues and missing glyphs.

## Typewriter

Typewriter is presentation: full text remains authoritative, skip/advance policy is explicit and rich text/Unicode handling must not slice invalid byte boundaries.

## Choice focus

Keyboard/gamepad paths need predictable default focus, navigation, confirm/cancel and a clear policy while text is still typing. Pair with `ui-ux.md` and `input-controls-accessibility.md`.

## Complexity boundary

Simple linear dialogue can remain project-owned Resource/JSON + UI. Evaluate dedicated tooling only when branching, mutations, editing, translation or content iteration becomes recurring complexity. Keep one narrative source of truth.

## Dialogue QA

Check branch reachability, invalid/missing next nodes, condition true/false paths, repeatable vs one-shot effects, save/reload policy, NPC re-entry, long/missing translations, gamepad choices, skip/typewriter and renamed content IDs.
