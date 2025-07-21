---
date: '2025-07-07T22:22:28-07:00'
draft: false
title: 'What is the center-squeeze effect?'
description: "Looking at simple voting simulations that illustrate center-squeeze"
cascade:
  featured_image: '/images/independent_candidates.png'
---

There are a lot of complex and controversial discussions surrounding voting
methods. Here, I try to short-circuit almost all the complexity and introduce a
simplified scenario. Although unrealistic, these reveal what I think is an
important feature of voting methods.

# A Very Simple Scenario

You're on a school basketball team, visiting out-of-state. You won your last
game, but won’t be returning home until tomorrow. There’s time to catch a movie!
Five movies are showing at a local theater. Some of your teammates want to see
something dramatic, while others want something lighter and comedic. Others
prefer something in between – enough drama to make you invested, but some humor
as well. The coach insists that everyone goes to the same movie, in the name of
team-building. They pass out ballots…

You’re managing a team in a small office building. There’s one thermostat, but
some argument about the ideal temperature. You list a series of temperature
settings on a ballot, and pass them out…

You’re the owner of a successful and independent breakfast diner. You have two
coffee options: regular and decaf. But some customers want a bold, strong,
almost bitter brew, while others want a light and smooth, almost watery cup.
Many want something in between. For a couple weeks, you offer a “flight” of
coffees with different beans but, most importantly, different strength. The
flights come with a questionnaire. Given the results, how do you pick one option
(for the regular brew) that makes your customers the happiest?

In real situations, it’s rare to have only one aspect or consideration that
differentiates multiple options, but here we explore an abstract version of this
kind of scenario. Not because it’s realistic, but because it’s tractable. We can
easily reason about what the best outcome should be.

# The Best Outcome

In this type of situation, the best outcome of a *single-winner* election is to
elect that candidate **closest to the middle** of the range. Note the emphasis
on "single-winner" election. Sure, if you could have two winners, one would
ideally be somewhere near one side, and the other on the opposite side. That's
complicated. One winner makes it simple. The best-representative choice will
always be the one nearest the center.

  Mathy lingo:
  
  I'm also assuming two simplifying conditions here. (1) There are a very large
  number of voters, and (2) the distribution of preference among voters is
  symmetric "left" to "right." With these conditions met, the mean of the voter
  preferences is very nearly equal to the median. (We'll come back to that
  later.) That candidate closest to the mean or median voter is the *ideal*
  candidate.

So again: The ideal candidate is the one closest to the middle. I can write
that, but can I justify it? Although I think it's obvious, to be perfectly
honest with you, I haven't found an iron-clad justification. I feel that there
should be a symmetry argument that proves this, but I cannot find it yet. It's
certainly true that when there are **two** candidates, all voting methods agree
(the whole subject of what method you use becomes uninteresting), and they all
do elect that candidate nearest the middle. But in general? If you can think of
a good reason why I'm either right or wrong here, I'd love to hear it!

# Two Candidates

Today, you'll see a lot of histograms, without
[explanation](https://en.wikipedia.org/wiki/Histogram) or apology.

When there are two candidates, all the voting methods that I'll present here
will elect the same candidate in every simulated election. It doesn't even
matter how many issues or other kinds of considerations I simulate. All voting
methods are basically the same when there are two candidates. That's probably
worth writing more about, but there isn't time here.

![oneissue_twocand.png](One issue, two candidates, histograms only)

Above I show the distribution (by histogram) of the candidates, as well as the
distribution of the "issue" of the winning candidate. These are the results of
2,000,000 simulated elections, each with two candidates and 100,000 voters.

Two details are worth digging into here...

## Why the Pyramid shape?

Consider one of the candidates: Candidate A. If A is the closest to the middle,
then the other candidate, B, is farther from the middle. If A's position is $x$,
then the probability that B is farther from the center (zero) than A is $(1-|x|)$.
That's the crux of it.

## What's the "Max Utility" Candidate?

My candidates and voters all have a preference drawn randomly and uniformly
between -1 and 1. Overlapping on this plot is also the distribution of the
candidate that has the highest "perceived utility", summed over all voters. The

### Perceived Utility

To simulate elections, I create a table of perceived utilities for each voter-candidate
pair. In the case of a single-issue election, a voter's perceived utility for a given candidate
is a simple function of their preference and the candidate's apparent preference, $p_{v,i}$ and $p_{c,j}$.

\[
\begin{aligned}
U(i, j) = -\left|p_{v,i} - p_{c,j}\right|
\end{aligned}
\]

It's easy enough to verify that in the case of a uniform distribution of voter
positions, total candidate utility maximizes at the mean voter position, as long
as all voters' utility functions are monotonically-decreasing functions of
distance only.

# More than Two Candidates

