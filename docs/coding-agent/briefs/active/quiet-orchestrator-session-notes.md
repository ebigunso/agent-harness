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

## Counsel's first read of the result, 2026-10-29

Written before any part of the closeout audit's verdict was seen; facts from the Orchestrator's note reporting pull request 93 ready.

- Against "the owner never needs to look at the Orchestrator's session": the note states the session asks him nothing under a brief, every question of any kind comes to Counsel, and the final response names what is with Counsel and phrases nothing as a question. Matches the brief's first and second gives.
- Against "a plan is never presented for approval, anywhere; three moves and no fourth": the note states exactly the three moves (correct input and audit again; send Counsel the value question; end blocked naming what failed) and that no plan is presented in the session or through Counsel. Matches.
- Against the amendment of 2026-10-29 on goal mode: the note states goal-mode work under a brief runs with its limits reaching him through Counsel and his relayed agreement starting the loop. Matches option (c) as he gave it.
- Against the constraint "runs without a brief unchanged": the note says so. Matches.
- One statement in the note goes beyond the brief's words while staying inside its first give: something only he can give (a credential, a permission) now comes to Counsel to bring to him rather than back to the session. Counsel reads it as a consequence of "every question, of any kind"; whether the audit marks it as bearing on direction is for the material after this read.
- Four decision records are proposed where the plan named two (ADR-D-0062 new; ADR-D-0063 replacing 0056); ADR-D-0064 and ADR-D-0065 replace 0040 and 0041 because those state the old plan-approval route. Each goes to him for acceptance by name with its path; the Orchestrator's two remarks (the goal-mode route worded differently in 0063 and 0064; whether ADR-D-0051 is reopened) go to him with them.
- Pass conditions: the note says fixtures were shown and names his next real run under a brief as the human-only check, which is what the brief states.
- The value document changed during the run is the brief's section Directed during the run at cbf2c9f, which Counsel wrote; confirmed as Counsel's.

Finished after the closeout audit's material arrived (verdict of 2026-10-28, as the Orchestrator sent it):

- Two items marked as bearing on direction, both inferred or implied rather than stated by him. JC-2: a goal run under a brief is a goal-mode run plus the Carrier, not a unit of the brief's run, so it is structured, reported and judged on goal mode's own terms (its completion report) and not through the run's "candidate ready". JC-4: in a repository with no philosophy, this one included, a goal run under a brief applies the documents, Asking The Owner and the Carrier only, and no value audit runs, so such work is never graded against the brief; this keeps the state before the range (the audit in goal mode only "in a repository that has a philosophy"). Both go to him as experience framings; the second is the consequence of his own answer (c) joined to the brief's constraint that the audit's grading is unchanged, and Counsel's read is that he should decide whether that consequence is what he wants, since his repository has no philosophy. Put to him 2026-10-29 as the experience of a goal run under a brief here, agreed through Counsel and judged by the assessor alone; his answer: "The goal mode point is covered by my previous answer, it is an acceptable limit." The consequence stands; the brief's constraint is unchanged.
- Inferred items: the version bump to 1.2.0 across the plugin and marketplace files, read as extending the human-only pass condition (an installed plugin receives the change only when its version changes). Cheap to undo; nothing to confirm beyond telling him.
- The credential-or-permission statement was graded cited against "Whatever needs him, of any kind, reaches him through Counsel", on both Counsel's receiving side and the Orchestrator's; it widens what reaches him and moves no decider. Counsel's read stands: inside the first give.
- Nothing let through on a provisional statement.

## From the Copilot review of pull request 93, 2026-10-29

Three findings the Orchestrator reported while the run is open and reported ready; nothing changed without his direction. (1) A value question: when a run needs a credential only he holds, the new text has that need come through Counsel and his answers are written into the brief and the run's records, which are published. Options put: (a) he provides the secret outside the conversation, in the environment or a secret store, and only "provided" comes back to the run; (b) he hands it over through Counsel as any other answer. (2) For information: the goal-mode limits line admits only his relayed answer, while without a peer channel his answers already reach the session as his own statement; the fix accepts either admitted form. (3) For information: for a goal-mode run under a brief in a repository with a philosophy, the audit's dispatch wording contradicts itself on whether the brief is named; the fix is one line in the mandate. His direction of 2026-10-23 on Copilot comments was for that run; whether it applies here is his. Brought to him the same day. His answers, 2026-10-29: on (1), "The sensible way to hand secrets over is to have them in a file and point to that file. But I don't think it's necessary to define this in the harness. It is up to whoever encounters the situation to choose." On (2) and (3), "For the goal mode points, those are acceptable limits so it is fine as is." Written into the brief under Directed during the run as constraints and relayed. He said nothing on resolving the review threads; Counsel's read, mine, is that the previous run's direction was for that run and has not been extended to this one.

## The two edges, and his answers

- Plan approval when the brief route does not authorize: Counsel offered carrying it through Counsel, or his looking in on the session for that case alone. He took neither: the question is not asked anywhere; the route authorizes or the plan is not yet one that can run.
- Runs with no Counsel channel, or on a philosophy alone with no brief: unchanged, by his word above.
