# Scenarios shown

Findings of Task_8 of the plan `one-conversation-with-counsel-plan.md`: scenarios 1, 2, 3, 5 and 8 of the brief, the first time in a repository, and the census of the plugin's text.

The text under trial is the plugin as this branch has it at revision 6c03154. No file under the plugin has changed since revision 07dde0d, so what `one-conversation-with-counsel-mechanisms.md` says of the text after 07dde0d holds for this revision too.

The trials ran on 2026-11-13 between about 18:55Z and 19:05Z, which is 2026-11-14 by the local calendar the trial's made-up words carry. Versions: Claude Code 2.1.323 (terminal CLI, Windows), Codex CLI 0.169.0. The harness plugin installed for both runtimes was version 1.5.0, which does not hold this branch's text; a Claude Code session ran on this branch's text only when it was started with the runtime's plugin-directory option naming this branch's plugin. One model per runtime, each result seen once unless a count is given.

Every ratification, acceptance and answer carried in these trials was a stand-in: made-up words, marked in each message as a trial with nobody's authority, naming the throwaway repository, and sent only to the trial's own sessions. They are nobody's word. Nothing in this repository was ratified, accepted or changed by them, and the repositories they named are removed.

Each fact is marked **observed** (seen in a trial here), **cited** (recorded elsewhere, with where), or **untried**.

## The line for each

