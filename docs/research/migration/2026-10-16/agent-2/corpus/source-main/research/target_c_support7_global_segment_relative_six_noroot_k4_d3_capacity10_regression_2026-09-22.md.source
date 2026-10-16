# Six-row capacity-ten regression and its failed clean lift

Date: 2026-09-22

Claim classification: **regression**. This is an exact six-row cycle-space
configuration. It is not an eight-row Profile B source, a planar configuration,
or a global minimum-diameter example.

The claim that a synchronized rank-two six-row state with virtual deficiency
three and full singleton-functional quotient rank seven has capacity at most
eight is false. Requiring every five-row child to have full singleton-functional
span does not repair that claim.

The explicit example below has capacity ten and satisfies all those child
conditions. It even realizes nine actual singleton replacements with exact
defect three. However, it admits no qualifying clean one-row lift, so it does
not extend to the remaining eight-row Profile B source.

Companion exact verifier:

`research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d3_capacity10_regression_2026_09_22.py`

## The six-row example

Use the existing global four-cycle indices

```text
E = (106,109,112,115,105,107)
```

Their cyclic vertex descriptors are

```text
(1,2,4,3), (1,2,5,3), (1,2,6,3),
(1,2,7,3), (1,2,3,4), (1,3,2,4).
```

Take the rank-two coefficient space with row basis

```text
(1,1,1,1,0,1),
(0,0,0,0,1,1).
```

Every one-coordinate puncture preserves rank two. The virtual complete set is

```text
C = (1,2,3,4,5,6,7,8,15,16,17,18).
```

It consists of the twelve triples having exactly two vertices in `{1,2,3}` and
one vertex in `{4,5,6,7}`. The only touched virtual-empty block is block zero,
the triple `{1,2,3}`. Its rank-two empty constraint is exactly the coefficient
space displayed above.

The complete relation rows have rational rank nine, so their deficiency is
`12-9=3`. The canonical relation parameter space has dimension `12+4=16`.
The compatible singleton blocks and their unique state masks are

```text
(2,1), (3,1), (4,1), (6,1), (7,1), (8,1),
(15,2), (16,2), (17,2), (18,2).
```

The canonical relation columns have rational rank nine. Adjoining all ten
singleton functionals raises their rank to sixteen. Thus the functional extra
rank is seven, filling the quotient.

In deletion order `0,...,5`, the five-row child profiles
`(virtual deficiency, singleton capacity, functional extra rank)` are

```text
(3,10,6), (2,7,5), (2,7,5),
(2,7,5),  (3,12,6), (3,12,6).
```

Every child fills its quotient of dimension `3+d`.

## Actual nine-singleton realizations

This is not only a test of the enlarged compatible-singleton list. Select nine
of the ten compatible blocks by omitting any one of

```text
2,3,4,6,7,8.
```

Replace those nine virtual-complete blocks by their unique compatible singleton
states, retain the other three complete blocks, and keep block zero empty.
There are exactly six such nine-block choices with functional extra rank seven.
The actual coefficient space remains the displayed rank-two plane because the
empty block zero already generates it.

For each choice, exact rational ranks of the actual selected rows give

```text
number of rows = 24,
r_M = 24,
r_Q = 17,
delta = 7,
D = 24-3*7 = 3,
root-only deficiency = 0.
```

Consequently neither capacity at least nine nor the existence of an actual
nine-singleton six-row state excludes this seed.

## No clean one-row lift

An eight-row Profile B source with minimum coefficient support at least four
would give, after deleting either of its two restored rows, a seven-row lift
with minimum coefficient support at least three, virtual deficiency three,
and full singleton-functional extra rank eight.

The verifier enumerates every realizable rank-two coefficient-space lift for
each of the 99 unused no-root rows. It uses the established local-constraint
basis cover: one rank-two local constraint, or two rank-one constraints on
different blocks. This produces the exact census

```text
unused external rows                         99
realizable rank-two lift planes             123
planes with minimum coefficient support >=3  18
among those, virtual deficiency 3               6
profile of all six surviving lifts: capacity 6, extra rank 4
```

Thus no seven-row lift has the required extra rank eight. This excludes every
two-row Profile B lift of this particular seed without enumerating pairs of
restored rows. It does not exclude other six-row seeds.

All rank decisions in the companion verifier use rational arithmetic. It
generates no five-row or six-row orbit cover. The full verifier, including the
actual-state ranks and the 99-row lift scan, passed locally.