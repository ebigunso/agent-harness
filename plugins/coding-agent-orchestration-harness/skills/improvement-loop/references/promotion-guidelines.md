# Promotion Guidelines (Lesson → Durable Prevention)

Use these rules to decide where prevention belongs.

## Promote to repo rules (docs/coding-agent/rules/*.md) when:
- the prevention is a behavior constraint or workflow guardrail
- it applies broadly within the repo (or is likely cross-repo)
- it can be expressed as a short, testable rule

## Promote to a first-party skill or reference when:
- the prevention is a reusable workflow or tool integration
- it benefits multiple repos/tasks
- an existing first-party skill is the natural long-term owner
- it would otherwise bloat Orchestrator instructions or repo rules

## Create or route to a wrapper skill when:
- the lesson belongs in a durable first-party governance skill rather than repo-local staging
- the procedure should live in the skill's `SKILL.md` or `references/*`, not in ad hoc draft files

## Promote to troubleshooting knowledge when:
- the lesson is about a recurring environment/tool failure
- it has a repeatable “symptom → cause → safe steps” structure

## Severity heuristic
- If it caused broken output or wasted significant time → always record a lesson and propose prevention.
- If it repeats twice → promotion is required (rule or skill), not optional.
