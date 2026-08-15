---
name: shopify-dev
description: Handle Shopify-specific theme, Liquid, admin configuration, app integration and store implementation tasks with native-first, minimal and reversible changes.
---

# Shopify Development

## Workflow

1. Identify the actual layer: admin setting, theme setting, Liquid/CSS/JS, app, Shopify API, checkout/platform constraint.
2. Inspect the current theme/store setup before proposing a rewrite.
3. Prefer, in order when they solve the problem:
   - Shopify-native setting/feature;
   - existing theme capability;
   - small theme/code change;
   - existing app;
   - new dependency/app only when justified.
4. For current Shopify plan/API/checkout/platform limitations, verify current official documentation before making a definitive claim.
5. Make code placement and rollback explicit.
6. Validate on the affected template/device/market and ensure the change does not break theme editor/update behavior unnecessarily.

## Output

Default:

- **Recommended path**
- **Where to change it**
- **Code/config steps**
- **Platform limitation / tradeoff** when relevant
- **Validation / rollback**

Mention an app-based alternative only when it is genuinely useful.

## Constraints

- Do not default to paid apps for a problem Shopify/theme code can solve simply.
- Do not assume checkout customization or platform capability from stale plan knowledge.
- Keep custom snippets scoped and reversible.
- Do not modify generated/vendor theme files blindly when an appropriate extension/section/snippet exists.
- For store data, payments, customer information or app permissions, account for security/privacy and migration impact.
- If the task is generic frontend/backend work unrelated to Shopify, use a general development Skill instead.