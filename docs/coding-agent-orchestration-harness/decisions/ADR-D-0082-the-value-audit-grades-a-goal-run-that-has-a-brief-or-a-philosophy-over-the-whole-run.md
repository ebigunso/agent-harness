---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0063-a-goal-mode-run-under-a-brief-or-with-a-philosophy-is-graded-over-the-whole-run-by-the-value-audit-beside-the-assessor.md"]
superseded_by: null
depends_on: ["ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0050-independent-judgement-of-the-orchestrators-work-is-held-by-a-role-of-its-own-the-auditor.md", "ADR-D-0084-no-goal-loop-starts-without-an-authority-envelope.md"]
---

# ADR-D-0082: The value audit grades a goal run that has a brief or a philosophy over the whole run

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition inside an envelope fixed before the loop starts (ADR-D-0084). The person directing the work is the one who says what the work should do and judges what is built from its behaviour. A brief is a ratified brief governing the run. A philosophy is a product philosophy or an engineering philosophy the repository's rules point to. The value documents are the brief and the philosophies. The value audit is the independent judgement of how a run's items stand against the value documents (ADR-D-0052).

ADR-D-0052 states the value audit for a plan-mode run and leaves goal mode out. A goal loop runs between human touchpoints, so its drift from the brief it serves or from the repository's philosophy has no moment at which a person would see it. The fork is whether a goal run is held to the value documents at all, how much of the run is graded, and what an item the audit holds does to the loop.

## Decision

- A goal run under a brief, or in a repository that has a philosophy, is graded by the value audit over the whole run: its envelope, its loop while the loop runs, and its result. Under a brief the run is graded against the brief, and against the repository's philosophy as well where there is one. A goal run with neither a brief nor a philosophy is not graded by the value audit.
- An item the audit holds stops the whole loop until the decision is given. The one exception, under a brief, is an item whose remedy is already determined within the run's authority (ADR-D-0067).

## Why

A goal loop runs between human touchpoints, so left ungraded its drift from the brief or the philosophy shows only when the work is built; graded over the whole run, the drift shows while the loop runs. A held item stops the whole loop because a goal loop is one optimizer with no parts to set aside.

## Rejected Alternatives

- Under a brief, only the envelope graded, or any goal run judged only at the ends of the run: it lost because drift during the loop then shows only when the work is built; reopen if the audit's judgements inside the loop are found to hold nothing run after run.
- A check before merge that the audit judged at every point inside the loop: it lost because the judgement at completion covers the whole run, so a point missed inside the loop is judged with the rest of the run; reopen if a completion judgement is found catching drift that a point missed inside the loop would have caught.
- The part a held item concerns waits and the rest of the loop continues, as in a plan-mode run under a brief: it lost because a goal loop is one optimizer with no parts to set aside; reopen if goal runs are found stopped whole over a question the loop could have worked around.

## Decision Boundary

Not covered: that nothing of the audit enters what the assessor reads (ADR-D-0083); the audit itself, its independence of the Orchestrator, its grades and what they hold, and the comparison with the Orchestrator's reading (ADR-D-0052, ADR-D-0050, and the audit's mandate); under a brief, an item whose remedy is already determined, carried out by the run without a stop (ADR-D-0067); who authorizes the envelope and on what conditions (ADR-D-0064, ADR-D-0065); what an envelope consists of and that the loop never changes it (ADR-D-0084, ADR-D-0085, ADR-D-0086); the test that admits work to goal mode (ADR-D-0073), the stall rule (ADR-D-0074) and the completion report with the check before merge (ADR-D-0075), none of which this record touches; how a held item's question reaches the person directing the work and how the answer is admitted (ADR-D-0062, ADR-D-0038); at which points of the run the audit judges, how it is asked, where its verdicts and the Orchestrator's readings are kept, and which records a stop may touch, which goal mode's text states.

## Validation

The decision is broken where:

- a goal run under a brief or in a repository with a philosophy reached its end with its envelope, a stretch of its loop or its result judged by no value audit, or a run under a brief was graded against the philosophy and not the brief;
- a loop went on working while an item the audit held waited for a decision, other than as ADR-D-0067 states.

## Revisit When

- The premise that drift arises inside a goal loop and is caught by judging there no longer holds: the audit's judgements inside the loop are found to hold nothing run after run.
- The premise that the judgement at completion covers what a point missed inside the loop would have judged no longer holds: a completion judgement is found catching drift that a point missed inside the loop would have caught.
- The premise that a goal loop has no part to set aside no longer holds: goal runs are found stopped whole over a question the loop could have worked around.
- None of these premises had been exercised when ADR-D-0063 stated them: on 2026-10-05 the repository that holds the harness had no philosophy, so no goal run there had been graded by the audit, and on 2026-11-07 no goal run under a brief had run. The failures that reopen this record are the three above.

## More Information

Replaces ADR-D-0063 at the audit's coverage of a goal run and what an item it holds does to the loop; ADR-D-0083 replaces it at the separation from the assessor's evidence. The stop of the whole loop departs from the means stated in `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md` under "A better design noticed mid-flight", that the part a finding concerns waits while the rest continues. Source of intent: that brief, Limits (the goal-mode exception) and its pass condition on goal mode; `docs/coding-agent/briefs/completed/quiet-orchestrator-session-brief.md`, "Directed during the run". Related: ADR-D-0052 (the value audit), ADR-D-0050 (the Auditor), ADR-D-0067 (a determined remedy carried out without a stop under a brief), ADR-D-0065 (when a ratified brief authorizes a goal envelope). Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
