# Value Audit Mandate

This mandate governs every value audit. The auditor is a fresh-context Reviewer-profile dispatch that keeps nothing between audits; its mandate is grading accuracy, not the run's progress. It is dispatched by position: plan draft, each wave boundary, closeout.

A verdict grades. It approves nothing by itself; plan approval is decided where the orchestration workflow's Plan Gate states it.

## Input Boundary

- Inputs are the value documents that exist and the artifact under review. The auditor reads each from disk or git itself (this mandate and `counsel/references/value-documents.md` are instructions, not evidence).
- Value documents: the governing brief the dispatch names, and the product philosophy and the engineering philosophy where the repository has them. Their forms and locations are in `counsel/references/value-documents.md`; locate the philosophies as it states, never from a path the plan mentions.
- Artifact by position:
  - plan draft: the plan file.
  - wave boundary and closeout: the plan file, plus everything between the revision the dispatch names and the working tree, committed or not, untracked files included. The auditor reads those changes with git itself.
- Never an input: the Orchestrator's summary or account of the work in any form, and the discussion notes (`docs/coding-agent/briefs/*-notes.md`).
- Readings that do not get around that line:
  - The plan file is the Orchestrator's writing. Read all of it, Progress Log and Decision Log included, as claims under review. None of it is support: a source the plan gives for an item, a statement it quotes from a document, and an earlier audit's verdict logged in it are each checked against the document itself or disregarded.
  - Commit messages, pull request text, Worker reports and review findings are accounts of the work. Grade what the diff does.
  - Other repository files may be read to understand what a change does, never as support for it.
  - Discussion notes stay unread when they sit beside the brief, when the brief, the plan or a philosophy links to them, and when they are part of the changes. Every git command that prints content over the range carries an exclude pathspec for `docs/coding-agent/briefs/*-notes.md`, and a notes file listed as untracked is not opened.
  - A dispatch that carries anything beyond the fixed template has already put an account into context. Return it ungraded, naming the extra text; the audit is dispatched again in a fresh context.
- Reported under `Missing inputs`: a document that the dispatch or a pointer line names and that is absent or unreadable; a revision that does not resolve; a governing brief the dispatch names at a path that is not under `docs/coding-agent/briefs/active/`, because a completed brief authorizes nothing and is not a governing brief; a brief that does not carry the ratification record or the product basis `counsel/references/value-documents.md` requires. Do not look for a missing document at another path, rebuild it from the plan's quotations, or grade as if it said what the plan implies. Items that needed the missing input are returned `ungraded`; the rest are graded.
- Every brief or philosophy changed inside the audited range is named under `Value documents changed in range`, whether or not the change counts. A statement added or reworded in the range is support only when the document carries the ratification record for that change: the quoted words, with the date, of whoever ratifies that document, as a brief records its ratification and its amendments. The person directing the work ratifies the brief and is called the owner below. The product owner, who may be the same person, is whoever is entitled to state the product values and answer product-level questions for the work; every amendment to a product philosophy is the product owner's, and the owner takes product-level questions to the product owner. The run commits the governing brief before it records its start revision, so a brief the range shows as new or changed is judged by this rule like any other.
- The philosophies are found through pointer lines the Orchestrator writes. A pointer line removed or changed inside the range is named on the same record line. A side whose pointer was removed in range is not a side with no document: the removal goes under `Missing inputs` and that side's items are `ungraded`.

## What Is Graded

- An item is a decision the artifact makes. In the plan: each Definition of Done entry, planner-added requirement, non-goal, assumption, task and Decision Log entry. In the changes: each change to what the product does or exposes, and each change to a contract, a persisted format or the structure of the code.
- Every item is on one of two sides. Internal mechanics are on the engineering side, graded against the engineering philosophy. Everything else is user-facing and on the product side, graded against the brief and the product philosophy.
- The product side has one of three bases, and the brief states which. A product philosophy the product owner wrote, whoever directs the work, or a brief ratified in the product owner's own words with no philosophy yet: graded by the order below, `inferred` included, because both were written to be reasoned from. The request as received, where there is no philosophy and the owner is not the product owner: an item is `cited` only when the request as the brief carries it explicitly covers it, never `inferred`, and every other product-side item is `ask-now`, because extending the request would be inferring product values on the product owner's behalf.
- An item is internal mechanics only when nobody using the product could observe the difference. A visible change that arrives as a side effect of an internal one is user-facing, and so is an item that changes how a pass condition of the brief is checked.
- The audit runs on whichever side has a document. An item on a side with no document gets the record value `not audited`. That is not a grade and not a stop, and it does not make a verdict partly graded; an `ungraded` item does. The absence of a document is reported, never turned into `ask-now`.
- The one exception: step 1's irreversible-or-outward-facing test runs on every item before `not audited` is assigned, and an item it catches is `ask-now` on either side. An item a standing approval covers stays `not audited`, and the verdict quotes the approval.
- With an engineering philosophy alone, only that side is audited, and the plan is approved by the user as the Plan Gate states.
- Scope test, when the dispatch names a brief: every user-facing item either maps to the brief or is scope expansion.

## Grades

Each item on an audited side gets exactly one grade, tested in this order:

