# Lifecycle Gates

Use this reference for plan, research, execution, replan, and closeout lifecycle details.

## Primary Sources

Sources and their read conditions: `SKILL.md` Repository Rule Entry (canonical); the three rule files are the only unconditional reads, and lessons, plans, the reference documents listed in `common.md`, and project files each load on the condition stated there.

If the rule files are absent or unreadable, continue under the `orchestration-harness` skill and record the missing rule context when it materially affects planning or validation; creating rules is `rulebook` work triggered separately. Do not add global migration placeholders to role rule files.

## Plan Gate Details

Trivial/non-trivial criteria, requirement challenge, plan and approval requirements, and lifecycle selection: `SKILL.md` Plan Gate (canonical).

Follow-up non-trivial work re-enters the Plan Gate (`SKILL.md`): chain it through a new or updated plan, or, under a ratified brief, as a small change (below), never by extending the approved scope in place.

Clarifications, follow-up requirements, and plan refinements are NOT plan approval. In plan mode, execution of non-trivial work requires the user's explicit approval of the presented plan or the user's explicit waiver naming the approval step; the Orchestrator cannot grant that waiver. Neither a task request nor a direct instruction to do the work is plan approval unless it explicitly approves the presented plan or explicitly waives the approval step. When in doubt, ask; without applicable user approval or waiver and with no user to ask, present the plan and end the turn.

Authorization under a ratified brief is the second source in `SKILL.md` Plan Gate (canonical); whenever it does not authorize, the paragraph above is the whole rule. Its conditions for a plan in full:

