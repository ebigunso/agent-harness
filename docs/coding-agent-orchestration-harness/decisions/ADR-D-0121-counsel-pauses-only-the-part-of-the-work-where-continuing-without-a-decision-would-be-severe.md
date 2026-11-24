---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0044-counsel-pauses-the-affected-part-of-the-work-where-continuing-without-a-decision-would-be-severe.md"]
superseded_by: null
---

# ADR-D-0121: Where continuing without the decision of the person directing the work would be severe, Counsel pauses the part of the work concerned, and the Orchestrator session holds it without judging the pause

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. A pause is a stop of part of a run's work that Counsel issues on its own account.

Counsel's advice on direction goes to the person directing the work (ADR-D-0103), and Counsel tells an Orchestrator session nothing about how the work is done (ADR-D-0102). So between Counsel raising a matter and that person answering, the run goes on. For most matters that is what is wanted: what is done meanwhile can be redone, and a run that waited on every matter would return that person to being asked before anything proceeds. It fails where what is done meanwhile cannot be taken back, reaches outside the work, or builds further on a direction Counsel believes conflicts with what that person has said. The fork is whether anything Counsel says on its own account can stop work, how much of it, and whether the Orchestrator session may decline.

## Decision

- What continuing without that person's decision would cost decides what Counsel does with a matter it raises, and whether the matter stops work.
- Where what would be done meanwhile is easily undone and nothing builds on it, Counsel raises the matter at that person's next contact, and the work continues.
- Where continuing would cost some rework if that person decides otherwise, Counsel raises the matter with that person at once and tells the Orchestrator session only that a question on that matter is with that person. The work continues.
- Continuing is severe where what would be done meanwhile cannot be undone, reaches outside the work, or builds further on a direction Counsel believes conflicts with what that person has said. There Counsel raises the matter with that person at once and pauses the part of the work the matter concerns.
- A pause is narrow. It stops only the part the matter concerns, it carries the reason continuing would be severe, and it says nothing of what is to be done instead. It is never stretched to further work: stopping more takes a new pause with a reason of its own.
- The Orchestrator session holds the paused part and does not judge whether the pause is warranted. What else in the run depends on that part is the Orchestrator's to determine, and the rest of the run goes on.
- A pause lasts until that person answers or Counsel withdraws it. Counsel may withdraw its own pause when it finds the reason no longer holds, and says why. Having withdrawn a pause does not bar Counsel from pausing again for the same reason.
- Counsel raises the matter with that person at the same moment it pauses, and tells that person of every withdrawal, so that person sees every use and every withdrawal.
- A pause is no decision of that person and uses none of that person's authority: it defers the paused part to that person's decision. The Orchestrator session follows it as a rule of the run, not as that person's word. The cost accepted with this is that a pause which did not come from Counsel, or one Counsel did not raise with that person, holds the part it names until that person notices; the Orchestrator session's own report of every pause to that person bounds that.

## Why

A stop is different from a direction: waiting costs time and can be made up, while what cannot be undone, and work built on a direction that turns out wrong, cannot, which is where the product philosophy's "The line" has work wait for the person's yes and its "What goes wrong, in order" has a question asked whatever it interrupts. The party whose work waits cannot be the judge of whether it should wait, so the pause binds; and it is kept to the part concerned, and to the time until that person answers or Counsel finds its reason gone, so that it cannot become a way of steering the run.

## Rejected Alternatives

- No pause; Counsel raises every matter with that person and the work goes on meanwhile: it lost because work that cannot be undone or reaches outside, and work building on a direction that conflicts with what that person has said, cannot be cheaply put right when the answer comes; reopen if pauses are found to have stopped work that person then let continue unchanged, often enough to cost more than the rework they prevented.
- The pause is advisory and the Orchestrator session decides whether to honour it: rejected outright; the party whose work waits would judge whether it should wait.
- A pause stops the whole run: it lost because only the part concerned is at risk, and the rest of the run is not what the matter is about; reopen if the Orchestrator's determination of what depends on a paused part is found to let dependent work continue.
- Only that person can end a pause, a mistaken one included: it lost because a false alarm would then hold work until that person is next reachable, for a reason nobody still holds; reopen if withdrawals are found to have released work that person would have kept paused.
- A withdrawn pause may not be raised again for the same reason without that person: it lost because it restricts Counsel's judgement to close a gap that that person's sight of every pause and withdrawal already closes; reopen if pauses are found raised and withdrawn repeatedly on one matter.
- Every matter Counsel raises pauses the work: it lost because most matters are cheaply undone, and stopping on them returns that person to being asked before anything proceeds; reopen if matters that did not pause the work are found to have cost more rework than a pause would have.

## Decision Boundary

Not covered: when that person is told of anything else that needs them (ADR-D-0116); what else Counsel may say to an Orchestrator session and where its advice goes (ADR-D-0097, ADR-D-0100, ADR-D-0102, ADR-D-0103); how a matter comes to Counsel's notice while a run is under way (ADR-D-0122); what the value audit holds, which is a separate stop (ADR-D-0052); when that person's answer counts as that person's word (ADR-D-0112); the names given to degrees of severity; the wording of a pause, how it travels between sessions, that it needs no admitting as a relay of that person's words does, and where a pause and its end are written down, all of which the plugin's text states.

## Validation

The decision is broken where:

- work was paused on Counsel's word where continuing would not have been severe, or a matter short of severe held work up;
- a matter that would cost some rework if that person decides otherwise was not raised with that person at once, or the Orchestrator session was not told that a question on that matter is with that person, or was told more than that;
- a matter easily undone, with nothing building on it, stopped work or was not raised at that person's next contact;
- a pause stopped more than the part its matter concerns, came without its reason, said what to do instead, or was stretched to further work;
- an Orchestrator session went on with a paused part before that person answered or Counsel withdrew the pause, or weighed whether to honour it;
- a pause was in force, or was withdrawn, without that person having been told;
- a pause was acted on as that person's decision.

## Revisit When

- Pauses are found to have stopped work that the person directing the work then let continue unchanged, often enough to cost more than the rework they prevented.
- A pause is found to have named more than the part concerned, or a series of pauses to have ordered the run.
- A pause is found to have held work without the matter having reached the person directing the work.
- On 2026-10-02 no pause had been issued on any runtime; a pause the Orchestrator session did not honour reopens this record.

## More Information

Replaces ADR-D-0044 in full. ADR-D-0044 stated what Counsel does with a matter as three named levels of severity; this record states the same three by what continuing would cost and carries no names for them. Related: ADR-D-0116 (when that person is told of what needs them); ADR-D-0102, whose one exception this record is; ADR-D-0103 (where Counsel's advice goes); ADR-D-0052 (what the value audit holds); ADR-D-0112 (that person's word). Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions".
