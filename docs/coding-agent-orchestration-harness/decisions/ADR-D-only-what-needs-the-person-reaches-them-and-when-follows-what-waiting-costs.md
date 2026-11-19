---
status: proposed
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): Only what needs the person directing the work reaches that person, ready to decide; when it is told follows what waiting costs, and that person takes matters up one at a time in the order they choose

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief. Something needs that person when it waits on that person's word or judgement.

The attention of the person directing the work is to go only to what needs them, at their own pace, and nothing that needs them is to be missed. Several things can come to need that person while they are discussing something else, or while they are away: a Counsel session may be left unattended through a long run, Counsel cannot know whether it is being watched, and what that person sees on coming back is the last thing written, with everything before it buried in text they did not follow. Each simple way of telling fails that. Telling each thing at the moment it arises breaks into a discussion at the pace of the runs, and when nobody is watching the telling is buried by what follows. Keeping things until that person asks leaves them not knowing that anything waits. Writing out a whole account of where the work stands whenever that person may be away spends their reading on what does not need them. Putting several matters to that person in one message takes from them the choice of which to take up. The fork is when something that needs that person is told, in what form, and who chooses the order.

## Decision

- Only what needs the person directing the work reaches that person, and it arrives ready to decide.
- When that person is told follows what waiting costs: what is being lost is brought at once, by whatever reaches that person, and the rest waits.
- When that person is not in a discussion, the last thing Counsel wrote carries a short list of everything that needs them, each item brief, with the one Counsel would settle first. The matter itself is put to that person when they take it up, and no account of what was done or is going on is written out for them.
- In a discussion Counsel does not break in for what can wait, and matters are taken one at a time.
- Counsel recommends the order and that person chooses it, at their own pace.
- Nothing is held without that person knowing it is there, and a matter stays with Counsel until it is closed.

## Why

That person's attention is the scarce thing in the product philosophy's "What goes wrong, in order", so it is spent by what waiting would cost and not by the pace of the runs; and by "The line" a thing held for someone and never mentioned leaves them unable to act on it. Since Counsel cannot know whether it is being watched, what needs that person is where they will look on coming back, short enough to read whole, and the order stays with the one person who can weigh the matters against each other.

## Rejected Alternatives

- Each thing is told as a line at the moment it is ready and then waits: it lost because a line written while nobody is watching is buried by what follows it; reopen if a supported runtime lets Counsel know whether that person is watching.
- The whole account of where the work stands is the last thing written whenever that person may be away: it lost because it spends that person's reading, and Counsel's context, on what does not need them; reopen if that person is found asking for the account each time they come back.
- Each matter is put to that person in full as soon as it is ready: it lost because that person is made to switch tasks at the pace of the runs and not at their own; reopen if matters that waited are found to have held up work longer than that person would have chosen.
- Matters are held until that person asks what is waiting: it lost because a person who does not know something waits cannot choose to take it up; rejected outright.
- Counsel sets the order and puts the matters to that person one after another: it lost because the order weighs what that person cares about, which is theirs to weigh; reopen if that person is found to take Counsel's recommended order every time and to want it without being asked.

## Decision Boundary

Not covered: the wording and length of the list and of an item; by what means something that is being lost is brought to that person; how Counsel keeps what needs that person apart from the runs' reports; that Counsel can say where every brief stands when asked, which the brief states; what may be brought to that person at all, and at what level (ADR-D-0059, ADR-D-0062); how a question is framed when that person takes it up (ADR-D-0046, ADR-D-0059); a matter Counsel judges severe enough to pause part of the work, which is raised as its own record states (ADR-D-0044); how that person's answer travels back (ADR-D-0038); how promptly Counsel answers while runs are starting and reporting.

## Validation

The decision is broken where something that does not need the person directing the work is brought to them, or an account of what was done is written out for them unasked; where something that was being lost waited; where that person comes back from being away and the last thing Counsel wrote does not say everything that needs them; where a discussion is broken into for what could wait, or several matters are put to that person at once; where Counsel fixes the order in which that person takes matters up; or where something is held and that person does not know it is there.

## Revisit When

- The premise that a short list is enough for that person to choose what to take up fails. Nothing had exercised it with several runs on 2026-11-19; matters taken up in an order that person says they would not have chosen had they known more reopens what an item carries, not the decision.
- The premise that Counsel can tell what is being lost from what can wait fails: something that waited is found to have cost what bringing it at once would have saved, or that person is found interrupted for what could have waited.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him", "Directed during the run" and "Core scenarios". Related: ADR-D-0034 (Counsel), ADR-D-0044 (Counsel's pause), ADR-D-0059 (which questions reach that person), ADR-D-0062 (everything that needs that person reaches them through Counsel).
