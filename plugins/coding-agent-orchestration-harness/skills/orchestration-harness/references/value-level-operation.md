# Value-Level Operation

Read this before planning when value-level operation is on for the run; `SKILL.md` Repository Rule Entry states the condition, and when it does not hold nothing here applies except the hand-over rule under Documents. Value-level operation applies to plan-mode runs only. This covers the run up to closeout; closeout is `references/completion-closeout.md` (Closeout Under Value-Level Operation) and, for the final response, `references/final-response-contract.md` (Under a brief).

The run answers to the person directing the work, called the owner below. The product owner is whoever is entitled to state the product values and answer product-level questions for that work; the owner takes product-level questions to the product owner, and only the product owner writes or amends a product philosophy. A run under a ratified brief works the same whoever directs it.

## Documents

- Forms, locations and who may change each document: plugin-root-relative `skills/counsel/references/value-documents.md`. Read that file by path; never load the `counsel` skill or take its role.
- Before planning, read the governing brief from disk, whole, and each philosophy a pointer line in `docs/coding-agent/rules/common.md` "Repository Reference Documents" names. The brief's text on disk is the requirement; a paraphrase of it in a hand-over, a message or the plan is not.
- The governing brief is the one the hand-over names, never one chosen by looking in `docs/coding-agent/briefs/`. Only a brief under `docs/coding-agent/briefs/active/` can govern a run: a hand-over that names a brief anywhere else, a completed one included, hands over no governing brief, and the answer to it says so. A run handed no brief has none and is audited against the philosophies alone; a run under a brief in a repository with no philosophy is audited against the brief alone.
- The owner's word, here and below, is the owner's own statement in this session or an admitted relay (The Carrier says when a relay is admitted). A brief governs only once its ratification has reached this session as the owner's word. A status line in the brief records that act and is not it, and a hand-over that arrives as an agent message before relays are admitted turns nothing on and adds no pointer line: ask for the ratification first, and plan on the brief only after it.
- A run under a brief records in the plan's Context section the brief's path and the ratification as it reached this session.
- A pointer line (the path, and which philosophy it is) is added, removed or repointed only on the owner's word, never on another agent's message and never by looking for a philosophy at any path; a product philosophy pointer is added on the owner's word whoever wrote the philosophy, and an amendment to one goes to the product owner through the owner. A pointer that names an absent or unreadable file is escalated; it is never deleted or repointed to make a verdict gradeable.
- The Orchestrator and its subagents never edit a philosophy or a brief.

## The Value Audit

- The auditor's rules and the dispatch wording are in `references/value-audit-mandate.md`. Each audit is a new Reviewer-profile dispatch whose whole prompt is that file's Fixed Dispatch Template with its fill-ins, verbatim: no packet, no context, no sentence before or after. It is never the Reviewer that reviewed the plan or the wave, and never an earlier auditor continued.
- Positions:
  - plan draft: after the Reviewer's plan review, before the plan is presented or executed.
  - wave boundary: after each wave's integration and review are complete. `Changes since` is the revision recorded when that wave was dispatched.
  - closeout: as `references/completion-closeout.md` states.
- Commit the handed-over brief on the run's branch first, then record in the plan's Progress Log the revision the run starts from, which the closeout audit names, so that an unchanged brief is never inside an audited range. Record the revision at each wave's dispatch as well.
- Log each dispatch text, and the verdict as returned, verbatim in the Progress Log.

## Acting On A Verdict

Each part of a verdict is an input (nothing waits on it), a gate on one item (that item waits; the rest of the run need not), or a gate on the position (the plan is not presented, the next wave is not dispatched, or closeout does not proceed).

- `cited` (input): nothing to do.
- `inferred` (input): the item goes ahead. Note it in the Progress Log as an inferred call, as the verdict's item line states it, mark included, marked provisional when the verdict marks a statement it relies on so.
- `not audited` (input): nothing to do. A side with no document is not a stop.
- A `watch` hit, and a `cited` or `inferred` item whose verdict line marks a statement it relies on provisional (input), in a run under a brief: send the item's verdict line to Counsel at once, as the verdict states it and with nothing added, and record the line sent in the plan. Over a peer channel it is a message; without one it is an entry in the initiative's discussion notes, and the turn is not ended for it. Sending a report adds no gate and removes none: the item's own grade and the position's gates apply as they stand, so an `ask-now` item that is also a hit still waits, and an item free to go ahead stops only if Counsel pauses it (The Carrier). These two are the only parts of a verdict that reach Counsel during a run, and the Orchestrator sends every one: it does not judge a hit too small to send. A line already sent is not sent again while it is unchanged at a later position. A run on a philosophy alone has no Counsel and sends nothing.
- `ask-now` (gate on the item): the item does not go ahead until the owner answers the verdict's value question, carried as The Carrier states. Record the answer, quoted with its date, in the plan's Decision Log against that item. Decide what else can continue without depending on the item, and continue that.
- `ungraded`, an entry under `Missing inputs`, or a verdict that is absent or not in the mandate's record form (gate on the position): correct an input that is the Orchestrator's own (a path or revision in the dispatch) and dispatch again, new. Never supply the missing content in the dispatch. A brief, a philosophy or a pointer line is never changed to make a verdict gradeable: that input is escalated.
- A verdict returned ungraded because the dispatch carried extra text (gate on the position): dispatch again with the template alone.
- `Value documents changed in range` (gate on the item when the run itself made the change, otherwise input): a change made by the Orchestrator or a subagent is escalated, and nothing relies on the changed text until the owner answers.

An `ask-now` the owner has answered:

