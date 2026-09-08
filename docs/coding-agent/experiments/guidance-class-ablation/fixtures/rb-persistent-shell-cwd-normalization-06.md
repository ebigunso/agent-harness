---
id: rb-persistent-shell-cwd-normalization-06
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; Git Bash (Git for Windows 2.47.0); Java 21.0.5; Gradle wrapper 8.10.2. Intended execution base: C:/work/jvm-app.

Prior command in this same persistent shell: `cd '/c/work/jvm-app/service'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `/c/work/jvm-app/service`.

Command: `ls -1`; exit/status 0; stderr empty. stdout:
```text
build.gradle.kts
src
```

Failing command: `./gradlew test`

Exit code / shell status: 127

stdout:
```text
(empty)
```

stderr:
```text
bash: ./gradlew: No such file or directory
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/jvm-app/gradlew
C:/work/jvm-app/settings.gradle.kts
C:/work/jvm-app/service/build.gradle.kts
```

Captured comparison:

1. `cd '/c/work/jvm-app'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/jvm-app; exit/status 0.
3. `./gradlew test` — exit/status 0.

stdout:
```text
> Task :service:test

BUILD SUCCESSFUL in 1s
3 actionable tasks: 1 executed, 2 up-to-date
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/jvm-app; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/jvm-app as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs. gradlew has its executable bit and Unix line endings; its wrapper JAR and dependencies are available.
