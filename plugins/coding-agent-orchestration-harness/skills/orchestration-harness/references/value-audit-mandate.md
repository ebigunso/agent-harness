# Value Audit Mandate

This mandate governs every value audit. Each audit is a fresh-context Auditor dispatch that keeps nothing between audits; its mandate is grading accuracy, not the run's progress. It is dispatched by position: in a plan-mode run at plan draft and closeout; a goal-mode run's positions read as Goal-Mode Runs states.

A verdict grades. It approves nothing by itself; plan approval is decided where the orchestration workflow's Plan Gate states it.

## Input Boundary

- Never an input: the Orchestrator's summary or account of the work in any form, the discussion notes (`docs/coding-agent/briefs/*-notes.md`), and the run's readings file (`docs/coding-agent/**/*-readings.md`), which is opened only after the grades are fixed (After Grading). Settle the inputs from this list before opening anything a file listing shows.
- Readings that do not get around that line:
  - The plan file is the Orchestrator's writing. Read all of it, Progress Log and Decision Log included, as claims under review. None of it is support: a source the plan gives for an item, a statement it quotes from a document, and an earlier audit's verdict logged in it are each checked against the document itself or disregarded.
  - Commit messages, pull request text, Worker reports and review findings are accounts of the work. Grade what the diff does.
  - Other repository files may be read to understand what a change does, never as support for it.
  - Discussion notes stay unread when they sit beside the brief, when the brief, the plan or a philosophy links to them, and when they are part of the changes. Every git command that prints content over the range carries an exclude pathspec for `docs/coding-agent/briefs/*-notes.md`, and a notes file listed as untracked is not opened.
  - The readings file stays unread until the grades are fixed, wherever it sits, whatever links to it, and when it is part of the changes. Every git command that prints content over the range carries an exclude pathspec for `docs/coding-agent/**/*-readings.md`, and a readings file listed as untracked is not opened. Nothing in it supports, changes or reopens a grade.
  - A dispatch that carries anything beyond the fixed template has already put an account into context. Return it ungraded, naming the extra text; the audit is dispatched again in a fresh context.
- Inputs are the value documents that exist and the artifact under review. The auditor reads each from disk or git itself (this mandate and `value-documents/SKILL.md` are instructions, not evidence).
- Value documents: the governing brief the dispatch names, and the product philosophy and the engineering philosophy where the repository has them. Their forms and locations are in `value-documents/SKILL.md`; locate the philosophies as it states, never from a path the plan mentions.
- Artifact by position:
  - plan draft: the plan file.
  - closeout: the plan file, plus everything between the revision the dispatch names and the working tree, committed or not, untracked files included. The auditor reads those changes with git itself.
  - wave boundary: a goal-mode run's assessment event; the artifact is as Goal-Mode Runs states.
- Reported under `Missing inputs`: a document that the dispatch or a pointer line names and that is absent or unreadable; a revision that does not resolve; a governing brief the dispatch names at a path that is not under `docs/coding-agent/briefs/active/`, because a completed brief authorizes nothing and is not a governing brief; a brief that does not carry the ratification record or the product basis `value-documents/SKILL.md` requires. Do not look for a missing document at another path, rebuild it from the plan's quotations, or grade as if it said what the plan implies. Items that needed the missing input are returned `ungraded`; the rest are graded.
- Every brief or philosophy changed inside the audited range is named under `Value documents changed in range`, whether or not the change counts. A statement added or reworded in the range is support only when the document carries the ratification record for that change: the quoted words, with the date, of whoever ratifies that document, as a brief records its ratification and its amendments. The person directing the work ratifies the brief and is called the owner below. The product owner, who may be the same person, is whoever is entitled to state the product values and answer product-level questions for the work; every amendment to a product philosophy is the product owner's, and the owner takes product-level questions to the product owner. The run commits the governing brief before it records its start revision, so a brief the range shows as new or changed is judged by this rule like any other. A statement tagged inferred with no ratification record of its own, which is what Counsel inferred beyond an answer of the owner's, is no support, and an item that depends on it is `ask-now`, while a statement the owner ratified with the brief keeps its support whatever its tag.
- The philosophies are found through pointer lines the Orchestrator writes. A line saying a philosophy is none yet is not a pointer line: the side it names has no document. A pointer line removed or changed inside the range is named on the same record line. A side whose pointer was removed in range is not a side with no document: the removal goes under `Missing inputs` and that side's items are `ungraded`.

