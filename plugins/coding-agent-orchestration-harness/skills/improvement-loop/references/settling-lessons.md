# Settling lessons

A lesson exists so that the same mistake is not made twice. The log, `docs/coding-agent/lessons.md`, holds the lessons that still wait: each is applied when its situation arises, and each leaves the log when it is settled, so whatever is in the log has not been settled. "The person" below is whoever directs the work and whose the repository's rules are to decide. Settling (removing an entry, proposing, raising the log's size, writing to the log's header) is the work of the session that holds the work as a whole, the Orchestrator's where there is one; a seat that receives a dispatch takes lessons into account and reports what it found, a lesson candidate included, and settles nothing.

## Finding and applying lessons

- A log short enough to read whole is read whole. A longer one is searched by its headings and `When:` lines, and each entry that bears on the work is then read in full. A lesson is found by the situation it applies to, which is why an entry states it.
- Look at the start of work, for what is known then, and again at any action that was not in view at the last lookup: the mistake a lesson prevents often sits at an action nobody foresaw when the task began. Always look before an action that cannot be undone or that reaches outside the work, in trivial work too.
- A dispatch names the entries that bear on its unit, as it carries what is known of the machine. The seat that receives it looks again at an action the dispatch did not name.
- Say which lessons were taken into account, in the report or the reply, so that whoever reads it can see what the work rested on.

## A waiting lesson informs and requires nothing

A session takes a waiting lesson into account in its next judgement and says that it did. The lesson is no requirement of a plan and nothing a review or an audit holds the work to; only the person's yes gives anything from a lesson that force. Instinct goes wrong by treating the log as a second rule file. A lesson is one incident's reading, not yet checked for how far it reaches or how it should be worded.

## How a lesson leaves

A lesson leaves in one of three ways, depending on what it is:

- It is deleted: it no longer holds, a rule already says it, or the person dropped it.
- It moves into the repository's rules.
- It moves into the person's own scope, where it is a fact that holds for the person in all their repositories and for nobody else who works on this one. A fact of the person's machine goes where the machine's record is kept (`workspace-troubleshooting`, What this machine is known to do) and not into the repository's rules; the session writes it there without asking first and tells the person in a line.

A settled entry leaves in the change that settles it. What leaves is deleted, the log's version history being its trace, unless the log's header names a place where the repository keeps what leaves; then it is moved there.

## When its leaving is decided

At four moments, each of which occurs in any repository:

1. When the lesson is written, where its leaving is already clear. It is settled in the same turn, and no entry need be left in the log for what is settled; what would make it a rule still waits, as an entry, for the person's yes (What waits for the person's yes). A miss of a rule that already exists is such a case: its remedy, which holds work to no more than that rule already says, is made in that turn and no entry is left to wait for a second occurrence (The four questions, 1).
2. When the mistake occurs a second time. The entry gains a line under `Seen again:` and is worked through the four questions. Where no existing rule covers the mistake, the outcome is a proposal to the person and never a rule.
3. When a change reverses or removes what the lesson is about. That change takes the lesson with it.
4. When the log has grown too large (A log grown too large).

How much a repeat would cost decides when a lesson is first proposed: a mistake that broke output or cost significant time is proposed when it is written, and waiting for a second occurrence is for the cheap ones.

No clock decides any of this, and nothing outside the session does: not a fixed pace, a run's schedule or a job in the repository's automation. Work comes at no fixed pace, and the automation may not be the person's to change.

## What is removed without asking

A lesson that no longer holds is removed without asking, and the person is told in a line that it was and why. The reason has to be a fact the session can show:

- the conditions that produced the lesson are gone;
- a later decision reversed it;
- an existing rule already says all of what the lesson would prevent, shown by the existing-text check (The four questions, 3). A rule that says part of it is no ground.

Judging that a lesson which still holds is not worth a rule is accepting a risk on the person's behalf. It goes to them as a proposal to drop it.

## What waits for the person's yes

Nothing from a lesson becomes a new obligation on later sessions, as a rule of the repository or as a setting in the person's own scope, until the person has said yes. A review finding, and a Worker's rule candidate that is the prevention of a mistake, are lessons and wait in the same way. No context is well known enough to make an exception. The reason, which holds although a rule can be undone: a rule binds every later session, so a badly framed one is costly, and a rule made from a lesson is prone to being badly framed.

The test is whether the remedy adds an obligation. Where it adds none and only makes something the person already accepted take effect, as when an existing rule is moved to the point of action or given a check that runs, it is done and the person is told in a line (who does it, when, and its limit: The four questions, 1): asking again spends their attention on what they have already answered. A rule candidate that records a fact of the repository (a command, a path) and adds no obligation is rule upkeep and goes through `rulebook` unasked.

A rule written from a lesson carries the person's yes, quoted with its date, where the rule is written, so that a later session or a reviewer can tell a rule the person agreed to from one written unasked. The yes is the person's answer to the proposal as it was shown to them, or the person's own statement of the rule; a yes given to something else is not it.

## The four questions

Every proposal reaches the person already worked through these, in this order, so that what is proposed is of good quality from the start.

