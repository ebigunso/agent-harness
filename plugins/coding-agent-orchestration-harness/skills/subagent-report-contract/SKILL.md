---
name: subagent-report-contract
description: Standardizes Worker subagent final YAML output for machine processing, including validation evidence, rule candidates, and (when deviations occur) lesson candidates. Use when defining or updating Worker reporting requirements.
---

# Skill: subagent-report-contract

This skill standardizes the Worker subagent final output format so the Orchestrator can integrate results reliably.

---

## Absolute requirements

- The Worker’s final message MUST contain exactly one YAML code block and nothing else.
- The YAML top-level keys and types must be respected (missing required keys breaks integration).

---

## YAML schema (required keys)

task_id: "Task_2"              # from Orchestrator prompt
status: done | blocked | failed

summary: |-
  1–5 lines: what changed / what remains (include expectation vs reality when blocked/failed)

files_changed:
  - path: "src/..."
    change: modified | created | deleted
    intent: "one-line intent"

commands_run:
  - command: "npm run test:unit"
    result: pass | fail | skipped
    notes: "brief failure/skip reason"

validation_results:
  - kind: command | manual | e2e | review
    required: true | false
    owner: worker | reviewer | orchestrator | user
    detail: "what was validated"
    status: pass | fail | skipped
    evidence: "brief proof or failure excerpt"

tests:
  ran: true | false
  notes: "what was validated / what remains unvalidated"

blockers:
  - "required if blocked/failed; otherwise []"

questions_for_orchestrator:
  - "max ~3 recommended"

assumptions:
  - "assumptions made; [] if none"

rule_candidates:
  - audience: common | worker | orchestrator
    intended_home: repo_specific | global_candidate
    id: "RB-CAND-<short>"
    rule: "one-sentence reusable rule"
    rationale: "why it prevents rework/risk"
    scope: "where it applies"
    example: "optional; use '' when none"

Notes:
- `validation_results` is the evidence contract for required and optional validation items.
- `rule_candidates` route by `audience` to the destination rules file, then by `intended_home` within that file.
- Do not emit `skill_candidates`; use `lesson_candidates` for deviations and route skill ideas through their own repo docs.

---

## Optional: lesson_candidates (recommended when deviations occur)

Lesson candidates are NOT rules. They are “what went wrong / why / how to prevent it”
so Orchestrator can log atomic lessons and promote them later.

Include lesson_candidates when:
- status is blocked/failed, OR
- required validation failed unexpectedly, OR
- you needed unusual recovery steps, OR
- you discovered a significant assumption mismatch, OR
- you needed a waiver/skip to proceed.

Schema:

lesson_candidates:
  - id: "LESSON-CAND-<short>"
    category: planning | delegation | validation | environment | review | docs | other
    deviation: "what went wrong / what required course correction (1 sentence)"
    root_cause: "why it happened (1 sentence)"
    prevention: "what would prevent recurrence (1 sentence)"
    promotion_target: "rules/* | references/* | troubleshooting/* | global-skill"

Guidance:
- Keep candidates atomic (one failure category each).
- Prefer promoting prevention into repo docs/rules when it is repo-specific.
- Use global-skill only when it is clearly cross-repo.

---

## Filling notes

- files_changed: include only files actually modified/created/deleted.
- commands_run: if you cannot run a required command, use result=skipped and explain.
- validation_results: include every validation item assigned in the task contract; required worker-owned failures/skips cannot accompany `status: done` unless the skip has explicit waiver evidence.
- If required validation evidence is missing and cannot be produced, status should be blocked (not done).