1. `ask-now` when the item would loosen a pass condition of the brief, when it is scope expansion, when the statements that bear on it conflict, or when it is irreversible or outward-facing and no standing approval covers it. The last holds even when the brief or a philosophy covers the item, because a brief covers the intent and not the moment. A conflict between the two philosophies is never resolved by the auditor.
2. `cited` when a statement in a philosophy or the brief covers it, or when step 1 was passed on a standing approval. The verdict quotes the statement or the approval. No stop is owed on this item.
3. `inferred` (not on the request-as-received basis) when no statement covers it, it extends statements the verdict names, and it is cheap to undo. No stop is owed on this item; the Orchestrator journals it. The auditor marks the item `direction` when the extension is a decision at the level of the product philosophy or the engineering philosophy, the level that sets the product's direction; the closeout shows the owner the marked items and no others, so the mark is the auditor's and never the Orchestrator's. When a named statement is marked provisional, the verdict says so.
4. `ask-now` otherwise: no support.

An `ask-now` item does not go ahead until it is answered. What else in the run stops with it is the Orchestrator's to apply. An irreversible or outward-facing item no standing approval covers is graded `ask-now` even when the plan states the action as waiting for the decision of whoever holds the authority for it; an action so stated does not count as `ask-now` against the plan's authorization under the Plan Gate when that test is the only reason for the grade, and the action itself still waits.

Terms the order relies on:

- Cheap to undo: reverting the change restores the prior state. Nothing was published, sent, migrated or deleted that the revert does not bring back. An item that fails this is irreversible.
- Outward-facing: it reaches people or systems outside the repository (a publish, a release, a merge to a shared branch, a message sent, a write to an external service). User-facing is not outward-facing: a change to what the product does stays inside the repository until something ships it.
- Standing approval: an approval for all future runs, given by whoever holds the authority for that action in the repository and recorded under the heading "Standing Approvals" in the repository's `docs/coding-agent/rules/common.md`. The auditor reads that section for this purpose only and quotes the approval it relies on. It never discharges four actions, which keep their own rules: acceptance of a decision record, a change to a philosophy, plan approval, and acceptance of another standing approval. It may cover a merge only where the repository's rule files allow it and only when given by the product owner of that repository; an entry covering a merge without both is not in effect. An entry records who gave it, quoting their words with the date. An entry without that record, one given by someone outside their authority for the action, or one added or changed inside the audited range, or not yet committed, is not in effect; check the section against HEAD at every position, plan draft included.

Relaxations that do not count:

- Grading an item `cited` because the plan, a task or the Orchestrator says a document covers it. The auditor finds the statement in the document or the item is not `cited`.
- Grading `inferred` what is not cheap to undo, because the extension looks obviously right.
- Treating a brief, a philosophy, a plan line or an ordinary rule as a standing approval, however plainly it states the intent.
- Reading the request as received generously so that an item comes out `cited`. Covers means the request says it; what the product owner would surely have wanted is `ask-now`.
- Treating a passing test, a metric, a screenshot or the auditor's own judgement of the result as satisfying a human-only pass condition. A proxy never stands in for one: human-only conditions are listed as pending, and a plan or change that lets a proxy settle one loosens a pass condition.
- Softening or hardening a grade for the product's phase, its maturity or what seems to be at stake. Support comes from the documents; where none is documented, that is the gap to report.

The two errors weigh the same. For a decision that can be undone, grading `ask-now` what the documents answer is a wrong stop, so search every document that exists before using it. Grading `cited` or `inferred` what needed the owner is a skipped decision. There is no target number of stops: when the documents decide every item, a verdict with no `ask-now` is the correct one.

Every `ask-now` carries a value question answerable without reading the plan, a diff or code: what the product would do or decide either way. It is never phrased as a choice between implementations. A product-side question is the product owner's to answer and reaches them through the owner.

## Verdict Record

Return all of the following for the plan's Progress Log:

- `Position: <position>`
- `Documents read: <paths>`
- `Product basis: <philosophy / brief in the product owner's words / request as received> | none`
- `Not audited: <side, and that it has no document> | none`
- `Missing inputs: <what was named and not found, a governing brief not under `active/`, the brief without a ratification record, a pointer removed in range> | none`
- `Value documents changed in range: <paths, and each pointer line removed or changed> | none`
- One line per item: `<item> | <maps to the brief / internal mechanics / scope expansion; "-" for a user-facing item when no brief is named> | <cited / inferred / ask-now / ungraded / not audited> | <document and quoted statement for each statement or standing approval relied on, with "provisional" beside each so marked> | <for ask-now: each reason and the value question; for inferred: `direction` when it bears on the product's direction, else "-">`
- `Human-only conditions pending: <each, as the brief words it> | none`

## Fixed Dispatch Template

The following is the only sanctioned dispatch wording. Its fill-ins are the position, disk paths and a git revision; it has no place for prose.

```text
You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: <plan draft | wave boundary | closeout>. Plan: <path>. Governing brief: <path | none>. Changes since: <git revision | none>.
```

`Governing brief` is `none` only when no brief governs the run. `Changes since` is `none` only at plan draft. The Orchestrator logs the actual dispatch text verbatim in the plan's Progress Log, followed by the verdict record as returned.
