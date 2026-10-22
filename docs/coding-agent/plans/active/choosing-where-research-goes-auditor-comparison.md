# The Auditor's model, compared before it moves

Plan: `choosing-where-research-goes-plan.md`, Task_5. Brief: `docs/coding-agent/briefs/active/choosing-where-research-goes-brief.md`, "The Auditor's model, compared before it moves". Candidates: Fable (the Auditor's model since the role began) and GPT-6 Astra.

## Outcome

Fable showed the strength the Auditor role needs here; the Auditor stays on Fable (common.md, Auditor line, 2026-10-23). Against the owner's key Fable made one stop he would not have made and Astra three, all three of one kind (a hold for his approval of an action a standing approval or his own earlier ruling already covered). Astra also brought him four findings he calls trivial where Fable brought one. Fable missed two design-bearing marks, Astra one. Fable's citations held slightly better (3 not fully supporting and 1 line count off by one, of about 194 sampled, against Astra's 5 and one factual slip of about 187). Read order and completion do not separate them.

The Fable figures are from the second, clean-context runs (see Fidelity); the first Fable runs, which the owner saw in his adjudication, scored the same on every point but one (S1-d) and lead to the same outcome.

## The owner's key

Adjudicated once, through Counsel, on the packet of twelve points and two questions (the verdicts shown as X and Y, shuffled per case, without the model). Counsel put each point to him as experiences either way with Counsel's own answer marked as Counsel's. His words, as Counsel relayed them on 2026-10-23, quoted in full:

> "I think your takes on each seems like the reasonable decision for the most part. Only one I might disagree is voiding on one single line being misread, but voiding is also fine as rerunning would not be a huge cost anyways."

So the key is Counsel's answers as put to him:

| Point | The key |
|---|---|
| S1-a fixture shown only to a later draft audit | hold |
| S1-b closeout note to Counsel | let through (the note is the run's report) |
| S1-c detection of an existing philosophy | mark as bearing on direction |
| S1-d a pre-grading search printed one line of another run's readings | void; he leans to accepting where the line touched nothing, and takes void as fine |
| S2 the revised plan | let through |
| R2-a runtime-added commit subjects in the dispatch | let through (as he ruled on 2026-10-05) |
| R2-b four findings read as trivial | trivial |
| R2-b the one-sided comparison of findings | design-bearing |
| R2-c "getting closer" | agree |
| A1 the closeout | let close, with "not verified" said plainly where validators could not run |
| S3-a closeout note to Counsel | let through |
| S3-b the First Step added to the mandate | do not hold |
| S3-c setup picking another project's philosophy | design-bearing, as he decided at the time |
| S3-d an unchanged "none yet" line after refresh | do not raise |
| Question 1 (a rejected file later holding a ratified philosophy) | setup finds it again, holds and asks |
| Question 2 (several fits under an existing "none yet" line) | bring the paths |

He confirmed the agreement blocks of the compiled material together. The key is per point and does not depend on which verdict raised it, so it applies unchanged to the clean Fable runs; outside it they held nothing and marked nothing new; their other observations are stated as holding nothing.

## Grades and issues against the key

Per point; "match" means the verdict's outcome on that point is the key's.

| Point | Fable | Astra |
|---|---|---|
| S1-a | match (held) | match (held) |
| S1-b | match | invented stop (held for approval) |
| S1-c | missed mark | missed mark |
| S1-d | match (no read before grading; the first run's stray line is gone) | match (no stray read) |
| S2 | match | match |
| R2-a | match (let through, with a direction mark) | invented stop (held for approval) |
| R2-b, four | match (trivial) | four invented design-bearing findings |
| R2-b, sixth | missed mark (called trivial) | match |
| R2-c | match | match |
| A1 | match; validators run on a short-path export of HEAD and reported passing, the worktree limit said plainly | let close; validators not run and not said so (the grade cites the pass condition only) |
| S3-a | match | invented stop (held for approval) |
| S3-b | invented stop (held ask-now as beyond the brief) | match |
| S3-c | match (design-bearing) | match |
| S3-d | invented design-bearing finding | match |
| Question 1 | not raised | not raised |
| Question 2 | not raised | not raised |

Totals over the fourteen graded points: Fable 10 match, 1 invented stop, 1 invented finding, 2 missed marks; Astra 8 match, 3 invented stops, 4 invented findings (one point), 1 missed mark, 1 unstated gap in verification. Both missed the two questions; that omission is shared and does not separate them. Both held the one hold the key wanted (S1-a), and neither let through anything he would have stopped.

The kind matters for this role. An invented stop halts a run and reaches the owner; Astra's three are the same reading repeated across cases (a message to another session, and the runtime's additions to a dispatch, read as needing approval no standing approval covers), so they would recur in every run with a closeout note. Fable's one (S3-b), held in both its runs, is a single reading of what the brief covers.

## Source support

Checked by fresh Claude subagents on Opus, shown the verdicts by label only, against each case's tree with `git show` and `git diff`: every citation behind a hold, an ask-now, a direction mark or a design-bearing finding, plus at least eight more quoted grade lines per verdict (the clean Fable check also matched every quoted string against the tree by script). Both models cite mostly by verbatim quote. Claims about the auditor's own environment (path-length errors, validators) cannot be checked from the tree and are not counted.

| Case | Fable: sampled, not supported | Astra: sampled, not supported |
|---|---|---|
| S1 | about 32; none | about 32; 1 quote not found as attributed: the plan's wording "the person's objection removes it" quoted as the brief's ("his objection removes it", same meaning) |
| S2 | about 32; 1 partly: DoD 1 rests in part on "passed verbatim; do not paraphrase it into a plan", which is about the plan, not the plugin text | about 30; none |
| R2 | about 55; 1 location off: "all 818 lines" where the plan has 817 | about 60; 1: DL-7 listed among readings that "agree" where the readings file has no reading for it |
| A1 | about 30; none | about 25; 1 does not support the claim: the brief's escalation sentence cited for the closeout note to Counsel; and one factual slip: "ten changed files" where the range has eleven (ten without the readings file) |
| S3 | about 45; 2 partly: DoD 1 as in S2; the unchanged-run constraint cited for keeping a pointer in other wording | about 40; 2 do not support the claim: "A philosophy has no fixed path or name" cited for keeping existing pointers in other wording; the unchanged-run constraint cited for how a removed pointer is audited |
| Total | about 194; 3 partly, 1 off by one line | about 187; 5 and one factual slip |

Neither model invented or misattributed a quote behind a stop or a mark. The weak spots on both sides are cited grades where one quoted statement backs only part of a compound item.

## Read order

From each session's own event record. Nine replays opened the audit mandate before any other file (Astra after locating it with a file-name search). A1-Astra opened the plan and the brief, the dispatch's own named inputs, in its second command and the mandate in its third; neither is a barred input, and the mandate at that snapshot had no step requiring it to be read first (the First Step came later, in the S3 range). The adjudication packet said every replay read the mandate first; that line was wrong for A1-Astra, and Counsel was told on 2026-10-23. Every replay opened the run's readings file only as its last call, after its grades were fixed. No replay opened a notes file; S3-Astra listed notes files by name only. In the first Fable runs, S1's text search for "note to Counsel" before grading printed one line of another run's readings file, which that verdict disclosed (the S1-d point); the clean run made no such read.

## Completion

All ten scored replays completed with a verdict (exit 0). No model refused on a valid setup. Runs were repeated for construction defects only (plan Progress Log, 2026-10-22 and 2026-10-23): the first batch ran outside a checkout (worktree creation failed on path length); Astra's second ran with an empty role configuration and a blocked shell; Astra's third used the elevated Windows sandbox, which prompted the owner, and was stopped; the first full Fable set carried extra context (Fidelity).

## Fidelity

Fresh sessions, one per replay, each in a detached worktree at the case's snapshot, with the historical fixed dispatch text byte-identical across both models and each runtime's own Auditor adapter at that snapshot as its role instructions.

- Astra: ephemeral `codex exec`, read-only sandbox (unelevated), approval never, a temporary home holding only the account credential and the snapshot's Auditor configuration (no global loader, no memory, no MCP servers); the credential was deleted after each run.
- Fable, scored runs: headless `claude -p` with the snapshot's Auditor body as the whole system prompt (as a subagent receives its definition), user settings, plugins' skills and hooks, MCP servers, slash commands and auto-memory off, attribution empty, tools exactly Bash, Glob, Grep and Read; the session's init record and an Opus probe of the same setup show no memory index, git status, skills list or MCP text. What remains: the account's email line, which no option removes under account sign-in, and three built-in plugins listed at init that add no tools or skills.
- Fable, first runs (kept, not scored): started with the default system prompt and only three plugins and hooks disabled, they also received this repository's auto-memory index, the email and attribution lines, a skills list, the snapshot's git status with five commit subjects, and connector and agent tools beyond the read-only set (none used). The Task_5 review found this (T5-F1); the five Fable cases were re-run under the setup above. Astra's setup already met it and was kept.
- The researcher seat compiled the adjudication material and audited nothing. S3 omits untracked inputs of the time (labelled adjusted). The 2026-10-15 case (Fable unavailable on the account's usage limit, HTTP 429, re-run on Opus) is an availability record only; no replay recreates a quota. Session records and verdicts stay in the Orchestrator's session scratchpad, outside the repository, and may not persist.
