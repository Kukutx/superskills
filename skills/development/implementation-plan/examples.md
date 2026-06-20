# Implementation Plan Examples

## Example

### Input

```text
Feature: referral system v1
Stack: Next.js + PostgreSQL
```

### Expected output pattern

```text
Files to create/change:
- db/schema.sql: add referral_code
- app/api/referrals/route.ts: referral lookup
- app/signup/page.tsx: accept referral code

Tests:
- valid referral
- invalid referral
- self-referral blocked
```

## Bad output

```text
Implement backend, then frontend, then test.
```

Why bad: not file-level or testable.
