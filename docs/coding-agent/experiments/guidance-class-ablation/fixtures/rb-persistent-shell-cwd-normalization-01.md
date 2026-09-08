---
id: rb-persistent-shell-cwd-normalization-01
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2. Intended execution base: C:/work/shop.

Prior command in this same persistent shell: `Set-Location -LiteralPath 'C:/work/shop/web'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `C:/work/shop/web`.

Command: `Get-ChildItem -Name`; exit/status 0; stderr empty. stdout:
```text
package.json
src
node_modules
```

Failing command: `cd web && npm run build`

Exit code / shell status: 1

stdout:
```text
(empty)
```

stderr:
```text
Set-Location: Cannot find path 'C:\work\shop\web\web' because it does not exist.
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/shop/web/package.json
C:/work/shop/web/src/index.ts
```

Captured comparison:

1. `Set-Location -LiteralPath 'C:/work/shop'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/shop; exit/status 0.
3. `cd web && npm run build` — exit/status 0.

stdout:
```text
> web@1.0.0 build
> tsc
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/shop/web; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/shop as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs. Command status 1 is the shell adapter status for failed Set-Location; npm never launched on that attempt. The earlier command had already entered web.
