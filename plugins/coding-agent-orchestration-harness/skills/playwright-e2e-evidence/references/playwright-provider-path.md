# Playwright Provider Path

Use this reference only when the generic browser-validation contract is being executed with `playwright-cli`.

## Required provider fields

- Set `provider: "playwright-cli"` in the spec or task context.
- Set `artifact_root: ".playwright-cli"`.
- Save screenshots and related evidence under `.playwright-cli/` and reference those paths directly in the evidence payload.

## Execution guidance

- Use the `playwright-cli` skill for concrete commands and session handling.
- Keep the run bounded to the requested flows, viewports, and evidence requirements.
- Preserve any provider-native artifacts needed for review, such as screenshots, snapshots, traces, or videos.

## Example mapping

- Generic contract: `provider`, `artifact_root`, required screenshots, console findings, network findings.
- Playwright path: `provider: "playwright-cli"`, `artifact_root: ".playwright-cli"`, screenshot paths like `.playwright-cli/home.png`.
