# Discussion notes: design-led long runs

Unratified. Kept by Counsel. Nothing here gates anything; the auditor does not read this file. The discussion that led to the brief, with ebigunso's words dated, is in `value-level-operation-notes.md` in this folder, under "Open questions and ideas".

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

## Answered from his standing words during this run

- Nothing yet.

## Ruling given in the Orchestrator session (unratified; written by the Orchestrator)

- 2026-10-04, ebigunso, typed in the Orchestrator session: "Opus is an acceptable cheap model. Fable and Astra count as expensive, for me at the moment." and later "I've configured the codex worker and reviewer to use GPT-6.1-Sol instead of GPT-6 Astra so you can continue dispatching them freely." Recorded in this repository's `docs/coding-agent/rules/orchestrator.md` as his setting for the workspace. Unratified as a value statement; nothing is graded on it.
