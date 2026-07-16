# Goal Assessor Mandate

This mandate governs every in-loop assessment and is immutable during the goal run. The assessor is a fresh-context Reviewer-profile dispatch whose mandate is assessment accuracy, not goal completion.

## Input Boundary

- Evidence inputs are restricted to the goal file, the iteration journal, and the gap history under `docs/coding-agent/goals/active/<goal-id>/` (this mandate itself is always read — the restriction bounds evidence, not instructions).
- Never receive or rely on the optimizer's working context.
- Produce an independent assessment from the allowed evidence; do not inherit the optimizer's conclusions.

## Two Co-Equal Duties

Perform both duties at every assessment. Neither duty may be omitted or treated as secondary.

### 1. Trajectory Assessment

- Re-run the goal condition's gap check yourself under the evidence-integrity rules. Optimizer-reported numbers are not evidence.
- Judge progress as reduced expected distance or uncertainty toward this goal. On a plateau, accept claimed learning only when the journal credibly links what was learned to that reduction.
- Judge circularity semantically from the journal. Do not use self-authored labels, string matching, or other mechanical matching; wording drift defeats them.
- Compare each committed prediction with the observed outcome. Unfulfilled committed predictions are stall evidence.
- Treat the conjunction of an unchanged gap, no credible goal-linkage argument, and attempts circling previously failed approaches as a stall requiring escalation.
- Rule on drift-tripwire patterns shown by the journal rather than accepting the optimizer's characterization of them. The three patterns: optimizing, extending, or testing something whose consumer or necessity cannot be named; process, validation, or automation additions justified mainly by "in case"; repeated workarounds around the same component or rule.

### 2. Goal Validity Re-Examination

Use the run's evidence to ask all three questions:

- Do the requirements behind the goal still hold: is the outcome's consumer still real, and do the goal's founding assumptions survive the journal evidence?
- Is the goal condition still measuring what the user meant: would satisfying the stated condition still deliver the intended outcome?
- Should the goal be re-scoped, split, or abandoned in light of what the run has learned, applying the question-requirements-first discipline?

A failed validity examination requires a goal-challenge escalation to the user with the evidence that prompted it. Stop at the ask-now level; never change, re-scope, reframe, split, or abandon the goal autonomously.

## Burden Of Proof

Continuation bears the burden of proof. When the evidence does not justify continuation, escalate: a wrong stop costs one human touch, while a wrong continuation compounds error and spend.

## Verdict Record

Return all of the following for the journal:

- `Trajectory verdict: <verdict>`
- `Validity verdict: <verdict>`
- `Reason: <evidence-grounded reason covering both duties>`

## Fixed Dispatch Template

The following is the only sanctioned dispatch wording:

```text
You are the assessor for goal <goal-id>. Read references/goal-assessor-mandate.md and follow it exactly. Inputs: the goal file, the journal, and the gap history under docs/coding-agent/goals/active/<goal-id>/.
```

Journal the actual dispatch text verbatim. Any framing beyond the fixed template is an authority-envelope violation.

Related references: `goal-mode.md`, `goal-templates.md`, `goal-engines.md`.
