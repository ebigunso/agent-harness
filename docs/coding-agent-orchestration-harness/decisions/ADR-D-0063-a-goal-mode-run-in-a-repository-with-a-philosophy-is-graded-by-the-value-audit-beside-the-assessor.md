---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0056-a-goal-mode-run-in-a-repository-with-a-philosophy-is-graded-by-the-value-audit-beside-the-assessor.md"]
superseded_by: null
depends_on: ["ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0029-the-optimizer-never-judges-its-own-continuation.md", "ADR-D-0050-independent-judgement-of-the-orchestrators-work-is-held-by-a-role-of-its-own-the-auditor.md", "ADR-D-0027-the-forbidden-set-is-a-criterion-ratified-before-the-loop.md"]
---

# ADR-D-0063: A goal-mode run in a repository with a philosophy is graded by the value audit beside the assessor

Proposed on 2026-10-29 to replace ADR-D-0056 together with ADR-D-0064; awaiting acceptance by the person directing the work, by name.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. A philosophy is a product philosophy or an engineering philosophy the repository's rules point to. The assessor is the independent judgement of whether a goal loop continues (ADR-D-0029, ADR-D-0050).

The value audit grades a plan-mode run against the value documents (ADR-D-0052), and that record leaves goal mode out. A goal-mode loop runs between human touchpoints inside an envelope ratified before it starts (ADR-D-0027), and its assessor judges continuation from its own evidence alone (ADR-D-0029). Nothing in a goal run is graded against a philosophy, so in a repository that has one, the loop's drift from the values of the person directing the work shows only when the work is built. The fork is whether and how far a goal loop is held to those values as it runs, what an item the audit holds does to the loop, and how the audit is kept from changing what the assessor reads.

## Decision

- In a repository that has a philosophy, the value audit grades a goal-mode run as ADR-D-0052 states it, as a judgement of its own, independent of the Orchestrator and separate from the assessor, over the whole goal run, inside the loop as well as at its ends.
- An item the audit holds stops the loop, as goal mode's own stop for a question does, until the decision is given.
- Nothing of the audit reaches what the assessor reads beyond the stop it causes and the question it puts; the assessor's evidence and mandate are unchanged.
- Goal mode's admission test, stall rule and completion rule are unchanged.
- A goal-mode run in a repository with no philosophy is not graded by the value audit, under a brief or not.

## Why

A goal-mode run in a repository that has a philosophy is to keep to the values of the person directing the work as it goes ("Design-led long runs", "Limits", its one exception for goal mode), so the audit judges inside the loop and not only at its ends. A goal loop is one optimizer with no separable parts to hold, so a held item stops the whole loop, a tightening the brief leaves free; and the assessor's inputs must not change, so the audit's material is kept out of them.

## Rejected Alternatives

- Judgement only at the two ends of the run: it lost because it keeps the run to the values of the person directing the work only at the ends, and drift during the loop shows only when the work is built; reopen if the audit's judgements inside the loop are found to hold nothing run after run.
- A record of each value audit kept where the assessor reads it, so that their number can be checked before merge: rejected outright; it puts audit material into the assessor's evidence.
- A check before merge that the audit judged at every point inside the loop: it lost because the judgement at completion covers the whole run, so a point missed inside the loop is judged with the rest of the run; reopen if a completion judgement is found catching drift that a point missed inside the loop would have caught.
- The part a held item concerns waits and the rest of the loop continues, as in a run under a brief: it lost because a goal loop is one optimizer with no parts to set aside; reopen if goal runs are found stopped whole over a question the loop could have worked around.
- One judgement carrying both the assessor's mandate and the audit's: rejected outright; it changes the assessor's inputs, which ADR-D-0050 and the brief's limit on goal mode keep.

## Decision Boundary

Invariant: in a repository that has a philosophy, a goal run is held to the values of the person directing the work by the value audit, judging independently and apart from the assessor over the whole run, inside the loop as well as at its ends; an item it holds stops the loop; nothing of the audit reaches what the assessor reads beyond the stop and its question; the assessor, the admission test, the stall rule and the completion rule are unchanged; a goal run in a repository with no philosophy is not graded by the audit.

Not covered: who agrees the envelope and on whose authority the loop starts, under a brief or not (ADR-D-0064, ADR-D-0027); at which points of the run the audit judges, how it is asked, where its verdicts and the Orchestrator's readings are kept and which records a stop may touch, which the harness text states; the grades, what they hold and the comparison with the Orchestrator's reading (ADR-D-0052 and the audit's mandate); how a held item's question reaches the person directing the work and how the answer is admitted (ADR-D-0062, ADR-D-0038); the hold on a change that loosens a stop, a pass condition or who decides inside a goal loop; the completion report and the check before merge (ADR-D-0031), which are unchanged.

## Validation

- Review of any change to goal mode's text asks: in a repository with a philosophy, does the value audit judge the run independently, apart from the assessor, inside the loop as well as at its ends; does anything of it reach what the assessor reads beyond a stop and its question; does an item it holds stop the loop; and is a run in a repository with no philosophy left ungraded?

## Revisit When

- The audit's judgements inside the loop are found to hold nothing run after run.
- A completion judgement is found catching drift that a point missed inside the loop would have caught.
- Goal runs are found stopped whole over a question the loop could have worked around.

## More Information

Replaces ADR-D-0056 in full together with ADR-D-0064, which holds who agrees the envelope. Source of intent: `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md`, Limits (the goal-mode exception) and its pass condition on goal mode; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md`), "Directed during the run". The first brief states none of what this record fixes as a means: judgement inside the loop, the stop of the whole loop and the separation from the assessor's evidence are the run's own design. The stop of the whole loop departs from the means that brief states under "A better design noticed mid-flight", that the part a finding concerns waits while the rest continues. On 2026-10-05 the repository that holds the harness has no philosophy, so no goal run there has exercised the audit's attachment. Related: ADR-D-0052 (the value audit), ADR-D-0029 (the assessor), ADR-D-0050 (the Auditor), ADR-D-0027 (the envelope), ADR-D-0028 (the stall rule), ADR-D-0031 (completion and merge), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0064 (whose authority starts the loop). Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
