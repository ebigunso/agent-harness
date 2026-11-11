---
status: accepted
adr_type: design
date: 2026-11-07
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["superseded/ADR-D-0056-a-goal-mode-run-with-a-philosophy-is-graded-by-the-value-audit-beside-the-assessor--superseded-by-ADR-D-0063.md"]
superseded_by: null
depends_on: ["ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0029-the-optimizer-never-judges-its-own-continuation.md", "ADR-D-0050-independent-judgement-of-the-orchestrators-work-is-held-by-a-role-of-its-own-the-auditor.md", "ADR-D-0066-a-goal-loops-forbidden-set-is-a-criterion-and-its-envelope-is-fixed-before-the-loop-and-never-changed-by-it.md"]
---

# ADR-D-0063: A goal-mode run under a brief or with a philosophy is graded over the whole run by the value audit beside the assessor

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. A philosophy is a product philosophy or an engineering philosophy the repository's rules point to. A brief is a ratified brief governing the run. The assessor is the independent judgement of whether a goal loop continues (ADR-D-0029, ADR-D-0050).

The value audit grades a plan-mode run against the value documents (ADR-D-0052), and that record leaves goal mode out. A goal-mode loop runs between human touchpoints inside an envelope fixed before it starts (ADR-D-0066), and its assessor judges continuation from its own evidence alone (ADR-D-0029). Ungraded, a goal loop's drift from the brief it serves or from the repository's philosophy shows only when the work is built. The fork is whether and how far a goal loop is held to the value documents as it runs, what an item the audit holds does to the loop, and how the audit is kept from changing what the assessor reads.

## Decision

- A goal-mode run under a brief, or in a repository that has a philosophy, is graded by the value audit as ADR-D-0052 states it: a judgement of its own, independent of the Orchestrator and separate from the assessor, over the whole run, before the loop starts, inside it and at its end. Under a brief the run is graded against the brief, and against the repository's philosophy as well where it has one.
- An item the audit holds stops the loop until the decision is given, as goal mode's own stop for a question does. Under a brief, ADR-D-0067 states the one exception: an item whose remedy is already determined within the run's authority.
- Nothing of the audit reaches what the assessor reads beyond a stop it causes and the question put. The assessor's evidence and mandate are unchanged.
- Goal mode's admission test, stall rule and completion rule are unchanged.
- A goal-mode run with neither a brief nor a philosophy is not graded by the value audit.

## Why

A goal loop runs between human touchpoints, so left ungraded its drift from the brief or the philosophy shows only when the work is built; graded over the whole run, the drift shows while the loop runs. The audit is kept apart from the assessor because the two judge different things, the assessor whether the loop is still closing its gap and the audit whether the work fits the value documents, and continuation bears the burden of proof (ADR-D-0029), so a favourable grade among the assessor's inputs would argue for continuing.

## Rejected Alternatives

- Under a brief, only the envelope graded, or any goal run judged only at the ends of the run: it lost because drift during the loop then shows only when the work is built; reopen if the audit's judgements inside the loop are found to hold nothing run after run.
- A record of each value audit kept where the assessor reads it, so that their number can be checked before merge: rejected outright; it puts audit material into the assessor's evidence.
- A check before merge that the audit judged at every point inside the loop: it lost because the judgement at completion covers the whole run, so a point missed inside the loop is judged with the rest of the run; reopen if a completion judgement is found catching drift that a point missed inside the loop would have caught.
- The part a held item concerns waits and the rest of the loop continues, as in a plan-mode run under a brief: it lost because a goal loop is one optimizer with no parts to set aside; reopen if goal runs are found stopped whole over a question the loop could have worked around.
- One judgement carrying both the assessor's mandate and the audit's: rejected outright; it puts the audit's grade among the assessor's inputs, where a favourable grade would argue for continuing a loop whose continuation bears the burden of proof (ADR-D-0029).

## Decision Boundary

Invariant: a goal run under a brief or in a repository that has a philosophy is held to the value documents by the value audit, judging independently and apart from the assessor over the whole run, before, inside and at the end of the loop, under a brief against the brief and against a philosophy as well where the repository has one; an item it holds stops the loop, except as ADR-D-0067 states under a brief; nothing of the audit reaches what the assessor reads beyond a stop and its question; the assessor, the admission test, the stall rule and the completion rule are unchanged; a goal run with neither a brief nor a philosophy is not graded by the audit.

Not covered: who authorizes the envelope and on what conditions (ADR-D-0064, ADR-D-0065); what an envelope consists of and that the loop never changes it (ADR-D-0066); under a brief, an item whose remedy is already determined, carried out by the run without a stop, and how that remediation reaches what the assessor reads (ADR-D-0067); at which points of the run the audit judges, how it is asked, where its verdicts and the Orchestrator's readings are kept, and which records a stop may touch, which the harness text states; the grades, what they hold and the comparison with the Orchestrator's reading (ADR-D-0052 and the audit's mandate); how a held item's question reaches the person directing the work and how the answer is admitted (ADR-D-0062, ADR-D-0038); the hold on a change that loosens a stop, a pass condition or who decides inside a goal loop; the completion report and the check before merge (ADR-D-0075), which are unchanged.

## Validation

- Review of any change to goal mode's text asks: under a brief or in a repository with a philosophy, does the value audit judge the run independently, apart from the assessor, before, inside and at the end of the loop, under a brief against the brief and against a philosophy as well where the repository has one; does anything of it reach what the assessor reads beyond a stop and its question; does a held item stop the loop, other than as ADR-D-0067 states; and is a run with neither a brief nor a philosophy left ungraded?

## Revisit When

- The audit's judgements inside the loop are found to hold nothing run after run.
- A completion judgement is found catching drift that a point missed inside the loop would have caught.
- Goal runs are found stopped whole over a question the loop could have worked around.

## More Information

Replaces ADR-D-0056 in full together with ADR-D-0064, which holds who authorizes the envelope, and ADR-D-0067, which holds the remedy carried out under a brief without a stop. What this record changes from ADR-D-0056: a goal run under a brief is graded against the brief, in a repository with no philosophy too, and against the philosophy as well where there is one. Source of intent: `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md`, Limits (the goal-mode exception) and its pass condition on goal mode; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/completed/quiet-orchestrator-session-brief.md`), "Directed during the run". The design-led long runs brief states none of what this record fixes as a means: judgement inside the loop, the stop of the whole loop and the separation from the assessor's evidence are the run's own design. The stop of the whole loop departs from the means that brief states under "A better design noticed mid-flight", that the part a finding concerns waits while the rest continues. On 2026-10-05 the repository that holds the harness had no philosophy, so no goal run there had exercised the audit's attachment; on 2026-11-07 no goal run under a brief had run, so the audit's grading of one had not been exercised. Related: ADR-D-0052 (the value audit), ADR-D-0029 (the assessor), ADR-D-0050 (the Auditor), ADR-D-0066 (the envelope), ADR-D-0067 (a determined remedy carried out without a stop under a brief), ADR-D-0074 (the stall rule), ADR-D-0075 (completion and merge), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0064 (who authorizes non-trivial work), ADR-D-0065 (when a ratified brief authorizes a plan or a goal envelope). Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
