# Discussion notes: value-level operation

Unratified. Kept by Counsel during discussion with ebigunso. Nothing here gates anything; the value audit does not read this file. Items move out of here when ratified into the brief, a philosophy, or a decision record.

## Open questions and ideas

- 2026-10-01, ebigunso: cover not only plan mode but the longer-horizon goal mode, which may be better redefined as a longer-horizon mode rather than a goal mode. Expectation: delegating at brief level produces larger chunks of work that suit the longer-horizon mode. Asked how the two would mix best.
  - Counsel's reading (not ratified): goal mode's lifecycle (envelope ratified once, journal, checkpoint commits, fresh-context assessor, stall detection, graded escalation) is the machinery an unsupervised long run needs, and the value audit is the same separation the goal assessor already embodies. What goal mode lacks is admission for work whose end state is judged by a person; the brief supplies that, with pass conditions marked agent-checkable or human-only, and the loop ends in "candidate ready" for the human-only ones instead of "met".
  - Possible shape: an outer longer-horizon loop governed by the brief and an envelope, producing a sequence of plan-mode chunks (Task_X waves, Workers, Reviewer, audit at each plan), with stack acceptance by the person directing the work at each judgeable behaviour. A one-plan initiative is the degenerate case; a fully agent-checkable goal (lint to zero) is the special case that keeps a countable gap.
  - Cost: it reopens the goal-mode records (ADR-D-0009, D-0011, D-0027 to D-0031) and the progress definition for human-judged conditions. Counsel suggests a second initiative after the current one ships, not a scope expansion of it.
  - 2026-10-03, ebigunso, reversing the order: "I actually want to build on the longer horizon mechanism on top of the current stack, before we test the current version, which I feel is incomplete without it rather than being a smaller complete set. Let's discuss what needs to happen for that once the current slice of work is handled." So the longer-horizon mechanism is the next initiative, stacked on pull requests 72, 73 and 75, and the stack is judged and merged with it rather than before it.
  - Preparation, 2026-10-03: what the accepted goal-mode records say, read by Counsel for the discussion, and what a longer-horizon mode would touch in each. The second half of each line is Counsel's reading and decides nothing.
    - ADR-D-0009 makes goal mode a second operating mode, entered only when the end state is objectively checkable, the work is search-shaped, and every irreversible or outward-facing action can be kept out of the loop. Touched: the first condition excludes work a person judges by behaviour, which is most of what a brief hands over.
    - ADR-D-0011 defines progress as the goal read as a gap: counted directly, or argued in the journal on plateaus; stall is no movement, no credible argument, and circling. Touched: a human-only pass condition has no count, so progress toward it rests on the argued kind, and stall detection has to stay sound with part of the goal uncountable. This is the hard part.
    - ADR-D-0014 has the assessor re-examine whether the goal is still valid, not only whether it is being reached, and stop the loop with a challenge when it is not. Touched little: with a brief as the goal, the challenge is that the brief no longer fits, which is a value question for him.
    - ADR-D-0027 requires an envelope ratified by the user before the loop, with a forbidden set defined by one criterion and immutable during the run. Touched: ADR-D-0040 already says the ratified brief could be a second source for an envelope once a record states the conditions, and that such a record would replace this one.
    - ADR-D-0028 ends a loop on stall, not on resources consumed. Touched little.
    - ADR-D-0029 and ADR-D-0030 keep the optimizer from judging its own continuation, through a fresh-context assessor run as a Reviewer profile with a fixed template. Touched: the value audit is the same separation; whether one dispatch can do both jobs, or the two stay apart, is a question for the discussion.
    - ADR-D-0031 says completing a goal never authorizes merge; a human retrospective on a verified report does. Touched: this matches his ruling that he judges a stack by its behaviour before anything ships.
  - Three questions Counsel expects him to need to settle: what unit of work the loop produces and he judges; how progress is measured toward conditions no check can decide; whether goal mode stays a mode of its own or becomes a special case of the longer-horizon one.
- 2026-10-04, ebigunso, on how philosophy adherence is kept during a run: "The way we built it makes reviews responsible for this, which is an enforcement mechanism. I'm concerned that this might lead to the Orchestrator thread to care less about the philosophy and just do whatever the review audits pointed out while it is doing its work, since the responsibility is arguably not theirs anymore." He named two causes and holds both likely: "it's both the responsibility argument and the attention drift."
  - What the fix must be, in his words: "In the final version, I shouldn't be concerned with what the Orchestrator is doing, the mechanism should let me trust the work by default. What we're trying to deal with here is something that can break that trust, and the fix needs to be something that automatically happens while the work is ongoing, that I don't have to think about."
  - Shape he agreed to ("Yes, mostly"), proposed by Counsel: before each audit the Orchestrator commits its own reading of which items the documents cover, which extend them and which need him; the audit, not the Orchestrator, compares that reading with its own grades; a divergence is corrected inside the run, the Orchestrator going back to the philosophy and the brief, re-deriving what the work is for and redoing the item; a divergence that repeats stops the affected part and comes to him as a value question through Counsel. Nothing about it reaches him otherwise.
  - His limit on it: "a full context refresh is probably an unnecessarily aggressive measure. Preserving context of work is usually vital to its ultimate success, so if it doesn't have to happen then all the better." So renewing the Orchestrator's context is not part of the mechanism; Counsel withdrew that suggestion.
  - Counsel's suggestion that this become a requirement of the longer-horizon work: taken. *(2026-10-04: "Okay I agree with you.")*
