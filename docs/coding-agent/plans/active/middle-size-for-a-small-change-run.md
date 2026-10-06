# Run record: A middle size for a small change

- Governing brief: `docs/coding-agent/briefs/active/small-change-from-his-word-brief.md`
- Run starts from revision: 12b1892
- State: reported ready 2026-10-06 (candidate ready); open for the owner's judgement; closes on his acceptance of its stack

## Scenarios

State is one of: not yet; demonstrated (with how to observe); ready for the owner's judgement.

| Scenario | State |
| --- | --- |
| 1. With a stack unmerged, he states a one-sentence change to something already built. It is built on top of the stack, reviewed and audited once at its close, with no plan document and no new pull request, and he is told when it is done. | not yet |

## Units

| Unit | State | What its closeout audit found |
| --- | --- | --- |
| `docs/coding-agent/plans/completed/middle-size-for-a-small-change-plan.md` | authorized under the ratified brief 2026-10-06; closed 2026-10-06 | Scenarios: 1 not yet (the text is in place; no small change built this way yet); getting closer: yes (closeout verdict logged in full in the plan) |

## Small change 1: the run record holds only what audits stated; a small change's trace is kept beside it

- Directed by the owner while the run is open, on the closeout items C4 and J10. His words, relayed by Counsel on 2026-10-06 (admitted by the standing approval of 2026-10-01), quoted in full: "Yes, keep the rule and move the trace to the readings file, or any other place that is appropriate." Counsel's proposal he answered: keep ADR-D-0051's rule and move the small-change trace out of the run record, the run record keeping only the audit verdict on it; a text change, no record returning.
- Where the statement stands in the brief: `docs/coding-agent/briefs/active/small-change-from-his-word-brief.md`, section "A small change and the run", the gives-statement added 2026-10-06 with his quoted words (committed after the start revision, on this branch).
- Starts from revision: 32f0c67.
- The Orchestrator's call that this is small and needs no plan: one task, text only, in the files that say where a small change's trace lives; his statement leaves the place open and delegates it ("or any other place that is appropriate"), so the Orchestrator chooses: a file `<run>-changes.md` beside the run record, moving with it, since the readings file may be opened by the auditor only after grading and the trace is what the audit grades.
