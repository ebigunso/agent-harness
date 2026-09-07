---
id: rb-windows-npm-eperm-locks-09
section: rb-windows-npm-eperm-locks
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; process/lock observations are constructed, not live machine evidence.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2; cwd C:/work/npm-lock. npm color is disabled. node-pty 1.0.0 (source build)

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
npm error path C:\work\npm-lock\node_modules\node-pty\build\Release\pty.node
npm error errno -4048
npm error EPERM: operation not permitted, unlink 'C:\work\npm-lock\node_modules\node-pty\build\Release\pty.node'
npm error The operation was rejected by your operating system.
npm error It's possible that the file was already in use (by a text editor or antivirus), or that you lack permissions to access it.
```

Diagnostic observations:

- package.json and package-lock.json are synchronized; project and cache are writable. Registry requests succeed. The process can create/remove an ordinary probe file beside the affected module, and no ACL denial is observed.
- Installed layout: node-pty 1.0.0 (source build); the named binary exists. Where marked source build, the addon was built for its host runtime and loaded successfully before this install.
- The addon has been rebuilt for this Electron ABI; it loads successfully. The holder image is electron.exe.

Command: `tasklist /m pty.node`

Exit code: 0; stderr: (empty). stdout:
```text
Image Name                     PID Modules
========================= ======== ===========================================
electron.exe                  4109 pty.node
```

Repository ownership inspection:

- PID 4109: Electron terminal preview; process inspection shows loaded module `C:\work\npm-lock\node_modules\node-pty\build\Release\pty.node`. Launch command references `C:/work/npm-lock/preview/main.js`; the task is owned by this repository.
