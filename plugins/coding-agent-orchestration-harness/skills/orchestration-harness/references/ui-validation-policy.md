# UI Validation Policy

Use this reference when UI behavior, user flows, visual layout, routing, forms, or interaction correctness are affected.

## Three-Tier Model

| Tier | Owner | Purpose |
|---|---|---|
| UI probe | Worker | implementation feedback |
| UI research | Researcher | understand existing behavior before planning |
| UI acceptance evidence | Reviewer | independent validation |

## Worker UI Probes

Workers may run bounded UI probes when assigned UI/frontend work or when the Orchestrator explicitly assigns a probe.

Worker probes:

- are implementation-local checks;
- default to local URLs only;
- cover only task-owned behavior;
- help catch obvious issues while editing;
- must be reported in Worker YAML when they materially affect implementation.

Worker probes do not satisfy Reviewer-owned validation unless the Orchestrator or user explicitly reassigns or waives that validation.

## Researcher UI Research

Researchers may use bounded UI exploration to understand existing behavior before planning.

Researcher UI research should answer planning questions such as:

- what flow currently exists;
- which screens/components are involved;
- what evidence a Reviewer should collect later;
- what constraints or risks the plan should include.

Researcher findings do not replace Worker validation or Reviewer acceptance evidence.

## Reviewer UI Acceptance Evidence

When UI/user flows/layout correctness are impacted, non-trivial plans must include Reviewer-owned E2E/visual validation unless explicitly waived.

Reviewer evidence should include:

- selected provider and artifact root;
- base URL and startup/readiness details;
- flows and viewports checked;
- screenshots or other evidence paths when captured;
- console/network issues when relevant;
- status and failure details.

Use `playwright-e2e-evidence` for the E2E spec shape. Use `playwright-cli` when that is the selected provider.
