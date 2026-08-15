# Game UI / UX Reference

用于 Godot 2D HUD、menus、overlays、Control/Container/Theme、responsive layout、controller focus、safe area 与 UI feedback。

## 1. Control owns UI

正常游戏 UI 用 `Control` hierarchy。

Prefer：

- anchors；
- Containers；
- MarginContainer；
- Theme/theme overrides；
- signals/events；
- explicit screen flow。

不要用 Node2D coordinates 假装 UI layout。

## 2. Layout before styling

顺序：

1. root anchors；
2. container hierarchy；
3. min size/spacing；
4. stretch/reference policy；
5. aspect-ratio checks；
6. theme/art；
7. motion/polish。

16:9 看起来漂亮但其他比例炸掉，不算完成。

## 3. Anchor vs container

Anchor 表达“这个区域属于屏幕哪里”。
Container 表达“children 怎么排列”。

Examples：

```text
health/status -> top-left + VBox/HBox
currency/objective -> top-right
hotbar -> bottom-center + HBox
pause -> centered PanelContainer + VBox
inventory -> outer margin + grid/list
```

不要手摆每一颗 heart/item。

## 4. Scaling/aspect

明确一个项目级策略：

- base/reference resolution；
- stretch mode；
- aspect behavior；
- pixel UI sampling；
- extra width/height use。

至少检查 target-relevant：

- narrow/mobile-like；
- 16:9；
- wide/ultrawide。

## 5. Safe area

Mobile notch/rounded corner/TV overscan 需要时：

- 读取 platform safe area；
- 在 screen root 附近统一 inset；
- critical UI stay inside safe region。

不要每个 button 自己算一套 safe offset。

## 6. Controller/keyboard focus

每个 screen：

- open 时有 default focused control；
- directional navigation 可预测；
- visible focus state；
- confirm/cancel/back；
- child screen 返回时恢复合理 focus；
- mouse/touch/controller switching 不 strand user。

手柄 menu 打开后 nothing focused = broken UI。

## 7. Screen flow

简单项目可以一个 small controller。
多个 overlay 推荐 stack 思维：

```text
Game
-> push Pause
-> push Settings
-> pop Settings
-> pop Pause
```

Top screen owns relevant input。

不要用十几个 `is_pause/is_settings/...` bool 互相打架。

## 8. Event-driven HUD

Gameplay owns truth，HUD displays：

```text
health_changed -> update bar
ammo_changed -> update count
cooldown_changed -> update fill
objective_changed -> update text
```

避免 `_process()` 每帧读所有 state。

## 9. HUD hierarchy

优先级：

1. survival/current action；
2. objective/critical resource；
3. secondary info；
4. decoration。

所有 widget 都高亮/跳动 = 没有 hierarchy。

## 10. UI feedback

适合：

- hover/focus；
- press pop；
- short fade/slide；
- HP loss flash；
- cooldown fill；
- damage number；
- currency increment；
- confirm/cancel SFX。

快速 retrigger 的 property Tween 要 replace/restart，不要叠。

## 11. Pixel UI

- consistent icon resolution；
- crisp sampling；
- 9-slice/stylebox corners 不变形；
- arbitrary fractional scale 先看实际 blur；
- text readability > 强行低像素化。

## 12. Localization-ready layout

- normal text 不烤进 button image；
- containers allow longer strings；
- gameplay ID != displayed label；
- avoid English-only fixed width。

## 13. Accessibility

按项目需要：

- text size；
- contrast；
- focus indicator；
- remappable controls；
- reduced shake；
- reduced flashes；
- non-color-only cues。

核心 gameplay info 不应依赖唯一视觉通道。

## 14. Touch

Mobile/touch 目标时：

- tap targets 足够；
- edge controls respect safe area；
- avoid tiny hover-only interactions；
- joystick/action buttons 不遮最关键 gameplay；
- orientation/aspect changes tested。

## 15. UI QA

测试：

- supported aspect ratios；
- keyboard-only；
- gamepad-only；
- mouse/touch if target；
- open/close/back；
- focus restore；
- localization-length string；
- rapid health/currency/cooldown updates；
- bright/dark gameplay background；
- pause/time-scale；
- no stale HUD after scene reload。

## Source synthesis

主要吸收 awesome-gamedev `game-ui-ux`、Godot UI container/theme practices 与 GodotPrompter responsive UI/HUD patterns。
