---
id: rb-windows-npm-eperm-locks-c4
section: rb-windows-npm-eperm-locks
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; process/lock observations are constructed, not live machine evidence.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2; cwd C:/work/npm-lock. npm color is disabled.

Command: `npm test -- --runInBand`

Exit code: 1

stdout:
```text
> npm-lock@1.0.0 test
> jest --runInBand
```

stderr (error-level output):
```text
FAIL test/count.test.js
  ● counts visible items
    expect(received).toBe(expected) // Object.is equality

    Expected: 3
    Received: 4

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
```

Diagnostic observations:

- npm ci already exited 0 for this unchanged lockfile and installed tree.
- Jest 29.7.0 returned exit 1, and the runner process ended; no watcher is configured.
- The failure is the deterministic application assertion in test/count.test.js. No EPERM, EBUSY or native module unlink error occurred.
