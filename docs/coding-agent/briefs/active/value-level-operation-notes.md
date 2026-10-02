# Discussion notes: value-level operation

Unratified. Kept by Counsel during discussion with ebigunso. Nothing here gates anything; the value audit does not read this file. Items move out of here when ratified into the brief, a philosophy, or a decision record.

## Open questions and ideas

- 2026-10-01, ebigunso: cover not only plan mode but the longer-horizon goal mode, which may be better redefined as a longer-horizon mode rather than a goal mode. Expectation: delegating at brief level produces larger chunks of work that suit the longer-horizon mode. Asked how the two would mix best.
  - Counsel's reading (not ratified): goal mode's lifecycle (envelope ratified once, journal, checkpoint commits, fresh-context assessor, stall detection, graded escalation) is the machinery an unsupervised long run needs, and the value audit is the same separation the goal assessor already embodies. What goal mode lacks is admission for work whose end state is judged by a person; the brief supplies that, with pass conditions marked agent-checkable or human-only, and the loop ends in "candidate ready" for the human-only ones instead of "met".
  - Possible shape: an outer longer-horizon loop governed by the brief and an envelope, producing a sequence of plan-mode chunks (Task_X waves, Workers, Reviewer, audit at each plan), with stack acceptance by the person directing the work at each judgeable behaviour. A one-plan initiative is the degenerate case; a fully agent-checkable goal (lint to zero) is the special case that keeps a countable gap.
  - Cost: it reopens the goal-mode records (ADR-D-0009, D-0011, D-0027 to D-0031) and the progress definition for human-judged conditions. Counsel suggests a second initiative after the current one ships, not a scope expansion of it.

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

## Decisions pending ratification

- None.

## Facts

- None recorded here; facts in use are in the brief with their source.

## Assumptions

- None recorded here.
