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

Before decomposing non-trivial work, challenge the requirements themselves and surface doubts to the requirement owner, regardless of who authored them.

Trivial work may skip a plan only when all are true:

- small and mechanical edit;
- clearly bounded scope;
- no meaningful behavior/design change;
- no non-obvious validation beyond a quick sanity check.

Non-trivial work requires a plan and approval when any are true, unless the user or Orchestrator explicitly waives the plan with a recorded reason and evidence:

- new behavior or feature;
- non-obvious bug fix;
- refactor or cross-cutting change;
- multiple files/components or unknown patterns;
- dependency, config, or CI implications;
- UI/UX behavior changes or visual correctness concerns.

Follow-ups after completion re-run the Plan Gate. Do not chain non-trivial work without a new or updated plan and explicit approval unless the plan is explicitly waived with a recorded reason and evidence.

Clarifications, follow-up requirements, and plan refinements are NOT plan approval. Execution requires an explicit approval or a direct execution instruction from the user; when in doubt, ask.

## Research Dispatch Details

For non-trivial requests:

1. Dispatch at least one Researcher before repository exploration outside `docs/coding-agent/**`.
2. Before Researcher returns, only read allowed planning docs, ask necessary clarifying questions, or create missing planning scaffolding.
3. Do not use repo-wide search or read implementation files outside allowed docs before Researcher returns.

Research waivers are allowed only for trivial work per the Plan Gate. Record `Research waived: <reason>` before execution. If discovery is needed to decide whether work is trivial, treat it as non-trivial and dispatch Researcher.

## Replan Procedure

Pause planned execution when a significant new insight changes scope, risk, dependencies, or approach.

Then:

1. Stop dispatching further Workers.
2. Summarize the insight and impact.
3. Propose a plan delta covering tasks, waves, and validation.
4. Ask at most three questions.
5. Continue only after user confirmation.

Record the decision in the plan Decision Log.

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
