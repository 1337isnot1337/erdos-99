# Target C: r=1 closure for the final k=4 p=3 profile

Date: 2026-09-27

Status: closes the `r=1` subcase of the remaining eight-no-root
`k=4,D=-1,d_root=0,p=3` three-singleton profile. Here `r` is the
number of projective weight-two lines in the rank-four coefficient space
`P<=Q^8`. This does not close Target C-II or Erdos Problem #99.

Companion verifier:
`research/verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_r1_closure_2026_09_27.py`

## Proof reduction

Current main gives
`rank(P)=4` and `(d1,d2,d3,d4)(P)>=(2,4,5,7)`, with exactly three
selected singleton blocks.

Assume `P` has exactly one projective weight-two line, with support `M`.
The committed sharp-puncture theorem gives, for every selected singleton
`b`,

`|I_b \ M| >= 2`

and `E_b not subset P+K_(M union {j})` for every `j notin M`.

A rank-two selected singleton cannot have exactly three touches. If its three
local direction multiplicities are `m0,m1,m2`, the selected constraint row
has weight `3-m_s>=2`. Each nonselected row represents the nonzero quotient
line `(E_b+P)/P`; weight one would violate a sharp puncture, so each also has
weight at least two. Hence all three multiplicities are one. The selected row
then has weight two and, because `r=1`, support exactly `M`. The remaining
touch is the only touch outside `M`, contradicting `|I_b\M|>=2`.
Therefore every rank-two selected singleton has at least four touches.

For a touched actual-empty block `a`, compatibility gives `E_a<=P`.
A rank-one empty block has at least two touches; if it has exactly two, its
touch set is `M`. A rank-two empty block has at least four touches by
`d2(P)>=4`.

There is at most one rank-one empty block with exactly two touches. Any such
block is touched by the same two external occurrences in `M`. If their
tetrahedral supports coincide, the local-block rule gives local rank two.
If the tetrahedral supports differ, they have at most one common triangle,
so they cannot support two distinct rank-one blocks with that same touch pair.

Let `h,e,c` count touched, actual-empty, and complete blocks. Then
`h=e+3+c`. Since `d_root=0`, complete rows are independent, and the
face-local capacity inequality gives `c<=11`, hence `e>=h-14`.

The three selected singletons contribute at least six incidences. If `e>0`,
the empty blocks contribute at least `3e-1`, and complete touched blocks
contribute at least `c`. Since the eight no-root four-cycles contribute
exactly 32 incidences,

`32 >= (3e-1)+6+c = h+2e+2 >= 3h-26`.

Thus `h<=19`. If `e=0`, then already `h<=14`.

## Exact certificate

The verifier enumerates all 27,763 `S_7` orbits of multisets of eight
tetrahedral four-supports. Exactly 9,444 have at most 19 touched triangle
blocks. For each, it checks all 28 possible supports `M`, for 264,432
support-orbit/pair tests.

It deliberately enlarges the state space: every individually eligible block
is made virtually empty. For each possible singleton triple it checks only
necessary complete-row independence, face-local capacity, coefficient
dimension at least four, and generator support at least seven coordinates.
Every actual `r=1` state would therefore survive.

The exact census is:

```text
range          h<=19    pair tests    survivors
0:5000          3924      109872          0
5000:10000      1642       45976          0
10000:15000     1586       44408          0
15000:20000      781       21868          0
20000:25000     1065       29820          0
25000:27763      446       12488          0
total           9444      264432          0
```

Triangle-row ranks are exact over `Q`: the verifier checks that
`2^31-1` is prime by Lucas-Lehmer and that
`(2^31-1)^2 > 3^15`, so Hadamard's inequality rules out rank loss modulo
the chosen prime.

Therefore the `r=1` subcase is empty. On current main, the remaining split
`r=0,1,2,4` is reduced to `r=0,2,4`.
