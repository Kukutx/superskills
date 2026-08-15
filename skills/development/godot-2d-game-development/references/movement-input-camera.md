# Movement / Input / Camera Compatibility Index

旧版兼容入口。新任务不要把 movement、input 和 camera 全部一起加载。

按意图读取：

- CharacterBody2D、jump/dash、physics、knockback、Camera2D、pixel camera -> `movement-physics-camera.md`
- Input Map、keyboard/gamepad/touch、remapping、device switching、rumble/accessibility -> `input-controls-accessibility.md`
- menu focus / responsive UI -> `ui-ux.md`
- camera shake / impact feedback -> `game-feel.md`

组合示例：

```text
“做 top-down movement + smooth camera”
-> movement-physics-camera

“键鼠切手柄时 prompt 自动变化”
-> input-controls-accessibility + ui-ux

“dash 输入经常被 attack recovery 吃掉”
-> input-controls-accessibility + movement-physics-camera
```

不要因为旧 prompt 引用了本文件就自动加载所有相关 reference。