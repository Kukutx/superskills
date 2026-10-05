# Design smells baseline

Use when a review reaches design quality and the repository documents no standard of its own for it. Each entry is a labelled judgement call ("possible Feature Envy"), never a hard violation: a documented repository standard overrides it, and anything tooling already enforces is left to the tooling.

Match each against the diff, name it and quote the hunk:

| Smell | What it is | Usual fix |
| --- | --- | --- |
| Mysterious Name | a function, variable or type whose name does not say what it does or holds | rename it; when no honest name comes, the design is unclear |
| Duplicated Code | the same logic shape in more than one hunk or file of the change | extract the shared shape and call it from both |
| Feature Envy | a method that reaches into another object's data more than its own | move the method to the data it uses |
| Data Clumps | the same few fields or parameters travelling together | bundle them into one type |
| Primitive Obsession | a primitive or string standing in for a domain concept | give the concept its own small type |
| Repeated Switches | the same switch or if-cascade on the same type recurring across the change | one shared map, or polymorphism |
| Shotgun Surgery | one logical change forcing scattered edits across many files | gather what changes together into one module |
| Divergent Change | one module edited for several unrelated reasons | split it so each part changes for one reason |
| Speculative Generality | abstraction, parameters or hooks for needs nobody has | delete it and inline until a real need appears |
| Message Chains | long `a.b().c().d()` navigation the caller should not depend on | hide the walk behind one method |
| Middle Man | a class or function that mostly delegates onward | remove it and call the real target |
| Refused Bequest | a subclass or implementer that ignores most of what it inherits | drop the inheritance and compose |
