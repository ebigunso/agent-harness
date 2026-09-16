---
name: wave-integration
description: Orchestrator-owned integration checklist for Worker waves. Use after one or more Worker reports return, before Reviewer dispatch, or before final closeout.
---

# Wave Integration

Use this skill after each Worker wave.

The Orchestrator remains the only writer for shared plan lifecycle state. This skill does not create a new subagent role by default.

## Integration Contract

Apply the following to every Worker report in the wave, including malformed, `blocked`, and `failed` ones. A report that fails an item still enters the checklist for triage, corrective follow-up, or escalation; item 3 gates only Reviewer dispatch and final closeout.

1. Parsed and validated: the report is one YAML block valid against `subagent-report-contract`, maps to exactly one assigned Task_X, and its status (`done`, `blocked`, `failed`) is recorded. A malformed report is a blocker: request a corrected report or dispatch follow-up work before review.
2. Ownership reconciled: every `files_changed` path is inside the task's `owns`, or outside it only when minimal and explicitly explained. An unexplained cross-owns edit is a blocker.
3. Required evidence present: every required Worker-owned validation item is `pass` or explicitly waived. `skipped` is not a waiver; missing evidence blocks progression to Reviewer dispatch and closeout, not the follow-up dispatch that obtains it.
4. One assignment per report: each report maps to exactly one assigned Task_X, and a completed process is not reused for unrelated work; duplication of still-active child work is governed by `subagent-strategy/references/async-dispatch-lifecycle.md`.
5. Async cleanup owned: after a report is validated and integrated, the Orchestrator closes or terminates the completed async/background subagent process per `subagent-strategy/references/async-dispatch-lifecycle.md`, which holds the cleanup policy.

## Routes

- After applying the contract to every report: run `references/integration-checklist.md` (blockers and questions, candidates, the Progress Log entry, and the follow-up Worker versus Reviewer decision).
- Before a Reviewer dispatch, build the packet for the review kind:
  - Post-Worker review: build the packet with `references/reviewer-packet-template.md`; the packet's field list has one home, `orchestration-harness/references/dispatch-guidance.md` (Reviewer Dispatch).
  - Draft-plan review (before user approval): dispatch with the Reviewer snippet (plan review) in `subagent-strategy/references/prompt-snippets.md`, the one home for its inputs.

## Closeout Validation

Use `scripts/validate_closeout.py` from this skill directory when a structured closeout summary is available.
