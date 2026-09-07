---
id: rb-windows-npm-eperm-locks-08
section: rb-windows-npm-eperm-locks
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; process/lock observations are constructed, not live machine evidence.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2; cwd C:/work/npm-lock. npm color is disabled. onnxruntime-node 1.19.2

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
npm error path C:\work\npm-lock\node_modules\onnxruntime-node\bin\napi-v3\win32\x64\onnxruntime_binding.node
npm error errno -4082
npm error EBUSY: resource busy or locked, unlink 'C:\work\npm-lock\node_modules\onnxruntime-node\bin\napi-v3\win32\x64\onnxruntime_binding.node'
```

Diagnostic observations:

- package.json and package-lock.json are synchronized; project and cache are writable. Registry requests succeed. The process can create/remove an ordinary probe file beside the affected module, and no ACL denial is observed.
- Installed layout: onnxruntime-node 1.19.2; the named binary exists. Where marked source build, the addon was built for its host runtime and loaded successfully before this install.
- The Node inference preview process is serving this repository.

Command: `tasklist /m onnxruntime_binding.node`

Exit code: 0; stderr: (empty). stdout:
```text
Image Name                     PID Modules
========================= ======== ===========================================
node.exe                      4108 onnxruntime_binding.node
```

Repository ownership inspection:

- PID 4108: model preview server; process inspection shows loaded module `C:\work\npm-lock\node_modules\onnxruntime-node\bin\napi-v3\win32\x64\onnxruntime_binding.node`. Launch command references `C:/work/npm-lock/workers/model-preview.js`; the task is owned by this repository.
