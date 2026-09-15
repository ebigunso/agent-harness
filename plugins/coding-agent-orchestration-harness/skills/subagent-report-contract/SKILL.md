---
name: subagent-report-contract
description: The contract for the YAML report a Worker subagent returns as its final message, and the validator for it. Use when producing a Worker report, validating one, or defining or updating Worker reporting requirements.
---

# Skill: subagent-report-contract

This skill standardizes the Worker subagent final output format so the Orchestrator can integrate results reliably.

---

## Absolute requirements

- The Worker's final message MUST contain exactly one YAML code block and nothing else.
- The YAML top-level keys and types must be respected (missing required keys breaks integration).
- Do not emit `skill_candidates`; use `lesson_candidates` for deviations and `harness_migration_candidates` for proposed harness-global migrations.

---

## Required keys

- `task_id`: the `Task_X` id from the Orchestrator prompt.
- `status`: `done | blocked | failed`.
- `summary`: 1-5 lines on what changed and what remains; when blocked or failed, expectation versus reality.
- `files_changed`: every file actually `modified | created | deleted`, each with a one-line intent; nothing else.
- `commands_run`: each command with `pass | fail | skipped` and a note; emit it, though validators do not require it.
- `validation_results`: the evidence list, one entry per validation item assigned in the task contract, with `kind: command | manual | e2e | review`, `required`, `owner: worker | reviewer | orchestrator | user`, `status: pass | fail | skipped`, and `evidence`.
- `tests`: whether tests ran and what remains unvalidated; emit it, though validators do not require it.
- `blockers`: required non-empty when blocked or failed; otherwise `[]`.
- `questions_for_orchestrator`: max ~3 recommended.
- `assumptions`: assumptions made; `[]` if none.
- `rule_candidates`: repo-local rule proposals, each routed to the destination rules file by its audience: common | worker | orchestrator | reviewer
  - Use `audience: reviewer` only for review policy, review-risk hotspots, Reviewer-owned evidence, or recurring review misses.

Evidence rules:
- A required worker-owned failure or skip cannot accompany `status: done` unless the skip carries explicit waiver evidence; if required validation evidence is missing and cannot be produced, status is `blocked`, not `done`.
- When a required command did not run, `evidence` names the skipped command and its reason, including waiver evidence when applicable.

---

## Optional blocks (when each applies)

- `ui_probes`: only when a bounded Worker UI probe ran or materially affected implementation. A Worker UI probe does not satisfy Reviewer-owned validation.
- `lesson_candidates`: when status is blocked or failed, required validation failed unexpectedly, unusual recovery steps were needed, a significant assumption mismatch was discovered, or a waiver or skip was needed to proceed. Lesson candidates are not rules; they record what went wrong, why, and how to prevent it so the Orchestrator can log atomic lessons and promote them later.
- `harness_migration_candidates`: for cross-repo harness improvements that should be staged for later harness-maintenance work.

---

## Design alerts (convention, not a schema field)

A design alert is a structured `blockers` or `questions_for_orchestrator` entry raised when a cleaner fix would need a change the task is not authorized to make on its own: a shared type, schema, boundary, or constraint, whether it sits outside `owns` or inside `owns` as a contract other code depends on, that the plan could change on request. The entry states three things: the boundary, the cleaner alternative, and the cost delta between them. If a fix that is not a workaround exists inside `owns`, take it and raise the alert under `questions_for_orchestrator`; if the only fix inside `owns` is a workaround, raise it under `blockers` and await an Orchestrator ruling.

---

## References

- Full schema with every field, enum, and filling note: `references/schema.yaml`.
- Worked reports (done, done with a UI probe, blocked, done with rule and migration candidates): `references/examples.md`.
- Validation: `python scripts/validate_worker_report.py --file <report.yaml>`; `--message-file <final-message.md>` also enforces the one-YAML-block rule; add `--task-contract <task.yaml>` to check that every required worker-owned validation item has a result.
