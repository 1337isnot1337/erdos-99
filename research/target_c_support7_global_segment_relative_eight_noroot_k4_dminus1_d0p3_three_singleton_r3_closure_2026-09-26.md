<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f78c06c996538df645802743a1532d65d759a182", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_r3_closure_2026-09-26.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8e265a76e39c4e0920163234c076e21801a9fe887302317a55a52126ec1dcc96"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the three-weight-two-line subcase of the final k=4 p=3 profile

Date: 2026-09-26

Status: proof-level reduction plus exact finite support certificate. This closes only the
`r=3` subcase of the remaining eight-no-root
`k=4,D=-1,d_root=0,p=3` three-singleton profile, where `r` is the number of
projective weight-two lines in the rank-four coefficient space `P<=Q^8`.
It does not close the whole three-singleton profile, Target C-II, or Erdos
Problem #99.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_r3_closure_2026_09_26.py`

## 1. Inputs from current main

Current main gives `rank(P)=4` and
`(d1,d2,d3,d4)(P)>=(2,4,5,7)`, and proves that the remaining `p=3`
root profile consists of exactly three singleton blocks. If a weight-two line
of `P` has support `M`, then for every coordinate `j notin M`, deleting
`M union {j}` gives a sharp five-row `D=2,k=2,p=3` descendant.
Consequently every selected singleton block `b` satisfies
`E_b not subset P + K_(M union {j})` for every such `j`, and is still
touched after every one of those deletions. Distinct weight-two lines have
disjoint supports.

Assume now that `P` has exactly three projective weight-two lines. Write their
disjoint supports as `M1,M2,M3`, and let `U` be the unmatched pair of external
coordinates.

## 2. Unmatched-pair localization

Fix a selected singleton block `b`. Current main gives
`W_b=(E_b+P)/P` one nonzero quotient line.

Take any nonzero representative `w` of `W_b`. A weight-one representative is
impossible: if its coordinate lies in some `Mi`, then it belongs to
`K_Mi`; if it lies in `U`, choose any `Mi` and take `j` equal to that coordinate.
Either way `w in P+K_(Mi union {j})`, contradicting sharpness.

Now suppose `w` has weight two. If its support meets one of the matched pairs
`Mi`, then its two-coordinate support is contained in `Mi union {j}` for some
`j notin Mi` (or is contained in `Mi` itself). Sharpness again gives a
contradiction. Therefore `support(w)=U`.

Hence every quotient representative has weight at least three, except that a
weight-two representative is allowed only on the unique unmatched pair `U`.

## 3. Rank-two three-touch singletons are impossible

Suppose a selected singleton block has `rank(E_b)=2` and exactly three touches.
The local two-space has the three projective directions. Let their touch
multiplicities be `m0,m1,m2`, and let direction `s` be selected by the singleton
row.

The singleton constraint line `L_b=E_b intersect P` has support size
`3-m_s`. Since `d1(P)>=2`, this is at least two. For either nonselected local
direction `j`, the corresponding local coefficient row represents the nonzero
quotient line `W_b`, so its support size `3-m_j` is also at least two by the
preceding localization. Thus every `m_i<=1`, and therefore
`(m0,m1,m2)=(1,1,1)`.

The two nonselected-direction quotient rows then have two different
weight-two supports. Their union is the three-touch set. But every weight-two
quotient representative must have the same support `U`. Contradiction.

Therefore every rank-two selected singleton has at least four touches.

## 4. At most one two-touch rank-one singleton

If `rank(E_b)=1`, the unique nonzero local row itself represents `W_b`. A
two-touch rank-one singleton therefore has touch support exactly `U` by the
localization lemma.

There cannot be two distinct such singleton blocks. If the two external cycles
in `U` had the same tetrahedral four-support, the committed local-block rule
would make every common touched block rank two, not rank one. Thus the two
four-supports are distinct. Two distinct four-subsets of the seven labels can
contain at most one common triangle: if they contained two distinct triangles,
the union of those triangles would be a four-set contained in both supports,
forcing the supports to be equal.

So at most one selected singleton block can be rank one with exactly two
touches.

