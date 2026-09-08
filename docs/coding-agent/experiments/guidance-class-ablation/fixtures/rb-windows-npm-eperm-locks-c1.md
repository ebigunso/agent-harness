---
id: rb-windows-npm-eperm-locks-c1
section: rb-windows-npm-eperm-locks
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; process/lock observations are constructed, not live machine evidence.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2; cwd C:/work/npm-lock. npm color is disabled.

Command: `npm ci`

Exit code: 1

stdout:
```text
(empty)
```

stderr (error-level output):
```text
npm error code EUSAGE
npm error
npm error `npm ci` can only install packages when your package.json and package-lock.json or npm-shrinkwrap.json are in sync. Please update your lock file with `npm install` before continuing.
npm error
npm error Invalid: lock file's is-number@6.0.0 does not satisfy is-number@7.0.0
```

Diagnostic observations:

- The developer intentionally changed package.json to is-number 7.0.0; package-lock.json still records 6.0.0.
- Project/cache paths are writable; registry is reachable. No native addon unlink occurred.
- tasklist /m better_sqlite3.node: exit 0, stdout "INFO: No tasks are running which match the specified criteria.", stderr empty.
- The lockfile update is pending; dependency resolution has not completed.
