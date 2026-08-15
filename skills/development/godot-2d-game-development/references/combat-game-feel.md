# Combat / Game Feel Compatibility Index

旧版兼容入口。现在将 **战斗正确性** 与 **反馈/打击感** 分开。

- hitbox/hurtbox、damage、i-frame、combo、attack window、projectile、death -> `combat-system.md`
- hit-stop、camera shake、flash、recoil、squash/stretch、impact FX、rumble -> `game-feel.md`
- particles/shader implementation -> `rendering-vfx-shaders.md`
- SFX/mix/ducking -> `audio.md`
- attack animation/frame timing -> `animation-pixel.md`

示例：

```text
“一个挥砍扣了三次血”
-> combat-system

“伤害判定都对，但砍起来很软”
-> game-feel + optional audio/rendering

“攻击第 4 帧才应该启用 hitbox”
-> combat-system + animation-pixel
```

不要因为任务提到 combat 就同时加载所有表现 reference。