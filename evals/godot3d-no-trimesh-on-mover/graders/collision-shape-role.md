---
type: llm
---

PASS if the reply identifies the trimesh (concave) collision shape on the moving CharacterBody3D as the main problem and recommends replacing it with a simple primitive (capsule, or cylinder/box) or at most a convex shape for the character, keeping trimesh/concave collision for static world geometry.
FAIL if the reply does not tell the user to replace the trimesh shape on the player, or mentions it only as a minor side note while the main fix is something else (raising physics ticks further, safe_margin tweaks, enabling continuous collision detection, or rewriting the movement code).
