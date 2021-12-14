Extended Polymerization
=======================

https://adventofcode.com/2021/day/14

Part one was solved with brute force. It could obviously be reimplemented without brute force using the same part two
solution, just changing the number of steps, but brute force is kept here for whatever referrence :D

Part two finally takes quite its time using brute force and the reality is that we really don't care about the actual
string at all, we only care about character occurrences. Bottom line the counting was changed to actually maintain the
counts for individual characters and distinct pairs at each step. Note that at each step we must reconsider all of our
pair counts as new pairs are formed at each step and old pairs should no longer be considered.
