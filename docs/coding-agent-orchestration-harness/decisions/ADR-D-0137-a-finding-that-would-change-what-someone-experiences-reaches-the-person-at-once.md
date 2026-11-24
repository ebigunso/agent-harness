---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0053-a-design-level-finding-is-escalated-by-the-orchestrator-with-the-part-it-concerns-held.md"]
superseded_by: null
---

# ADR-D-0137: A finding that would change what someone experiences reaches the person directing the work at once, whatever acting on it would cost, with only the part it concerns held

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. The design is the experience someone gains from the feature. The value audit is the independent grading of a run's plan and result against the value documents, which are the brief and the philosophies.

Someone who handed over a design wants to hear of a better one while there is still time to take it, the expensive one included, and does not want attention spent on a change nobody would notice. While the work goes on, those doing it notice things: a better way to give what the design asks for, a part of the design that will not work as stated, a cheaper route. Some bear on the design and most do not. What a run decided without that person is shown when the work is reported to that person as ready for their judgement (ADR-D-0133), by which time a better design costs a rebuild; and the test that lets a run's own choices through, whether they are cheap to undo, measures the wrong thing here, since an expensive change can be the better design and a cheap one can make no difference to anyone. The fork is what happens to something noticed that bears on the design: who decides that it does, when it reaches that person, and what the run does meanwhile.

## Decision

- Anything noticed during a run that suggests a better design exists is recorded as a finding, with the Orchestrator's reading of it: it bears on the design, or it is trivial.
- A finding bears on the design when acting on it would change what someone experiences from the feature. What acting on it would cost is not the measure, in either direction: a finding is neither raised nor withheld for being cheap or expensive to act on. The test is the same for every finding, whatever it is a finding about.
- A finding the Orchestrator reads as bearing on the design is a question that needs the decision of the person directing the work. The Orchestrator escalates it at once as a value question, as it escalates any question that needs that person, and the escalation carries the question and not an account of the run.
- While that person decides, the Orchestrator holds the part of the work the finding concerns, and only that part: work the finding does not concern goes on.
- A finding read as trivial is not escalated as a question about the design, however cheap acting on it would be; it stays in the run's records.
- A finding's reading decides that and nothing else. Whatever else carries a matter is unchanged by it: a judgement call or an extension that bears on direction is marked by the audit and shown to that person as ADR-D-0133 states, and what the audit reports to Counsel during a run is reported as ADR-D-0045 states, whatever reading the finding has.
- The Orchestrator's reading does not stand unchecked. The value audit compares the reading of every recorded finding, in both directions, the next time it judges the run after the finding is recorded, and only after its own grades are fixed.
  - It names each finding read as trivial that it judges to bear on the design. The Orchestrator escalates each of those in the same way and holds its part.
  - It names each finding read as bearing on the design that it judges trivial, so that a trivial finding is kept from the person directing the work by more than the Orchestrator's own reading. The Orchestrator releases the part held for such a finding and withdraws its question, unless that person has already answered, in which case the answer stands. A finding so named whose question has not yet been sent is not sent.

## Why

The product philosophy's "What goes wrong, in order" has "If a question would prevent the wrong thing, it is asked, whatever it interrupts", and names as a failure "The person's attention, spent on what could have been settled": whether a finding changes what someone experiences is what tells the two apart, and what it costs to act on does not. Holding the part concerned keeps the expensive path from growing more expensive while the decision is made. The Orchestrator reads its findings first because it is the one that notices them and can ask at once, and its reading is compared because, in the words of the same philosophy's "What it must not be", "A builder's confidence in its own work is not evidence": a selection nobody checks is the Orchestrator deciding alone what that person gets to hear.

## Rejected Alternatives

