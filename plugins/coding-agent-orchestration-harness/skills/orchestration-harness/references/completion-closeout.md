# Completion Closeout

Use this reference before declaring a Task_X, phase, wave, or full plan complete.

## Task_X Done Criteria

A Task_X is done only when:

- Worker report status is `done`;
- required Worker-owned validations are evidenced as `pass` or explicitly waived;
- no unresolved blockers remain;
- any files changed outside `owns` are minimal, justified, and reported.

Worker `done` does not imply plan `done`.

## Plan Done Criteria

A plan is done only when:

- all Task_X entries are done or explicitly waived;
- all required Worker-owned validation evidence exists;
- all required Reviewer-owned validation evidence exists;
- Reviewer status is `APPROVED` for non-trivial work unless waived;
- no unresolved blockers or required questions remain;
- required rule/lesson/skill governance follow-ups are recorded;
- plan status and active/completed location are updated.

## Blocked State

Report blocked, not done, when:

- required validation evidence is missing;
- required validation failed;
- required validation was skipped without waiver evidence;
- Reviewer status is `NEEDS_REVISION` or `FAILED`;
- a blocker remains unresolved;
- user-owned validation is pending and not acknowledged as pending.

## Closeout Procedure

1. Parse Worker and Reviewer outputs.
2. Run Worker report validation when available.
3. Confirm all required validation evidence is pass or waived.
4. Confirm no unresolved blockers remain.
5. Confirm Reviewer approval or waiver for non-trivial work.
6. Update Progress Log and Decision Log.
7. Move completed active plan to `docs/coding-agent/plans/completed/` when applicable.
8. Only then report final done.
