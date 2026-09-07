---
id: rb-persistent-shell-cwd-normalization-11
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Ruby 3.3.6; Bundler 2.5.23. Intended execution base: C:/work/ruby-app.

Prior command in this same persistent shell: `Set-Location -LiteralPath 'C:/work/unrelated'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `C:/work/unrelated`.

Command: `Get-ChildItem -Name`; exit/status 0; stderr empty. stdout:
```text
notes.txt
```

Failing command: `bundle exec rake spec`

Exit code / shell status: 10

stdout:
```text
(empty)
```

stderr:
```text
Could not locate Gemfile or .bundle/ directory
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/ruby-app/Gemfile
C:/work/ruby-app/Gemfile.lock
C:/work/ruby-app/Rakefile
C:/work/ruby-app/spec/app_spec.rb
```

Captured comparison:

1. `Set-Location -LiteralPath 'C:/work/ruby-app'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/ruby-app; exit/status 0.
3. `bundle exec rake spec` — exit/status 0.

stdout:
```text
.

Finished in 0.01 seconds (files took 0.1 seconds to load)
1 example, 0 failures
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/ruby-app; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/ruby-app as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs. BUNDLE_GEMFILE is unset, no Gemfile/.bundle exists in cwd or its ancestors, and installed gems satisfy the application lockfile.
