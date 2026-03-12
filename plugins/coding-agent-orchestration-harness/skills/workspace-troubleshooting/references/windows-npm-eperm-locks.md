# Windows npm EPERM/EBUSY native module lock (npm ci / npm install)

## Symptoms
- npm ci / npm install fails with EPERM or EBUSY
- error mentions unlinking/removing a file under node_modules
- error often references a native module binary like <module>.node

## Likely cause
A running process (node/dev server/test runner/editor extension) is holding a lock on a native module binary inside node_modules.

## Safe, ordered steps

1) Stop obvious lock holders
- stop dev servers, test runners, watchers
- close terminals running node processes for this repo
- stop editor-integrated test runners

2) Identify locking process by module (best-effort)
If the error shows a specific <module>.node:

Preferred (PowerShell 7):
- "C:\Program Files\PowerShell\7\pwsh.exe" -Command "tasklist /m <module>.node"

Fallback:
- powershell.exe -Command "tasklist /m <module>.node"

3) Kill the locking PID(s) (last resort)
- taskkill /PID <pid> /F

4) Retry install
- npm ci

If it still fails:
- repeat using the new module filename in the error
- confirm no other node processes:
  - tasklist | findstr node

## Evidence to capture
- original npm command + full error output
- module filename
- tasklist output
- killed PIDs
- retry result
