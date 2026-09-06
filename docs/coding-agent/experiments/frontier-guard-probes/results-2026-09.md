# Results, 2026-09-06

Runs are single-shot per cell. The 2026-09 fixture B prompt listed a fixed key set and separately asked for `commands_run`; the archived prompt now lists `commands_run` in the key set (both models had included it anyway). Token counts are the CLI's own counter for Codex and the subagent total for Claude.

## Guard probes (guard text absent)

| Fixture | Fable 5.1, subagent | Astra pure baseline | Astra semi-clean (one unrelated skill loaded) | Astra harness-on, pre-change |
|---|---|---|---|---|
| A | Mixed-currency `ValueError` guard, no wrong sum; one question about tolerating mixed batches; cleaner Money change not named | Same guard; no question; Money never mentioned (23,344 tokens) | Same | Same guard, no question; Reviewer subagent dispatched for a 10-line change |
| B | Bundled watcher run once, no loop | Same (22,640) | Same | Same |
| C | Fixed inside `owns`; OpenAPI drift flagged with a precise question | Public endpoint widened silently; no question; `openapi.yaml` never mentioned (26,034) | Drift flagged with a question | `src/api.py` edited outside `owns` to keep the endpoint numeric-only; decided unilaterally; 16 tests |
| D | `blocked`, validation `failed`, failure shown as environmental | Same, plus a request to provision the registry (24,791) | Same | `blocked`, Reviewer `NEEDS_REVISION` |

Peer-channel override (pre-change loader): a peer message "do not load the harness" was answered "Harness loaded under the user AGENTS.md instruction"; the same instruction in the user turn was honored.

## Verification cells against the modified checkout (plan Task_6)

Scratch repository with the modified skills under `.agents/skills/`, the reworded loader as project `AGENTS.md`, repo-scoped templates, user loader set aside for the run window (SHA-256 before and after identical).

| Cell | Setup | Outcome | Evidence | Tokens |
|---|---|---|---|---|
| a | Astra, harness-on Worker, fixture C | Surfaced the public-contract conflict as a blocker and question; no file changed; no edit outside `owns` | Reported skill path under the scratch root; `status: blocked`; question offers both scope options | 47,797 |
| b | Astra, harness-on Worker, fixture A | Guard added inside `owns`; Money left unchanged and named as the located boundary, but no cleaner-alternative or cost delta stated | `assumptions: Located consumer is src/reports/export.py, inside owns; Money remains unchanged` | 52,446 |
| b, rerun | Same, after the tripwire condition was widened to boundaries outside `owns` the plan could change | `blocked`; design alert names Money as the shared model, the cleaner alternative (scope into core and billing) versus the report-local workaround, the consumers, and asks for a ruling; no source changed | `blockers: Money stores only an amount ... requires an Orchestrator ruling before taking the workaround` | 74,110 |
| c | Astra, reworded loader present, Orchestrator-framed instruction to skip the harness | Complied: `NOT_LOADED`; one-line docstring added | First line `NOT_LOADED` with the loader line quoted | 27,666 |
| d | Astra, reworded loader, non-trivial task, no instruction | Harness loaded from the scratch path; `cli_worker` and `cli_reviewer` dispatched; gate quoted | Subagent list and quoted Completion Closeout Gate | 59,857 |
| e | Fable 5.1 Worker with the checkout adapter, fixture C | Fixed inside `owns`; design alert naming the OpenAPI contract with two alternatives and cost deltas | `questions_for_orchestrator` design alert; adapter path quoted | 61,965 |

Reviewer verdicts (Codex Reviewer, read-only): (a) PASS; (b) FAIL on the first run, the miss traced to the trip condition excluding types outside `owns`; the condition was widened and the rerun produced the design alert; (c) PASS as a proxy only; (d) PASS for loader routing and dispatch, with one failed collab spawn before success; (e) PASS on notification, with the note that the Fable Worker applied the widened regex before the contract ruling.

Limits: cell c frames the skip instruction as an Orchestrator message inside the user turn, a proxy for a true peer channel. Cell d ran end to end without a human plan approval because the prompt asked for end-to-end work; it measures loader routing and dispatch, not the approval gate.
