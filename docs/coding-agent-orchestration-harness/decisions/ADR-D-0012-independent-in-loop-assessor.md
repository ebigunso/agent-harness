---
status: accepted
adr_type: design
date: 2026-07-16
deciders:
  - ebigunso
consulted:
  - Claude Fable 5
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0012: Independent In-Loop Assessor As A Reviewer Dispatch Profile

## Context and Problem Statement

Stall-versus-progress and continue-versus-escalate judgments cannot be made by the goal-pursuing agent: an optimizer under goal pressure rationalizes continuation, and any decision criterion loose enough to require judgment gives it room to make excuses. The judge has a conflict of interest. Separately, mechanical stall detection over self-authored journal labels (approach tags, failure signatures) was considered and rejected: intended or unintended wording drift defeats string matching, and if independent review suffices, redundant mechanical checks fail the deletion test.

The judge's packaging also matters. A fourth named role would put the assessor mandate into runtime instruction blocks (which the verified adapter loading model shows are enforced above thread content, immune to dispatch-message subversion), but it adds replicated instruction blocks across three runtimes, and it does not solve starvation — the loop controls when any assessor is dispatched, whatever its shape.

## Decision Drivers

- The optimizer must never grade its own continuation.
- Assessment must resist subversion through the dispatcher's wording.
- Start small; add parts only on evidence (the fourth role is three more replicated instruction blocks plus role-map and permissions).
- The never-dispatched failure mode needs a home at a gate that actually exists.

## Decision

Assessment is performed by an independent assessor: a Reviewer-role dispatch profile with fresh context that reads only the goal file, the gap history (derived from the journal's per-iteration gap-value entries, not a separate artifact), and the journal — never the optimizer's working context. Its mandate is assessment accuracy, not goal completion, and it carries two co-equal duties:

1. trajectory assessment — is the loop progressing toward the goal? It re-runs the goal condition's gap check itself (reported numbers are not evidence), judges circularity and the credibility of claimed plateau progress semantically from the journal, and tie-breaks toward escalation: continuation bears the burden of proof, because a wrong stop costs one human touch while a wrong continuation compounds;
2. goal validity re-examination — is the goal itself still worth pursuing as stated? This duty is defined in ADR-D-0014; its outcome is a goal-challenge escalation to the user, never an autonomous goal change.

Three hardenings close the dispatch-profile's subversion surface:

1. the assessor mandate lives in the goal-mode skill reference — versioned, immutable during the run, never dispatch prose;
2. the dispatch template is fixed and minimal ("assessor for goal G; read the reference; inputs: goal file, journal, gap history") and the actual dispatch text is journaled verbatim, so framing beyond the template is a visible envelope violation at retrospective;
3. assessment cadence compliance is asserted in the completion report and verified by the pre-merge reviewer against the journal, so a starved assessor invalidates the report and blocks merge.

Assessment cadence is uncertainty-adaptive, driven by journal events (fresh start, post-pivot, suspected stall) with a slow heartbeat as the maximum gap. A fourth named role — mandate in the instruction block — is the recorded upgrade path if trials show dispatcher bias leaking through the fixed template.

## Considered Options

1. Self-assessment by the optimizer with well-defined criteria.
2. Mechanical stall detection over structured journal labels, with review as backup.
3. A fourth named assessor role with instruction-block mandate.
4. A Reviewer-role dispatch profile with mandate-in-reference, fixed journaled dispatch template, and report-gated cadence enforcement.

## Decision Outcome

Chosen option: **Option 4**.

Option 1 puts the conflicted party in the judge's seat. Option 2 loses to wording drift and is redundant beside competent review. Option 3 is the strongest against dispatch-wording subversion but adds real parts, does not solve starvation, and its advantage is only needed if the fixed template proves insufficient — so it is staged as the evidence-gated upgrade rather than built first. The subversion surface of Option 4 is only the dispatcher's wording (a fresh assessor has no in-context pressure), and template deviation inside an append-only record is the same detectability class as not dispatching at all.

## Consequences

### Positive

- The continuation judgment moves to an uninvested party with an accuracy mandate.
- No adapter changes: the reviewer instruction block stays untouched; the assessor profile is dispatch plus reference.
- The asymmetric-cost tie-break makes ambiguity stop the loop instead of extending it.

### Negative / Tradeoffs

- Mid-run assessor starvation has no in-run watcher in any self-driving design; the retrospective backstop is the accepted residual.
- Reference-carried mandates are thread-level, weaker than instruction blocks; the fixed template plus journaling is the compensating control.
- Each assessment is an extra dispatch with cost; the adaptive cadence keeps the count proportionate to uncertainty.

## Validation

- Journaled dispatch texts match the fixed template across a goal run.
- Completion reports carry the assessment assertion and the pre-merge reviewer verifies it against the journal.
- Assessor verdicts cite re-run gap checks, not optimizer-reported numbers.

## Revisit When

- Retrospectives find dispatcher framing effects despite the fixed template (promote to the fourth role).
- Platform evaluator hooks become expressive enough to host the trajectory-level mandate natively.

## More Information

- `docs/coding-agent-orchestration-harness/design/goal-mode-design.md` (pillar 4)
- ADR-D-0003 (runtime-namespaced role identities), ADR-D-0011 (what the assessor judges), ADR-D-0013 (report-gated enforcement)
