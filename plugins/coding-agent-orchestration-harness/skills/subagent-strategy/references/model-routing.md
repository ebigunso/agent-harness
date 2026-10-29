# Model Routing

Use this reference whenever a Researcher is dispatched, in a workspace with one model too, and whenever more than one model is available for a dispatch or a session. Each role goes to the option its reason below resolves to, never to an option picked by the name of its model, family or platform.

## The record of options

Which seats and subagent types a workspace has, the role each can hold, its model, the tendencies observed of that model's family, what the environment runs on (a subscription plan or a pay-as-you-go budget), the budget allowance the owner states, and the option each reason resolves to, make up a dated record that belongs to the workspace, not to this reference. It is kept in `docs/coding-agent/rules/common.md`, the rule file both the Orchestrator and Counsel read, and routing follows what is recorded there; a record kept in `docs/coding-agent/rules/orchestrator.md` moves to `common.md`, where Counsel reads it too. Each resolution names, dated, the capability finding it rests on: what its model was found able to do for that role's work; the record keeps no separate inventory of what each model can do. Setup fills the record and holds it for the owner's confirmation, as the `rulebook` skill states.

The reasons resolve against that record. For a family the workspace has observed nothing of, they resolve against the seed, `references/model-tendencies-seed.md`; a workspace's own dated observation of a family replaces the seed for that family. A model change is an occasion to re-observe and replace the record with a newly dated one.

## How a reason reads

Each role's reason names the kind of capability the role needs, splits it by work type where the work types want different things, and sets how much cost may weigh. For each work type it states the tendency that serves the work, the tendency that harms it, and why each is so.

- No option is best overall. Options are compared per kind of capability: the option that fits one work type best may fit another poorly, and a ranking for one work type says nothing of another.
- A tendency is what an option tends to do when left to itself, not what it can or cannot do.
- The fit ranking for a work type orders the recorded options by how capable each is for that work: how closely its observed tendencies match the one that serves the work and avoid the one that harms it, and what setup found its model can do for that work (the capability finding). Cost never orders it; cost and capability for a given work type do not always go together.
- The reasons describe the ideal case. Where the environment keeps part of a reason from applying, whatever part still applies is applied, as best effort.
- Where the observed tendencies do not tell the options apart for a work type (every option of one family, say, since tendencies are observed per family), the capability finding orders them. Where neither tells them apart, they count as equally capable for that work, and any one the role's cost setting accepts serves, as best effort; its resolution's finding says that none told them apart.
- A role with no cost ceiling (the Auditor; the Researcher, its cost notwithstanding) takes the option first in the fit ranking for its work. A cost-bounded role walks down the fit ranking with cost as the check at each step, as the Worker's cost setting below states.

## Reasons by role

### Orchestrator

- Capability: judgement that keeps the whole picture in view on an under-specified ask.
- Serves the work: holding the ask's aim and the run's larger shape in view, filling what the ask leaves open in the direction its aim points, and spending attention in proportion to consequence. Why: the Orchestrator turns an open ask into a plan, rulings, and the integration of many reports; its mistakes are of direction and proportion, and every task it dispatches inherits them.
- Harms the work: fixing on detail that does not change the outcome; holding work back, or narrowing a design to a safe alternative, without weighing the aim; inventing hardening or checks beyond what the risk warrants. Why: each spends the session on what does not decide the result while every task waiting on it stalls, and a narrowed design leaves the ask's aim unserved.
- Cost: the best fit whose cost allows long sessions, judged against what the environment runs on as the Worker's cost setting judges it, since the Orchestrator's session lasts the whole run.
- The Orchestrator's model is the session's own and is not dispatched: the record states which option fits this reason, so that the owner can open the session on it. Plan decisions and design rulings stay with the Orchestrator and are never dispatched to Workers; who may draft a decision record (ADR): `durable-docs-authoring/references/adr.md`.

### Auditor

- Capability: insight on open-ended questions, for independent judgement of the Orchestrator's work (the value audit, the in-loop goal assessment), where no checklist decides.
- Serves the work: seeing what a question implies beyond its wording, and reaching a judgement where the documents leave room, naming the statement it rests on. Why: the audit is there to find what the Orchestrator did not see, and a departure that matters is more often one of intent than of letter.
- Harms the work: reading for literal conformance only; taking over the framing of the work under audit. Why: a check of the letter passes work that keeps the words and misses the aim, and an auditor that adopts the Orchestrator's framing confirms it instead of judging it.
- Cost: no cost ceiling: the best fit for open-ended insight, whatever it costs, because an audit runs at few points of a run and what it misses reaches the owner unexamined.

### Researcher

- Capability: finding what a plan or a discussion will rest on, split by what the research is for.
- Insight and ideas (exploratory or design research: option framing, architecture surveys, open questions):
  - Serves the work: the wide view: options the ask did not name, tradeoffs framed across the area, connections a narrow reading misses. Why: this research exists to widen what the dispatcher can choose from, so its value is in what the dispatcher had not thought of.
  - Harms the work: answering only the most literal reading of the question; settling early on the safe, known option. Why: either returns what the dispatcher already had.
- Rigor and fact assembly (forensic research: inventories, censuses, evidence gathering, conformance checks):
  - Serves the work: literal, in-bounds retrieval: every instance within the asked scope, each fact tied to where it was found, nothing claimed past the evidence. Why: the result is used as complete and exact, and what is planned on it fails where it is not.
  - Harms the work: going broad and summarizing past what the evidence shows; filling a gap by inference; flagging what is not there. Why: an inferred fact reads like a found one, and the error surfaces only when the work built on it breaks.
