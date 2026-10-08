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

# ADR-D-0051: Work under a ratified brief is a run of one or more units, plans or small changes; each unit is authorized on its own as its kind is and closes without being reported as ready; a run reported as ready stays open for the judgement of the person directing the work and takes the changes that person directs against its brief; the run closes once, when that person's acceptance of its stack reaches the session

Revision of 2026-10-08 awaiting acceptance by name: the reason the rejected alternative "one plan extended by replans until the design is carried" lost. Until ebigunso accepts the revised record by name, the terms accepted on 2026-10-06 stand.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

A ratified brief can authorize a plan without the person directing the work reading it (ADR-D-0041), or a small change that person stated in it without a plan (ADR-D-0055), and the closeout reports the result as ready for that person's judgement (ADR-D-0042). A design held in a brief is often larger than one plan can carry: its shape is found as the work goes. When the unit that closes is the plan, the work ends after the first plan and that person is called to judge a part, or has to hand the rest over again. Once the result is reported as ready, that person, judging it, may direct a change against the same brief before accepting it. The fork is what a brief governs and what closes: each unit, the work up to its report as ready, or the work up to that person's acceptance of it.

## Decision

- What a ratified brief governs is a run: one or more units of work, each a plan-mode plan or a small change as ADR-D-0055 states, taken one after another as the work shows what the next has to be.
- Each unit of a run is authorized on its own: a plan exactly as ADR-D-0040 and ADR-D-0041 state, a small change as ADR-D-0055 states; nothing about being inside a run authorizes a unit.
- A unit of a run closes with its own checks and is not reported as ready for judgement; the run continues into its next unit without the person directing the work.
- When the run's last unit has closed, the result is reported as ready for that person's judgement, the note sent to Counsel, and the reviewed branches published where a standing approval covers that.
- A run so reported stays open for that person's judgement. A change that person directs against the run's brief while it is open is work of the run: built on the run's stack as a small change (ADR-D-0055) or as a plan where the Orchestrator chooses one, authorized as its kind is, reviewed and audited at its close, and logged in the run record; when it is done, the run is reported as ready again.
- The run closes once: when that person's acceptance of its stack reaches the session.
- A small change stated against a brief whose run is already accepted and merged starts a run of its own, of that one small change, which closes once like any run.
- A run's report as ready leads with behaviour, one scenario of the brief at a time, with how to observe each; a scenario only that person can judge is reported as ready for judgement and never as met.
- What a brief gives does not depend on how many units the work takes: a run of one unit is a run.
- A run keeps a run record beside its units: the brief's scenarios and any the run added, each with the state the last audit gave it, and each unit, each change directed while the run was open included, with what its closing audit found. The record holds only what audits stated.
- Between units the person directing the work is reached only by what already reaches that person during a unit: an item the audit holds, a question the Orchestrator escalates, or Counsel's pause.

## Why

Someone who hands over a design wants to come back to it built, not to a first part and a request to continue: being called at each unit boundary would have that person steering the work unit by unit, which the brief exists to end. The check that lets a unit start without that person is made per unit and stays per unit, so a longer run adds no authority; it only moves the moment of judgement to where there is a whole to judge. A change that person directs on judging that whole corrects the work the run did, under the same brief, so it is done as part of the run and on its stack, and the run is finished only when that person accepts what it built.

## Rejected Alternatives

- Each plan closes as ready for judgement, as a single plan does: it lost because the person directing the work would be asked to judge parts and to restart the work after each, when the design is judged by scenarios that only the whole shows; reopen if runs are found to reach closeout with results that person would have stopped at an earlier plan.
- One plan extended by replans until the design is carried: it lost because the plan every audit re-reads would grow without bound; reopen if drafting a new plan for each step is found to cost more than the bounded, separately reviewed unit it buys (a revision now gets its own review too, so the review alone is not what a new plan buys).
- The run authorized once, its later units starting on the first unit's authorization: rejected outright; a verdict covers the unit it graded (ADR-D-0041, ADR-D-0055), and later units decide things no audit has seen.
- Extending goal mode to designs a person judges: it lost because it gives one loop two kinds of end and changes how goal mode admits work; reopen if runs under a brief are found to need goal mode's per-iteration checks.
- The run closes when it is reported as ready, and a change directed after that, or a small change, is a new run or stands outside any run: it lost because the brief would then govern something other than its run, and the change would be parted from the work it corrects; reopen if changes directed while a run is open are found not to correct the work the run did but to start work its brief did not ask for.

## Decision Boundary

Invariant: a brief governs a run of one or more units, plans or small changes; each unit is authorized on its own as its kind is and closes without being reported as ready; the run is reported as ready scenario by scenario, with human-only scenarios reported as ready for judgement and never as met, and stays open for that judgement; a change directed against its brief while it is open is work of the run, on its stack, after which the run is reported as ready again; the run closes once, when the acceptance of its stack by the person directing the work reaches the session; the run record holds only what audits stated; the Decision list states the rest.

Not covered: the conditions for authorizing a plan (ADR-D-0041) and a small change (ADR-D-0055); what a run's closeout shows of the extensions the audit let through (ADR-D-0042); when a run stops without finishing because it has stopped getting closer, which the workflow text states; what the Orchestrator writes for the audit to compare, and where (ADR-D-0052); design-level findings during a run (ADR-D-0053); how the word of the person directing the work reaches the session (ADR-D-0038); merge authorization; a change directed against a brief whose run is accepted and not yet merged; the form of the run record and of the report; goal mode; work with no brief.

## Validation

- A run's record lists each unit with the dispatch and verdict that authorized it or, for a small change, its state, the dispatch and verdict that closed it being in the run's changes file, and shows each report as ready for judgement only after every unit before it has closed.
- No unit of a run starts on another unit's verdict.
- A change directed while a run is open appears in that run's record, its review and closing audit in its plan or, for a small change, the run's changes file, followed by a report as ready again; the run is closed only once the acceptance of its stack has reached the session.
- A report as ready names each scenario of the brief with its state and how to observe it, and reports no human-only scenario as met.

## Revisit When

- Runs are found to reach closeout with results the person directing the work would have stopped at an earlier plan.
- Units inside a run are found starting without the checks their kind requires.
- On 2026-10-04 one run had been carried over more than one plan, by hand, before this text existed; a run in which the person directing the work had to be called between units for something other than a held item, an escalated question or a pause reopens this record.
- Changes directed while a run is open are found not to correct the work the run did but to start work its brief did not ask for.

## More Information

Source of intent: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`, "The run" and "Closeout"; `docs/coding-agent/briefs/active/small-change-from-his-word-brief.md`, "A small change and the run". Of what this record fixes, the first brief states one thing as a means: that a scenario only the person directing the work can judge ends as ready for that person's judgement. The run record is the run's own addition. Related: ADR-D-0040 and ADR-D-0041 (authorization), ADR-D-0055 (a small change), ADR-D-0042 (closeout), ADR-D-0038 (the word of the person directing the work), ADR-D-0044 (Counsel's pause), ADR-D-0045 (what reaches Counsel during a run).
