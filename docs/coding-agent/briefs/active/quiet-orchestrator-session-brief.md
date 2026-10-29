# Brief: A quiet Orchestrator session under a brief

- status: ratified by ebigunso on 2026-10-29 ("I ratify both briefs, hand them over now."). Asked before ratifying whether there is anything the work must not do or must ask before doing, he added nothing.
- handed to: agent-harness-orchestrator on 2026-10-29
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-10-28 and 2026-10-29
- product basis: the product owner's own words in this brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(agent-proposed)* = Counsel originated it and he accepted it. His quoted words with the date stand beside each.
- kind marks: **gives** (what the work must give him; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- While a run under a ratified brief is in progress, the owner never needs to look at the Orchestrator's session. Whatever needs him, of any kind, reaches him through Counsel, and the Orchestrator's final response names what is with Counsel instead of asking him. **gives** *(told 2026-10-28: "Orchestrator session tends to ask questions within its own session unprompted, even under a brief and is handed instructions to load the orchestration-harness skill when being dispatched. The default behavior should be to route questions through Counsel.")*
- The case he saw: the Orchestrator asked for plan approval in its own session under a brief. *(told 2026-10-28: "I did have a case where the Orchestrator asked for plan approval in its session even under a brief.")*
- What Counsel found and he did not contest: the text sends only a value question to Counsel and leaves three older lines pointing at the session ("owns user questions", "ask at most three questions", "questions or blockers, max 3"); and when the brief route does not authorize a plan, one sentence in the lifecycle gates returns the Orchestrator to the plan-mode rule, which ends in "When in doubt, ask". The notes beside this brief hold the trace.

## What the plugin states

- Under a ratified brief, a plan is never presented to the owner for approval, in this session or through Counsel. It is authorized by the brief route or it is not yet a plan that can run. When the route does not authorize, the Orchestrator has three moves and no fourth: correct its own input and dispatch the audit again; carry the verdict's value question to Counsel as the Carrier states; or end the turn blocked, naming which condition of the route failed. The plan-mode rule's asking applies only to work no brief governs. **gives** *(told 2026-10-28, offered the choice of carrying the approval question through Counsel or looking in on the session for that case: "This should be avoided rather than have that question brought anywhere.")*
- Under a brief, every question that needs the owner, whatever its kind, travels by the Carrier. The Orchestrator's session puts no question to the owner, and its final response names what is with Counsel and what the turn ended blocked on, in place of questions. **gives** *(told 2026-10-28, see above)*
- The lines that today point at the session are read, under a brief, as pointing at the Carrier or at the blocked report: the Orchestrator's ownership of user questions is ownership of taking them to Counsel; the replan procedure's confirmation questions go by the Carrier, as the Carrier already lists; the final-response slot for questions holds what is with Counsel; goal mode's "surface the question" surfaces it by the Carrier. **means** *(agent-proposed 2026-10-28, as the root cause: the Counsel route is written as an exception for one kind of question instead of as the default for every question while a brief governs, so the fix belongs where the default is stated; he did not contest it)*
- A brief, a hand-over or a dispatch instruction arriving as a message in the Orchestrator's session does not make the owner present there for questions; anyone may still talk to the session directly, and a question is answered where it was asked. **means** *(agent-proposed 2026-10-29, from his first words: the session is "handed instructions to load the orchestration-harness skill when being dispatched" and still asked in session)*
- A run without Counsel, on a philosophy alone or with no brief, is unchanged: the run's own mode applies and the user is asked in that session. **constraint** *(told 2026-10-28: "Keeping the behavior as is for a run without a Counsel is fine.")*

## Directed during the run

- Work handed over through a brief that turns out to be search-shaped, its end state checkable but its structure found by iterating, may run in goal mode under the brief. Its goal and limits (what it may change, its budget, when it must stop) reach the owner through Counsel like every other question, and his relayed answer agreeing to them is what starts the loop; the brief itself still does not stand in for that agreement. This changes what can start a goal-mode run, and the earlier record stating that only an agreement in the Orchestrator's session starts one is revised accordingly. **gives** *(told 2026-10-29, answering the plan-draft audit's ask-now, put to him as three experiences, (a) plan mode under a brief, (b) the one question still asked in the session, (c) limits through Counsel: "For the first question, I'd take option C then.")*
- How a credential or other input only the owner holds is handed to a run is not defined by the harness; whoever meets the situation chooses. **constraint** *(told 2026-10-29, answering the Copilot review's first finding on pull request 93, put to him as (a) provided outside the conversation with only "provided" returning, (b) handed over through Counsel: "The sensible way to hand secrets over is to have them in a file and point to that file. But I don't think it's necessary to define this in the harness. It is up to whoever encounters the situation to choose.")*
- The goal-mode limits line admitting only the relayed answer, and the audit mandate's dispatch wording for a goal run under a brief in a repository with a philosophy, stay as written. **constraint** *(told 2026-10-29, answering the Copilot review's second and third findings: "For the goal mode points, those are acceptable limits so it is fine as is.")*

## Limits

- No new carrier and no new kind of message is added; what exists (the Carrier, the blocked report, the open question in the discussion notes where no channel exists) carries everything, the goal-mode limits of Directed during the run included. **constraint** *(agent-proposed; follows from the above)*
- Nothing here changes what the audit grades or what authorizes a plan under a brief. **constraint** *(agent-proposed; the brief route stays as ADR-D-0051 and the lifecycle gates state it)*

## Core scenarios

Agent-proposed; ratified with the brief.

1. A plan under a brief fails the route because the review left a finding open: the Orchestrator closes the review and audits again, or ends blocked naming the open finding; no approval question appears anywhere.
2. A plan under a brief draws an ask-now: the value question goes to Counsel; the owner never sees the plan.
3. The replan procedure meets an outward-facing change under a brief: the confirmation goes by the Carrier, and the session shows no question.
4. A run on a philosophy alone, no brief: the plan is presented in session and the user asked there, as today.
5. The final response of a run under a brief: it names what is with Counsel and nothing is phrased as a question to the reader.

## Pass conditions

- Agent-checkable: the package validators pass; the plugin text contains no line that, under a brief, asks the user in the Orchestrator's session, the lifecycle-gates fallback included; the three moves when the route does not authorize are stated once, where the route is; scenarios 1, 2 and 5 are shown where one can be made, and where one cannot the closeout says so plainly.
- Human-only: his next run under a brief in this repository ends with nothing asked of him in the Orchestrator's session.

## Left out on purpose

- Carrying plan approval through Counsel. *(told 2026-10-28, see What the plugin states)*
- Any change to runs without Counsel. *(told 2026-10-28)*
