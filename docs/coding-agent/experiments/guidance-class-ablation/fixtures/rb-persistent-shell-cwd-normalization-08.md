---
id: rb-persistent-shell-cwd-normalization-08
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CMake 3.30.5; Ninja 1.12.1. Intended execution base: C:/work/native.

Prior command in this same persistent shell: `Set-Location -LiteralPath 'C:/work/native/build'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `C:/work/native/build`.

Command: `Get-ChildItem -Name`; exit/status 0; stderr empty. stdout:
```text
CMakeCache.txt
build.ninja
```

Failing command: `cmake --build build`

Exit code / shell status: 1

stdout:
```text
(empty)
```

stderr:
```text
Error: C:/work/native/build/build is not a directory
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/native/CMakeLists.txt
C:/work/native/build/CMakeCache.txt
C:/work/native/build/build.ninja
```

Captured comparison:

1. `Set-Location -LiteralPath 'C:/work/native'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/native; exit/status 0.
3. `cmake --build build` — exit/status 0.

stdout:
```text
[1/1] Linking CXX executable native.exe
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/native; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/native as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs.
