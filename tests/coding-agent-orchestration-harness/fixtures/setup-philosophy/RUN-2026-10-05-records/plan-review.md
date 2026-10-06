As returned by the agent; machine paths replaced by placeholders.

## Review: Draft plan, docs/coding-agent/plans/active/tally-could-not-read-plan.md

Status: APPROVED

Summary:
- The plan does exactly what the user's narrowed answer asks for: replace the failure sentence in `tally.py` with `tally could not read <path>.`, print no number, and exit non-zero. It drops the friendly sentence (N1) and the path-length fallback (N2), and it carries every product-philosophy line the change touches into its DoD and acceptance.
- Validation evidence: `validate_plan.py --mode balanced` printed "Plan validation passed." (exit 0). I found three MINOR wording issues and nothing that blocks approval.

Strengths:
- Every source checks out:
  - A1 matches `tally.py:8-12` (the "Cannot read the file." message on stderr, `SystemExit(1)`).
  - The pointer in `docs/coding-agent/rules/common.md` names `docs/product/what-tally-is-for.md`, and no engineering philosophy pointer exists.
  - The `README.md` == `21` check is in `common.md`, `worker.md` maps it, and I re-ran it and got `21`.
  - `docs/usage.md` says "an error and no count".
  - A repository grep finds "Cannot read the file." only in `tally.py` and the plan.
- Value-level operation: the plan itself carries the philosophy, so no value audit is needed between the draft and the close.
  - "one plain sentence and prints no number" becomes D1 and D2.
  - "number alone on one line" becomes D4 and N1.
  - "never changes the file" becomes an acceptance bullet and the Safety note.
- `Design` is in the full form, which is correct because the change touches a CLI output contract. The alternative (`Path(arg).name`) differs on structure (an added conversion) and on human (it hides the directory), and the plan says why the chosen design wins. The plan makes no fit claim about the project's direction, so none needs a source.
- The validation commands pin the requested contract exactly: stderr text, empty stdout, non-zero exit, and the success output unchanged. They do not pin implementation details.

Issues Found:
- [MINOR] Rule 12 (`plan-format/SKILL.md`) gap, D1 (plan line 12). "`<path>` is the argument as the user typed it" is a constraint the plan added while drafting. The request only says "names the file", and its example (`notes.txt`) fits a bare name. The `Design` section decides this choice, but `Planner-added requirements` lists only P1. The reason would hold under the chosen design: it shows what tally actually tried to open. So this is a missing listing, not a wrong requirement. The other items all trace to a source:
  - D2, D3, N1 and N2 come from the user's answer.
  - D4 and the never-writes bullet come from the philosophy and `common.md`.
  - The `docs` directory case is an instance of "unreadable".
  - P1 is listed, and its reason holds: the philosophy's "so it can be piped" and today's stream.
- [MINOR] A2's claim "checked by Task_1's validation" (plan line 50) is only half true. `tally.py:10` does support the catch claim, since PermissionError is an OSError and UnicodeDecodeError is a UnicodeError. But Task_1's validation runs only the missing-file case and the directory case; the permission and non-UTF-8 cases rest on the source alone.
- [MINOR] Internal contradiction. D1 says "writes exactly one line", but Notes (plan line 121) says "a path containing a newline prints it as given", which gives two lines. Either qualify D1 (one sentence, one line except for a path that contains a newline) or drop that edge case from Notes.

Recommendations:
- Add P2 for path-as-typed with the Design's reason, or reword D1 so the choice is cited to `Design`.
- In A2, change the wording to "missing and directory cases checked by Task_1's validation; permission and non-UTF-8 from the source".
- Fix the mismatch between D1 and Notes in whichever direction the Orchestrator prefers.
- Length is acceptable: about 120 lines, mostly template sections and the append-only logs. A1, A2 and the edge-case Notes come close to restating things the Worker can find cheaply (rule 10), but they are short.

Next Steps:
- Make the three wording fixes, or not, at the Orchestrator's discretion. None of them changes the tasks or the validation. Then go on to the plan-draft value audit and the user's approval, as the Progress Log states.

Questions for Orchestrator:
- The compatibility stance is `break` on an externally invoked CLI. That is justified here because the user explicitly asked for the new text, so this is not a silent break. Confirm that the user's approval of the plan is meant to cover the change of the old message text as well.

Quality routing note
- In-scope docs: plan-format/SKILL.md; engineering-quality-baselines core-principles.md and review-rubric.md Symmetric checks
- Out-of-scope docs: latent-risk references (the Design section touches no failure-degradation, hot-path or data-exposure change beyond echoing the user's own argument)
- Top risks: contract (CLI message text)
- Risk profile: low; one string in a single script, revert is one commit
- Validation depth: targeted
- Required checks: [{name: validate_plan.py --mode balanced, status: pass, evidence: "Plan validation passed." exit 0}]
- Optional recommended checks: [{name: README.md == 21 baseline, status: pass, evidence: printed 21}]
- At Risk items: []
- Residual risk / follow-up: the permission-denied and non-UTF-8 paths are not exercised by any validation command

Paths: docs/coding-agent/plans/active/tally-could-not-read-plan.md, tally.py, docs/product/what-tally-is-for.md, docs/usage.md, docs/coding-agent/rules/common.md, docs/coding-agent/rules/worker.md, REQUEST.md

APPROVED
