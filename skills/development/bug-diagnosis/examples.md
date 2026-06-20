# Bug Diagnosis Examples

## Example 1: Frontend API bug

### Input

```text
Use the Bug Diagnosis Skill.

Symptom: Login button shows loading forever.
Expected behavior: redirect to dashboard.
Actual behavior: spinner never stops.
Error logs: POST /api/login returns 401.
Recent changes: changed cookie domain settings.
```

### Expected output pattern

```text
Most likely cause:
Cookie/session domain mismatch after the recent cookie configuration change.

Why this fits:
The API returns 401 and the UI waits for an authenticated session that never becomes valid.

Fast verification steps:
1. Inspect Set-Cookie in Network tab.
2. Check cookie domain and SameSite flags.
3. Confirm whether session cookie is sent on dashboard request.

Suggested fix:
Align cookie domain with current app domain and update auth callback handling.
```

## Bad output

```text
Try clearing cache or reinstalling dependencies.
```

Why bad:

- Not tied to the evidence.
- Ignores the 401.
- No verification path.
