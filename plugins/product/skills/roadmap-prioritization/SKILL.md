---
name: roadmap-prioritization
description: Prioritize features and initiatives with RICE or value versus effort, build a Now/Next/Later roadmap and reshuffle it when capacity changes. Use for what to build next, not a project schedule.
---

# Roadmap Prioritization

## Use

Use when the question is which product work comes first and how to show it: ranking a backlog of ideas, building a roadmap, adding an initiative and deciding what moves, or explaining a change of plan.

A dated plan across workstreams with dependencies belongs to `planning/project-planner`. Specifying one feature belongs to `product/prd-builder`. Ranking technical debt belongs to `development/tech-debt-triage`.

## Domain inputs and blockers

The list of candidates, what each is for, a rough effort, and the capacity available. For a change to an existing roadmap: the current roadmap in any form, and what happened that prompts the change. Reach and impact estimates come from the user's data where it exists; where they are guesses, the confidence factor says so.

## Scoring

**RICE** = (reach × impact × confidence) ÷ effort.

- Reach: people or accounts affected in a fixed period.
- Impact: 3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal.
- Confidence: 100% with data, 80% with some evidence, 50% for a guess.
- Effort: person-months.

Alternatives when RICE is more precision than the inputs deserve: value against effort in a two-by-two (quick wins, big bets, fill-ins, money pits), or must / should / could / won't, where "won't" is written down so it stops coming back.

A score ranks; it does not decide. Strategy, a commitment already made, or a dependency can override it, and the override is stated.

## Capacity

- Adding something means asking what comes off. Capacity that is short is solved by cutting scope, not by assuming people will do more.
- A healthy default split is about 70% planned features, 20% technical health, 10% buffer. New products lean to features; mature ones, and any product after an incident, lean to health.
- A sprint or cycle is planned to 70% to 80% of nominal capacity, because interruptions always come. Within it, mark what must ship, what should, and what is a stretch, and decide in advance what is cut if time runs short.

## Roadmap shape

- **Now**: committed, high confidence.
- **Next**: one to three months out; scope understood, timing loose.
- **Later**: directional.

A roadmap communicates themes and outcomes, not tasks. A timeline with dates suits internal execution; shown outside, it reads as a promise and creates false precision.

Dependencies each get an owner and a date by which they are needed, with buffer around the riskiest. Cross-team ones are raised early.

## Changing the roadmap

Communicate a change in five steps: acknowledge it, explain why, show the trade-off, show the new plan, and acknowledge who is affected — telling directly the people whose expectations are being lowered.

Avoid churn: batch changes monthly or quarterly, set a threshold for what justifies a change, and separate a change of roadmap from an adjustment of scope. A roadmap that changes constantly points to an unclear strategy, not to agility.

## Output

Status overview; items grouped by Now, Next and Later, each with a one-line description, status (not started, on track, at risk, blocked, done), target period, owner and key dependency; risks and dependencies; and what changed in this update with the before and after. For a ranking, the scoring table with the inputs shown.

## Constraints

- Do not invent reach or impact numbers; a guess is entered as a guess at 50% confidence.
- Do not put dates on Later items.
- Do not hide a cut item; say what was dropped and why.