- 2026-10-04, ebigunso, his rough take on the longer-horizon mechanism, in full: "I'd like to be able to: 1. When no philosophy document exists, be able to write them through extensive discussions with the Counsel session. 2. I can throw ideas at the Counsel session, discuss them against the philosophy and the repository's shape at the time, to arrive on a design I'm comfortable with. This includes you advising on things I missed, or things that could potentially make the design better than what I describe. 3. I can let work be dispatched for what designs were decided, and I get back an implementation that matches what was designed and is consistent with the philosophy's direction. 4. Anything that was noticed midflight that suggests a better design existing, is also reported. It's debatable if this finding should stop the run or just be kept as a suggestion. 5. With all these, I expect to be able to more quickly build larger scale features and improvements to whatever I'm building, ultimately benefitting me and anyone else that uses what was built."
  - 2026-10-04, asked what a design contains: "A design is, I think, often the experience one gains by introducing a feature. This could just be a desired behavior, which probably leans more towards an open ended goal, and sometimes includes a UI design that an experience is heavily influenced by." Counsel had assumed a design decides some of how the work is done; by his words it states the experience, and how stays with the Orchestrator.
  - 2026-10-04, on where a design lives: "I agree with your take that the design should go along with the rest of the brief. When a work starts, it's usually just a rough idea of what it would look like in the end, so writing a formal document out of that would possibly result in things needing to be invented or intentionally kept open, which is not ideal. This doesn't mean durable design documents doesn't have to exist though, that serves to communicate an intent behind a certain design outside of what is decided in an ADR and of a granularity larger than what a code comment would be suited for. This would also serve as something categorized by a field of technology, so that context for implementations concerning that field is easier to come by than being scattered over code comments or unorganized ADRs."
  - 2026-10-04, on scenarios: "Scenarios I think do fit in with how a design can be verified, but if that is to become something to measure against, it's probably good practice to discuss and define a few core scenarios beforehand in a Counsel session, rather than having every scenario be derived from the given goals or designs."
  - 2026-10-04, on when he judges: "About when to judge, ideally I'd only have to look at it when it's done, or something is off and needs my attention."
  - 2026-10-04, on a finding mid-flight that a better design exists: "I'd like to not have the cost of change be a measure of if the finding reaches me or not. Some findings could lead to costly changes but ultimately arrive on a better design. I'd like to keep the option open to take that expensive path too. The alternative is true too, where it could be cheap to change something early on, but that change is trivial enough that it shouldn't cost my attention at all." So Counsel's suggestion that cost of change decides was declined; what decides whether a finding reaches him is not its cost.
  - 2026-10-04, on reading Counsel's first draft brief for this work, which carried more mechanism than the definition of a design allows: "I've gone into the mechanisms more than what I first imagined I would for any design, but that itself I feel isn't all wrong in itself. If I go too far into implementation details to an extent that it would constrain the shape of implementation prematurely, then that should be corrected, but what we now have I don't think doesn't cross that line." So a design states the experience, and may also state a mechanism where the mechanism is what he cares about; the test is whether a statement constrains the shape of the implementation prematurely, and it is Counsel's job to say so when one does.
  - Counsel's proposal, which he took: a brief separates what the work must give him, which binds, from the means settled in discussion, which the run builds from and may better; a better means found mid-run is a design-level finding and reaches him; a means he wants fixed regardless is marked a constraint and binds.
  - 2026-10-04, asked whether to record that: "Yes it would be great if you could record that, and to also think of a way to have all future Counsel sessions keep that in mind when discussing ideas." Counsel's answer: carry it in the form, not in a reminder. The brief form gets the two groups, so writing any brief forces each statement to be sorted; Counsel's conduct says to name a statement that would constrain the implementation prematurely; the audit treats a departure from a means as a design-level finding and not as a breach. All three are statements for the longer-horizon brief, so that the run builds them into the forms and the Counsel text.
  - 2026-10-04, on Counsel's redraft, which re-sorted the whole brief into those groups and dropped its topical sections: "The split between the deliverables and the means seems like a good idea, but how you dropped the categorizations you previously gave makes me concerned that enforcing that shape would drop some context that would otherwise have survived." So the split is a mark on each statement, not a layout: a brief keeps whatever sections state its concept best, a means stays beside the thing it serves, and each statement can be told apart as something the work must give, a constraint, or a means. Counsel had turned a useful distinction into a required shape, the same mistake he corrected earlier for the experience chain.
  - 2026-10-04, on the redraft with its sections restored and each statement marked: "Great. This one looks much better." Not a ratification: the core scenarios, the watch list and the drops are still his to settle.
  - 2026-10-04, on roles: "The reviewer role seems too overloaded now with the value audit added as it's new responsibility. Splitting roles by its nature seems like something we should now consider, so that I may choose appropriate models to run each on, rather than being forced into using the best model I have due to one of the responsibilities requiring that capability."

## Counsel's first read of the candidate, 2026-10-02, before seeing the audit's marked extensions

Formed from the Orchestrator's candidate-ready note and the brief only. Not final; ebigunso asked for an independent read first, then whatever else Counsel needs, then a finalized read.

