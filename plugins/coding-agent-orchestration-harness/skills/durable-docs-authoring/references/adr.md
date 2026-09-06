# ADR discipline: admission, form, lifecycle, acceptance

Rules for decision records (ADRs) in any repository the harness operates in. Format resolution: follow the repository's decision-record convention when its rules point to one; otherwise use the harness defaults `references/adr-template.md` and `references/adr-repo-readme.md`.

## Admission test

A decision record exists to carry a decision and its constraints forward, so that someone building later knows what is decided, why, and what they must not do. Write one only when all five hold:

1. **Load-bearing.** The decision constrains future design or implementation shape. Name the concrete thing someone would otherwise build.
2. **Severe if ignored.** Going against it is costly to detect or undo: a broken contract, silent drift, expensive rework. A miss a reviewer would catch on the next diff belongs in a rule, not a record.
3. **Not derivable from the artifact.** A reader with the code or docs alone, and no other context, could not reconstruct the reasoning in a few minutes.
4. **The why can be stated for a first-time reader.** In a sentence or two, at intent altitude. A why that needs a table, a commit hash, or an evidence section is describing an investigation, not a decision; that is the sign the record is at the wrong altitude.
5. **Only active content.** Nothing stale, superseded, or wrong stays in a live record.

Two negatives reject a proposal outright: the content is re-derivable from git history or from a plan; or the only constraint it carries is "do not re-add these files". Removal ledgers, evidence tables, and investigation summaries are never records; they live with the experiment and the closing plan.

The test is run on every proposed record, by the author, before drafting. A directive inside an older record ("each X is recorded as an ADR"), the shape of an existing record, or a plan task that says "write ADR-X" does not admit a record by itself; run the test anyway and say so when it fails.

Two further boundaries: records shape the repository's product domain, so decisions about how development is conducted belong in repo rules or harness skills (for a repository whose product is a development process, process governance is its product domain); and a record must not ratify an exception that exists only because it already lives in the code path. Propose remediation first; record a deliberate, bounded exception only when it passes the test on its own.

## Form

- **One decision per record.** Test: could this record be retired on its own without touching another decision? A bundle is split before it is written.
- **The why is prose.** Present tense, a sentence or two, the fork and the reason one branch won. Evidence lives with the experiment; when a premise is a measured fact that will expire, Revisit When names the models and the date of the check, nothing more.
- **Intent altitude.** The record does not mirror implementation wording, code or normative prose; the constraint is stated so that any rewording of the implementation that preserves it stays valid. Exact strings, formats, and thresholds are "not covered" and live in skill text or configuration.
- **No time-relative wording.** Name models, people, dates, and pull requests. "Current", "older", "the fleet", "now" expire silently.
- **Rejected alternatives carry their reopen condition** or state that they are rejected outright; an alternative rejected for a reason that no longer holds is a stale record.

## Three homes
- Record: the admitted decision, its constraint, the why, the rejected alternatives with reopen conditions, and Revisit When. Durable operational material that fails the admission test belongs in a rule or a skill, however long it lasts.
- Rule: executable enforcement read on every task; likely-but-cheap violation classes belong here.
- Decision Log: the plan-scoped chronicle, including every record proposal and its acceptance or decline.

Record-plus-rule pairs are the expected shape for enforced contracts; the homes are complements, never substitutes.

## Lifecycle

- **Proposed.** A record on a branch carries `status: proposed` until a human accepts it on its own (see Acceptance). While proposed it is a draft: rewritten, renumbered, split, or dropped freely; the plan's Decision Log carries the drafting history; a dropped draft frees its number.
- **Accepted.** The status flips to `accepted` on the explicit yes, before merge. Immutability attaches at merge to `main`, because that is when readers may have built on it. After merge a record changes only when a retirement elsewhere requires repairing a pointer in it, or to correct a typo that changes no meaning. Any change to the decision, its boundary, its reasons, or its reopen conditions is a new complete record, and the old one is retired. Refinement and reversal both replace; there is no partial supersession.
- **Superseded.** Retirement is one atomic operation: set `status: superseded`, add a header line under the title ("Retired on DATE. Replaced by ADR-X." or "Retired on DATE; nothing in it still binds."), move the file to `superseded/` with the `--superseded-by-ADR-X` or `--retired` suffix, repair every inbound reference in the repository, and prove it with an absence search for the old filename. A retired record is frozen.
- IDs are never reused; a gap in an active directory means a retirement.

## Acceptance

A record binds future work, so a human accepts it on its own, never by implication.

1. When the admission test passes, state the proposal in conversation and in the plan Decision Log in the same action: title, the decision in one line, the constraint it places on future work, the why.
2. Draft on the writing-strength side per `subagent-strategy/references/model-routing.md`.
3. Present the draft to the human by itself and ask for acceptance. Plan approval does not accept a record; merging a pull request does not accept a record. A no is terminal for that draft: record the decline in the Decision Log and do not re-propose.
4. Land the record only after the explicit yes, and list every proposed record with its acceptance state in the final response and the pull request body under its own heading.

Plan time is the best moment to propose, because the decision can still change before implementation, but it cannot be guaranteed: a decision point that surfaces mid-implementation follows the record-and-surface path and still gets its own acceptance ask before it lands, and a decision found wrong after landing follows retirement and replacement.
