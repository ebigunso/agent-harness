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

# ADR-D (not yet numbered): Nothing waits for the person directing the work without their knowing it is there: when they are not in a discussion, the last thing Counsel wrote lists everything that needs them

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. Something needs that person when it waits on that person's word or judgement.

Nothing that needs the person directing the work is to be missed, and what can wait for them waits (`ADR-D-when-the-person-is-told-follows-what-waiting-costs.md`). Things come to need that person while they are away: a Counsel session may be left unattended through a long run, Counsel cannot know whether it is being watched, and what that person sees on coming back is the last thing written, with everything before it buried in text they did not follow. A line written at the moment a thing arises is buried by what follows it. Keeping things until that person asks leaves them not knowing that anything waits. The fork is how that person comes to know what waits for them.

## Decision

- Nothing is held without the person directing the work knowing it is there.
- When that person is not in a discussion, the last thing Counsel wrote carries a short list of everything that needs them, each item brief.
- A matter stays with Counsel until it is closed.

## Why

By the product philosophy's "The line" a thing held for someone and never mentioned leaves them unable to act on it. Since Counsel cannot know whether it is being watched, what needs that person is where they will look on coming back, short enough to read whole.

## Rejected Alternatives

- Each thing is told as a line at the moment it is ready and then waits: it lost because a line written while nobody is watching is buried by what follows it; reopen if a supported runtime lets Counsel know whether that person is watching.
- Matters are held until that person asks what is waiting: it lost because a person who does not know something waits cannot choose to take it up; rejected outright.

## Decision Boundary

Not covered: the wording and length of the list and of an item; what is brought at once and does not wait (`ADR-D-when-the-person-is-told-follows-what-waiting-costs.md`); that the list carries no account of the work (`ADR-D-only-what-needs-the-person-reaches-them.md`); which item Counsel would settle first, and who chooses (`ADR-D-the-order-in-which-matters-are-taken-up-is-the-persons-to-choose.md`); how Counsel keeps what needs that person apart from the runs' reports; how that person's answer travels back (ADR-D-0038).

## Validation

The decision is broken where that person comes back from being away and the last thing Counsel wrote does not say everything that needs them; where something is held and that person does not know it is there; or where a matter that was not closed is no longer with Counsel.

## Revisit When

- The premise that Counsel cannot know whether that person is watching no longer holds: a supported runtime lets Counsel know it, and where that person will look is then known and not assumed.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him", "Runs side by side", "Directed during the run" and "Core scenarios". Related: ADR-D-0034 (Counsel), ADR-D-0062 (everything that needs that person reaches them through Counsel).
