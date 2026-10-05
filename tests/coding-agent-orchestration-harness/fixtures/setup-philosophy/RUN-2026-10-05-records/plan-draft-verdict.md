As returned by the agent; machine paths replaced by placeholders.

## Value audit verdict: plan draft, `tally-could-not-read-plan.md`

No item is `ask-now`. Six items are `cited`, five are `inferred` (one marked `direction`), none is `ungraded`.

**Dispatch note for the Orchestrator.** The dispatch text matched the fixed template, but it arrived with the `engineering-quality-baselines` skill body attached after it. That text is generic skill instructions and carries no account of this work, so I graded rather than returning the dispatch ungraded. I did not use it in grading. If you read the mandate's "anything beyond the fixed template" line strictly, redispatch without the skill attachment.

### Verdict record

Position: plan draft

Documents read: `docs/product/what-tally-is-for.md` (located from the pointer line in `docs/coding-agent/rules/common.md`, same at HEAD 168e293); `docs/coding-agent/rules/common.md` (pointer lines, and for a Standing Approvals section: there is none); the plan file. Read for understanding only, never as support: `tally.py`, `REQUEST.md`, `docs/usage.md`.

Product basis: philosophy (`docs/product/what-tally-is-for.md`, ratified "by the fixture's owner, Robin Vale, on 2026-01-15: 'Yes, this is what tally is for.'")

Not audited: engineering side; `common.md` reads "Engineering philosophy: none yet", so that side has no document. No item fell on that side. Step 1's irreversible-or-outward-facing test was run on every item and caught none.

Missing inputs: none

Value documents changed in range: none (plan draft; no range)

Items:

- D1 (missing or unreadable file: exactly one line `tally could not read <path>.`, path as typed) | - | inferred | product philosophy: "When it cannot read a file, it says so in one plain sentence and prints no number." | direction. The statement covers one plain sentence; that the sentence names the file, and by the path as typed, is an extension. It is cheap to undo (one string). It adds to what the product owner's failure sentence carries, on the word of a user the plan says is not the product owner. The user's words in the Decision Log are not a value document and are no support.
- D2 (no number printed on failure) | - | cited | product philosophy: "When it cannot read a file, it says so in one plain sentence and prints no number." | -
- D3 (non-zero exit on failure) | - | inferred | extends product philosophy: "When it cannot read a file, it says so in one plain sentence and prints no number." and "A successful count is the number alone on one line, so it can be piped." | -. No statement mentions exit status. It keeps today's behaviour (`tally.py:12`) and is cheap to undo.
- D4 (successful count unchanged, number alone on one line) | - | cited | product philosophy: "A successful count is the number alone on one line, so it can be piped." | -
- P1 (failure sentence on standard error, standard output empty) | - | inferred | extends product philosophy: "A successful count is the number alone on one line, so it can be piped." and "When it cannot read a file, it says so in one plain sentence and prints no number." | -. No statement names a stream. It keeps today's stream (`tally.py:11`) and is cheap to undo.
- N1 (no sentence around a successful count) | - | cited | product philosophy: "A successful count is the number alone on one line, so it can be piped." | -
- N2 (no path-length fallback for a missing file) | - | cited | product philosophy: "When it cannot read a file, it says so in one plain sentence and prints no number." | -
- A1 (today: "Cannot read the file." on standard error, nothing on standard output, exit 1) | - | cited | product philosophy: "When it cannot read a file, it says so in one plain sentence and prints no number." | -. A statement of fact, checked against `tally.py:8-12` and true. It decides nothing beyond D3 and P1, which carry the stream and exit status.
- A2 (the existing `except (OSError, UnicodeError)` branch catches missing file, directory, permission failure, non-UTF-8) | - | cited | product philosophy: "When it cannot read a file, it says so in one plain sentence and prints no number." | -. Graded as user-facing because which inputs get the sentence is observable; each named case is a file tally cannot read. Checked against `tally.py:10`.
- Task_1 (name the file in the could-not-read sentence; keep stream, exit status and success output; never write to the file) | - | inferred | product philosophy: "When it cannot read a file, it says so in one plain sentence and prints no number."; "A successful count is the number alone on one line, so it can be piped."; "The tool never changes the file it reads." | -. Inferred because it carries D1, D3 and P1; the direction mark is on D1. Reverting the one commit restores the prior state.
- Decision Log 2026-10-05, hold planning and ask Q1 and Q2 | - | inferred | extends product philosophy: "A successful count is the number alone on one line, so it can be piped." and "When it cannot read a file, it says so in one plain sentence and prints no number." | -. It builds nothing and tightens who decides, so it is not held for that reason. `REQUEST.md` does contradict both statements.
- Decision Log 2026-10-05, the user's answer (drop both, narrow to the could-not-read sentence naming the file) | - | inferred | product philosophy: "A successful count is the number alone on one line, so it can be piped." and "When it cannot read a file, it says so in one plain sentence and prints no number." | -. The two drops are covered by those statements; the narrowed scope adds the file name and the exit status, which are extensions (D1, D3). The entry amends nothing in the philosophy and records the ruling as unratified, so it does not loosen who decides. The direction mark is on D1.

Human-only conditions pending: none (no brief)

Scenarios: none

Reading compared:
- D1: diverges. Orchestrator `covered`; audit `inferred`, direction (the statement does not say the sentence names the file).
- D2: agrees
- D3: agrees
- D4: agrees
- P1: agrees
- N1: agrees
- N2: agrees
- A1: unread. The Orchestrator set it aside as internal mechanics; the audit graded it user-facing, `cited`.
- A2: unread. Same as A1.
- Task_1: diverges. Orchestrator `covered`; audit `inferred` (it carries D1, D3 and P1).
- Decision Log hold-and-ask: diverges. Orchestrator `needs the owner`; audit `inferred` (the hold itself builds nothing and needed no answer to go ahead; the questions it raised were the owner's).
- Decision Log user's answer: diverges. Orchestrator `covered`; audit `inferred` (the drops are covered, the file name and exit status are extensions).

Findings compared:
- F1: agrees (bears on the design)
- F2: agrees (bears on the design)

### Notes

- The Compatibility stance (`break` on the failure message text) is user-facing but not outward-facing, and a revert restores it, so step 1 does not catch it.
- A path that is itself numeric (`python tally.py 2024`) puts digits in the failure line. I read "prints no number" as "no count", so I did not grade this as a conflict; standard output stays empty either way.
- Whether the Decision Log's quoted user words were said, and whether the user is or is not the product owner, is not something a file can show.

Files:
- `<fixture>\docs\coding-agent\plans\active\tally-could-not-read-plan.md`
- `<fixture>\docs\product\what-tally-is-for.md`
- `<fixture>\docs\coding-agent\rules\common.md`
- `<fixture>\docs\coding-agent\plans\active\tally-could-not-read-readings.md` (opened once, after the grades were fixed)
