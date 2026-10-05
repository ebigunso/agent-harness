# Readings: The value audit at a plan's draft and close

What the Orchestrator writes for the audit to compare. The auditor opens this file only after its grades are fixed.

## Readings

### `audit-at-plan-draft-and-close-plan.md`, plan draft

Item | reading | statement relied on

- Definition of Done: two audit positions in a plan-mode run, none at a wave boundary | covered | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between."
- Definition of Done: a goal-mode run's audit moments unchanged | covered | brief: "In a goal-mode run it runs as the accepted record on goal mode states."
- Definition of Done: the plan review reports a plan that is unacceptably long | covered | brief: "A plan review catches a plan that is unacceptably long."
- Definition of Done: the fixed dispatch template byte-identical | extends | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between."
- Definition of Done: validators and review | covered as the repository's rule; no statement needed
- Definition of Done: the run closes with its branch published and a pull request opened, nothing merged | covered | standing approval in `docs/coding-agent/rules/common.md` on publishing a finished, reviewed run
- Design: two positions in the text, not a conditional wave-boundary audit | covered | brief: "and nowhere between"
- Compatibility stance: break for the plan-mode cadence; goal mode and the template preserved | covered | brief: "In a goal-mode run it runs as the accepted record on goal mode states."
- Planner-added: one version bump | covered as mechanics; no statement needed
- Non-goals: no numeric limit; no record; goal mode and the template untouched | extends | brief, the same two lines
- A1: the template keeps its three position values | extends | brief: "In a goal-mode run it runs as the accepted record on goal mode states."
- Task_1 | covered | brief, the two amended lines
- Task_2 | covered | standing approval on publishing a finished, reviewed run
- Decision Log: no record proposed, no count | extends | brief: "A plan review catches a plan that is unacceptably long."
- This run audited at its plan's draft and close only | covered | brief: "and nowhere between"

#### The audit's comparison, plan draft (2026-10-05), as returned

- `Reading compared:`
  - DoD 1: agrees
  - DoD 2: agrees
  - DoD 3: agrees
  - DoD 4: diverges (Orchestrator: extends, on "It runs by position…"; auditor: internal mechanics, not audited)
  - DoD 5: agrees (covered against cited; the auditor quotes the pass condition where the Orchestrator named no statement)
  - DoD 6: agrees
  - Planner-added version bump: diverges in form only (Orchestrator: covered as mechanics; auditor: not audited, same classification)
  - Non-goals, read by the Orchestrator as one item, extends: diverges (auditor: template not audited; goal mode, no record and no numeric limit each cited)
  - A1: diverges (Orchestrator: extends; auditor: internal mechanics, not audited)
  - Task_1: agrees
  - Task_2: agrees
  - Decision Log 1: diverges (Orchestrator: extends; auditor: cited, the entry adds nothing to the brief's statement)
  - Decision Log 2: unread
  - The Orchestrator also read three things the mandate does not list as items, and they were not graded: Design, Compatibility stance, and "this run audited at its draft and close only".
- `Findings compared: none found` (the readings file records "None yet"; no departure from a means was noted on any item line)

Readings corrected after this comparison: the fixed template kept byte-identical, the template's three position values (A1) and the template non-goal are mechanics; the Decision Log's requirement challenge and the non-goals on goal mode, records and a numeric limit are covered by the brief's two amended lines.

### `audit-at-plan-draft-and-close-plan.md`, closeout

Item | reading | statement relied on

- Every item read under the plan-draft heading keeps its reading as corrected after that comparison, with these additions.
- The text as built: two positions in a plan-mode run, the wave-boundary entry, the per-wave revision and the checklist step gone | covered | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between."
- The mandate keeps one line saying that `wave boundary` is a goal run's assessment event; its goal-run section and the template unchanged | covered | brief: "In a goal-mode run it runs as the accepted record on goal mode states."
- The plan-review snippet's line on a plan that is unacceptably long, with the fact to weigh | covered | brief: "A plan review catches a plan that is unacceptably long."
- Manifests at 0.29.0 | covered as mechanics; no statement needed
- Decision Log: draft review applied (design comparison, compatibility stance, the added measure dropped) | covered | brief, the two amended lines
- Worker's judgement calls (the sentence on the next audit left as it reads; where the mandate's pointer sits) | covered as mechanics; no statement needed
- Orchestrator's edit: this morning's lesson marked as overtaken | covered as mechanics; no statement needed
- Divergences at plan draft corrected in the readings only | covered | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between."
- This run audited at its plan's draft and close and at no wave boundary | covered | brief: "and nowhere between"

#### The audit's comparison, closeout, second dispatch (2026-10-05), as returned

- `Reading compared:`
  - DoD 1, 2, 3, 6, Task_1, Task_2: agrees (covered against cited)
  - DoD 4, A1, the template non-goal: agrees (read as mechanics after the plan-draft correction; not audited)
  - DoD 5: agrees (covered; the auditor quotes the pass condition)
  - Non-goals on goal mode, records and a numeric limit; Decision Log 1: agrees (covered against cited, as corrected)
  - Decision Log 2: agrees (covered against cited)
  - Planner-added version bump and manifests at 0.29.0: diverges (Orchestrator: covered as mechanics, no statement needed; auditor: user-facing because the installed version is visible, inferred from "the package validators pass" and "It ships as a first version.")
  - The text as built (two positions, wave-boundary entry and checklist step gone): agrees. The per-wave revision, read inside that item as covered: diverges in class only (auditor: internal mechanics, not audited)
  - The mandate's one line on `wave boundary`, goal-run section and template unchanged: agrees
  - The plan-review snippet's line: agrees
  - Worker's judgement calls: agrees (mechanics; not audited)
  - Orchestrator's edit to the lesson: agrees (mechanics; not audited)
  - This run audited at its plan's draft and close only: agrees (covered against cited)
  - "Divergences at plan draft corrected in the readings only": not an item of the plan or the range; not graded
  - Unread by the Orchestrator: the changed wording of the gate on the position; the new run record; the authorization ruling on the plan-draft verdict; the second closeout dispatch; research waived; the untracked `.claude/` files; the untracked brief
- `Findings compared:` the one finding (a second auditor opened a readings file before grading; read as trivial): agrees. Acting on it would change no grade and nothing anyone experiences from the feature beyond a spared dispatch. No departure from a means was noted on any item line; the brief carries no kind marks.

Reading corrected after this comparison: the version bump | extends | brief: "the package validators pass"

## Findings

- A second auditor opened a readings file before grading (the first closeout dispatch of this plan; the earlier one was in the design-led long runs run), each time by building its inputs from a file listing. Each caught itself and returned ungraded, at the cost of one dispatch. Reading: trivial; nothing the owner experiences changes, since no grade was given on a seen reading. Not built in this plan, whose brief lines do not cover it: the mandate could give the literal exclude pathspecs to copy, so that the safe command is the default one.
