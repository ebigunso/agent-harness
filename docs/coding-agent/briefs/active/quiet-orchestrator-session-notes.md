# Quiet Orchestrator session under a brief: discussion notes

Counsel's notes for the discussion opened 2026-10-28, beside the brief of the same stem.

## What the owner saw, 2026-10-28

> Orchestrator session tends to ask questions within its own session unprompted, even under a brief and is handed instructions to load the orchestration-harness skill when being dispatched. The default behavior should be to route questions through Counsel.

After Counsel traced the text:

> I did have a case where the Orchestrator asked for plan approval in its session even under a brief. This should be avoided rather than have that question brought anywhere. Keeping the behavior as is for a run without a Counsel is fine.

## What the plugin text says at 1.1.0, as Counsel read it the same day

- Under a brief, the Carrier section of `value-level-operation.md` sends a value question to Counsel and lists the reserved acts that travel the same way. It also says "Plan approval and its waiver are not carried by relay, and a plan is presented only in this session."
- Three older lines still point at the session and are the ones read first: the role list says the Orchestrator "owns ... user questions"; the replan procedure says "ask at most three questions" for confirmation; the final-response contract keeps a slot for "Questions or blockers, max 3". Goal mode says "surface the question to the user".
- The plan-approval case comes from one sentence in `lifecycle-gates.md`: authorization under a brief is the second source, and "whenever it does not authorize, the paragraph above is the whole rule". The paragraph above is the plan-mode rule, ending in "When in doubt, ask". Any shortfall on the brief route (a review not closed, a verdict in the wrong form, an ask-now) drops the Orchestrator back onto the path that asks in session. It did what the text told it to.

Counsel's read of the root cause, mine, put to him and not contested: the Counsel route is written as an exception for one kind of question instead of as the default for every question while a brief governs; the fix belongs where the default is stated.

## Questions from the run

- 2026-10-29, from the Orchestrator at the plan-draft stage, held as bearing on the design: goal-mode work under a brief. Today the limits of a goal-mode loop (what it may change, its budget, when it must stop) are agreed in the Orchestrator's session, and an earlier decision says a brief does not stand in for that agreement. The brief says nothing is asked in that session. Options put: (a) under a brief such work runs in plan mode; (b) goal mode stays, and agreeing to its limits is the one thing still asked in the session; (c) the limits reach him through Counsel and his relayed answer sets them, which changes what can start a goal-mode run. Brought to him as an experience framing the same day. He asked Counsel's view between (a) and (c) "both from the point of view of user experience, and how that would affect the integrity of work being done"; Counsel recommended (c): plan mode would turn each thing a loop finds into a discovered issue reopening the design, and goal mode's limits, stall detection and checkpoint audits are the integrity instrument for search-shaped work, kept intact under (c) with his explicit word still the agreement, carried as other consent gates are. His answer: "For the first question, I'd take option C then." Written into the brief under Directed during the run and relayed. The plan-draft audit then held the same matter as ask-now, so the plan is not authorized until the brief carries his answer; the verdict's value question, verbatim: "When work the owner handed over through a brief turns out to be search-shaped (its end state checkable but its structure found by iterating), does he agree its goal and boundaries through Counsel before it runs, is such work always planned instead under a brief, or is that the one case where he is asked in the Orchestrator's session?"

## The two edges, and his answers

- Plan approval when the brief route does not authorize: Counsel offered carrying it through Counsel, or his looking in on the session for that case alone. He took neither: the question is not asked anywhere; the route authorizes or the plan is not yet one that can run.
- Runs with no Counsel channel, or on a philosophy alone with no brief: unchanged, by his word above.
