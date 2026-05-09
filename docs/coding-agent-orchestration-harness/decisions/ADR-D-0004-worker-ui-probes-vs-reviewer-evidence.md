---
status: accepted
adr_type: design
date: 2026-05-09
deciders:
  - ebigunso
consulted:
  - GPT-5.5 Pro
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0004: Allow Worker UI Probes Without Replacing Reviewer Evidence

## Context and Problem Statement

Workers implementing UI work need a way to catch obvious local issues while editing. A strict "no browser automation" Worker boundary makes UI implementation more brittle because simple rendering, navigation, and interaction mistakes may survive until review.

Reviewer independence still matters. Final UI/E2E evidence should remain acceptance-facing and independently verified by a Reviewer unless the Orchestrator or user explicitly reassigns or waives that validation.

## Decision Drivers

- Let Workers catch obvious UI regressions during implementation.
- Preserve independent Reviewer-owned acceptance evidence.
- Keep Worker probes bounded to assigned task scope.
- Avoid treating implementation feedback as final validation.

## Decision

Workers may run bounded UI probes when implementing assigned UI/frontend work or when the Orchestrator explicitly assigns a UI probe.

Worker UI probes are:

- bounded;
- local by default;
- implementation-facing;
- limited to task-owned behavior.

Reviewer UI/E2E evidence remains independent and acceptance-facing. Worker probe evidence must not satisfy Reviewer-owned validation unless the Orchestrator or user explicitly reassigns or waives that validation.

## Considered Options

1. Prohibit all Worker browser/UI probing.
2. Let Worker probes satisfy final UI acceptance validation.
3. Allow bounded Worker probes while preserving Reviewer-owned evidence.

## Decision Outcome

Chosen option: **Option 3**.

This gives Workers practical implementation feedback without weakening the final review gate.

## Consequences

### Positive

- UI Workers can catch obvious issues earlier.
- Reviewer validation remains independent.
- Worker reports can include probe evidence for integration context.

### Negative / Tradeoffs

- Prompts and validators must clearly distinguish probe evidence from acceptance evidence.
- The Orchestrator must avoid counting Worker probes as Reviewer validation unless explicitly reassigned or waived.

## Validation

- Verify Worker prompts allow bounded probes and require reporting when probes materially affect implementation.
- Verify Reviewer prompts state Worker probes do not replace independent acceptance evidence.
- Verify Worker report schema supports optional `ui_probes` without making it required for non-UI work.

## Revisit When

- A runtime provides stronger built-in per-role browser evidence controls.
- The harness adds formal reassignment/waiver records that can be machine-checked across plans and reports.

## More Information

- `plugins/coding-agent-orchestration-harness/agents/Worker.md`
- `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
- `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
