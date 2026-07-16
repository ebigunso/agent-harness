# Goal Mode: Governed Long-Horizon Autonomy

- status: draft (for discussion; not yet a decision record)
- role: design document — owns the goal-mode architecture and its governance model; implementation sequencing and per-runtime mechanics are companion material at the end
- created: 2026-07-16
- last_updated: 2026-07-16
- terminology frozen in this document: plan mode, goal mode, goal condition, gap, authority envelope, progress obligation, stall, assessor, iteration journal, checkpoint, graded escalation, irreversibility criterion, completion report

## Governing claim

Coding-agent platforms now ship goal engines — turn-continuation loops that keep an agent working until a stated condition is met (`/goal` in Claude Code and Codex, Autopilot in GitHub Copilot). None of them ship governance. Goal mode is the harness's answer: it makes long-horizon autonomy governable by moving human oversight from gate-before-each-decision to envelope, journal, revert, and self-audit — so agents can pursue goals whose task structure is unknown at the start, without giving up the safety properties the harness exists to provide.

## The two operating modes

Plan mode (the current harness) assumes work is decomposable before execution: the human ratifies structure (Task_X, owns, acceptance) and the gates protect that contract. Goal mode inverts the assumption: the goal is the invariant and structure is discovered — attempt, observe, revise, attempt. Each mode is correct for its work shape; forcing either onto the other's shape fails predictably (stale plans and permission-pumping in one direction, ungoverned scope drift in the other).

Both modes share one substrate: the role model, validation and evidence-integrity rules, lessons capture, and the skill library. Goal mode changes the lifecycle around the substrate, not the substrate.

## Mode selection

Use goal mode when all of the following hold:

- the end state is objectively checkable (an executable goal condition exists or can be constructed);
- the task structure is not knowable up front — the work is search-shaped (iterate/measure/revise), not decomposition-shaped;
- every irreversible or outward-facing action can be excluded from the envelope or deferred to a human moment.

Stay in plan mode when the work is decomposable up front, when acceptance is subjective, or when the core of the work is itself irreversible (schema migrations against live data, deletions, releases). When in doubt, plan mode — goal mode is earned by the work shape, not the default.

Canonical goal-mode fits: get the suite green after a dependency bump; raise a benchmark metric above a threshold; drive lint/type debt to zero; port a module set where each port informs the next.

## The six pillars

### 1. Authority envelope

A goal is never accepted bare; it is negotiated with a boundary the user ratifies once, up front:

- decision scope: paths, components, and operation classes the agent may change freely;
- progress obligation: progress is reduction in expected distance to the goal — there is no separate "movement" object. It is measured directly when the goal condition yields a countable gap (failing tests, lint errors, files remaining, benchmark delta), or epistemically on plateaus, where the journal must argue that what was learned credibly reduces the remaining distance or uncertainty toward this goal. A stall — consecutive iterations with the gap unchanged, no credible goal-linkage argument, and attempts circling previously failed approaches — is an ask-now escalation, not something to grind through. Stall detection, not resource ceilings, is the primary runaway defense: it tracks the actual failure mode (continuing without learning) and stays valid across model and platform changes. Coarse resource backstops (wall-clock, cost) may optionally be set by the user but are never the load-bearing mechanism;
- the forbidden set, defined by the irreversibility criterion: any action that is irreversible or outward-facing (merge, deploy, force-push, data deletion, publishing, external service mutation) is outside the envelope by class, not by enumeration. New action types are judged against the criterion, so the envelope does not rot as tooling grows.

Inside the envelope the agent decides freely. At the boundary it escalates (pillar 5). The envelope is recorded in the goal file and is itself immutable during the run — renegotiation is a human moment.

### 2. Iteration journal and checkpoints

With no per-decision human gate, the evidence trail becomes the oversight surface:

