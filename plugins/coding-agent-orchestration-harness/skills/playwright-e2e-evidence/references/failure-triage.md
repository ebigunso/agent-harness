# Failure / Flakiness Triage

If E2E fails:
1) Record the exact flow step where it failed.
2) Capture:
   - screenshot at failure state
   - console errors (and warnings if relevant)
   - failed network requests
3) Note whether the app was “ready” (readiness check status).
4) If timing-related:
   - add a known_flakiness note (e.g., wait for element X)

When you cannot run E2E:
- State what is missing (server start command, auth state, env vars, ports).
- Return NEEDS_REVISION (Reviewer) or mark validation as not satisfied (Orchestrator).
