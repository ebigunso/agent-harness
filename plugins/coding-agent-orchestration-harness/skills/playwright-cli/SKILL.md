---
name: playwright-cli
description: Automates browser interactions for web testing, form filling, screenshots, and data extraction. Use when the user needs to navigate websites, interact with web pages, fill forms, take screenshots, test web applications, or extract information from web pages.
---

# Browser Automation with playwright-cli

This skill is a concrete provider-specific execution path for the generic browser validation contract defined by `playwright-e2e-evidence`.
When that contract selects `playwright-cli`, store provider artifacts under `.playwright-cli/`.

## Provider details

- Use `playwright-cli --help` or `playwright-cli <command> --help` for commands and options.
- `run-code` receives the current page: `playwright-cli run-code "async page => { return await page.title(); }"`. Returned values are serialized to command output.
- IndexedDB has no dedicated subcommand; use `run-code`.
- Never commit storage state files containing authentication tokens.
