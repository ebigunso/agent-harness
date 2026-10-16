---
status: proposed
adr_type: design
date: 2026-10-02
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md", "ADR-D-0043-counsel-speaks-to-the-orchestrator-only-in-the-words-of-the-person-directing-the-work-and-its-advice-goes-to-that-person.md"]
---

# ADR-D-0044: Where continuing without the decision of the person directing the work would be severe, Counsel pauses the affected part of the work, and the Orchestrator session holds that part until that person answers

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Counsel's advice goes to the person directing the work and never to the Orchestrator session (ADR-D-0043), so between Counsel raising a matter and that person answering, the run continues. For most matters that is right: what is done meanwhile can be redone. For some it is not: an irreversible or outward-facing step, or work piling onto a direction Counsel believes conflicts with what that person has said. The fork is whether anything Counsel says on its own account can stop work, how much, and whether the Orchestrator may decline.

## Decision

- Whether Counsel's advice stops work depends on how severe continuing without that person's decision would be:
  - low (easily undone, nothing builds on it): Counsel raises it at that person's next contact and the work continues;
  - medium (some rework if that person decides otherwise): Counsel raises it at once and tells the Orchestrator session only that a question on that matter is with that person; the work continues;
  - high (irreversible, outward-facing, or work piling onto a direction Counsel believes conflicts with what that person has said): Counsel raises it at once and pauses the affected part of the work.
- A pause names only the affected part and states the severity reason. It says nothing about what to do instead.
- The Orchestrator session holds the named part until that person's answer arrives as that person's word; it does not judge whether the pause is warranted. What else in the run depends on the paused part is the Orchestrator's to determine; the rest of the run continues.
- A pause ends only on that person's answer; Counsel neither lifts nor extends it.
- Counsel raises the matter with that person at the same moment it pauses, so that person sees every use.
- A pause exercises none of that person's authority and decides nothing for that person: it defers the affected work to that person's decision, as an item the value audit holds does, and the Orchestrator follows it as a rule of the run, not as that person's word. It needs no admission as a relay, since it carries no decision; the cost accepted is that a pause sent under Counsel's identity by another, or one Counsel did not raise with that person, holds the named part until that person notices, which the Orchestrator's own report of every pause to that person bounds.

## Why

A stop is different from a direction: waiting costs time and can be undone, while irreversible work, or work piled onto a direction that turns out wrong, cannot. So the one case where Counsel acts on the run without that person's words is the case where waiting for those words is the cheaper error. The party whose work waits cannot be the judge of whether it should wait, so the pause binds; and it is kept narrow, to the affected part and to the time until that person answers, so that it cannot become a way of steering the run.

## Rejected Alternatives

- No pause; Counsel raises every matter with that person and the work continues meanwhile: it lost because irreversible or outward-facing work, and work piling onto a direction that conflicts with what that person has said, cannot be cheaply undone when the answer comes; reopen if pauses are found to have stopped work that person then let continue unchanged, often enough to cost more than the rework they prevented.
- The pause is advisory and the Orchestrator decides whether to honour it: rejected outright; the party whose work waits would judge whether it should wait.
- A pause that stops the whole run: it lost because only the affected part is at risk; the rest of the run is not what the advice is about; reopen if the Orchestrator's determination of what depends on a paused part is found to let dependent work continue.
- Every matter Counsel raises pauses the work: it lost because most matters are cheaply undone, and stopping on them returns that person to being asked before anything proceeds; reopen if matters graded low or medium are found to have cost more rework than a pause would have.

## Decision Boundary

Invariant: Counsel pauses only where continuing would be severe, only the affected part, with a stated reason and with the matter raised to that person at the same moment; the Orchestrator session holds that part until that person answers and does not judge the pause; a pause directs nothing and is no decision of that person; the Decision list states the rest.

Not covered: what else Counsel may say to an Orchestrator session and where its advice goes (ADR-D-0043); what the value audit holds, a separate stop that is unchanged (ADR-D-0039); when that person's answer counts as that person's word (ADR-D-0038); the wording of a pause notice; how the pause travels between sessions.

## Validation

- Counsel's policy states the three severities, that a pause names only the affected part with its reason and says nothing of what to do instead, and that the matter is raised with that person at the same moment.
- The Orchestrator's run-side text states that a pause from Counsel stops the named part until that person's answer arrives as that person's word, that the Orchestrator determines what depends on it, and that a pause is not that person's decision.
- Each pause recorded in a plan shows the part paused, the severity reason as Counsel gave it, and the answer of that person that ended it.

## Revisit When

- Pauses are found to have stopped work that the person directing the work then let continue unchanged, often enough to cost more than the rework they prevented.
- A pause is found to have named more than the affected part, or a series of pauses to have ordered the run.
- A pause is found to have held work without the matter having reached the person directing the work.
- On 2026-10-02 no pause had been issued on any runtime; a pause the Orchestrator did not honour reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "Roles and sessions". ADR-D-0034 says Counsel gives no direction on how the work is done and holds none of that person's authority; the Decision above states why a pause is neither. Related: ADR-D-0043 (what Counsel says to the Orchestrator), ADR-D-0039 (the value audit's held items), ADR-D-0038 (that person's word).
