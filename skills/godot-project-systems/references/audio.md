# Godot Audio Reference

Use for SFX, music, audio buses, ducking, variation, positional/non-positional sound and audio-driven feedback in 2D or 3D projects.

## Audio is feedback, not gameplay truth

Common gameplay events include attack windup/contact, hurt/death, jump/land, dash, pickup, interaction, UI confirm/cancel and warnings/telegraphs.

Sound should represent a meaningful event, not determine damage, quest or state truth.

## Bus structure

A small project often needs only:

```text
Master
Music
SFX
UI
```

Add Ambience, Voice, Combat or other buses only when routing/mixing requirements justify them.

Global user volume settings should normally target buses rather than reimplementing global volume logic on every player node.

## Event ownership

```text
gameplay/domain event
-> audio layer chooses stream/variation/bus/spatial presentation
```

Do not let audio completion become the authority for gameplay transitions unless that timing is explicitly part of the design and ownership is clear.

## Variation

For frequent SFX, small controlled variation in sample, pitch or volume can reduce repetition. Do not randomize enough to destroy the sound's identity or make important cues ambiguous.

## Layered impact

A strong impact may combine weapon transient, material/body response, low-end weight and optional character response. Not every small event needs every layer.

## Spatial audio

Use the dimensional node that matches the project when position matters:

- `AudioStreamPlayer2D` for 2D world sound;
- `AudioStreamPlayer3D` for 3D world sound;
- non-positional players for UI/music or sounds that should not attenuate with world distance.

Check attenuation, source position and listener/camera context against the actual game scale. Important UI/critical feedback should not disappear because it was accidentally routed as distant world audio.

## Music transitions

Make transition triggers explicit: exploration/combat, boss phase, safe room, pause/menu or another real state change. Prefer controlled state/crossfade transitions over repeatedly restarting tracks from noisy frame-by-frame conditions.

## Ducking

When voice or critical cues need priority, use bus effects or controlled automation with sensible attack/release. Do not abruptly mute the entire mix without a design reason.

## Pause / lifecycle

Define which audio pauses with gameplay, which continues in menus, how scene changes stop/retain audio, and how device/reload state resets. Audio should not remain stuck after pause, scene transition or interrupted playback.

## Pooling / reuse

Profile first. High-frequency events may justify reusable players or pooling, but do not build a complex audio pool for every project by default.

## Validation

Check frequent-event repetition, impact hierarchy, UI audibility, spatial attenuation, simultaneous-source mix, pause/resume, music transitions, correct bus-volume persistence and that missing optional audio never breaks gameplay behavior.