1. Why did it happen? The kind of cause decides the remedy, and who found the mistake (a reviewer, CI, the person) does not.
   - Did not know: state it where that role reads before that action.
   - Knew and did not apply it: no new rule. The session that settles makes the remedy in the same turn: it moves the existing rule to the point of action or gives it a check that runs, asks nothing, leaves no entry to wait for a second occurrence, and tells the person in a line. The remedy holds work to what the existing rule already says and no more: a check that would hold work to anything further, or a change to something that is not the person's to change (A repository several people work in; the repository's automation may not be theirs, When its leaving is decided), is a proposal and waits for the person's yes. Where the remedy cannot be made in the work in hand, the lesson waits as an entry that records the remedy to be made, unasked, by the next session that can make it; the person is asked only where the limit makes it a proposal.
   - The tool or process made it easy: the tool or process is put right.
   - The instruction was unclear or in conflict: that instruction is put right. A plan or a dispatch in hand is put right there, and the change noted in the plan's Decision Log.
   - What the owner wants was not known: ask, and keep the answer (An answer the owner gave for one case).
2. How far does it reach? As far as the incident and the person confirm, and no further. A wider reach that is plausible and unconfirmed is asked about and not assumed.
3. Where does it live? By whose fact it is, who reads it and who may change it: the rule file of the role that acts (the reviewer's for what a review should have caught, the Worker's for a check a Worker runs), a check that runs, a troubleshooting note under `docs/coding-agent/` for a failure with a repeatable symptom, cause and safe steps, or the machine's record. Then the existing-text check: read the target, quote its closest existing line, and state what the proposal adds. One that adds nothing is not made.
4. How is it worded? One sentence, a check at a named action, with what it is for and what would let it go.

The outcome goes on the entry's `Proposal:` line.

## Putting a proposal to the person

- Each proposal shows what would bind, stated briefly, where it would go, and the mistake it prevents.
- Lessons that share one cause reach the person as one decision, and not as one for each incident.
- The work does not wait for the answer; the lesson waits. The entry's `Waits for:` then says the person's answer and the date it was asked, so that a later session neither puts it again as new nor takes silence for a yes.
- Beside yes, four answers are offered, each carrying its reason so that nobody has to ask why:
  - it no longer holds, or is already said: the lesson leaves;
  - not yet: it waits;
  - it belongs elsewhere: it is sent there;
  - it is not worth it: it leaves, as a risk the person accepted.

## An answer the owner gave for one case

Something the owner wants, learned in one case, is kept as a lesson with its account, and may become a rule of the repository on the owner's word; it is not held back until a philosophy can hold it. The answer holds for the case it was given for. At the next case of the kind the session does not assume it: it asks, offering the earlier answer, and asks once whether it becomes a rule. Where value-level operation is on, it is also a candidate amendment in the closeout list for Counsel (`orchestration-harness/references/completion-closeout.md`).

## A log grown too large

The log is too large when a session, because of its length, searches it and does not read it whole.

- The person's work is not touched by the size of the log. Work they ask for starts at once and applies the lessons that bear on it; no settling stands between them and it.
- A session settles nothing on its own because of the size. The first session to search the log for its length raises the size once, as one line among what needs the person, saying how many decisions wait, and adds a dated line to the log's header saying that it was raised. A session that finds that line does not raise it again. The line is removed by a session that reads the log whole after entries have left it since the line's date, so that a log which grows too large again is raised again; a session that merely reads it whole leaves the line.
- When the person takes it up, at a moment of their choosing, the proposals come in the order of what a repeat would cost and how likely the situation is to come again, and each says why it is placed where it is, so that they can disagree with the order. They may stop after any number; the rest waits and nothing is lost.
- Lessons of which a repeat would cost little and which have not come up again are put to the person as one group, by their titles, for one answer.
- How much a lesson matters is judged from its own account: what the mistake cost when it happened, whether it has recurred, and how often that situation arises in the repository. It is a judgement shown with its reason and never a score.

## A repository several people work in

All of the above holds where the lessons are one person's to decide. In a repository several people work in, a session settles only entries from the work of the person it serves: it removes, proposes and raises the size for those and no others, because one person's yes cannot settle another contributor's entry. Whose work produced an entry is told from the log's version history, and an entry the session cannot place is treated as not the person's. Taking any entry into account while working is reading the repository, and is open to every session. Anything that would bind the others goes by whatever way that repository changes its rules. The rest of a shared log is left as it is.

## A defect of the harness

A lesson may show a defect of the harness itself: a bundled skill, reference, agent, validator or other plugin file. It is met in the repository being worked on, by whatever the four questions lead to. Bundled harness files are never edited, and no change to the harness is written up in the repository as though someone would act on it. Where the repository being worked on is the harness's own source, a defect of the harness is ordinary work on it.

## Older entries and headers

- An entry in an older form is read as it stands and counts as waiting. It is found by its heading, and gains the lines of the present form only when a session settles it or adds to it.
- Where the header of an existing log carries procedure that says otherwise, as one that tells sessions to promote lessons into rules, this handling governs. The header is not rewritten; the dated line on the log's size is an addition to it.
