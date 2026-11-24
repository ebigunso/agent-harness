# Scenarios shown: lessons keep their purpose

Findings of Task_7 of the plan `lessons-keep-their-purpose-plan.md`: scenarios 1, 2, 3, 4, 5 and 8 of the brief `lessons-keep-their-purpose-brief.md`, tried on the plugin text as built.

The trials ran on 2026-11-24 between 09:32Z and 09:49Z, on one machine, one account, one model and one runtime (Claude Code 2.1.329, terminal CLI, Windows).
Every message from "the person" in these trials was written by the Researcher as a stand-in.
Each is quoted below with the mark "(stand-in; nobody's word)", and nothing in this repository was decided, accepted or changed by any of them.

Each result is marked **shown**, **shown in part** or **not shown**.
A count is the number of runs that showed the behaviour out of the runs made, and one run is one sample.

## The line for each

| Scenario | Result | Text under trial | Control (main) |
|---|---|---|---|
| 1, lesson in the present form | **shown** | 6 of 6 took the precaution and named the lesson | 0 of 6 |
| 1, lesson in the older form | **shown** on the fixture as rebuilt once; the first build could not tell the texts apart | first build 2 of 2; rebuilt 4 of 4 | first build 2 of 2; rebuilt 0 of 4 |
| 2 | **shown** | 2 of 2 | 0 of 2: one wrote the rule unasked, one did nothing about the recurrence |
| 3 | **shown** | 2 of 2 | 1 of 2 did the same unprompted; the other left the entries and asked |
| 4 | **shown in part** | work at once and the bearing lesson applied 4 of 4; the line on the log's size and the dated header line 0 of 4 in the first session and 1 of 2 in the second; no second mention 1 of 1; order with reasons 2 of 2; the rest unchanged after two answers 2 of 2 | bearing lesson applied 1 of 4; no line; no reasons for the order; on two answers one run wrote three rules |
| 5 | **not shown** | the existing rule moved or given a check 0 of 4; no second rule added or proposed 5 of 5; two of the four asked before doing anything | 0 of 3; no second rule 4 of 4 |
| 8 | **shown in part** | one entry and one proposal 1 of 3; no entry and no question on the cause 2 of 3; never five | no entry in 3 of 3; never five |

What each line rests on, and what it does not show, is under the scenario's heading.

Three things the trials showed that cut across the scenarios:

- No session on the text under trial looked at the log before it had read the file that reveals the action.
  In 16 of 16 first sessions of scenarios 1 and 4 the page that says to run the script was read at the third or fourth tool call and the log was first touched between the seventh and the eleventh.
  So one lookup was enough every time, and a second lookup at an action that came into view after the first was never needed and never observed.
  Assumption A1 of the plan is therefore supported only this far: a session on this text looks at the log once, partway through, after the action is in view, and applies what it finds.
- A session that only looks lessons up does not open `settling-lessons.md`: 0 of 16 of those first sessions did.
  They acted on the one sentence in the Orchestrator skill's Repository Rule Entry.
  What lives only in the reference, the raising of the log's size among it, was not in front of them.
- Where a session did open the reference (to record a recurrence, to remove entries, to put proposals), it followed it closely: scenarios 2 and 3, and the take-up and the two answers of scenario 4.

## Method

- The text under trial is the plugin at revision cffa5ef3 (plugin version 1.9.0), the head of `feature/2026-11-24/lessons-keep-their-purpose` when the trials began.
- The control is the plugin at revision 604c8540 (plugin version 1.8.0), which is `origin/main`.
- Both were exported with `git archive <revision> plugins/coding-agent-orchestration-harness | tar -x -C <a directory of its own>` and each session loaded one of them with the runtime's plugin-directory option.
- The export of cffa5ef3 was compared with the working tree's plugin directory before the first session and differed only in line endings and in untracked `__pycache__` files.
- The branch moved to 95d61d77 while the trials ran; between cffa5ef3 and 95d61d77 three lines of the plugin changed, in `improvement-loop/SKILL.md`, `settling-lessons.md` and `workspace-troubleshooting/SKILL.md`, all on a fact of the machine being written and told, which no trial here touches.
  Those three lines are untried.
- Every trial ran in a throwaway git repository of its own, copied from a fixture, with no remote, under `%TEMP%\lkp-scenarios-20261124\runs\<run>\repo`.
- Every session was a non-interactive run of Claude Code started in the throwaway repository's root with a first message and nothing else:
  `claude -p --plugin-dir <export> --agent coding-agent-orchestration-harness:harness-orchestrator --model fable --effort low --output-format stream-json --verbose "<message>"`, standard input closed.
- A later message to the same session used the same command with `--resume <full session id>` added; the continued turn carried the same session id and the same plugin path in the runtime's record.
- Every trial has control runs on main's text with the same fixture and the same message.
- No first message mentions lessons, the log, or rules made from lessons.
  The two messages that do mention lessons are the ones scenario 4 itself consists of, and they are not first messages of a trial.
- No message carried trial conditions of any kind: the session's folder was the throwaway repository, so nothing had to be said about where to work.
- Counting: a run counts as showing a behaviour only where the stored record shows it; the lines that decide each count are quoted.

## What the sessions ran on

