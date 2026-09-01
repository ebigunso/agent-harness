# Running Custom Playwright Code

Use `run-code` to execute arbitrary Playwright code for advanced scenarios not covered by CLI commands.

## Syntax

```bash
playwright-cli run-code "async page => {
  // Your Playwright code here
  // Access page.context() for browser context operations
}"
```

The body is standard Playwright API — write it as you would in any Playwright script. The function receives the session's current `page`; a returned value is serialized and printed as the command output.

```bash
# Example: return a value
playwright-cli run-code "async page => {
  return await page.title();
}"
```
