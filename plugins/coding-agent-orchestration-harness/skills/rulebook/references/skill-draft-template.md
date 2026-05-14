# Harness Migration Draft Template

Use this structure for `docs/coding-agent/skill-drafts/HMC-YYYYMMDD-short-kebab-description.md` when a harness migration candidate is too large for a single backlog entry.

```md
# HMC-YYYYMMDD-short-kebab-description

## Problem

- <what happened and why the current harness did not catch it>

## Generalized Rule

- <cross-repo rule or workflow improvement>

## Trigger

- <when this should apply>

## Proposed Owner / Home

- <skill, reference, agent adapter, validator, or ADR hint>

## Examples

- <repo evidence or abstract examples>

## Validation Idea

- <how a future harness-maintenance pass could validate the change>

## Open Questions

- <unknowns to resolve before editing bundled harness content>
```

Drafts are proposals for later harness-maintenance PRs or issues. They are not active repo rules and should not instruct ordinary target-repository agents to edit bundled harness content.
