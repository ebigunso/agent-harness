# Dispatch Guidance

Use this reference when preparing Researcher, Worker, and Reviewer prompts.

## General Prompt Framing

Provide a short Context / Rationale section only when it materially changes decisions.

Prefer:

- source paths over pasted background;
- one objective per subagent invocation;
- explicit `owns`, acceptance, validation, and output contracts;
- concise constraints and what to ignore.

Avoid long narrative background that does not change deliverables.

## Researcher Dispatch

Researcher is research-only.

Researcher may:

- read workspace files;
- inspect docs/rules/plans;
- run bounded UI research through a selected provider when it materially improves planning;
- create artifacts only under the provider-defined artifact root when using browser/UI tooling.

Researcher must not:

- implement changes;
- edit plan files;
- call nested subagents.

Ask Researcher for focused findings, relevant files, risks, existing patterns, and planning recommendations.

## Worker Dispatch

Worker executes exactly one atomic Task_X.

Include:

- `task_id`, title, and type;
- `owns`;
- `depends_on`;
- acceptance criteria;
- Worker-owned validation items;
- expected YAML report contract;
- explicit permission for bounded UI probes when the task includes UI/frontend work.

Worker must not:

- modify outside `owns` without minimal justification and reporting;
- perform shared-state Git mutations unless explicitly delegated;
- claim Reviewer-owned validation is satisfied.

## Reviewer Dispatch

Reviewer is review-only and acceptance-facing.

Provide a Reviewer packet when available:

- phase/wave objective;
- tasks included;
- changed files;
- acceptance criteria;
- required validation checklist;
- Worker validation evidence;
- Worker UI probes, if any;
- known waivers;
- known blockers/questions;
- risk areas.

Reviewer must independently verify required Reviewer-owned evidence. Worker probes may inform review but do not replace Reviewer acceptance evidence.

When Reviewer uses browser/UI tooling, artifacts must stay under the selected provider-defined artifact root, such as `.playwright-cli/` for `playwright-cli`.

Use `wave-integration/references/reviewer-packet-template.md` as the packet shape after Worker waves.

## Parallel Dispatch

Dispatch Workers in parallel by default when:

- dependencies are met;
- `owns` are disjoint;
- parallelism does not introduce known conflict or ordering risk.

Choose sequential execution when ordering materially reduces risk, one task generates inputs for another, or the plan explicitly calls for sequential gating.
