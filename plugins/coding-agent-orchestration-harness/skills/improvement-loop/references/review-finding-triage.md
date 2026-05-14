# Review Finding Triage

Use after a human reviewer, Copilot, CI, Reviewer, or another source finds an issue the harness should have caught.

Classify by durable risk category, not by finding source.

## Destinations

### Repo-specific review behavior

Destination:
- `docs/coding-agent/rules/reviewer.md`

Use for:
- Review Risk Hotspots
- Required Reviewer-Owned Evidence
- Review Heuristics
- Recurring Misses And Prevention

### Repo-specific executable validation

Destination:
- `docs/coding-agent/rules/worker.md`

Use when:
- the repository has or accepts a command/check
- the check should become Worker-owned validation

### Proposed mechanical gate, not yet accepted

Destination:
- `docs/coding-agent/rules/worker.md` or `docs/coding-agent/rules/reviewer.md` Mechanical Gate Candidates

Use when:
- the check is plausible but not yet implemented or accepted as required validation

### Cross-repo harness improvement

Destination:
- `docs/coding-agent/skill-candidates.md`
- `docs/coding-agent/skill-drafts/*.md`, when useful

Use when:
- the prevention is reusable across repositories
- the likely durable owner is a harness skill, reference, agent adapter, validator, or ADR

### Dispatch or packet issue

Destination:
- the active implementation plan Decision Log
- `docs/coding-agent/lessons.md`
- relevant repo rule file if future dispatch behavior changes

Use when:
- the issue came from incomplete task ownership, missing acceptance criteria, missing validation assignment, or poor Reviewer packet context

### Accepted residual risk

Destination:
- `docs/coding-agent/lessons.md`
- relevant repo rule file if it changes future behavior

Use when:
- the risk is understood and explicitly accepted rather than prevented now
