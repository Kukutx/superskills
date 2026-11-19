---
name: idea-evaluation
description: Judge whether a project, product or research idea is worth doing by listing its assumptions, scoring risk and payoff, testing the riskiest first and planning pivots. Not for roadmaps or fact research.
---

# Idea Evaluation

## Use

Use when the question is which problem to work on, whether an idea is worth months of effort, why a project is stuck, or what to do after a setback: a side project, a product bet, a research or R&D direction, a thesis topic.

Ordering work on a goal already chosen belongs to `planning/project-planner`. Scoping a feature already decided belongs to `product/prd-builder`. Checking outside facts belongs to `research/research-brief`. Ranking items on an existing roadmap belongs to `product/roadmap-prioritization`.

## Domain inputs and blockers

The idea in one or two sentences: what will be done, how, and why it matters if it works. The user's field, strengths, resources, constraints and time horizon. With only the idea, list the assumptions and score them anyway, marking which scores are the assistant's guesses; the user corrects them.

How crowded the area is and what has already been tried are facts: they come from the user or from a source checked in the session, not from recall.

## Rules

1. **Choosing matters more than executing.** A mediocre problem executed well gives an incremental result, and people spend days choosing and years executing. Do not stop at the first idea: set three to five alternatives side by side, because comparing is what sharpens judgement.
2. **Look for the flaws first.** Treat a new idea as something about to take the user's time.
3. **Two axes**: the chance it works, and what it is worth if it does. Every change to the idea moves it along one of them. Low on both is dropped.
4. **List every assumption from start to finish**, in two kinds: facts about the world, which will not change as the project goes on, and assumptions about capability (technique, skill, resources), which may improve. Score each from 1 to 5 by the risk that it is false (1 almost certain to hold, 3 a coin toss, 5 very unlikely to hold), and write how many months pass before the answer is known. Score while trying to prove the idea wrong, and mark which assumptions depend on which.
5. **Warning signs**: a 4 or 5 that cannot be tested for more than about a year and a half; more than two or three assumptions at 4 or 5; high-risk assumptions chained one after another; doing the easy, safe parts first and postponing the risky test; no clear pass or fail criterion; "it will probably work" as the argument. A project that needs several miracles is rewritten or dropped.
6. **Good signs**: the riskiest assumption can be tested within about six months; more than one outcome counts as success; if one assumption fails another route remains; the risk is spread along the timeline instead of piled at the end.
7. **Five ways to cut a high risk**: test it earlier with something rough, a proxy or a simpler setting; run several candidates in parallel instead of betting on one; rewrite the question so the most fragile assumption disappears; move to a setting of similar value and lower technical risk; add a second method that checks the core assumption sooner.
8. **For the three riskiest assumptions, design a pass-or-fail test each**: the question, the most direct test even if crude, what result means go, what result means change course or stop, how long it takes and what it needs. The risky part does not go away by being left for later.
9. **A risk review ends in one of three ways**: reorder the plan by risk, rewrite the project, or choose another. "Too many miracles, choose another" is a useful result.
10. **Pick the yardstick by the kind of project.** Understanding something: how much is learned, and how general the thing studied is. Building a tool: how many will use it, and how critical it is to what they do. Solving a practical problem: how large the benefit, and for how many. One axis high is enough; both low to middling is a problem. A tool that few will use and nobody depends on is rarely worth building.
11. **The default outcome is that nobody cares**: a finding is ignored, a tool goes unused, a company closes. Say how this idea escapes that default.
12. **State the yardstick and agree it** with whoever will judge the work. Many disagreements are a tool judged as research, or research judged as a tool.
13. **Count the fixed parameters.** A project is defined by its subject, question, method, application, output, collaborators, time and resources. "Use X to do Y in Z" fixes three, and one failed assumption sinks everything; fixing none ("something with impact") paralyses. Fix one meaningful thing, at most two, and let the rest float. What to fix: what gives the fastest prototype, what the people around the user are unusually good at, what the user would do without being asked, or a real advantage such as rare access, an unusual mix of skills or data nobody else has.
14. **When a problem and a solution are both fixed**, check whether a technique is being forced onto an application. Release one, then the other, and compare the projects that result. For each fixed parameter write what is released if it fails.
15. **Idea traps**: letting "what I can do" choose the question instead of "what matters"; applying a familiar tool to yet another subject when the tool is already everywhere.
16. **Prompts for alternatives**: turn a one-off into something done systematically across a whole set; treat a tool's fundamental limit as the opening; "I cannot imagine a future without ____, and it does not exist yet"; turn a snapshot into a process over time; build the thing that answers many questions instead of one; ask why something that should exist does not.
17. **Separate doing from deciding.** Work day to day, and once a week step back for an hour or two and judge the work as if it were someone else's: what was learned, what comes next. When stuck, stop debugging, ask what has become possible that was not before, write three alternatives, and only then choose between persisting and switching.
18. **A project is a family of related projects.** List in advance what could go wrong, how likely, how damaging and when it would show. After a setback the aim is to repair and upgrade at once, for example from making one case work to making the method work for the whole class. After a major one, wait a couple of days before deciding.
19. **Pivots, by kind of obstacle**: an ordinary execution problem, release a fixed parameter; the original goal is out of reach, find a goal of comparable value that the work so far serves; data without a meaning, ask what interesting question it does answer. A new direction has to be more interesting, not merely feasible.

The month thresholds and the 1-to-5 scale are working conventions for comparing ideas, not measurements.

## Output

- The idea restated, with its kind and the yardstick used.
- Assumption table: `Assumption | World or capability | Risk 1–5 | Months to know | Depends on`.
- The verdict on risk: warning and good signs found, and which of the three endings applies.
- Pass-or-fail tests for the three riskiest assumptions.
- Fixed and floating parameters, with the alternative projects that open when each fixed one is released.
- What could go wrong and the pivot for each.
- When several ideas were compared, one table across them and a recommendation with its reason.

## Constraints

- A score is a judgement to be argued with, never a probability presented as measured.
- No claim about competitors, prior work or market size from memory.
- The decision to start, continue or stop is the user's; say which evidence would change the recommendation.