- each iteration appends a journal entry: hypothesis, what was attempted, observed evidence, decision for the next iteration;
- each iteration that changes the worktree ends in a checkpoint commit on the goal branch, so any iteration can be reverted in isolation;
- rollback is the safety property: a human retrospective reviews the journal, and any wrong turn is cheap to undo. Oversight moves from approve-before to review-after precisely because revert is guaranteed cheap.

The journal is the goal-mode analogue of the plan file: same repository home, same single-writer rule, same append-only discipline.

Artifact layout and terminal semantics: each goal is a directory — `docs/coding-agent/goals/active/<goal-id>/` containing `goal.md` (statement, condition with its protected gap reading and linkage credibility bar, envelope, cadence, status) and `journal.md` (append-only iterations and assessor records). Goal status is one of `draft | active | awaiting_decision | completed | aborted | abandoned`: an ask-now escalation sets `awaiting_decision` and the directory stays under `active/` until the human decides (resume, re-ratify, or abandon); every terminal outcome (`completed`, `aborted`, `abandoned`) archives the whole directory to `docs/coding-agent/goals/completed/` with the final status preserved in `goal.md`, so target-met, abort, and abandonment remain distinguishable after archiving.

Lifecycle selection: at the Plan Gate position, non-trivial work selects exactly one lifecycle. When goal mode is selected, envelope ratification replaces plan approval, the journal with checkpoint commits replaces the Task_X lifecycle, and the completion report with human retrospective replaces plan closeout; every other gate and safety property (validation and evidence rules, role boundaries, Git safety, the merge hard stop) applies unchanged in both modes.

### 3. Tamper-evident goal conditions

A self-driving loop optimizes its stop condition, so the condition must resist being gamed (Goodhart pressure):

- every goal condition names both the target and the invariants that may not be touched to reach it ("suite green without modifying test files"; "benchmark above X with the eval harness unchanged");
- condition evaluation runs against evidence produced under the existing evidence-integrity rules — targeted reruns, positive executed-test counts, no ignore-blind absence claims. Those rules were written for honesty toward humans; here they defend the loop against self-deception;
- weakening an invariant (deleting a failing test, relaxing an assertion, touching the measurement harness) is treated as leaving the envelope: escalate, never absorb;
- the gap reading and the credibility bar for epistemic goal-linkage are part of the condition: they may be tightened freely mid-run, but loosening either is invariant pressure — ask-now. Proxy metrics (cheaper intermediate signals) may inform the journal but are never load-bearing.

The existing test-authoring guidance is load-bearing here: tests that assert behavior contracts are exactly the tests a goal loop cannot legitimately game.

### 4. Independent in-loop assessment

Long horizons compound error silently, and a goal-pressured optimizer judging its own stall will rationalize continuation — the judge must not be the party with the conflict of interest. The optimizer produces evidence; an independent assessor decides.

