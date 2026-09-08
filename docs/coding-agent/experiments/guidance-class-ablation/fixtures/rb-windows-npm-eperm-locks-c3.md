---
id: rb-windows-npm-eperm-locks-c3
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
npm error code EPERM
npm error syscall mkdir
npm error path C:\locked-cache
npm error errno -4048
npm error EPERM: operation not permitted, mkdir 'C:\locked-cache'
```

Diagnostic observations:

- npm config get cache: stdout C:\locked-cache, exit 0, stderr empty.
- icacls C:\locked-cache: the effective ACL explicitly denies this user directory creation/write access. A scoped write probe fails there; the repository path remains writable.
- package and lockfile are synchronized; no native binary unlink is present in the failure. No module holder was identified.
