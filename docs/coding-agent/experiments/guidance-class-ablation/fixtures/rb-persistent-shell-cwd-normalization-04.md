---
id: rb-persistent-shell-cwd-normalization-04
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Java 21.0.5; Maven 3.9.9. Intended execution base: C:/work/orders.

Prior command in this same persistent shell: `Set-Location -LiteralPath 'C:/work/orders/src/main/resources'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `C:/work/orders/src/main/resources`.

Command: `Get-ChildItem -Name`; exit/status 0; stderr empty. stdout:
```text
application.properties
```

Failing command: `mvn test`

Exit code / shell status: 1

stdout:
```text
[INFO] Scanning for projects...
[ERROR] The goal you specified requires a project to execute but there is no POM in this directory (C:\work\orders\src\main\resources). Please verify you invoked Maven from the correct directory. -> [Help 1]
```

stderr:
```text
(empty)
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/orders/pom.xml
C:/work/orders/src/main/resources/application.properties
```

Captured comparison:

1. `Set-Location -LiteralPath 'C:/work/orders'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/orders; exit/status 0.
3. `mvn test` — exit/status 0.

stdout:
```text
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/orders; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/orders as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs.