- The governing brief is the one the hand-over named for this work, and its ratification reached this session as the owner's word (`references/value-level-operation.md` Documents); an amendment to the brief counts on the same terms as the brief.
- The plan review is closed only when no finding is left open. A review loop that does not converge goes to the owner as a value question and is not a closed review. The audit is dispatched after the review closes.
- A verdict that is missing, not in the mandate's record form, leaves any item `ungraded`, or grades nothing on the brief's side authorizes nothing. A side with no document is `not audited` and does not stand in the way.
- One `ask-now` item means the plan is not authorized by this route. The item goes to the owner as a value question (`references/value-level-operation.md` The Carrier), unless it is `ask-now` only because of a line the Orchestrator added to its own plan, which is first dropped or redone as that reference's Acting On A Verdict states; this route can authorize only on a new audit of the plan as it then stands, after the answer is in the value documents or the plan no longer makes that decision.
- An irreversible or outward-facing action that no standing approval in effect covers: the plan is authorized by this route only when it states the action as waiting for the decision of whoever holds the authority for it, taken at its moment and not before. So stated, the action's `ask-now` does not count against authorization when that test is the verdict's only reason for it; otherwise only the approval or waiver in the paragraph above authorizes that plan. Either way the action itself still waits.
- The verdict covers the plan as it stands when execution starts. What is later added to or changed in what the plan decides goes back through its gate, as Replan Procedure step 4 states, before the changed item is executed; a second audit on unchanged inputs does not replace the first.
- Before execution starts the plan records the ratification as it reached this session (the owner's statement, or the relay with the quoted words), the plan review closed with no finding open, and the audit's dispatch text and verdict, logged as `references/value-level-operation.md` states.

A small change built without a plan (`SKILL.md` Plan Gate, canonical) is authorized by the same source on these terms:

- The owner stated the change in the governing brief, or in an amendment to it on the same terms as the brief; the statement, as it stands in the brief, is the requirement in place of a plan.
- The Worker builds it as one Task_X. The Orchestrator writes the task's `type`, `owns`, `depends_on`, acceptance and validation items from the statement into the Worker dispatch, as the Dispatch Integrity Gate requires; no plan file holds them. Wave integration, the Reviewer packet and review, and `git-workflow`'s checks before a push, its privacy sweep included, apply as for a plan.
- No plan review and no plan-draft audit runs. After the review of the change, one value audit is dispatched at position closeout, and nothing of the change is published or reported as done before its verdict holds nothing: the verdict is acted on as `references/value-level-operation.md` Acting On A Verdict states, and an item beyond the statement is held there as any `ask-now` is.
- Before the Worker is dispatched, the run's changes file logs the change in a section of its own (`references/completion-closeout.md` The changes file): where the owner's statement is, with the owner's words as they reached this session, and the revision the change starts from.
- When the Orchestrator drafts a plan for a change instead, the plan path above applies in full.
- Where it goes: a small change, whether built without a plan or with one drafted for it, goes on top of its stack's last branch whenever that stack is unmerged, with no branch and no pull request of its own, and the text of the existing pull request is brought up to date. A plan of full size keeps the ordinary branch and pull-request policy (`git-workflow`).

Plan review loop: the Orchestrator triages each Reviewer finding as fix, research-and-rewrite, or dispute; re-review scopes to the delta only when the delta re-review condition in `skills/wave-integration/references/integration-checklist.md` holds, otherwise it is full; a third round on the same seam applies that file's third-bounce detector; a finding that needs a ruling follows Escalation Ruling below.

## Research Dispatch Details

Gate: `SKILL.md` Research Dispatch Gate.

1. The Orchestrator may read repository files and run searches to decide triviality, scope, and validation; reading is not a substitute for a Researcher on unfamiliar or cross-cutting areas.
2. Dispatch one Researcher per narrow focus (see `subagent-strategy`); parallel Researchers for complex or high-ambiguity work.
3. When non-trivial work proceeds without a Researcher, record `Research waived: <reason>` in the plan before execution; the reason names what the Orchestrator read instead.

## Replan Procedure

Triggers: `SKILL.md` Replan Triggers. The procedure covers every issue discovered during authorized work, whoever found it: a Worker, a Reviewer, a Researcher, the Auditor, or the Orchestrator itself.

1. Read the issue as one of three: within the task as given, fixed in place because it was always part of it, which is no revision and asks nothing; a change to the design, which revises or extends the plan; or a matter for later, noted for its own task. No issue is absorbed into the current change as if it had been part of the task. Record the reading, and for a change to the design its impact and the plan delta (tasks, waves, validation), in the plan Decision Log.
2. Surface it in the next report or wave integration.
3. Pause for user confirmation when the change is contract-shape (Escalation Ruling below), irreversible, or outward-facing: stop dispatching further Workers, ask at most three questions, and continue only after confirmation.
4. A plan revised or extended mid-run goes back through the gate that admitted it, for what changed, before any of the change is built. First the plan review of the revision, closed with nothing open. Then, under a governing brief, whichever source authorized the plan, a value audit of the plan as it now stands at position `plan draft` with `Changes since: none`, graded as a whole against the brief and the philosophies and not against the issue that prompted it. A plan the user approved, as every plan without a brief is, also needs the user's explicit approval of the revision or explicit waiver naming the approval step, after the review and any audit. The audit's scope test applies to the revision as to a draft, and the plan review's two questions to each piece it adds. Nothing is extended on the Orchestrator's judgement alone, and step 3 replaces none of this. Where the repository's engineering philosophy or rules say otherwise, they win (`engineering-quality-baselines` Precedence).

When value-level operation is on (`SKILL.md` Repository Rule Entry), `references/value-level-operation.md` states who is asked at step 3 and for a ruling under Escalation Ruling that needs the owner, how the question travels, and what counts as the answer. The pause cases and what each confirmation must say are unchanged.

## Escalation Ruling

Use this procedure when a Worker or Reviewer escalation asks for a ruling rather than a fact.

Two-tier threshold:

- Routine escalations (missing input, ambiguous acceptance, local sequencing) may be answered at coordination tempo.
- Contract-shape escalations — anything that would change a schema, interface, boundary, invariant, or other owned contract — require a deliberate design decision, never a quick coordination answer.

For contract-shape rulings:

1. Enumerate the blast radius before ruling: every consumer across repos, serialization surfaces, deferred scopes, and owned contracts the ruling touches.
2. If self-verification cannot cover that radius, dispatch a Researcher first and rule only on its evidence.
3. Delivering the ruling and recording it in the plan Decision Log are one action — never send the answer without the log entry.

When recording a ruling, run the admission test in `durable-docs-authoring/references/adr.md`; if it passes, propose an ADR and make its acceptance ask separately from the ruling.

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
