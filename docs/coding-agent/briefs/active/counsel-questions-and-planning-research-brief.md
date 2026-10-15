# Brief: Counsel's questions while drafting, and research before a plan

- status: ratified by ebigunso on 2026-10-14 ("I ratify the brief, hand it over now."). Asked before ratifying whether there is anything the work must not do or must ask before doing, he added nothing.
- handed to: agent-harness-orchestrator on 2026-10-14
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-10-14, over two issues he wrote in the repository: issue 90 (Counsel's questions while drafting) and issue 86 (research before an execution plan). The issues are his and are the requirement's source; this brief states what they ask in the brief's form and adds nothing of substance to them.
- product basis: the product owner's own words in the two issues and in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(agent-proposed)* = Counsel originated it and he accepted it. His quoted words with the date stand beside each.
- kind marks: **gives** (what the work must give him; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- Two small fixes to the harness text ship with the current stack before the bigger changes he has written up are taken on. **gives** *(told 2026-10-14: "let's discuss the smaller fixes first, so we can ship the current stack with those fixes before we work on bigger changes." and, of Counsel's pick of issues 90 and 86: "The two you picked is the right ones I think.")*

## Counsel's questions while drafting (issue 90)

Issue 90 is the source; the shape below came from discussion on 2026-10-14 and goes further than the issue's text.

- Before a question reaches the owner while a brief is being drawn out, Counsel writes it as an experience change: who, what they do, what they then experience, with the options side by side. If the options read the same at that level, the question is Counsel's: decided, written into the brief, and tagged inferred or agent-proposed. If they read differently, it goes to the owner in that form. The framing is itself the test, not a presentation of a question already judged to be the owner's. **gives** *(told 2026-10-14: "the right shape would be for you to show me the experience framing for each thing you want me to decide on. And when doing that, if a question isn't something I have to answer, then that would be very clear when framed as an experience change, like something that really doesn't affect what I experience on the surface level, you would know before bringing it to me." Counsel's reading that the framing is the test: "Both readings are right.")*
- A conflict between statements Counsel itself drafted is Counsel's to resolve the same way when the discussion made the intent plain. **gives** *(told, issue 90, first rule)*
- At ratification the owner is shown the experience framings for the decisions in the brief that changed anything, not the brief itself. The brief stays the record on disk for the run and the audit; the owner reads it only if he wants to. **gives** *(told 2026-10-14: "Reading through a long brief is the same kind of pain reading a plan incurs, which was one of the core points that was supposed to be addressed with this stack's changes."; Counsel's reading that he sees the framings and not the brief at ratification: "Both readings are right.")*
- Where the work could be done with or without the owner's help, the brief states the unassisted path as the default and the assisted path as the backup. Counsel does not ask which; at most it tells the owner once that the backup may be needed. **gives** *(told, issue 90, second rule)*
- These rules live in the Counsel skill, which owns Counsel's conduct toward the owner, and not in a repository's rules. **constraint** *(told, issue 90)*
- The issue's own lever, a list of tagged decisions at ratification and at closeout, is replaced by the framings above as what the owner sees; the tags stay in the brief for the audit. **means** *(agent-proposed; follows from his words above)*

## Research before an execution plan (issue 86)

- Before an execution plan is drafted, the investigation needed to decide what the plan should contain is done: enough to establish the relevant current behaviour, the affected areas, the constraints and the validation approach; and its findings are used to write concrete tasks with meaningful scope, dependencies, acceptance criteria and validation. Depth stays proportional to the change, and the plan still states what, why and constraints, leaving implementation details to the Worker. **gives** *(told, issue 86, "Expected behavior")*
- Where a material unknown cannot be resolved beforehand, the plan states what remains unknown, why, and what decision or evidence is needed; dependent work is conditional or awaits replanning, and is not presented as settled behind a generic investigate-first task. **gives** *(told, issue 86)*
- Plan review flags an investigation-first plan when that task merely postpones research needed to make the rest of the plan concrete. **gives** *(told, issue 86, "Acceptance criteria")*
- Research remains a legitimate deliverable when the request is itself an investigation, or when a bounded experiment or implementation-stage check is genuinely necessary; such a task states the question it answers, the expected evidence, and how its outcome affects later work. **constraint** *(told, issue 86, "Scope")*
- The planning guidance, the plan template and the plan-review expectations are aligned around this; the existing Research Dispatch Gate is the place it builds on. **means** *(told, issue 86)*

## Version

- The plugin's version becomes 1.0 once everything in the stack has landed and the Counsel session design is shipped. This brief is the last piece of that stack, so the bump is made in this work, as the last change before the stack is reported ready. **gives** *(told 2026-10-14: "Version should be bumped to 1.0 once everything lands and the Counsel session design is shipped." The placement in this run is Counsel's reading; the stack is pull requests 72, 73 and 75 to 85 plus this work.)*

## Limits

- A matter that differs from what the owner believes was agreed is not made a standing reason to ask him during a run. **constraint** *(told 2026-10-14, declining Counsel's proposal of such a line: "'What I think I agreed' only lives in my mind, which you can only assume, and if you could correctly assume what I thought then you'd probably be able to warn or correct me at that moment. If there was a gap there, nothing can catch that until I look at it and notice. Asking me every time is being overly cautious, and bog down day to day work. I'd leave it be for now, but if you want to prevent it further, then the place to apply a fix is at discussion and brief writing time rather than during a work.")*
- Nothing of the bigger issues (89, 87, 88) is taken on here. **constraint** *(told 2026-10-14, see the first section)*

## Core scenarios

Agent-proposed, restating the issues' acceptance cases; ratified with the brief.

1. A Counsel session drafting a brief meets a choice: framed as an experience change the options read the same, so Counsel decides it and tags it, and the owner is not asked. A choice whose framings differ reaches the owner as those two framings, and is answered in a sentence.
2. A brief is ready: the owner sees a handful of experience framings for what changed anything, ratifies on those, and does not read the brief. Where the work could use his help, the brief states the unassisted path as the default and tells him once that the backup may be needed.
3. A plan is drafted for a change in unfamiliar code: the research is done first, the tasks are concrete, and no task says "investigate first" for what the plan needed to know.
4. A draft plan whose first task postpones the research the rest depends on: plan review flags it.

## Pass conditions

- Agent-checkable: the package validators pass; the Counsel skill carries the rules of the issue 90 section and no repository rule file does; the planning text, the plan template and the plan-review snippet carry issue 86's behaviour; scenarios 3 and 4 are shown on a fixture where one can be made, and where one cannot the closeout says so plainly.
- Human-only: scenarios 1 and 2 in his next Counsel discussion; whether plans in his next real run were concrete on first draft.

## Left out on purpose

- The both-ways line on matters differing from what the owner believes was agreed. *(told, see Limits)*
- Issues 89, 87 and 88, in that order, after the stack ships. *(told 2026-10-14)*
