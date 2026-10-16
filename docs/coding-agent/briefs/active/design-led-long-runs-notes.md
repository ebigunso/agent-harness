# Discussion notes: design-led long runs

Unratified. Kept by Counsel. Nothing here gates anything; the auditor does not read this file. The discussion that led to the brief, with ebigunso's words dated, is in `value-level-operation-notes.md` in this folder, under "Open questions and ideas".

## Owed after this run closes (added 2026-10-05)

- Decision: hand `setup-names-what-is-missing-brief.md` to the Orchestrator once this run has closed, relaying his ratification in full: "I ratify the brief, hand it over after the run closes." Not before.

## State for Counsel at session compaction, 2026-10-05

Written by Counsel at ebigunso's word ("Prepare yourself for session compaction."), so that a Counsel whose earlier context is gone can pick up from the files. It records where things stand and how Counsel works here; it decides nothing.

### Where things stand

- Two briefs are active. `value-level-operation-brief.md`: built; stack 74 of pull requests 72, 73 and 75 is published and unmerged; records ADR-D-0034 to 0049 accepted; its four human-only conditions are pending his first real use. `design-led-long-runs-brief.md`: ratified 2026-10-04 and amended many times since, each amendment with his words beside it; this is the governing brief of the run in progress, which stacks on those pull requests.
- He will not judge or merge anything until the design-led run is finished: he considers the first stack incomplete without it.
- The run so far, as the Orchestrator reported it: plan 1 (the brief form, Counsel's policy, the Auditor role) closed; plan 2 (the run across plans) had its second wave built and audited on 2026-10-04; a further plan is to keep a goal-mode run to his values, with a decision record of its own. Nothing of this run is published; its unpushed commits are to be rebuilt before publication so that no machine path reaches the remote, which he allowed.
- Records of this run: ADR-D-0050 (the Auditor) accepted; ADR-D-0036 reworded, file renamed to say "stated", accepted; ADR-D-0051 to 0054 accepted by him on 2026-10-05 and relayed at 08:18 UTC.
- Still to come back to him: ADR-D-0045, changed in substance by his removal of the watch list; the record for goal-mode runs kept to his values; then the run's closeout and the whole stack for his judgement.
- Five relays of 2026-10-05 had no answer in the channel when this was written (07:37 records handling and Workers writing records; 07:46 unsupported plan lines and Counsel's wording; 07:51 watch list removed; 08:18 acceptance of ADR-D-0051 to 0054; 08:31 the stop requirement). The Orchestrator's last message to Counsel was 2026-10-04 12:12 UTC. It is nonetheless active: it had committed Counsel's edits to this brief and these notes, and he was reading its session directly.
- Nothing was waiting on his judgement when this was written.

### Set aside for later discussion with him

- A product philosophy and an engineering philosophy for this repository. Candidates for both, in his words with dates, are in `value-level-operation-notes.md`.
- The rules for durable design documents; enforcing Counsel's limits by tool settings; how a decision he delegates to Counsel is recorded; the delivery failures between the sessions, which he holds to be the delivery mechanism's to fix.
- His local privacy hook and the `machine-setup` repository went to another session of his; the handoff file is gone from this repository.

### To check in the closeout read

- The closed list of stops in the built text: the auditor noted that a closed list lets work continue wherever a stop in force today is not on it.
- Whether the stop for a run that has stopped getting closer is the Auditor's judgement with the burden of proof on continuing, as the brief now says, and not the Orchestrator's count of two plans.
- The lines of the brief that are Counsel's wording or inference and that he was not asked to accept one by one: the reworded scenario 9, the pass condition on goal mode, the means that demonstrated scenarios are evidence the Auditor weighs. They are to be listed for him once, at closeout.
- What Counsel answered from his standing words without bringing it to him: nothing so far.

### How Counsel works here

- Identity: `agent-harness-counsel` in the agmsg team `AgentHarness`; the Orchestrator is `agent-harness-orchestrator`. After a session restart the role is re-claimed and the inbox watch started again with the new session id.
- Reading the channel: the message history, not the inbox command, which has reported nothing new while messages were stored. The history call can hang and is run with a time limit.
- Sending: one message per call, the body in single quotes with no apostrophes inside it.
- The watch is kept running, re-armed at each expiry, while work is running; it is left to lapse when the work is complete or blocked on him.
- Records that govern Counsel: ADR-D-0034 (the role), 0035 (reach into the work), 0038 (how his word reaches the Orchestrator), 0043 (Counsel speaks to the Orchestrator only in his words), 0044 (the pause), 0045 (what Counsel hears during a run; due to change), 0046 (discussion as a person's experience), 0047 (documents free in their terms).
- To the Orchestrator: his words quoted in full, the question or proposal he was answering as Counsel put it, facts it asks for, and notice that a brief changed. No instruction, opinion or ordering of Counsel's own. A relay of an acceptance names the record in his words; one that does not is no acceptance.
- To him: answer first; a question put as a person's experience (who, what they do, what they then experience, what they gain); anything Counsel originated marked as its own; his words kept when recorded.
- Before any of Counsel's files is written: no machine-specific user name or path.

### Faults of Counsel's in this work, kept so they are not repeated

- Reading more into his words than he said, then relaying it as his direction. Twice a useful distinction was turned into a required form (the experience chain as a document format; kinds of statement as a layout).
- Recommending a proposal from the Orchestrator that loosened a rule governing its own stopping, without asking what he would experience under it or why that was better.
- Bringing him too much: every exception report however low, wording points on records that changed no meaning, and requests to bless Counsel's own wording.
- Then the opposite: grading as low, and keeping from him, the Orchestrator's own stop rule, which differed from what he believed was agreed. The test added since: a matter that differs from what he thinks was agreed is never low.
- Relaying his critique of a proposal without the requirement that went with it, so that the Orchestrator kept a rule he had not agreed to.

## Facts

- What the accepted goal-mode records say, as Counsel read them on 2026-10-03 for the discussion:
  - ADR-D-0009 makes goal mode a second operating mode, entered only when the end state is objectively checkable, the work is search-shaped, and every irreversible or outward-facing action can be kept out of the loop.
  - ADR-D-0011 defines progress as the goal read as a gap: counted directly, or argued in the journal on plateaus; stall is no movement, no credible argument, and circling.
  - ADR-D-0014 has the assessor re-examine whether the goal is still valid and stop the loop with a challenge when it is not.
  - ADR-D-0027 requires an envelope ratified by the user before the loop, with a forbidden set defined by one criterion, immutable during the run.
  - ADR-D-0028 ends a loop on stall, not on resources consumed.
  - ADR-D-0029 and ADR-D-0030 keep the optimizer from judging its own continuation, through a fresh-context assessor run as a Reviewer profile with a fixed template; ADR-D-0030 names a further role as its upgrade path.
  - ADR-D-0031 says completing a goal never authorizes merge.
  - ADR-D-0040 says the ratified brief could authorize a goal-mode envelope once a record states the conditions, and that such a record would replace ADR-D-0027.

## Assumptions

- Counsel assumed, and wrote into the brief as inferred, that goal mode for goals a check can decide keeps working as it does today. He ratified the brief with that line in it; he did not discuss it separately.
- Counsel assumed the earlier brief's rulings carry over to this run (push after review, records accepted by name, quoted relay, stops for irreversible actions). Same standing.

## Decisions

- None pending. The brief was ratified whole on 2026-10-04.

## Open questions

- Whether goal mode remains a mode of its own beside design-led runs or becomes a special case of them was raised by Counsel and not settled by him; the brief only fixes that today's goal-mode behaviour is kept.
- How progress toward a scenario only he can judge is argued, and how stall is detected when part of the design is uncountable, is the hard part Counsel named; the brief gives one means (demonstrated scenarios are what a run counts) and leaves the rest open.

## Exception reports received

- 2026-10-04, from the plan-draft audit of the first plan: sixteen items hit the watch list; none rests on a provisional statement. Counsel's grading, which decides nothing:
  - Ten hit "a change to how goal mode behaves today". Each says goal mode stays as it is except that the in-loop assessor is dispatched to the Auditor, which the brief states. Low; nothing off.
  - Three hit "anything that weakens who may authorize or stop work" and are the brief's own statements restated as the plan's definition of done. Low; nothing off.
  - The stall is judged by the audit from demonstrated scenarios against the Orchestrator's prediction, with the prediction opened only after the grades are fixed. Low; it strengthens who judges a stop.
  - Whether a mid-flight finding bears on the design is the Orchestrator's reading first, compared by the audit at its next position; a missed one is escalated with the part held. Low to medium: a misjudged finding reaches him one audit late.
  - A repeat of a divergence is defined as the same item at two audits in a row. Medium: an Orchestrator that diverges on a different item at every audit would never be stopped, which is what drift looks like. Raised with him at once; the Orchestrator was told only that a question on that matter is with him.
  - Counsel's own fault: two watch-list entries it proposed are worded so broadly that any statement touching goal mode or stopping hits them, the plan's own restatements of the brief included.

- 2026-10-04, from a second plan-draft audit of the same plan: three lines already reported gained a second watch mark, "anything that weakens who may authorize or stop work", recorded by the auditor as unsure because the role that judges a goal loop's end changes hands from the Reviewer to the Auditor. Counsel's grading: low. That change is the one the brief states, and it moves the judgement to a role with a stricter rule on what it may be told. A first copy of this report arrived with its list empty through a failed script on the Orchestrator's side; the corrected copy followed a minute later.

- 2026-10-04, from a third plan-draft audit of the same plan: one new line, graded ask-now by the audit, so the gate holds it whatever Counsel thinks. The plan added that a run of a single plan under a brief behaves as before; the audit found no supporting statement and said it narrows what the brief gives, since the gives-statements on self-correction, design-level findings, closeout by scenario and stopping apply to any run under a design. The value question as the audit put it: when a design he hands over turns out to need only one plan, should that work still keep itself to his values as it goes, bring him a better design it notices, and report back scenario by scenario, or run as work does today? Counsel's handling: brought to him at once. Counsel considered answering from his standing words ("One design is carried over as many plans as it takes, without you.") and did not, because that statement does not say in terms that the other gives apply to a run of one plan, and Counsel has over-read his words before.

- 2026-10-04, his answers, now in the brief as amendments with his words: the number of plans a design takes does not matter to what the brief gives; a divergence caught and fixed promptly is the audit doing its job, and the work stops when it depends on a philosophy-worthy decision that what he supplied does not cover nearly enough to settle without him; the watch list is narrowed as Counsel proposed; the three parts of the brief file that went beyond the chat text are confirmed.
- 2026-10-04, from a fourth plan-draft audit: the held line, reworded by the plan to "a run with no brief behaves as before, where that run is under a philosophy and so is audited", is still graded ask-now. The audit's reason: keeping to the philosophy needs a philosophy and an audit, not a design, so "as before" would leave such a run without the self-correction the brief's statement gives. The value question as the audit put it: when work runs under his philosophy with no brief, should it also keep itself to his values as it goes and correct itself before he hears of it, as work under a brief will, or should that come only with work that carries a design in a brief? Brought to him at once.

- 2026-10-04, from the wave-boundary audit after Wave 1, matched against the amended watch list: six lines hit, every one recorded by the auditor as unsure, none resting on a provisional statement. Five are the in-loop goal assessment moving to the Auditor, where who is dispatched changes and the rule texts do not; one is that later plans of a run start without him, which the brief asks for in terms. Counsel's grading: all low; nothing off. Pattern Counsel sees: narrowing the list cut the hits from sixteen to six, and every remaining hit is the plan doing what the brief itself states, graded cited. A watch entry that overlaps what the brief asks for will fire each time the brief is carried out.

- 2026-10-04, from the closeout audit of the run's first plan: two new lines hit the watch list, both recorded by the auditor as unsure, neither resting on a provisional statement. One is the rewording of ADR-D-0036, where text Counsel worded and he ratified becomes ground the audit may extend without a stop; he still ratifies every statement, and the rewording is his own direction. The other is the log entry recording his acceptance of ADR-D-0050 and the retirement of ADR-D-0030. Counsel's grading: both low; nothing off.

- 2026-10-04, from the plan-draft audit of the run's second plan (the run across plans): four lines hit the watch list, none resting on a provisional statement. Counsel's grading:
  - The held item, graded ask-now: work under a philosophy that runs no audit today, goal mode and work handled directly as trivial, gets no reading and no comparison under this plan. He has since answered for goal mode in his own words. For directly handled work the Orchestrator holds no word of his; Counsel had only told him it would leave that alone. Brought to him for an explicit word.
  - The stops are a closed list: a held grade, the part a finding concerns, a run that has stopped getting closer, Counsel's pause. Cited from his amendment on when the work stops. Low.
  - A plan under a brief closes without "candidate ready" while the run continues, and the run closes once. Cited; it is what he asked for. Low.
  - Publication: the standing approval for a finished, reviewed run to publish and open pull requests was given when a run was one plan; the plan reads it as the whole multi-plan run, published once at its end. Low, and worth his knowing: pull requests for a multi-plan run appear only when the whole run finishes.
- 2026-10-04: he corrected Counsel's reading of "The watch list stands corrected." He meant the wording of the list can be corrected too. The entry on goal mode is reworded in the brief; the wording is Counsel's, shown to him.

- 2026-10-04, from a second plan-draft audit of the run's second plan, matched against the reworded goal-mode entry: two lines changed, both now graded cited from his amendment on goal mode, both recorded by the auditor as unsure, neither resting on a provisional statement. One commits the run to changing goal mode in a further plan and does not yet say which part changes; the other closes this plan without "candidate ready" and drafts that next plan, with publication after the run's last plan. Counsel's grading: both low. The earlier ask-now on this item is gone now that his answer on goal mode is in the brief; the audit holds nothing on work handled directly as trivial, on which he has still given no word of his own.
- 2026-10-04: ADR-D-0036 landed with its file renamed to say "stated", pointers repaired, and set accepted, on his words "Go ahead and change the file name too. ADR-D-0036 is accepted once that lands."

## Questions the Orchestrator brought for him

- 2026-10-04: the final review of the run's first two branches found that seven audit verdicts logged word for word into the plan each named, as a full path on his machine with his user name in it, where the auditor had read its instructions. Nothing was pushed. The Orchestrator replaced the paths with a redaction mark and wrote the lesson, but the earlier local commits still hold the original text, and asks whether he allows it to rebuild this run's unpushed commits before publishing so the paths never leave his machine. Counsel did not answer from his standing words: his privacy rule states the end ("it should be redacted before they ever reach the remote") and not that commits may be rebuilt, and rewriting history is an act the Orchestrator does only on his word. Brought to him at once. Status the Orchestrator gave with it: the first plan has passed its closeout audit and final review on every other point, and the second plan, the run across plans, is being drafted.

- 2026-10-04, raised while planning the second plan; nothing waits on it. Two statements in the brief pull against each other for goal-mode work: his amendment that work under a philosophy keeps itself to his values whatever the type of work, and the constraint that goal mode for goals a check can decide keeps working as it does today. Goal mode has no value audit today, so a goal-mode run in a repository with a philosophy gets none of what the amendment describes; work handled directly as trivial has none either. The second plan builds the self-correcting behaviour where the audit already runs and leaves goal mode alone. The question: should a goal-mode run in a repository with a philosophy also be kept to his values as it goes, which adds an audit to goal mode and so changes it, or does goal mode stay exactly as it is for now? Counsel's note for him: the amendment is his own words; the constraint was Counsel's inference, ratified with the brief but never discussed. Brought to him.

- 2026-10-04, a design-level finding from the Orchestrator, the first under the brief's rule that a plan departing from a means is a finding and not a breach. The part it concerns waits; the rest of the second plan proceeds. The brief's means is that demonstrated scenarios are what a run counts toward the design. The plan would better it in one place: a plan also counts as having brought the run closer when its result is a credible precondition of a named scenario, judged by the audit and counted at most once per scenario. Its reason: some plans lay ground and demonstrate nothing by themselves, this run's first plan being one, and without this a run would be stopped as stuck after two such plans in a row though it is on its way. Its cost: a run can go one plan further on a precondition before the stop falls. Its question: when a plan shows nothing he could observe yet but the audit judges it a real precondition of one of his scenarios, should that count as the run getting closer, once per scenario, or should only scenarios he could observe count? Until he answers the stop rule and its decision record are not written. Brought to him.
- 2026-10-04, a fact the Orchestrator gave Counsel about the brief: its agent-checkable pass condition on goal mode still read "is unchanged" with no exception while its Limits allow the one change he named. Counsel brought the pass condition in line with his amendment and told him.

- 2026-10-04, his response to the finding on how a run counts progress, and to how Counsel handled it: "I feel the proposed stop condition is more on the mechanical side than I prefer to judge myself. And I feel that the recent rounds are leaning towards too many reports coming up, nudging the Counsel into micromanaging. The gap I'm feeling here is that you are not catching that this proposal just tries to loosen the criteria slightly to let it's actions slide, without a clear grounding in why that would ultimately lead to a better behavior and experience."
  - Counsel's faults, as it now sees them: it recommended the proposal although it came from the party whose own run the stricter rule would have stopped; it called the slack bounded without working out that once per scenario allows as many extra plans as there are scenarios; it never asked what he would experience under either rule; it brought a mechanical question to him as if it were a decision about the design. It had also been bringing him every exception report it graded low, at once and in detail, where the accepted rule says a low matter is raised at his next natural contact, and it had raised wording points on records that changed no meaning.

- 2026-10-04: he took Counsel's change to the rule on departures from a means ("Yeah I think that approach is better."); the brief is amended and the Orchestrator told, so that ADR-D-0053 and ADR-D-0054 are corrected before he is asked to accept them.
- 2026-10-04: the Orchestrator withdrew its proposal on counting progress. A run counts only a scenario's state moving forward, as the brief's means says, and stops after two plan closeouts in a row with none; it proposes no record for that measure. Counsel's grading: low, kept here and not brought to him. To watch at closeout: that measure is the Orchestrator's own and could stop a run that is laying ground; if it does, the stop reaches him and shows whether the measure serves what the brief gives.

- 2026-10-04, from the wave-boundary audit after Wave 2 of the second plan: eight lines hit the watch list, the same decisions reported at plan draft, now built; none held, nothing asked of him. Counsel's grading: all low, kept here and not brought to him in detail. For the closeout read: the closed list of stops is graded inferred, and the auditor noted that a closed list lets work continue wherever a stop in force today is not on it; Counsel cannot tell from here whether any is missing.
- 2026-10-04, a point from the auditor for Counsel: the brief's agent-checkable pass condition on goal mode and its watch-list entry on goal mode were reworded by Counsel on his words for the Limits amendment, and the brief quotes no acceptance of either wording. Nothing built so far rests on them; the run's next plan will. Counsel to confirm both wordings with him before then.

## Too many escalations: his observation and Counsel's count

- 2026-10-05, ebigunso: "I'm starting to spot a pattern here of too many escalation opportunities and too little autonomy for the Orchestrator. I'm feeling that I'm getting pinged for decisions too often and for things that probably can be settled without me. Can you double check how the current proposed structure would work, and spot those points, so that I would get a better experience as an end result? And you, the Counsel, is getting pinged too often I feel too."
- Facts Counsel counted from the channel for this run, hand-over at 09:14 UTC to 12:12 UTC on 2026-10-04, about three hours: 23 messages from the Orchestrator to Counsel, of which 10 were exception reports; about 17 separate asks reached him through Counsel.
- Where the asks to him came from, by Counsel's count: decision records accepted one at a time mid-run and again after each wording change (ADR-D-0050; ADR-D-0036 three times; ADR-D-0051 to 0054); questions the audit raised because a line the Orchestrator added to its own plan narrowed what the brief gives (a run of one plan; work with no brief); Counsel returning for his word on its own wording or inference (the three brief additions, the watch-list wordings twice, trivial work, two reworded lines); an action that needed his word (rebuilding unpushed commits); one mechanical finding (how a run counts progress) and the rule that sent it to him; one real conflict between two statements of the brief (goal mode).
- Where the messages to Counsel came from: an exception report at every audit position, each re-audit of the same plan draft included; watch hits on items the brief itself states, graded cited; the mandate's "is, or bears on" and reporting when unsure.

- 2026-10-05: Counsel proposed five changes to cut what reaches him and Counsel, the first being that a run's records are accepted once at its close. Asked to explain the first in detail, Counsel did, naming its risk: his record reviews had caught changes of substance, not only wording. His answer: "I think it's still beneficial to check proposed ADRs before things are built on it, but minor wording changes coming back to me is I feel too much." So early acceptance stays; what goes is a change of wording returning to him.

## Answered from his standing words during this run

- Nothing yet.

## Ruling given in the Orchestrator session (unratified; written by the Orchestrator)

- 2026-10-04, ebigunso, typed in the Orchestrator session: "Opus is an acceptable cheap model. Fable and Astra count as expensive, for me at the moment." and later "I've configured the codex worker and reviewer to use GPT-6.1-Sol instead of GPT-6 Astra so you can continue dispatching them freely." Recorded in this repository's `docs/coding-agent/rules/orchestrator.md` as his setting for the workspace. Unratified as a value statement; nothing is graded on it.

## Counsel's first read of the run's candidate, 2026-10-05, before seeing the audit's marked items

Formed from the Orchestrator's candidate-ready note of 11:30 UTC, the description of the top pull request, the commit titles and the brief only. Not final.

- Fits the brief as reported, mechanism by mechanism: design in the brief with kind marks and scenarios; one run over several plans closing once; the Orchestrator's reading compared after grading; a design-level finding held by part, checked in both directions; the Auditor as its own role; no watch list; the hold on loosening; Workers drafting records; goal mode kept to his values. Each traces to a statement or an amendment of his.
- The stop for a run that has stopped getting closer is reported as the Auditor's judgement at each plan's close, which is what he required on 2026-10-05, and not a count of two plans.
- The note does not do what the brief's Closeout section says the closeout gives: it does not lead scenario by scenario with how to observe each. It names no state for scenarios 1 to 4, and the pass condition says a scenario no run could demonstrate is said so plainly. Only the goal-mode point is said plainly not shown. Counsel does not know whether the run's record holds this and the note left it out.
- Scenario 1 as an experience of his in this very run: three plans were carried, but he was asked a great deal that did not need him, which he said himself on 2026-10-05. The run built the changes meant to cure that; it did not demonstrate them.
- A commit title of the third plan says wave-boundary audits were missed and are covered by the closeout audit. The note does not mention it. The audit at fixed positions is what lets him trust the work by default, so how this is recorded and what the closeout audit made of it is for him to hear.
- Not in the note: the closed list of stops; the list of records whose wording changed after acceptance (at least ADR-D-0053, whose references to the watch-list record were due to be trimmed).
- Records: ADR-D-0050 to 0054 and 0056 accepted by name; ADR-D-0036, 0045 and 0053 amended and accepted by name; ADR-D-0055 withdrawn at his word. That matches what Counsel relayed.
- Value documents changed in the run: the amendments to this brief, the note beside the earlier brief's watch-list line, and these notes are Counsel's, except the section "Ruling given in the Orchestrator session", which the Orchestrator wrote as the form allows.
- Lines of the brief that are Counsel's wording or inference, owed to him once at this closeout: the reworded scenario 9; the pass condition on goal mode; the means that demonstrated scenarios are evidence the Auditor weighs; the statement that a run that has stopped getting closer stops and tells him.
- Not evidenced, judged in first use: scenarios 5 to 9, and whether he could trust the result by default.
- Counsel cannot verify the agent-checkable claims.
- Answered from his standing words during this run, without bringing it to him: nothing.

## Counsel's finalized read of the run's candidate, 2026-10-05, after the audit's marked items

Formed after the Orchestrator's message of 11:32 UTC carrying the closeout verdicts' marked items, the scenario states, the records reworded after acceptance and the record of the missed audits.

- Scenarios as the closing verdict states them: 1 to 4 not yet, and not demonstrable by this run, since no run was made on the built plugin; 5 to 9 ready for his judgement in first use. The first read's gap is closed: the states exist and are stated plainly; the candidate-ready note had left them out.
- The whole run was carried out by an older installed plugin (0.21.0), with the audit on the Reviewer's agent type. Nothing in the range is evidence of how the built plugin behaves.
- Three wave-boundary audits of the third plan were not dispatched. The Orchestrator ruled that the closeout audit over the whole range stands in. The Reviewer did not accept it as their equal. The closeout audit graded nothing in the range ask-now, so nothing went ahead that an earlier audit would have held; it calls it the run failing to keep itself to his values as it went, and notes no question was put to him at the time though the built text escalates such a finding at once. Medium: it bears on what his trust rests on; nothing needs undoing.
- In this runtime every Auditor dispatch arrives with the Orchestrator's commit subjects in its context, added by the runtime and not by the dispatch. The Orchestrator ruled the audit counts. The audit marks that the audited party settled whether an audit of itself counts. Medium: his to settle.
- Three marked items settle things for later runs and are his to know: a statement tagged inferred that he ratified with a brief keeps its support for the audit, and only what Counsel inferred beyond an answer with no ratification of its own does not; where no value audit runs, the Reviewer confirms the Orchestrator's call that a record change is wording only; a question already sent to him can be withdrawn on the audit's judgement, which he accepted by name in the amendment to ADR-D-0053.
- The one-sided comparison of findings marked in the second plan was cured by that amendment.
- Records reworded after acceptance, wording only: ADR-D-0036, 0038, 0040, 0041, 0042, 0044, 0045, 0046 and 0050, each a pointer to a renamed or replaced record; ADR-D-0053, its clause naming the watch list.
- Nothing in the marks contradicts the first read. Two matters go to him as questions: the missed audits and the commit subjects.
