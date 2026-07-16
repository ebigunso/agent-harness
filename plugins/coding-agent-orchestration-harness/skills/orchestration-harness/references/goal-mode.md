# Goal Mode

Use this reference when deciding whether work belongs in goal mode and when operating a goal-mode run: envelope negotiation, the iteration loop, escalation, and the goals/ lifecycle.

Cross-routes (do not duplicate; read when needed):

- Assessor mandate and fixed dispatch template: `references/goal-assessor-mandate.md`
- Goal-condition construction checklist (pre-loop, with reviewer pass): `references/goal-condition-checklist.md`
- Goal file, journal entry, and completion-report templates: `references/goal-templates.md`
- Runtime goal-engine mapping (read only when a goal-capable runtime is in play): `references/goal-engines.md`

## Two Operating Modes

- Plan mode assumes work is decomposable before execution: the human ratifies structure (Task_X, owns, acceptance) and the gates protect that contract.
- Goal mode inverts the assumption: the goal is the invariant and structure is discovered — attempt, observe, revise, attempt.
- Each mode is correct for its work shape; forcing either onto the other's shape fails predictably (stale plans and permission-pumping in one direction, ungoverned scope drift in the other).
- Both modes share one substrate: the role model, validation and evidence-integrity rules, lessons capture, and the skill library. Goal mode changes the lifecycle around the substrate, not the substrate.
- When goal mode is selected at the Plan Gate position, envelope ratification replaces plan approval, the journal with checkpoint commits replaces the Task_X lifecycle, and the completion report with human retrospective replaces plan closeout; every other gate and safety property applies unchanged in both modes.

## Mode-Selection Test

Use goal mode only when ALL of the following hold:

- the end state is objectively checkable: an executable goal condition (a check that decides "met / not met" without human judgment) exists or can be constructed;
- the task structure is not knowable up front — the work is search-shaped (iterate/measure/revise), not decomposition-shaped;
- every irreversible or outward-facing action can be excluded from the envelope or deferred to a human moment.

Stay in plan mode when the work is decomposable up front, when acceptance is subjective, or when the core of the work is itself irreversible (schema migrations against live data, deletions, releases). When in doubt, plan mode — goal mode is earned by the work shape, not the default.

Routing decomposable work through goal mode to skip planning is misuse; record it when observed.

Canonical fits: get the suite green after a dependency bump; raise a benchmark metric above a threshold; drive lint/type debt to zero; port a module set where each port informs the next.

Before the loop starts, construct the goal condition with `references/goal-condition-checklist.md` (includes a reviewer pass).

## Authority Envelope

A goal is never accepted bare. Negotiate an authority envelope — the boundary of the loop's autonomy — with the user, ratified once up front and recorded in the goal file (template: `references/goal-templates.md`). It contains:

- Decision scope: paths, components, and operation classes the loop may change freely.
- Progress obligation: progress is reduction in expected distance to the goal — there is no separate "movement" object. Measure it:
  - directly, when the goal condition yields a countable gap (failing tests, lint errors, files remaining, benchmark delta);
  - epistemically on plateaus, where the journal must argue that what was learned credibly reduces the remaining distance or uncertainty toward this goal.
- Stall: consecutive iterations with the gap unchanged, AND no credible goal-linkage argument, AND attempts circling previously failed approaches. A stall is an ask-now escalation, not something to grind through. Stall detection — not resource ceilings — is the primary runaway defense: it tracks the actual failure mode (continuing without learning) and stays valid across model and platform changes.
- Optional resource backstops: coarse ceilings (wall-clock, cost) the user may set; never the load-bearing mechanism.
- Forbidden set, defined by the irreversibility criterion as a class, not a list: any action that is irreversible or outward-facing (merge, deploy, force-push, data deletion, publishing, external-service mutation) is outside the envelope. New action types are judged against the criterion, so the envelope does not rot as tooling grows.

Inside the envelope the loop decides freely. At the boundary it escalates (see Graded Escalation). The envelope is itself immutable during the run — renegotiation is a human moment.

## Iteration Lifecycle

With no per-decision human gate, the evidence trail is the oversight surface. Each iteration:

1. Attempt: act on the current hypothesis within the envelope.
2. Journal: append an entry (format: `references/goal-templates.md`) — hypothesis, what was attempted, observed evidence, gap value, decision for the next iteration, and a committed falsifiable prediction of what the next iteration will change. The committed prediction constrains narrative: an append-only expectation is harder to narrate around than a retrospective story, and the assessor compares it against the observed outcome.
3. Checkpoint: every iteration that changes the worktree ends in a checkpoint commit on the goal branch, so any iteration can be reverted in isolation.

Rollback is the safety property: a human retrospective reviews the journal, and any wrong turn is cheap to undo. Oversight moves from approve-before to review-after precisely because revert is guaranteed cheap.

## Tighten-Free, Loosen-Escalates

The gap reading (how the countable gap is measured) and the credibility bar for epistemic goal-linkage are part of the goal condition:

- Tightening either mid-run is free.
- Loosening either is invariant pressure — ask-now, never absorb.

Likewise, weakening any named invariant (deleting a failing test, relaxing an assertion, touching the measurement harness) is treated as leaving the envelope: escalate, never absorb. Proxy metrics (cheaper intermediate signals) may inform the journal but are never load-bearing.

## Graded Escalation

Four levels replace plan mode's binary proceed/blocked:

- proceed: in-envelope decision; act, journal briefly.
- decide-and-journal: in-envelope but judgment-heavy; act, journal the decision with rationale, flag for retrospective review.
- ask-now: envelope boundary hit (forbidden class, invariant pressure, budget exhaustion, self-audit failure, stall); stop the loop, surface the question, wait.
- abort: safety condition (destructive surprise, evidence of data exposure, runaway behavior); stop, revert to the last good checkpoint, report.

A goal condition is never just "the target is met": it is "the target is met, OR an ask-now/abort state is reached". Reaching a human moment is a successful termination of the loop, not a failure to grind through. This is the single most important defense against platform engines' native goal pressure.

## Assessment Cadence

An independent assessor (a fresh-context Reviewer-role dispatch; mandate and fixed dispatch template: `references/goal-assessor-mandate.md`) judges the trajectory — the optimizer never judges its own stall. Cadence is uncertainty-adaptive, driven by the journal's own events, not a fixed interval:

- early iterations of a fresh goal;
- the iterations immediately after a major pivot (approach change, goal re-scoping, surprising evidence);
- a suspected stall;
- a slow heartbeat as the maximum gap, so assessment never stops entirely.

Assessment evidence at this cadence is part of the completion report (template: `references/goal-templates.md`); completion cannot be claimed without it.

## Goals/ Lifecycle Convention

The goal file and journal are the goal-mode analogue of the plan file:

- Layout: each goal is a directory — `docs/coding-agent/goals/active/<goal-id>/` containing `goal.md` (statement, condition, envelope, cadence, status) and `journal.md` (append-only iterations and assessor records).
- Status vocabulary: `draft | active | awaiting_decision | completed | aborted | abandoned`.
- An ask-now escalation sets `awaiting_decision` and the directory stays under `active/` until the human decides: resume (back to `active`), re-ratify (back to `active` with a new envelope), or abandon.
- Every terminal outcome (`completed`, `aborted`, `abandoned`) archives the whole directory to `docs/coding-agent/goals/completed/` with the final status preserved in `goal.md`, so target-met, abort, and abandonment stay distinguishable after archiving.
- Create the directories per-repo at first use, like `plans/`; no scaffolding ships.
- Single-writer: only the Orchestrator writes the goal file and journal.
- The journal is append-only.
