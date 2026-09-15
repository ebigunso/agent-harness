---
name: improvement-loop
description: Self-improvement loop for Orchestrator-driven workflows. Use when a hard gate was missed (required validation or evidence skipped, a wrong done/blocked state, a safety or policy gate miss), when a review, CI, or human finding arrives that the harness should have caught, or when a user correction changes a durable default (workflow, validation, scope). Records the lesson and states the durable default change before ending the turn; low-signal corrections (tone, wording, a one-off format) are applied without a lessons entry.
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

1) Close the correction loop
Before ending the turn, append the lesson entry for each capture trigger in rule 2 that occurred, and state any durable default change.

2) One capture rule
- Record a lesson before ending the turn when any of these occurred:
  - a hard gate was missed (required validation or evidence skipped, a wrong done/blocked state, a safety or policy gate miss)
  - a review, CI, or human finding arrived that the harness should have caught
  - a correction changed a durable default (workflow, validation, scope)
- Low-signal corrections (tone, wording, a one-off format) are applied in the current task without a lessons entry.
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

6) Session-start usage
Before non-trivial work, skim recent or relevant entries in `docs/coding-agent/lessons.md` and apply them proactively.

---

## Progressive disclosure (read only what you need)

If you need a lessons file template:
- Read references/lessons-template.md

If you need a single lesson entry template:
- Read references/entry-template.md

When classifying a lesson or deciding whether to promote it — promotion is mandatory on a lesson's second occurrence — read `references/promotion-guidelines.md`.

If a human reviewer, Copilot, CI, Reviewer, or another source finds an issue the harness should have caught:
- Read references/review-finding-triage.md
