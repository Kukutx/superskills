# Technical Design Examples

## Example 1: Referral system v1

### Input

```text
Use the Technical Design Skill.

Feature: referral system v1
Users: logged-in app users
Current stack: Next.js, PostgreSQL
Requirements: users can share invite link, new users are attributed to inviter
Constraints: avoid complex reward fraud logic for v1
```

### Expected output pattern

```text
Recommended approach:
Use a simple referral_code on users and referral_events table for attribution.

Architecture overview:
- Generate referral code per user.
- Attach code to invite link.
- Store inviter on signup if code is valid.

Data model:
users.referral_code
referral_events(id, inviter_user_id, referred_user_id, created_at)

Risks:
- Self-referral
- Duplicate attribution
- Code enumeration

Testing plan:
- Valid referral signup
- Invalid code
- Duplicate signup
- Self-referral blocked
```

## Bad output

```text
Use microservices and event-driven architecture for referrals.
```

Why bad:

- Overengineered for v1.
- No data model.
- No implementation path.