All three singleton blocks are touched. Rank-one singletons therefore have at
least two touches, with at most one attaining two, while rank-two singletons
have at least four. In every case the three singleton blocks contribute at
least `2+3+3=8` touch incidences.

## 5. Touched-block bound

Let `h,e,c` be the numbers of touched root blocks, touched actual-empty blocks,
and touched complete blocks. There are exactly three touched singleton blocks,
so `h=e+3+c`.

Because `d_root=0`, the touched complete triangle rows are independent. The
committed face-local containment of the four external relation directions gives
`rank H(T)-rank H(C)>=4`.

The triangle boundary space on seven labels has rank at most 15, hence `c<=11`
and therefore `e>=h-14`.

Every touched actual-empty block has at least two incidences because its nonzero
local constraint space lies in `P` and `d1(P)>=2`. The three singleton blocks
contribute at least eight incidences, and every touched complete block at least
one. The eight no-root four-cycles contribute exactly 32 cycle-block
incidences. Thus
`32 >= 2e + 8 + c = h+e+5 >= 2h-9`.

Therefore `h<=20`.

## 6. Exact virtual support certificate

The verifier enumerates every `S_7` orbit of multisets of eight tetrahedral
four-supports, with multiplicity at most three. It reproduces the established
orbit sequence
`1,1,4,14,61,268,1283,6032,27763`.

Exactly 13,574 size-eight support orbits have at most 20 touched triangle
blocks.

For each such orbit, the verifier checks all 420 ways to choose three disjoint
matched coordinate pairs `M1,M2,M3` and the unmatched pair `U`. This is
`13574 * 420 = 5,701,080` support-orbit/matching pairs.

For a fixed matching, a touched block is declared virtually empty whenever it
passes only the following necessary tests:

- rank-one with at least three touches, or rank-one with exactly two touches on
  one of `M1,M2,M3`;
- rank-two with at least four touches.

A block is eligible as a selected singleton whenever it survives every sharp
`Mi union {j}` deletion, with the additional proved rule that rank-two
singletons need at least four touches. Among a selected singleton triple, at
most one rank-one block may have exactly two touches.

The search then makes every empty-eligible block virtually empty, even if no
single rank-four `P` could contain all those local spaces simultaneously. This
strictly enlarges the actual state space. The remaining necessary checks are:

1. the virtual complete triangle rows are independent;
2. `rank H(T)-rank H(C)>=4`;
3. the sum of virtual local coefficient dimensions, granting each rank-two
   singleton one independent constraint line, is at least four;
4. the union of the corresponding virtual generator supports covers at least
   seven external coordinates, as required by `d4(P)>=7`.

Turning additional blocks empty can only shrink the complete-row span and
increase the nominal coefficient dimension/support. Hence every actual `r=3`
state would survive this virtual search.

The six fixed verifier shards give:

```text
orbit range      h<=20       matching pairs       virtual survivors
0:5000            4633          1,945,860                 0
5000:10000        2628          1,103,760                 0
10000:15000       2451          1,029,420                 0
15000:20000       1370            575,400                 0
20000:25000       1691            710,220                 0
25000:27763        801            336,420                 0
-----------------------------------------------------------------
total            13574          5,701,080                 0
```

Thus no `r=3` state exists.

## 7. Exactness of rank decisions

All support, matching, incidence, and canonicalization calculations are exact.
Triangle-row ranks are computed modulo `2^31-1`. The verifier checks primality
by Lucas-Lehmer. Triangle rows have squared Euclidean norm three and rank at
most 15, and the verifier checks
`(2^31-1)^2 > 3^15`.

Hadamard's inequality therefore makes every modular triangle-row rank used by
the certificate equal to its rational rank.

## 8. Consequence

The final three-singleton profile has no `r=3` branch. On current main this
reduces the coefficient-code split from `r=0,1,2,3,4` to `r=0,1,2,4`.

The separately pushed `r=4` perfect-matching closure is not used by this proof
and is not assumed here. After that result is integrated, only `r=0,1,2`
remain in this finite eight-no-root `k=4,p=3` route.
