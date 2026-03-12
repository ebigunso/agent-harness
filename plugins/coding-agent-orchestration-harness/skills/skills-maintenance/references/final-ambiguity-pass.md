# Final Ambiguity Pass

Use this before marking a skill change complete.

## Required checks

### 1) Trigger precision

- The description states what the skill does and when to use it in concrete, searchable language.
- Likely user phrasings map cleanly to the skill.
- No critical trigger cue is buried only in the body or only in references/*.

### 2) Taxonomy alignment

- The skill name, frontmatter description, and body agree on the same ownership boundary.
- Responsibilities do not materially overlap a neighboring first-party skill without an explicit routing boundary.
- References reinforce the same taxonomy instead of introducing competing categories.

### 3) Evidence-template enforceability

- Any required output or report shape is concrete enough to validate.
- Mandatory fields or sections are named explicitly rather than implied.
- Checklists and templates live in references/* unless they are truly always-on core rules.

## Exit condition

- If any item is still ambiguous, tighten the frontmatter, boundary text, or reference doc before finishing.
- If the change actually requires draft creation, evals, benchmarks, packaging, or description optimization, hand off to skill-creator instead of extending this skill.
