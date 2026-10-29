---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0056-a-goal-mode-run-in-a-repository-with-a-philosophy-is-graded-by-the-value-audit-beside-the-assessor.md"]
superseded_by: null
depends_on: ["ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0029-the-optimizer-never-judges-its-own-continuation.md", "ADR-D-0050-independent-judgement-of-the-orchestrators-work-is-held-by-a-role-of-its-own-the-auditor.md", "ADR-D-0027-the-forbidden-set-is-a-criterion-ratified-before-the-loop.md", "ADR-D-0062-under-a-ratified-brief-the-orchestrator-session-asks-the-person-directing-the-work-nothing-and-presents-no-plan.md", "ADR-D-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md"]
---

# ADR-D-0063: A goal-mode run in a repository that has a philosophy is graded by the value audit, as its own dispatch beside the assessor, at the envelope, at each assessment and at the completion report; an item it holds stops the loop, and nothing of the audit enters the assessor's evidence

Proposed on 2026-10-29 to replace ADR-D-0056; awaiting acceptance by the person directing the work, by name.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work. A philosophy is a product philosophy or an engineering philosophy the repository's rules point to. The assessor is the fresh-context Auditor dispatch that judges whether a goal loop continues (ADR-D-0029, ADR-D-0050).

The value audit grades a plan-mode run against the value documents (ADR-D-0052), and that record leaves goal mode out. A goal-mode loop runs between human touchpoints inside an envelope ratified before it starts (ADR-D-0027), and its assessor judges continuation from the goal file, the journal and the gap history alone (ADR-D-0029). Nothing in a goal run is graded against a philosophy, so in a repository that has one, the loop's drift from the values of the person directing the work shows only when the work is built. Goal mode for goals a check can decide keeps working as it did, with that one exception. Work handed over through a ratified brief may turn out to be search-shaped and run in goal mode, while the person directing the work is reached only through Counsel (ADR-D-0062). The fork is where the value audit attaches to a goal loop, what an item it holds does to the loop, how it is kept from changing what the assessor reads, and how the envelope it grades is ratified under a brief.

## Decision

- In a repository that has a philosophy, a goal-mode run is graded by the value audit as ADR-D-0052 states it: its own dispatch to the Auditor on its own mandate and fixed template, beside the assessor and never folded into it.
- The audit grades at three moments: the envelope, before the person directing the work ratifies it; each event on which the assessor is due; and the completion report, where it grades the whole range of the run.
- An item the audit holds stops the loop, as goal mode's own stop for a question does, until the decision is given.
- Nothing the audit returns and nothing the Orchestrator writes for it enters the goal file, the journal or the gap history beyond the stop and the question put to the person directing the work. The assessor's evidence, its mandate and its fixed dispatch template are unchanged.
- Goal mode's admission test, stall rule and completion rule are unchanged.
- The envelope is ratified by the person directing the work before the loop starts: in the Orchestrator session or, under a ratified brief, by that person's answer relayed through Counsel agreeing to the goal and its limits, as ADR-D-0062 states for every question under a brief. No brief stands in for that ratification.
- A goal-mode run in a repository with no philosophy is not graded by the value audit, under a brief or not.

## Why

The person directing the work asked that a goal-mode run in a repository with a philosophy be kept to that person's values as it goes, and the assessor's cadence is the only rhythm goal mode has that is not a fixed count, so the audit takes it. A goal loop is one optimizer with no separable parts to hold, so a held item stops the whole loop; adding a stop tightens, which the brief leaves free. The goal file, the journal and the gap history are the assessor's evidence, and its inputs must not change, so the audit's material is kept out of them. Under a brief the envelope's ratification travels through Counsel because that person should not need to look at the Orchestrator session for it, and it is still that person's agreement, not the brief, that starts the loop.

## Rejected Alternatives

