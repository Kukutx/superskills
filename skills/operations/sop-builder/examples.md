# SOP Builder Examples

## Example 1: App store screenshot production

### Input

```text
Use the SOP Builder Skill.

Process name: App store screenshot production
Goal: create and export compliant screenshots
Trigger: before app release
Inputs: app UI screenshots, logo, brand colors, platform size requirements
Owner: designer/developer
Risks/common mistakes: wrong size, tiny text, fake UI, forgetting localization
Final output: exported PNG/JPEG assets ready to upload
```

### Expected output pattern

```text
SOP name:
App Store Screenshot Production SOP

Step-by-step process:
1. Confirm platform and required sizes.
2. Collect current UI screenshots.
3. Define main message per screenshot.
4. Create layout with safe margins.
5. Check readable text at preview size.
6. Export and compress.
7. Final upload QA.

Definition of done:
All assets match required dimensions, use real UI, and are readable in store preview.
```

## Bad output

```text
Design screenshots, check them, and upload them.
```

Why bad:

- No inputs.
- No quality checks.
- No failure handling.
