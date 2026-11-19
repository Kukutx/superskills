# Navigation and AI Reference

Use for 3D navigation geometry, `NavigationAgent3D`, target/path following, local avoidance, perception and AI-to-movement handoff.

## 1. Separate AI intent, navigation and movement

Keep the ownership chain explicit:

```text
AI/perception -> intent/target
navigation -> path / next position / optional avoidance velocity
CharacterBody3D controller -> actual collision-aware movement
combat/state -> attack/action validity
animation/VFX -> presentation
```

NavigationAgent3D does not move its parent automatically. Do not create a second movement authority inside the AI layer.

## 2. Navigation data must match the actor

Before debugging path behavior, confirm:

- navigation region/map exists and is enabled;
- navmesh covers intended walkable space;
- agent radius/height and world geometry are compatible;
- slopes, stairs, gaps and links match the locomotion model;
- navigation layers/masks select the intended regions;
- target is actually reachable under the current map.

A visually open corridor can still be invalid for the configured navigation geometry.

## 3. Required path-following update

After setting `NavigationAgent3D.target_position`, current Godot documentation requires `get_next_path_position()` once per physics frame while navigation is active so the agent's internal path state advances.

Use the returned position to derive desired movement for the parent controller. Stop path-following updates when navigation is finished to avoid target-end jitter.

Do not throttle this required path update together with expensive AI reasoning.

## 4. Avoid recursive path queries from signals

Some navigation methods can trigger path recalculation. Avoid calling path-advancing/query methods recursively from navigation-agent signal callbacks; handle them in the physics step or defer where appropriate for the exact version.

## 5. Perception can run at a different cadence

Expensive sensing/decision work can often run less frequently than body movement/path-following:

```text
cheap movement/path step -> physics cadence
line-of-sight / target scoring / tactical reasoning -> only as often as gameplay requires
```

Use Area3D, ray queries or other sensors according to the actual perception semantics. Do not raycast every possible target every physics frame without evidence that it is necessary.

## 6. Avoidance is optional

Local avoidance solves a different problem from pathfinding. Enable it only when agents need dynamic local separation/obstacle response and validate its behavior/cost with the actual crowd density.

Do not assume avoidance makes an invalid navmesh, oversized agent or impossible corridor traversable.

For vertical/fully 3D movement, confirm the project's avoidance/navigation setup actually models that space; do not assume a ground-agent configuration automatically becomes flying navigation.

## 7. State stability

Prevent AI oscillation when thresholds overlap:

- detection/lose-target hysteresis;
- attack/chase range gates;
- cooldown/reaction windows;
- explicit return/search state when useful.

Do not solve every oscillation by adding another framework/state layer; first check target/path thresholds and ownership.

## 8. Dynamic world changes

When doors, obstacles or generated geometry change navigability, make the update ownership explicit. Navigation data and physical collision should not silently diverge.

Avoid rebuilding large navigation data on every small event without measuring the need; use the project's supported dynamic strategy for the exact Godot version.

## 9. Debug visibility

Useful development evidence includes:

- current AI state/target;
- nav path and next point;
- agent radius/height;
- target reachability;
- line-of-sight result;
- current desired vs actual velocity.

Keep debug overlays optional and out of production behavior.

## 10. Validation

Test:

- same target from multiple start positions;
- unreachable target;
- narrow corridor/stairs/slope;
- target moving rapidly;
- target reached / navigation finished without jitter;
- blocked line of sight;
- many agents with and without avoidance;
- dead/stunned/paused agents stop producing invalid intent;
- dynamic obstacle/world changes when supported;
- actual CharacterBody3D motion follows navigation without bypassing collision.
