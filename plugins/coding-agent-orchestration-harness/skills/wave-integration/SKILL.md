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
5. Collect blockers/questions.
6. Collect rule/lesson candidates.
7. Update plan Progress Log.
8. Decide whether to dispatch follow-up Workers or Reviewer.
9. Prepare Reviewer packet.

## References

- `references/integration-checklist.md`
- `references/reviewer-packet-template.md`

## Closeout Validation

Use `scripts/validate_closeout.py` when a structured closeout summary is available.
