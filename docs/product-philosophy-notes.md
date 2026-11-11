# Notes: the product philosophy's discussion

Unratified. Counsel's notes for the discussion of a product philosophy for this repository. No philosophy is drafted. Product values are ebigunso's to state: he owns the harness. Counsel originates a statement here only as a proposal to him. No entry is grounds for a plan or a grade, and none is his answer; his words are quoted so that a later Counsel session can continue from them.

## How it opened, 2026-11-11

- While looking for what underlies the engineering philosophy he separated two things: "how repository content quality is held, which should go to the engineering philosophy, and how the harness should assume lazy humans as the default and aim to reduce human churn where possible, which probably is more of a product philosophy line."
- Asked whether to draw out a product philosophy from that line: "Yes, if that is the right shape then lets draft the product philosophy as well."

## What he has already said about what the harness is for

Collected from his words in this and earlier discussions, each already recorded in a brief or its notes. None was said as a statement of product philosophy; each is evidence for the discussion.

- "We shouldn't assume everyone would know the difference between the two roles enough to make an informed decision, and you shouldn't underestimate how lazy humans are." (2026-11-11, on Counsel as the default role for everyone)
- "The pain is the wait before a brief starts." (2026-11-11)
- Questions are "raised only when any accessible information source does not settle the question". (2026-11-11)
- "if a finding can be remediated without any additional decisions, I'd like it automatically handled as well." (2026-11-07)
- Of a full plan-and-build suite run for a very small change: "it seems a bit overkill too." (2026-10-06)
- "An agent harness runs on a capable agentic model, not an inert code after all." (2026-10-29)
- "there's only one person at the helm at a given time". (2026-11-11)
- A brief he ratified: someone who sets up the harness in a new repository and says nothing about models has fitting dispatches at once. (2026-10-29)
- A brief he ratified: under a ratified brief the Orchestrator session asks the person nothing; the run goes on without them while they talk with Counsel and judge what is built. (2026-10-29)
- His standing rules: only direction-level decisions reach him; merges, decision records, changes to a philosophy, and anything irreversible or outward-facing are his.

## Counsel's restatement, its own, put to him 2026-11-11

A person says what they want and judges what they get. The harness does everything between, asks them only what only they can answer, and never decides what is theirs.

## Questions put to him

- Who he pictures: himself, or someone who installs it knowing nothing about roles, models or the harness.
- The failure that counts whatever else is right.

## His answers, 2026-11-11

- On who he pictures: "The latter. Optimizing for someone who doesn't know the mechanics, also makes me free from unnecessary decisions that could be cut, so it's a win-win for the most part. Tuning on the finer details could be available, but as overrides to defaults, which would happen either if I explicitly direct that, or be proposed from the agent and set either automatically or by user choice, depending on the impact of that decision."
- On the failure that counts: "\"It builds the wrong thing confidently\" is what should be avoided. \"It spends your attention on something it could have settled\" comes second, and \"The harness decides something that was yours to decide\" comes third but this one isn't as strong as the other two."

Counsel's reading, its own:

- The person pictured does not know the mechanics. Everything works on defaults; a finer setting is an override, made on the person's explicit direction or proposed by the agent, and whether a proposed one is set automatically or put to the person depends on its impact.
- The order of failures: building the wrong thing confidently, then spending the person's attention on what could have been settled, then deciding what was the person's, the last weaker than the other two.
- Insight offered: the order explains most of what the harness already is. It spends agents' effort freely (drawing out intent, review, an independent audit) to guard the first without paying the second.
- Candidates carried over from the engineering philosophy's first draft, where they did not belong: no party judges its own work; a failure should show; the person is asked only what only they can answer, and what goes ahead unasked is reported; ceremony is sized to the change.
- Questions put to him next: whether what sorts a decision is its impact and whether it can be undone, not whose it is; and where cost and waiting sit beside the three failures.

## His answers on the line and on cost and waiting, and the first draft, 2026-11-11

- On whether impact sorts a decision: "Yes, the first case is acceptable while the second is not." (The first case: a default he would have chosen differently, told afterwards, easily changed. The second: something that cannot be undone or reaches outside, done without asking.)
- On cost and waiting: "Reducing waits and maximizing parallelism is aimed for a productivity gain, a performance upgrade to the harness as it stands, rather than something to be in the core philosophy. Cost on the other hand, it is best handled automatically but when it goes wrong the disappointment is quite large so it should be carefully tuned."
- Decision, Counsel's: a first draft is written at `docs/product-philosophy.md` with a companion beside it. Unratified; no pointer line names it. It does not refer to the engineering philosophy.
- Gap check against the philosophy reference, read after the draft: Counsel finds every item covered. His to confirm.
- Departure from the conventional answer, for him to see before ratifying: the convention for agent tools ranks acting without permission as the first failure and asks for confirmation at each step; this philosophy ranks it last of three and has the harness decide and tell, keeping the person's yes for what cannot be undone or reaches outside. A second: the convention offers the machinery as control; this hides it behind defaults.
- Not recorded in the draft: waiting and parallelism, at his word; the candidate "a failure should show", which Counsel judged to be about how the harness is built and left for a decision record.

## His reading of the shorter draft, 2026-11-11

- Fact: the draft was rewritten shorter the same day, in Counsel's wording, after his correction that Counsel was quoting him too literally (recorded in the engineering philosophy's notes). It lost its sections on overrides, on how it behaves and on success one could watch for.
- His words on it: "The first paragraph in section 2 of the product philosophy lists how the harness behaves, which reads as pinning that behavior. I'd like you to assess if those really would survive in the long run, and leave only those you see fit, and make sure to have it read as an example not pinning. \"As an example...\" could be one way to put it."
- Counsel's assessment, its own, of the three behaviours that paragraph listed:
  1. Saying outright what was not done or not checked: kept as a principle. It is the direct opposite of "confidently" and holds whatever the means.
  2. Learning what is meant in terms the person can judge: the principle is kept, that what is meant is established in terms the person can judge. That it is learned by asking before building is not kept as a principle: showing something cheap and letting the person judge it may replace asking. The question put as an experience is now an example.
  3. Having the result judged by someone other than its builder: the principle kept is that confidence is never taken on the builder's word. A second agent as the judge is a means, and is now an example; a decision record holds it.
- Also changed on the same ground, in section 5: "Not its own judge" no longer names a second agent.
- The sentence "Everything the harness does before and after building exists to prevent it" is removed as an overclaim.

- His words on section 4, 2026-11-11: "Cost should be clarified so that it is unmistakably about monetary costs not time." The section is retitled "What it costs in money" and says it is about money only, with time left to the part on what is left out.

## Open

- His answers. Where the philosophy will live; no pointer line exists.
