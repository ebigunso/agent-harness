# Harness Migration Candidates

Purpose:
- Stage cross-repository improvements discovered during target-repository work.
- Keep proposed harness-global changes separate from active repo rules.
- Provide a backlog for later harness-maintenance PRs or issues.

This file shape applies to:
- `docs/coding-agent/skill-candidates.md`
- optional fuller drafts under `docs/coding-agent/skill-drafts/*.md`

## Candidate IDs

Use:
- `HMC-YYYYMMDD-short-kebab-description`

If a Worker or Reviewer already supplied a stable `HMC-*` id, preserve it unless it conflicts with an existing candidate.

## Categories

Use one of:
- review
- validation
- orchestration
- delegation
- rulebook
- troubleshooting
- adapter
- validator
- other

## Candidate Template

```md
# Harness Migration Candidates

Purpose:
- Stage cross-repository improvements discovered during target-repo work.
- These are not active repo rules.
- These should be picked up by a later harness-maintenance PR/issue.

## Candidates

### HMC-YYYYMMDD-review-public-api-compatibility

- Status: staged
- Category: review
- Proposed home: `engineering-quality-baselines/references/review-latent-risk-public-api.md`
- Generalized rule:
  Public API changes should be reviewed for downstream compatibility, export completeness, and documented construction/import paths.
- Trigger:
  Public structs, enums, functions, traits, DTOs, exports, examples, or feature-gated public items change.
- Evidence from this repo:
  <brief finding / review miss / correction>
- Why this generalizes:
  <why this is likely useful outside this repository>
- Suggested change:
  <specific future harness update>
- Draft:
  `docs/coding-agent/skill-drafts/HMC-YYYYMMDD-review-public-api-compatibility.md`
```

If the candidate is small, use `Draft: none`. If the candidate is large, ambiguous, or likely to affect multiple harness files, create a fuller draft using `references/skill-draft-template.md`.

## Draft Template

Use `docs/coding-agent/skill-drafts/HMC-YYYYMMDD-short-kebab-description.md` with `references/skill-draft-template.md`.

Drafts are proposals for future harness-maintenance work. They are not active runtime instructions until a later harness-maintenance change applies them to bundled harness content.
