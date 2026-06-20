# Image Prompt Director Examples

## Example 1: Mobile app banner

### Input

```text
Use the Image Prompt Director Skill.

Goal: Create a friendly app marketing banner
Subject: phone mockup with activity chat UI, young friends in soft background
Format / size: 1024 × 500 px
Style: clean, realistic, European lifestyle, not AI-looking
Brand/context: social planning app
Must include: warm friendly mood, clear space for headline
Must avoid: detailed street addresses, distorted hands, fake tiny UI text
```

### Expected output pattern

```text
Visual direction:
A clean horizontal marketing banner with a phone mockup as the hero object and soft lifestyle context behind it.

Main prompt:
...

Negative prompt / avoid list:
no distorted hands, no unreadable tiny text, no street-level address, no overly glossy AI look...

Composition notes:
- Keep left third clear for headline.
- Phone on right side.
- Background low detail.
```

## Bad output

```text
Make a beautiful modern app banner with friends and a phone.
```

Why bad:

- No composition control.
- No negative prompt.
- No production constraints.
