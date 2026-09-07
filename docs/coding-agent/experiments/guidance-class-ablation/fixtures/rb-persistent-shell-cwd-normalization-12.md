---
id: rb-persistent-shell-cwd-normalization-12
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; PHP 8.3.14. Intended execution base: C:/work/php-app.

Prior command in this same persistent shell: `Set-Location -LiteralPath 'C:/work/php-app/docs'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `C:/work/php-app/docs`.

Command: `Get-ChildItem -Name`; exit/status 0; stderr empty. stdout:
```text
README.md
```

Failing command: `php bin/console cache:clear`

Exit code / shell status: 1

stdout:
```text
(empty)
```

stderr:
```text
Could not open input file: bin/console
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/php-app/bin/console
C:/work/php-app/composer.json
```

Captured comparison:

1. `Set-Location -LiteralPath 'C:/work/php-app'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/php-app; exit/status 0.
3. `php bin/console cache:clear` — exit/status 0.

stdout:
```text
[OK] Cache for the "dev" environment (debug=true) was successfully cleared.
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/php-app; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/php-app as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs. PHP 8.3.14 emits this missing-input message on stderr.