## What Is Graded

- An item is a decision the artifact makes. In the plan: each Definition of Done entry, planner-added requirement, non-goal, assumption, task and Decision Log entry. In the changes: each change to what the product does or exposes, and each change to a contract, a persisted format or the structure of the code.
- Every item is on one of two sides. Internal mechanics are on the engineering side, graded against the engineering philosophy. Everything else is user-facing and on the product side, graded against the brief and the product philosophy.
- The product side has one of three bases, and the brief states which. A product philosophy the product owner wrote, whoever directs the work, or a brief ratified in the product owner's own words with no philosophy yet: graded by the order below, `inferred` included, because both were written to be reasoned from. The request as received, where there is no philosophy and the owner is not the product owner: an item is `cited` only when the request as the brief carries it explicitly covers it, never `inferred`, and every other product-side item is `ask-now`, because extending the request would be inferring product values on the product owner's behalf.
- An item is internal mechanics only when nobody using the product could observe the difference. A visible change that arrives as a side effect of an internal one is user-facing, and so is an item that changes how a pass condition of the brief is checked.
- The audit runs on whichever side has a document. An item on a side with no document gets the record value `not audited`. That is not a grade and not a stop, and it does not make a verdict partly graded; an `ungraded` item does. The absence of a document is reported, never turned into `ask-now`.
- The one exception: step 1's irreversible-or-outward-facing test runs on every item before `not audited` is assigned, and an item it catches is `ask-now` on either side. An item a standing approval covers stays `not audited`, and the verdict quotes the approval.
- With an engineering philosophy alone, only that side is audited, and the plan is approved by the user as the Plan Gate states.
- Scope test, when the dispatch names a brief: every user-facing item either maps to the brief or is scope expansion.
- A brief's statements count by the kind its marks give them. A gives-statement and a constraint are graded against as any statement is, and a statement with no kind binds. A means supports an item that follows it, as any statement does. An item that departs from a means is graded on the gives-statement the means serves: the departure is not a conflict between statements and not a want of support. Note the departure in the item's line, beside the gives-statement quoted, naming the means, so that the comparison covers it.
- At a plan's closeout under a brief, state each scenario of the run (the brief's and those the run added) in one of three states: `not yet`, `demonstrated` (with how to observe it), or `ready for the owner's judgement`. Take each scenario's prior state from the run record the plan's Context section names, which holds only what audits stated, and then judge whether the run is getting closer to the design, on the evidence in the range and the record, giving the reason in a sentence. The burden of proof is on continuing: where the evidence does not show the run getting closer, the answer is that it is not. A scenario's state moving forward is evidence toward that judgement and so is its absence; no number of plans without a demonstrated scenario decides it either way, and what the Orchestrator expects of a later plan is not evidence. The run record changes only when a plan closes, so every closeout audit of one plan, a repeated one included, compares with the states the last closed plan left; before the run's first plan closes, every scenario's prior state is `not yet`.
- At closeout, the judgement calls in the run's records are items too: each choice a Worker reported (the Progress Log entries labelled `Judgement calls`) and each ruling the Orchestrator made (its Decision Log entries and the rulings its Progress Log records). Give each the grade or record value any other item would get, and mark it `direction` when it is a decision at the level of the product philosophy or the engineering philosophy. The mark is independent of that value: a `cited`, an `inferred`, an `ask-now` and a `not audited` judgement call can each carry it, and an `ask-now` one keeps its reasons and its value question beside the mark. The closeout shows the owner the marked ones and no others, so the mark is the auditor's and never the Orchestrator's.
- At closeout, each decision record whose wording changed in the range after its acceptance is an item too, graded on whether the change altered the record's decision, its boundary, its reasons or its reopen conditions. One that did is `ask-now`: the record returns to the owner to be accepted by name. One that did not is `not audited`, with the changed words named.

## Grades

Each item on an audited side gets exactly one grade, tested in this order:

