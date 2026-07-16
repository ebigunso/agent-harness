# Goal Condition Checklist

Complete this checklist before starting a goal loop. A Reviewer must record a pass; any unchecked item keeps the loop from starting.

## Required Pre-Loop Review

- [ ] The target states an objectively checkable end state.
- [ ] The condition defines a countable gap reading where possible: the numeric distance from the current state to the target. If no countable reading is workable, it is explicitly marked `epistemic-only` and flagged as weaker because progress depends entirely on judged learning.
- [ ] Every untouchable invariant — a protected part of the condition that may not be weakened to reach the target — is enumerated, including:
  - [ ] test files and behavior-contract assertions;
  - [ ] the measurement or evaluation harness;
  - [ ] the gap reading itself; and
  - [ ] the linkage credibility bar used to decide whether learned information reduces distance or uncertainty toward this goal.
- [ ] The condition states that weakening any invariant leaves the authority envelope and requires escalation.
- [ ] The escalation clause makes either outcome a successful termination: the target is met, or an ask-now/abort state is reached. `Ask-now` stops for a user decision; `abort` stops and returns to the last safe checkpoint after a safety condition.
- [ ] The framing check passes: satisfying the stated condition would deliver the user's intended outcome.
- [ ] The authority envelope — the user-ratified boundary for autonomous action — excludes every action that is irreversible or outward-facing under the irreversibility criterion, or defers that action to a human moment.
- [ ] The Reviewer has verified every item above against the recorded goal condition and recorded a pass.

Related references: `goal-mode.md`, `goal-templates.md`, `goal-engines.md`.
