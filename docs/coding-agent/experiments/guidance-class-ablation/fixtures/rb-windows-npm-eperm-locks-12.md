---
id: rb-windows-npm-eperm-locks-12
section: rb-windows-npm-eperm-locks
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; process/lock observations are constructed, not live machine evidence.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2; cwd C:/work/npm-lock. npm color is disabled. sharp 0.32.6

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
npm error path C:\work\npm-lock\node_modules\sharp\build\Release\sharp-win32-x64.node
npm error errno -4048
npm error EPERM: operation not permitted, unlink 'C:\work\npm-lock\node_modules\sharp\build\Release\sharp-win32-x64.node'
npm error The operation was rejected by your operating system.
npm error It's possible that the file was already in use (by a text editor or antivirus), or that you lack permissions to access it.
```

Diagnostic observations:

- package.json and package-lock.json are synchronized; project and cache are writable. Registry requests succeed. The process can create/remove an ordinary probe file beside the affected module, and no ACL denial is observed.
- Installed layout: sharp 0.32.6; the named binary exists. Where marked source build, the addon was built for its host runtime and loaded successfully before this install.
- A previous attempt named better_sqlite3.node and PID 4113. That worker was stopped; the new attempt below names sharp. PID 4113 is no longer running.

Command: `tasklist /m sharp-win32-x64.node`

Exit code: 0; stderr: (empty). stdout:
```text
Image Name                     PID Modules
========================= ======== ===========================================
node.exe                      4114 sharp-win32-x64.node
```

Repository ownership inspection:

- PID 4114: thumbnail watcher; process inspection shows loaded module `C:\work\npm-lock\node_modules\sharp\build\Release\sharp-win32-x64.node`. Launch command references `C:/work/npm-lock/workers/thumbnails.js`; the task is owned by this repository.
- Fresh module lookup is the tasklist output above; the old PID/module listing is retained only as history.
