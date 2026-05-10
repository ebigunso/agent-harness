# Final Response Contract

Use this structure for user-facing closeout after harness work.

## Required Shape

1. Outcome: `done` or `blocked`.
2. Changed files/artifacts.
3. Validation summary.
4. Review summary.
5. Repo rule updates.
6. Skill staging updates.
7. Questions or blockers, max 3.

## Outcome

State whether the work is done or blocked. Do not report done when required evidence is missing.

## Changed Files / Artifacts

List meaningful files and artifacts. Keep the list scoped to the completed work.

## Validation Summary

Include required checks with status:

- `pass`;
- `fail`;
- `skipped` with reason;
- `waived` with evidence.

Mention checks that could not be run.

## Review Summary

For non-trivial work, include Reviewer status:

- `APPROVED`;
- `NEEDS_REVISION`;
- `FAILED`;
- waived with evidence.

If UI/E2E evidence was required or run, summarize flows/viewports and artifact paths.

## Rule And Skill Updates

Report repo rule updates and skill staging updates. If none occurred, say so briefly.

## Questions / Blockers

Ask at most three questions. If no questions remain, omit this section or state that no blockers remain.