- The assessor is a separate dispatch with fresh context that reads only the goal file (condition, envelope), the gap history, and the journal — never the optimizer's working context. No sunk cost, no accumulated rationalization chain; its mandate is assessment accuracy, not goal completion. This extends the harness's existing role separation (Workers do not verify their own acceptance) into the loop, and upgrades the platforms' separate-evaluator pattern from judging the stop predicate to judging the trajectory.
- Role shape (resolved 2026-07-16): the assessor is a Reviewer-role dispatch profile, not a fourth named role, with three hardenings against dispatcher subversion. The mandate lives in the goal-mode skill reference — versioned, immutable during the run, never dispatch prose (the reviewer instruction block stays untouched; no mixed instructions). The dispatch template is fixed and minimal ("assessor for goal G; read the reference; inputs: goal file, journal, gap history") and the actual dispatch text is journaled verbatim, so framing beyond the template is a visible envelope violation at retrospective. The subversion surface is only the dispatcher's wording — a fresh-context assessor has no in-context pressure to resist — and template deviation inside an append-only record is the same detectability class as not dispatching at all. A fourth named role (instruction-block enforcement of the mandate, per the verified adapter loading model) is the recorded upgrade path if trials show dispatcher bias leaking through the template — evidence-gated promotion, same discipline as automation-last.
- Starvation (the loop never dispatching its assessor) is orthogonal to role shape and is enforced at the strongest existing gate instead: assessment evidence at the required cadence is part of the completion-report contract (pillar 6), so completion cannot be claimed without it and a starved assessor surfaces at the merge retrospective as an invalid report. Mid-run starvation has no watcher in any self-driving design; the retrospective backstop is the accepted residual.
- The assessor carries two co-equal duties. Trajectory assessment: it re-runs the goal condition's gap check itself (evidence-integrity: reported numbers are not evidence) and rules on the judgment-heavy signals — epistemic goal-linkage credibility, circularity (judged semantically from the journal; self-authored labels and mechanical matching are defeated by wording drift and are deliberately not used), and drift-tripwire patterns in the journal. Goal validity re-examination: is the goal itself still worth pursuing as stated — do its founding assumptions survive the run's evidence, would satisfying the stated condition still deliver the intended outcome, should it be re-scoped or abandoned per the five-step discipline's first duty (question the requirements)? A failed validity examination produces a goal-challenge escalation to the user with the prompting evidence; the loop never changes its own goal. Efficient progress toward a wrong goal is the worst goal-mode failure — worse than any stall — which is why validity is a standing duty, not an occasional check.
- Continuation bears the burden of proof: the assessor's tie-break is escalate. The costs are asymmetric — a wrong stop costs one human touch (ask-now is a successful termination), a wrong continuation compounds error and spend.
- Assessment cadence is uncertainty-adaptive, not a fixed interval: early iterations of a fresh goal; the iterations immediately after a major pivot (approach change, goal re-scoping, surprising evidence); a suspected stall; and a slow heartbeat as the maximum gap so assessment never stops entirely. The journal's own events drive the cadence — turn counts are a weak proxy.
- Journal structure serves the assessor: each iteration entry commits a falsifiable prediction of what the next iteration will change. Predictions are not machine-checked; their value is that an append-only committed expectation is harder to narrate around than a retrospective story — the assessor compares the committed claim against the observed outcome.

### 5. Graded escalation

Plan mode's binary (proceed / blocked) is too coarse for autonomy. Goal mode uses four levels:

- proceed: in-envelope decision; act, journal briefly;
- decide-and-journal: in-envelope but judgment-heavy; act, journal the decision with rationale, flag for retrospective review;
- ask-now: envelope boundary hit (forbidden class, invariant pressure, budget exhaustion, self-audit failure); stop the loop, surface the question, wait;
- abort: safety condition (destructive surprise, evidence of data exposure, runaway behavior); stop, revert to the last good checkpoint, report.

A goal condition is therefore never just "the target is met": it is "the target is met, or an ask-now/abort state is reached" — reaching a human moment is a successful termination of the loop, not a failure to grind through. This is the single most important line of defense against the platforms' native goal pressure (Copilot's synthetic "you aren't done" nudge being the sharpest case).

### 6. Completion report and human retrospective

Goal completion is not merge authorization. Before the goal branch may merge, the loop produces a self-asserted completion report — concise and contract-shaped, so the human reviews a report, not a pile of journal text:

- goal condition satisfied, with the evidence (per pillar 3 rules) inline;
- assessment assertion: one concise statement that assessor dispatches occurred at the required cadence and complied with the fixed dispatch template. The verbatim dispatch texts and verdicts stay in the journal (pillar 4), not the report; the pre-merge reviewer verifies the assertion against the journal — along with the report's other assertions — before the report is accepted. A report whose assessment assertion fails verification is invalid and cannot support merge;
- invariant integrity assertions: each named invariant untouched, with the check that proves it;
- envelope compliance: no forbidden-class actions taken; every decide-and-journal item listed with its rationale, so judgment-heavy calls are surfaced for exactly the review they were flagged for;
- trajectory summary: pivots taken, stalls hit, what was abandoned and why;
- checkpoint index: which commits map to which iterations, so any single decision can be inspected or reverted from the report alone.

