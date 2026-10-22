# Model Routing

Use this reference whenever a Researcher is dispatched, in a workspace with one model too, and whenever more than one model is available for delegation. Route each role by the strength the model behind it has demonstrated on that kind of work, not by the name of its platform.

## Choosing where research goes

The Orchestrator and Counsel choose where research goes by this rule alike. It assumes no seat, peer or model: what a workspace has is read only from its own record of options, kept where Strengths routed on below says.

1. Research is the Researcher role's work, whatever the environment; it is never part of a Worker's task.
2. Read the workspace's record of options: each seat or subagent type, the role it can hold, its model, and the strengths that model has shown in this workspace.
3. Pick by the strength the research needs, as Routing by work type below states: forensic research wants detail strength, exploratory research wants writing strength, a large corpus wants long-context reading.
4. Among the options with that strength, pick by what the owner has said of quality against cost for that kind of work, and by where the result should live: a peer keeps its own context and returns a report; a subagent returns into the dispatcher's context; bulk reading goes where it will not fill the dispatcher.
5. Where nothing recorded has the strength, dispatch the Researcher as a subagent on the dispatcher's own model, and record the observation with its date. The Orchestrator records it; Counsel, which never edits rule files, passes its observation to the Orchestrator.
6. Research may still be skipped where the harness allows a skip (for the Orchestrator, the waiver of the `orchestration-harness` Research Dispatch Gate); the waiver then says what was read instead, so a reviewer can judge whether reading was enough.

## Strengths routed on

- Writing: altitude and lateral design judgment, and general prose — framing tradeoffs, spotting cross-cutting design risk, producing clear text.
- Detail scrutiny: forensic inventories and mechanical-precision work — exhaustive census passes, spec-conformance checking, line-level correctness.
- Long-context reading: holding a large corpus (many files, long transcripts, whole record sets) in one pass without losing what an early part said.

A model shows a strength through its results on this kind of work in this workspace; that observation is the routing key. A model that has shown a strength is called a writing-strength, detail-strength, or long-context model below.

Which models have shown which strength, and which models and peers a workspace has, is a dated observation that belongs to the workspace, not to this reference: it is recorded in `docs/coding-agent/rules/common.md`, the rule file both the Orchestrator and Counsel read, and routing follows what is recorded there; a record kept in `docs/coding-agent/rules/orchestrator.md` moves to `common.md`, where Counsel reads it too. Where nothing is recorded for a strength, route on it only after observing it, and record the observation with its date. A model change is an occasion to re-observe and replace the record with a newly dated one.

## Routing by work type

Give each role to the model that has shown the strength the work needs:

- Forensic research (inventories, audits, evidence census): detail-strength.
- Exploratory or design research (option framing, architecture surveys): writing-strength.
- Research over a large corpus (whole-repo reads, long transcripts): a long-context model, chosen among those showing the strength the research type above needs.
- Review, correctness tier (line-level defects, spec conformance, validation evidence): detail-strength.
- Review, design tier (boundaries, contracts, proportionality, long-horizon cost): writing-strength.
- Implementation: either — prefer detail-strength when acceptance is mechanical precision, writing-strength when acceptance is judgment or prose.
- Independent judgement of the Orchestrator's work (the value audit, the in-loop goal assessment): the Auditor role; which model holds it is the workspace's choice, recorded with the observations above.
- Plan decisions and design rulings: authored by the coordinating, writing-strength side — never dispatched to implementation workers. Who may draft a decision record (ADR): `durable-docs-authoring/references/adr.md`.

## Prose quality

- User-facing prose (records, lessons, skill text, PR bodies) authored by a detail-strength model receives a rewording pass by a writing-strength model before finalizing, without semantic change.
- Machine-consumed or contract text (YAML reports, fixtures, scripts) authored by a detail-strength model receives that pass only when its prose needs it — a summary, message, or comment that misleads or reads poorly; otherwise it finalizes as authored.

## Tiers and fallback

- Keep the tiers (correctness vs design review, forensic vs design research) as separate dispatches when the tiers differ in the strengths the task needs. When they call on the same strength, one dispatch may cover both, with the packet naming each tier's acceptance.
- When only one model is available, it covers every role; the tier rule above still decides whether the tiers are dispatched separately.
