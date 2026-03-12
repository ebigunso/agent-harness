---
name: skills-maintenance
description: Maintain first-party skills and govern skill updates. Use when creating, reviewing, or updating a skill's trigger description, structure, provenance handling, bundled references, or maintenance rules, and when deciding whether a change belongs in SKILL.md, references/*, or should instead go through skill-creator for draft, eval, or packaging work.
---

# Skill: skills-maintenance

This skill defines how to maintain first-party skills without turning SKILL.md into a procedural runbook or casually mutating upstream content.

---

## Core rules (always apply)

1) Triggerability starts in frontmatter
- Treat the frontmatter description as the primary trigger surface.
- Write it description-first: say what the skill does, then add concrete "use when" cues that match likely user phrasing and contexts.
- Do not rely on body-only trigger cues for critical routing.

2) Keep SKILL.md lean
- SKILL.md should contain routing, scope boundaries, and core rules only.
- Move procedures, checklists, templates, and examples into references/*.
- If a reference becomes universally mandatory, promote only the minimal always-on rule back into SKILL.md.

3) Respect provenance
- Treat third-party or unknown-provenance skills as read-only unless the user explicitly approves editing them.
- Prefer a first-party wrapper skill for local governance or policy overlays instead of modifying upstream content.

4) Run a final ambiguity pass before finishing
- Before concluding a skill change, do a final pass for trigger precision, taxonomy alignment, and evidence-template enforceability.
- Use the reference checklist for this pass.

5) Route to skill-creator only when that workflow is actually needed
- Use skill-creator for open-ended draft creation, eval or benchmark loops, packaging, or description-optimization workflows.
- Do not invoke skill-creator for routine first-party maintenance when this skill alone is sufficient.

---

## Progressive disclosure (read only what you need)

If you are shaping or reviewing the frontmatter description, scope boundary, or SKILL.md versus references split:
- Read references/frontmatter-and-structure.md

If you need provenance rules or need to decide whether a skill may be edited directly:
- Read references/provenance-governance.md

If you are about to finish a skill change and need the required QA pass:
- Read references/final-ambiguity-pass.md

If draft creation, evals, benchmarks, packaging, or description-optimization work is actually required:
- Switch to skills/skill-creator/SKILL.md
