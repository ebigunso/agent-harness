---
id: rb-windows-npm-eperm-locks-01
section: rb-windows-npm-eperm-locks
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; process/lock observations are constructed, not live machine evidence.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2; cwd C:/work/npm-lock. npm color is disabled. better-sqlite3 9.6.0

Command: `npm ci`

Exit code: 1

stdout:
```text
(empty)
```

stderr (error-level output):
```text
npm error code EPERM
npm error syscall unlink
npm error path C:\work\npm-lock\node_modules\better-sqlite3\build\Release\better_sqlite3.node
npm error errno -4048
npm error EPERM: operation not permitted, unlink 'C:\work\npm-lock\node_modules\better-sqlite3\build\Release\better_sqlite3.node'
npm error The operation was rejected by your operating system.
npm error It's possible that the file was already in use (by a text editor or antivirus), or that you lack permissions to access it.
```

Diagnostic observations:

- package.json and package-lock.json are synchronized; project and cache are writable. Registry requests succeed. The process can create/remove an ordinary probe file beside the affected module, and no ACL denial is observed.
- Installed layout: better-sqlite3 9.6.0; the named binary exists. Where marked source build, the addon was built for its host runtime and loaded successfully before this install.
- The dev server is still running in its original terminal.

Command: `tasklist /m better_sqlite3.node`

Exit code: 0; stderr: (empty). stdout:
```text
Image Name                     PID Modules
========================= ======== ===========================================
node.exe                      4101 better_sqlite3.node
```

Repository ownership inspection:

- PID 4101: Express/TypeScript dev server; process inspection shows loaded module `C:\work\npm-lock\node_modules\better-sqlite3\build\Release\better_sqlite3.node`. Launch command references `C:/work/npm-lock/src/server.ts`; the task is owned by this repository.