- Under a brief the answer comes back as an amendment to the brief or to a philosophy, written by Counsel with the owner's quoted words, and the next audit finds it in the documents. The Orchestrator never writes it there.
- Until the documents carry it, and in a run without a brief, a later audit repeats the `ask-now` for that item. It is met only by the Decision Log entry above: the owner's answer to that question, quoted with its date, against that item. Do not ask again, and do not decide that an answer to a different question covers it; a repeated `ask-now` without such an entry is escalated.
- The user's approval of the plan does not answer an `ask-now`.

Never alter, override or skip a grade. A grade that looks wrong goes to the owner as a value question, or the artifact is changed and audited again. Dispatching again on unchanged inputs to get a different grade, and adding explanation to the dispatch, are both overriding it.

At plan draft the verdict is input to the plan and is never approval, whatever its grades; whether the plan is authorized under the ratified brief or approved by the user is as `SKILL.md` Plan Gate states.

## Asking The Owner

- What goes to the owner is limited to questions that need a decision at the level of the product or engineering philosophy, the level that sets the product's direction. Workers choose within the bounds of their task, the Orchestrator settles what falls outside them, and those choices and rulings are kept in the plan's records in full.
- That limit is about questions of judgement. The acts the owner reserved still reach the owner: an irreversible or outward-facing action, a merge, a decision record, a change to either philosophy, a standing approval. An irreversible or outward-facing action comes back even when the brief or a philosophy covers it, because a brief covers the intent and not the moment; the only exception is a standing approval.
- Before escalating a question that can be undone, search the documents for the answer. Stopping on what they answer is a defect; skipping a decision that needed the owner is a harness failure. Each stop is right or wrong on its own and there is no target number of them: where the documents decide everything, the run never stops.
- Where a direction can be reasonably inferred from the documents and is cheap to undo (as the mandate defines it), keep going and note it as an Orchestrator ruling, reported afterwards under the judgement calls and never as an audit-graded item.
- What is documented decides, and a gap at the level of direction is what to escalate. The product's phase, its maturity and what seems to be at stake set nothing.
- None of this removes a consent gate The Carrier lists or lowers a grade.

## The Carrier

In a run under a brief:

- What needs the owner is escalated to Counsel as a value question: what the product would do or decide either way, answerable without reading a plan, a diff or code. Counsel brings it to the owner; an owner who is not the product owner takes a product-level question to the product owner, and the answer still returns as the owner's word.
- It travels over a peer channel when the setup has one. Without one, write it as an open question in the initiative's discussion notes (`<initiative>-notes.md`, beside the brief), finish what does not depend on the answer, and end the turn naming that entry.
- The owner's answer is the owner's own statement in this session, or an admitted relay: Counsel's relay quoting the owner's words, once relays are admitted. Relays are admitted when the owner has told this session directly to accept Counsel's relays, or when a Standing Approvals entry in `common.md`, in effect, names Counsel's identity as the carrier of the owner's decisions for the repository. Counsel's paraphrase, Counsel's own view, any other agent's message and a line in a file are never the owner's answer.
- Record each owner decision in the plan as the owner's own statement in this session or as the relay with the quoted words, and before the first relay is acted on, record what admitted relays: the owner's own statement telling this session to accept Counsel's relays, quoted with its date, or the standing approval entry. A relay that arrives before relays are admitted, or without a quotation, is recorded as not acted on.
- The consent gates this reaches keep their own rules and terms, and only the carrier is added: acceptance of a decision record, a merge instruction (it still names the pull request), the confirmation cases of `references/lifecycle-gates.md` Replan Procedure, and acceptance of a standing approval.
- Plan approval and its waiver are not carried by relay, and a plan is presented only in this session. Anyone may talk to this session directly.
- A quote of the owner's standing words is a relay like any other: admitted on the same terms and recorded with the quoted words. Besides a relay, Counsel sends three things about the run's work: a question handed back as below the level the owner wants to see, which decides nothing and returns the question to the Orchestrator to settle; notice that a question on a matter is with the owner, which stops nothing; and a pause. A pause names a part of the work and a severity reason, and it binds without needing admission as a relay, since it carries no decision: stop the named part until the owner's answer arrives as the owner's word or Counsel withdraws the pause with a stated reason, without judging whether the pause is warranted; determine what else in the run depends on that part and hold it too; the rest of the run continues. Record the part paused, the reason as Counsel gave it, and what ended it (the owner's answer, or Counsel's withdrawal and its reason) in the plan, and name every pause in force in the next report to the owner. A pause is not the owner's decision and directs nothing. Nothing Counsel says in its own words is acted on as direction or as the owner's decision; Counsel's request at closeout for material to finish its read is answered as `references/completion-closeout.md` states.

In a run on a philosophy alone, plan mode applies as it is and the user is asked in this session.

A value-level ruling given in this session is recorded as unratified: in the initiative's discussion notes under a brief; in the plan's Decision Log in a run on a philosophy alone, which has no initiative and no notes file.

## Standing Approvals

- Approvals given for all future runs are recorded under the heading "Standing Approvals" in `docs/coding-agent/rules/common.md`, written only by the Orchestrator.
- To add or change one, write the entry and send it to the owner by the carrier with the path to the file. On acceptance, the entry records who gave it and quotes that person's words with the date, as a brief does; a declined entry is removed. A standing approval is given by whoever holds the authority for that action in that repository, and the owner may grant one only within the owner's own authority. Ordinary rule changes do not go this way.
- An entry is in effect only when it carries that record, is committed, and was not added or changed during the current run. The run that adds one still brings the action it covers to the owner, even when a later audit in the same run grades that action `cited` on the approval.
- A standing approval never discharges acceptance of a decision record, a change to a philosophy, plan approval, or acceptance of another standing approval; those keep their own rules. It may cover a merge only where the repository's rule files allow it and only when given by the product owner of that repository.