- Findings are treated like other extensions, let through when cheap to undo and shown at closeout: it lost because by closeout the better design costs a rebuild, and the cheap-to-undo test would stop an expensive better design and pass a trivial one; reopen if findings escalated during runs are found to be ones that person would rather have seen only at the end.
- The audit alone selects which findings reach that person, at the points of the run where it judges: it lost because a finding noticed between those points would wait for the next one while work piles onto the design it questions, and because the audit sees the work only where the workflow places it; reopen if the Orchestrator's readings are found wrong so often that the comparison does the selecting anyway.
- The Orchestrator selects and nobody compares: rejected outright; the party whose work a finding would hold decides alone whether it is raised.
- The whole run stops for a finding: it lost because only the part the finding concerns is in question; reopen if work continued outside a held part is found to have needed redoing once the decision came.
- Cost of the change decides whether a finding is raised: rejected outright; it measures the run's convenience, not the design.

## Decision Boundary

Not covered: that a departure from a way of doing something written in a brief is a finding, read by this record's test, and how the item that departs is judged (ADR-D-0138); what the audit grades and how, and that what the Orchestrator writes for comparison is not opened before the grades are fixed (ADR-D-0134, ADR-D-0135); what Counsel hears from the audit during a run, which is nothing about findings (ADR-D-0045, which the proposed ADR-D-0122 takes over); what is shown of a run's extensions and judgement calls when the work is reported to that person as ready for their judgement (ADR-D-0133); Counsel's pause (ADR-D-0044, which the proposed ADR-D-0121 takes over); how a question travels to the person directing the work and what counts as the answer (ADR-D-0112); what the Orchestrator does with a discovery inside authorized work that is not a finding about the design (ADR-D-0057), and what a Worker may act on alone (ADR-D-0058); how far the part a finding concerns extends in a given run, a goal loop included; the words by which a reading is written; where findings and readings are kept and in what form, at which points of a run the value audit judges it, and so which of its judgements is the next after a finding is recorded, and the route by which a question is sent and withdrawn, all of which the plugin's text states.

## Validation

The decision is broken where:

- something noticed during a run that suggested a better design was recorded nowhere, or was recorded without the Orchestrator's reading;
- a finding that would change what someone experiences reached the person directing the work only when the work was reported to that person as ready for their judgement, or the part it concerns went further before that person answered;
- a finding was raised, or withheld, on the ground of what acting on it would cost;
- more of a run was held for a finding than the part it concerns;
- a finding read as trivial was put to that person as a question about the design with no judgement of the audit behind it;
- a reading of a finding was compared by nobody, was compared in one direction only, or was before the audit while its grades were still open;
- a finding the audit judged to bear on the design was not escalated, or a part stayed held for a finding the audit named trivial and that person had not answered;
- an answer that person had already given was set aside because the audit later named the finding trivial.

## Revisit When

- Findings escalated during runs are found to be ones the person directing the work would rather have seen only at the end.
- The audit's comparison is found naming findings the Orchestrator read as trivial, run after run.
- Findings the audit named trivial are found to be ones the person directing the work wanted to decide.
- Work continued outside a held part is found to have needed redoing once the decision came.
- On 2026-10-04 one finding had been escalated this way, by hand, before this text existed; a finding that bore on the design and reached that person only at closeout reopens this record.

## More Information

Replaces ADR-D-0053 in full; accepted together with ADR-D-0138, which states that a departure from a means is a finding. ADR-D-0053's line that the audit sends nothing about findings to Counsel is held by ADR-D-0045 ("During a run Counsel hears from the value audit of one thing only"). Source of intent: `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md`, "A better design noticed mid-flight" and "What a design is". Of what this record decides, that brief states one thing as a means: that the part a finding concerns waits while the rest of the run continues. Related: ADR-D-0133 (what is shown of a run's extensions and judgement calls), ADR-D-0134 and ADR-D-0135 (the value audit and the comparison of the Orchestrator's reading), ADR-D-0057 (discoveries within authorized work), ADR-D-0082 (what a held item does to a goal loop).
