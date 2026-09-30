# Brief: Value-level operation of the harness

- status: ratified by ebigunso on 2026-09-30 ("That looks reasonable enough. You can now start delegating work to the orchestrator.")
- drafted by: agent-harness-counsel, from discussion with ebigunso
- handed to: agent-harness-orchestrator
- provenance tags: *(told)* = ebigunso said it; *(inferred)* = Counsel inferred it and ebigunso did not object; *(agent-proposed)* = Counsel originated it and ebigunso accepted it with the brief

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's.

## Who it is for and why

- You (ebigunso), as owner of a product built with agents. *(told)*
- You talk with Counsel about what the product does or should do, and judge what was built by its behaviour. *(told)*
- You shape direction by objecting at product level, and no longer audit each plan for drift. *(told)*
- You get aligned results, more achieved in features and maturity, and sharper thinking from the discussion. *(told)*

## What Counsel is

- It draws out your views and cements them as the grounds for implementation. *(told)*
- It is available at any time, not only before a project or a phase: routine check-ups on the project's state when you ask, and open conversations that produce insight for the product. The role must not be too limiting. *(told)*
- Its limit is the level it works at, behaviour and decisions, not the occasions it may be used on. For a check-up it learns the project's state through a read-only Researcher reporting at that level. *(agent-proposed)*

## How a conversation with Counsel should go *(agent-proposed; the positive form was requested)*

- You speak first, and it restates so you can check it.
- It follows where the conversation goes and doesn't walk a list. It must never feel like filling in a form. *(the prohibition is told)*
- It explains what you need to know before asking you to judge.
- It raises views outside yours and says what the conventional answer would be.
- It ends by saying what changed in the documents, or that nothing did.

## Stops during a run

- The measure is whether each stop was right, not how many there were. *(told)*
- Where enough is already decided, never stopping is the desired behaviour. *(told)*
- Where a direction can be reasonably inferred from standing values, the run keeps going and reports it afterwards. *(told)*
- Skipping a decision that needed to reach you is a harness failure to be fixed. *(told)*
- Stopping on something the documents already answer is also a defect. *(inferred)* This applies to decisions that can be undone.
- An irreversible or outward-facing action stops and comes back to him through Counsel even when the brief or a philosophy covers it; a brief covers the intent, not the moment. *(agent-proposed, accepted 2026-09-30: "Yeah I agree with your assessment. Critical decisions should come back to me through the Counsel.")*
- The exception is what he has approved for all future runs. That standing approval holds, and its home is the repository rule files. *(told 2026-09-30: "But not for everything, what I approve for all future runs should probably hold, and that I think the home would be the repository rule files.")*
- A change that adds a standing approval to the rule files reaches him through Counsel with a link to the file, and he accepts it himself before it takes effect, the same way as the three kinds of document he reads himself. Ordinary rule changes stay as they are. *(agent-proposed, accepted 2026-09-30: "Yes, I think that's sound.")*
- Autonomy comes from the decisions documented; where none is documented, that is the gap. No separate judgement of product phase sets it. *(told)*

## Closeout

- It leads with behaviour. *(told)*
- Implementation detail is allowed when your judgement needs it, with the reason stated. It is not the default and it is not prohibited. *(told; the stated-reason requirement is agent-proposed)*
- It also reports what was learned that the philosophies don't account for. *(agent-proposed, accepted 2026-09-30: "This seems like a good idea.")*

## Delivery and judgement

- It ships as a first version. No trial on a development build is required first. *(told)*
- You judge it through first real use on Character Memory, and what proves off comes back as corrections. *(told)*
- You don't judge skill wording, file layout, validators or the sync across runtimes. *(inferred)*

## Limits on the run

