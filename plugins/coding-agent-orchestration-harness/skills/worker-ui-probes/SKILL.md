---
name: worker-ui-probes
description: Defines bounded Worker-owned UI probes for implementation feedback during UI tasks. Use when a Worker is assigned UI/frontend work and needs local browser checks without replacing Reviewer-owned E2E/visual validation.
---

# Worker UI Probes

Worker UI probes are implementation-local checks. They help the Worker catch obvious issues while editing.

## Core Rules

- Use only when the assigned Task_X includes UI/frontend behavior or the Orchestrator explicitly assigns a UI probe.
- Keep probes bounded: local URLs only unless explicitly authorized.
- Probe only the task-owned behavior; do not expand into full acceptance testing.
- Fix obvious issues within `owns`.
- Report probes in the Worker YAML when they materially affect implementation.
- A Worker probe does not satisfy Reviewer-owned validation unless the Orchestrator explicitly reassigns or waives that validation.
- Reviewer still owns independent E2E/visual acceptance evidence for non-trivial UI work.

## Evidence Expectations

Report:

- base URL used; if no URL applies, record the command or setup note in `notes`;
- flow or screen checked;
- result;
- issue found and fixed, if any;
- artifact path, if a screenshot was captured.