The journal remains the backing audit trail; the report is the human interface to it. Merge stays behind the existing hard stop, informed by this report — the retrospective is cheap because the loop pre-asserted everything a retrospective would otherwise have to dig for.

## Runtime mapping (companion detail)

The engine differs per platform; the governance above is engine-agnostic and lives in harness content, not in platform configuration.

- Claude Code `/goal`: independent fast-evaluator gate per turn; goals survive `--resume`. The harness goal condition (target + invariants + escalation clause) is given verbatim as the `/goal` condition; the evaluator's judgment is advisory — pillar-3 evidence rules decide, not the evaluator alone.
- Codex goals (`features.goals`): thread-attached, semi-manual continuation; the loop is driven by the harness cadence with the goal as tracked state.
- GitHub Copilot Autopilot: `task_complete`-gated with synthetic continuation nudges and `--max-autopilot-continues`; the nudge must never override an ask-now/abort state — the escalation clause is part of task completion, and the continue cap is set from the envelope's iteration budget.

Per the environment-gating rule, this mapping belongs in a gated reference read only when a goal-capable runtime is in play.

## Risks and resolved design questions

- Compounding error: mitigated by checkpoints and the uncertainty-adaptive self-audit cadence (pillar 4). Resolved 2026-07-16: cadence is event-driven (fresh start, post-pivot, stall, heartbeat maximum), not a fixed turn count — turns are a weak proxy for uncertainty.
- Runaway continuation: resolved 2026-07-16 by reframing — resource budgets were a vague proxy; the actual failure mode is continuing without progress, and the primary defense is the envelope's progress obligation with stall-based escalation (model- and platform-agnostic). Optional coarse resource backstops remain available but are never load-bearing.
- Goodhart residue: invariants can be enumerated imperfectly. Resolved 2026-07-16: goal-condition construction gets its own checklist and a reviewer pass before the loop starts.
- Oversight debt: resolved 2026-07-16: goal completion requires the pillar-6 self-asserted completion report, and merge stays behind the existing human hard stop informed by that report.
- Mode misuse: the temptation to route decomposable work through goal mode to skip planning. Mitigation: the mode-selection test above, enforced at the same place the Plan Gate lives today.
- Stall interpretation under goal pressure: resolved 2026-07-16 — progress collapses to one object (reduction in expected distance to the goal; no separate movement definition), and the stall/continuation judgment is made by the independent assessor (pillar 4), never by the optimizer; continuation bears the burden of proof. Mechanical circularity detection was considered and rejected (self-authored labels lose to wording drift); the one retained journal structure is the committed per-iteration prediction, valued for constraining narrative, not for machine matching.
- Assessor role shape: resolved 2026-07-16 — Reviewer-role dispatch profile with mandate-in-reference, fixed journaled dispatch template, and completion-report cadence enforcement; fourth named role recorded as the evidence-gated upgrade path.
- Completion-report enforcement: resolved 2026-07-16 — reviewer-verified prose, not a validator-checked contract (the report is judgment-heavy; a validator would check shape, not truth). The pre-merge reviewer autonomously verifies the report's assertions — assessment cadence and template compliance, invariant integrity, envelope compliance — against the journal before the report is accepted; verbatim evidence stays in the journal to keep the report readable.

## Incremental adoption path (companion detail)

1. Content first, no new machinery: a goal-mode reference set under orchestration-harness (mode selection, envelope negotiation, condition construction, journal format, escalation protocol) plus a `goals/` lifecycle mirroring `plans/`. The loop itself can run on any platform's engine — or manually — from day one.
2. Instrument: journal, envelope, and completion-report templates; the condition-construction checklist with its pre-loop reviewer pass; self-audit prompts wired to the existing five-step lens.
3. Trial on a canonical fit (suite-green or lint-zero class goal) in one target repo with tight budgets; capture lessons; iterate the references.
4. Only then consider validators or automation (drift checks on journals, budget accounting) — automation last, per the discipline.