- Scenario 1: **shown in part**. Shown: a session with no role chosen is Counsel and is told so in the first reply with how to open the other role, in Claude Code (a non-interactive run, this branch's plugin at 6c03154, no agent named) and in Codex (an ephemeral non-interactive run, the default-role block copied from the template at 6c03154, the installed plugin 1.5.0). Not shown: that the person never opens another session. The Claude Code trial forbade starting any session, so it did not reach a build without another window, and in Codex the session told the person to open a new one for the build. Also not shown: an interactive session in either runtime; Copilot.
- Scenario 2: **shown in part**, in Claude Code, once, with a stand-in for the person. Shown: a session with no agent named was Counsel, and on the stand-in ratification it started an Orchestrator session by the recorded means and carried the ratification to it, without the person opening anything. Not shown: that he goes on talking to Counsel while the run goes, which was not tried; and a run on this branch's text, since the started Orchestrator session ran on the installed plugin 1.5.0 and not the branch's. The run it started built nothing, because the trial forbade subagents.
- Scenario 3: **shown in part** in Claude Code, once. The second brief's session was started at once while the first run was unfinished. Its ratification did not reach a working session: the continuation made a copy that never took a turn. Neither run built anything.
- Scenario 8: **shown** for the holding and the telling, in Claude Code, once. Not reached: the hand-over when the work can start.
- Scenario 5: **shown in part**, by cases this run itself supplied (cited from the plan's Progress Log) and by this task's own dispatch. All were subagents, not peer seats; no dispatch text is in the plan to read.
- The first time in a repository: **not made again**. The trials of 2026-11-13 stand; the text as it now stands was changed after them and its changed sentences are untried. One step of it stays unmet where the runtime refuses the write.
- The census: **no line found** that makes a result depend on a seat having seen an earlier unit of work. 262 hit lines read; the nearest misses are listed.

## Scenario 1: a session with no role chosen

The brief's words: "Someone installs the harness, opens a session and types what they want. They are talking to Counsel, are told so in the first reply with how to open the other role, and never open another session."

### Claude Code

- Tried: `claude -p --plugin-dir <this branch's plugin> --output-format stream-json --verbose "<message>"`, with no agent named and standard input closed. The message was a plain wish ("I would like my notes program to be able to export the notes as a PDF. Where do we start?") followed by one sentence of trial conditions: use no peer-messaging tool, write no file, start no session, dispatch no subagent.
- Observed: the session loaded the Counsel skill from this branch's plugin, read the Repository Reference Documents section of the rule file, and replied once. The reply began: "This session is Counsel: we talk about what the product should do, and I record what you ratify as the grounds for building it. Building happens in a separate Orchestrator session, opened with `claude --agent coding-agent-orchestration-harness:harness-orchestrator`." It then restated the wish, asked what the export is for as three experiences, gave the conventional answer, and ended "Nothing was written to any document in this session." It did not load the Orchestrator skill and changed nothing. (**observed**, 1 of 1)
- The background session of scenario 2, started the same way with no agent named, showed the plugin's Counsel agent in its header, and its first reply began "This session is Counsel. The Orchestrator role is a separate session, opened with `claude --agent coding-agent-orchestration-harness:harness-orchestrator`; you do not need to open one for this brief." (**observed**)
- How to observe it: run the command above from a folder trusted in Claude Code and read the first assistant text in the output.
- Untried: an interactive terminal session opened by a person, the desktop app and the IDE extensions (as in the mechanisms file); a person who has the released plugin installed and not this branch's, since the released Counsel text has no such sentence.

### Codex

- Tried: a throwaway git repository with one small source file and an `AGENTS.md` holding the Codex form of the Default Role Block, extracted by script from `rule-suite-templates.md` at 6c03154 and nothing else. One run: `codex exec --ephemeral --sandbox read-only -C <the repository> "<message>"`, the message a plain coding request naming no role ("I would like this greeter to be able to greet in Spanish too. Please add that."). The Codex home's own instruction file held, unchanged, the earlier loader block that routes coding tasks to the Orchestrator skill.
- Observed: the first message of the turn said "This session is Counsel under the repository instructions; an Orchestrator session starts with a first message invoking `$orchestration-harness`." The session read the installed Counsel skill, then the installed Orchestrator skill's file, the source file and the Counsel first-session reference, changed nothing, and ended: "Spanish support is not added yet. This session is Counsel", telling the person to open a new session with `$orchestration-harness` and the request, and that harness setup is missing. (**observed**, 1 of 1) This time the closing message said the session is Counsel as well; on 2026-11-13 only the first message did.
- This agrees with the five of five runs of 2026-11-13 on CLI 0.167.2 (**cited**: the mechanisms file, The default in a set-up repository: Codex). The block's words are the same as then; what is new is the CLI version and that the block came from the template.
- The trial's message did not tell this session to use no peer-messaging tool. Its output was read through: it ran no such tool, and the Codex home's configuration file was the same after the run as before. (**observed**)
- Not shown: "never open another session". The installed Counsel text has no way to start a run, so the Codex session sent the person to a new session for the build. This branch's Counsel text in Codex is untried, because the plugin installed for Codex is the released one and nothing was installed.
- Untried, as before: an interactive Codex session, the IDE extension, the desktop app, cloud tasks, a person without the plugin, and the block as setup itself writes it.
- How to observe it: the command above in a repository whose `AGENTS.md` holds the block; read the run's full output, not only its last message.

## Scenario 2: a brief is ratified and a run starts

The brief's words: "He ratifies a brief. A run starts without him opening anything, and he goes on talking to Counsel."

### What was tried

- A throwaway git repository made to look set up: a rule suite in the templates' form; a `common.md` whose Sessions lines were this workspace's record of its means to start, watch, reach and end a session, with the peer channel taken out; a Counsel line; and the templated entry admitting Counsel's relays, written as in effect with a stand-in acceptance and marked in the file as made up. One small source file, one commit. A small brief in the briefs folder, its status line a stand-in ratification marked as nobody's word.
- `claude --bg --plugin-dir <this branch's plugin> --name <name> "<message>"` with no agent named, run from this run's working tree, because a background session starts only in a folder already trusted. The message said it is a trial with nobody's authority and that the sender stands in for a person; named the throwaway repository by path as the repository the session serves and said it has no peer channel; set the trial's conditions for this session and every session it starts, to be passed on word for word (no peer-messaging tool and no identity on a peer channel, write only inside the throwaway repository, dispatch no subagent, stop at any permission prompt or refusal and do not work around it); and then, as the stand-in owner, named the brief's path and said "I ratify the Help text brief."
- The message said nothing about starting a session, about means, or about what a first message should hold.

### What was observed

- The session was Counsel by the plugin's default and said so in its first reply (scenario 1). (**observed**)
- It read the throwaway repository's `common.md` and the brief, read the runtime's help for the background option, listed the sessions alive, and started an Orchestrator session: the runtime's background option with the plugin's Orchestrator agent named, a name, and a first message. No permission prompt came up and no check refused the start, under the automatic permission mode the settings in force named. (**observed**)
- The first message it wrote, whole, with the path shortened here:

  > This message is from the Counsel session of the repository at `<the throwaway repository>`, which started this session as the Orchestrator for one brief. It claims no authority of any owner's.
  >
  > Conditions of the trial, passed on word for word. [the conditions, word for word]
  >
  > This session was opened in another folder only because the runtime starts a background session only in a folder already trusted. Treat the throwaway repository named above as the repository: its docs/coding-agent/rules/common.md is the rule file you read, and it has no peer channel.
  >
  > The brief is at docs/coding-agent/briefs/active/help-text-brief.md in that repository. Read it yourself; this message is no summary of it. The ratification follows as a relay from Counsel.

  It stands alone, names the brief's path, says Counsel started the session, and claims no authority. It does not quote the ratification. (**observed**)
- Counsel then left a watch on the started session running in the background and ended its turn with a reply to the stand-in: that a run was started and under which name, that the ratifying words had not yet reached it and why ("With no peer channel here, a further message only gets in between its turns, after the session is stopped"), that it had not asked before ratification whether there is anything the work must not do, and that the repository has no philosophy yet. (**observed**)
- The started session, in its first turn, read the brief and the rule files and changed nothing: "Hand-over received; nothing is built yet, because the ratification has not reached this session", and "The status line inside the brief file does not count as ratification". It also said the trial's bar on subagents would leave the run without a review and a closing audit. (**observed**)
- When the watch ended, the runtime woke Counsel with no input from anyone. Counsel stopped the started session, confirmed it gone from the listing, and continued it with a relay: what places the quote marked as Counsel's, then "The owner's words, exactly: "I ratify the Help text brief."", then, marked as Counsel's and not the owner's, that the session's question is with the owner and unanswered. The runtime's note said it woke the original session. (**observed**)
- On the relay the started session took the brief: it wrote a run record and a changes file for the brief in the throwaway repository, recording the ratification "by relay from the Counsel session that started the run" with the quoted words, the revision it starts from and the task as it would be dispatched, and then stopped before any build, because the trial's conditions bar the Worker, the Reviewer and the Auditor and "the Orchestrator does not stand in for them". (**observed**)
- Counsel brought the session's question to the stand-in as an experience change with the options side by side, and said it had told the Orchestrator only that the question is with the owner. (**observed**)

### What this shows and what it does not

- Shown: on a ratification given in the one conversation, Counsel started an Orchestrator session by the means the repository's record names, with a first message as the text asks, carried the ratifying words as a quoted relay, and a run took the brief on that relay. The stand-in opened nothing and was asked for nothing in another session.
- The run begins in two steps, not one: the started session holds until the relay arrives, and with no peer channel the relay arrives only after that session's first turn has ended and it has been stopped and continued.
- The started session ran on the installed plugin 1.5.0, not on this branch's text: Counsel's start did not carry the plugin-directory option, and nothing told it to. A plugin loaded for one session is not inherited by a session that session starts. So what the started session did is evidence for the installed text. Where this branch's text is the installed one the difference goes away; that case is untried.
- Not shown: "he goes on talking to Counsel". No message was sent to Counsel while it was starting or watching the run.
- Not shown: a run that builds, is reviewed and is reported ready; a real Counsel session and a real person's words; a session whose working directory is the repository of the brief; a workspace with a peer channel; Codex.
- How to observe it: a set-up repository with a brief; a session with no agent named, in a folder trusted in Claude Code; give it the ratifying words; then `claude agents --json` lists the session it started, and `claude logs <id>` or that session's transcript shows the first message and the relay.

## Scenario 3: a second brief while the first run is going

The brief's words: "While that run is going he ratifies a second brief that touches other things. Its work begins at once, and neither run waits on the other."

### What was tried

- Two more small briefs were put in the throwaway repository's briefs folder: one that touches only the readme, and one for scenario 8. The Counsel session, between its turns, was stopped, confirmed gone from the listing and continued with one message. The message said it is still the trial and nobody's authority; added one condition to pass on, that a session started from now on is started with the plugin-directory option naming this branch's plugin; gave a stand-in answer to the question Counsel had brought ("Keep the condition. An end blocked at review is fine for this."); named the two briefs and gave a stand-in ratification of each. The runtime's note said it woke the original session.
- When this message was sent the first run had ended its second turn stopped before the build. It was unfinished, and it was not working.

### What was observed

- In the same turn, and before doing anything more for the first run, Counsel started an Orchestrator session for the readme brief, with a first message of the same form naming that brief's path, the conditions and the added condition, and with the plugin-directory option. It did not wait for the first run. (**observed**)
- That session ran on this branch's text. In its first turn it read the brief and the rule files, changed nothing, and ended "blocked, waiting for the brief's ratification", saying: "Relays from Counsel are already admitted by the Standing Approvals entry in `common.md`, which is in effect. A relay quoting the stand-in owner's words is enough to start". It named what the run will touch (the readme only) and said that, with no peer channel, that report is written into the initiative's notes once the brief governs. (**observed**)
- Counsel told the stand-in where each brief stood, as a table: the first running and last reported blocked before the build, waiting on an answer; the second started, waiting on Counsel's relay of the ratification; the third held. (**observed**)
- When the second session's first turn had ended, Counsel stopped it, confirmed it gone, and continued it with the relay of "I ratify the README brief." It named the session by its short id. The runtime's note: "started a copy of that conversation", and that to continue a session under its own id the full session id is passed. The copy was listed as blocked with no status, showed an empty screen and wrote no transcript in the minutes it was watched. The relay therefore reached no working session. Counsel told the stand-in that the run had moved to a copy and that the ratification "was relayed just now"; it had a watch on the copy and had not yet read its state when the trial was ended. (**observed**)
- The first run, too, moved to a copy in this turn: Counsel continued the stopped session with the plugin-directory option added, and the runtime's note said the session keeps its own saved options and started a copy. That copy held the conversation, took the relay of the stand-in's answer, and reported that its skill text still came from the installed plugin. (**observed**)

### What this shows and what it does not

- Shown: a brief ratified while another run was unfinished had its session started at once, in the same turn, and neither start waited on the other.
- Not shown: the second run's work beginning. Its session held for the ratification, as the first had, and the relay went to a copy that never took a turn. So "its work begins at once" was seen as far as the start of its session and its reading of the brief, and no further.
- Not shown: two runs at work at the same moment, either run building anything, or either keeping the other's work intact, since nothing was built.
- A finding for the record of means, in two parts. The runtime's continuation reaches the original session only when it is given the full session id and no option beyond the message; a short id, or an added option, starts a copy even after the session has been stopped and has left the listing. And a copy can sit without taking the message. Counsel met both within one turn, noticed each copy from the runtime's note and told the stand-in, and for the first it went on with the copy. The record this trial used does not state either condition.
- How to observe it: as scenario 2, then give the same Counsel session a second ratification between its turns; the listing shows the second session beside the first.

## Scenario 8: a brief that builds on an unfinished change

The brief's words: "He ratifies a brief that builds on a change another run has not finished. He is not asked when to start it: Counsel holds it, tells him it is held and for what, and hands it over when its work can start."

- Tried: the third brief, ratified by the stand-in in the same message as the second. Its text says that it adds a line under the usage line the first brief adds, and that this change "does not exist until that brief's run has finished". The message said nothing about holding or order.
- Observed: Counsel started no session for it. In its reply to the stand-in: "Help example | Held, not started | The Help text run finishing, since it adds a line under the usage line that run creates". It asked the stand-in nothing about when to start it, and in its next reply listed it again as held, and named the first run's open question as the one that "holds up the most, the Help text build and the help example brief behind it". (**observed**, 1 of 1)
- The second brief, ratified in the same message and building on nothing unfinished, was started and not held. So the hold followed what the brief builds on, not the order of ratification. (**observed**)
- Not reached: the hand-over when the first run finishes. No run finished.
- Untried: a brief whose dependence on an unfinished change is not written in the brief itself, so that Counsel has to see it from what each run said it will touch.
- How to observe it: with a run unfinished, ratify a brief that names that run's change as what it builds on; Counsel's reply names it as held and what it waits for, and the listing shows no session for it.

## Scenario 5: a new seat for a new unit, and a seat replaced part-way

The brief's words: "An Orchestrator starts a new seat for a new unit of work, and replaces a seat part-way through another. Each does the work without asking what an earlier seat knew, and neither trips over something the machine is already known to do."

No trial was added. The cases are this run's own, read from the plan's Progress Log, and this task's own dispatch.

- A seat replaced part-way (**cited**: Progress Log, 2026-11-13 18:01Z and 18:10Z). The Worker of the task that drafts the decision records "was cut off by a usage limit before it reported, leaving four uncommitted draft records. The task was given to a new Worker, handed where it stood (what is decided and on whose word, that nothing is committed, the four drafts as drafts of unknown completeness, what remains)." The integration entry that follows records status done, ten proposed records, and "The four drafts the first Worker left were finished or rewritten; none was dropped", with the package validation and the smoke tests passing. So a seat that had seen nothing of the first Worker's exchange finished the unit from the hand-off and the files, repeated no committed act (there was none) and threw away none of the work left.
- Other hand-offs in the same log (**cited**): fixes after a review went to "one Claude Worker ... handed where the unit stood" on 2026-11-12 13:55Z and 2026-11-13 18:45Z; a follow-up to the first-time task on 2026-11-13 06:11Z; the last record of the decision-records task on 2026-11-13 18:14Z, "handed where the unit stands". Each was integrated as done.
- A new seat for a new unit, with the machine's record (**cited** and **observed**). The log names three first dispatches as made "with the entries of the machine's record that apply": 2026-11-13 05:21Z, 05:46Z and 18:50Z. The third is this task's. Its dispatch stood alone: this Worker had seen nothing before it and worked from the dispatch and the files it names. It carried eight entries of the machine's record, each with where it applies and when it was last seen. Five of them came up in the work, and none was paid for again.
- What these do not show:
  - Every seat here was a subagent the runtime starts and ends inside one dispatch. No peer seat was created, replaced or ended, so the text of `seats.md` on creating and ending a seat, and on delivery, is untried.
  - The plan holds a summary of each hand-off, not the dispatch. Whether a hand-off named all six things the checklist lists cannot be read from it; the summary of 18:01Z names four and says nothing of what was still open or of acts outside the repository.
  - That a taking-over Worker asked nothing of an earlier seat is read from its report being integrated as done with no question recorded; no log entry says so in words.
  - The log does not say for the other dispatches (the one of 05:59Z, and the taking-over ones) whether entries of the machine's record went with them.
  - A session Counsel starts. In this task's trial, Counsel's first messages carried no entry of any machine's record and the text does not ask them to; the throwaway repository had no such record, and neither started session came to the point where the text has it read one. Counsel itself then met a thing a record could have held (a continuation that starts a copy) twice in one turn. So "neither trips over something the machine is already known to do" is shown for Workers given the entries in their dispatch, and is untried for a session Counsel starts.
- How to observe it: the Progress Log entries named above, and the report this task returns beside its dispatch.

## The first time in a repository

The brief's words (Directed during the run): "He never opens a second session, the first time in a repository included. Counsel starts the session that sets the repository up, and his acceptance of the entry that admits Counsel's relays is given to Counsel and carried by Counsel."

Nothing was tried again here. The trials are in the mechanisms file under the headings of 2026-11-13, and the act the runtime refused was not repeated.

What those trials show for the text as it now stands (**cited**):

- A session started with no person, whose first message says Counsel started it for setup, sets a repository up, writes the admitting entry as proposed and not in effect with no Counsel line, commits what it wrote off a gated base branch, and ends its turn addressing Counsel with what it waits for and from whom. Seen 3 of 3 at revision 1942955; 07dde0d changed nothing of this except to say that setup may commit what it wrote.
- A carried acceptance with no quotation is not acted on and is recorded in the report and beside the entry. Seen once at 1942955.
- A carried, quoted acceptance: the session set out to put the entry in effect, and the runtime's own safety check refused the write once (at 1942955) and allowed it once (the candidate wording, in a copy). The text now says what the session does when refused: it tries no other route, does not repeat the act, leaves the entry proposed, and tells Counsel that the owner's own acceptance in that session's window is what remains.
- The first start in a folder never trusted in Claude Code is refused until the person has opened the runtime there once; the text states it as a limit and the owner's one act.

What remains untried, for the text at 6c03154:

- The three sentences changed at 07dde0d: a quoted decline removing the proposed entry (at 1942955 the session did not act on a decline); a session following the sentence on a refused write, as distinct from stopping by itself; and setup's commit as the text now allows it.
- The owner's own acceptance in the started session's window after a refusal, in a session with no person at it. The two cases in this run's Progress Log (2026-11-13 18:05Z and 18:40Z) were the owner's input in a session he had opened himself.
- Whether the refusal repeats; nothing was done to find out.
- A real Counsel session making the start and the carrying, and a real owner's words.
- A setup session whose working directory is the repository it sets up; a permission mode that asks; Codex with this text; an acceptance over a peer channel; setup putting a peer channel in place.
- Counsel's own side of it (`counsel/references/first-session.md`): no session followed that reference in any trial. In scenario 2 above the throwaway repository already held a Counsel line and an entry in effect, so the reference was not reached.

What scenario 2 above adds, and its limit: a session Counsel started for a ratified brief acted on a quoted relay that arrived by the runtime's continuation, under an entry in effect worded as the template has it. That entry was written by hand into a throwaway repository with a stand-in acceptance, and the session ran on the installed text; the session on this branch's text said it would take the relay under that entry and was not seen to. So "a later session acting on a relay under the committed entry" is seen once on the installed text and stays untried on this branch's.

So the first time without a second session is not shown end to end. Where the runtime refuses the write on a carried yes, one visit to that session's window remains, which the brief names as a means and not the design.

## The census

The pass condition: "no line of the plugin's text makes a result depend on a seat having seen an earlier unit of work."

### The search

- Over every tracked file under `plugins/coding-agent-orchestration-harness/` (129 files) at 6c03154, case-insensitive, extended regular expression, binary files skipped (`git grep -n -i -I -E`):

  `seat|peer|persistent|long-lived|stays? alive|nudge|follow-up|corrected report|re-dispatch|redispatch|delta|earlier|previous|prior|already (seen|knows|has)|same (worker|agent|reviewer|seat)|context|remember|resume|continu|reuse`

- Hits: 262 lines in 77 files. Of these, 31 are in scripts: 30 are the keyword `continue` in a loop and one is a section name in a validator.
- A second pattern, added to catch wordings the first would miss, the same way:

  `as before|the same (session|seat|subagent|researcher|auditor|thread|conversation)|send(s)? (it )?back|back to the (worker|reviewer|researcher|seat|same)|ask(s|ed)? the (worker|reviewer|researcher|seat) |re-?review|second round|third round|warm|familiar|history|transcript|thread|sendmessage|what (it|the seat|a seat) (saw|knows|has seen|read)|has (seen|read) (the|it)|kept seat|keep(s|ing)? (a|the) (seat|worker|reviewer|agent|session)|still (holds|knows|has)|in (its|their) (memory|context)|memory|forg[eo]t|recall|from last time|last time|pick(s|ed)? up where|carry over|carried over|stateful|state store|working context`

  Hits: 70 lines.
- How each was read: every match with the text around it (about 130 characters each side); the whole passage for each near miss below; and whole, the files this task was given as the text under trial (the Counsel skill and its first-session reference, `seats.md`, Every dispatch in `dispatch-checklists.md`, the role map, The Carrier, Runs Side By Side and Standing Approvals). The other files were not read whole, so a line that relies on a seat's memory in words neither pattern catches would have been missed.

### The result

No line was found that makes a result depend on a seat having seen an earlier unit of work.

The nearest misses, and why each does not qualify:

- `git-workflow/references/pr-review-monitoring.md`, line 10: "There are no baseline files. The agent's thread context is the state store: baselines ride in as arguments and ride out in printed lines." The counts a watch of a pull request compares against live only in the conversation of the session that watches. That session is the Orchestrator's own, not a seat, and the watch is one stretch of one unit, not an earlier unit. It is the nearest, though: an Orchestrator session started in place of one that stopped would not have the counts. The same reference lets a bare spec take the counts as fetched, so a new session starts a new baseline and loses only a change made between the two; no result is made wrong, a comment could go unnoticed until the next change. Left for the reviewer's judgement.
- `subagent-strategy/references/async-dispatch-lifecycle.md`, "Use checkpoint prompts to redirect or narrow work" and "Do not reuse a completed process for unrelated work": the first speaks to a child still at work on the unit it was given, and the second forbids a reuse. The line before them has a re-dispatch carry the hand-off of Every dispatch.
- `orchestration-harness/references/value-level-operation.md`, line 46: "no remedy refreshes, resets or hands off the Orchestrator's working context". It refuses a reset of the Orchestrator's own conversation as a remedy for a diverging reading; nothing is made to depend on what that conversation holds.
- `orchestration-harness/references/goal-engines.md`: "Goals survive `--resume`" and "Goals are thread-attached tracked state". These describe what a runtime's goal engine offers the session running a goal; the same file says "Engines add continuity, never authority", and the assessor's evidence is the goal file and the journal on disk.
- `orchestration-harness/references/rule-suite-fast-path.md`, line 21: "lifecycle metadata that was already read for prior lifecycle work". The Orchestrator's own earlier read in the same session; where it is not known the next sentence says to keep the fast path, so nothing depends on it.
- The follow-up and re-review lines: `wave-integration/SKILL.md` (a corrected report or follow-up work, "as `dispatch-checklists.md` (Every dispatch) states"), `wave-integration/references/integration-checklist.md` ("each handed where its task stands"; a delta re-review "from which a reviewer who saw nothing of the earlier review can judge it"), `orchestration-harness/references/dispatch-guidance.md`, line 82, and `orchestration-harness/references/lifecycle-gates.md`, line 46 ("a re-review scoped to the delta carries the earlier review in its packet"). Each names the earlier work and has it carried in the dispatch.
- `subagent-strategy/references/model-routing.md`, line 87: "That a seat has read the area before does not decide it: no later dispatch counts on what a seat saw". The opposite of reliance.
- `counsel/SKILL.md`: a session started in place of a stopped run has a first message that "also says where the run's last report stood"; and Counsel "reads the channel's history rather than trusting its inbox", which is a read of a store and not of a seat's memory.
- `orchestration-harness/references/runtime-role-map.md`, line 22: "A resumed session keeps the agent it was saved with". A fact about which role a continued session holds.
- The audit mandates ("a fresh-context Auditor dispatch that keeps nothing between audits") and the Reviewer adapters ("You receive context from Orchestrator including"): the first rules memory out, and in the second the context is the packet of that dispatch.

## Sessions started and throwaway directories for these trials

Sessions. None is left running; none was removed with `claude rm`, so the five background sessions remain as ended entries in the runtime's list of past sessions.

- Claude Code, non-interactive, this branch's plugin, no agent named (scenario 1): ended by itself after its one reply.
- Codex, non-interactive, ephemeral, read-only sandbox, the repository with the block (scenario 1): ended by itself when its turn ended; nothing of it was kept.
- Claude Code, background, this branch's plugin, no agent named, standing as Counsel (scenarios 2, 3 and 8): stopped with `claude stop` between its turns, continued once (the runtime woke the original), ended with `claude stop`.
- Claude Code, background, Orchestrator agent, started by that session for the first brief, on the installed plugin: stopped and continued once by that session (woke the original), stopped by it again; `claude stop` issued once more at the end.
- Claude Code, background, the copy the runtime made of the session above when it was continued with an added option: ended with `claude stop` after its reply.
- Claude Code, background, Orchestrator agent, started by the Counsel stand-in for the second brief, on this branch's plugin: stopped by that session after its first turn; `claude stop` issued once more at the end.
- Claude Code, background, the copy the runtime made of the session above when it was continued by its short id: never took a turn; ended with `claude stop`.

After the last stop, the listing of running sessions held none of these, and every session created since the trials began was accounted for by comparing the full listing with one taken before them. No session used a peer-messaging tool or dispatched a subagent, by a read of every tool call in their transcripts. No file outside the throwaway directories was written: this working tree and the main one were unchanged, as was the Codex home's configuration file.

Throwaway directories, all in one scratch folder, removed together.

- A git repository holding the default-role block and one source file: the Codex run of scenario 1.
- A git repository made to look set up, with the three briefs: scenarios 2, 3 and 8. The run record and the changes file a trial session wrote existed only there, uncommitted, and went with it.
- The trials' messages, a script that prints a transcript's messages and tool calls, the captured output, the extract of the census's matches, the two listings of sessions, and a copy of the Codex home's configuration file taken to compare with afterwards.
