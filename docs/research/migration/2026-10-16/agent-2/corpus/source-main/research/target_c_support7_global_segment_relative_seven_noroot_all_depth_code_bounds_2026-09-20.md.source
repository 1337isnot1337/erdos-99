# Target C: seven-no-root all-depth deletion and code bounds

Date: 2026-09-20

Status: exact structural strengthening of the seven-no-root deletion reduction. This does not close the remaining seven-no-root boundary and does not change the direct 3,874-cell generic-H6 endpoint.

Companion arithmetic verifier:

`research/verify_target_c_support7_global_segment_relative_seven_noroot_all_depth_code_bounds_2026_09_20.py`

## Setup

Let

`B = R union E`

be a hypothetical seven-no-root factor-three counterexample, where `R` is the selected root-row set and `|E|=7`. Write

`D(X)=|X|-3 delta(X)`.

The established six-no-root theorem and one-row deletion argument already give

`D(B) in {-2,-1}`

and show that every row of `E` is an `M`-coloop in the restriction to `B`.

Let `P <= Q^7` be the external coefficient-constraint space. As in the preceding local-block audits,

`rank(P)=7-k`.

The previous depth-two note used only deletions of one or two external rows. The same argument gives a bound for every deletion depth.

## Arbitrary deletion subsets

Fix `S subseteq E` with `|S|=s`, where `1<=s<=7`, and write

`B_S = B \ S`.

Because every external row is an `M`-coloop in `B`, deleting the whole set `S` lowers `r_M` by exactly `s`.

Let

`q_S = r_Q(B)-r_Q(B_S)`.

Then

`delta(B)-delta(B_S)=s-q_S`,

so

`D(B_S)=D(B)+2s-3q_S`.

The family `B_S` has at most six no-root rows when `s>=1`, so the established factor-three theorem applies:

`D(B_S)>=0`.

Therefore

`q_S <= floor((D(B)+2s)/3)`.

For the two possible seven-row defects this is

```text
s                         1  2  3  4  5  6  7
D(B)=-2: maximum q_S      0  0  1  2  2  3  4
D(B)=-1: maximum q_S      0  1  1  2  3  3  4
```

The first two columns recover the earlier one- and two-deletion statements. The later columns are new constraints on every remaining finite search.

## Coefficient-space interpretation

Deleting the external coordinates in `S` projects `P` onto the remaining coordinates. Its rank loss is exactly `q_S`. Hence

`q_S = dim {x in P : supp(x) subseteq S}`.

In other words, every shortened subcode of `P` supported on `s` coordinates has dimension at most the table above.

Let `d_j(P)` be the `j`th generalized Hamming weight: the minimum support size of a `j`-dimensional subspace of `P`. The shortened-dimension bound gives

`d_j(P) >= ceil((3j-D(B))/2)`.

Thus:

```text
D(B)=-2: d_1>=3, d_2>=4, d_3>=6, d_4>=7
D(B)=-1: d_1>=2, d_2>=4, d_3>=5, d_4>=7
```

Only the bounds with `j<=rank(P)=7-k` are relevant in a given arithmetic branch. Equivalently:

```text
D=-2
k=3, rank(P)=4: (d1,d2,d3,d4) >= (3,4,6,7)
k=4, rank(P)=3: (d1,d2,d3)    >= (3,4,6)
k=5, rank(P)=2: (d1,d2)       >= (3,4)
k=6, rank(P)=1: d1            >= 3
k=7, rank(P)=0

D=-1
k=3, rank(P)=4: (d1,d2,d3,d4) >= (2,4,5,7)
k=4, rank(P)=3: (d1,d2,d3)    >= (2,4,5)
k=5, rank(P)=2: (d1,d2)       >= (2,4)
k=6, rank(P)=1: d1            >= 2
k=7, rank(P)=0
```

## Local block consequences

For a touched root quotient block `b`, let `L_b <= P` be its local coefficient-constraint subspace. It is supported only on the external cycles that touch `b`.

An empty block can contribute rank zero, one, or two to `L_b`. A singleton can contribute rank zero or one. A pair or complete block contributes rank zero.

Therefore the generalized-weight bounds immediately imply:

- in the `D=-2` branch, every nonzero rank-one local constraint is supported on at least three external cycles;
- in the `D=-1` branch, every nonzero rank-one local constraint is supported on at least two external cycles;
- in either branch, every rank-two local constraint is supported on at least four external cycles.

The last item is stronger than the previous minimum-support prefilter, which only controlled individual nonzero vectors.

Since seven no-root four-cycles contribute exactly `7*4=28` block-touch incidences, if `n_2` blocks carry rank-two local constraint spaces and `n_1` blocks carry nonzero rank-one local constraint spaces, then necessarily

```text
D=-2: 4 n_2 + 3 n_1 <= 28
D=-1: 4 n_2 + 2 n_1 <= 28.
```

These are necessary conditions, not closure statements.

## Immediate filters for the two active small branches

For the remaining

`D=-2, k=4, d=0, p=3`

branch, `rank(P)=3`. The new bounds require

`d_1>=3, d_2>=4, d_3>=6`.

So any exact extension search can reject a candidate as soon as any of the following occurs:

- a nonzero coefficient vector has support at most two;
- a two-dimensional coefficient subspace is supported on at most three coordinates;
- the whole rank-three space is supported on at most five coordinates.

Equivalently, after deleting `s` external coordinates, the projected ranks must be at least

```text
s=1..7: 3, 3, 2, 1, 1, 0, 0.
```

For the active

`D=-1, k=3, d=0, p=1`

branch, `rank(P)=4`. The generic all-depth bounds require projected ranks at least

```text
s=1..7: 4, 3, 3, 2, 1, 1, 0.
```

The branch-specific five-row slack theorem already strengthens the `s=2` entry from `3` to `4`. The new `s>=3` entries remain additional necessary filters for its direct six-shadow verifier. In particular the full four-dimensional `P` must use all seven coordinates, and every two-dimensional subspace of `P` must use at least four coordinates.

## Verification

The companion verifier checks:

1. the complete list of 30 seven-no-root arithmetic boundary tuples from `D=7+p+3d-3k`;
2. the all-depth quotient-rank-drop caps for both `D=-2` and `D=-1`;
3. the closed-form generalized-weight formula against direct scanning of deletion sizes;
4. the branch-by-branch generalized-weight table; and
5. the projected-rank lower bounds for the two active small branches above.

It is a pure arithmetic checker and introduces no modular or probabilistic rank step.

## Next use

The next finite scans should impose these shortened-subcode bounds during coefficient-space generation, not only as a final pair-deletion test. For the remaining `D=-2,k=4,d=0,p=3` branch, rank-two empty-block constraints touched by only three cycles can now be discarded immediately. For the `D=-1,k=3,d=0,p=1` branch, triple- and deeper-deletion rank caps can be added to the existing direct six-shadow extension search before any `T`-space work.

The direct C-II endpoint remains unchanged:

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

No theorem-state authority file is changed by this result.
