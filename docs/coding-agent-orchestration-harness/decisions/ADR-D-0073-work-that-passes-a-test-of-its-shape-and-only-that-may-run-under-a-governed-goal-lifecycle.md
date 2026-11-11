---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0009-goal-mode-as-second-operating-mode.md"]
superseded_by: null
---

# ADR-D-0073: Work that passes a test of its shape, and only that, may run under a governed goal lifecycle

## Context and Problem Statement

Terms used here: search-shaped work is work whose end state can be checked objectively and whose task structure is not known when it starts, so that it proceeds by attempting, measuring and revising. A goal engine is a platform's loop that keeps an agent working until a stated condition is met. The substrate is what the harness applies to all work: its roles, its validation and evidence-integrity rules, its capture of lessons and its skills. Plan mode is the lifecycle in which a person approves the work's structure before it is executed. Goal mode is the lifecycle this record decides.

Coding-agent platforms ship goal engines (on 2026-07-16: `/goal` in Claude Code and Codex CLI, Autopilot in GitHub Copilot CLI) and no governance for the decisions those loops take away from people. Plan mode assumes that work can be decomposed before it is executed, and protects that with a person's gate at each decision. Search-shaped work does not fit the assumption: put through plan mode it produces stale plans and repeated requests for permission, and run on a bare goal engine it is autonomy nobody governs. The fork is whether the harness leaves such work to one of those two, or gives it a governed lifecycle of its own.

## Decision

- Work that passes a test of its shape, and only that, may run in goal mode, a lifecycle in which the goal is held fixed and the work's structure is discovered by attempting, observing and revising.
- A person's oversight of that work is relocated, never removed: it moves from a gate before each decision to structure around the loop, before it starts, while it runs and after it ends. While the loop runs, its work stays recorded and cheap to undo, which is what makes review after the work sufficient.
- The test is of the work's shape, never of preference: its end state can be checked objectively, its structure cannot be known before it starts, and every irreversible or outward-facing action can be kept out of the loop. Where the test is in doubt, the work is planned. The test is applied as a gate before the work starts.
- Goal mode and plan mode run on the one substrate. Goal mode changes the lifecycle around the substrate and nothing in it.

## Why

A structure that cannot be known in advance cannot be approved in advance, so holding such work to plan mode forfeits it, and a platform's goal engine as shipped hands an agent the decisions with nothing in place of the person's gates; the governance is the part the platforms do not ship. Admission by a test of shape keeps goal mode from becoming a way around planning for work that can be planned, and one substrate under both lifecycles keeps the harness from forking into two.

## Rejected Alternatives

- Goal engines used only to speed up the execution of approved plans, with no lifecycle added: it lost because it forfeits long-horizon work whose structure cannot be approved beforehand; reopen if trial evidence shows that goal mode's governance fails to contain scope drift or compounding error.
- Goal engines adopted as the platforms ship them, with no harness governance: it lost because it delegates decisions to agents and relocates a person's oversight nowhere; reopen if platform goal engines gain governance of their own that overlaps or conflicts with the harness's.

## Decision Boundary

Invariant: a governed goal lifecycle exists for work that passes the test of its shape; work enters it only by that test and is planned where the test is in doubt; a person's oversight is relocated to structure around the loop and never removed; the loop's work stays recorded and cheap to undo; both lifecycles run on one substrate.

Not covered: the mechanisms that carry the rest of the oversight, each left to a record of its own: what bounds the loop (ADR-D-0066), who assesses it (ADR-D-0029, ADR-D-0050), and what stands between its completion and a merge (ADR-D-0075); that the loop's work stays recorded and cheap to undo is carried here, and the form of the record and the means of undoing are goal mode's text; the wording of the test and the point in a session at which it is applied; who authorizes a goal run; which goal engine runs the loop.

## Validation

- Review of the guidance asks: is the test of shape applied as a gate before the work starts, and is work that could have been planned and was run toward a goal recorded as misuse?
- Review of an edit to goal mode's guidance asks: does it refer to the substrate's validation, evidence and role rules, and redefine none of them?

## Revisit When

- The premise that goal mode's governance contains scope drift and compounding error no longer holds. It was held when the decision was taken on 2026-07-16; the record of that date reports no trial. Trial evidence that the governance fails to contain either reopens the record.
- The premise that platform goal engines carry no governance of their own no longer holds. It was held on 2026-07-16 of `/goal` in Claude Code and Codex CLI and of Autopilot in GitHub Copilot CLI.
- The premise that the test of shape routes real work to the lifecycle that fits it no longer holds. The record of 2026-07-16 reports no trial; a test shown too coarse to route real work correctly reopens the record.

## More Information

Replaces ADR-D-0009 in full. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`. Related: ADR-D-0066 (the loop's envelope), ADR-D-0029 and ADR-D-0050 (its assessment), ADR-D-0075 (what stands before a merge).
