# Answer key — Rust fixtures

Grading rule: hit = planted mechanism at planted location; partial = area without mechanism.
Findings on clean fixtures are false positives unless they expose a real authoring error.

## Planted

| id | bullet | planted defect | a hit must state |
|---|---|---|---|
| rs-01 | R10/R5 | `.unwrap()` twice on operator-supplied manifest data | fallible boundary now panics in production; restore `Result` propagation |
| rs-02 | R13 | `offset as u32` on byte offsets that reach 8 GiB | silent truncation past 4 GiB corrupts offsets; needs `try_from` or wider slot |
| rs-03 | R14/R2 | exhaustive `match` rewritten as `if let` chain with fall-through | compiler exhaustiveness lost; the next variant added will silently fall through instead of failing the build |
| rs-04 | R12 | `String` for wallet ids, amount, currency in a money path | primitive obsession; crate already has `WalletId`/`Money`/`TxId`; string amount parse loses currency safety |
| rs-05 | R15 | `.clone()` sprayed to satisfy borrowck (`doc`, `body`, `term`, `id`) | clones bypass ownership design; iterate by reference / restructure instead |
| rs-06 | R16 | account-closure rules (balance, pending, grace period) inline in HTTP handler | domain lifecycle logic in transport layer; belongs in `domain::accounts` with the other transitions |
| rs-07 | R6 | structured `CertError` enum deleted for `Result<_, String>` | callers matched `CertError::Io` for retry; stringly errors destroy caller-actionable categories |
| rs-08 | R10/R9 | `.expect()` on operator YAML in scheduler main loop | untrusted config input panics the scheduler; parse fallibly with a default or error |

## Clean decoys

rs-c1 (exhaustive match extended), rs-c2 (error translation kept in Result), rs-c3 (typed
ids/money), rs-c4 (checked `try_from` with documented startup invariant).

Known acceptable nitpicks on decoys: rs-c4 panic-on-invariant debate (the note states the
invariant is validated at startup; accept, do not count).
