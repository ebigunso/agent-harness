# Brief: Design-led long runs

- status: ratified by ebigunso on 2026-10-04 ("I ratify the brief, hand it to the Orchestrator.")
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-10-04
- handed to: agent-harness-orchestrator
- product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(inferred)* = Counsel inferred it and he did not object; *(agent-proposed)* = Counsel originated it and he accepted it. For anything told or accepted, his quoted words with the date stand beside the statement.
- three parts of this file went beyond the text he had read in chat when he ratified it: the statement on writing a philosophy where none exists, the pass conditions as marked, and the Limits line carrying his earlier rulings over to this run. Counsel put them to him and he confirmed them on 2026-10-04: "Items 2 and 3 from before are fine to proceed as proposed." (item 3 being those three parts).
- kind marks: each statement is marked **gives** (what the work must give him; it binds), **constraint** (fixed regardless), or **means** (a way settled in discussion to get what a gives-statement asks for; the run builds from it and may better it, and a better means is a design-level finding that reaches him).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- You bring an idea to Counsel and arrive at a design you're comfortable with. **gives** *(told 2026-10-04: "I can throw ideas at the Counsel session, discuss them against the philosophy and the repository's shape at the time, to arrive on a design I'm comfortable with. This includes you advising on things I missed, or things that could potentially make the design better than what I describe.")*
- Where no philosophy document exists, you can write one through extensive discussion with Counsel. **gives** *(told 2026-10-04: "When no philosophy document exists, be able to write them through extensive discussions with the Counsel session.")*
- You let the work go and come back to an implementation that matches the design and fits the philosophy's direction. **gives** *(told 2026-10-04: "I can let work be dispatched for what designs were decided, and I get back an implementation that matches what was designed and is consistent with the philosophy's direction.")*
- You build larger features faster, for yourself and whoever uses what was built. **gives** *(told 2026-10-04: "With all these, I expect to be able to more quickly build larger scale features and improvements to whatever I'm building, ultimately benefitting me and anyone else that uses what was built.")*

## What a design is

- A design is the experience someone gains from a feature. It may be only a desired behaviour, which is open-ended, and may include a UI design. **gives** *(told 2026-10-04: "A design is, I think, often the experience one gains by introducing a feature. This could just be a desired behavior, which probably leans more towards an open ended goal, and sometimes includes a UI design that an experience is heavily influenced by.")*
- A design lives in the brief; no formal design document is written before the work. **gives** *(told 2026-10-04: "I agree with your take that the design should go along with the rest of the brief. When a work starts, it's usually just a rough idea of what it would look like in the end, so writing a formal document out of that would possibly result in things needing to be invented or intentionally kept open, which is not ideal.")*
- A statement in a brief may describe a mechanism where the mechanism is what you care about. Counsel says so when a statement would constrain the shape of the implementation prematurely, and the choice stays yours. **gives** *(told 2026-10-04: "I've gone into the mechanisms more than what I first imagined I would for any design, but that itself I feel isn't all wrong in itself. If I go too far into implementation details to an extent that it would constrain the shape of implementation prematurely, then that should be corrected, but what we now have I don't think doesn't cross that line.")*
- Each statement in a brief is marked as something the work must give, a constraint, or a means. The mark is on the statement, not a layout: a brief keeps whatever sections state its concept best, and a means stays beside the thing it serves. **gives** *(agent-proposed; he took the split and corrected its form 2026-10-04: "The split between the deliverables and the means seems like a good idea, but how you dropped the categorizations you previously gave makes me concerned that enforcing that shape would drop some context that would otherwise have survived." and, of the version with sections restored and each statement marked, "Great. This one looks much better.")*
- A few core scenarios are defined beforehand by you with Counsel, and are ratified with the brief. **gives** *(told 2026-10-04: "Scenarios I think do fit in with how a design can be verified, but if that is to become something to measure against, it's probably good practice to discuss and define a few core scenarios beforehand in a Counsel session, rather than having every scenario be derived from the given goals or designs.")*
  - The run may add scenarios of its own; those are its reading of the design. **means** *(inferred)*
  - Scenarios are evidence of the experience, not its definition: a run that satisfies every listed scenario and misses the experience has not delivered the design. **means** *(agent-proposed, accepted with the brief)*

## Counsel discussions

- A philosophy says what you ratified; it need not be in your wording. What Counsel originated is marked as such, and nothing counts until you ratify it. The form's rule that a philosophy's statements keep the owner's wording changes accordingly. **gives** *(told 2026-10-04: "'in your wording' is a bit too constraining, so that can be dropped." and, asked whether the form's rule should change too, "Yes, change the requirements in the form as well.")*

## The run

