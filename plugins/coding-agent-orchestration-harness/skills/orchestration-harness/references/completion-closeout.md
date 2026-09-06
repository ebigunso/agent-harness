# Completion Closeout

Use this reference before declaring a Task_X, phase, wave, or full plan complete.

## Task_X Done Criteria

Done/blocked conditions: `SKILL.md` Validation Gate (canonical). Additionally confirm:

- Worker report status is `done`;
- any files changed outside `owns` are minimal, justified, and reported.

Worker `done` does not imply plan `done`.

## Plan Done Criteria

`SKILL.md` Completion Closeout Gate (canonical).

## Blocked State

`SKILL.md` Validation Gate and Completion Closeout Gate (canonical). Reviewer status `NEEDS_REVISION` or `FAILED` is not approval.

## Closeout Procedure

1. Parse Worker and Reviewer outputs.
2. Run Worker report validation when available.
3. Confirm the `SKILL.md` Validation Gate and Completion Closeout Gate conditions hold, including targeted rule refresh when rule-source files were edited.
4. Update Progress Log and Decision Log.
5. Move completed active plan to `docs/coding-agent/plans/completed/` when applicable.
6. Only then report final done.

Before final done, sweep the plan's Decision Log for entries that meet the ADR warrant criteria in `skills/durable-docs-authoring/references/adr.md` but have no ADR proposed; propose each missing ADR or record the user's decline.

Pre-merge value audit after churn: if the work accumulated repeated fix rounds on one area, apply the value-audit appendix in `skills/engineering-quality-baselines/references/long-horizon-audit.md` before merge — triggered by churn, never run continuously.

When a structured closeout summary is available, use the plugin-root-relative `skills/wave-integration/scripts/validate_closeout.py` before final done.
