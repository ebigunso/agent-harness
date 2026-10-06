---
status: accepted
adr_type: design
date: 2026-10-04
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0040-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md", "ADR-D-0041-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit-that-holds-nothing-above-the-run.md", "ADR-D-0042-every-extension-is-recorded-and-the-audit-marks-which-bear-on-direction-for-closeout.md"]
---

# ADR-D-0051: Work under a ratified brief is a run of one or more plans; each plan is authorized on its own as plans are, a plan closes without being reported as ready, and the run closes once, scenario by scenario

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

A ratified brief can authorize a plan without the person directing the work reading it (ADR-D-0041), and the closeout of that plan reports the result as ready for that person's judgement (ADR-D-0042). A design held in a brief is often larger than one plan can carry: its shape is found as the work goes. When the unit that closes is the plan, the work ends after the first plan and that person is called to judge a part, or has to hand the rest over again. The fork is what a brief governs and what closes: each plan, or the whole of the work the brief asks for.

## Decision

- What a ratified brief governs is a run: one or more plan-mode plans, drafted one after another as the work shows what the next has to be. A small change the person directing the work stated in the brief, built without a plan as ADR-D-0055 states, is the one exception: it is not a plan and forms no run.
- Each plan of a run is authorized on its own, exactly as ADR-D-0040 and ADR-D-0041 state; nothing about being inside a run authorizes a plan.
- A plan of a run closes with its own closeout audit and review and is not reported as ready for judgement; the run continues into its next plan without the person directing the work.
- The run closes once. Only then is the result reported as ready for that person's judgement, the note sent to Counsel, and the reviewed branches published where a standing approval covers that.
- A run's closeout leads with behaviour, one scenario of the brief at a time, with how to observe each; a scenario only that person can judge is reported as ready for judgement and never as met.
- What a brief gives does not depend on how many plans the design takes: a run of one plan is a run.
- A run keeps a run record beside its plans: the brief's scenarios and any the run added, each with the state the last audit gave it, and each plan with what its closeout audit found. The record holds only what audits stated.
- Between plans the person directing the work is reached only by what already reaches that person during a plan: an item the audit holds, a question the Orchestrator escalates, or Counsel's pause.

## Why

Someone who hands over a design wants to come back to it built, not to a first part and a request to continue: being called at each plan boundary would have that person steering the work plan by plan, which the brief exists to end. The check that lets a plan start without that person is made per plan and stays per plan, so a longer run adds no authority; it only moves the moment of judgement to where there is a whole to judge.

## Rejected Alternatives

- Each plan closes as ready for judgement, as a single plan does: it lost because the person directing the work would be asked to judge parts and to restart the work after each, when the design is judged by scenarios that only the whole shows; reopen if runs are found to reach closeout with results that person would have stopped at an earlier plan.
- One plan extended by replans until the design is carried: it lost because additions would get an audit but no fresh plan review, and the plan every audit re-reads would grow without bound; reopen if drafting a new plan for each step is found to cost more than the review it buys.
- The run authorized once, its later plans starting on the first plan's authorization: rejected outright; a verdict covers the plan it graded (ADR-D-0041), and later plans decide things no audit has seen.
- Extending goal mode to designs a person judges: it lost because it gives one loop two kinds of end and changes how goal mode admits work; reopen if runs under a brief are found to need goal mode's per-iteration checks.

## Decision Boundary

Invariant: a brief governs a run of one or more plans, a small change built without a plan (ADR-D-0055) excepted; each plan is authorized on its own through the Plan Gate; a plan closes without being reported as ready, and the run closes once, scenario by scenario, with human-only scenarios reported as ready for judgement and never as met; the run record holds only what audits stated; the Decision list states the rest.

Not covered: the conditions for authorizing a plan (ADR-D-0041); when a small change is built without one and what it keeps (ADR-D-0055); how a small change closes and is reported, which the workflow text states; what a run's closeout shows of the extensions the audit let through (ADR-D-0042); when a run stops without finishing because it has stopped getting closer, which the workflow text states; what the Orchestrator writes for the audit to compare, and where (ADR-D-0052); design-level findings during a run (ADR-D-0053); the form of the run record and of the closeout; goal mode; work with no brief.

## Validation

- A run's record lists each plan with the dispatch and verdict that authorized it, and shows one closeout reported as ready for judgement, the last.
- No plan of a run starts on another plan's verdict.
- A closeout names each scenario of the brief with its state and how to observe it, and reports no human-only scenario as met.

## Revisit When

- Runs are found to reach closeout with results the person directing the work would have stopped at an earlier plan.
- Plans inside a run are found starting without their own plan review and audit.
- On 2026-10-04 one run had been carried over more than one plan, by hand, before this text existed; a run in which the person directing the work had to be called between plans for something other than a held item, an escalated question or a pause reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`, "The run" and "Closeout". Of what this record fixes, the brief states one thing as a means: that a scenario only the person directing the work can judge ends as ready for that person's judgement. The run record is the run's own addition. Related: ADR-D-0040 and ADR-D-0041 (authorization), ADR-D-0042 (closeout), ADR-D-0044 (Counsel's pause), ADR-D-0045 (what reaches Counsel during a run).
