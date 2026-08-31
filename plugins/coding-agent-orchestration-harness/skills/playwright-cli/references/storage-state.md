# Storage Management

Manage cookies, localStorage, sessionStorage, and browser storage state.

## Storage State

Save and restore complete browser state (Playwright storageState format: cookies plus per-origin localStorage).

```bash
# Save to auto-generated filename (storage-state-{timestamp}.json)
playwright-cli state-save

# Save to specific filename
playwright-cli state-save my-auth-state.json

# Load storage state from file, then reload page to apply
playwright-cli state-load my-auth-state.json
playwright-cli open https://example.com
```

## Cookies

```bash
playwright-cli cookie-list
playwright-cli cookie-list --domain=example.com
playwright-cli cookie-list --path=/api
playwright-cli cookie-get session_id
playwright-cli cookie-set session abc123
playwright-cli cookie-set session abc123 --domain=example.com --path=/ --httpOnly --secure --sameSite=Lax
playwright-cli cookie-set remember_me token123 --expires=1735689600
playwright-cli cookie-delete session_id
playwright-cli cookie-clear
```

For operations the CLI doesn't cover (e.g. adding multiple cookies at once), use `run-code` with standard Playwright API:

```bash
playwright-cli run-code "async page => {
  await page.context().addCookies([
    { name: 'session_id', value: 'sess_abc123', domain: 'example.com', path: '/', httpOnly: true }
  ]);
}"
```

## Local Storage

```bash
playwright-cli localstorage-list
playwright-cli localstorage-get token
playwright-cli localstorage-set theme dark
playwright-cli localstorage-set user_settings '{"theme":"dark","language":"en"}'
playwright-cli localstorage-delete token
playwright-cli localstorage-clear
```

## Session Storage

```bash
playwright-cli sessionstorage-list
playwright-cli sessionstorage-get form_data
playwright-cli sessionstorage-set step 3
playwright-cli sessionstorage-delete step
playwright-cli sessionstorage-clear
```

IndexedDB has no dedicated subcommands — use `run-code` for it.

## Authentication State Reuse

```bash
# Step 1: Login and save state
playwright-cli open https://app.example.com/login
playwright-cli snapshot
playwright-cli fill e1 "user@example.com"
playwright-cli fill e2 "password123"
playwright-cli click e3
playwright-cli state-save auth.json

# Step 2: Later, restore state and skip login
playwright-cli state-load auth.json
playwright-cli open https://app.example.com/dashboard
# Already logged in!
```

Note: by default, sessions run in in-memory mode, which is safer for sensitive operations; never commit storage state files containing auth tokens.
