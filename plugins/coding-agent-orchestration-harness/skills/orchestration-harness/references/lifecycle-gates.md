# Lifecycle Gates

Use this reference for plan, research, execution, replan, and closeout lifecycle details.

## Primary Sources

At the start of non-trivial work, read:

1. `docs/coding-agent/rules/index.md`
2. `docs/coding-agent/rules/common.md`
3. `docs/coding-agent/rules/orchestrator.md`
4. Any repository reference documents listed in `common.md`
5. `docs/coding-agent/lessons.md`, if present
6. Relevant plans under `docs/coding-agent/plans/active/` and `docs/coding-agent/plans/completed/`
7. Relevant project files after the Research Dispatch Gate is satisfied

If `docs/coding-agent/rules/` does not exist, create the minimal repo-rule skeleton from the Rulebook templates. Do not add global migration placeholders to role rule files. If `docs/coding-agent/plans/active/` does not exist, create it before writing draft or in-progress plans.

## Plan Gate Details

Trivial/non-trivial criteria, requirement challenge, plan and approval requirements, and lifecycle selection: `SKILL.md` Plan Gate (canonical).

Follow-up non-trivial work re-enters the Plan Gate (`SKILL.md`): chain it through a new or updated plan, never by extending the approved scope in place.

Clarifications, follow-up requirements, and plan refinements are NOT plan approval. Execution requires an explicit approval or a direct execution instruction from the user; when in doubt, ask.

Plan review loop: the Orchestrator triages each Reviewer finding as fix, research-and-rewrite, or dispute; re-review scopes to the delta only when the delta re-review condition in `skills/wave-integration/references/integration-checklist.md` holds, otherwise it is full; a third round on the same seam applies that file's third-bounce detector; a finding that needs a ruling follows Escalation Ruling below.

## Research Dispatch Details

Gate: `SKILL.md` Research Dispatch Gate.

1. The Orchestrator may read repository files and run searches to decide triviality, scope, and validation; reading is not a substitute for a Researcher on unfamiliar or cross-cutting areas.
2. Dispatch one Researcher per narrow focus (see `subagent-strategy`); parallel Researchers for complex or high-ambiguity work.
3. When non-trivial work proceeds without a Researcher, record `Research waived: <reason>` in the plan before execution; the reason names what the Orchestrator read instead.

## Replan Procedure

Triggers: `SKILL.md` Replan Triggers.

1. Record the insight, its impact, and the plan delta (tasks, waves, validation) in the plan Decision Log.
2. Surface it in the next report or wave integration.
3. Pause for user confirmation only when the change is contract-shape (Escalation Ruling below), irreversible, or outward-facing: stop dispatching further Workers, ask at most three questions, and continue only after confirmation.

## Escalation Ruling

Use this procedure when a Worker or Reviewer escalation asks for a ruling rather than a fact.

Two-tier threshold:

- Routine escalations (missing input, ambiguous acceptance, local sequencing) may be answered at coordination tempo.
- Contract-shape escalations — anything that would change a schema, interface, boundary, invariant, or other owned contract — require a deliberate design decision, never a quick coordination answer.

For contract-shape rulings:

1. Enumerate the blast radius before ruling: every consumer across repos, serialization surfaces, deferred scopes, and owned contracts the ruling touches.
2. If self-verification cannot cover that radius, dispatch a Researcher first and rule only on its evidence.
3. Delivering the ruling and recording it in the plan Decision Log are one action — never send the answer without the log entry.

When recording a ruling, check the ADR warrant criteria in `skills/durable-docs-authoring/references/adr.md`; if they are met, propose an ADR per that reference before the affected work closes.

## Plan Lifecycle

- Draft and execute under `docs/coding-agent/plans/active/`; create the directory if missing.
- Append Progress Log entries after each Worker wave, Reviewer gate, and closeout decision.
- Append Decision Log entries for replans, waivers, or material assumptions.
- When finished and validated, set status to `done` and move the plan to `docs/coding-agent/plans/completed/`.

## Decomposition Harmonization

Before dispatching Reviewer for final review, run one harmonization pass when a plan mixes abstraction levels, such as architecture-level tasks alongside file-level edit tasks.

Confirm:

- task granularity is coherent;
- dependencies still make sense;
- names and boundaries are consistent;
- validation ownership remains explicit;
- each acceptance criterion remains satisfiable within `owns`.
