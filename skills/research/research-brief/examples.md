# Research Brief Examples

## Example 1: Tool comparison

### Input

```text
Use the Research Brief Skill.

Research question: Should I use Shopify or WooCommerce for a small EU store?
Decision context: I want fast setup and low maintenance.
Need latest info: yes
Output depth: normal
```

### Expected output pattern

```text
Research question:
Should the user choose Shopify or WooCommerce for a small EU store?

Executive summary:
Shopify is likely better for fast setup and lower maintenance. WooCommerce is better if customization and hosting control matter more.

Key findings:
...

Uncertainty and gaps:
- Exact monthly cost depends on apps, theme, and payment setup.

Recommendation:
Choose Shopify for v1 unless there is a strong reason to self-host.
```

## Bad output

```text
Both are good. Shopify is easy and WooCommerce is flexible.
```

Why bad:

- No decision context.
- No source awareness.
- No tradeoffs.
- No recommendation.
