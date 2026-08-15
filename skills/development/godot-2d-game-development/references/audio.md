# Audio Reference

用于 2D SFX、music、audio bus、ducking、variation、positional sound 与 audio-driven feedback。

## 1. Audio is feedback, not decoration

常见 gameplay events：

- attack windup/whoosh；
- confirmed hit；
- hurt/death；
- jump/land；
- dash；
- pickup；
- interact；
- UI confirm/cancel；
- warning/telegraph。

Sound 要与事件意义对应，不是“哪里空就塞音效”。

## 2. Bus structure

常见最小结构：

```text
Master
Music
SFX
UI
```

项目需要时再加：

```text
Ambience
Voice
Combat
```

用户 volume settings 改 bus，不要每个 AudioStreamPlayer 各写一套全局音量逻辑。

## 3. Event ownership

Gameplay event 发出事实：

```text
attack_connected
item_picked
menu_confirmed
```

Audio layer 选择 sample/variation/bus。

不要让 audio completion 决定 damage/quest truth。

## 4. Variation

高频 SFX 防重复：

- small pitch range；
- sample variants；
- volume variation carefully；
- cooldown for noisy repeated events。

不要 random 到破坏声音 identity。

## 5. Layered impact

Strong hit 可分层：

```text
weapon transient
+ body/material impact
+ low-end weight layer
+ optional enemy hurt
```

不是每个 small hit 都需要全部 layers。

## 6. 2D positional audio

AudioStreamPlayer2D 适合 world sound：

- source position meaningful；
- attenuation fits camera/game scale；
- important UI/feedback 不应因为 offscreen distance 听不到；
- many sources 时注意 voice count。

UI sound 通常不做 world attenuation。

## 7. Music transitions

明确触发条件：

- exploration -> combat；
- boss phase；
- safe room；
- pause/menu。

优先 smooth crossfade/state change，而不是每帧根据 enemy count 反复 restart track。

## 8. Ducking

需要保证 voice/critical cue 可听时，可通过 bus effect/controlled volume automation duck music/ambience。

Ducking 必须有 attack/release；不要突然把 BGM 砍到 0。

## 9. Pause/time scale

明确哪些 audio：

- pauses with game；
- continues in pause menu；
- UI still plays；
- music continues/fades。

不要让 pause 后 timer/audio state 永久错乱。

## 10. Pooling/reuse

先 profile/观察 voice/node churn。

高频 impact/projectile 可考虑 reusable audio players/pool，但不要为每个项目预建复杂 audio pool。

## 11. Audio QA

- frequent events 不刺耳/重复；
- hit hierarchy clear；
- UI always audible；
- positional attenuation sensible；
- simultaneous enemies 不爆音量；
- pause/resume works；
- music transition no repeated restart；
- volume settings affect correct buses；
- missing optional audio 不破 gameplay。

## Source synthesis

主要吸收 awesome-gamedev `audio-design`、GD-Agentic-Skills Godot audio patterns 与 game-feel layered feedback。
