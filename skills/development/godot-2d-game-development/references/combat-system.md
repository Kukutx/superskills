# Combat System Reference

Use for 2D combat correctness: attack state, startup/active/recovery, hitbox/hurtbox, damage payload, repeated-contact policy, combo/cancel and handoff to Health/Vitals and movement.

If mechanics are correct but feedback feels weak, use `game-feel.md`.

## Ownership

Keep the conceptual roles distinct even when a small project combines them in fewer nodes:

```text
action/state controller -> whether an action can start/continue/cancel
combat/attack resolver -> attack instance, contact validity, damage calculation, repeated-contact policy
Health/Vitals -> current HP, invulnerability state, alive/dead result
movement controller -> physical knockback/stagger movement
animation/VFX/audio/camera/UI -> presentation
```

Do not let hitboxes, animation tracks or UI directly become competing owners of HP/state truth.

## Attack phases

Make the relevant phases explicit:

```text
startup -> active -> recovery
```

The active window may be synchronized by one authoritative timeline/event. Avoid several independent timers guessing the same window.

## Hitbox / hurtbox

A common 2D pattern is `Area2D` + `CollisionShape2D` with collision layers/masks for filtering. The hitbox is normally inactive outside the intended contact window.

When changing physics state from callbacks, follow the exact Godot version's safe/deferred-change requirements rather than adding arbitrary delays.

## Repeated-contact policy

Define what happens when one attack overlaps the same receiver across several physics frames:

- once per attack instance;
- blocked while the receiver is invulnerable;
- explicit per-target interval;
- intentionally repeated/ticking behavior.

The rule must be explicit; accidental repeated callbacks are not a combat design.

## Damage payload

Pass enough structured context for the receiver/resolver to make one consistent decision, for example:

```text
source
base value
type/tags
critical/status info when used
knockback intent
attack instance id
```

Keep the payload as small as the game needs. Do not scatter related context across unrelated globals.

## Health / invulnerability handoff

The resolver can determine a proposed/validated combat result, but Health/Vitals owns persistent runtime health state and invulnerability gates under the project's chosen architecture.

If the project combines resolver and Health in one component, preserve the same conceptual boundary internally so there is still only one authoritative HP/invulnerability/death state.

## Knockback / stagger

Combat produces intent/result; the movement controller applies the physical strategy. If the controller rewrites velocity every tick, choose an explicit knockback model such as temporary state, external velocity channel or short controlled override.

Presentation recoil belongs to `game-feel.md`.

## Combo / cancel

When used, define:

```text
input buffer
combo window
next-action mapping
cancel window
resource/stamina rules
recovery/whiff policy
```

Animation may expose timing events, but gameplay/state decides whether transition is valid.

## Projectiles

Define owner/team, collision filters, lifetime/range, repeat/pierce/bounce policy, spawn direction and cleanup. Add pooling only after measurements justify it.

## Debug order

For incorrect combat results, check in order:

1. action/state entered correctly;
2. contact window is active at the intended time;
3. layer/mask;
4. hitbox/hurtbox callback/query;
5. repeated-contact / invulnerability gate;
6. resolver -> Health/Vitals handoff;
7. state exit/cancel;
8. presentation synchronization.

Prove gameplay correctness before tuning feedback.

## Validation

Test the relevant cases: expected contact count, sustained overlap, rapid repeated actions, misses, multiple targets, invulnerability, combo timing, interruption, state termination and collision enable/disable lifecycle.
