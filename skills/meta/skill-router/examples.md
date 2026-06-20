# Skill Router Examples

## Example 1

### Input

```text
我想做一个欧美市场的 App Store 上架素材，包括文案和图片。
```

### Expected output pattern

```text
Recommended primary skill:
marketing/product-positioning

Supporting skills:
writing/app-store-copy, design/app-store-assets, design/image-review-refiner

Workflow sequence:
marketing/product-positioning → writing/app-store-copy → design/app-store-assets → image-review-refiner
```

## Bad output

```text
Use a design skill.
```

Why bad: too vague; no workflow sequence.
