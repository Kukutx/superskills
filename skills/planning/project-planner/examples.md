# Project Planner Examples

## Example 1: Build a small app feature

### Input

```text
Use the Project Planner Skill.

Goal: Add a referral feature to my mobile app
Current status: app already has login and user profiles
Deadline: no fixed deadline
Resources: solo full-stack developer
Constraints: keep it simple, avoid complex reward fraud logic for v1
Output: roadmap and first actions
```

### Expected output pattern

```text
Goal definition:
Ship a v1 referral flow that lets users invite friends and track basic referral status.

Assumptions:
- Existing user IDs are stable.
- No payment reward is needed in v1.

Recommended phases:
1. Define referral model
2. Implement invite link
3. Track signup attribution
4. Add simple UI
5. Test abuse edge cases

First 3 actions:
1. Define referral_code field on user.
2. Decide attribution window.
3. Sketch UI states.
```

## Bad output

```text
You should plan, design, develop, test, and launch the feature.
```

Why bad:

- Too generic.
- No dependencies.
- No first action.
- No risk handling.
