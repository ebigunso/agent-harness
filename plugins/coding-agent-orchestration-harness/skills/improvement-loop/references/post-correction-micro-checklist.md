# Post-Correction Micro-Checklist (Mandatory)

Complete this checklist before ending a turn where a correction event occurred.

## Step 1: Classify the correction (pick at least one)

- workflow/process (planning, delegation, parallelism, review gates)
- validation/verification (required checks, evidence, “done” criteria)
- scope/ownership (owns boundaries, what files can be touched, creep)
- tone/communication (conciseness, style, language, format)
- output contract (YAML schema, headings, file layout)
- assumptions/interpretation (misread requirement, missing constraints)
- tooling/environment (Windows quirks, CI mapping, dev server steps)

## Step 2: Write the lesson entry (repo-local)

Append an entry to `docs/coding-agent/lessons.md` using the entry template.

Minimum must-have fields:
- tags
- symptom
- root cause
- fix
- prevention (at least one durable guardrail)

If the correction is about “I forgot to do X before ending the turn,”
the prevention should include a *turn-closing guardrail* (e.g., checklist).

## Step 3: State same-turn durable behavior changes back to the user

If the correction establishes a real persistent default or future-behavior change, include in the same response where you acknowledge the correction:

- “Applied change:” (1 sentence)
- “New default going forward:” (1 sentence)

If the user explicitly said it is one-time only, replace the second line with:
- “One-time exception noted:” (1 sentence)

Do not add a “New default going forward” line for ordinary plan edits, local implementation tactics, or other non-durable adjustments.

Keep it short and concrete. Avoid vague promises.

## Step 4: Decide promotion (optional but recommended)

If the lesson is cross-repo and durable:
- stage it as a “Global Migration Candidate” in repo rule placeholders, OR
- update the owning first-party skill/reference if it is procedural or tool-heavy and already has a durable home.

If it is repo-specific:
- encode it in `docs/coding-agent/rules/*.md`.

If it is troubleshooting:
- stage it under troubleshooting knowledge for later migration.

## Completion criteria

You may end the turn only after:
- lessons.md is updated (or explicitly impossible with explanation), AND
- when a durable default or future-behavior change was made, the user-facing response includes “Applied change” + “New default going forward” (or “One-time exception noted”).
