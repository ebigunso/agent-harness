# Test Generation

Every action you perform with `playwright-cli` emits the corresponding Playwright TypeScript code in its output, ready to copy into a test file.

## Example Workflow

```bash
# Start a session
playwright-cli open https://example.com/login

# Take a snapshot to see elements
playwright-cli snapshot
# Output shows: e1 [textbox "Email"], e2 [textbox "Password"], e3 [button "Sign In"]

# Actions emit code
playwright-cli fill e1 "user@example.com"
# Ran Playwright code:
# await page.getByRole('textbox', { name: 'Email' }).fill('user@example.com');

playwright-cli click e3
# Ran Playwright code:
# await page.getByRole('button', { name: 'Sign In' }).click();
```

Collect the emitted lines into a `@playwright/test` test body. Generated code captures actions only — add assertions yourself.