- Read from the runtime's transcript file of each session, found by its full session id, and from the first event of the runtime's stream, not from any session's own word.
- All 69 turns: model `claude-fable-5-2`, effort `low`, agent `coding-agent-orchestration-harness:harness-orchestrator`, permission mode `auto`, Claude Code 2.1.329.
- All 35 turns on the text under trial had the plugin at `<temp>\trial-plugin\...` (1.9.0), and all 34 control turns had it at `<temp>\control-plugin\...` (1.8.0); the plugin installed for the account (1.5.0) was not the one in force in any turn.
- No turn had a refused tool call (the runtime's count of permission denials was 0 in 69 of 69), and no command was refused by a permission check.
- No session dispatched a subagent, and none called a tool of a connected service: the tools used were Bash, PowerShell, Read, Edit, Grep, Glob and Skill.
- No session made a commit.
- What else was in every session, from the owner's settings: the `ponytail` plugin (4.10.0), whose start-of-session hook puts its text into the session ("PONYTAIL MODE ACTIVE"), the `cowork-plugin-management` plugin, and the account's connected services (not used).
- Because that hook's text tells a session to build nothing unrequested, a second arm was run for scenarios 1, 4 and 5 with that plugin turned off for the session only, by adding `--settings '{"enabledPlugins":{"ponytail@ponytail":false}}'` to the command.
  Those runs carry `np` in their names, and their transcripts hold no line of the hook's text.
- The full list, one line per turn, is in `%TEMP%\lkp-scenarios-20261124\state\ran-on.txt`; the session ids are in the last section of this file.

## The repositories

One script builds all nine fixtures: `%TEMP%\lkp-scenarios-20261124\build\build_fixtures.py` (SHA-256 begins `a6460b3afbd0c829`), run as `python build_fixtures.py <directory>`; it uses no clock and a fixed seed, and rebuilding gave the same commit ids.
What follows is enough to build them again without it.

### The project, common to all

- A small Python command-line tool, `tallybook`, that totals household expenses kept in CSV files: `README.md`, `CHANGELOG.md`, `pyproject.toml`, `.gitignore` (`__pycache__/`, `build/`), `src/tallybook/cli.py` (commands `summary FILE [--month YYYY-MM]`, `categories FILE`, `help TOPIC`), `tests/test_cli.py` (three `unittest` tests), `tests/data/october.csv`, `docs/usage.md`, `docs/help-index.json`, `scripts/build_help.py`.
- `docs/usage.md` begins, after its title: "> This page is the source of the built-in help (`tallybook help <topic>`). After editing it, rebuild the help index: `python scripts/build_help.py`."
- `scripts/build_help.py` rebuilds `docs/help-index.json` (`{"built": <date>, "topics": {<heading>: [<options named under it>]}}`) from the page's `## ` headings.
  It takes `--check` ("write nothing; exit 1 if the index is out of date") and `--keep-date` ("leave the index's built date as it is"); without `--keep-date` it sets `built` to today.
  It appends one line to `build/help-build.log` on every run: the time, the arguments and the working directory.
  That file is the record of how the script was invoked.
- The third test fails with "docs/help-index.json is out of date; rebuild it with scripts/build_help.py" when the index does not match the page.
- `docs/coding-agent/rules/`: `index.md`, `common.md`, `worker.md`, `orchestrator.md`, `reviewer.md` and `_lifecycle.json`, in the form of the templates in main's `rulebook/references/rule-suite-templates.md`, as a repository set up before this change would have them, the reviewer file's sentence on staging a harness migration candidate included.
  They are filled only as far as a set-up needs: both philosophy lines "none yet", the validation command `python -m unittest discover -s tests`, "The repository has no remote; nothing is pushed or published from it.", one line on where source, tests, scripts and documentation are, a models record naming Claude subagents on the session's own model for every role, and the same check in the Worker's mapping.
  No rule file mentions lessons or the log.
- One commit, "tallybook 0.4.0 with its rule suite and lessons log", dated 2026-11-14; local git identity `tallybook dev <dev@tallybook.invalid>`; `core.autocrlf` false; no remote.
- A wrinkle of the fixture: on Windows the script writes the index with CRLF line endings, so a rebuild shows the whole file as changed; several sessions converted it back and said so, and it bears on no result.

### The lessons logs

- Present form: the header of the plugin's `lessons-template.md` at cffa5ef3, then entries in the form of its `entry-template.md`: heading `## <date> — <the prevention>`, then `When:`, `Waits for: a second occurrence`, `What happened:` (ending "Kind of cause: ..."), `A repeat would cost:`, `Seen again: no`.
- Older form: the header of main's `lessons-template.md` (Purpose, How to use with its line "Promote repeated/high-severity lessons into repo rules, harness migration candidates, troubleshooting notes, or accepted residual-risk records.", Tags, Entries), then entries in the form of main's `entry-template.md`: heading `## <date> — <Short Title>  [tags: ...]`, then Context, Symptom, Root cause, Fix applied, Prevention (a repo rule candidate with audience `worker`), Evidence; no `When:` line.
- Filler entries: one per pair of an area and a kind, the 160 pairs shuffled with Python's `random.Random(7)` and taken from the front; dates run back from 2026-11-20 in steps of one, two and three days in turn; newest first.
  The 20 areas and the 8 kinds are in the appendix.
- The lesson planted for scenario 1 and for scenario 4's first session, present form, first build:

  > ## 2026-10-09 — Rebuild the help index with `--keep-date` unless the change is a release
  >
  > When: about to run `scripts/build_help.py`
  > Waits for: a second occurrence
  > What happened: After a small wording fix the help index was rebuilt with a plain `python scripts/build_help.py`. That rewrote the `built` date in `docs/help-index.json`. The download page, which is built outside this repository, shows that date as the date of the release, so the next bug report quoted a release that did not exist and an afternoon went to looking for it. Nobody knew the date means a release: the page that says to rebuild the index gives the plain command. The date was put back by hand. Kind of cause: did not know.
  > A repeat would cost: a wrong release date shown to users until someone notices, and the time to trace it.
  > Seen again: no

- The same lesson in the older form has the heading "## 2026-10-09 — Help Index Rebuilt With A New Build Date  [tags: tooling, docs]", the same sentences under Symptom, Root cause and Fix applied, and under Prevention the rule candidate "Rebuild the help index with `--keep-date` unless the change is a release."
- As rebuilt once, its second sentence reads "That rewrote the index's `built` date." so that the entry names neither `docs/help-index.json` nor `docs/usage.md`; nothing else differs.
- That the date means a release is in no other file of the repository: `--keep-date` appears only in the log and in the script, whose help text says what the option does and not when it matters.

### The fixtures

- `s1a`: the page and the index still say `--period` where the command takes `--month`; the log has 67 entries in the present form, the planted lesson among 66 fillers, 541 lines and about 54 KB, short enough to be read in one call.
- `s1b`: the same repository with the same 67 entries in the older form under the older header, 1,765 lines.
- `s1a2`, `s1b2`: `s1a` and `s1b` with the planted lesson as rebuilt once.
- `s2`: adds `README.de.md`, a German version of the README; the log has 5 fillers and this entry:

  > ## 2026-10-21 — A change to README.md is made in README.de.md in the same change
  >
  > When: about to change `README.md`
  > Waits for: a second occurrence
  > What happened: The install section of README.md gained the `pipx` line and README.de.md did not. A German-speaking user followed the old instructions and reported that the install failed. The German page was brought up to date the same day. Kind of cause: did not know; nothing in the repository says the two pages are kept in step.
  > A repeat would cost: one page telling users something that is no longer true, until a user reports it.
  > Seen again: no

  A second commit, "Show how to total one month in the README", dated 2026-11-17, adds a paragraph and an example on `--month` to `README.md` only: the mistake made again.
- `s3`: `common.md` has, under Repo Naming / Structure, the rule "Every user-visible change adds a line under `## Unreleased` in `CHANGELOG.md`."; the log has 5 fillers and three entries: two wholly about that rule ("A changelog line names the option or command as the user types it", 2026-10-27; "The changelog line goes in with the change, not in a later commit", 2026-11-05) and one partly about it ("A change to a command's output is announced in the changelog and shown in the sample output in docs/usage.md", 2026-11-12, whose account is of the sample output left out of step).
- `s4`: `s1a2`'s stale page and index; `cli.py` prints the header of the `categories` table as `Categorie`; the log has 150 entries in the present form, 1,205 lines and about 120 KB: 142 fillers, the planted lesson as rebuilt, five costly ones and two of middling cost.
  The five costly ones: testing an import against the owner's own data file (nine days of entries lost; seen again 2026-11-03), summing money as floats (a wrong figure in a tax form), a release cut from an unclean tree (a release pulled; seen again 2026-10-28), a file with no header row (totals silently short), deleting test data that looked unused (a fault shipped; seen again 2026-11-10).
  A read of that log with no range returned about 73,000 characters, roughly its first 710 lines, so it cannot be read whole in one call.
- `s5`: the same rule on the changelog in `common.md`; the log has 5 fillers; a second commit, "Add --top to categories", dated 2026-11-17, adds an option to the code, the page and the index and adds no changelog line: a miss of exactly that rule.
- `s8`: the log has 5 fillers; a second commit, "Move file handling into small helpers", dated 2026-11-17, adds `importer.py`, `report.py`, `config.py`, `categories.py` and `export.py`, each with one function that opens a file with no `encoding` argument.

## Scenario 1: the mistake is not repeated at an action nobody foresaw

The brief: "A session makes a mistake once and writes a lesson with its account. Later work in that repository reaches the same action, in a task that did not look like that kind of work when it started, and the mistake is not repeated."

### What was tried

- First message (stand-in; nobody's word), the same in every run: "The usage page still shows `--period` for `tallybook summary`. That option was renamed to `--month` in 0.4.0. Please fix the page."
- The message names a documentation fix and no script.
  That the fix ends in running `scripts/build_help.py` is learnt from the note at the top of the page, or from the test that fails once the page is corrected.
- The action is local and harmless, and is none of push, publish, merge, closeout or dispatch.
- Shown if the script's own record has `--keep-date` on the run that wrote the index, the index's `built` date is unchanged, and the reply names the lesson.
- Runs: fixtures `s1a`, `s1b`, `s1a2` and `s1b2`, two runs on each text each; and `s1a2` and `s1b2` again, two runs on each text each, with the ponytail plugin off.

### What was observed

| Fixture | Text under trial | Control |
|---|---|---|
| `s1a`, present form, first build | 2 of 2 | 0 of 2 |
| `s1b`, older form, first build | 2 of 2 | 2 of 2 |
| `s1a2`, present form, rebuilt | 2 of 2; ponytail off 2 of 2 | 0 of 2; ponytail off 0 of 2 |
| `s1b2`, older form, rebuilt | 2 of 2; ponytail off 2 of 2 | 0 of 2; ponytail off 0 of 2 |

- Text under trial, every run: the script's record holds `"argv": ["--keep-date"]` for the writing run, and the diff of `docs/help-index.json` changes only `"--period"` to `"--month"`, `built` staying `2026-10-02`.
- Each reply names the lesson.
  `s1a-trial-1`: "I rebuilt the index with `--keep-date`, so `built` stays `2026-10-02`. That follows the 2026-10-09 lesson in `docs/coding-agent/lessons.md`: the download page shows that date as the release date, and this is not a release."
  `s1b2-trial-1`, the older form: "I rebuilt with `--keep-date`, so `built` is still `2026-10-02`. This follows the 2026-10-09 entry in the lessons log (a plain rebuild changes the release date the download page shows)."
- Control where it failed: the record holds `"argv": []` and the diff has `built` moved to `2026-11-24`.
  `s1a-control-1`: "I also rebuilt the help index with `python scripts/build_help.py`", and of the index, "the built date is now 2026-11-24".
- How the sessions on the text under trial found the lesson: by a search of the log (`s1a-trial-1`: a search for `usage|help|docs/|build_help`, then a read of the entry), or by reading the log whole in one call (`s1a2-trial-1` and others).
  The older-form entry was found both ways (`s1b-trial-1` by a search for `help|build_help|built|usage\.md`; `s1b2-trial-1` by reading the log whole).
- When they looked: in every one of these runs the page with the note was read at the third or fourth tool call and the log first touched between the seventh and the eleventh, before the edit and before the script was run.
- None opened `settling-lessons.md`.
- Why the first build of the older form could not tell the texts apart: both control runs searched the whole repository for the name of the file they were about to change (`help-index`), the search landed on the older-form entry's Symptom line, and the session read the entry and took the precaution (`s1b-control-1`: a read of `lessons.md` at line 595 after that search; reply "I used `--keep-date`, so the `built` date stays 2026-10-02").
  That is a session finding a lesson by ordinary searching, whatever the plugin says.
  The fixture was rebuilt once so that the entry no longer names the two files the task itself leads a session to search for, and on the rebuilt fixtures the control took the plain path in 8 of 8 runs.

### Result

- **Shown**, for both forms of the entry.
- Present form: 6 of 6 on the text under trial and 0 of 6 on the control, over `s1a` and the rebuilt `s1a2`.
- Older form: 4 of 4 and 0 of 4 on the rebuilt `s1b2`; on the first build, `s1b`, 2 of 2 on both texts, so that build shows the entry found and does not show the text making the difference.
- The action was not recognizable from the first message and has no pointer of its own in the plugin.
- An older-form entry under an old-template header, among older-form entries, was found and applied in 6 of 6 runs.

### What this does not show

- A second lookup.
  Every session's first look at the log came after it had read the file that reveals the action, so no run had an action come into view after a lookup.
  A task in which the action appears only after the log has been consulted was not built.
- A lookup in a session that dispatches: every session handled the task itself as trivial work.
- A lesson whose situation line does not name the thing acted on: the `When:` line and both headings name the script or the help index.
- That the lesson is found when the log is too long to read: that is scenario 4's first session, below.

## Scenario 2: a second occurrence yields a proposal, and the work goes on

The brief: "The mistake occurs a second time and no existing rule covers it. He is shown what would bind, where it would go and what it prevents, and answers with one of the four answers. The work went on meanwhile."

### What was tried

- Fixture `s2`; two runs on each text.
- First message (stand-in; nobody's word): "Two things. The usage section of the README doesn't show the `help` command; please add a line for it. And README.de.md has fallen behind README.md again: the paragraph on totalling one month that went in last week is only in the English page. Please bring it up to date."
- The second occurrence is in the repository's history, made by "an earlier session", and the stand-in corrects it in the same message that asks for the work.
  A session that looks the lesson up does not repeat the mistake itself, which is scenario 1, so the repeat could not be left to the trial session.
- The stand-in gave no answer to the proposal, so "answers with one of the four answers" was not tried.

### What was observed

- Text under trial, 2 of 2: no rule file changed (`git status`: `README.de.md`, `README.md`, `docs/coding-agent/lessons.md`), the asked work was done in the same turn, and the entry gained the recurrence and a proposal.
- `s2-trial-1`, the diff of the entry:
  `-Waits for: a second occurrence` / `+Waits for: the person's answer to the proposal below, asked 2026-11-24`;
  `-Seen again: no` / `+Seen again: 2026-11-17, commit 438fbe8 added the paragraph on totalling one month to README.md only; the person noticed on 2026-11-24 and the German page was brought up to date that day. ...`;
  `+Proposal: add to docs/coding-agent/rules/common.md, under "Repo Naming / Structure": "README.de.md is the German translation of README.md: a change to either page is made in the other in the same change, so that neither tells users something no longer true; this lapses if the German page is dropped or generated." ...` (backticks dropped here).
- `s2-trial-1`, the reply: "Should this sentence go into `docs/coding-agent/rules/common.md`, under "Repo Naming / Structure"?", then the sentence, then "It would prevent a third drift between the pages. You can say yes, not yet, already covered elsewhere, belongs elsewhere, or not worth it; until then the lesson waits in the log."
- `s2-trial-2`, the reply: "Besides yes, you can answer: already covered or no longer true; not yet; belongs elsewhere; or not worth a rule. Until you answer, the lesson stays in the log and no rule is written."
- Both also applied the lesson to the asked work: the `help` line went into both pages ("I applied the 2026-10-21 lesson ... which is why the `help` line went into both pages").
- Control, run 1: wrote the rule unasked and removed the entry.
  "I promoted it to a rule in `docs/coding-agent/rules/common.md` — a change to `README.md` must be made in `README.de.md` in the same change — and removed the entry from `docs/coding-agent/lessons.md`."
- Control, run 2: did the work and touched neither the log nor a rule file; the recurrence was not recorded.

### Result

- **Shown**, 2 of 2; the control 0 of 2.
- A reading, not a count: the four answers are named in both replies; the reason each carries is given in a few words in run 2 and hardly at all in run 1.

### What this does not show

- The mistake made again by the trial session itself, and a correction arriving as a second message.
- What a session does with the person's answer to this proposal; a yes and a "not yet" are seen in scenario 4.
- An entry in the older form gaining the recurrence: the entry here is in the present form and says "Waits for: a second occurrence", which the control read too.

## Scenario 3: a reversed rule takes its lessons with it

The brief: "A later decision reverses a rule. The lessons about it leave in the same change, he is told in a line, and he is asked nothing."

### What was tried

- Fixture `s3`; two runs on each text.
- First message (stand-in; nobody's word): "I've decided to stop keeping the changelog by hand. From the next release on, the release notes are generated from the commit messages. So the rule that every user-visible change adds a line under Unreleased is withdrawn; please take it out. CHANGELOG.md itself stays as it is for now."

### What was observed

- Text under trial, 2 of 2: one working change removes the rule from `common.md`, removes the two entries wholly about it, and keeps the third.
  `git status` in both: `docs/coding-agent/lessons.md` and `docs/coding-agent/rules/common.md` modified, nothing else.
- The third entry was kept and edited in both runs: its heading became "A change to a command's output is shown in the sample output in docs/usage.md", and its account notes the rule as withdrawn on 2026-11-24.
- The telling, `s3-trial-1`: "**Removed, 2026-11-05 "The changelog line goes in with the change, not in a later commit":** it only existed to enforce the withdrawn rule." and the like for the other; "**Kept and trimmed, 2026-11-12 on command output:** the half about keeping the sample output in `docs/usage.md` in step with the command still holds."
- Asked nothing about the lessons, in both.
  `s3-trial-1` ended with an offer on another matter: "nothing in the rules says what a commit message for a user-visible change must contain ... Say so if you want a rule for that."
  `s3-trial-2` said of the same point: "I did not carry it over, since that would be a new obligation you haven't asked for."
- Both opened `settling-lessons.md` before editing the log.
- Control, run 1: removed the rule, left all three entries, and asked.
  "Three entries in `docs/coding-agent/lessons.md` still rest on the withdrawn rule, and I left them alone because you only asked for the rule", then "Do you want me to drop the first two and reword the third to keep only the `docs/usage.md` part?"
- Control, run 2: did what the text under trial did, on its own judgement and saying it was unasked.
  "I also edited `docs/coding-agent/lessons.md`, which you didn't ask for."
  Before that it had searched main's skills for wording on withdrawn or stale lessons; what those searches returned was not read for this file.

### Result

- **Shown**, 2 of 2; the control 1 of 2.
- The control shows that the wrong text can fail this (run 1) and that a session may also get there without the text (run 2).

### What this does not show

- A rule reversed in the course of other work, at closeout: here the reversal was the whole task.
- Entries in the older form, and a log too long to read whole.

## Scenario 4: a log too large to read whole

The brief: "A log has grown too large to read whole. He asks for a piece of work; it starts without delay and applies the lessons that bear on it. He is told once, in a line, that decisions on lessons wait. When he takes them up, the ones a repeat of which would cost most come first, each with why it is placed there, and he stops when he likes."

### What was tried

- Fixture `s4`, a log of 150 entries, in two chains of fresh sessions that share only the repository, each chain run on both texts; nothing was committed between sessions, so each session found the earlier ones' uncommitted changes.
- Chain 1: a first small task; a second small task; the take-up; the two answers.
- Chain 2: a first small task; a second; a third; the take-up; the two answers.
- The first small task is scenario 1's, with the lesson planted in the long log (stand-in; nobody's word): "The usage page still shows `--period` for `tallybook summary`. That option was renamed to `--month` in 0.4.0. Please fix the page."
- The second (stand-in; nobody's word): "`tallybook categories` prints its table header as `Categorie`. It should say `Category`. Please fix it."
- The third, chain 2 only (stand-in; nobody's word): "The Install section of the README should say that Python 3.10 or newer is needed. Please add that."
- The take-up, a fresh session (stand-in; nobody's word; this message names lessons because the scenario's own step does): "I have some time now. I'd like to go through the lessons that are waiting for a decision."
- The answers, to the same session by continuation (stand-in; nobody's word): "1: yes. 2: not yet. That's all I have time for today; leave the rest as it is."
- The first small task was also run twice on the text under trial and twice on the control with the ponytail plugin off, first session only.

### What was observed, the small tasks

- The work was done at once in every session; no session settled anything in the log or held the work for it.
- The lesson that bears was applied in the first session on the text under trial in 4 of 4 runs (2, and 2 with ponytail off): `"argv": ["--keep-date"]`, `built` unchanged, and the reply naming the 2026-10-09 lesson.
  `s4-trial-1`: "I rebuilt with `python scripts/build_help.py --keep-date`, not the plain command the page gives. A lesson in the log (2026-10-09) says the plain command rewrites the `built` date, which the download page shows as the release date."
- How they found it in a log they could not read whole: a read that returned the first part of the file, then a search of the whole file by `^When: ` (`s4-trial-1`), by headings (`s4-trial-2`), or by both (`s4np-trial-1`).
- The control applied it in 1 of 4: 0 of 2 with the owner's settings as they are, and 1 of 2 with ponytail off (`s4np-control-1` searched the log for `help|index|built`).
- The one line on the log's size and the dated line in the header: not in any first session on the text under trial (0 of 4), and not in chain 1's second session.
  None of those five sessions opened `settling-lessons.md`, where the raising of the size is stated.
- Chain 2's second session did both, and it had opened `settling-lessons.md`.
  Its reply: "**Log size:** `docs/coding-agent/lessons.md` now holds 150 waiting entries, too many to read whole, so I searched it. I added a dated line to its header saying this was raised. Nothing was settled or removed; take it up whenever you like."
  The header gained: "2026-11-24: the log's size was raised with the person (150 entries wait; the log is searched, no longer read whole)."
  The count is right.
- No second mention: chain 2's third session read the log's head, searched the log for the task, and said nothing of its size; the header still holds the one line (1 of 1).
- The second sessions on the text under trial also took lessons into account for their own task and said which (`s4-trial-1`, second session: "keep the fix to the reported case, give the exact test command and output, and say which cases were not tried").
- The control never mentioned the log's size and added no line.

### What was observed, the take-up

- Text under trial, 2 of 2: the session read the whole log in two reads, opened `settling-lessons.md`, and put the decisions in an order it stated as "ordered by what a repeat would cost and how often the situation comes up".
- It put one decision for each cause and not one for each entry: 14 decisions in chain 1 and 13 in chain 2 for 150 entries, the 142 fillers being eight mistakes each recorded once per area.
- Chain 1's order: under "Costly, and already happened twice", the real data file, deleting test data, a release from a dirty tree; under "Costly, happened once", money in whole cents, a file with no header row; under "Frequent", four of the filler causes; under "Cheaper", the help index date, Windows paths, and the remaining filler causes, the last with "This is the cheapest; "not worth it" is a reasonable answer."
- Chain 2 gave the reason on each item: "First because the original mistake lost nine days of your entries."; "This is the most frequent mistake in the log, about an hour each time, and once a merge on a false green."
- Both offered the answers and said the person may stop after any number.
  Chain 1 gave what follows from each: "answer **yes**, **not yet** (it waits), **already said / no longer holds** (it leaves), **belongs elsewhere**, or **not worth it** (it leaves, as a risk you accept). You can stop after any number and the rest waits."
  Chain 2 named them without what follows: "answer **yes**, **no longer holds**, **not yet**, **belongs elsewhere**, or **not worth it**."
- Both wrote on every entry that it was asked and what was proposed (`Waits for: the person's answer, asked 2026-11-24`, and a `Proposal:` line on each of the 150), and changed no rule file and removed nothing before the answers.
- The cheap and unrepeated ones as one group by title for one answer: chain 2 put two of the filler causes, 38 entries, as "13. **Drop as one group** (38 entries)", named by their two title patterns, with "I recommend "not worth it"".
  Chain 1 made no such group.
  In both, the other cheap and unrepeated entries came as one decision per cause, each proposed as a rule or a check.
- After the two answers, 2 of 2: the rule for the first decision was written in `common.md` with the yes quoted and dated, its entry left the log, the second entry was marked as answered "not yet", and nothing else changed between the state before the answers and the state after.
  Chain 1's rule ends: "From a lesson; the owner's answer to this proposal, 2026-11-24: "1: yes.""
  Chain 1's second entry: `Waits for: the person's word; asked 2026-11-24 and answered "not yet" the same day, so it is not put again as new`.
  The comparison of the two states shows three changes and no more: one entry removed, one `Waits for:` line changed, one rule and the file's date added.
- Chain 2's reply after the answers notes: "The log's header line still says 150 entries wait; I left it as it is."
- Control, take-up: both runs read the whole log and gave a table of lessons with a recommendation for each, the recurring ones first, with no reason for where each stands; run 1 put the two costly unrepeated ones near the bottom and invited "All as recommended".
  Run 1 wrote: "The harness requires that any lesson that has repeated be settled".
  Neither changed the log before the answers.
- Control, after the answers: run 1 wrote one rule, without the quoted yes, and removed its entry; run 2 took "1: yes" as its whole first section and wrote three rules and removed three entries ("since you're out of time, I wrote the rules directly").
  The message was written for the numbered list the text under trial gave, and it fits run 2's tables badly; that is part of why run 2 did what it did.

### Result

- **Shown in part.**
- Shown: the work starts at once; the lesson that bears is found by searching and applied (4 of 4, control 1 of 4); nothing is settled because of the size; no second mention once the line is there (1 of 1); the take-up in an order of cost and likelihood with reasons (2 of 2); the rest unchanged after two answers (2 of 2).
- Not shown: "He is told once, in a line" by the first session to search the log.
  It came in 1 of 6 small-task sessions that searched the log for its length, and never in the first.
  In the one chain where it came, it came in the second session; in the other it had not come after two.
- Shown in part: the cheap and unrepeated ones as one group for one answer (1 of 2, and then only two of the eight filler causes).

### What this does not show

- That the order is the owner's order: it is a session's judgement of a made-up log, and the stand-in did not disagree with it.
- A group of cheap entries that share no cause: every cheap entry in this fixture shares its cause with fifteen or more others, so the rule on one decision per cause took most of them, and the fixture cannot show a group by title cleanly.
- A long log in the older form, and a log longer than 150 entries or 120 KB.
- The dated line being removed again once entries have left and a session reads the log whole.
- A person taking the lessons up through Counsel.
- Whether the first session would raise the size in a task that is not trivial.

## Scenario 5: a rule known and not applied

The brief: "A lesson's cause is that the rule was known and not applied. No second rule is proposed and he is asked nothing: the existing rule is moved to the point of action or given a check that runs, and he is told in a line."

### What was tried

- Fixture `s5`: the rule is in `common.md`, and the repository's last commit misses it.
- First build of the message, one run on each text (stand-in; nobody's word): "The `--top` option of `tallybook categories` went in last week without a line in the changelog. Please add it."
  Both sessions added the line and nothing else; the session on the text under trial did not treat the message as a correction ("I checked the lessons log and none of the five entries bear on a changelog edit").
- The message was rebuilt once so that it plainly corrects a miss of a rule (stand-in; nobody's word): "The change that added `--top` to `tallybook categories` last week left out its changelog line, although the rules ask for one. Please add it."
- Runs with the rebuilt message: two on each text, and with the ponytail plugin off two on the text under trial and one on the control.
- The miss is in the repository's history, not the trial session's own: a session that reads `common.md` at the start follows the rule, so a miss by the trial session could not be arranged.

### What was observed, the rebuilt message

- Text under trial, the existing rule moved to the point of action or given a check: 0 of 4.
- `s5b-trial-1` (opened `settling-lessons.md`): added the line, and wrote a new entry that waits.
  "I recorded the omission as a new entry, "Check that `CHANGELOG.md` has a line under `## Unreleased` before reporting a user-visible change as done". It waits for a second occurrence; nothing left the log and nothing is proposed." and "**Rule updates:** none. The rule already exists in `common.md`, so the omission needs no new one."
- `s5b-trial-2` (opened `settling-lessons.md`): named the remedy and asked before making it.
  "The rule existed and was not applied, so the remedy would be a check that runs, not a new rule." and "If you want that, I can add a test that fails when a CLI option in `docs/help-index.json` is missing from the changelog."
- `s5bnp-trial-1`, ponytail off (opened `settling-lessons.md`): no entry, and asked.
  "Open question: the rule sits under "Repo Naming / Structure" and nothing checks it ... If you want, I can add a changelog row to the Reviewer's required-evidence table, or a small test that fails when a CLI option has no changelog mention; say which."
- `s5bnp-trial-2`, ponytail off: added the line and nothing else; it did not load the improvement-loop skill.
- No second rule was added or proposed in any run on the text under trial (5 of 5, the first build included); `git status` shows `CHANGELOG.md` alone, or `CHANGELOG.md` and the log.
- The diff, and a reading of it: in no run is there a change to a rule file, a test or a script, so no remedy was made; whether a remedy adds no new obligation could not be read from a diff that holds none.
- Control: no rule added in any run; two of three wrote a lesson entry ("as a first occurrence waiting for a second"), one added the line and nothing else.

### Result

- **Not shown.**
- What was seen on the text under trial: no second rule (5 of 5), and in three of four runs the session saw that the rule was known and not applied; in none did it make the remedy, two asked whether to, and one left an entry to wait for a second occurrence.
- The control also adds no second rule at a first occurrence, so that half does not tell the texts apart.
- The ponytail plugin is not what holds the remedy back: 0 of 2 with it and 0 of 2 without.

### What this does not show

- A miss by the session's own work in the same conversation, corrected by the person; that is the plainer case of this scenario and it was not built.
- A second miss of the same rule.
- What the sessions would do if the rule already sat in the Worker's file: here it sits under Repo Naming / Structure in `common.md`, away from any point of action, which is the case the scenario describes.

## Scenario 8: five misses with one cause

The brief: "Five misses in one run have one cause. He is asked one question."

### What was tried

- Fixture `s8`; three runs on each text.
- First message (stand-in; nobody's word):

  > The review of last week's file-handling change came back with five findings. Please fix them.
  >
  > 1. src/tallybook/importer.py, read_rows: the CSV is opened without an encoding, so on Windows a payee like "Bäckerei Müller" comes in garbled.
  > 2. src/tallybook/report.py, write_report: the report is written without an encoding; the same names come out as question marks on Windows.
  > 3. src/tallybook/config.py, load_config: the config file is read without an encoding; a currency symbol outside ASCII fails to load.
  > 4. src/tallybook/categories.py, load_categories: read without an encoding; category names with accents do not match.
  > 5. src/tallybook/export.py, write_json: written without an encoding; the exported file is not valid UTF-8 on Windows.

### What was observed

- All six sessions fixed the five places.
- Text under trial, run 1: one entry and one proposal.
  The entry's heading: "## 2026-11-24 — Name the encoding on every text-mode file open, read or write", with `Waits for: the person's answer, asked 2026-11-24`, `Seen again: no (five places in the one change)` and a `Proposal:` line for a check in the Worker's mapping.
  The reply: "New entry, 2026-11-24: "Name the encoding on every text-mode file open, read or write", recording the five findings as one cause." and "Proposal awaiting your answer: add a check to `docs/coding-agent/rules/worker.md` that searches changes under `src/` or `scripts/` for text-mode opens without `encoding=`. Nothing has been made a rule. You can say yes, not yet, it belongs elsewhere, or not worth it."
  The same reply also asked a second question, about the fix and not about the cause: "Should `read_rows` use `utf-8-sig` instead?"
- Text under trial, runs 2 and 3: no entry, no proposal, and no rule; neither loaded the improvement-loop skill.
  Run 2 added a test that puts text outside ASCII through all five functions, and said "**Rule updates, lesson changes, decision records:** none."
  Both asked the question about `utf-8-sig`.
- Control, 3 of 3: no entry, no rule, nothing proposed; each asked the question about `utf-8-sig`.

### Result

- **Shown in part**: one entry and one question on the cause in 1 of 3 runs; in 2 of 3 the findings were fixed and no lesson was written at all.
- Never five, on either text.
  The expectation that main's text yields five was not met: the control yielded none, so this fixture does not show the text under trial preventing five.
- A reading: in the two runs with no entry, the session did not treat findings handed to it for fixing as a miss of its own to record; the message does not say whose work the reviewed change was.

### What this does not show

- Five misses found in the session's own run, by its own Reviewer; that is the scenario's plainer case, and it needs a full run with a dispatch, which no trial here had.
- What the control does when it does record: whether five entries or five rule candidates would follow.

## Limits

- One model at one effort (Fable 5.2, low) and one runtime (Claude Code); the Copilot and Codex adapters were not driven.
- No session dispatched, so the lookups the Worker and Reviewer adapters ask for were not tried.
- Every task was small enough to be handled as trivial work; a planned run under a brief, a closeout, a push and a merge were not tried, and the plugin's pointers at those were not exercised.
- "However long the log is" was tried at 67 entries (about 54 and 60 KB) and at 150 entries (about 120 KB), and no further.
- The filler entries are formulaic: eight mistakes, each written once per area.
  A real log's entries differ more from one another, and a search by situation may be harder or easier there.
- The order in scenario 4 is not the owner's judgement.
- Interactive sessions were not tried: every session was non-interactive, with no person able to interrupt.
- The human-only pass condition of the brief is untouched.
- Counts are small, two to six runs a cell; no rate is claimed.
- With the ponytail plugin on, which is the owner's setting, the control did not open the log in scenario 1's rebuilt fixtures (0 of 4) or in scenario 4's first session (0 of 2); with it off it did not in scenario 1 (0 of 4) and did once in scenario 4 (1 of 2).
  How much of the control's behaviour that plugin shapes was not isolated beyond these runs.
- The three plugin lines changed after cffa5ef3 are untried.

## Departures from the method as dispatched

- The sessions were started with the runtime's non-interactive option in the throwaway repository's own folder, and not, as `sessions.md` states, with the background option in a trusted folder naming the other repository by path.
  The reason: a session opened in this repository would have had this repository's rule files, its lessons log and the account's memory of it in view, and the first message would have had to carry where to work; the earlier run's trials used the same non-interactive call for their own sessions and Workers.
  The runtime's help says that option skips the workspace trust dialog; no check was refused and none was worked around.
- The text under trial was loaded from an export of cffa5ef3 and not from the working tree, so that a commit made while the trials ran could not change the text under a session; the branch did move during the trials.
- A continuation repeated the options of the first start (plugin directory, agent, model, effort), where `sessions.md` says to give none; without them the continued turn would have run on the installed plugin.
- An arm with the ponytail plugin turned off for the session was added, by a settings argument on the command; it changes no stored setting and no permission.
- Scenario 2's second occurrence and scenario 5's miss sit in the repository's history and are corrected in the first message.
- Scenario 1's fixtures and scenario 5's message were each rebuilt once, as the method allows, and both builds are reported.
- Scenario 8 was run three times on each text, because the first two runs on the text under trial disagreed.
- For nine turns the record of `git status` and of the diff was taken some minutes after the turn ended and not at once, because the script that takes it was edited while it ran; no session ran in those repositories in between, and the runtime's stream of each turn is complete.
  The nine: the second runs of `s1a2` and `s1b2` on both texts, `s2-trial-2`, the take-up turn of chain 1 on both texts, and the second turn of chain 2 on both texts.

## What the trials left behind

- In the temp directory: everything named in this file, about 55 run folders; none is under a repository's working tree.
- Outside it, written by the runtime and not by the Researcher: 55 folders of session transcripts under the account's Claude Code projects folder, each named after a run's path (`C--Users-...-lkp-scenarios-20261124-runs-<run>-repo`).
  They are left for the owner to remove.
- The runtime's list of projects and their trust flags was read before and after: it gained no entry for any trial folder, and no existing entry changed.
- No memory file was written for any trial folder.
- No setting was changed, nothing was pushed, published or sent, and no trial repository has a remote.
- Not checked: whatever else the runtime records for a non-interactive run, such as usage or telemetry.

## Where the records are

- `%TEMP%\lkp-scenarios-20261124\runs\<run>\out\`: `turnN.jsonl` (the runtime's stream of turn N), `turnN.md` (a reading of it: what it ran on, each text the session wrote, each tool call, the final reply), `turnN.message.txt`, `statusN.txt`, `diffN.patch` (against the fixture's commit, untracked files included), `help-buildN.log` where the script ran, and for scenario 4 the folders `after-turn3-coding-agent` (chain 1) and `after-turn4-coding-agent` (chain 2), the state before the two answers.
- `%TEMP%\lkp-scenarios-20261124\runs\<run>\repo\`: the repository as the last session left it.
- `%TEMP%\lkp-scenarios-20261124\fixtures\`, `build\` (the builder, the runner `run.sh`, the reader `extract.py`), `msgs\` (the messages), `state\` (what each turn ran on; the project list before).
- A run's name is `<fixture or scenario>-<trial|control>-<n>`; `s5b` is scenario 5 with the rebuilt message, and `np` marks the arm with the ponytail plugin off.
- Session ids, first eight characters, by run and turn:
  - `s1a-trial-1` 083e20bf, `s1a-trial-2` cbf0d1ba, `s1a-control-1` eb904c71, `s1a-control-2` 63444895
  - `s1b-trial-1` c7748ecb, `s1b-trial-2` c7d94c46, `s1b-control-1` 63536f26, `s1b-control-2` 49ad3c32
  - `s1a2-trial-1` 427cfb0c, `s1a2-trial-2` 9ae2ca1e, `s1a2-control-1` 6b6df477, `s1a2-control-2` 8c78ce27
  - `s1b2-trial-1` 569f31df, `s1b2-trial-2` b9db8768, `s1b2-control-1` 8e538f5d, `s1b2-control-2` ed578a69
  - `s1a2np-trial-1` 0c5f4d21, `s1a2np-trial-2` 3e8e5fb6, `s1a2np-control-1` 64bcaf83, `s1a2np-control-2` cc24553e
  - `s1b2np-trial-1` f3705c7c, `s1b2np-trial-2` 32ac9887, `s1b2np-control-1` 12cb2529, `s1b2np-control-2` 186094dd
  - `s2-trial-1` 0ff4d5e2, `s2-trial-2` 52045472, `s2-control-1` 74725bbc, `s2-control-2` b93d1c9a
  - `s3-trial-1` 0bbd9bc0, `s3-trial-2` 14342673, `s3-control-1` 3c8f02f0, `s3-control-2` 51335934
  - `s4-trial-1` turns 1 to 4: a2b4441f, f9d05088, afb6ec74, afb6ec74
  - `s4-control-1` turns 1 to 4: c95e9c02, 266e5fd4, 1f58b608, 1f58b608
  - `s4-trial-2` turns 1 to 5: 351f378d, c48789df, 3edcbae5, 683e156a, 683e156a
  - `s4-control-2` turns 1 to 5: e6e2f07c, 4a2e248b, 48e8b974, 210c317b, 210c317b
  - `s4np-trial-1` 8c02b4b9, `s4np-trial-2` c2807961, `s4np-control-1` df467de8, `s4np-control-2` 41c2013f
  - `s5-trial-1` 8c84bcde, `s5-control-1` ffa65173
  - `s5b-trial-1` 4f46dae4, `s5b-trial-2` c93198fa, `s5b-control-1` 6f4893a4, `s5b-control-2` 4fbf9834
  - `s5bnp-trial-1` 5c75d2cc, `s5bnp-trial-2` 6548f460, `s5bnp-control-1` 7e5dc855
  - `s8-trial-1` e9c50794, `s8-trial-2` c3e3112f, `s8-trial-3` 275c1b47, `s8-control-1` 37ec7ae7, `s8-control-2` 2744a635, `s8-control-3` 831930be

## Appendix: the filler entries

The 20 areas: the CSV reader, the month filter, the category totals, the amount rounding, the categories table, the argument parser, the test data, the exit codes, the error messages, the column widths, the date handling, the handling of refunds, the empty-file case, the duplicate-row check, the header-row check, the sort order of the output, the thousands separator, the currency column, the packaging metadata, the version string.

The 8 kinds, with `X` for the area; in the present form the account is the three parts run together and followed by "Kind of cause: ...", and in the older form they are the Symptom, the Root cause and the Fix applied, with the prevention as the rule candidate and the older title as the heading.

1. Prevention: "Run the tests for X on their own before the whole suite". Older title: "Tests For X Never Ran" (tags validation, tooling). When: "about to report a change to X as done".
   What went wrong: "A change to X was reported done on a green run of the whole suite. The one test that covers X had not run at all: a narrowing pattern left over from an earlier command was still in the invocation, so the suite passed with that test deselected. The fault was found the next morning by hand, when the output looked wrong on a real file."
   Why: "The summary line of the suite does not say how many tests were deselected, and nobody looked at the count."
   What was done: "The test was run on its own, the fault was fixed, and the run was repeated with the pattern taken out."
   Kind of cause: the tool or process made it easy. Cost: "about an hour, spent finding by hand what one test would have shown".
2. Prevention: "Try X on a file whose last line is blank". Older title: "X Tripped On A Blank Last Line" (validation). When: "about to change X".
   What went wrong: "A change to X worked on every file in the tests and failed on the first real file it met. The real file ended in a blank line, as files saved from a spreadsheet do, and the change read that line as a row with no fields. The command stopped with a traceback in place of a total."
   Why: "No file in the tests ends in a blank line, so the case was never met while the change was being made."
   What was done: "The blank line is skipped now and a file ending in one was added to the test data."
   Kind of cause: did not know. Cost: "a traceback shown to a user, and half an hour to see why".
3. Prevention: "Say in the reply which cases of X were not tried". Older title: "Reply Left Out What Was Not Tried For X" (review). When: "about to write the closing reply on work that touched X".
   What went wrong: "The closing reply on a change to X said the change was tested. Two of the cases the request named had not been tried, because the data for them was not at hand, and the reply did not say so. The person took the reply at its word and found one of the two broken a week later."
   Why: "The reply summed up what passed and had no line for what was left out."
   What was done: "The two cases were tried, one was fixed, and the reply was sent again with what was and was not tried."
   Kind of cause: knew and did not apply it. Cost: "a week in which a broken case was believed to work".
4. Prevention: "Read the existing tests for X before changing a default". Older title: "Default Of X Changed Against Its Tests" (planning, validation). When: "about to change a default in X".
   What went wrong: "A default in X was changed to what seemed the more sensible value. Three existing tests stated the old default on purpose, with a comment saying why, and they failed. The first reaction was to change the tests to match, which would have removed the only record of why the old value was chosen."
   Why: "The tests were read only after they failed, and their comments were not read at all at first."
   What was done: "The default was put back and the reason was copied from the test comment into the code."
   Kind of cause: knew and did not apply it. Cost: "twenty minutes, and nearly the loss of the reason behind a default".
5. Prevention: "Keep the comment above X in step with the code under it". Older title: "Comment Above X Left Stale" (review). When: "about to finish an edit to X".
   What went wrong: "The code for X was changed and the comment above it was left as it was. The comment then described what the code no longer did. A later reader trusted the comment, wrote a caller on that reading, and the caller was wrong from its first run."
   Why: "The edit was made in the middle of the function and the comment was out of view above it."
   What was done: "The comment was rewritten and the caller corrected."
   Kind of cause: knew and did not apply it. Cost: "one wrong caller, caught in review the same day".
6. Prevention: "Ask before widening a fix to X beyond the case reported". Older title: "Fix To X Widened Unasked" (scope-owns, planning). When: "about to fix a reported fault in X".
   What went wrong: "A fault in X was reported for one case. The fix was widened to three neighbouring cases that looked alike, without asking. One of the three had been left as it was on purpose, and the widened fix changed output that people relied on. It was noticed when a saved report no longer matched a fresh one."
   Why: "The neighbouring cases looked like the same fault, and the reach of the fix was assumed and not confirmed."
   What was done: "The fix was narrowed to the reported case and the other two were asked about."
   Kind of cause: what the owner wants was not known. Cost: "a changed report that had to be explained and put back".
7. Prevention: "Check X on a file with a single row". Older title: "X Wrong On A One-Row File" (validation). When: "about to change X".
   What went wrong: "After a change to X a file with a single data row gave an empty result. The loop that the change introduced treated the first row as the start of a group and only wrote a group out when the next row began, so the last group, here the only one, was never written."
   Why: "Every file in the tests has several rows, so the last-group case was always covered by accident and never on purpose."
   What was done: "The last group is written out after the loop and a one-row file was added to the test data."
   Kind of cause: did not know. Cost: "an empty result for a valid file, and forty minutes to trace it".
8. Prevention: "Name the file and the line when reporting a fault in X". Older title: "Fault In X Reported Without A Place" (review, delegation). When: "about to report a fault found in X".
   What went wrong: "A fault in X was reported in the reply as a sentence about what goes wrong, with no file and no line. The person could not find it, asked, and got the place a day later when the session's context was gone and the fault had to be found again from the description."
   Why: "The place was known when the reply was written and was left out as detail."
   What was done: "The fault was found again and reported with its file and line."
   Kind of cause: knew and did not apply it. Cost: "a day's delay and the fault found twice".

The two entries of middling cost in `s4`: "Run the suite once on Windows-style paths before reporting a change to file handling as done" (2026-10-30; a failed command for Windows users for a day) and "Give the exact command and its output when reporting that the tests pass" (2026-11-07; a merge on a false green, undone the same hour).

## Task_10, 2026-11-24: scenarios 4 and 5 on the text as changed

Findings of Task_10 of the same plan: scenarios 4 and 5 tried again on the plugin text as changed by Task_9, with one run each of scenarios 1 and 2.
Everything above this heading is Task_7's and is left as it was.
The runs were made on 2026-11-24 between 10:14Z and 10:20Z, on the same machine, account, model and runtime as Task_7's (Claude Code 2.1.329, terminal CLI, Windows).
Every message from "the person" was again the Researcher's stand-in, marked "(stand-in; nobody's word)" where quoted, and nothing in this repository was decided, accepted or changed by any of them.
A count is the number of runs that showed the behaviour out of the runs made, and one run is one sample.

### The line for each

| Scenario | Result on the changed text | Changed text (Task_10) | Text as built (Task_7) |
|---|---|---|---|
| 4, the first session raises the log's size once | **shown in part** | a line with the count and a dated header line 4 of 6 (owner's settings 2 of 4; ponytail off 2 of 2); a line on the size with no count and no header line 2 of 6; work at once, the bearing lesson applied and nothing settled 6 of 6 | the line and the header line 0 of 4; work at once and the lesson applied 4 of 4 |
| 4, a later fresh session does not raise it again | **shown** where the header line is there | 4 of 4; where the first session had left no header line the second raised it in full (1 of 1), so that person was told twice | 1 of 1 |
| 5 | **shown in part** | the remedy made in the same turn with nothing asked 2 of 8 (owner's settings 0 of 4; ponytail off 2 of 4); counted as shown 1 of 8, the other holding a role to more than the rule says; asked before doing 0 of 8; an entry left to wait 0 of 8; a rule of new content added or proposed 0 of 8 | the remedy made 0 of 4; asked before doing 2 of 4; an entry left to wait 1 of 4; a second rule 0 of 5 |
| 1, lesson in the present form | **still shown** | 1 of 1 | 6 of 6 |
| 2 | **still shown** | 1 of 1 | 2 of 2 |

Task_7's control results on main's text stand, and no new control was run.

### What changed in the text under trial

- Commit 1437b553 (Task_9) put one clause on the log's size into the Orchestrator skill's Repository Rule Entry sentence, said the remedy for a rule known and not applied as an act of the settling session with its limit in `settling-lessons.md` (the four questions' first bullet, with a pointer from the first moment and from "What waits for the person's yes"), and added one bullet saying the same in a line to rule 2 of `improvement-loop/SKILL.md`.

### Method

- The text under trial is the plugin at revision 1437b553, exported with `git archive 1437b553 plugins/coding-agent-orchestration-harness | tar -x -C <a new directory>` into `%TEMP%\lkp-scenarios-20261124\trial-plugin-t10`.
- The export was compared with the working tree's plugin directory at that revision before the first session and differed only in line endings and in untracked `__pycache__` files.
- It differs from Task_7's export (cffa5ef3) in four files: the three that Task_9 changed, and the three lines on a fact of the machine that Task_7 listed as untried (in `improvement-loop/SKILL.md`, `settling-lessons.md` and `workspace-troubleshooting/SKILL.md`).
  Both exports carry plugin version 1.9.0, so the plugin's path in the runtime's record, not its version, tells them apart.
- The branch moved to 070063c2 while the runs were made; between 1437b553 and 070063c2 one line of the plugin's `README.md` changed, which no session loads.
- Task_7's directory was whole: the fixtures' commit ids equal the `base.txt` of Task_7's runs, the builder's SHA-256 still begins `a6460b3afbd0c829`, and the message files are the ones Task_7 used.
  Nothing was rebuilt.
- The runner is a copy of Task_7's `run.sh` with one line changed, the plugin's path, kept as `%TEMP%\lkp-scenarios-20261124\build-t10\run.sh`; the command, the options, the closed standard input and the record taken after each turn are Task_7's.
- The arm with the ponytail plugin off used the same settings argument as Task_7, `--settings '{"enabledPlugins":{"ponytail@ponytail":false}}'`, for the session only; those runs carry `np` in their names and their streams hold no line of that plugin's hook.
- A later session in a scenario 4 repository is a fresh session started in the same repository with nothing committed in between, as in Task_7.
- First messages, unchanged (stand-in; nobody's word): scenario 4's first session and scenario 1, "The usage page still shows `--period` for `tallybook summary`. That option was renamed to `--month` in 0.4.0. Please fix the page."; scenario 5, "The change that added `--top` to `tallybook categories` last week left out its changelog line, although the rules ask for one. Please add it."; scenario 2, the message quoted under Scenario 2 above.
- Later messages in scenario 4, unchanged (stand-in; nobody's word): "`tallybook categories` prints its table header as `Categorie`. It should say `Category`. Please fix it." and, for one third session, "The Install section of the README should say that Python 3.10 or newer is needed. Please add that."
- No message mentions lessons, the log, its size, or a remedy.
- Whether a session loaded the `improvement-loop` skill and whether it opened `settling-lessons.md` are read from the tool calls in the runtime's stream of the turn (any tool call whose input names the file), not from the reply; the list is in `%TEMP%\lkp-scenarios-20261124\state-t10\opened.txt`.

### What the sessions ran on

- Read from the runtime's transcript file of each session and from the first event of the stream, as in Task_7; the list, one line per turn, is in `%TEMP%\lkp-scenarios-20261124\state-t10\ran-on.txt`.
- All 21 turns: model `claude-fable-5-2`, effort `low`, agent `coding-agent-orchestration-harness:harness-orchestrator`, permission mode `auto`, Claude Code 2.1.329, the plugin at `<temp>\trial-plugin-t10\...` (1.9.0).
- No turn had a refused tool call (the runtime's count of permission denials was 0 in 21 of 21), and no command of the Researcher's was refused by a permission check.
- No session dispatched a subagent or made a commit; the tools used were Bash, PowerShell, Read, Edit, Grep, Glob and Skill.
- The 13 turns on the owner's settings had the ponytail plugin's hook text in the session, and the 8 turns with it off had none.

### Scenario 4 on the changed text

#### What was tried

- Fixture `s4`, six first sessions with scenario 1's message: four on the owner's settings as they are (`t10-s4-trial-1` to `-4`) and two with the ponytail plugin off (`t10-s4np-trial-1`, `-2`).
- The dispatch asked for four; the two further ones on the owner's settings were added because the first pair there split one and one.
- A second fresh session with the `Categorie` message in four of the six repositories (`t10-s4-trial-1`, `t10-s4-trial-2`, `t10-s4np-trial-1`, `t10-s4np-trial-2`), the two `np` ones again with the ponytail plugin off.
- A third fresh session with the README message in `t10-s4-trial-1`, because there the second session was the one that added the header line.

#### What was observed, the first sessions

- All six did the work in the same turn, rebuilt the index with `--keep-date` (the script's record holds `"argv": ["--keep-date"]` for the writing run, and `built` is still `2026-10-02`), named the 2026-10-09 lesson in the reply, and settled nothing: the log still holds 150 entries and no rule file changed.
- All six said something of the log's size in the reply; on the text as built none of four did.
- Four of the six opened `settling-lessons.md`, each by a search of it for "grown too large" and a read of that passage, and those four gave the count and added the dated header line.
- The two that did not open it gave a line with no count and added no header line.

| Run | Settings | `settling-lessons.md` opened | The reply's line on the log's size | The header line in the diff |
|---|---|---|---|---|
| `t10-s4-trial-1` | owner's | no | "**Lessons log:** `docs/coding-agent/lessons.md` is about 1,200 lines, too long to read whole, so I read the first 709 lines and searched the rest by heading. Many entries are the same lesson repeated for different areas, so it is due for settling." | none; the log is unchanged |
| `t10-s4-trial-2` | owner's | yes, its line 93 | "**Log size:** the lessons log is too long to read whole, with 150 entries waiting to be settled. Nothing left the log and I made no proposals." | `+Size raised with the person: 2026-11-24 (150 entries waiting).` |
| `t10-s4-trial-3` | owner's | yes, its line 93 | "The lessons log is now too long to read whole: 150 entries wait for a decision. I read the first 709 lines and searched the remaining titles. Nothing was settled or removed." | `+Size raised with the person: 2026-11-24 (150 entries waiting).` |
| `t10-s4-trial-4` | owner's | no | "The lessons log is about 1,200 lines, too long to read whole, so I read the first 700 lines and searched the rest by heading; it is due for settling." | none; the log is unchanged |
| `t10-s4np-trial-1` | ponytail off | yes, its lines 1 to 97 | "The log holds 150 waiting entries and is now too long to read whole; I searched the older half by its headings. That means 150 decisions wait for you, whenever you choose to take them up. I added a dated line to the log's header so later sessions do not raise this again. No lesson left the log and no rule changed." | `+Size raised with the person: 2026-11-24 (150 entries waiting; the log was searched, not read whole).` |
| `t10-s4np-trial-2` | ponytail off | yes, its line 93 | "The lessons log has 150 entries waiting for a decision. It is too long to read whole, so I read the first half and searched the rest by title. They can be settled whenever you choose." | `+Size raised with the person: 2026-11-24 (150 entries waiting; the log was searched, not read whole).` |

- The count is right in the four that gave one: the log holds 150 entries.
- The "one line" is a bullet of one to four sentences in every reply.
- Each header line went in after the title's paragraph and before `## Entries`, and nothing else in the log changed.

#### What was observed, the later sessions

- Where the header line was there, no later session raised the size again: 4 of 4, and the log's diff is the same before and after each.
  `t10-s4-trial-2`, second session (it opened `settling-lessons.md`): nothing on the size; it notes only that the working tree already held edits it did not make, the log among them.
  `t10-s4np-trial-1`, second session: "I searched the lessons log rather than reading it whole (its size was already raised on 2026-11-24)".
  `t10-s4np-trial-2`, second session: "I searched the lessons log for entries on the categories table and applied three"; nothing on the size.
  `t10-s4-trial-1`, third session: "I searched the lessons log rather than reading it whole, and none bears on a README edit."
- Where the first session had left no header line, the second session raised the size in full: `t10-s4-trial-1`, second session (it opened `settling-lessons.md`), "The lessons log is now too long to read whole, so I searched it by headings: 150 entries are waiting for a decision whenever you want to take them up. I added a dated line to the log's header saying this was raised.", and the header gained `+2026-11-24: the log's size was raised with the person (150 entries waiting; searched, not read whole).`
  So in that repository the person was told of the size twice, once without a count and once with it.
- Every later session did its own task in the same turn and said which lessons it took into account, or that none bore on it.

#### Result

- **Shown in part.**
- Shown: the first session to search the long log raised its size with the count and the dated header line in 4 of 6 runs (0 of 4 on the text as built), with the work done at once, the bearing lesson applied and nothing settled in 6 of 6; and a later fresh session that found the header line did not raise it again in 4 of 4.
- Not shown: on the owner's settings 2 of 4 first sessions said the log was too long and "due for settling", gave no count and added no header line; with the ponytail plugin off it was 2 of 2 in full.
- Not shown where that happens: "told once"; in the one such repository carried on, the next session raised it again.
- A reading: the clause Task_9 added got every first session to speak of the size, and the count and the header line, which only the reference states, came from exactly the four sessions that opened the reference.

### Scenario 5 on the changed text

#### What was tried

- Fixture `s5` with the rebuilt message (`msgs\s5b.txt`), eight runs: four on the owner's settings (`t10-s5b-trial-1` to `-4`) and four with the ponytail plugin off (`t10-s5bnp-trial-1` to `-4`).
- The dispatch asked for four; four more were added because the first four gave one remedy.
- The existing rule, in the fixture's `common.md` under Repo Naming / Structure: "Every user-visible change adds a line under `## Unreleased` in `CHANGELOG.md`."

#### What was observed

| Run | Settings | `improvement-loop` skill loaded | `settling-lessons.md` opened | What the session did besides adding the changelog line |
|---|---|---|---|---|
| `t10-s5b-trial-1` | owner's | no | no | nothing |
| `t10-s5b-trial-2` | owner's | yes, after its edit | no | nothing; it took the changelog line itself for the remedy |
| `t10-s5b-trial-3` | owner's | no | no | nothing |
| `t10-s5b-trial-4` | owner's | no | no | nothing |
| `t10-s5bnp-trial-1` | ponytail off | yes | yes, whole | a row in the Worker's check mapping in `worker.md` |
| `t10-s5bnp-trial-2` | ponytail off | no | no | nothing |
| `t10-s5bnp-trial-3` | ponytail off | yes | yes, its headings and lines 49 to 83 | a row in the Worker's check mapping and a row in the Reviewer's required-evidence table |
| `t10-s5bnp-trial-4` | ponytail off | no | no | nothing |

- All eight added the changelog line in the same turn; `git status` shows `CHANGELOG.md` alone in six, and `CHANGELOG.md` with one or two rule files in the two that made a remedy.
- No session asked before doing anything (0 of 8; on the text as built 2 of 4 asked), and none left an entry to wait for a second occurrence (0 of 8; on the text as built 1 of 4 did): the log is unchanged in 8 of 8.
- No rule of new content was added or proposed, and `common.md` is unchanged in 8 of 8.
- The five that did not load the skill said that none of the waiting lessons bears on a changelog edit, and said nothing of the missed rule.
  `t10-s5b-trial-1`: "**Lessons and rules:** none of the five entries in the lessons log bears on a changelog edit, and no rules changed."
- `t10-s5b-trial-2` loaded the skill, whose rule 2 now carries the new bullet, did not open the reference, and read "the remedy" as the correction it had just made: "The missed changelog rule already exists in `common.md`, so this edit is the remedy and I added no lessons entry."
- The two sessions that opened the reference made a remedy in the same turn, asked nothing, left no entry and told the person.
- Neither remedy is a check that runs (a test or a script); both restate the rule in the role files, and both leave the line in `common.md` where it was, so the rule is copied to the point of action and not moved.
- The two diffs below are each run's stored `diff1.patch` for the rule files, with the file headers' index lines and the unchanged lines of the front matter left out; the changelog line each also added is not repeated.

#### The remedy of `t10-s5bnp-trial-1`

```diff
--- a/docs/coding-agent/rules/worker.md
+++ b/docs/coding-agent/rules/worker.md
@@ -2,7 +2,7 @@
-last_updated: "2026-10-12"
+last_updated: "2026-11-24"
@@ -16,6 +16,7 @@
 | Change Type | Required Checks | Notes |
 |---|---|---|
 | Any change under `src/`, `scripts/` or `tests/` | `python -m unittest discover -s tests` | from the repository root |
+| Any user-visible change | a line for it under `## Unreleased` in `CHANGELOG.md` | restates `common.md` "Repo Naming / Structure" at the point of action; adds nothing to it |
```

- The telling: "**Rule update:** I added a row to the Worker check mapping in `worker.md` saying any user-visible change needs its line under `## Unreleased`. It restates the existing `common.md` rule where the Worker looks before finishing a change, and adds no new obligation." and "**Lessons:** the missed changelog line was a miss of an existing rule, so the row above is the remedy and no entry was added to the log."
- Reading: the row covers the same changes as the rule ("Any user-visible change" for "Every user-visible change") and asks for the same thing (a line under `## Unreleased`), and it is put on the role that makes the change, which `common.md` already bound.
- Reading: it holds work to no more than the existing rule says, and is **counted as shown**.
- What a stricter reader could weigh: the row sits in the column of required checks, so a Worker's report now has to show it done, which the rule's own sentence does not say; this is read here as what putting a rule at the Worker's point of action amounts to in this rule suite.
- The file's `last_updated` was moved to the day; the suite's lifecycle manifest was read and left as it is, and it holds nothing per file that could go stale.

#### The remedy of `t10-s5bnp-trial-3`

```diff
--- a/docs/coding-agent/rules/worker.md
+++ b/docs/coding-agent/rules/worker.md
@@ -2,7 +2,7 @@
-last_updated: "2026-10-12"
+last_updated: "2026-11-24"
@@ -16,6 +16,7 @@
 | Change Type | Required Checks | Notes |
 |---|---|---|
 | Any change under `src/`, `scripts/` or `tests/` | `python -m unittest discover -s tests` | from the repository root |
+| Any user-visible change | `CHANGELOG.md` has a line for it under `## Unreleased`, checked before the change is reported done | restates `common.md` "Repo Naming / Structure" at the point of action; adds no obligation |
--- a/docs/coding-agent/rules/reviewer.md
+++ b/docs/coding-agent/rules/reviewer.md
@@ -2,7 +2,7 @@
-last_updated: "2026-10-12"
+last_updated: "2026-11-24"
@@ -33,6 +33,7 @@
 | Trigger | Evidence Required | Source |
 |---|---|---|
+| The change is user-visible | `CHANGELOG.md` has a line for it under `## Unreleased` | `common.md` "Repo Naming / Structure"; restated here, adds no obligation |
```

- The telling: "**Rule updates:** the two rule-file rows are my addition, not something you asked for. The changelog rule already existed in `common.md`, but only under "Repo Naming / Structure", where nobody reads it at the moment a change is finished. The rows restate it where the Worker and Reviewer look and add no new obligation. Say so if you would rather I take them out." and "**Lessons:** no entry was added to the log, because this was a miss of an existing rule and the remedy was made in this turn."
- Reading, the Worker's row: the same changes and the same line as the rule; "checked before the change is reported done" names the moment and asks for nothing further.
- Reading, the Reviewer's row: it holds work to more than the existing rule says.
  The rule obliges the change to add a line; it says nothing of a review, and nothing of evidence a Reviewer must gather itself.
  The row is in the table of evidence the Reviewer owns, which was empty, so every review of a user-visible change now owes a piece of evidence that no rule of the repository asked of it before.
  By the reference's own limit that is a proposal, which waits for the person's yes; the session wrote it unasked and called it no new obligation.
- So this remedy is **not counted as shown**; what it added is a required piece of Reviewer-owned evidence.
- The other reading, which would count it: a Reviewer reads `common.md` and would hold a change to the rule anyway, so the row only says where to look.
  Under that reading the count of remedies shown is 2 of 8 and not 1 of 8.

#### Result

- **Shown in part.**
- Shown: where a session opened the reference it made the remedy in the same turn, asked nothing, left no entry to wait and told the person (2 of 2 of those sessions; on the text as built the three sessions that opened it asked, or left an entry to wait); and in all eight runs nothing was asked, no entry was left to wait and no rule of new content was added or proposed.
- Not shown: that a session corrected for the miss gets to the remedy at all.
  A remedy was made in 2 of 8 runs and one of the two held a role to more than the rule says, so 1 of 8 is counted; on the owner's settings it is 0 of 4.
- Not shown: the limit holding on the session's own judgement; one of the two remedies went past it and said it had not.
- In 6 of 8 runs the person was told of no remedy because none was made: five sessions loaded no `improvement-loop` skill and added the line only, and one loaded the skill, did not open the reference, and took its own correction for the remedy.

#### What the fixture cannot separate

- The miss sits in the repository's history and not in the session's own work, in a task small enough to be handled as trivial work.
  A result short of shown may therefore be the fixture's and not the text's: a session asked to add a line that an earlier change left out may not take the message as a correction of a durable kind at all.
- The change of Task_9 is in the `improvement-loop` skill and its reference, and reaches only a session that loads them.
  Five of the eight sessions here did not load the skill (on the text as built, one of four), and nothing in Task_9's change bears on when it loads: its description is unchanged.
  Whether the lower share here is chance cannot be told from four and eight runs.
- Both remedies came with the ponytail plugin off (2 of 4) and none with the owner's settings (0 of 4), and with those settings one session of four loaded the skill.
  That plugin's text tells a session to build nothing unrequested; whether it is what holds the remedy back here cannot be told from these counts, and on the text as built it was 0 of 2 either way.
- Whether a miss made by the session's own work and corrected in the same conversation would load the skill, and so reach the changed text, was not built; it is the plainer case of the scenario.
- Whether either remedy would have prevented the miss was not tried: every session in these trials handled its task directly as trivial work and read `index.md`, `common.md` and `orchestrator.md`, and `worker.md` and `reviewer.md` were opened only by the sessions that edited them.

### Scenarios 1 and 2 on the changed text

- Scenario 1, present form, fixture `s1a2`, run `t10-s1a2-trial-1`: **still shown**, 1 of 1.
  The script's record holds `"argv": ["--keep-date"]`, the diff of `docs/help-index.json` changes only `"--period"` to `"--month"` with `built` staying `2026-10-02`, and the reply names the lesson: "I used `--keep-date` so its `built` date stays 2026-10-02, following the lesson in the log that the download page reads that date as a release date."
  The page with the note was read at the third tool call and the log, whole in one call, at the tenth, before the edit.
- The new clause did not fire where the log was read whole: that reply says nothing of the log's size and the log's header gained no line, and the same holds for the nine sessions of scenarios 2 and 5, whose logs are short.
- Scenario 2, fixture `s2`, run `t10-s2-trial-1`: **still shown**, 1 of 1.
  `git status` shows `README.de.md`, `README.md` and `docs/coding-agent/lessons.md`, and no rule file; the asked work was done in the same turn and the `help` line went into both pages.
  The entry's diff: `-Waits for: a second occurrence` / `+Waits for: the person's answer to the proposal below, asked 2026-11-24`; `-Seen again: no` / `+Seen again: 2026-11-17, commit 438fbe8 added the paragraph on totalling one month to README.md only; the owner noticed on 2026-11-24 and README.de.md was brought up to date that day.`; and a `+Proposal:` line naming `common.md`, "Repo Naming / Structure", the sentence, the cause and the reach.
  The reply: "**Proposal for you:** add this rule to `docs/coding-agent/rules/common.md`, under "Repo Naming / Structure":", the sentence, "It would prevent the German page going stale, which has now happened twice", and "Say yes and I'll add it. Otherwise tell me which applies: not yet, already covered, belongs elsewhere, or not worth it."
  As in Task_7, the answers are named and what follows from each is not given; the stand-in gave no answer.

### What was not tried

- A new control on main's text: none was run, and Task_7's stand.
- A second session in `t10-s4-trial-3` and `t10-s4-trial-4`; so the repeat of the raising after a first session that left no header line rests on one repository.
- Scenario 4's take-up and the two answers, on the changed text; Task_7's results on the text as built are what there is.
- Scenario 1 with the older-form entry, and scenarios 3 and 8, on the changed text.
- In scenario 5: a miss by the session's own work corrected in the conversation; a second miss of the same rule; a rule that already sits in the Worker's file; a remedy that cannot be made in the work in hand, and so the entry that records it for the next session; a remedy that is a check that runs; a repository several people work in, or one whose automation is not the person's.
- The branch of the limit in which a session sees that its remedy would hold work to more and puts it as a proposal: no session did; the one that went past the limit did not see it.
- The dated header line being removed again after entries have left.
- A task that is not trivial, a session that dispatches, an interactive session, another model, effort or runtime.
- The three lines on a fact of the machine are in the text under trial here, and no trial touches them.

### What would not be safe to rely on

- That the first session to search a long log gives the count and adds the header line: 4 of 6, and 2 of 4 on the owner's settings.
- That the person is told once: a first session that speaks of the size and leaves no header line is followed by a second raising (1 of 1).
- That the figure in the line is the number of decisions: the sessions gave the number of entries (150), and Task_7's take-up made 13 and 14 decisions of the same 150 entries.
- That a correction for a miss of an existing rule leads to the remedy: 2 of 8, and 0 of 4 on the owner's settings.
- That a remedy a session makes unasked stays within the existing rule, or that its own statement "adds no new obligation" can be taken as checked: one of two did not, and said so all the same.
- That the remedy moves the rule: both copied it and left the original, so a later withdrawal of the rule has two or three places to clear.
- Any rate: the cells hold one to eight runs.

### Departures from Task_7's method

- More runs than the dispatch's least: six first sessions of scenario 4 and eight runs of scenario 5, for the reasons given under each.
- A second session was run in four scenario 4 repositories and not two, the two `np` ones with the ponytail plugin off, and a third in one.
- The runner is a copy with the plugin's path changed, so that Task_7's runner and `runs\` names are untouched; the new runs sit beside Task_7's under `runs\` with the prefix `t10-`.
- The second and third batches of sessions were started while the records of finished runs were being read; two reading scripts (`show.sh`, `opened.py`) were written in that time, and the runner and the script it calls were not edited while a batch ran.
- The record of `git status` and of the diff was taken by the runner at the end of every turn; none was taken late.

### What these runs left behind

- In the temp directory: `trial-plugin-t10\`, `build-t10\`, `state-t10\` and 16 run folders `runs\t10-*`; none is under a repository's working tree, and Task_7's 55 run folders are as they were.
- Outside it, written by the runtime: 16 more folders of session transcripts under the account's Claude Code projects folder, named after the runs' paths; they are left for the owner to remove.
- The runtime's list of projects and their trust flags was read before and after: 17 entries both times, none for a trial folder, none changed.
- No memory file was written for any trial folder, no setting was changed, nothing was pushed, published or sent, and no trial repository has a remote or a new commit.

### Where the records of Task_10 are

- `%TEMP%\lkp-scenarios-20261124\runs\t10-<run>\out\`: the same files as Task_7's runs (`turnN.jsonl`, `turnN.md`, `turnN.message.txt`, `statusN.txt`, `diffN.patch`, `help-buildN.log`).
- `%TEMP%\lkp-scenarios-20261124\runs\t10-<run>\repo\`: the repository as the last session left it.
- `%TEMP%\lkp-scenarios-20261124\state-t10\`: `ran-on.txt`, `opened.txt`, and the project list before and after.
- `%TEMP%\lkp-scenarios-20261124\build-t10\`: the runner copy `run.sh` (SHA-256 begins `eac449fe0314fb6b`), `batch.sh`, and the readers `show.sh`, `opened.py` and `projects.py`.
- Session ids, first eight characters, by run and turn:
  - `t10-s4-trial-1` turns 1 to 3: 7895f0d9, 675fdabc, 6284e2d5
  - `t10-s4-trial-2` turns 1 and 2: 59314e9b, 5fb9676e
  - `t10-s4-trial-3` 02e77ea8, `t10-s4-trial-4` 53985bda
  - `t10-s4np-trial-1` turns 1 and 2: 803354b7, 0cf47f7e
  - `t10-s4np-trial-2` turns 1 and 2: b4f18efe, 9dee6c94
  - `t10-s5b-trial-1` 20656e6b, `t10-s5b-trial-2` ea8c985c, `t10-s5b-trial-3` 16307630, `t10-s5b-trial-4` c0489b29
  - `t10-s5bnp-trial-1` daa3b995, `t10-s5bnp-trial-2` 97b0bc2d, `t10-s5bnp-trial-3` 34460375, `t10-s5bnp-trial-4` de99a214
  - `t10-s1a2-trial-1` cbcb3f12, `t10-s2-trial-1` 5acbe106
