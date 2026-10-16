# Brief: A middle size for a small change

- status: ratified by ebigunso on 2026-10-06. Counsel put the proposal below to him in chat and said it would be written as a short brief; his answer, quoted in full: "Your proposal seems like a good way to handle things. I'll take it." This file restates that proposal and adds nothing to it.
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-10-06
- handed to: agent-harness-orchestrator on 2026-10-06
- product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(agent-proposed)* = Counsel originated it and he accepted it. His quoted words with the date stand beside each.
- kind marks: **gives** (what the work must give him; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- Someone directing work gives a very small change in their own words, and it is built without the ceremony of a full plan. **gives** *(told 2026-10-06, of the several-fit follow-up to setup: "Especially the last amendment, that was a very small change but I saw the Orchestrator ran a full suite of plan and implement on a new branch. This might be beneficial to exercise the guards, but it seems a bit overkill too.")*
- Why: the harness knows two sizes. Trivial work is handled directly, but only when it changes no behaviour; everything else gets a plan, a plan review, a draft audit, a build, a review, a closing audit, a branch and a pull request. A change he states always changes behaviour, so even a one-branch change gets the full suite. *(agent-proposed; accepted 2026-10-06 with the proposal)*

## The middle size

All of this section is agent-proposed and was accepted on 2026-10-06 in the words quoted in the status line.

- A small change that comes from his word keeps two checks: the review of the change, and one closing value audit, which checks that what was built is what he said and nothing more. **gives**
- It may be built without the separate plan, the plan's review and the plan-draft audit; his statement in the brief then stands in place of the plan. The Orchestrator chooses, per change, whether to draft a plan, and when it drafts one the full plan path applies as today. A plan is the right choice when the work needs more than one task, or when his statement leaves open a choice about how to do it that someone should see before it is built. **gives** *(amendment 2026-10-06. On reading the record this line produced he said: "Hmm... waiving plans entirely for small changes may be overkill. I'd like to leave the decision open on whether a plan is deemed necessary, based on what is being worked on." and "I'd like to have less of a strict rule that may result in cases where that would result in suboptimal choices." Counsel proposed this wording and that the trivial class stay strict because it has no audit behind it; his answer: "That seems reasonable. Make the proposed change to ADR-D-0055, and keep the definition of trivial work as is.")*
- While the stack it belongs to is unmerged, it takes no branch and no pull request of its own; it goes on top of the last one. **gives**
- Whether a change is small is the Orchestrator's call. The guard on that call is the closing audit: where the change went beyond his statement, the audit holds it. **gives**

## A small change and the run

- A change he directs after a run is reported ready belongs to the closing of that run and is handled inside it: the run's closing conditions anticipate such changes. A small change is a unit of a run, as a plan is, and not an exception outside it. **gives** *(told 2026-10-06, of ADR-D-0051 as first revised: "I think the better approach is to revise the closing conditions of a run, to anticipate directed changes after a run is reported done and handle them appropriately, rather than to make an exception to allow small runs." Counsel's reading, which he confirmed: that such a change belongs to the run's closing and a small change is a unit of a run.)*
- A small change stated against a brief whose run is already accepted and merged starts a run of its own, of one small change, closing once like any run. A run is one or more units, plans or small changes. **gives** *(agent-proposed 2026-10-06; his answer: "Yes, that reading is right.")*

- The run record holds only what audits stated, as ADR-D-0051 says. The trace the Orchestrator writes for a small change (where the statement is, the words as they reached the session, the start revision, outcome, rulings, review and verdict) lives in a place of its own, not in the run record. **gives** *(told 2026-10-06, a change directed while the run was open for his judgement. The closing audit had marked that the built text put that trace in the run record, against the record he accepted. Counsel put to him: keep the rule and move the trace into the readings file. His answer: "Yes, keep the rule and move the trace to the readings file, or any other place that is appropriate." Where it goes is the Orchestrator's; it reported the readings file cannot hold it, since the auditor opens that file only after grading and the trace is what it grades.)*

## Limits

- This loosens a gate, and he was told so before he took it. It changes the Plan Gate, so the accepted record that states it returns to him for acceptance by name. **constraint** *(agent-proposed; accepted 2026-10-06 with the proposal)*
- Trivial work and work of full size are handled as they are today; the definition of trivial work does not change. **constraint** *(agent-proposed, as the proposal's "middle size"; told 2026-10-06: "keep the definition of trivial work as is.")*

## Core scenario

Agent-proposed, restating the case he raised.

1. With a stack unmerged, he states a one-sentence change to something already built. It is built on top of the stack, reviewed and audited once at its close, with no plan document and no new pull request, and he is told when it is done.

## Pass conditions

- Agent-checkable: the package validators pass; the record that states the Plan Gate is accepted by him by name before the change lands.
- Human-only: the next small change he gives, judged by whether it felt proportionate.

## Left out on purpose

- Running the full suite on small changes to exercise the guards. *(told 2026-10-06: "This might be beneficial to exercise the guards, but it seems a bit overkill too." Counsel's reading, which he took with the proposal: that is a reason to test, not a reason for the product to behave this way.)*
- A rule on test artifacts. *(told 2026-10-06: "No recorded rule required yet.")*
