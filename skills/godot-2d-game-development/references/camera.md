# Camera Reference

Use for `Camera2D` follow/framing, smoothing, dead zones, look-ahead, room/world bounds, transitions, zoom and pixel-camera behavior. Impact shake/zoom punch may pair with `game-feel.md`.

## Framing vs feedback

Framing owns what the player should see:

- follow target;
- smoothing;
- dead zone;
- look-ahead;
- room/world limits;
- zoom and transition framing.

Feedback owns temporary presentation effects such as shake, impact offset or zoom punch. Neither should move the player's physics body.

## Top-down camera

Typical decisions:

- centered vs soft follow;
- optional aim/cursor look-ahead;
- world/room limits;
- scene transition behavior;
- arena/boss framing only when needed.

## Platformer camera

Consider horizontal look-ahead, vertical dead zone, jump/landing framing, room transitions and bounds. Do not chase every tiny sprite deformation or shake offset as if it were gameplay position.

## Pixel-camera policy

Define the project policy instead of assuming one universal “pixel perfect” recipe:

```text
base render resolution
filtering
integer display scale yes/no
camera subpixel policy
stretch policy
```

Integer snapping can improve crispness but create stepped motion; smooth subpixel movement can feel better but introduce shimmer. Validate during motion, not only in screenshots.

## Bounds and transitions

Check camera limits against actual room geometry and aspect ratios. For room changes, make the transition ownership explicit: snap, eased transition, temporary lock or scripted framing. Avoid multiple systems simultaneously writing Camera2D position/zoom.

## Validation

Run actual movement and check world edges, fast direction changes, vertical/horizontal transitions, look-ahead reversal, different aspect ratios, target-resolution pixel shimmer and any shake/zoom interaction.
