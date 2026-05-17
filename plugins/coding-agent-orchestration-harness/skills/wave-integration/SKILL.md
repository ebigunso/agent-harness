---
name: wave-integration
description: Orchestrator-owned integration checklist for Worker waves. Use after one or more Worker reports return, before Reviewer dispatch, or before final closeout.
---

# Wave Integration

Use this skill after each Worker wave.

The Orchestrator remains the only writer for shared plan lifecycle state. This skill does not create a new subagent role by default.

## Core Checklist

1. Parse every Worker report.
2. Validate every report against `subagent-report-contract`.
3. Confirm each changed file is inside `owns` or explained.
4. Confirm all required Worker-owned validations are pass or explicitly waived.
5. Close or terminate completed async/background subagent processes after their final reports are validated and integrated. If the runtime does not expose a close/terminate action, record cleanup as unavailable and do not reuse the completed process for unrelated work.
6. Collect blockers/questions.
7. Collect rule/lesson candidates and `harness_migration_candidates`.
8. Update plan Progress Log.
9. Decide whether to dispatch follow-up Workers or Reviewer.
10. Prepare Reviewer packet.

## References

- `references/integration-checklist.md`
- `references/reviewer-packet-template.md`

## Closeout Validation

Use `scripts/validate_closeout.py` from this skill directory when a structured closeout summary is available.
