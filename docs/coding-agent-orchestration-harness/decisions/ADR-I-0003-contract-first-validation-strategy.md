---
status: accepted
adr_type: implementation
date: 2026-05-09
deciders:
  - ebigunso
consulted:
  - GPT-5.5 Pro
informed: []
supersedes: []
superseded_by: null
---

# ADR-I-0003: Use Contract-First Validation With Balanced Strictness

## Context and Problem Statement

The harness should prevent malformed plans, malformed Worker reports, missing validation evidence, unsafe shared-state Git mutations, and false "done" states. At the same time, it should not become brittle by validating exact prose, exact task decomposition aesthetics, prompt wording, or every non-critical strategy choice.

Validation should be strict where the workflow depends on structured contracts and completion state, and flexible where agents need room to choose an execution strategy.

## Decision Drivers

- Block false completion and malformed contracts.
- Preserve agent flexibility for decomposition and prose.
- Avoid transcript-matching validators.
- Make runtime-facing validation useful by default without being maximally strict.

## Decision

The harness uses contract-first validation with `balanced` as the default runtime mode.

Validation is strict for:

- package structure;
- runtime role maps;
- plan/task contracts;
- Worker report contracts;
- required validation evidence;
- final closeout state.

Validation is flexible or advisory for:

- exact prose;
- exact task decomposition;
- prompt wording;
- non-critical strategy choices;
- optional validation aesthetics.

Validators should fail malformed contracts and missing required evidence. They should warn, explain, or defer for subjective strategy issues unless a hard rule is clearly violated.

## Implementation Impact

- Package validation should check structure, manifests, referenced paths, role maps, and obvious duplicated workflow sections without exact wording checks.
- Plan validation should hard-fail malformed task contracts and missing validation ownership.
- Worker report validation should hard-fail malformed schema and required validation failures/skips without waiver evidence.
- Closeout validation should block final completion when tasks, blockers, reviewer status, or required evidence remain unresolved.

## Considered Options

1. Validate only by human review.
2. Validate exact transcript/prose behavior.
3. Validate contracts strictly and strategy/prose flexibly.

## Decision Outcome

Chosen option: **Option 3**.

This blocks the failures that damage harness reliability while preserving runtime adaptability.

## Consequences

### Positive

- Required evidence and completion state become harder to fake or miss.
- Validators remain useful across runtime wording differences.
- Balanced mode can be run by default without excessive false positives.

### Negative / Tradeoffs

- Some subjective quality problems remain reviewer-owned rather than validator-owned.
- Validators need clear warning/failure categories.

## Validation

- Smoke tests include valid and invalid plan/report fixtures.
- Package validator runs successfully on the plugin.
- Invalid required evidence and malformed contract fixtures fail clearly.
- Balanced mode is the default for runtime-facing validator commands.

## Revisit When

- Repeated reviewer findings show that advisory checks need to become hard rules.
- Runtime adapters become generated from a shared source where exact structural checks become reliable.

## More Information

- `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/validation-strictness.md`
- `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
- `plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md`
