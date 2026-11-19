---
type: llm
---

PASS if both hold: (1) the reply has saves store a stable, non-display item ID (e.g. an `id` / `item_id` StringName field on ItemData) instead of `display_name` or translated text, with display names coming from localization keys/tr(); and (2) it handles existing player saves that contain the old Chinese display names, e.g. a save version/schema field plus a migration or legacy-name -> ID mapping (including the renamed "小血瓶").
FAIL if saves still identify items by display_name, translated text, resource path index or NodePath; or if the reply gives no way for already-shipped saves with old names to load correctly after the rename.
