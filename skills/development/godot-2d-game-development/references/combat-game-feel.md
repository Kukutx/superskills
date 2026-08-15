# Combat and Game Feel Reference

Use this reference when the mechanic already exists or is being implemented and the task involves combat, impact, responsiveness, hit-stop, knockback, camera shake, flash, particles or other feedback.

## 1. Separate combat truth from feedback

Combat logic decides:

- whether an attack is allowed;
- when the hitbox is active;
- what was hit;
- damage / armor / resistance / crit rules;
- knockback intent;
- i-frames;
- death / stagger / combo state.

Feedback reacts to the result:

- hit sound;
- flash;
- particles;
- screen shake;
- hit-stop;
- damage popup;
- squash/stretch;
- recoil animation.

Do not make particles, animation or camera shake the source of combat truth.

## 2. Hitbox / hurtbox baseline

For typical 2D action combat:

- use `Area2D` for attack hitboxes and hurtboxes;
- use collision layers/masks for filtering;
- activate a hitbox only during the intended attack window;
- deactivate it immediately afterward;
- pass a structured attack/damage payload instead of directly editing a target field from the attacker;
- let health/damage handling own i-frames and death decisions;
- disable or retire collision on dead entities cleanly.

Avoid:

```text
target.health -= 10
```

Prefer a clear boundary such as:

```text
Hitbox -> Hurtbox -> take_damage(attack_data) -> health_changed / died
```

The exact class names do not matter; ownership does.

## 3. Synchronize attack windows

An attack should have explicit phases:

```text
startup -> active -> recovery
```

The hitbox is active only during `active`.

Prefer AnimationPlayer method/property tracks or a single authoritative attack timeline when frame timing matters. Avoid several unrelated timers trying to approximate the same moment.

For pixel/cel animation, a frame event can activate the hitbox and trigger SFX/VFX on the exact impact frame.

## 4. I-frames and repeated overlap

A hurtbox can overlap a hitbox for several physics frames. Without a gate, one visual swing may deal damage repeatedly.

Use one of these explicit policies:

- one hit per attack instance;
- short target i-frame window;
- per-target cooldown for multi-hit attacks;
- intentionally repeated ticks for damage-over-time areas.

Do not leave the policy implicit.

## 5. Knockback and recoil

Knockback is gameplay; visual recoil is presentation.

Keep them distinct:

- gameplay knockback changes target motion/state;
- sprite recoil can briefly offset or squash the visual child;
- weapon recoil can animate the weapon/hand without moving the collision body.

Scale knockback by event type and game design. Do not add physics impulses blindly if the character controller is velocity/state driven.

## 6. Hit-stop

Hit-stop is a very short slowdown/freeze that emphasizes a confirmed impact.

Rules:

- trigger once per meaningful impact, not every process frame;
- keep duration short;
- recovery timer must ignore the slowed game clock if global `time_scale` is used;
- always restore the previous/global time state safely;
- do not use blocking sleep/delay;
- preserve or buffer important player input when the game design expects responsiveness.

Suggested starting ranges are only tuning references, not rules:

```text
light hit:  ~20–40 ms
medium hit: ~40–70 ms
heavy hit:  ~70–120 ms
```

Tune by playtesting. Frequent combat usually needs shorter values.

## 7. Camera shake

Use shake for impact, not as constant noise.

Good model:

```text
impact event -> add bounded trauma/intensity -> camera samples smooth offset -> intensity decays to zero
```

Prefer smooth noise or controlled oscillation over a brand-new random offset each frame.

Scale shake by importance:

- small: tiny positional shake or none;
- medium: short positional shake;
- large: stronger position + optional slight rotation/zoom punch.

Never shake the actual physics body.

Provide a reduced-screen-shake option when the game uses strong or frequent camera motion.

## 8. Flash and hit material

A short white/bright flash is one of the cheapest readable hit confirmations.

Preferred pattern:

```text
confirmed hit -> set shader/material parameter -> short unscaled/normal-time recovery -> reset
```

Keep it brief. On repeated hits, replace/restart the existing effect cleanly instead of stacking material Tweens indefinitely.

For pixel art, preserve sharp edges and avoid glow/blur that destroys the sprite silhouette unless the art direction intentionally uses it.

## 9. Particles and impact FX

Impact FX should answer at least one question:

- where did the hit happen?
- what direction did force travel?
- what kind of damage occurred?
- how important was the event?

Useful layers:

- small spark/slash burst at contact point;
- directional debris/blood/magic particles;
- weapon trail during active frames;
- landing dust;
- death burst.

Do not cover the target so completely that the player cannot read its pose or next attack.

## 10. Sound

A convincing hit often depends more on sound than on extra particles.

For attacks, separate when useful:

```text
wind-up / whoosh -> contact impact -> enemy hurt -> environment response
```

Avoid one identical sample at exactly the same pitch for very frequent events. Small controlled variations can reduce repetition.

## 11. Layer feedback deliberately

A satisfying hit often uses several tiny responses in a very short window, but do not enable all of them by default.

Start with:

```text
impact sound + contact FX + knockback
```

Then add, only if needed:

```text
flash -> short hit-stop -> camera shake -> popup -> extra secondary FX
```

Use importance tiers:

| Tier | Typical feedback |
| --- | --- |
| Small | sound + tiny FX |
| Medium | sound + FX + recoil/knockback + small shake |
| Heavy | strong sound + FX + short hit-stop + stronger shake + flash |
| Boss/critical | authored bundle; stronger but still readable |

## 12. Movement feel beyond combat

The same principles apply to non-combat events:

- jump: immediate launch pose + small stretch;
- land: squash + dust + optional tiny camera response;
- dash: trail + short stretch + directional sound;
- pickup: pop/ease + sparkle + audio;
- button press: scale/color tween + click sound.

Feedback must return to rest. Permanent exaggeration stops feeling like feedback.

## 13. Common failure modes

- Hit-stop is so long that controls feel broken.
- Shake is random static instead of decaying motion.
- Every small hit uses maximum effects.
- A Tween is started on the same property every hit without cancelling the previous one.
- Hitbox stays active for the whole animation.
- Attack animation ends but character state never exits recovery.
- UI damage popups create unlimited nodes and are never freed/reused.
- Feedback is added before the underlying hit detection is reliable.

## 14. Validation

Test repeated real gameplay, not a single staged hit.

Verify:

- one intended attack produces the intended number of damage events;
- fast repeated hits cannot permanently freeze time;
- hit-stop always restores normal speed;
- shake decays fully to neutral;
- flash/tween state returns to default;
- input is still accepted as designed;
- effects remain readable when several enemies are hit together;
- low-value actions do not visually overpower high-value actions.

## Upstream inspiration

Condensed from `godot-combat-system` in `thedivergentai/GD-Agentic-Skills` and `game-feel` in `gamedev-skills/awesome-gamedev-agent-skills`. The main retained ideas are explicit hit windows, structured damage handling, i-frame policy, layered event feedback, decaying camera trauma, short real-time-safe hit-stop and proportional feedback intensity.