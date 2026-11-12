# Brief: One conversation with Counsel

- status: ratified by ebigunso on 2026-11-12 ("I ratify the "One conversation with Counsel" brief."). He ratified on the experience framings of its decisions, after being shown what is left out and where it departs from the usual answer. Asked before ratifying whether there is anything the work must not do or must ask before doing: "Not at the moment."
- handed to: agent-harness-orchestrator on 2026-11-12
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-11-11 and 2026-11-12
- product basis: it traces to the product philosophy (who it is for; the order of what goes wrong; the line; what it costs in money; what it aspires to). ebigunso owns the harness and is the product owner.
- provenance tags: *(told)* = ebigunso said it; *(agent-proposed)* = Counsel originated it and he accepted it, in discussion or by ratifying this brief; *(inferred)* = Counsel inferred it and he did not object. His quoted words with the date stand beside what he told or accepted.
- kind marks: **gives** (what the work must give; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- The person directing the work can ask for anything at any moment. At any moment the only things waiting are waiting for that person to say something or judge something, or for the machine's own limits. **gives** *(told 2026-11-12: "What I want, is the freedom to ask for anything at any moment, and barring machine capability limits, I am free of bottle necks. The best outcome is where I am the bottle neck, not the machinery.")*
- The pain it starts from: a brief handed over while another run is in progress waits for that run. *(told 2026-11-11: "The pain is the wait before a brief starts.")*
- It is for someone who does not know the mechanics as much as for him: such a person does not choose a role, open a second session, start a seat or repair one. *(told 2026-11-11: "We shouldn't assume everyone would know the difference between the two roles enough to make an informed decision, and you shouldn't underestimate how lazy humans are.")*

## One conversation

- A session opened with no role chosen is Counsel, in every runtime the harness supports and for everyone who installs it. **gives** *(told 2026-11-11: "No, I think we should have Counsel as the default, and ship it for everyone.")*
- Whoever opens a session can still choose either role by what the runtime offers, and every supported runtime offers a way into both. A skill loaded because its description matched never gives a session a role. **gives** *(told 2026-11-11: "These two are usually chosen when a session is opened, so it should be able to support both roles not just one. It should also be able to support a default role, since when no role was explicitly given at session start, the harness still needs to take some kind of role or else there wouldn't be a harness there.")*
- A session that holds the default role says so in its first reply, with how to open the other role. The role a session holds does not change while it lives. **gives** *(agent-proposed 2026-11-11; not yet answered by him)*
- When he ratifies a brief, the run starts without him opening anything. The default role and this ship together, as one change. **gives** *(agent-proposed; Counsel's take, put to him 2026-11-11 as whether the default ships on its own or together with Counsel starting the Orchestrator; accepted 2026-11-11: "Go with your takes on both.")*
- Counsel starts an Orchestrator session for the brief. **means** *(agent-proposed 2026-11-11, accepted with the statement above; a means on his word of 2026-11-12, see Runs side by side)*
- He is not kept waiting by Counsel's own work: while runs start, report and wait, he can speak to Counsel and be answered. **gives** *(agent-proposed 2026-11-12, from "the freedom to ask for anything at any moment"; the consulted model named one Counsel becoming a queue as a way this design could fail him)*
- One Counsel session at a time per repository. **constraint** *(told 2026-11-11: "Probably it's acceptable to have one Counsel at a time, since there's only one person at the helm at a given time")*

## Runs side by side

- A brief ratified while other runs are in progress does not wait for them. **gives** *(told 2026-11-11: "The pain is the wait before a brief starts.")*
- Each run has its own Orchestrator session, and several run at once. **means** *(told 2026-11-11: "probably there could be multiple Orchestrator sessions that handles different work in parallel, commanded by one Counsel session." Asked on 2026-11-12, on the consulted model's advice that the experience be the requirement and the arrangement of sessions stay revisable, whether several Orchestrators are something he cares about or a way to have nothing wait: "A way.")*
- How many runs go at once is the harness's to decide, and by default nothing bounds it. **gives** *(told 2026-11-12: "The harness can decide here, and the default should be unbounded. The most harm it can do is to hit someone's 5 hour token limits, and that I think is an acceptable level of surprise compared to finding out they have no weekly limit left or has eaten up a huge chunk of pay-as-you-go tokens because of a long running expensive model.")*
- The harness may hold part of a run back where running it now would collide with another run or slow all of them. That is its decision and not a question to him; it is not a bound on what the work may cost. **gives** *(inferred from "The harness can decide here"; the consulted model's advice)*
- Runs side by side do not need him to untangle them. What two runs share (numbers, the files every run edits, the stack of pull requests) is settled without him. Each run keeps the other's work intact, a run validates the revision it delivers, and no run silently makes another's finished result wrong. Where two briefs ask for things that cannot both hold, that is shown to him before both results are called ready. **gives** *(agent-proposed 2026-11-12, the outcomes in the third and fourth sentences from the consulted model)*
- He can ratify a brief at any moment. When it is handed over is Counsel's to settle, and he is not asked: a brief that builds on a change another run has not finished is held by Counsel until its work can start. He is told that it is held and what it waits for; no brief waits without his knowing. **gives** *(told 2026-11-12, on Counsel's draft that had him told at hand-over: "I think it's better if I get to approve them anytime and when it gets handed over is handled by Counsel."; that he is told it is held follows from his words under What reaches him)*
- A number that must be unique across runs is taken when the work lands, not while it is drafted. Each Orchestrator states when it takes a brief what its run will touch. **means** *(agent-proposed 2026-11-11)*
- He can ask Counsel at any moment where every brief stands, and Counsel can answer without him looking at any other session. **gives** *(agent-proposed 2026-11-11, as "every Orchestrator report states the status of every brief handed to it")*

## Seats

- Seats are created and destroyed as the work needs, by the session that uses them. **means** *(told 2026-11-11: "I think a seat should be freely spawned and destroyed to allow maximum freedom and parallelism"; a means on the same word of his, "A way.")*
- Nothing depends on a seat surviving. How long a seat lives is not fixed: a session may keep one while it is useful and may end one at any time. **gives** *(agent-proposed 2026-11-12, after two rounds of research into the channel history and session transcripts of this and three other repositories; put to him as the basis to go ahead on; accepted 2026-11-12: "Alright. Now with that information, let's sort out what needs to happen.")*
  - The first dispatch of a unit of work stands alone: a seat that has seen nothing before it can do the work from it and the files it names.
  - A seat that takes over a unit of work part-way is handed where that unit stands: what it is for, what is decided and on whose word, what is done and at which revision, what remains, what is still open, and what may already have been done outside the repository. It neither repeats an act already performed nor undoes a decision already made. That the earlier messages are stored somewhere is not enough. *(the list is the consulted model's)*
  - What is known about the obstacles of the machine the work runs on reaches every new seat and every new Orchestrator session when it starts, and an obstacle one seat has got past is not paid for again by the next. Each such thing says where it applies and when it was last seen, so that it is checked again and not trusted for ever. *(his question of 2026-11-12 is what brought this in: "how much did prior context help in working around or diagnosing persistent environment related issues")*
- A session holds one identity on the peer channel, given when it is created and not changed after. Reading another seat's messages never requires holding that seat's identity. **gives** *(agent-proposed 2026-11-11, from his account that day of a session that "had many roles held")*
- What is known about a machine's obstacles is kept where it does not reach the remote. **constraint** *(inferred from his standing rule that nothing specific to a machine is in any file that reaches the remote)*
- Two peer seats are never shared between two Orchestrators in the middle of a run. **means** *(agent-proposed 2026-11-11)*

## What reaches him

- When something becomes ready for him he is told that it is there: what it is and what it holds up, briefly, and not put to him in full. It then waits, and he takes things up in the order and at the pace he chooses. Nothing is held without his knowing it is there, and Counsel can always tell him everything that is waiting on him and which item holds up the most work. **gives** *(told 2026-11-12, offered each item reaching him as it is ready against its being held for him: "Yes, I think it's better to leave the choice of order to me rather than having to constantly switch tasks."; and on Counsel's scenario in which nothing was said until he asked: "I think it's better if I get to know what is waiting, so I can choose to pick it up at my own pace, rather than be silently held and never know it's there.")*
- A decision of his is given once. A run started by Counsel acts on his word as Counsel relays it and asks him for it nowhere else. **gives** *(agent-proposed 2026-11-12)*
- A session started by Counsel does not stop to ask him for permission in its own window. It works within what he has already allowed for the repository, and anything outside that reaches him as a question through Counsel. **gives** *(agent-proposed 2026-11-12; accepted 2026-11-12: "Yes, but the reality may be that other sessions would require manual input or "manual-ish" input directly in it's chat box to get around automatic permission checks.")*
- Where a runtime's own permission check can be satisfied only by input in that session's window, that input is the backup and not the default: it carries his word and nothing else, the work keeps such cases as few as the runtime allows, and the closeout says plainly which remain and what he has to do for each. No check a runtime makes for safety is defeated to avoid it. **constraint** *(inferred from his words above; the last sentence is Counsel's)*
- He does not have to notice that a run or a seat has stopped. A run that has stopped making progress is found without him, told apart from one that is working long or rightly waiting, and either recovers within a stated limit or reaches him through Counsel as a clear report. It is never restarted over and over. **gives** *(agent-proposed 2026-11-12, after he twice that day had to say that something had stopped; the limit on recovery is the consulted model's)*

## Limits

- What waits for him today still waits for him: ratifying a brief, accepting a decision record by name, a merge, a change to a philosophy, a standing approval, and anything that cannot be undone or that reaches outside. **constraint** *(his standing rules; the product philosophy's line)*
- This changes two decision records, which are replaced by records he accepts by name: that a session's role is entered only by an explicit act of the person opening it (ADR-D-0037), and that a session routed by the loader assumes the Orchestrator role (ADR-D-0020). **constraint** *(inferred from the above)*
- It changes two standing rules of his, and only as far as this brief says: that Counsel starts and prompts no peer, and that no new seat is started for a dispatch. **constraint** *(inferred from his words on seats and on Counsel starting the Orchestrator)*
- When the machine's limit for a period is reached, everything stops until it resets, his conversation with Counsel included. That is accepted. **constraint** *(inferred from "barring machine capability limits" and his words on the five-hour limit, 2026-11-12)*

## Core scenarios

Agent-proposed; ratified with the brief. Scenarios 4 and 8 were changed on his words of 2026-11-12 before ratification.

1. Someone installs the harness, opens a session and types what they want. They are talking to Counsel, are told so in the first reply with how to open the other role, and never open another session.
2. He ratifies a brief. A run starts without him opening anything, and he goes on talking to Counsel.
3. While that run is going he ratifies a second brief that touches other things. Its work begins at once, and neither run waits on the other.
4. Three runs have things ready for him while he is discussing something else. He is told in a line each that they are there and what each holds up, and the discussion goes on. He takes them up later, in his own order; when he asks, he is told everything that is waiting and which holds up the most work.
5. An Orchestrator starts a new seat for a new unit of work, and replaces a seat part-way through another. Each does the work without asking what an earlier seat knew, and neither trips over something the machine is already known to do.
6. A run stops making progress. He hears of it from Counsel without having looked, or it resumes without him.
7. He accepts a pull request by name in his conversation with Counsel. It merges, and he is asked nowhere else.
8. He ratifies a brief that builds on a change another run has not finished. He is not asked when to start it: Counsel holds it, tells him it is held and for what, and hands it over when its work can start.
9. He asks Counsel something unrelated while two runs are starting and a third is reporting. He is answered as promptly as when nothing is running.

## Pass conditions

- Agent-checkable: the package validators pass; scenarios 1, 2, 3, 5 and 8 are shown where one can be made, and where one cannot the closeout says so plainly; no line of the plugin's text makes a result depend on a seat having seen an earlier unit of work.
- Human-only: the next two briefs he hands over close together both start without him opening a session; over those two runs he opens no Orchestrator session, starts or repairs no seat, and is not the one who notices a stop.

## Left out on purpose

- More than one Counsel session at a time. *(told 2026-11-11, see above)*
- How money is handled in a goal run. It is open with him as a matter of the product philosophy. *(told 2026-11-12: "How to handle this should be considered further.")*
- Holding back part of the machine's limit so that his conversation survives when runs reach it. *(inferred; he excepted the machine's limits)*
- How long a new seat takes to find its way in an area, and what that costs in money. The logs could not answer it; it is watched in the first runs under this brief. *(agent-proposed 2026-11-12)*
