---
id: rb-windows-npm-eperm-locks-05
section: rb-windows-npm-eperm-locks
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; process/lock observations are constructed, not live machine evidence.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2; cwd C:/work/npm-lock. npm color is disabled. bcrypt 5.1.1

Command: `npm install`

Exit code: 1

stdout:
```text
(empty)
```

stderr (error-level output):
```text
npm error code EBUSY
npm error syscall unlink
npm error path C:\work\npm-lock\node_modules\bcrypt\lib\binding\napi-v3\bcrypt_lib.node
npm error errno -4082
npm error EBUSY: resource busy or locked, unlink 'C:\work\npm-lock\node_modules\bcrypt\lib\binding\napi-v3\bcrypt_lib.node'
```

Diagnostic observations:

- package.json and package-lock.json are synchronized; project and cache are writable. Registry requests succeed. The process can create/remove an ordinary probe file beside the affected module, and no ACL denial is observed.
- Installed layout: bcrypt 5.1.1; the named binary exists. Where marked source build, the addon was built for its host runtime and loaded successfully before this install.
- The test process is in watch mode after the last test completed.

Command: `tasklist /m bcrypt_lib.node`

Exit code: 0; stderr: (empty). stdout:
```text
Image Name                     PID Modules
========================= ======== ===========================================
node.exe                      4105 bcrypt_lib.node
```

Repository ownership inspection:

- PID 4105: Nest/Jest integration-test worker; process inspection shows loaded module `C:\work\npm-lock\node_modules\bcrypt\lib\binding\napi-v3\bcrypt_lib.node`. Launch command references `C:/work/npm-lock/node_modules/jest/bin/jest.js --watch`; the task is owned by this repository.
