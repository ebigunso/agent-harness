# Readings: Process principles in the plugin

Written by the Orchestrator for the value audit to compare after its grades are fixed. Not read by an auditor before grading.

## Readings

### `process-principles-in-the-plugin-plan.md`, plan draft

Item | reading | statement relied on

- DoD 1 (the two questions at plan review, once, the Plan Gate pointing) | covered | brief, first principle; means: "tightens the existing text rather than adding a second statement"
- DoD 2 (three-way reading; never absorbed; the guard: review and audit of the revised plan before any is built) | covered | brief, second principle and its two sub-statements
- DoD 3 (reports: left out, not verified, scoped down out loud) | covered | brief, third principle
- DoD 4 (evidence named by the closing review; kept only with the case made; regression tests are not evidence) | covered | brief, fourth principle; scenario 4
- DoD 5 (additions carry their reason, widening the suppressions line) | covered | brief, fifth principle
- DoD 6 (no new code norm; existing ones left and named) | covered | brief, Limits, first constraint; "no new text states a code norm"
- DoD 7 (ADR-D-0033 replaced and retired; ADR-D-0041 revised; each accepted by name) | covered | brief, pass condition on the record on discoveries
- DoD 8 (the repository's text wins, stated once in Precedence) | covered | brief, Limits, third constraint
- DoD 9, 10 (validators; review; the run reported ready) | covered as mechanics
- Planner-added 1 (without a brief the gate is the user's approval or waiver; the discoveries record's pause cases widen) | extends | brief: "goes back through the same gate that admitted it"
- Planner-added 2 (a revision audited at plan draft on the whole plan) | extends | brief: "the value audit on the plan as it now stands, graded as a whole"
- Non-goals (code norms; porting mechanism; adapters' output format; template; fixture) | covered | brief, Limits and Left out on purpose; pass conditions agent-checkable on the text
- Design (tighten one statement per principle; records revised in place) | covered | brief, means: tighten rather than add
- A1 (smaller design as outcome, not target) | covered | brief: "when the questions pull a draft toward a smaller design, the smaller design is the right one"; Limits
- A2 (ADR-D-0053's experience test kept beside the design-change reading) | extends | brief, second principle: "how it sits under the repository's philosophies"
- Task_1 to Task_3 | covered, as the Definition of Done items they carry
- Decision Log 1 | as Planner-added 1 and 2
- Decision Log 2 (review applied; the hand-over condition unresolved and asked) | covered as mechanics; the hand-over question is the owner's
- Scenarios, the Orchestrator's expectation only: all four not yet; no fixture is run; his next real run shows them.

#### The audit's comparison, plan draft (2026-10-08), as returned

- `Reading compared:` DoD 1 agrees; DoD 2 agrees; DoD 3 agrees; DoD 4 agrees; DoD 5 agrees; DoD 6 diverges (Orchestrator: covered by Limits constraint 1 and "no new text states a code norm"; auditor: inferred with direction, since the brief addresses new text only and keeping existing code norms against the stated neutrality is an extension); DoD 7 agrees; DoD 8 agrees; DoD 9 agrees; DoD 10 agrees (Orchestrator "covered as mechanics", auditor cited on the standing approval); Planner-added 1 agrees; Planner-added 2 diverges (Orchestrator: extends; auditor: cited, the means names the audit of the plan as it now stands and the position is how); Non-goals: code norms agrees, porting mechanism agrees, adapters' output format agrees, fixture agrees, template diverges (Orchestrator: covered; auditor: inferred, no brief statement names the template); Design agrees; A1 agrees; A2 agrees; Task_1 agrees; Task_2 agrees; Task_3 agrees; Decision Log 1 agrees; Decision Log 2a agrees; 2b agrees; 2c agrees; 2d diverges (Orchestrator: covered as mechanics; auditor: inferred); 2e agrees; 2f agrees.
- `Findings compared: none found` (the readings file records no finding; the one departure from a means-adjacent wording noted on DoD 7, replacement in place of "revised", changes nothing anyone experiences from the feature: agrees, cited)

Readings corrected after this comparison: keeping the existing code norms extends the brief, which speaks of new text; publication rests on the standing approval; the plan-draft position for a revision is what the means names; the template non-goal and the stance's reader list extend the brief.

## Findings

- None yet.
