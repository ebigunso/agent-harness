---
id: rb-persistent-shell-cwd-normalization-c1
section: rb-persistent-shell-cwd-normalization
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Node 20.18.0; npm 10.8.2; TypeScript 5.6.3; cwd and intended root both C:/work/shop/web. Tool UI workspace root is also C:/work/shop/web.

Prior command: `Set-Location -LiteralPath "C:/work/shop/web"` — status 0.

Before retry/repair: `pwd` reports C:/work/shop/web; `Get-Item -Force -LiteralPath 'package.json','package-lock.json','tsconfig.json','src/index.ts' | Select-Object -ExpandProperty FullName` exits 0, stderr empty, stdout:
```text
C:/work/shop/web/package.json
C:/work/shop/web/package-lock.json
C:/work/shop/web/tsconfig.json
C:/work/shop/web/src/index.ts
```

Failing command: `npm run build`

Exit code: 1

stdout:
```text
> web@1.0.0 build
> tsc

src/index.ts(3,7): error TS2322: Type 'string' is not assignable to type 'number'.
```

stderr:
```text
(empty)
```

Diagnostic observations: This is the package root declared in the build instructions. The tsc command found its config and source. Source line 3 assigns a string to a number-typed variable. TypeScript writes this compiler diagnostic to stdout; no directory is missing.

Final `pwd` remains C:/work/shop/web. No navigation, file or environment change occurred.
