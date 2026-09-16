---
name: playwright-cli
description: Provider-specific execution path for browser automation with playwright-cli (commands, run-code, artifact conventions). Use when a browser automation provider has been selected for the task and it is playwright-cli.
---

# Browser Automation with playwright-cli

This skill is a concrete provider-specific execution path for the generic browser validation contract defined by `playwright-e2e-evidence`.
When that contract selects `playwright-cli`, store provider artifacts under `.playwright-cli/`.

## Provider details

- Use `playwright-cli --help` or `playwright-cli <command> --help` for commands and options.
- `run-code` receives the current page: `playwright-cli run-code "async page => { return await page.title(); }"`. Returned values are serialized to command output.
- IndexedDB has no dedicated subcommand; use `run-code`.
- Never commit storage state files containing authentication tokens.
