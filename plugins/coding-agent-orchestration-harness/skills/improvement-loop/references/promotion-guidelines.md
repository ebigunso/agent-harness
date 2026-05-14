# Promotion Guidelines (Lesson → Durable Prevention)

Use these rules to decide where prevention belongs.

## Promote to repo rules (`docs/coding-agent/rules/*.md`) when:
- the prevention is a behavior constraint or workflow guardrail
- it applies broadly within the repo
- it can be expressed as a short, testable rule

## Stage as a harness migration candidate when:
- the prevention is a reusable workflow or tool integration
- it benefits multiple repos/tasks
- the likely durable owner is a first-party harness skill, reference, agent adapter, validator, or ADR
- applying it immediately would require editing bundled plugin content

Destination:
- `docs/coding-agent/skill-candidates.md`
- `docs/coding-agent/skill-drafts/*.md`, when useful

- Stage the proposal in `docs/coding-agent/skill-candidates.md` using the Rulebook `references/skill-candidates-file.md` format.
- Use `docs/coding-agent/skill-drafts/*.md` when the candidate needs a fuller draft before a harness-maintenance pass.

Only edit bundled harness content during an explicit harness-maintenance task.

## Create or route to a wrapper skill proposal when:
- the lesson may belong in a durable first-party governance skill rather than repo-local rules
- it would otherwise bloat Orchestrator instructions or repo rules
- the candidate needs a fuller draft before a harness-maintenance pass can decide ownership

## Promote to troubleshooting knowledge when:
- the lesson is about a recurring environment/tool failure
- it has a repeatable “symptom → cause → safe steps” structure
- it can live as a repo-local troubleshooting note or be staged as a harness migration candidate

## Severity heuristic
- If it caused broken output or wasted significant time → always record a lesson and propose prevention.
- If it repeats twice → promotion is required (repo rule, harness migration candidate, troubleshooting note, or accepted residual-risk record), not optional.
