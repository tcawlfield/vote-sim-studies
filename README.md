# vote-sim-studies
Studies of voting simulations

This is a blog and collection of notebooks, ideas, and insights from
[my voting simulation](https://github.com/tcawlfield/vote-sim).

## Ideas for future work

### Collective stupidity vs collective intelligence

I consider a voting method to be good when it consistently picks candidates
with the highest *perceived* utility. Can I simulate an "actual" utility
and introduce errors and/or biases to voters and/or voter groups? Can any
voting method do better than just maximizing perceived utility? This
question is not yet well-formed.

Still, maybe add a new issue: virtue. Do voter groups with errors/biases and their own
sensitivities to certain issues tend to elect candidates with fewer or smaller
virtues? That's the rough idea anyway.

### Condorcet Methods

For multi-dimensional issue space, I keep finding that 0.7% (+/- 0.1%) of
simulated elections have a Smith set >= 3 candidates. What considerations
can I pick that decreases or increases this fraction?

If I only examine such elections, which Condorcet methods result in
candidates with higher net utilities? Which ones tend to elect centrists
(when issues are a consideration or maybe virtues).

### Multi-voting

#### Reweighted range voting with cycles and hopeful convergence

RRV seems to give me results that are too clumpy. Perhaps a new algoritmn
might help that elects the first winner, second, and so on for round one.
Then loop through the ring of winners. The first-elected winner can be removed
from the set, weights updated, and a replacement re-elected. Then the next
winner. Continue to do this until you reach a point that after N replacements
the set of winners has not changed.

I need to think harder about this for a more robust and precise stopping
condition. Seems like an obvious enough idea, I'm sure someone has
published on this topic.

#### How to assess the utility (yeah, perceived) of multiple winners?

How well do the elected candidates collectively represent the electorate?
I'm thinking in political terms, but that's a mistake. Do we look at the
utilities, summed over each voter, of the candidate with maximum utility
for that voter? That's one possibility but it does not reward proportional
representation, where a large group of voters have similar assessments
of the candidates, and would be better served by multiple winners.
Perhpas better to sum with a decreasing weight factor as you add in candidates
that are less preferred for each given voter?

I need to do research on what has already been published.

### The Mutual-Majority criteria

How often is there a mutual majority of more than one candidate but less than all
the candidates? In these cases, how often do various methods elect a candidate
who is not in the mutual-majority-supported set?

## Random thoughts

### Perception versus reality

First thought: A voting method attempts to capture the collective will of the people.
It is not the role of a voting method to address the difference between perceived utility
and actual utility that a canditate may provide to a voter.

Second thought: It has been observed that some collective activities
result in "collective intelligence." But other activities can produce collective stupidity.
A good voting method ought to result in collective intelligence.
So it may be possible for a voting method to help maximize *actual utility* even while
individual ballots can only be based on percieved utility. This should only be possible
if perceived utility, on average, has a positive correlation with actual utility.
This can be modelled in a simulation, provided there is some distinction made
between (simulated) actual utility and perceived, which would be affected by biases.

### Ideal virtues of voting methods

* Net utility of the winning candidate should be close to that of the ideal candidate
  * Compare average VSE, worst-case, and fraction of elections that yield the ideal
* Ballots are expressive
* It is obvious and natural how to best fill out your ballot
  * It should not be tedious or require too much specificity
* Various criteria should be satisfied more often than not
* The method should be relatively easy to explain
* Honest voting should be nearly as effective as any kind of strategic voting
* Votes can be tabulated within precincts in a generally compact way.
  * For each method, this compactness is a function of the number of candidates
    and, for score-based systems, the number of scale degrees.
  * This can help for auditing purposes
