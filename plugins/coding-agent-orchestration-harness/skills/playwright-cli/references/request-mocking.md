# Request Mocking

Intercept, mock, modify, and block network requests.

## CLI Route Commands

```bash
# Mock with custom status
playwright-cli route "**/*.jpg" --status=404

# Mock with JSON body
playwright-cli route "**/api/users" --body='[{"id":1,"name":"Alice"}]' --content-type=application/json

# Mock with custom headers
playwright-cli route "**/api/data" --body='{"ok":true}' --header="X-Custom: value"

# Remove headers from requests
playwright-cli route "**/*" --remove-header=cookie,authorization

# List active routes
playwright-cli route-list

# Remove a route or all routes
playwright-cli unroute "**/*.jpg"
playwright-cli unroute
```

Patterns are standard Playwright URL glob patterns (e.g. `**/api/users`, `**/*.{png,jpg}`).

## Advanced Mocking with run-code

For conditional responses, request body inspection, response modification, aborts, or delays, use `run-code` with the standard `page.route()` API:

```bash
playwright-cli run-code "async page => {
  await page.route('**/api/offline', route => route.abort('internetdisconnected'));
}"
```