- One design is carried over as many plans as it takes, without you. **gives** *(told 2026-10-04, in the same words as the third statement of the first section, and: "I expect to be able to more quickly build larger scale features")*
- What this brief gives does not depend on how many plans a design turns out to need: a design that takes one plan is kept to your values as it goes, brings you a better design it notices, and is reported scenario by scenario, like one that takes several. **gives** *(amendment 2026-10-04. The plan-draft audit held a planner-added line that a run of a single plan under a brief behaves as before, and asked: "when a design you hand over turns out to need only one plan, should that work still keep itself to your values as it goes, bring you a better design it notices, and report back scenario by scenario, or should it run as work does today, with those things arriving only when a design takes several plans?" Counsel suggested the first, since how many plans a design takes is the Orchestrator's business and not his. His answer: "The new question, I feel the same as your take so I'll take your suggestion that the number of plans doesn't matter.")*
- You look only when it is done, or when something is off and needs you. **gives** *(told 2026-10-04: "About when to judge, ideally I'd only have to look at it when it's done, or something is off and needs my attention.")*
- A run that has stopped getting closer to the design stops and tells you; it does not grind on. **gives** *(inferred, from the line above and from how goal mode already ends a loop)*
  - Demonstrated scenarios are what a run counts toward the design; scenarios only you can judge end as ready for your judgement. **means** *(agent-proposed, accepted with the brief)*

## Keeping to the philosophy without you

- You do not have to think about what the Orchestrator is doing. The run keeps itself to your values and corrects itself while the work is ongoing, and you hear only when it could not. **gives** *(told 2026-10-04: "The way we built it makes reviews responsible for this, which is an enforcement mechanism. I'm concerned that this might lead to the Orchestrator thread to care less about the philosophy and just do whatever the review audits pointed out while it is doing its work, since the responsibility is arguably not theirs anymore."; "it's both the responsibility argument and the attention drift."; and "In the final version, I shouldn't be concerned with what the Orchestrator is doing, the mechanism should let me trust the work by default. What we're trying to deal with here is something that can break that trust, and the fix needs to be something that automatically happens while the work is ongoing, that I don't have to think about.")*
  - Before each audit the Orchestrator commits its own reading of which items the value documents cover, which extend them, and which need you; the audit, not the Orchestrator, compares that reading with its own grades; a divergence is corrected inside the run, the Orchestrator going back to the philosophy and the brief, re-deriving what the work is for and redoing the item. **means** *(agent-proposed; 2026-10-04: "Yes, mostly." and, to the version without a context refresh, "Okay I agree with you.")*
  - A divergence that was caught and fixed promptly is the audit doing its job and is no reason to stop, however often it happens. The work stops, for the affected part, when it depends on a decision worthy of the philosophy and what you supplied does not cover it nearly enough to settle it without you. **gives** *(amendment 2026-10-04, replacing the earlier means that a divergence which repeats stops the affected part. The plan defined a repeat as the same item at two audits in a row; Counsel suggested any divergence at two audits in a row. He took neither: "a divergence that was caught and fixed promptly would probably be fine, that is the audit doing its job. When to stop, probably is when a work depends on a philosophy worthy decision, but what is supplied does not cover it nearly enough to settle them autonomously.")*
- Keeping to the philosophy is not limited to work that carries a design in a brief. Work that runs under a philosophy with no brief also keeps itself to your values as it goes and corrects itself before you hear of it. **gives** *(amendment 2026-10-04. The plan-draft audit held a planner-added line that a run with no brief behaves as before, and asked: "when work runs under your philosophy with no brief, should it also keep itself to your values as it goes and correct itself before you hear of it, as work under a brief will, or should that come only with work that carries a design in a brief?" Counsel suggested the first. His answer: "I take the first. Philosophy adherence is critical whatever the type of work it is.")*
- The Orchestrator's working context is not refreshed as a remedy for drift. **constraint** *(told 2026-10-04: "a full context refresh is probably an unnecessarily aggressive measure. Preserving context of work is usually vital to its ultimate success, so if it doesn't have to happen then all the better.")*

## A better design noticed mid-flight

- Anything noticed during the work that suggests a better design exists is reported. It reaches you if it bears on the design, whatever it would cost to act on; a trivial one never does, however cheap. **gives** *(told 2026-10-04: "Anything that was noticed midflight that suggests a better design existing, is also reported." and "I'd like to not have the cost of change be a measure of if the finding reaches me or not. Some findings could lead to costly changes but ultimately arrive on a better design. I'd like to keep the option open to take that expensive path too. The alternative is true too, where it could be cheap to change something early on, but that change is trivial enough that it shouldn't cost my attention at all.")*
  - While you decide, the part the finding concerns waits and the rest of the run continues, so that the expensive path does not grow more expensive. **means** *(agent-proposed; confirmed 2026-10-04: "Yes I confirm both of your readings.")*
- A plan that departs from a means stated in a brief is such a finding, not a breach. **gives** *(agent-proposed, accepted with the brief)*

## Roles and models

- You can choose a model suited to each kind of work, and are not forced onto your strongest model for everything because one responsibility needs it. **gives** *(told 2026-10-04: "The reviewer role seems too overloaded now with the value audit added as it's new responsibility. Splitting roles by its nature seems like something we should now consider, so that I may choose appropriate models to run each on, rather than being forced into using the best model I have due to one of the responsibilities requiring that capability.")*
  - Roles are split by the nature of their work. A separate role, the Auditor, holds independent judgement of the Orchestrator's work: the value audit and goal-mode assessment. The Reviewer keeps checking the work for the Orchestrator. **means** *(agent-proposed; accepted 2026-10-04: "Yes, add it to the brief, Auditor is fine.")*
  - A dispatch to the Auditor carries locations only; an account of the work in it is misuse on sight. **constraint** *(from the accepted record on the value audit)*

## Closeout

- It leads with behaviour, scenario by scenario, with how to observe each. **gives** *(inferred, from the earlier brief's closeout and from the scenarios being what he judges)*
  - The durable design document for the field the work touched is updated at closeout. The rules for what goes into such documents wait for the engineering philosophy; he does not read them himself. **means** *(agent-proposed; confirmed 2026-10-04: "Yes I confirm both of your readings."; and: "Design documents on the level I described, are something closer to the implementation than what I'd like to review myself. So, I probably won't be reading them.")*

## Limits

- The work stacks on pull requests 72, 73 and 75, and nothing merges until you have judged the whole stack. **constraint** *(told 2026-10-03: "I actually want to build on the longer horizon mechanism on top of the current stack, before we test the current version, which I feel is incomplete without it rather than being a smaller complete set.")*
- Goal mode for goals a check can decide keeps working as it does today. **constraint** *(inferred)*
- Everything he has ruled for the earlier brief still holds for this run: changes reach the remote only after review; each decision record is accepted by him by name; his word reaches the Orchestrator through Counsel's quoted relay; irreversible or outward-facing actions stop for him unless a standing approval in effect covers them. **constraint** *(inferred; each is in an accepted record or rule)*

## Core scenarios

Ratified with the brief. Each is an experience of his.

On the run *(2026-10-04: "The scenarios you gave are fine as is.")*:

1. You hand over a behaviour-only design that takes several plans. You come back to it built, having been asked nothing that did not need you.
2. A design-level finding reaches you mid-run, and the part it concerns has waited.
3. A run that has stopped getting closer has stopped and told you.
4. You put a cheaper model on the Reviewer and your strongest on the Auditor, and the run works as before.

On a Counsel discussion *(2026-10-04: "'in your wording' is a bit too constraining, so that can be dropped. The last two scenarios you gave can be omitted. I feel they are less important than the others. Other ones, I'll take as an accepted scenario.")*:

5. Starting from nothing. You open a Counsel session in a repository with no philosophy. After talking it through at length you hold a philosophy that says what you mean, and at no point did it feel like filling in a form.
6. Bringing an idea. You bring a rough idea. Counsel restates it as a person's experience so you can check it, weighs it against the philosophy and the repository as it stands, and where it sees something you missed or a better way it says so, naming the conventional answer. You end with a design you're comfortable with.
7. Unfamiliar ground. You are about to judge something you don't know well. Counsel explains what you need to know first, and only then asks.
8. Going too far. You describe an implementation detail that would constrain the build prematurely. Counsel says so before it is written down, and the choice stays yours.
9. Closing. Before you ratify, Counsel shows you what was discussed but left out and why, writes the watch list with you, and takes nothing as settled that you haven't said yes to in whole.

## Pass conditions

- Agent-checkable: the package validators pass; the role map states the Auditor and its home; goal mode's behaviour for goals a check can decide is unchanged; every decision record the run proposes is accepted by him by name before it lands; nothing merges before he has judged the stack; scenarios 1 to 4 are demonstrated by a run where one can be made, and where one cannot the closeout says so plainly.
- Human-only: scenarios 5 to 9, judged by him in his first use of a Counsel session opened from the built plugin; scenarios 1 to 4 where no run could demonstrate them; and whether he could trust the result by default, without having thought about what the Orchestrator was doing.

## Watch list

Written with him and ratified with the brief *(2026-10-04: "And the other two parts, seems fine to me.")*. He would want to hear at once of:

- anything that would have him reading plans again;
- a change to goal mode's admission test, loop, stall rule or completion rule;
- anything that lets work start, continue or merge with less say from him than today.

*(amendment 2026-10-04. The second and third entries first read "a change to how goal mode behaves today" and "anything that weakens who may authorize or stop work". Those were Counsel's wording and proved too broad: across three audits of one plan they fired on every line that touched goal mode or stopping, lines that say nothing changes included. Counsel proposed the narrower entries above and he took them: "Items 2 and 3 from before are fine to proceed as proposed." (item 2 being this narrowing).)*

## Left out on purpose

Each drop confirmed by him on 2026-10-04 by the same words as the watch list, and each kept for a later discussion:

- the rules for durable design documents;
- enforcing Counsel's limits by tool settings where a runtime allows;
- how a decision he delegates to Counsel is recorded in a brief;
- a product philosophy and an engineering philosophy for this repository;
- the delivery failures between the two sessions, which he holds to be a matter for the delivery mechanism.
