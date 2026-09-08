---
id: rb-persistent-shell-cwd-normalization-c4
section: rb-persistent-shell-cwd-normalization
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Rust/Cargo 1.82.0; cwd and intended root both C:/work/rust-service. Tool UI workspace root is also C:/work/rust-service.

Prior command: `Set-Location -LiteralPath "C:/work/rust-service"` — status 0.

Before retry/repair: `pwd` reports C:/work/rust-service; `Get-Item -Force -LiteralPath 'Cargo.toml','api/Cargo.toml','api/src/lib.rs' | Select-Object -ExpandProperty FullName` exits 0, stderr empty, stdout:
```text
C:/work/rust-service/Cargo.toml
C:/work/rust-service/api/Cargo.toml
C:/work/rust-service/api/src/lib.rs
```

Failing command: `cargo test -p api`

Exit code: 101

stdout:
```text
running 1 test
test tests::count ... FAILED

failures:

---- tests::count stdout ----
thread 'tests::count' panicked at api/src/lib.rs:18:9:
assertion `left == right` failed
  left: 4
 right: 3
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

failures:
    tests::count

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
```

stderr:
```text
Finished `test` profile [unoptimized + debuginfo] target(s) in 0.02s
     Running unittests src/lib.rs (target\debug\deps\api-12ab34cd56ef78ab.exe)
error: test failed, to rerun pass `-p api --lib`
```

Diagnostic observations: cargo metadata succeeds, identifies api as a workspace member at this root, and source file api/src/lib.rs exists. The actual regression assertion expected 3 and computed 4. Dependencies resolve and compilation succeeds.

Final `pwd` remains C:/work/rust-service. No navigation, file or environment change occurred.
