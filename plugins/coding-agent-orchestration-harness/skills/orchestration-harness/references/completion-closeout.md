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
6. Only then report final done, or `candidate ready` for a run under a brief (below).

Before final done, sweep the plan's Decision Log for entries that pass the admission test in `durable-docs-authoring/references/adr.md` but have no record proposed; propose each missing record on its own for acceptance, or note the user's decline.

Pre-merge existence audit after churn: if the work accumulated repeated fix rounds on one area, apply the existence-audit verdicts in `skills/engineering-quality-baselines/references/long-horizon-audit.md` before merge — triggered by churn, never run continuously.

When a structured closeout summary is available, use the plugin-root-relative `skills/wave-integration/scripts/validate_closeout.py` before final done.

## Closeout Under Value-Level Operation

`SKILL.md` Repository Rule Entry states when value-level operation is on; `references/value-level-operation.md` states how the value audit is dispatched, how a verdict is acted on, and the carrier to Counsel. When it is off, skip this section: the run closes out as above, as `done` or `blocked`.

The closeout audit runs after step 3 and before step 5:

- Dispatch the value audit at position closeout with the fixed template of `references/value-audit-mandate.md`; `Changes since` names the revision the run started from. Log the dispatch text and the verdict record verbatim in the Progress Log.
- Act on the verdict as that reference's "Acting On A Verdict" states; closeout does not proceed while anything it calls a gate on the position holds.
- An `ask-now` item goes to the owner by the carrier that reference states (through Counsel, under a brief) before the result is reported as a candidate. It is not settled by the Orchestrator, by Counsel's view, or by reporting it as an open question beside `candidate ready`; a turn that ends before the owner answers ends `blocked` with the value question as the blocker.

When a brief governs the run:

- Outcome. With required work and validation complete, the outcome is `candidate ready` in place of `done`: the run's work is finished and the result awaits the owner's judgement. The Plan Done Criteria and steps 4 and 5 are unchanged, so the plan takes status `done`, moves to completed, and a closeout summary still carries `plan_status: done`. The brief's human-only pass conditions are not plan validation items; they stay pending and hold back neither the plan nor the outcome. `blocked` keeps its meaning.
- A result the owner rejects returns as a new correction; the closed plan is not reopened.
- The brief. Step 5 moves the plan only; the brief and its discussion notes stay under `docs/coding-agent/briefs/active/` at `candidate ready`. Once the owner's acceptance of the brief's final stack of pull requests has reached this session as the owner's word, the Orchestrator moves both together to `docs/coding-agent/briefs/completed/`, in the same change as the plan when the acceptance has already arrived. The move changes no text in either file.
- Note to Counsel. Tell Counsel that a candidate is ready, by the same carrier as an escalation. The note carries what the result does; what was learned that the philosophies do not account for; and the path of every value document changed during the run, so Counsel can confirm each change is one it wrote. Counsel forms a first read before seeing any part of the auditor's verdict (watch hits and provisional-statement items are sent as they arise, the closeout audit's included, and are the one exception), so the note never carries the verdict record, any grade, the items the audit marked `direction`, whether `inferred` items or judgement calls, or a remark on how the audit went, whether quoted, summarized or pointed to. Once Counsel says its first read is written down, send what it asks for, the marked items as the verdict states them included, as text and not as a pointer into the plan; Counsel then brings the owner its finished read.
- Counsel's read is advice to the owner and reaches the owner from Counsel, not through this session. Do not wait for it, ask for it or report on it: `candidate ready` does not depend on it.
- Amendments. A result the owner rejects, or an `inferred` item the owner confirms, yields a candidate amendment to a philosophy. Taking it to the owner is Counsel's; the Orchestrator supplies those items in the final response, and to Counsel in the material it sends after Counsel's first read, and never writes to a philosophy.
- A wrong stop or a skipped decision found at closeout or reported by the owner is an `improvement-loop` trigger.
- Final response: the brief part of `references/final-response-contract.md`.
