---
id: rb-persistent-shell-cwd-normalization-09
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; Git Bash (Git for Windows 2.47.0); GNU Make 4.4.1; GCC 14.2. Intended execution base: C:/work/c-lib.

Prior command in this same persistent shell: `cd '/c/work/c-lib/tests'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `/c/work/c-lib/tests`.

Command: `ls -1`; exit/status 0; stderr empty. stdout:
```text
test_math.c
```

Failing command: `make -f Makefile test`

Exit code / shell status: 2

stdout:
```text
(empty)
```

stderr:
```text
make: Makefile: No such file or directory
make: *** No rule to make target 'Makefile'.  Stop.
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/c-lib/Makefile
C:/work/c-lib/tests/test_math.c
```

Captured comparison:

1. `cd '/c/work/c-lib'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/c-lib; exit/status 0.
3. `make -f Makefile test` — exit/status 0.

stdout:
```text
./build/test_math.exe
1 test passed
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/c-lib; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/c-lib as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs.
