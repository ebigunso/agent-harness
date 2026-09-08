# cp-7 grading key

Author-only; exclude from review input. A full hit names the mechanism/location and repair direction. Secondary overlap is permitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| cp-7-01 | “Can critical behavior be validated without fragile setup?” | Python expiry logic reads real time and global timezone; tests sleep until midnight to hit the branch. | Name hidden time dependence and replace sleeps with explicit deterministic time seam. |
| cp-7-02 | “Structure logic so important decisions are easy to test.” | Go retry policy calls time.Sleep directly inside decision logic; tests must wait minutes to exercise budget exhaustion despite fake sleeper already used by sibling worker. | Identify hardwired sleep seam and use deterministic time/sleeper to exercise actual attempt/budget boundaries. |
| cp-7-03 | “Prefer deterministic seams over hidden global state.” | Java invoice calculator reads global exchange-rate singleton updated by unrelated tests; result depends on suite order. | Name shared mutable rate state; supply a controlled rate snapshot for decisions and independent tests. |
| cp-7-04 | “Match validation depth to risk and change surface.” | TypeScript authorization change validates only a happy-path screenshot, with no evidence for denied roles despite adding role branching. | Identify missing denied-role evidence and require targeted authorization branch checks, not more screenshots. |
| cp-7-05 | “Can critical behavior be validated without fragile setup?” | Python fee formula uses random promotional selection internally; tests assert approximate totals over repeated runs, masking exact boundary mistakes. | Expose deterministic selection/random seam and test exact decision cases without probabilistic retries. |
| cp-7-06 | “Is evidence proportional to risk?” | Rust serializer change affects persisted data but validation report runs formatter only; no old-data read or new-data round-trip check. | Name missing persisted-format evidence and require focused compatibility/round-trip validation. |
| cp-7-07 | “Structure logic so important decisions are easy to test.” | C# controller embeds a pure tax decision inside a method that must open a live paid vendor session before reaching the branch. | Separate decision from external adapter setup so tax boundaries can be tested deterministically. |
| cp-7-08 | “Prefer deterministic seams over hidden global state.” | Ruby tests patch a process-global ENV rate limit in setup and never restore it; parallel examples observe different policy limits. | Identify leaking environment dependence and inject local configuration or scope/restore seam safely. |
| cp-7-09 | “Can critical behavior be validated without fragile setup?” | Kotlin cancellation behavior is tested by hoping a real network request remains active after Thread.sleep(10), so test often misses cancellation branch. | Require controlled in-flight transport/latch or deterministic seam exercising cancellation, not arbitrary sleep. |
| cp-7-10 | “Match validation depth to risk and change surface.” | PHP password-reset refactor changes token expiry and replay behavior but evidence only shows successful valid-token case. | Require targeted expired-token and replay rejection evidence proportional to reset risk. |
| cp-7-11 | “Prefer deterministic seams over hidden global state.” | C++ scheduling decision reads hardware clock directly and test waits until system clock crosses threshold, failing when CI is paused. | Pass a fixed clock/time source and assert threshold behavior deterministically. |
| cp-7-12 | “Can critical behavior be validated without fragile setup?” | Scala event reducer is tested only by booting a full cluster and searching logs; isolated transition logic has no seam for explicit input-state/output-state checks. | Make reducer transitions callable with controlled state/events and verify critical outcomes directly. |

## Clean decoys

No blocking target defect. Nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Intended correct behavior | Known acceptable optional nitpick |
|---|---|---|
| cp-7-c1 | Python expiry takes now and tests before/at/after boundary deterministically. | General clock framework. |
| cp-7-c2 | Go payment retry test deterministically simulates transient failure and dedupe. | Broad new load suite. |
| cp-7-c3 | Rust pure decisions are tested locally with one adapter integration check. | Mocking every helper. |
| cp-7-c4 | TypeScript label-only edit has targeted render evidence and no new logic. | Full E2E suite for a label. |
