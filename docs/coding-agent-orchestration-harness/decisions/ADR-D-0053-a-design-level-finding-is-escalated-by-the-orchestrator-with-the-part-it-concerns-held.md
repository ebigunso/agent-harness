---
status: accepted
adr_type: design
date: 2026-10-04
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0045-during-a-run-counsel-hears-from-the-audit-only-of-an-item-let-through-on-a-provisional-statement.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md"]
---

# ADR-D-0053: A finding during a run that bears on the design is escalated by the Orchestrator as a value question, whatever acting on it would cost, with the part it concerns held and the rest continuing; every finding is recorded with the Orchestrator's reading, and the audit compares that reading

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

During a run the Orchestrator and its Workers notice things: a better way to give what the design asks for, a part of the design that will not work as stated, a cheaper route. Some bear on the design, which is the experience someone gains from the feature; most do not. An extension the value audit lets through is shown at closeout (ADR-D-0042), and during a run Counsel hears from the audit by exception only (ADR-D-0045). Neither brings a better design to the person directing the work while there is still time to take it, and the cheap-to-undo test that lets extensions through measures the wrong thing here: an expensive change can be the better design, and a cheap one can be trivial. The fork is what happens to a finding that bears on the design: who decides that it does, when it reaches that person, and what the run does meanwhile.

## Decision

- Anything noticed during a run that suggests a better design exists is recorded as a finding, with the Orchestrator's reading of it: it bears on the design, or it is trivial.
- A finding bears on the design when acting on it would change what someone experiences from the feature. What acting on it would cost is not the measure, in either direction. A departure from a means a brief states is read by the same test (ADR-D-0054).
- A finding the Orchestrator reads as bearing on the design is a question that needs the decision of the person directing the work. The Orchestrator escalates it at once as a value question, as it escalates any question that needs that person, and the escalation carries the question and not an account of the run.
- While that person decides, the Orchestrator holds the part of the work the finding concerns, and the rest of the run continues.
- A finding read as trivial is not escalated as a design-level question, however cheap acting on it would be; it stays in the record. This changes nothing about what else may carry it: a judgement call or extension that bears on direction is still marked by the audit and shown at closeout (ADR-D-0042), and what the audit reports to Counsel during a run is still reported (ADR-D-0045), whatever reading the finding has.
- The Orchestrator's readings of the findings are kept with what it writes for comparison (ADR-D-0052). At its next position the value audit, after its grades are fixed, compares the reading of every recorded finding and names each one read as trivial that bears on the design. The Orchestrator then escalates each of those the same way and holds its part. The audit also names each one read as bearing on the design that it judges trivial, so that a trivial finding is kept from the person directing the work by more than the Orchestrator's own reading. When the audit so names a finding the Orchestrator had already escalated, the Orchestrator releases the held part and withdraws the question by the carrier, unless the person directing the work has already answered, in which case the answer stands; a finding so named that has not yet been sent is not sent.
- The audit sends nothing about findings to Counsel; what Counsel hears from the audit during a run is as ADR-D-0045 states.

## Why

Someone who handed over a design wants the option of the better one kept open, including the expensive one, and does not want attention spent on a change that makes no difference to anyone: so what decides whether a finding reaches that person is whether it changes the experience, not what it costs. Holding the part concerned keeps the expensive path from growing more expensive while the decision is made. The Orchestrator reads its findings first because it is the one that notices them and can ask at once, and its reading is compared because a selection nobody checks is the Orchestrator deciding alone what that person gets to hear.

## Rejected Alternatives

- Findings are treated like other extensions: let through when cheap to undo and shown at closeout: it lost because by closeout the better design costs a rebuild, and the cheap-to-undo test would stop an expensive better design and pass a trivial one; reopen if findings escalated during runs are found to be ones that person would rather have seen only at the end.
- The audit alone selects which findings reach that person, at its fixed positions: it lost because a finding noticed inside a wave would wait for the next position while work piles onto the design it questions, and because the audit sees the work only where the workflow places it; reopen if the Orchestrator's readings are found wrong so often that the comparison does the selecting anyway.
- The Orchestrator selects and nobody compares: rejected outright; the party whose work a finding would hold decides alone whether it is raised.
- The whole run stops for a finding: it lost because only the part the finding concerns is in question; reopen if work continued outside a held part is found to have needed redoing once the decision came.
- Cost of the change decides whether a finding is raised: rejected outright; it measures the run's convenience, not the design.

## Decision Boundary

Invariant: every finding is recorded with the Orchestrator's reading; one that bears on the design is escalated at once as a value question whatever its cost, with only its part held; a trivial one is not raised as a design-level question, and what closeout shows and what Counsel hears from the audit are unchanged by a finding's reading; the audit compares every reading after its grades are fixed and names a reading it judges wrong in either direction; a finding it names as bearing on the design is escalated the same way; the Decision list states the rest.

Not covered: what the audit grades and how (ADR-D-0052 and its mandate); how a brief's kinds bear on a finding (ADR-D-0054); what Counsel hears from the audit during a run (ADR-D-0045); Counsel's pause (ADR-D-0044); how a question travels to the person directing the work and what counts as the answer (ADR-D-0038); what the Orchestrator does when a discovery inside authorized work is not a finding about the design (ADR-D-0057; what a Worker may act on alone, ADR-D-0058); where findings are written and in what form.

## Validation

- A run's records show each finding with the Orchestrator's reading, and for each one read as bearing on the design the question sent, the part held, and what released it: the answer, or the audit's naming of the finding as trivial with the question withdrawn.
- A verdict reports the comparison of findings apart from the grades, naming both each finding read as trivial that it judges bears on the design and each finding read as bearing on the design that it judges trivial; each finding it identifies as bearing on the design is escalated before the part it concerns goes further; a finding it agrees is trivial is kept and not held.
- No finding is found raised or withheld on the ground of what the change would cost.

## Revisit When

- Findings escalated during runs are found to be ones the person directing the work would rather have seen only at the end.
- The audit's comparison is found naming findings the Orchestrator read as trivial, run after run.
- Findings the audit named trivial are found to be ones the person directing the work wanted to decide.
- Work continued outside a held part is found to have needed redoing once the decision came.
- On 2026-10-04 one finding had been escalated this way, by hand, before this text existed; a finding that bore on the design and reached that person only at closeout reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`, "A better design noticed mid-flight" and "What a design is". Of what this record fixes, the brief states one thing as a means: that the part a finding concerns waits while the rest of the run continues. The Orchestrator reading first and the audit comparing is the run's own design. Related: ADR-D-0042 (extensions at closeout), ADR-D-0045 (whose "questions the Orchestrator escalates, which are unchanged" this record relies on), ADR-D-0052 (the comparison), ADR-D-0057, which replaced ADR-D-0033 on this (discoveries within authorized work). Changed on 2026-10-05, before merge: the comparison of findings named only a finding read as trivial that bears on the design, and the closeout audit of `docs/coding-agent/plans/completed/run-across-plans-plan.md` named that one-sided comparison as bearing on the design, since a trivial finding is never to reach the person directing the work; the audit now names a wrong reading in both directions.
