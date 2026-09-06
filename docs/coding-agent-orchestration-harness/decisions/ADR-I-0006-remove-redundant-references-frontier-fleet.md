---
status: accepted
adr_type: implementation
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely re-add tool-help mirrors, worked examples, and restated gate text on the intuition that agents need them, and would treat the retained guards as equally removable because the probes look like a general obsolescence result"
  detected_signals: "rejected alternative likely to be re-proposed; premises likely to expire (the fleet's behavior profile); deliberately bounded scope (redundancy class only, latent-risk family excluded)"
  cost_of_wrong_preservation: "if a weaker model joins the fleet, the deleted examples and mirrors are the cheapest content to have kept; this record names what was removed and how to check"
  cost_of_over_extension: "reading the probe table as evidence that guards which were not probed, or the latent-risk family, or core-principles 2-10, can be deleted; those need their own ablation under ADR-D-0015"
supersedes: []
superseded_by: null
supersession_scope: null
implements: ["ADR-D-0015-remove-obsolete-guidance-as-models-improve.md"]
---

# ADR-I-0006: Remove redundant references for the frontier fleet, with guard probes

## Context and Problem Statement

A 2026-09-06 audit of every harness skill and reference against Claude Fable 5.1 and GPT-6 Astra classified content into knowledge the models apply unprompted, behavior guards traced to incidents, and redundancy: tool-help mirrors, worked examples that restate a template, duplicated gate text, and artifacts with no consumer. ADR-D-0015 requires ablation evidence to remove guidance. Redundancy is not guidance in that sense, but the same audit proposed relaxing several guards, and those needed evidence before anything was cut.

## Decision

Delete the redundancy class listed under Implementation Impact, keep every guard the probes showed is not native, and record the probe protocol and results under `docs/coding-agent/experiments/frontier-guard-probes/` so the check can be rerun when the fleet changes.

## Considered Options

1. Keep everything and rely on progressive-disclosure routing.
2. Delete the full audit list, including guidance-class content, on the strength of the audit's judgment.
3. Delete only the redundancy class now; probe the guards; route guidance-class removals to a separate ablation.

## Decision Outcome

Chosen option: **Delete the redundancy class, probe the guards**. Option 1 pays routing cost for content whose only value is availability of the same information elsewhere. Option 2 was the audit's first pass and was wrong in at least two places the probes exposed: GPT-6 Astra with nothing loaded widened a documented public API contract without a question, and neither model named the cleaner boundary change when a workaround was available. Option 3 removes what needs no evidence and keeps what the evidence says still earns its place.

### Rejected Alternatives

Deleting `review-latent-risk-failure.md` and trimming the latent-risk family was proposed and withdrawn at plan review: ADR-I-0004 explicitly excludes that family from its evidence, and a missing-Postgres probe does not test failure-review content. It reopens only with a planted-defect ablation on that subject matter. Deleting the Researcher-before-reading gate, the replan pause, and the tripwire hard stop outright was rejected in favor of rewording under ADR-D-0017.

## Implementation Impact

Deleted, each classified as duplicate (D), tool-help mirror (M), or consumer-less (C), with the verification used:

| File | Class | Verification |
|---|---|---|
| `plan-format/references/examples.md` | D | template already shows the shape; four near-identical examples |
| `plan-format/references/task-waves.md` | D | restates `plan-format/SKILL.md` core rule 4 |
| `subagent-strategy/references/research-splits.md` | D | splits any orchestrator invents; SKILL.md rule 3 (parallelize analysis) covers parallel research |
| `playwright-cli/references/{request-mocking,running-code,session-management,storage-state,test-generation}.md` and the SKILL.md command catalogue | M | `playwright-cli --help`; kept the `run-code` page-argument signature, the IndexedDB note, and the auth-state warning |
| `playwright-e2e-evidence/references/{viewport-presets,flow-patterns,failure-triage}.md` | D | spec and evidence templates already carry the fields; triage steps are plain knowledge |
| `improvement-loop/references/post-correction-micro-checklist.md` | D | the always-on rules in that SKILL.md already mandate lesson capture and durable-default reporting |
| `engineering-quality-baselines/references/review-rubric.md` scorecard and outcome bands | C | grep found no consumer of the scores; symmetric checks and gate-fail precedence kept |
| `review-latent-risk.md` twelve-item list | D | consolidated into the trigger table with every trigger preserved, confirmed at review |
| `testing-validation.md` lines 126-133 and 137-158 | D | ambiguity-as-escalation shown unnecessary by probe D on both models; decision flow restated lines 25-28 |
| `wave-integration/references/reviewer-packet-template.md` latent-risk stanzas | D | twelve identical stanzas naming one skill; one line suffices |
| `subagent-strategy/references/dispatch-checklists.md` bullet caps and tooling-preference lines; `prompt-snippets.md` tooling lines | D | prompt-shaping the fleet does not need; every non-default obligation retained |
| Package validator micro-checklist block and four-filename packet loop | C | consumers of the deleted content; packet existence and router checks kept |

Guards probed and kept: workaround tripwire and design alert (both models avoid the crude workaround but do not name the cleaner alternative unprompted; with the harness on, GPT-6 Astra still did not name it until the trip condition was widened to cover a shared type outside `owns` that the plan could change, after which it produced the alert), inline-poll ban (incident 2026-09-05, one line), smallest-diff escape hatch, boundary-crossing surface routing (Astra pure baseline widened a public contract silently), status contract (one canonical copy). Plugin version 0.16.0.

## Consequences

- Positive: ~4,000 tokens leave the loaded surface per matching task; the review packet drops ~700 tokens per review; five help-mirror files leave the maintenance surface.
- Negative / tradeoffs: a weaker model joining the fleet loses the examples first; the probe protocol is single-run per cell.

## Decision Boundary

Invariant: none of the deleted files returns without a stated consumer or a demonstrated salience gap; the latent-risk family, `core-principles.md` principles 2-10, `architecture-gates.md`, and the troubleshooting runbooks are outside this decision and need their own ADR-D-0015 ablation.

Not covered: wording of the retained guards, which ADR-D-0017 governs; the probe fixtures' content, which may be extended.

## Measurement Basis

`docs/coding-agent/experiments/frontier-guard-probes/` at commits `a8fc57a78d6c` ("Frontier guard probe records") and `4ace1fdf5eab` ("Harden probe runner exit semantics", branch `feature/2026-09-06/frontier-model-guidance-refresh`): four fixtures, prompts, the pure-baseline runner, the discovery probe record, and `results-2026-09.md` with sixteen guard-probe cells (four fixtures across Fable subagent, Astra pure baseline, Astra semi-clean, Astra harness-on) plus five verification cells against the modified checkout. Limits: single run per cell; probe B lacked the recorded incident's trigger condition; the harness-on control was one session.

## Validation

Package validation, smoke tests, and fixture validators pass after the deletions; directory-scoped pointer greps return nothing for every deleted file; the Task_6 verification cells in the implementing plan record the retained guards firing on the modified checkout.

## Revisit When

Per ADR-D-0015: a daily-use model is replaced or a weaker tier is added, or real tasks show misses on the removed subject matter (a Worker that needs a worked plan example, a Reviewer that misses a latent-risk trigger the consolidated table should have routed, a probe-class behavior recurring in review). Rerun `run_baseline.sh` and the verification cells before reintroducing any deleted file, and before removing any retained guard.

## More Information

Implements ADR-D-0015. Companion design record: ADR-D-0017. Implementing plan: `docs/coding-agent/plans/completed/frontier-model-guidance-refresh-plan.md` after closeout.
