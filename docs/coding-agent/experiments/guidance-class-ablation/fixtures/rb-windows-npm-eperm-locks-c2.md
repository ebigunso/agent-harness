---
id: rb-windows-npm-eperm-locks-c2
section: rb-windows-npm-eperm-locks
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; process/lock observations are constructed, not live machine evidence.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2; cwd C:/work/npm-lock. npm color is disabled.

Command: `npm install`

Exit code: 1

stdout:
```text
(empty)
```

stderr (error-level output):
```text
npm error code E401
npm error Unable to authenticate, your authentication token seems to be invalid.
npm error To correct this please try logging in again with:
npm error   npm login
```

Diagnostic observations:

- Captured registry response: HTTP/1.1 401 Unauthorized; WWW-Authenticate: Bearer. Request went to the configured private registry scope; no credential values are included.
- .npmrc scope/registry URL is correct. package.json and lockfile agree; cwd and cache are writable.
- No native addon unlink was attempted; tasklist /m sharp-win32-x64.node reports no matching tasks.
