# Godot 2D Reference

Use this reference for Godot-specific 2D implementation: nodes, movement, physics, TileMap, camera, particles, shaders and audio. Keep the project’s existing language and architecture unless there is a concrete reason to change them.

## 1. Scene and node ownership

Prefer small scene composition over one giant script.

Typical responsibilities:

- `CharacterBody2D`: movement and collision response.
- `CollisionShape2D`: body collision.
- `Area2D`: hitbox, hurtbox, pickup, trigger and detection zones.
- `AnimatedSprite2D` or `Sprite2D`: visual sprite.
- `AnimationPlayer`: property/method/audio/VFX synchronization.
- `AnimationTree`: only when transition/blending complexity justifies it.
- `Camera2D`: camera follow and visual offset.
- `Control` nodes: HUD and menus, not Node2D positioning hacks.

A child component may own one concern such as health, hit detection or audio, but do not split trivial logic into dozens of one-method nodes.

## 2. Physics and movement

For CharacterBody2D gameplay movement:

- Read input intent, update velocity and call `move_and_slide()` from `_physics_process()`.
- Treat physics state as authoritative; animation should read movement state rather than secretly move the body unless the design explicitly requires root-motion-like behavior.
- Use input buffering / coyote time only when the game benefits from them; do not add them to every genre by habit.
- Prefer collision layers/masks over groups for physics filtering.
- Change collision shapes safely; when enabling/disabling during a physics callback, use deferred changes where required by Godot.
- Avoid non-uniform scaling on collision shapes. Adjust the shape resource dimensions instead.

When debugging collision problems, inspect:

1. layer and mask bits;
2. monitoring / monitorable for Area2D;
3. enabled/disabled CollisionShape2D state;
4. actual world position and scale;
5. whether the expected callback is body-vs-area or area-vs-area.

## 3. Input

Use named actions in Input Map instead of hardcoded key codes.

Prefer gameplay-facing actions such as:

```text
move_left
move_right
move_up
move_down
jump
attack
secondary_attack
dash
interact
pause
```

Do not embed hit resolution or large gameplay branches directly in `_input()`. Input should express intent; gameplay/state systems decide whether the action is allowed.

For action games, consider a small input buffer when animation recovery or hit-stop could otherwise make valid presses feel lost.

## 4. TileMap and 2D world

For current Godot 4 projects, prefer the project’s existing `TileMapLayer` / tile workflow rather than introducing a second map system.

Keep visual tiles, collision, navigation and interactive props conceptually separate even if they share one authored tileset.

Useful rules:

- Reusable scenery belongs in tiles or reusable scenes, not copied node trees.
- Interactive objects, enemies and pickups should usually remain scenes instead of being baked into decorative map art.
- Collision should match gameplay silhouette, not every pixel of the artwork.
- Y-sort / draw-order rules should be explicit in top-down games.
- Generated map art should not replace editable collision, exits, spawn points or encounter metadata.

## 5. Camera2D

Separate **camera framing** from **camera feedback**.

Framing owns:

- follow target;
- smoothing;
- dead zone / look-ahead;
- bounds;
- zoom.

Feedback owns:

- shake / trauma;
- short zoom punch;
- impact offset.

Never shake the player body to fake camera shake. Apply shake to Camera2D offset/rotation or a dedicated visual pivot so physics and aiming remain stable.

For repeated impacts, accumulate a bounded intensity value and decay it smoothly instead of picking a new random position every frame.

## 6. Tween

Use Tween for short runtime effects such as:

- UI button pop;
- damage number rise/fade;
- sprite squash/stretch;
- recoil recovery;
- short color/alpha changes;
- panel transitions.

If an effect can be retriggered before finishing, keep a reference to the Tween and kill/replace it before starting another Tween on the same property. Two Tweens fighting over one property create unstable presentation.

Use easing deliberately:

- ease-out: settle quickly and naturally;
- back/overshoot: small pop or UI emphasis;
- elastic: rare, exaggerated effects;
- linear: continuous mechanical motion where constant speed is intentional.

## 7. Particles and VFX

Use particles to clarify events, not to hide them.

Examples:

- landing dust;
- hit sparks;
- dash trail;
- pickup burst;
- death burst;
- environment ambience.

For impact FX:

- spawn at the actual contact/event position;
- orient directional particles using the hit direction when useful;
- keep lifetime short;
- reuse/pool expensive repeated scenes when profiling shows allocation pressure;
- avoid filling the screen with full-alpha particles that destroy silhouette readability.

## 8. CanvasItem shaders

2D shaders are useful for presentation effects such as:

- hit flash;
- palette swap;
- dissolve;
- outline;
- damage tint;
- simple water/fire distortion;
- screen-space transitions.

Keep gameplay state outside the shader. Code or AnimationPlayer should drive a small set of shader parameters.

If multiple instances need independent values, make sure the material/resource is not unintentionally shared.

For pixel art, avoid effects that introduce unintended blur, subpixel shimmer or inconsistent pixel scale.

## 9. Audio

Treat sound as part of gameplay feedback.

Prefer event-driven SFX:

- attack wind-up;
- impact;
- hurt;
- dash;
- jump/land;
- pickup;
- menu confirm/cancel.

Keep repeated sounds from becoming machine-gun identical: use a small controlled pitch/variant range when appropriate.

Use audio buses for broad groups such as Master / Music / SFX / UI rather than adjusting every AudioStreamPlayer globally from arbitrary scripts.

## 10. Signals and events

Signals are useful when one gameplay event has multiple listeners.

Good examples:

```text
health_changed
character_died
attack_connected
item_picked_up
score_changed
```

Avoid turning every method call into a global event. If one object owns another directly and the relationship is simple, a direct method call is often clearer.

## 11. Performance priorities for 2D

Do not optimize blindly. First inspect what is actually expensive.

Common 2D pressure points:

- too many active nodes / process callbacks;
- huge transparent sprites causing fill-rate waste;
- excessive particles/overdraw;
- large uncompressed textures;
- repeated runtime allocation of projectiles/FX;
- per-frame node lookups in hot loops;
- unnecessary UI polling every frame.

Cache frequently accessed nodes with `@onready` or equivalent project conventions.

Use MultiMesh / GPU-heavy techniques only when entity counts actually justify the complexity.

## 12. Minimum validation

After a change, verify the smallest relevant set:

- scene opens without parse/resource errors;
- player input still works;
- physics behavior is stable at runtime;
- collisions/layers behave as intended;
- animation and events trigger once at the expected moment;
- repeated triggering does not leak nodes or stack Tweens indefinitely;
- resizing / camera movement does not reveal obvious layout or pixel-scaling defects.

## Upstream inspiration

Condensed from Godot-specific patterns in `thedivergentai/GD-Agentic-Skills`, especially the 2D physics, CharacterBody2D, camera, Tween, particles, shader, audio and animation domains. For exact signatures and version-sensitive behavior, check the Godot documentation that matches the project version.