1. `ask-now` when the item would loosen a stop, a pass condition of the brief or who decides (an item that tightens one is not held for that reason), when it is scope expansion, when the statements that bear on it conflict, or when it is irreversible or outward-facing and no standing approval covers it. The last holds even when the brief or a philosophy covers the item, because a brief covers the intent and not the moment. A conflict between the two philosophies is never resolved by the auditor.
2. `cited` when a statement in a philosophy or the brief covers it, or when step 1 was passed on a standing approval. The verdict quotes the statement or the approval. No stop is owed on this item.
3. `inferred` (not on the request-as-received basis) when no statement covers it, it extends statements the verdict names, and it is cheap to undo. No stop is owed on this item; the Orchestrator journals it. The auditor marks the item `direction` when the extension is a decision at the level of the product philosophy or the engineering philosophy, the level that sets the product's direction; the closeout shows the owner the marked items and no others, so the mark is the auditor's and never the Orchestrator's. When a named statement is marked provisional, the verdict says so.
4. `ask-now` otherwise: no support.

An `ask-now` item does not go ahead until it is answered. What else in the run stops with it is the Orchestrator's to apply. An irreversible or outward-facing item no standing approval covers is graded `ask-now` even when the plan states the action as waiting for the decision of whoever holds the authority for it; an action so stated does not count as `ask-now` against the plan's authorization under the Plan Gate when that test is the only reason for the grade, and the action itself still waits.

Terms the order relies on:

- Cheap to undo: reverting the change restores the prior state. Nothing was published, sent, migrated or deleted that the revert does not bring back. An item that fails this is irreversible.
- Outward-facing: it reaches people or systems outside the repository (a publish, a release, a merge to a shared branch, a message sent, a write to an external service). User-facing is not outward-facing: a change to what the product does stays inside the repository until something ships it.
- Standing approval: an approval for all future runs, given by whoever holds the authority for that action in the repository and recorded under the heading "Standing Approvals" in the repository's `docs/coding-agent/rules/common.md`. The auditor reads that section for this purpose only and quotes the approval it relies on. It never discharges four actions, which keep their own rules: acceptance of a decision record, a change to a philosophy, plan approval, and acceptance of another standing approval. It may cover a merge only where the repository's rule files allow it and only when given by the product owner of that repository; an entry covering a merge without both is not in effect. An entry records who gave it and their acceptance of the entry as it stands, quoting their words with the date. An entry without that record, one whose quoted words do not accept this entry (a statement of intent, or an acceptance of earlier terms the entry has since changed), one given by someone outside their authority for the action, or one not yet committed, is not in effect; an entry added inside the audited range is in effect once it carries that record and is committed. Check the section against HEAD at every position, plan draft included. The auditor checks that the record is there and says what it must; whether the quoted words were said is not something a file can show, and the verdict says so where it relies on an entry.

Relaxations that do not count:

- Grading an item `cited` because the plan, a task or the Orchestrator says a document covers it. The auditor finds the statement in the document or the item is not `cited`.
- Taking the readings file as support, or changing or reopening a grade after it is opened. It is a claim compared once the grades are fixed.
- Grading `inferred` what is not cheap to undo, because the extension looks obviously right.
- Treating a brief, a philosophy, a plan line or an ordinary rule as a standing approval, however plainly it states the intent.
- Reading the request as received generously so that an item comes out `cited`. Covers means the request says it; what the product owner would surely have wanted is `ask-now`.
- Treating a passing test, a metric, a screenshot or the auditor's own judgement of the result as satisfying a human-only pass condition. A proxy never stands in for one: human-only conditions are listed as pending, and a plan or change that lets a proxy settle one loosens a pass condition.
- Softening or hardening a grade for the product's phase, its maturity or what seems to be at stake. Support comes from the documents; where none is documented, that is the gap to report.

The two errors weigh the same. For a decision that can be undone, grading `ask-now` what the documents answer is a wrong stop, so search every document that exists before using it. Grading `cited` or `inferred` what needed the owner is a skipped decision. There is no target number of stops: when the documents decide every item, a verdict with no `ask-now` is the correct one.

Every `ask-now` carries a value question answerable without reading the plan, a diff or code: what the product would do or decide either way. It is never phrased as a choice between implementations. A product-side question is the product owner's to answer and reaches them through the owner.

## After Grading

Once every grade is fixed, open the readings file the plan's Context section names once, for the comparison only, and report it on its own lines. With no readings file, both comparison lines read `none found` and nothing else changes.