- Two audits only, the envelope before ratification and the result at the completion report: it lost because it keeps the run to the values of the person directing the work only at the two ends, and drift during the loop shows only when the work is built; reopen if the audits on the assessor's events are found to hold nothing run after run.
- A journal line for each value audit, and a count of them checked before merge: rejected outright; it puts audit material into the journal, which is the assessor's evidence.
- The audit's cadence verified before merge from outside the journal: it lost because the audit at the completion report grades the whole range, so a position missed inside the loop is still graded before anything merges; reopen if a completion audit is found grading drift that a skipped position inside the loop would have caught.
- The part a held item concerns waits and the rest of the loop continues, as in a run under a brief: it lost because a goal loop is one optimizer with no parts to set aside; reopen if goal runs are found stopped whole over a question the loop could have worked around.
- One dispatch carrying both the assessor's mandate and the audit's: rejected outright; it changes the assessor's inputs and its fixed template, which ADR-D-0050 and the brief's limit on goal mode keep.

## Decision Boundary

Invariant: in a repository that has a philosophy, the value audit grades a goal run as its own dispatch at the envelope before ratification, at each assessment event and at the completion report; an item it holds stops the loop; nothing of the audit enters the goal file, the journal or the gap history beyond the stop and the question; the assessor, the admission test, the stall rule and the completion rule are unchanged; the envelope is ratified by the person directing the work, under a brief through Counsel, and never by the brief; the Decision list states the rest.

Not covered: the grades, what they hold and the comparison with the Orchestrator's reading (ADR-D-0052 and the audit's mandate); how the fixed template's fill-ins read for a goal run, which the mandate states; where the verdicts and the Orchestrator's readings are kept, and their form; the assessor's cadence schedule, which the goal-mode reference owns; who may authorize an envelope (ADR-D-0064); how a held item's question and the envelope travel to the person directing the work and how the answer is admitted (ADR-D-0038, ADR-D-0062); the hold on a change that loosens a stop, a pass condition or who decides inside a goal loop, which the goal-mode reference carries; the completion report's sections and the check before merge (ADR-D-0031), which are unchanged.

## Validation

- The assessor's mandate, its fixed dispatch template and the goal-condition checklist are unchanged by the audit's attachment to the loop.
- No goal file, journal or gap history shows a grade, a verdict, a reading or any other record of the audit; a journal shows a value hold only as its stop and the question.
- A goal run in a repository that has a philosophy shows a value audit dispatched by its fixed template at the envelope before ratification, at each assessment event and at the completion report.
- A goal run in a repository with no philosophy shows no value audit.
- A goal run under a brief records the envelope's ratification as the relay quoting the person directing the work, or that person's own statement in the session, before its first iteration.

## Revisit When

- The audits on the assessor's events are found to hold nothing run after run.
- A completion audit is found grading drift that a skipped position inside the loop would have caught.
- Goal runs are found stopped whole over a question the loop could have worked around.
- On 2026-10-29 no goal run under a brief had been made on any runtime; a goal run under a brief in which the person directing the work had to look at the Orchestrator session to ratify its envelope or answer one of its stops reopens this record.

## More Information

Replaces ADR-D-0056 in full: everything it decided is carried, and under a ratified brief the envelope is ratified by the answer of the person directing the work relayed through Counsel. Source of intent: `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md`, Limits (the goal-mode exception) and its pass condition on goal mode; the brief "A quiet Orchestrator session under a brief" (`quiet-orchestrator-session-brief.md`), "Directed during the run". The first brief states none of what this record fixes as a means: the three moments, the stop of the whole loop and the separation from the assessor's evidence are the run's own design. The stop of the whole loop departs from the means that brief states under "A better design noticed mid-flight", that the part a finding concerns waits while the rest continues. Related: ADR-D-0052 (the value audit), ADR-D-0029 (the assessor), ADR-D-0050 (the Auditor and its fixed templates), ADR-D-0027 (the envelope), ADR-D-0028 (the stall rule), ADR-D-0031 (completion and merge), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0064 (the sources of authorization). On 2026-10-05 the repository that holds the harness has no philosophy, so no goal run there has exercised the audit's attachment. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
