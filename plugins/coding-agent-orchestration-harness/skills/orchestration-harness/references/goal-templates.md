# Goal Mode Templates (Goal File, Journal Entry, Completion Report)

Read this when starting or running a goal per `references/goal-mode.md`.

Three copy-paste templates. Keep them readable; prefer short bullets over narrative.

Never hard-wrap prose mid-sentence in committed goal/journal files — keep one sentence, paragraph, or list item per line.

Term glosses used throughout (graded escalation levels; full protocol in `references/goal-mode.md`):
- proceed: in-envelope decision; act and journal briefly.
- decide-and-journal: in-envelope but judgment-heavy; act, journal the decision with rationale, flag it for retrospective review.
- ask-now: envelope boundary hit; stop the loop, surface the question to the user, wait. Reaching ask-now is a successful termination, not a failure.
- abort: safety condition; stop, revert to the last good checkpoint (the per-iteration commit on the goal branch), report.

---

## 1. Goal file template

Each goal is a directory: `docs/coding-agent/goals/active/<goal-id>/` containing `goal.md` (this template) and `journal.md` (template 2). Every terminal outcome (`completed`, `aborted`, `abandoned`) archives the whole directory to `docs/coding-agent/goals/completed/` with the final status preserved in `goal.md`, so outcomes stay distinguishable after archiving.

Copy this structure into:
- `docs/coding-agent/goals/active/<goal-id>/goal.md`

The envelope (the user-ratified boundary of what the loop may decide alone) is immutable during the run; renegotiation is a human moment.

---

```markdown
# Goal: <Title>

- status: draft | active | awaiting_decision | completed | aborted | abandoned
  - ask-now sets `awaiting_decision`; the goal stays under `active/` until the human decides: resume (back to `active`), re-ratify (back to `active` with a new envelope), or abandon.
  - terminal outcomes (`completed`, `aborted`, `abandoned`) archive the directory to `docs/coding-agent/goals/completed/` with the final status preserved here.
- created: <YYYY-MM-DD>
- last_updated: <YYYY-MM-DD>

## Goal statement
- <the outcome being pursued, in one or two sentences>

## Goal condition
- target: <objectively checkable end state, e.g. "test suite green", "benchmark >= X">
- invariants (untouchable; weakening any one is an ask-now escalation, never absorbed):
  - <invariant 1, e.g. "no test files modified">
  - <invariant 2, e.g. "measurement harness unchanged">
- gap reading (protected part of the condition — tightening is free mid-run; loosening is invariant pressure, ask-now; write `epistemic-only` here when no countable gap reading exists, per the condition checklist):
  - <how the condition is measured as a number mid-run, e.g. "count of failing tests via <command>", "benchmark delta below threshold via <command>">
  - <on plateaus where the number does not move: the journal must argue epistemically that what was learned credibly reduces remaining distance or uncertainty toward this goal>
- linkage credibility bar (protected part of the condition — tightening is free mid-run; loosening is invariant pressure, ask-now):
  - <what counts as a credible epistemic goal-linkage argument on plateaus, i.e. the bar used to decide whether learned information reduces remaining distance or uncertainty toward this goal>
- escalation clause: the goal condition is satisfied when the target is met OR an ask-now/abort state is reached — reaching a human moment is a successful termination of the loop.

## Envelope
- decision scope (paths, components, operation classes the agent may change freely):
  - <path or component 1>
  - <operation class, e.g. "refactor within src/**", "dependency version pins">
- progress obligation:
  - progress = reduction in expected distance to the goal, read from the gap or from a credible epistemic goal-linkage argument on plateaus.
  - stall = consecutive iterations with the gap unchanged, no credible goal-linkage argument, and attempts circling previously failed approaches. A stall is an ask-now escalation, not something to grind through.
- resource backstops (optional; never load-bearing — stall detection is the primary runaway defense):
  - <e.g. wall-clock cap, cost cap, iteration cap — or "none">
- forbidden set acknowledgment:
  - Any action that is irreversible or outward-facing (merge, deploy, force-push, data deletion, publishing, external service mutation) is outside the envelope by class, not by enumeration; new action types are judged against this irreversibility criterion.

## Assessment cadence events
Dispatch the independent assessor (fresh-context Reviewer-role dispatch; see `references/goal-assessor-mandate.md`) on each of these events:
- fresh start: <first N iterations of the goal>
- post-pivot: <iterations immediately after an approach change, re-scoping, or surprising evidence>
- suspected stall: <whenever stall criteria above may be met>
- heartbeat maximum: <never more than N iterations between assessments>

---
```

## 2. Journal entry template (append-only)

The iteration journal is `docs/coding-agent/goals/active/<goal-id>/journal.md`, beside `goal.md` in the goal directory — single-writer, append-only: anchor each append on the previous entry so it inserts rather than replaces.

```markdown
### Iteration <id>

- hypothesis: <what this iteration believes will reduce the gap and why>
- attempt: <what was actually done, briefly>
- observed evidence: <what happened — command output summaries, measurements, failures>
- gap value: <number from re-running the goal condition's gap check this iteration>
- committed prediction: <falsifiable claim about what the next iteration will change, checked against the next entry's observed evidence>
- decision: <next step> — escalation level: proceed | decide-and-journal | ask-now | abort
  - <if decide-and-journal: rationale for the judgment-heavy call, flagged for retrospective>
  - <if ask-now/abort: what boundary or safety condition was hit>
- checkpoint: <commit hash, if this iteration changed the worktree>

### Assessment <id> (assessor record; mirrors the verdict record in `references/goal-assessor-mandate.md` verbatim)

- dispatch text (verbatim, exactly as sent — deviation from the fixed template in `references/goal-assessor-mandate.md` is a visible envelope violation):
  - <the dispatch text>
- `Trajectory verdict: <verdict>`
- `Validity verdict: <verdict>`
- `Reason: <evidence-grounded reason covering both duties>`

---
```

## 3. Completion report template

Produced by the loop before the goal branch may merge; the pre-merge reviewer verifies every assertion against the journal before the report is accepted (ADR-D-0013).
Keep it readable at a glance: verbatim evidence (dispatch texts, full outputs) stays in the journal — the report asserts and points.
Exactly these six sections.

```markdown
# Completion Report: <Goal title>

## 1. Goal condition satisfied
- <the condition as stated in the goal file>
- evidence (inline): <the executed check and its result proving the target is met — or the ask-now/abort state reached, per the escalation clause>

## 2. Assessment assertion
- <one line: assessor dispatches occurred at the required cadence events and complied with the fixed dispatch template; verbatim texts and verdicts are in the journal at <entry ids>>

## 3. Invariant integrity
- <invariant 1>: untouched — proven by <the check, e.g. "git diff --stat shows no test file changes">
- <invariant 2>: untouched — proven by <check>

## 4. Envelope compliance
- forbidden-class actions taken: none — a hard assertion: an autonomously taken forbidden-class action is a critical defect, never made compliant by a record of it.
- boundary escalations (every ask-now event at an envelope boundary):
  - <event>: <what boundary was hit and the human decision> (journal entry <id>)
- decide-and-journal items (every one, with rationale):
  - <item>: <rationale> (journal entry <id>)

## 5. Trajectory summary
- pivots: <approach changes taken and why>
- stalls: <stalls hit and how they resolved>
- abandonments: <what was abandoned and why>

## 6. Checkpoint index
- <commit hash> ↔ iteration <id>: <one-line description>
- <commit hash> ↔ iteration <id>: <one-line description>
```