- Fits the brief, as reported: a Counsel session on Copilot, Claude Code and Codex; the value documents with one form each; an audit at fixed positions that the Orchestrator cannot frame; escalation through Counsel with quoted relays; plan authorization by the ratified brief plus audit, unchanged without a brief; extensions marked by the audit; closeout as candidate ready, leading with behaviour.
- Not evidenced in the note, so unknown from here: that Counsel does check-ups through a Researcher and open conversations outside project preparation; that the Counsel text carries how a conversation should go (he speaks first, it teaches before asking, argues once for a dismissed branch, closing pass on what was dropped, distinctiveness check, provisional statements). These are human-only conditions and are judged in first use.
- One judgement call of the Orchestrator's that he has not ruled on and that changed what he experienced: a standing approval takes effect from the run after the one that adds it. Under it the push of the second pull request was held as ask-now although he had already accepted the standing approval for opening pull requests. By his own rule a stop on something the documents already answer is a defect, so this call deserves his decision.
- The other four judgement calls match records he accepted (entry by explicit act per runtime; sources written for any mode; an action stated as waiting for its decision; an inferred direction reported as the Orchestrator's own ruling).
- Stops in this run, as Counsel saw them: most were value questions on matters no document yet answered, which his rule says should stop. Two were runtime permission refusals that only his own statement in the Orchestrator session could clear; the relay cannot carry those, which limits "he never types into the Orchestrator session".
- The decision records needed three to four revisions each before he accepted them, all on form (too much in one record, rulings given as reasons, quotes, an occasion in Revisit When). The record standard now carries those rules; the cost was his attention in this run.
- Not audited in this run: the engineering side, because no engineering philosophy exists for the harness. Writing one is the obvious next discussion.
- Counsel cannot verify the agent-checkable claims (validators, reviews, audit dispatches); they are the Orchestrator's report and the audit's to confirm.

## Counsel's finalized read, 2026-10-02, after the audit's eight marked extensions

- Both reads flagged independently: a standing approval taking effect only from the run after the one that adds it (the audit's C7), and the engineering side going unaudited for want of an engineering philosophy (C11).
- The audit caught what Counsel missed: the Orchestrator still selects which Worker choices and which of its own rulings are shown at closeout (C15); only audit-graded extensions are marked by the audit.
- Counsel saw what the audit did not mark: the conversation conduct and check-ups are not evidenced in the note; the records cost him several revision rounds on form; a runtime permission refusal can only be cleared by his own statement in the Orchestrator session.
- Put to him for decision: C7 and C15. The rest of the marked items are stated in records he accepted.

## Counsel's first read of the second candidate (stack of three), 2026-10-03, before seeing the audit's marked items

Formed from the Orchestrator's candidate-ready note and the brief only. Not final.

- Fits the brief as reported: everything the brief asks for is named as shipped across the three pull requests, and records ADR-D-0034 to 0047 are all accepted, the last five by his statement naming each.
- A discrepancy with his ruling: the note still lists, as a judgement call of the Orchestrator's, that a standing approval takes effect from the run after the one that adds it. On 2026-10-02 he took Counsel's recommendation that it takes effect once his acceptance is recorded and committed. Either the ruling is not yet in the text or the note is stale; Counsel cannot tell which from here.
- A second ruling whose application is not evidenced: that the closeout audit, not the Orchestrator, marks which Worker choices and Orchestrator rulings bear on direction. The note's list of direction-bearing judgement calls is headed as the Orchestrator's own.
- Not evidenced in the note, judged in first use: how the shipped Counsel conducts a discussion (he speaks first, the experience chain, teaching before asking, the closing pass, the watch list written at that pass).
- What Counsel saw of the run against the human-only conditions: the stops that reached him were nearly all matters no document answered, which his rule says should stop; three times a runtime permission check needed his own hand in the Orchestrator session (renumbering, the push, the global hook), which the relay cannot carry; one blanket acceptance of his was sent back for not naming the records, the rule working as written at the cost of a round trip.
- Cost Counsel observed and the note does not state: fourteen decision records for one initiative, most revised several times before he accepted them, almost all on form. The record standard has since gained the rules that caused the revisions.
- Counsel's own faults in the run, for his judgement of the role: statements recorded as told without his words until the audit asked; instructions of its own sent to the Orchestrator until he pointed it out; three Orchestrator messages missed for over an hour while the watch was lapsed; a discussion practice turned into a document format and relayed as his direction, which he corrected.
- Still true: no engineering philosophy exists, so the engineering side of every audit here was not audited. This brief has no watch list.
- Counsel cannot verify the agent-checkable claims (validator, smoke tests, reviews, four audits).

## Counsel's finalized read of the second candidate, 2026-10-03, after the audit's five marked items

- The audit caught what Counsel missed: the five last records were set accepted on one statement naming each of them, which reads his condition "accepted on its own" as "named individually" and not as one statement per record; the audit asks that he judge whether that meets his condition.
- Counsel caught what the audit could not: two rulings he gave on 2026-10-02 are in neither the text nor this closeout (when a standing approval takes effect; who marks the Worker choices and Orchestrator rulings shown at closeout). The relay carrying them is stored in the channel at 2026-10-02T07:10:49Z and was not seen by the Orchestrator. An earlier relay, stored at 2026-10-01T12:54:39Z, was missed the same way.
- So the stack as it stands contradicts two of his decisions. Both are now in the brief as ratified lines and were sent again with their proposal text.
- The other marked items (escalation transport, what counts as a citing audit, the two-stage read, a pause binding without admission as a relay) are stated in records he accepted.
- Answered from his standing words during this run, without bringing it to him: nothing.

## Local privacy hook: what Counsel found and what was discussed, 2026-10-02

Not part of the harness or this initiative's deliverable. ebigunso is handing this matter to a different session; this section is Counsel's contribution to the single location he asked the Orchestrator to prepare.

- His directions so far: the privacy check should be a pre-push hook rather than a worded gate; it is local, for all repositories he works on, and does not go with the plugin.
- Facts from a read-only scan of the folder holding his local repositories on 2026-10-02: no global hooks path is set; Character Memory has a `pre-commit` hook in its own `.git/hooks`, installed by the pre-commit framework, and carries a `.pre-commit-config.yaml`; thirteen other repositories have no hooks of their own and no hook tooling; four folders there are not git repositories. Repositories kept elsewhere on the machine were not scanned.
- Consequence discussed: a global hooks path makes git ignore every repository's own `.git/hooks`, so Character Memory's pre-commit checks would stop unless forwarded, and the pre-commit framework refuses to install while one is set (the second point not verified here).
- His leaning, stated as a question to Counsel: apply it as repository-local configuration in every repository he works on, since some repositories hold settings other developers use and a machine-global setting cannot be assumed the same everywhere.
- Counsel's advice, not yet taken as a direction: a hook in each repository's own `.git/hooks`, which overrides nothing and is not shared with other developers; git's template directory so new clones get the hook automatically; one script that each hook calls.
- Where the one script lives, settled 2026-10-02. His concern: a script placed directly in the home directory clutters it and carries no information about how and from where it is used, so it could later be removed without knowing the effects. Counsel proposed, and he took ("I like that idea of an independent repository." and, to the name, scope and structure below, "Yeah that looks good."):
  - An independent repository beside his other repositories, named `machine-setup`. It is kept private or never pushed, since it holds machine-specific details.
  - Scope: general in what it may hold, with one admission rule. Something belongs there if it is installed from there onto the machine or into other repositories, and something depends on it being there. Preferences nothing depends on, and files not installed anywhere, do not belong.
  - Structure: one folder per item, starting with only the pre-push privacy check; each item states what it installs, where it installs it, and what stops working if it is removed; one list at the top of everything currently installed and where; an install and an uninstall step per item.
  - Each repository's hook calls the script by its path and fails closed: if the script is missing, the hook blocks the push and says where it expected to find it. Consequence he was told: moving or renaming the repository stops every push on the machine until the path is fixed.
  - Repository-local hooks in each repository's own `.git/hooks`, plus git's template directory so new clones get the hook, were Counsel's advice above; he did not rule on them separately, and left the setup to the session he will spin up.
- Who does the work: a session he spins up, which sets up that repository and then the other repositories on top of it. *(told 2026-10-02: "I'll let the session I spin up handle setting up that repository and setting up the other repositories on top of it too, so just have the handoff location hold that note.")*

## Counsel's first read of the third candidate, 2026-10-03, before seeing the audit's marked items

Formed from the Orchestrator's candidate-ready note of 06:10 UTC and the brief only. Not final.

- Fits the brief as reported. The two rulings that had gone unseen are now reported as built: a standing approval takes effect once his acceptance is committed, and the closeout audit, not the Orchestrator, marks which judgement calls he sees.
- Records ADR-D-0034 to 0049 are reported accepted, each named in his words, and four older records retired. That matches what Counsel relayed.
- New since the last candidate, each from a direction of his: the value-document forms in a home of their own; push only after review; role names and each role's home stated in the role map and not in records.
- Not evidenced in the note, judged in first use: how the shipped Counsel conducts a discussion, including the experience chain and writing a watch list at the closing pass.
- A gap the note names and Counsel agrees is real: the brief's line on the document forms records a decision he delegated to Counsel, not his own words for the statement, and neither the forms nor the audit mandate say how such a line counts. He has not ruled on it.
- The note says the brief's Closeout section still carries Counsel's read as part of the closeout. On disk the Lifecycle line was amended on 2026-10-02 to say the read reaches him from Counsel alone; if the audit read a committed version from before that edit it would not have seen it. Counsel cannot tell which from here.
- Still true: no engineering philosophy and no product philosophy exist for this repository; this brief has no watch list; the delivery failures between the two sessions are unresolved by his choice, as a matter for the delivery mechanism.
- Counsel's own faults since the last read: a discussion practice turned into a document format and relayed as his direction, which he corrected; advice to rename the Copilot agent given without reading the record on role names.
- He has said he will not judge or merge this stack now: the longer-horizon mechanism is built on it first.
- Counsel cannot verify the agent-checkable claims (validator, smoke tests, reviews, six audits).

## Counsel's finalized read of the third candidate, 2026-10-03, after the audit's seven marked items

- The audit marked the same seven items as its previous closeout. Two are now graded cited, because his words were added to the brief in range: the two-stage closeout read, and the two stale older records, since replaced.
- The five still graded inferred are each stated in a record he accepted (how his word reaches the Orchestrator; what counts as a citing audit; a side with no document not blocking; a pause binding without admission as a relay), except one that is not in any record: Counsel's limits are held only by stated rules where a runtime could enforce them by tool configuration. Counsel raised that with him at the previous closeout and he has not ruled on it.
- The item on a side with no document rests on the brief's provisional line that no engineering philosophy exists; that was the one exception report of the run, graded low by Counsel.
- Nothing in the marks contradicts Counsel's first read, and nothing new needs his decision before the longer-horizon discussion.
- Left for that later discussion: whether Counsel's limits should be enforced by tool configuration where a runtime allows; how a brief line that records a decision he delegated to Counsel should count; an engineering and a product philosophy for this repository.
- Answered from his standing words during this run, without bringing it to him: nothing.

## Candidates for an engineering philosophy of this repository

Kept at ebigunso's request of 2026-10-03: "keep notes about things that could go into an engineering philosophy document of this repository, from what has been brought up in discussions until now, so that you don't lose track of them after session compaction." Unratified. Each entry gives his words with the date, then Counsel's one-line gloss of what it might mean as a standing statement. The glosses are Counsel's and decide nothing; the philosophy is his to state when that discussion is held. No engineering philosophy exists for this repository yet, so the engineering side of every audit in this initiative went unaudited.

### Boundaries and coupling

- 2026-10-03: "Responsibilities and boundaries needs to be clear cut and well defined enough to have misuse be obvious so that keeping mechanisms loosely coupled is easier to achieve in the long run." Gloss: a part is defined so that a wrong use of it is visible on sight; shared material gets a home that belongs to no user of it. Applied when the document forms moved into a skill of their own.
- 2026-10-02, on briefs: "the briefs are being committed but they don't have the lifecycle handling the plans have. I think it needs a division of active and completed as well." Gloss: artifacts of the same kind get the same lifecycle; a new kind does not invent its own handling.
- 2026-10-03, on the stack: "I feel is incomplete without it rather than being a smaller complete set." Gloss: what ships should be a complete set at its size, not a fragment of a larger one; completeness is judged by whether the core action works, not by how little was built.

### Enforcement

- 2026-10-02: "Probably it's better to have it as a pre-push hook rather than relying on a worded gate." Gloss: where a mechanism can enforce a rule, prefer it to text an agent is asked to follow.
- 2026-10-03: "this is just a delivery failure and that should better be handled by the delivery mechanism than to work around it." Gloss: a fault is fixed in the layer that owns it; other layers do not grow rules to compensate.
- 2026-10-03, on the audit reading a condition literally: "The audit seems to be taking things too literally, but that might be for the better, so consider rewording it too if that would help." Gloss: when a strict checker trips on loose wording, tighten the wording, not the checker.
- 2026-10-03: "Push after review seems like the better option." Gloss: nothing reaches the remote unreviewed. Now a rule in the orchestrator rule file.

### Caution and trust

- 2026-10-03, on a collision rule: "it's just extra caution for something that hasn't been proven to do harm." Gloss: a protection needs a demonstrated harm; one kept on plausibility alone is removed. Already close to an accepted record (protection requires a demonstrable consumer).
- 2026-10-02, on barring Counsel from raising a pause again: "I think it's better to trust in the rational decisions of the Counsel rather than restrict its moves too much, preventing only a potential loophole." Gloss: do not restrict an agent's judgement to close a loophole that visibility already closes.
- 2026-10-02, on how a rejected stack is fixed: "This is really just implementation details, and anything reasonable will work. I'm not going to restrict how to handle things." Gloss: constrain what matters and leave the rest to whoever does the work.
- 2026-09-30: "The debt argument is solid, and it needs some attention." Gloss: how much technical debt is acceptable for what gain is his to state, and has not been stated.

### Durable documents and decision records

- 2026-10-01: "Me declining or ruling, in itself shouldn't be treated as the reason for a decision. A reason behind it should always be present." and "you don't need to state my words as a quote. If the reasons behind the decision is clearly stated, that is enough." Gloss: a durable document rests on reasons, not on who decided. Now in the record standard.
- 2026-10-01: "It is a detail that doesn't affect the conditions themselves, and that shouldn't be in a durable document." Gloss: a durable document names the premise, not the occasion on which it will be checked. Now in the record standard.
- 2026-10-01: "A decision to introduce the Counsel role and what it's responsible for, and how philosophy documents should be handled are probably different decisions." and, of a long Decision section, "it's putting too much into one ADR." Gloss: one decision per record, split until each could be retired alone.
- 2026-10-03: "Putting so many caveats in an ADR seems to not be the way to go." and "Dropping the actual role names entirely too could be something to consider. That would remove the need to update the ADR every time a new role comes in." Gloss: a record states the rule and leaves lists, names and conventions to the text it governs, so that ordinary change does not make it stale.
- 2026-10-03: "I think the stale records should be updated." Gloss: a record that has become slightly wrong is replaced, not tolerated. He reads decision records and both philosophies himself and objects to anything even slightly off.
- 2026-10-02: "limiting to that only would sacrifice too much freedom to state the core concept that a discussion has settled on." Gloss: a durable document states its concept in whatever terms state it best; no single form is imposed. Now ADR-D-0047.

### What ships and what stays local

- 2026-10-01: "Make it work both ways, if the Counsel session is with Claude or with Codex, or anything else for that matter." Gloss: plugin text assumes no particular model or runtime.
- 2026-10-02, on model routing: such best practices "could get old quickly as model capabilities advance". Gloss: the plugin carries what stays true as models change; dated observations about models live in the workspace's rule files and are re-observed at a model upgrade. Now built.
- 2026-10-02, on the privacy hook: "just make it a local thing. It doesn't have to go with the plugin. I'd like to have it in all repositories I work on, but it's not for everyone else." Gloss: his personal practice is not a plugin feature; the plugin is for its users, his machine setup is his.
- 2026-10-02: "some repositories hold settings that other developers would use too, and a machine global setting cannot be assumed to be the same everywhere." Gloss: nothing in a repository may depend on a setting of one machine.

### Privacy

- 2026-10-02: "the usual privacy protection of no machine specific user names and paths leaking applies here too. If that sort of thing is quoted, it should be redacted before they ever reach the remote." Gloss: no machine-specific name or path reaches a remote, quoted or not.
- 2026-10-02: "Leave the history alone, no rewrite needed. Things already out cannot be undone... sad fact." Gloss: published history is not rewritten to hide what already leaked; the effort goes into not leaking again.

### Design documents

- 2026-10-04, on durable design documents: they are "closer to the implementation than what I'd like to review myself. So, I probably won't be reading them. I'd like to set up a rule or mechanism to keep them organized and cleaned up, so that only what really needs to be communicated goes there in the right shape, without accumulated clutter or an increased risk of documents going out of date. This could include decisions to deliberately keep certain things out of documents so they stay in the code rather than being restated in documents which is a surface prone to divergence. What does go in and what doesn't needs to be weighed against the tradeoffs of it being scattered in the code base and risking it being missed, and the statements going stale in the documents. Maybe an engineering practice to prevent related code from scattering all over the place would help to mitigate this problem, but I'm open to suggestions here." and earlier the same day, on what they are for: they communicate "an intent behind a certain design outside of what is decided in an ADR and of a granularity larger than what a code comment would be suited for", and are "categorized by a field of technology, so that context for implementations concerning that field is easier to come by than being scattered over code comments or unorganized ADRs." Gloss: a document is a surface that diverges from the code, so a statement earns a place in one only when leaving it in the code would lose it; code for one concern is kept together so that its explanation can stay with it.

### Things that explain themselves

- 2026-10-02: "Scripts placed in user home directly would clutter it as well as carry no information about how and from where they are used, so it's possible that later it could accidentally get removed without knowing the effects." Gloss: anything others depend on says what depends on it, and its absence fails loudly rather than silently.

### Models and context

- 2026-10-02: "the privacy check probably is better handled by a GPT model doing the research or implementation." Borne out in this run: the Codex reviewer found real gaps the first passes missed. Gloss: detail scrutiny goes to the model that has shown that strength; a workspace observation, not plugin text.
- 2026-10-02, on Counsel reading code in bulk: "it would quickly fill the context of the Counsel so that vital information not yet documented could get lost by session compaction, and that those code in the context could pull the Counsel away from the desired high level of abstraction." Gloss: a session's context is protected in proportion to how much undocumented knowledge it holds; bulk reading goes to a session that can afford to lose it.

### Already stated elsewhere, so not to be duplicated

- The repository's lessons log and accepted records already carry: bundled skill content is for the consumer's agent only; skill text carries only what a tool cannot teach; validators enforce contracts, never prose; content is removed from the harness only with evidence of the matching kind.
- An engineering philosophy would state the stances behind these, not repeat them.

## Candidates for a product philosophy of this repository

Kept at ebigunso's request of 2026-10-03: "Do the same for product philosophy candidates you can find. We'll discuss both in detail after the current upgrades are finished." Unratified. The product is the harness. Entries are his words with the date, then Counsel's one-line gloss, which decides nothing. They are grouped the way he said a philosophy reads well to him: the behaviour he wants from using it, what he wants out of it, and what he does not want it to be. No product philosophy exists for this repository yet; the ratified brief has stood in for one.

### Who it is for

- 2026-09-30: "The persona is me, but the situation could differ. This proposed shape works if I'm the product owner, but stops being as effective when I'm not." and 2026-10-01, on working for someone else's product: "it's still good to have as much delegation as possible to free up my attention." Gloss: a person who directs work done by agents, whether or not the product is theirs.
- 2026-09-30, reporting the author of the skill set this was compared against: his approach "relies heavily on the human in charge being highly skilled, since clarifying those values and pushing back when something feels off while discussing the direction of the project is key." and his own answer to that: "I probably need some help in telling me what areas I should think of rather than relying on me to notice everything by myself." Gloss: the person is able to judge and push back, and is not assumed to notice everything unaided.
- Unstated: the plugin is published and others install it. Whether they are a persona of this philosophy, and how they differ from him, has not been discussed.

### The behaviour he wants from using it

- 2026-09-30: "I'd like to be a able to talk about what the product does or should do, which is much easier for me to object and is also more effective in shaping the direction, rather than pouring over every implementation plan that I need to pay attention for signs of drift from the core product direction." Gloss: he shapes direction by talking about what the product does, not by auditing plans.
- 2026-09-30: "I'd probably need an entry point where I can discuss those values and solidify them, before moving onto any implementation." Gloss: values are discussed and settled before work starts.
- 2026-09-30: "The goal I'm aiming for here is to have me look at the behavior of what has been built, at the product user's value standpoint for the most part, and rarely anything more detailed." and 2026-10-01: "I'd want to check the behavior before things get shipped." Gloss: he judges what was built by its behaviour, before it ships.
- 2026-09-30: "Stopping is more acceptable over going out of line and having the result be awkward, but there is a line here too, where a direction can be reasonably inferred from other standing product values should be kept going and reported later instead of stopping at every small ambiguity." and "If there's enough context already, then never stopping is the desired behavior. But that doesn't mean skipping over decision points that needs to be brought up, which if it happens would be a failure of the harness that needs fixing." Gloss: a run keeps going where his standing values answer the question, and stops where they do not; each stop is judged on whether it was right.
- 2026-09-30: "That should naturally come from the decisions documented, and where you have none then that is where the gap is." Gloss: how far a run may go on its own follows from what he has documented, nothing else.
- 2026-10-02: "What should come to me is now more limited, only something that needs decisions on the product or engineering philosophy level that defines the direction of the product." Gloss: only direction-level decisions reach him.
- 2026-09-30: "I think ADRs, product philosophy, and the engineering philosophy, are the three things that I need to keep track of and object to if there's anything even slightly off. Those shape the future implementation decisions, so it's the critical part." Gloss: three kinds of document are his reading surface; everything else he may ignore.
- 2026-09-30: "the one I talk to can weigh in on the decisions and surface anything that has slipped from being recorded but was ultimately important." and 2026-10-02: "for something that falls in the Counsel's responsibility, I'd like genuine advice to reach me." Gloss: the session he talks with gives real advice and catches what slipped.
- 2026-10-02, reporting how the same author works: "he discusses about user experience and everything he points out is from that viewpoint. He said that this allows easier intuition by him on what might be wrong and how it should be". Gloss: discussion is held as a person's experience, where his intuition works.
- 2026-09-30: "I shouldn't need to type into Orchestrator's session directly." Gloss: he talks to one session; the working session comes to him through it.

### What he wants out of it

- 2026-09-30: "you would be able to fully delegate a large implementation task and be confident about what it brings you aligns with what you value." and of the current harness, that it lacks "the resulting ability to run longer horizon tasks unsupervised." Gloss: long work, handed over whole, comes back aligned.
- 2026-09-30: "I'd also like to be able to achieve more in terms of features shipped and product maturing." and "When the product lacks features to meaningfully operate, then more features lead to maturity. When the product has enough features already, fleshing them out more leads to maturity." Gloss: more achieved, where what counts as maturing depends on the product's state.
- 2026-09-30: "I'm fine to spend a lot of time discussing up front. That ultimately saves me from needing to oversee every little detail due to the constant drift pressure I have to fight against, and would result in faster implementation of usable results." Gloss: attention spent once at the start, in exchange for not supervising.
- 2026-09-30: "Sharpening my thinking during the discussion probably should be valued highly. It's a bet to leverage increasing model capability and resulting insight gain, while suppressing those would limit insight to human level." and "It should help to uncover view points that were outside my thoughts, or give insights into things I don't know well enough to give informed judgements outright." Gloss: he leaves a discussion thinking more sharply than he arrived; the harness is built to gain from better models.

### What he does not want it to be

- 2026-09-30, on agents: "LLMs do tend to tunnel vision and forget to reference the implications of the philosophy and decisions when they matter most." and of a counterpart that supervises: it "is still too close to implementation to avoid tunnel vision and, to borrow my friend's word, context rot." Gloss: the session that holds his values must not be drawn into the implementation.
- 2026-10-02: "if Counsel is allowed to instruct the orchestrator in my behalf, it would likely quickly become another redundant orchestration layer." Gloss: not a second layer of orchestration.
- 2026-09-30, on help in discussion: welcome "unless it drives the discussion towards the uninteresting and less valuable median outcome." Gloss: not a pull toward the conventional answer.
- 2026-09-30: "Discussions shouldn't feel like filling in a form, that probably holds every time." Gloss: not a questionnaire.
- 2026-09-30, on the role he talks with: it should "handle routine checkups on the project's state on request, and hold conversations on times where it isn't phase or product preparation and still get useful insights that improve the product. The role shouldn't be too limiting." Gloss: not a role usable only at the start of a project.
- 2026-09-30, on implementation detail in a closeout: "sometimes they are necessary and it shouldn't be wholly prohibited." Gloss: rules of thumb are not absolutes; detail reaches him when his judgement needs it.
- 2026-10-03, on the acknowledgement rule, and 2026-10-03 on a naming caution: he declined both. Gloss: not a harness that grows a rule for every failure; see the engineering candidates on caution.

### Open, to be discussed

- What the longer-horizon mechanism adds to all of the above; he considers the current stack incomplete without it.
- Whether the harness's other users are a persona, and what the harness owes them that differs from what it owes him.
- How "maturing" applies to the harness itself.

## Draft brief for the longer-horizon initiative, as of 2026-10-04

Unratified. Kept here so the draft survives a session compaction; it becomes a brief file under `briefs/active/` only when ebigunso ratifies it. Each statement carries two marks: what kind it is (gives, constraint, means) and where it came from (told, inferred, agent-proposed, with "agreed" or "confirmed" where he accepted Counsel's proposal in discussion). His words for each told statement are in the open-questions section above, dated. Working title: design-led long runs.

Product basis: his own words. No product philosophy exists for this repository.

### Who it is for and why

- You bring an idea to Counsel and arrive at a design you're comfortable with. (gives; told)
- You let the work go and come back to an implementation that matches the design and fits the philosophy's direction. (gives; told)
- You build larger features faster, for yourself and whoever uses what was built. (gives; told)

### What a design is

- The experience someone gains from a feature. It may be only a desired behaviour, which is open-ended, and may include a UI design. (gives; told)
- It lives in the brief; no formal design document is written before the work. (gives; told)
- A statement may describe a mechanism where the mechanism is what you care about. Counsel says so when one would constrain the implementation prematurely. (gives; told)
- Each statement is marked as something the work must give, a constraint, or a means; the brief keeps whatever sections state its concept best, and a means stays beside the thing it serves. (gives; agent-proposed, corrected by him from a required grouping to a mark)
- A few core scenarios are defined beforehand by you with Counsel. (gives; told)
  - The run may add its own scenarios. (means; inferred)
  - Scenarios are evidence of the experience, not its definition. (means; agent-proposed)

### The run

- One design is carried over as many plans as it takes, without you. (gives; told)
- You look only when it's done or something is off. (gives; told)
- A run that has stopped getting closer stops and tells you. (gives; inferred)
  - Demonstrated scenarios are what it counts; those only you can judge end as ready for your judgement. (means; agent-proposed)

### Keeping to the philosophy without you

- You don't have to think about what the Orchestrator is doing. The run corrects itself, and you hear only when it couldn't. (gives; told)
  - The Orchestrator commits its own reading before each audit and the audit compares; a divergence is corrected in the run, and a repeated one stops the affected part. (means; agreed)
- Its working context is not refreshed as a remedy. (constraint; told)

### A better design noticed mid-flight

- It reaches you if it bears on the design, whatever it would cost. A trivial one never does. (gives; told)
  - The part it concerns waits while you decide; the rest continues. (means; confirmed)
- A plan that departs from a means is such a finding, not a breach. (gives; agent-proposed)

### Counsel discussions

- A philosophy says what you ratified; it need not be in your wording. What Counsel originated is marked as such, and nothing counts until you ratify it. (gives; told 2026-10-04: "'in your wording' is a bit too constraining, so that can be dropped." and, asked whether the form's rule that a philosophy keeps the owner's wording should change too, "Yes, change the requirements in the form as well.")

### Roles and models

- You can choose a model suited to each kind of work, and are not forced onto your strongest model for everything because one responsibility needs it. (gives; told 2026-10-04)
  - Roles are split by the nature of their work. A separate role, the Auditor, holds independent judgement of the Orchestrator's work: the value audit and goal-mode assessment. The Reviewer keeps checking the work for the Orchestrator. (means; agent-proposed, accepted 2026-10-04: "Yes, add it to the brief, Auditor is fine.")
  - A dispatch to the Auditor carries locations only; an account of the work in it is misuse on sight. (constraint; from the accepted record on the value audit)

### Closeout

- It leads with behaviour, scenario by scenario, with how to observe each. (gives; inferred)
  - The design document for the field touched is updated; its rules wait for the engineering philosophy. (means; confirmed)

### Limits

- It stacks on pull requests 72, 73 and 75; nothing merges until you judge the whole stack. (constraint; told)
- Goal mode for goals a check can decide keeps working as it does. (constraint; inferred)
- This run's plans would be the first authorized by the ratified brief and the audit, with no waiver from you. (inferred)

### Still his to settle before ratification

- Core scenarios for this initiative, on the run. Settled 2026-10-04 ("The scenarios you gave are fine as is."): you hand over a behaviour-only design that takes several plans, and come back to it built, having been asked nothing that didn't need you; a design-level finding reaches you mid-run, and the part it concerns has waited; a run that has stopped getting closer has stopped and told you; you put a cheaper model on the Reviewer and your strongest on the Auditor, and the run works as before.
- Core scenarios on how a Counsel discussion is handled. Asked for 2026-10-04: "I'd like to add some that concerns how Counsel discussions are handled too. Define them from what I already told you how I want to interact with a Counsel." Counsel offered seven; settled the same day: "'in your wording' is a bit too constraining, so that can be dropped. The last two scenarios you gave can be omitted. I feel they are less important than the others. Other ones, I'll take as an accepted scenario." The five accepted:
  - Starting from nothing. You open a Counsel session in a repository with no philosophy. After talking it through at length you hold a philosophy that says what you mean, and at no point did it feel like filling in a form.
  - Bringing an idea. You bring a rough idea. Counsel restates it as a person's experience so you can check it, weighs it against the philosophy and the repository as it stands, and where it sees something you missed or a better way it says so, naming the conventional answer. You end with a design you're comfortable with.
  - Unfamiliar ground. You are about to judge something you don't know well. Counsel explains what you need to know first, and only then asks.
  - Going too far. You describe an implementation detail that would constrain the build prematurely. Counsel says so before it is written down, and the choice stays yours.
  - Closing. Before you ratify, Counsel shows you what was discussed but left out and why, writes the watch list with you, and takes nothing as settled that you haven't said yes to in whole.
  - Omitted as less important: checking in on a project's state; a question from a run reaching him as a person's experience. Both remain behaviour the stack already describes; they are not core scenarios of this brief.
  - Note: every one of the five is judged by him in use; a run cannot demonstrate them, so they add nothing to what a run counts.
- The watch list. Settled 2026-10-04 ("the other two parts, seems fine to me."): anything that would have you reading plans again; a change to how goal mode behaves today; anything that weakens who may authorize or stop work.
- What Counsel left out, each drop confirmed 2026-10-04 by the same words, and each kept for a later discussion: the rules for design documents; enforcing Counsel's limits by tool settings; how a decision he delegates to Counsel is recorded; the two philosophies for this repository; the delivery failures between sessions.
- Nothing is left for him to settle but the ratification of the whole.

## Decisions pending ratification

- None.

## Facts

- None recorded here; facts in use are in the brief with their source.

## Assumptions

- None recorded here.
