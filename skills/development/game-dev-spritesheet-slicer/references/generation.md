# Sprite Generation Reference

用于从角色/参考帧规划并生成 2D/pixel-art action strips。已有完整 sheet 只需要切图/打包时不要加载本文件。

## Approve one seed first

Generative workflow 优先：

1. approve one in-game seed frame;
2. lock identity, proportions, palette, outfit/equipment and perspective;
3. generate **one action + one direction per strip** when possible;
4. normalize only after the strip is stable;
5. preview motion before packaging.

不要默认一次生成“所有动作 × 所有方向”的巨型表。它更容易产生 identity drift、错格、frame inconsistency 和无法确定的空槽。

## Action planning

Frame count 按动作需求决定，不要全固定成 6 帧。

| Action | Starting range | Timing idea |
| --- | --- | --- |
| idle | 2–4 | subtle / slower |
| walk | 4–8 | even readable rhythm |
| run | 4–8 | faster, larger poses |
| attack | 3–8 | anticipation -> impact -> recovery |
| hurt | 2–5 | fast reaction + recovery |
| death | 4–10 | readable one-shot |
| dash | 2–6 | strong direction/readability |

Key poses + timing 比纯 frame 数更重要。

## Direction policy

Top-down 项目明确：

- 4 or 8 directions;
- 哪些方向允许 mirror;
- asymmetric weapon/outfit 是否必须独立绘制;
- 每个方向保持相同 apparent scale / ground anchor;
- direction 进入 naming/metadata.

不要为了减少素材把明显非对称角色强行镜像。

## Prompt contract

生成 prompt 至少明确：

- same character identity;
- same proportions;
- same outfit/equipment;
- same palette/style;
- one fixed facing direction for this strip;
- transparent background;
- exact frame count;
- fixed slot/frame-size target;
- readable silhouette at actual game size;
- crisp pixel clusters when pixel art;
- no labels, scenery or watermark;
- production animation asset, not concept sheet.

如果模型不能可靠保证 exact pixel geometry，把创意生成与 deterministic packaging 分开处理。

## Whole-strip workflow

```text
approved seed
-> optional layout guide
-> generate one full action strip
-> clean alpha
-> split temporary frames
-> apply shared scale
-> align shared anchor/baseline
-> optionally restore exact seed as frame 1
-> preview animation
-> approve
```

Independent frame-by-frame generation 是 fallback，不是默认，因为它显著增加 drift。

## Normalization target

同一角色 set 最终共享：

- frame canvas size;
- apparent scale;
- anchor/baseline;
- direction convention;
- transparent padding policy.

不要把每一帧 tight-crop 成不同 bounds 后直接播放。

## Timing

Geometry 与 timing 分开记录：

- per-frame duration;
- loop / ping-pong / one-shot;
- hold frames;
- action/tag range.

如果 editable source 已经带 timing/tags，优先保留，不手工重建第二份真源。

## Generation QA

生成阶段检查：

- identity/proportions stable;
- weapon/outfit 不 morph;
- correct direction;
- silhouette reads at game scale;
- action key poses clear;
- no extra limbs/props/text;
- transparent background clean;
- loop seam reasonable when intended;
- impact/startup/recovery progression readable.

通过后再进入 `packaging.md` 做 deterministic output。
