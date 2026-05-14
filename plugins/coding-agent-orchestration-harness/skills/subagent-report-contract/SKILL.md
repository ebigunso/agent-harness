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
  - audience: common | worker | orchestrator | reviewer
    id: "RB-CAND-<short>"
    rule: "one-sentence repo rule"
    rationale: "why it prevents rework/risk"
    scope: "where it applies"
    example: "optional; use '' when none"

# Optional: harness_migration_candidates
harness_migration_candidates:
  - id: "HMC-<short>"
    category: review | validation | orchestration | delegation | rulebook | troubleshooting | adapter | validator | other
    proposed_home: "skill/reference/agent/validator/adr hint"
    generalized_rule: "cross-repo lesson or proposed global rule"
    trigger: "when this should apply"
    evidence_from_repo: "what happened in this repo"
    rationale: "why this is not merely repo-specific"
    suggested_change: "what a future harness-maintenance pass should update"

Notes:
- `validation_results` is the evidence contract for required and optional validation items.
- `ui_probes` is optional and records Worker-owned implementation-local UI probes. It does not satisfy Reviewer-owned validation automatically.
- `ui_probes[*].base_url` is required when `ui_probes` is present; use `n/a` when no URL applies and describe the command or setup in `notes`.
- `rule_candidates` are always repo-local and route by `audience` to the destination rules file.
- Use `audience: reviewer` only when the rule candidate affects review policy, review-risk hotspots, Reviewer-owned evidence, or recurring review misses.
- Use `harness_migration_candidates` for cross-repo harness improvements that should be staged for later harness-maintenance work.
- Do not emit `skill_candidates`; use `lesson_candidates` for deviations and `harness_migration_candidates` for proposed harness-global migrations.

---

## Optional: ui_probes

Include `ui_probes` only when a bounded Worker UI probe was run or materially affected implementation.
This key does not satisfy Reviewer-owned validation automatically.

Schema:

ui_probes:
  - base_url: "http://localhost:3000"
    flow: "Open settings page and toggle dark mode"
    result: pass | fail | skipped
    evidence: "Screenshot path or brief observation"
    notes: "Fixes made or reason skipped"

Guidance:
- `ui_probes[*].base_url` is required when `ui_probes` is present; use `n/a` when no URL applies and describe the command or setup in `notes`.
- Do not use `ui_probes` as a substitute for Reviewer-owned validation evidence.

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
    promotion_target: repo_rule | harness_migration | troubleshooting | residual_risk
    suggested_destination: "optional; docs/coding-agent/rules/reviewer.md | docs/coding-agent/skill-candidates.md | docs/coding-agent/lessons.md | ..."

Guidance:
- Keep candidates atomic (one failure category each).
- Prefer promoting prevention into repo docs/rules when it is repo-specific.
- Use `harness_migration` when the prevention is reusable across repositories and should be staged for a later harness-maintenance pass.

---

## Filling notes

- files_changed: include only files actually modified/created/deleted.
- commands_run: if you cannot run a required command, use result=skipped and explain.
- validation_results: include every validation item assigned in the task contract; required worker-owned failures/skips cannot accompany `status: done` unless the skip has explicit waiver evidence.
- ui_probes: include only if a bounded Worker UI probe was run or materially affected implementation. Do not use it as a substitute for Reviewer-owned validation evidence.
- If required validation evidence is missing and cannot be produced, status should be blocked (not done).