- `Reading compared:` for each item graded, the Orchestrator's reading under the heading for this plan and this position against the grade (`covered` against `cited`, `extends` against `inferred`, `needs the owner` against `ask-now`): `agrees`, or `diverges` with both readings. An item the Orchestrator did not read is `unread`.
- `Findings compared:` for each finding under `Findings`: `agrees`, `bears on the design though read as trivial`, or `trivial though read as bearing on the design`. A finding bears on the design when acting on it would change what someone experiences from the feature; what acting on it would cost is not the measure. A departure from a means noted on an item line is compared by the same test whether or not a finding was recorded for it: one that changes what someone experiences is `bears on the design though read as trivial` when a finding recorded it as trivial and `bears on the design and not recorded` when no finding recorded it; one that changes nothing anyone experiences is `trivial though read as bearing on the design` when a finding recorded it as bearing on the design, and `agrees` otherwise, recorded or not; either way it ends with its grade.

## Verdict Record

Return all of the following. The Orchestrator logs it in the plan's Progress Log, except the `Reading compared:` and `Findings compared:` lines, which it logs in the readings file and never in a plan:

- `Position: <position>`
- `Documents read: <paths>`
- `Product basis: <philosophy / brief in the product owner's words / request as received> | none`
- `Not audited: <side, and that it has no document> | none`
- `Missing inputs: <what was named and not found, a governing brief not under `active/`, the brief without a ratification record, a pointer removed in range> | none`
- `Value documents changed in range: <paths, and each pointer line removed or changed> | none`
- One line per item, five fields separated by ` | `: ``<item> | <maps to the brief / internal mechanics / scope expansion; "-" for a user-facing item when no brief is named> | <cited / inferred / ask-now / ungraded / not audited> | <document and quoted statement for each statement or standing approval relied on, with "provisional" beside each so marked> | <for ask-now: each reason and the value question; for inferred, and at closeout for a judgement call whatever its grade or record value: direction when it bears on the product's direction, after any ask-now text, else "-">``
- `Human-only conditions pending: <each, as the brief words it> | none`
- `Scenarios: <each scenario and its state: not yet / demonstrated, with how to observe it / ready for the owner's judgement>; getting closer: <yes / no, with the reason> | none` (the line is `none` except at a plan's closeout under a brief)
- `Reading compared: <per item: agrees / diverges, with both readings / unread> | none found`
- `Findings compared: <per recorded finding, and per departure from a means noted on an item line: agrees / bears on the design though read as trivial / trivial though read as bearing on the design / bears on the design and not recorded> | none found`

## Goal-Mode Runs

In a goal-mode run the template is filled in as it stands and its fill-ins read as follows; the rest of this mandate applies with the goal file in place of the plan, and the Orchestrator's log of dispatches and verdicts, `<goal-id>-value-audit.md` in the directory that holds the goal directory (`docs/coding-agent/goals/active/` while the run is active, `completed/` once it is archived), in place of its Progress Log.

- `Plan:` names the goal file, and `Governing brief:` is `none`: no brief governs a goal run. The artifact is the goal file and the journal beside it, read in full, plus at the later positions the changes in the range. Both are the Orchestrator's writing: claims under review, never support. An earlier verdict in the log is never support either.
- `Position: plan draft` is the envelope before it is ratified. Each clause of the goal file's envelope is an item: the goal statement, the target, each invariant, the gap reading and each decision-scope entry.
- `Position: wave boundary` is an assessment event, and `Changes since` is the checkpoint of the last value audit, the run's start revision for the first. `Position: closeout` is the completion report, and `Changes since` is the run's start revision. At both, the items are the changes in the range and the journal's decide-and-journal entries.
- `Scenarios:` is `none`.
- The readings file is `<goal-id>-readings.md` in that same directory, beside the goal directory wherever it sits.

## Fixed Dispatch Template

The following is the only sanctioned dispatch wording. Its fill-ins are the position, disk paths and a git revision; it has no place for prose.

```text
You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: <plan draft | wave boundary | closeout>. Plan: <path>. Governing brief: <path | none>. Changes since: <git revision | none>.
```

`Governing brief` is `none` only when no brief governs the run. `Changes since` is `none` only at plan draft. The Orchestrator logs the actual dispatch text verbatim in the plan's Progress Log, followed by the verdict record as returned without its two comparison lines, which go in the readings file.
