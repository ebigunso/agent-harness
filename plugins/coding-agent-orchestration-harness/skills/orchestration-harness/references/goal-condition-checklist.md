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
- [ ] The escalation clause makes either outcome a successful termination: the target is met, or an ask-now/abort state is reached. `Ask-now` stops for a user decision (under a brief, the owner's, reached by the Carrier as `goal-mode.md` Authority Envelope states); `abort` stops and returns to the last safe checkpoint after a safety condition.
- [ ] The framing check passes: satisfying the stated condition would deliver the user's intended outcome.
- [ ] Under a brief, where this pass is the review the brief route requires (`lifecycle-gates.md` Plan Gate Details): every clause of the authority envelope is recorded as `goal-mode.md` Authority Envelope defines it: the decision scope names the paths, components and operation classes the loop may change; the progress obligation says how progress is read; the stall rule is stated; any resource backstop is a coarse ceiling and not load-bearing; and the forbidden set is the irreversibility class, not a list.
- [ ] The authority envelope — the boundary for autonomous action, ratified by the user or, under a brief, authorized by the brief route (`goal-mode.md` Authority Envelope) — excludes every action that is irreversible or outward-facing under the irreversibility criterion, or defers that action to a human moment.
- [ ] The Reviewer has verified every item of this checklist that applies against the recorded goal condition and envelope, in one pass, and recorded a pass.

Related references: `goal-mode.md`, `goal-templates.md`, `goal-engines.md`.
