---
name: improvement-loop
description: Self-improvement loop for Orchestrator-driven workflows. Use immediately after any user correction or behavior change request (workflow, validation, scope, tone, output format), after missed required gates (e.g., validation), or after review misses. Requires completing a post-correction micro-checklist before ending the turn.
---

# Skill: improvement-loop

This skill standardizes the “after correction → prevent recurrence” loop.

It introduces a repo-local Lessons Log and a promotion mechanism:
- Lessons Log (repo-local): `docs/coding-agent/lessons.md`
- Promotion targets:
  - repo rules (`docs/coding-agent/rules/*.md`)
  - repo lessons (`docs/coding-agent/lessons.md`)
  - harness migration candidates (`docs/coding-agent/skill-candidates.md`)
  - harness migration drafts (`docs/coding-agent/skill-drafts/*.md`)
  - troubleshooting notes under `docs/coding-agent/`

During ordinary target-repository work, runtime agents must not edit bundled/global harness skills, references, agents, validators, or plugin files. Cross-repo harness improvements must be staged in repo-local migration candidates or drafts. The exception is explicit harness-maintenance work where the target repository is the harness repository itself.

---

## Core rules (always apply)

1) Post-correction micro-checklist is mandatory
If this skill is active, you must complete the post-correction micro-checklist before concluding the turn.

- The checklist defines:
  - how to classify the correction
  - what to write into `docs/coding-agent/lessons.md`
  - when same-turn persistent-default or future-behavior reporting is required

2) Capture lessons at high signal; always capture hard-gate deviations
- Mandatory capture: append a lesson entry immediately for hard-gate deviations (missed required validation, required evidence missing, incorrect done/blocked state, safety/policy gate misses).
- High-signal capture: for non-gate corrections, append when the lesson is likely to prevent recurrence across future tasks (workflow drift, repeated review misses, repeated scope/dispatch mistakes).
- If capture is skipped for a low-signal correction, still apply a local prevention action in the current task.
- If the lessons file does not exist, create it using the template in references/lessons-template.md.

3) Lesson entries must be actionable
Each entry must contain:
- Symptom (what happened)
- Root cause (why it happened)
- Fix (what changed / what should have been done)
- Prevention (durable changes: rules/skills/plan/dispatch guardrails)
- Scope/tags (so it can be searched later)

4) Record durable default changes only when the correction changes future behavior
- If the user approves a new persistent default, workflow default, or other future-behavior change, state it back in the same turn as the correction handling.
- Do not treat ordinary plan refinements, one-off task tactics, or local execution adjustments as persistent defaults.
- If the user explicitly says the change is one-time only, record it as a one-time exception instead of a new default.

5) Promote lessons into prevention mechanisms
For each lesson, decide whether to stage:
- a repo rule candidate (rulebook)
- a harness migration candidate when a first-party skill, reference, agent adapter, validator, or ADR is the likely long-term owner
- a troubleshooting note or candidate under `docs/coding-agent/`
- a residual-risk record when prevention is intentionally not added

If prevention is unclear:
- still propose at least one small guardrail (e.g., “mandatory checklist before marking done”).

6) Session-start usage
Before non-trivial work, skim recent or relevant entries in `docs/coding-agent/lessons.md` and apply them proactively.

---

## Progressive disclosure (read only what you need)

If you need the post-correction checklist:
- Read references/post-correction-micro-checklist.md

If you need a lessons file template:
- Read references/lessons-template.md

If you need a single lesson entry template:
- Read references/entry-template.md

If you need guidelines for promoting lessons to rules/skills:
- Read references/promotion-guidelines.md

If a human reviewer, Copilot, CI, Reviewer, or another source finds an issue the harness should have caught:
- Read references/review-finding-triage.md
