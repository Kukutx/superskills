# Sprite Generation Reference

Use for planning/generating new 2D or pixel-art action strips from an approved character/reference. Existing sheets that only need slicing/packing should skip this reference.

## Approve one seed first

Prefer:

1. approve one in-game seed/reference frame;
2. lock identity, proportions, palette, outfit/equipment and perspective;
3. generate one action + one direction per strip when possible;
4. normalize only after the strip is coherent;
5. preview motion before packaging.

Avoid generating every action × direction in one giant image; drift and layout errors become harder to diagnose.

## Action planning

Choose frame count from motion needs, not a universal fixed count.

| Action | Useful starting range | Timing idea |
| --- | --- | --- |
| idle | 2–4 | subtle / slower |
| walk | 4–8 | readable rhythm |
| run | 4–8 | faster, larger poses |
| attack | 3–8 | anticipation -> impact -> recovery |
| hurt | 2–5 | reaction + recovery |
| death | 4–10 | readable one-shot |
| dash | 2–6 | strong directional read |

Key poses and timing matter more than raw frame count.

## Direction policy

For top-down sets define:

- 4 vs 8 directions;
- which directions may mirror;
- asymmetric weapon/outfit exceptions;
- shared apparent scale and ground anchor;
- direction naming/metadata.

Do not mirror clearly asymmetric characters merely to reduce asset count.

## Generation contract

A production prompt should state the relevant invariants:

- same character identity/proportions/outfit/equipment;
- same palette/style;
- one fixed facing direction for this strip;
- transparent background;
- exact frame count;
- fixed slot/frame-size target;
- readable silhouette at actual game size;
- crisp pixel clusters for pixel art;
- no labels/scenery/watermark;
- production animation asset, not concept art.

If the model cannot reliably produce exact pixel geometry, separate creative generation from deterministic packaging.

## Whole-strip workflow

```text
approved seed
-> optional layout guide
-> generate full action strip
-> clean alpha
-> split temporary frames
-> normalize shared scale
-> align shared anchor/baseline
-> optional exact-seed restore
-> preview
-> approve
```

Independent frame-by-frame generation is a fallback because it increases identity and proportion drift.

## Normalize as a set

Keep consistent:

- frame canvas;
- apparent scale;
- anchor/baseline;
- direction convention;
- transparent padding policy.

Do not tight-crop every frame to unrelated bounds and then play them directly.

## Timing

Keep geometry and timing separate:

- per-frame duration;
- loop / ping-pong / one-shot;
- intentional hold frames;
- action/tag range.

If authored source already contains tags/timing, preserve it as the source of truth.

## Generation QA

Check identity/proportions, equipment consistency, direction, game-scale silhouette, key poses, alpha cleanliness, intended loop seam and clear startup/impact/recovery progression.

Then use `packaging.md` for deterministic output.