- Merges happen only on your explicit instruction for each pull request. *(told, repository rule)*
- The change to plan approval needs its own decision record, accepted by you separately. *(inferred, from the lessons log)*
- Plan approval is waived for this initiative only. *(ruling 2026-09-30, relayed by Counsel: "Let's try going with the first option. I'll then retroactively look at the plan and see if something was still off, and then I'll discuss it's implications.")* The Reviewer's plan review still runs, and plans stay on disk for him to read afterwards. Counsel holds no authority to approve a plan.
- His ping to the Orchestrator said only that his words come through Counsel, so merge instructions travel through Counsel too. *(told 2026-09-30: "I only told it that my words come through you.")* Counsel relays a merge only with his exact words naming that pull request, and never infers one from agreement about something else. *(Counsel's own handling rule, stated to him)*
- He checks behaviour before anything ships. The unit he accepts is a stack of pull requests that together ship something he can judge, not each pull request on its own. *(told 2026-09-30: "I'd want to check the behavior before things get shipped. Then it's probably better off to have me check before merge, but not in the form of approving every individual PR, rather as an accepted stack that ships something I can decide to accept or not.")*
- Stack acceptance applies in this repository too, with every pull request named in his acceptance. *(put to him 2026-09-30 in those words: "Yes.")*
- A stack preferably arrives with a way to run or observe it before merge. It is a preference, not a requirement, since it may not be possible every time. *(told 2026-09-30: "Preferably yes, but it might not be possible every time, so I'm not sure if you should state it that way.")*
- How a rejected stack is fixed is not restricted. *(told 2026-09-30: "Fixes can either go directly into the PR branch that is responsible for that part of the code, or if that doesn't apply then a new PR stacked on top would work. This is really just implementation details, and anything reasonable will work. I'm not going to restrict how to handle things.")*
- A finished, reviewed run may publish its branch and open the pull request before his approval; the merge still waits for him. *(asked 2026-09-30 as "may a finished, reviewed run publish its branch and open the pull request on its own in this repository, as a standing approval?": "Yes, pull requests can be opened before approval.")* As a standing approval for later runs it takes effect only once the rule-file entry has reached him with a link and he has accepted it.
- Whether a stack has anything undecided that needs him is called by the closeout value audit, not by the Orchestrator about its own work. *(agent-proposed, accepted 2026-09-30: "Yeah I think that would be a good way to go as well.")*
- He considered letting pull requests with nothing undecided merge without him and withdrew it for this repository, because the plugin is installed from `main` and a merge here ships to its users. *(told 2026-09-30, in reply to Counsel's point about `main`: "Good catch. I take it back for this repository, as you pointed out. Fully support your take.")* How loose merging may be is a per-repository matter for that repository's rule files.
- Two checkpoints stay with ebigunso and reach him through Counsel: accepting the decision record that changes plan approval, and each merge. *(told, same ruling)*

## Provisional

- No engineering guidelines exist for the harness yet. This run leans on the existing rules and decision records. *(agent-proposed)*
- The wording of the persona's core action will stay rough until verdicts on real results sharpen it. *(told)*

## Decisions settled in discussion

These were agreed between ebigunso and Counsel before this brief. They are constraints on the design, stated at intent level.

### Roles and sessions

- The role is named Counsel; runtime name `harness-counsel`.
- Counsel and the Orchestrator are separate sessions. The session you open sets the altitude. Nested subagents are not required; the Orchestrator session stays flat.
- Counsel never dispatches Workers, and may dispatch read-only Researchers for facts.
- Counsel may do quick reads of code, which the engineering discussion may need; grounding work that requires bulk code reads is still delegated to a Researcher. *(told 2026-09-30, on reading ADR-D-0034, replacing the earlier line that Counsel never reads code: "Probably the boundary about you never reading code has gone too far. The engineering discussion may be better handled if the Counsel can do quick reads too. But grounding work that requires bulk code reads should still be delegated to a researcher.")*
- Plans and diffs stay off limits to Counsel. *(asked 2026-09-30, "Do plans and diffs stay off limits?": "Yes.")*
- A quick read serves a discussion with him and is never a check on a run's work. *(agent-proposed, accepted 2026-09-30: "This one is reasonable.")*
- Counsel does not list the files it read in the conversation. *(told 2026-09-30, declining Counsel's proposal: "This one probably is just too much to bring up. I don't want to look at a list of files you read. That doesn't serve the discussion at hand.")*
- Counsel hands over a ratified brief as a file the Orchestrator reads itself, and does not reach past it.
- Cementing is ebigunso's act. Counsel drafts and restates; nothing counts until ratified. A partial yes is not approval of the whole; after a correction the full text is presented again. Counsel never declares a discussion closed.
- Counsel has two later contacts with a run: value questions that come back during it, and an independent read when a result is presented for human judgement, formed before seeing the auditor's verdict. That read is advisory and quotes its source.
- Ratifying a brief takes an act of the owner, not a line in a file. The act happens in Counsel's session, and Counsel relays it to the Orchestrator quoting the owner's words. *(ruling 2026-09-30: "Come back to me, but I shouldn't need to type into Orchestrator's session directly. It should escalate, and the Counsel should bring it to me."; the relay-with-quote form is Counsel's reading of it)*
- As owner, ebigunso does not need to type into the Orchestrator session. When the Orchestrator needs his authority or judgement it escalates to Counsel, and Counsel brings it to him. *(told, same ruling)*
- The one exception: Counsel's relay carries his decisions to an Orchestrator session only after he has himself told that Orchestrator to accept Counsel's relays as his. *(told 2026-09-30, after the Orchestrator showed it cannot tell a faithful relay from any other agent message: "Yeah I'll ping the orchestrator to accept your message relayed as mine.")*
- One Counsel holds both the product and the engineering discussion. For the engineering one it is advisable to get advice from GPT models as well, brought into the discussion marked with its source. *(told 2026-09-30: "I'll take your case and stay with one counsel. Engineering could still use help from GPT models so it's advisable to get advice from them too for that.")*
- Which model Counsel runs on is the owner's choice when he opens the session; it is not harness text. *(told 2026-09-30: "This is just me switching out models so it doesn't have to go into the harness.")*
- Counsel serves the person directing the work, whether or not that person owns the product. A product philosophy exists only where that person owns the product. The brief traces to the philosophy where there is one, and to the request as received where there is not. Counsel never infers product values on behalf of an absent owner; where there is no product philosophy, product-level judgements come to the person directing the work, who takes them to the requester. The engineering side works exactly as in the owner case. *(agent-proposed, accepted 2026-10-01: "Yes, generalize it and have the Orchestrator revise 0034."; this replaces the earlier line under which a non-owner had no Counsel and talked to the Orchestrator directly. His reason: "it's still good to have as much delegation as possible to free up my attention.")*
- Plans are still presented only by the Orchestrator session, never relayed by Counsel, and anyone may talk to the Orchestrator session directly; a value-level ruling given there is recorded to the discussion notes as unratified.

### Counsel as contributor

- Sharpening ebigunso's thinking is a value in itself: viewpoints outside his own, and enough understanding of unfamiliar areas to judge them. It must not pull the discussion toward the conventional middle.
- Anything Counsel originates is tagged agent-proposed; tenets keep ebigunso's wording.
- Counsel argues once for a branch that was dismissed quickly, then accepts the call.
- Unusual preferences are tested for coherence, not normalised.
- Before ratification, Counsel lists what was discussed but not recorded and why, and each drop is confirmed.
- At closing, Counsel lists the tenets that depart from the conventional answer; if there are none it says the document cannot decide anything.
- Tenets not ready to settle are marked provisional; inferred calls resting on them are flagged at closeout.

### Documents, in the target repository

- Product philosophy: standing, changed only by the owner. It states the behaviour he wants from using the product, what he wants out of it, and what he does not want it to be. *(told 2026-09-30: "I feel it's well written, because it states the behavior I want from using Character Memory, what I want out of it, and what I don't want it to be."; this replaces an earlier tenet form with trade-off, decided case, priority and a one-page limit, which Counsel withdrew)* The model he named for the form is `docs/project_philosophy.md` in the Character Memory repository: prose that gives a view to reason from, with success written as observable behaviour. No fixed fields and no length limit.
- Engineering philosophy: a separate document, complete without the product philosophy. It says how he wants the project to look, which is broader than trade-off stances and can include things like data model expectations. It works at mostly the same level as the product philosophy, and both sit above decision records. *(told 2026-09-30: "The implementation implications section could move out, but it's not completely unreasonable to be there since they do state how I want the project to look like. In light of the new harness shape we talked about, it could move into the engineering document side that still operates mostly on the same level as the philosophy document, above ADRs."; and earlier the same day, on keeping the two apart: "I'd just like to have the engineering separated from product philosophy.")* It may refer to the product philosophy; the product philosophy never refers to it.
- A conflict between the two is never inferred; it is asked. The ruling is written into the engineering philosophy.
- The owner's reading surface is three kinds of document: decision records, the product philosophy and the engineering philosophy. They shape later implementation decisions, so he reads them himself and objects to anything even slightly off. A change to any of them reaches him through Counsel with a link to the document itself; Counsel's summary never stands in for it. Each decision record is still accepted on its own. *(told 2026-09-30: "You bring it to me, but with a link to the document itself so I can actually read them, and not take your word for granted. I think ADRs, product philosophy, and the engineering philosophy, are the three things that I need to keep track of and object to if there's anything even slightly off. Those shape the future implementation decisions, so it's the critical part.")*
- Both philosophies were and are revised by discussion after implementation and measurement shed new light. A review of philosophy and roadmap is something he asks Counsel for; a model capability upgrade is one occasion for it and not the only one. *(told 2026-09-30: "it has been amended a few times through further discussions which took place after some implementation work and measurements has shed new light on the situation." and "I had told it to review the philosophy and roadmap to bring up any points that needs to be revised or discussed. The reason I did that was because of a model capability upgrade that has occurred. That is one point to do a revision, but I think it probably doesn't have to be the only one.")* Other occasions, where Counsel points out that one has occurred and he decides whether to hold the review: a result he rejects, several escalations landing on the same gap, the end of an initiative when measurements are in, and a change in what he plans to build next. *(agent-proposed, accepted 2026-09-30: "The revision occasions you proposed also seems sound, so I'll take them as you proposed.")*
- Initiative brief: one initiative's acceptance; traces to product tenets; each pass condition marked agent-checkable or human-only.
- Discussion notes: unratified, typed (facts, assumptions, decisions, open questions). The auditor never reads them.
- Decision records (ADRs) stay for architectural forks; the why names the tenet served.
- Neither philosophy need be complete up front. They grow from what each initiative forces into words and from verdicts on results. A result ebigunso rejects, or an inferred call he confirms, yields a candidate amendment that he accepts or not in discussion.
- Wording note: where this brief says "tenet" or "engineering guidelines", read "a statement in the product philosophy" and "the engineering philosophy".

### Value audit

- A stateless Reviewer dispatch profile, not a new role. Fresh context each time; inputs are the documents that exist and the artifact under review, read from disk, never the Orchestrator's summary.
- It runs by position: plan draft, each wave boundary, closeout.
- Three grades: cited (a tenet or the brief covers it; proceed); inferred (extends named tenets and is cheap to undo; proceed, journal, show at closeout); ask-now (no support, tenets conflict, irreversible or outward-facing, or it would loosen a pass condition).
- Scope test: each user-facing item maps to the brief, is internal mechanics, or is scope expansion that escalates.
- A proxy never stands in for a human-only condition.
- It audits against whichever documents exist. With only engineering guidelines, it audits that side and plans are approved by ebigunso as today.
- Where the person directing the work owns the product, a brief they ratified in their own words stands in for their values on the product side until a product philosophy exists, and the audit grades the product side against it, including the inferred grade. Where that person does not own the product, the brief carries the request as received; the audit may grade an item cited when the request explicitly covers it, never inferred, and everything else on the product side comes to that person to take to the requester. *(the split was put to him by the Orchestrator and the refinement by Counsel; accepted 2026-10-01: "Yes to the split, and take the refinement too.")*
- Escalations reach ebigunso as value questions, not implementation questions.

### Lifecycle

- With a ratified brief, a citing audit approves plans; without one, ebigunso approves as today. One conditional inside plan mode, not a third lifecycle.
- A review loop that does not converge is treated as evidence against the brief and becomes a value question.
- Workers make choices within the bounds of their task, and the Orchestrator settles what falls outside them; that is unchanged from the accepted harness rule. No act-then-report. *(told 2026-09-30: "Workers make choices within its bounds, and the Orchestrator settles things that fall out of them, that is unchanged.")*
- What comes to ebigunso is limited to what needs a decision at the level of the product or engineering philosophy, the level that defines the direction of the product. *(told 2026-09-30: "What should come to me is now more limited, only something that needs decisions on the product or engineering philosophy level that defines the direction of the product.")*
- So the choices Workers report and the rulings the Orchestrator makes are kept in the run's records, and a closeout shows him only those that bear on direction. *(inferred from the line above, then confirmed 2026-09-30 when put to him as "A closeout shows you only the Worker choices and Orchestrator rulings that bear on direction.": "Looks good."; replaces an earlier line that showed all Worker judgement calls at closeout)*
- This limit is about questions of judgement. The acts he reserved still come to him: irreversible or outward-facing actions, merges, decision records, changes to either philosophy, and standing approvals. *(inferred, then confirmed 2026-09-30 when put to him as "Your limit on what reaches you is about questions of judgement; the acts you reserved still come to you.": "Yes.")*
- Closeout reports "candidate ready": evidence for agent-checkable conditions, human-only conditions pending, the collected judgement calls, and Counsel's read.

### Left out on purpose

- Persona voices for the discussion agent.
- Nested orchestration.
- A directory-structured discussion memory; one notes file per initiative is enough.

## Reference input

- The skill set this was compared against is a third-party one he keeps outside this repository (read-only): `align-user-gate`, `context-check` with its `DESIGN.md`, `salamander`, `undine`, `discussion-management`, `implementation-orchestration`.
