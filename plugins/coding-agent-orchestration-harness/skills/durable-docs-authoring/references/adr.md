# ADR discipline: warrant, homes, and collaboration flow

Criteria and workflow for decision records (ADRs) in any repository the harness operates in. Format resolution: follow the repository's decision-record convention when its rules point to one; otherwise use the harness defaults `references/adr-template.md` and `references/adr-repo-readme.md`.

## Warrant criteria (root test first)
The warrant is a single counterfactual over the decision's reasoning, premises, and boundaries. Record an ADR when losing the reasoning — and the fact that it was a decision point at all — is expected to make future work handle the decision wrongly in any of three modes:

- VIOLATE it while its premises hold (absent the record, the decided state reads as accident);
- wrongly PRESERVE it after its premises expire (ossification — the record's Decision Drivers and Revisit When are what make legitimate reversal safe);
- wrongly EXTEND it beyond its deliberately bounded scope (over-application — the boundary's rationale is as loseable as the decision's).

The test carries a severity conjunct: warrant requires stakes as well as likelihood. The expected mishandling must be costly to detect or undo — broken contracts, corrupted data or philosophy, expensive rework, or silent long-lived drift. A mishandling that normal review or cheap refactoring would catch and correct does not clear the bar however likely it is; route it to a rule (recurring) or the Decision Log (one-time).

Every ADR proposal must state the expected mishandling concretely, naming its mode and its cost: "without this record, future work would likely do X against / past / beyond Y, costing Z."

Recognition signals mark where the test usually fires; they prompt the test and are not independently sufficient:

- (a) externally observable or cross-boundary contract/authority/evidence-ownership shapes with tempting alternatives;
- (b) rejected alternatives likely to be re-proposed;
- (c) meaningful migration or reversal cost;
- (d) cross-repository obligations;
- (e) user rulings establishing durable governance defaults (authorship is provenance, not warrant);
- (f) decisions resting on premises likely to expire;
- (g) decisions whose scope boundary is as deliberate as the decision.

Negatives derive from the test rather than forming a separate list: no ADR where the mishandling is likely but cheap (review-catchable and reversible), and no ADR where nothing ongoing can be contravened — reversible measured parameters (the invariant may warrant an ADR; the numbers are evidence), expired deferrals and task sequencing, ordinary tactics — or where the record already exists: another repository's ADR (link to it instead), or always-loaded enforcement rules whose rationale burden is genuinely local.

## Three homes
- ADR: the why, rejected alternatives, and revisit conditions that outlive the implementing plan.
- Rule: executable enforcement read on every task.
- Decision Log: plan-scoped record.

ADR-plus-rule pairs are the expected shape for enforced contracts; the homes are complements, never substitutes. Severity routes between them: likely-but-cheap violation classes belong to rules, which prevent at act time on every task; the ADR bar is mishandling expensive or silent enough that rule-time prevention is not sufficient on its own.

## Collaboration flow
1. When the root test fires, state in-conversation the triggering signal, a proposed title, and the expected mishandling scenario with its mode and cost named (violate / wrongly preserve / wrongly extend; what the mishandling would break or cost); record all of it in the plan Decision Log in the same action.
2. Draft on the writing-strength side per `subagent-strategy/references/model-routing.md`; its authorship clause governs and is not restated here.
3. Persist nothing until the user approves. Decline is terminal: record it in the Decision Log and do not re-propose.

Amendment and lifecycle:

- Wording clarifications may amend in place with a revision note; changed authority or behavior requires a superseding ADR with `supersession_scope` and reciprocal frontmatter updates on the superseded ADR.
- Full supersession or retirement is one atomic operation: set frontmatter status, move the file to `docs/decisions/superseded/` renamed with a self-describing suffix (`--superseded-by-ADR-X-NNNN` or `--retired`), update every inbound reference to the new path, and prove link repair with an absence search for the old filename.
- Partial supersession never moves the file: the ADR remains authoritative in place for its surviving clauses.
- IDs are never reused; numbering gaps in active directories are meaningful.
