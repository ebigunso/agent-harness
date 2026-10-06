# Completion Closeout

Use this reference before declaring a Task_X, phase, wave, or full plan complete.

## Task_X Done Criteria

Done/blocked conditions: `SKILL.md` Validation Gate (canonical). Additionally confirm:

- Worker report status is `done`;
- any files changed outside `owns` are limited to a minimal touch the Worker's own edit needs to meet the acceptance criteria or a change a packet pre-ruling names, reported either way.

Worker `done` does not imply plan `done`.

## Plan Done Criteria

`SKILL.md` Completion Closeout Gate (canonical).

## Blocked State

`SKILL.md` Validation Gate and Completion Closeout Gate (canonical). Reviewer status `NEEDS_REVISION` or `FAILED` is not approval.

## Closeout Procedure

1. Parse Worker and Reviewer outputs.
2. Run Worker report validation when available.
3. Confirm the `SKILL.md` Validation Gate and Completion Closeout Gate conditions hold, including targeted rule refresh when rule-source files were edited.
4. Update Progress Log and Decision Log.
5. Move completed active plan to `docs/coding-agent/plans/completed/` when applicable.
6. Only then report final done, or, under a brief, close the unit or report the run ready as below.

For a small change built without a plan (`SKILL.md` Plan Gate), step 4 logs in its section of the run record and step 5 has no plan to move.

Before final done, sweep the plan's Decision Log (for a small change, its section of the run record) for entries that pass the admission test in `durable-docs-authoring/references/adr.md` but have no record proposed; propose each missing record on its own for acceptance, or note the user's decline.

Pre-merge existence audit after churn: if the work accumulated repeated fix rounds on one area, apply the existence-audit verdicts in `skills/engineering-quality-baselines/references/long-horizon-audit.md` before merge — triggered by churn, never run continuously.

When a structured closeout summary is available, use the plugin-root-relative `skills/wave-integration/scripts/validate_closeout.py` before final done.

## Closeout Under Value-Level Operation

`SKILL.md` Repository Rule Entry states when value-level operation is on; `references/value-level-operation.md` states how the value audit is dispatched, how a verdict is acted on, and the carrier to Counsel. When it is off, skip this section: the run closes out as above, as `done` or `blocked`.

The closeout audit runs after step 3 and before step 5:

- Dispatch the value audit at position closeout with the fixed template of `references/value-audit-mandate.md`; `Changes since` names the revision the plan started from. Log the dispatch text and the verdict record in the Progress Log as `references/value-level-operation.md` states. For a small change built without a plan this is its one audit, dispatched after the review of the change: `Plan:` names the run record, `Changes since` names the revision the change started from, and both are logged in its section of the run record.
- Act on the verdict as that reference's "Acting On A Verdict" states; closeout does not proceed while anything it calls a gate on the position holds.
- An `ask-now` item goes to the owner by the carrier that reference states (through Counsel, under a brief) before the result is reported as a candidate. It is not settled by the Orchestrator, by Counsel's view, or by reporting it as an open question beside `candidate ready`; a turn that ends before the owner answers ends `blocked` with the value question as the blocker.

When a brief governs the run:

