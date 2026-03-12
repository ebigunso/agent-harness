# Frontmatter And Structure

Use this when writing or reviewing a skill's trigger surface or deciding what belongs in SKILL.md.

## Frontmatter-description-first

- The frontmatter description is the first-class trigger surface.
- Put what the skill does first, then add concrete use-when cues in the same description.
- Include likely task phrases, contexts, artifacts, or failure modes the host may need for routing.
- Do not hide critical trigger language only in the SKILL.md body or in references/*.

## SKILL.md versus references/*

Keep in SKILL.md:
- name, scope, and routing boundary
- always-on core rules
- pointers to deeper references

Move to references/*:
- step-by-step procedures
- checklists
- templates or examples
- longer decision criteria
- host-specific or tool-specific details

When in doubt, default to references/* and link it from the progressive-disclosure section.

## Boundary with skill-creator

- skills-maintenance owns routine first-party skill maintenance and governance.
- skill-creator owns open-ended draft authoring, eval harness setup, benchmarking, packaging, and description-optimization workflows.
- If the task does not actually require draft, eval, or packaging work, stay in skills-maintenance.
