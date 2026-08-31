# Browser Session Management

Run multiple isolated browser sessions concurrently with state persistence.

## Named Browser Sessions

Use `-s` flag to isolate browser contexts (independent cookies, storage, IndexedDB, cache, history, tabs):

```bash
playwright-cli -s=auth open https://app.example.com/login
playwright-cli -s=public open https://example.com

# Commands are isolated by browser session
playwright-cli -s=auth fill e1 "user@example.com"
playwright-cli -s=public snapshot
```

When `-s` is omitted, commands use the default browser session.

## Browser Session Commands

```bash
# List all browser sessions
playwright-cli list

# Stop a browser session (close the browser)
playwright-cli close                # stop the default browser
playwright-cli -s=mysession close   # stop a named browser

# Stop all browser sessions
playwright-cli close-all

# Forcefully kill all daemon processes (for stale/zombie processes)
playwright-cli kill-all

# Delete browser session user data (profile directory)
playwright-cli delete-data                # delete default browser data
playwright-cli -s=mysession delete-data   # delete named browser data
```

## Environment Variable

Set a default browser session name via environment variable:

```bash
export PLAYWRIGHT_CLI_SESSION="mysession"
playwright-cli open example.com  # Uses "mysession" automatically
```

## Persistent Profile

By default, the browser profile is kept in memory only. Use `--persistent` flag on `open` to persist the browser profile to disk:

```bash
# Use persistent profile (auto-generated location)
playwright-cli open https://example.com --persistent

# Use persistent profile with custom directory
playwright-cli open https://example.com --profile=/path/to/profile
```

## Browser Session Configuration

Configure a browser session with specific settings when opening:

```bash
playwright-cli open https://example.com --config=.playwright/my-cli.json
playwright-cli open https://example.com --browser=firefox
playwright-cli open https://example.com --headed
```