- The run. Work under a ratified brief is a run: one or more units, each a plan-mode plan or a small change built without a plan (`SKILL.md` Plan Gate), taken one after another as the work shows what the next has to be. Each unit is authorized on its own as its kind is: a plan through `SKILL.md` Plan Gate, a small change by the owner's statement in the ratified brief; being in a run authorizes no unit. What the brief gives does not depend on how many units the design takes: a run of one unit is a run, and closes as below. Between units the owner is reached only by what reaches the owner during a unit: an item the audit holds, a question escalated by the carrier, or Counsel's pause.
- The run record. When the run's first unit starts (its first plan drafted, or its first small change logged before its Worker is dispatched), the Orchestrator creates `docs/coding-agent/plans/active/<run>-run.md` with two sections, and a section for each small change built without a plan (below): `Scenarios` (each scenario of the brief and each the run added, with its state as the last audit stated it and that verdict's date), and `Units` (each unit, whether a plan or a small change, its state, and the `Scenarios:` line of its closeout verdict). What one plan leaves to the next is recorded in the next plan's Context section, not here. A scenario's state is `not yet`, `demonstrated` (with how to observe it) or `ready for the owner's judgement`. Those two sections hold only what audits stated: the Orchestrator updates them from each verdict by copying the audit's lines, adds no judgement of its own, and writes no prediction, reading or finding into them. The record also names the readings file, `<run>-readings.md`, which sits beside it and moves with it; what goes in it: `references/value-level-operation.md`.
- A small change's section. Each small change built without a plan has a section of its own in the run record, headed by the change, which holds what a plan would hold for it: where the owner's statement is (the brief's section, and the owner's words as they reached this session), the revision the change starts from, recorded before its Worker is dispatched, the Worker's report outcome and the choices it reported, labelled `Judgement calls`, the Orchestrator's rulings for the change, the review's result, and the closing audit's dispatch text and verdict as `references/value-level-operation.md` logs them for a plan, its two comparison lines going to the readings file.
- Unit closeout. A plan of the run closes with its closeout audit (above) and review; the Plan Done Criteria and steps 4 and 5 are unchanged, so the plan takes status `done` and moves to completed while the run stays open. A small change closes with its review and its closeout audit, and nothing of it is pushed, published or reported as done before that verdict holds nothing. Only then, once per unit, copy the `Scenarios:` line of the closeout verdict the unit closed on into the run record; a closeout audit that is repeated before the unit closes changes nothing in the record. The unit is not reported as `candidate ready`, no note goes to Counsel and nothing is published; the run continues into its next unit.
- Stopping. Whether a run is getting closer to the design is a judgement, not a count, and it is the audit's: each unit's closeout verdict says on its `Scenarios:` line whether the run is getting closer, with the reason, and the run record keeps that line. Where the verdict says it is not and work remains, so that the run would start a further unit, the run has stopped getting closer: it starts no further unit, the outcome is `blocked`, and the owner is told by the carrier, with each scenario's state and the audit's reason as the verdict gives them and nothing argued for going on. A run whose last unit closes with nothing left to build is reported ready as below. The Orchestrator neither makes this judgement nor sets a number for it.
- Reported ready. When the run's last unit has closed, that unit's closeout reports the run ready: it alone carries the outcome, the design document and the note to Counsel below. Each unit's closeout audit graded and marked that unit's judgement calls, so the items shown to the owner and sent to Counsel are the marked items of every unit's closeout verdict, taken from each plan's Progress Log and each small change's section of the run record as the verdict states them. Where a standing approval in effect covers publishing the run's reviewed branches, they are published then and not before.
- While open. A run reported ready stays open for the owner's judgement. A change the owner directs against its brief while it is open is work of the run: a small change, or a plan where the Orchestrator chooses one, authorized as its kind is, built on the run's stack, reviewed and audited at its close, and logged in the run record. While the stack is unmerged the change goes on top of the stack's last branch and takes no branch and no pull request of its own; the text of the pull request it lands in is brought up to date. When it closes, the run is reported ready again as above, the note to Counsel and the publishing included.
- Run closeout. The run closes once: when the owner's acceptance of its stack reaches this session as the owner's word. A small change stated against a brief whose run is already accepted and merged starts a run of its own, of that one change, which takes a branch and a pull request as any run does and closes like any run.
- Outcome. With required work and validation complete, the outcome each time the run is reported ready is `candidate ready` in place of `done`: the run's work is finished and the result awaits the owner's judgement. A closeout summary still carries `plan_status: done`. The brief's human-only pass conditions are not plan validation items; they stay pending and hold back neither the unit nor the outcome. `blocked` keeps its meaning.
- Design document. Update the durable design document the repository keeps for the field the work touched. Where it keeps none for that field, the step does nothing and the closeout says so.
- A closed unit is not reopened: a result the owner rejects returns as a new correction, which while the run is open is a change directed against its brief (While open).
- The brief. Each plan moves to `docs/coding-agent/plans/completed/` at its own closeout. The run record and the readings file stay under `docs/coding-agent/plans/active/`, and the brief and its discussion notes under `docs/coding-agent/briefs/active/`, while the run is open, `candidate ready` included. Once the owner's acceptance of the brief's final stack of pull requests has reached this session as the owner's word, the run closes and the Orchestrator moves the run record and the readings file to `docs/coding-agent/plans/completed/` and the brief and its discussion notes to `docs/coding-agent/briefs/completed/`, all in one change, the same change as the run's last unit when the acceptance has already arrived. The move changes no text in any of these files.
- Note to Counsel. Each time the run is reported ready, tell Counsel that a candidate is ready, by the same carrier as an escalation. The note carries what the result does; what was learned that the philosophies do not account for; and the path of every value document changed during the run, so Counsel can confirm each change is one it wrote. Counsel forms a first read before seeing any part of the auditor's verdict (items let through on a statement marked provisional are sent as they arise, the closeout audit's included, and are the one exception), so the note never carries the verdict record, any grade, the items the audit marked `direction`, whether `inferred` items or judgement calls, or a remark on how the audit went, whether quoted, summarized or pointed to. Once Counsel says its first read is written down, send what it asks for, the marked items as the verdict states them included, as text and not as a pointer into the plan or the run record; Counsel then brings the owner its finished read.
- Counsel's read is advice to the owner and reaches the owner from Counsel, not through this session. Do not wait for it, ask for it or report on it: `candidate ready` does not depend on it.
- Amendments. A result the owner rejects, or an `inferred` item the owner confirms, yields a candidate amendment to a philosophy. Taking it to the owner is Counsel's; the Orchestrator supplies those items in the final response, and to Counsel in the material it sends after Counsel's first read, and never writes to a philosophy.
- A wrong stop or a skipped decision found at closeout or reported by the owner is an `improvement-loop` trigger.
- Final response: the brief part of `references/final-response-contract.md`, which says plainly of a small change built without a plan that it had no plan.