- Over a large corpus, among the options that fit the work type, prefer one that holds the whole corpus in one pass without losing what an early part said.
- Cost: cost notwithstanding: the best fit for the work type, whatever it costs, because everything planned or decided on the research inherits its quality.

### Worker

- Capability: carrying one task to its acceptance criteria, split by what acceptance judges.
- Design, human-readable writing, and human-facing interface work (acceptance judges what a person will read, use, or build on):
  - Serves the work: the wide view: keeping the reader or user and the whole design in sight, within the task's scope. Why: acceptance asks whether a person can understand or use the result, which only a view of the whole reaches.
  - Harms the work: executing the letter of the task with no sense of the person it is for; fixing on detail inconsequential to the whole; pulling a design toward a safe alternative without weighing its aim. Why: the result can pass every literal check and still read or work poorly for that person.
- Logic-oriented coding (acceptance judges mechanical precision: behaviour to a spec, line-level correctness):
  - Serves the work: literal, in-bounds execution: doing what the task states, within its `owns`, and nothing more. Why: the work is judged against a spec, and any change beyond the task is a defect the review must find, the subtle ones most easily missed.
  - Harms the work: over-eager edits past the task's bounds; reading the task more broadly than it is written; self-invented hardening and test-building that over-constrains or guards improbable risks. Why: each widens the change past what acceptance asked, adds behaviour nobody specified, and spends the time the task had on it.
- Cost: the best fit within the budget allowance the owner states in the record. Where the owner confirmed the record without naming an allowance, walk down the fit ranking for the work type: take the best-fitting option if its cost is acceptable against what the environment runs on, as the record states it (which subscription plan, or how large a pay-as-you-go budget); otherwise judge the next the same way, until one is acceptable.
  - An option's cost is judged by how much of that plan's usage, or of that budget, the role's work on it would take at the role's volume of use. A difference in cost between options is weighed in that measure, never set aside: an option that costs several times another takes several times the share. Acceptable is judged against that plan or budget, never against a fixed notion of what is expensive: no price is acceptable or not in itself, and the share it takes decides.
  - Where the record states the kind of budget but not which plan or how large, the walk does not take the most costly option by default. As best effort (How a reason reads), it judges against what the record does state, takes a more costly option only where that shows room for its share, and the gap is shown to the owner at setup's hold.

### Reviewer

- Capability: finding the kind of fault the work wants found at its stage, chosen on the Worker's grounds.
- A design still being worked out (boundaries, contracts, proportionality, long-horizon cost):
  - Serves the work: the wide-view review: whether the design serves its aim, what it couples, what it will cost later. Why: the design can still change, and the findings that matter are the ones that would change it.
  - Harms the work: hunting edge-case breakages and line-level defects. Why: they spend the design's iteration on detail the next revision may remove, and bury the finding that would change it.
- Work that must work precisely in production (line-level defects, spec conformance, validation evidence):
  - Serves the work: the rigorous review: precision-leaning, literal against the spec and the evidence, each finding a real defect. Why: what passes here runs, and a missed defect reaches production.
  - Harms the work: a broad skim that passes the work; going broad with findings that are not defects. Why: a skim's approval is trusted as a check that did not happen, and false positives spend the fix loop and hide the real finding.
- An option of a different family from the Worker's finds what the Worker's family missed. Choose one when its observed tendencies fit the kind of finding the stage wants, never for the difference alone.
- Cost: as the Worker's reason states, the walk included.

## Choosing where research goes

The Orchestrator and Counsel choose where research goes by this rule alike. It assumes no seat, peer or model: what a workspace has is read only from its own record of options, kept where The record of options above says.

1. Research is the Researcher role's work, whatever the environment; it is never part of a Worker's task.
2. Read the workspace's record of options: each seat or subagent type, the role it can hold, its model, and the tendencies observed of that model's family.
3. Pick by the Researcher's reason above for the research's work type, insight and ideas or rigor and fact assembly, resolved against the record and, for a family the workspace has observed nothing of, the seed.
4. Among the options that fit, cost does not decide (the Researcher's reason); pick by where the result should live: a peer keeps its own context and returns a report; a subagent returns into the dispatcher's context; bulk reading goes where it will not fill the dispatcher.
5. Where no recorded option fits the work type, dispatch the Researcher as a subagent on the dispatcher's own model, and record what it showed with the date. The Orchestrator records it; Counsel, which never edits rule files, passes its observation to the Orchestrator.
6. Research may still be skipped where the harness allows a skip (for the Orchestrator, the waiver of the `orchestration-harness` Research Dispatch Gate); the waiver then says what was read instead, so a reviewer can judge whether reading was enough.

## Prose quality

- User-facing prose (records, lessons, skill text, PR bodies) is human-readable writing in the Worker's reason. When it was authored on an option that reason does not fit for writing, it receives a rewording pass on an option that does, before finalizing, without semantic change.
- Machine-consumed or contract text (YAML reports, fixtures, scripts) authored on such an option receives that pass only when its prose needs it — a summary, message, or comment that misleads or reads poorly; otherwise it finalizes as authored.

## Tiers and fallback

- Keep the tiers (the Reviewer's two stages, the Researcher's two work types) as separate dispatches when the reasons resolve them to different options. When they resolve to the same option, one dispatch may cover both, with the packet naming each tier's acceptance.
- When only one model is available, it covers every role; the tier rule above still decides whether the tiers are dispatched separately.
