### 2) Prefer Root-Cause Fixes Over Symptom Patches

- Address the source of the issue instead of adding repeated local workarounds.
- Avoid duplicating fragile logic across modules.
- Strengthen invariants where failures originate.

Review checks:
- Does the change remove the cause or only suppress outcomes?
- Is duplicated or compensating logic being introduced?
