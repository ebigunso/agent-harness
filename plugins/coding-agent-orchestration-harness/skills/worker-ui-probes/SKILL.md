---
name: worker-ui-probes
description: Defines bounded Worker-owned UI probes for implementation feedback during UI tasks. Use when a Worker is assigned UI/frontend work and needs local browser checks without replacing Reviewer-owned E2E/visual validation.
---

# Worker UI Probes

Worker UI probes are implementation-local checks. They help the Worker catch obvious issues while editing.

## Core rules (always apply)

- Use only when the assigned Task_X includes UI/frontend behavior or the Orchestrator explicitly assigns a UI probe.
- Keep probes bounded: local URLs only unless explicitly authorized.
- Probe only the task-owned behavior; do not expand into full acceptance testing.
- Fix obvious issues within `owns`.
- Report probes in the Worker YAML when they materially affect implementation.
- A Worker probe does not satisfy Reviewer-owned validation unless the Orchestrator explicitly reassigns or waives that validation.
- Reviewer still owns independent E2E/visual acceptance evidence for non-trivial UI work.

## Evidence expectations

Report each material probe under `ui_probes` using the Worker report contract fields:

- `base_url` is always required; use the checked local URL, or `n/a` when no URL applies and record the command or setup note in `notes`;
- `flow`: flow or screen checked;
- `result`: `pass`, `fail`, or `skipped`;
- `evidence`: screenshot path, artifact path, or a brief observation when no artifact was captured;
- `notes`: fixes made, issue found, command/setup detail, or reason skipped.
