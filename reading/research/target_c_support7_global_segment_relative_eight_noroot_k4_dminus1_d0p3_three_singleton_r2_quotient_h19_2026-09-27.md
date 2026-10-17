> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_r2_quotient_h19_2026-09-27.md) · source SHA-256 `bd573103c1a253043866c2f5c8c1f8687d7b6895093a93b122d93d7586160800`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6cd8e11b6fef41043d547c287acd6ba4afe7df82", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_r2_quotient_h19_2026-09-27.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "37b4e40d8690c139f457326f6601b092f18bd77da537ec9469c0a1970fec8357"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: r=2 quotient-code reduction and h<=19 bound

Date: 2026-09-27

Status: proof-level reduction for the remaining eight-no-root
`k=4,D=-1,d_root=0,p=3` three-singleton profile in the subcase where
the rank-four coefficient space `P<=Q^8` has exactly two projective
weight-two lines. This note does not claim closure of the r=2 subcase,
Target C-II, or Erdos Problem #99.

## 1. Inputs from current main

Current main gives

$$
\operatorname{rank} P=4,\qquad
(d_1,d_2,d_3,d_4)(P)\ge (2,4,5,7).
$$

The incomplete-root profile consists of exactly three singleton blocks.
Distinct projective weight-two lines of `P` have disjoint supports.
If `M` is the support of a weight-two line, then every selected singleton
block `b` satisfies

$$
|I_b\setminus M|\ge2
$$

and the sharper puncture condition

$$
E_b\not\subset P+K_{M\cup\{j\}}
$$

for every `j notin M`.

Assume exactly two projective weight-two lines occur. Write their disjoint
supports as `M1,M2`, let `g_i` span the line supported on `M_i`, and put

$$
A=\langle g_1,g_2\rangle,\qquad
U=[8]\setminus(M_1\cup M_2).
$$

Thus `dim A=2` and `supp(A)=M1 union M2`.

## 2. The unmatched projection has rank two

Consider the coordinate projection

$$
\pi_U:P\to\mathbf Q^U.
$$

Its kernel is exactly `A`. Certainly `A<=ker(pi_U)`. If the kernel
contained any `v notin A`, then the three-dimensional subspace
`A+<v>` would be supported on the four coordinates `M1 union M2`.
That would give

$$
d_3(P)\le4,
$$

contrary to `d_3(P)>=5`.

Hence

$$
\ker(\pi_U|_P)=A,\qquad \operatorname{rank}\pi_U(P)=2.
$$

In particular, the four unmatched coordinates carry a genuine rank-two
projection of the residual coefficient geometry.

## 3. Quotient normal form

Quotient `Q^8` by `A`. Each matched pair `M_i` contributes one
residual quotient coordinate because `Q^{M_i}/<g_i>` is one-dimensional;
the four unmatched coordinates remain ordinary coordinates. Therefore

$$
\mathbf Q^8/A\cong\mathbf Q^6
$$

with coordinates

$$
(q_1,q_2,u_1,u_2,u_3,u_4).
$$

Let

$$
R=P/A\le\mathbf Q^6.
$$

Then `rank R=2`.

For any nonzero `r in R`, choose a lift `v in P`. Adding a suitable
multiple of `g_i` independently on each matched pair can kill one of the two
coordinates of `v|_{M_i}` whenever the residual coordinate `q_i` is
nonzero, and can kill both coordinates when `q_i=0`. Thus the minimum
Hamming weight among representatives of the coset `v+A` is exactly the
ordinary Hamming weight of `r` in these six quotient coordinates.

If `R` contained a nonzero word of weight one or two, `P` would therefore
contain a nonzero word of weight at most two outside `A`. Weight one is
excluded by `d_1(P)>=2`; weight two would be a third projective weight-two
line, contrary to the definition of the r=2 subcase. Hence

$$
\boxed{d_1(R)\ge3.}
$$

The restriction of `R` to the four unmatched coordinates has rank two by
Section 2. Also at least three unmatched coordinate columns are nonzero:
`A` already supports exactly four coordinates, while
`d_4(P)=|\operatorname{supp}P|>=7`.

Equivalently, the residual rank-two code `R` has length six, minimum
distance at least three, rank-two restriction on `U`, and support on at
least three of the four `U` coordinates.

## 4. Rank-two three-touch singleton blocks are impossible

Fix a selected singleton block `b`.

A weight-one representative of the nonzero quotient line
`W_b=(E_b+P)/P` violates a sharp puncture. If a weight-two representative
meets either `M_i`, its support is contained in `M_i union {j}` for some
`j notin M_i`, again violating the sharp puncture. Therefore every
weight-two representative of `W_b` is supported entirely in `U`.

Suppose now that `rank E_b=2` and `b` has exactly three touches. Write the
three projective local-direction multiplicities as `m0,m1,m2`, with
direction `s` selected by the singleton row.

The selected constraint row lies in `P`, so its weight is at least two.
Each of the two nonselected local rows represents `W_b`, so its weight is
also at least two. Since the three multiplicities sum to three, this forces

$$
(m_0,m_1,m_2)=(1,1,1).
$$

The two nonselected quotient rows then have two distinct weight-two supports.
By the preceding localization, both supports lie in `U`, so all three
touches lie in `U`. The selected constraint row is the third two-subset of
that three-touch set. It is a weight-two word of `P` supported inside
`U`, distinct from the two existing lines supported on `M1,M2`.
Contradiction.

Therefore every rank-two selected singleton has at least four touches.

## 5. At most two two-touch empty blocks

Let `a` be an actual-empty touched block. Compatibility gives `E_a<=P`.

If `rank E_a=1` and `a` has exactly two touches, its unique nonzero local
row is a weight-two line of `P`. Hence its touch set is exactly `M1` or
`M2`.

For a fixed matched pair `M_i={x,y}`, at most one rank-one block can have
touch set `M_i`. If the tetrahedral supports of occurrences `x,y`
coincide, the committed local-block rule makes every common touched block
rank two, not rank one. If those tetrahedral supports are distinct, two
distinct four-subsets of the seven ground labels contain at most one common
triangle: two distinct common triangles would have four-vertex union, forcing
the two tetrahedra to coincide.

Thus each of `M1,M2` supports at most one rank-one two-touch actual-empty
block. Across all actual-empty blocks, at most two have incidence two.
Every other rank-one empty block has incidence at least three, while every
rank-two empty block has incidence at least four by `d_2(P)>=4`.

If `e` is the number of touched actual-empty blocks, their total incidence
is therefore at least

$$
3e-2.
$$

## 6. Improved touched-block bound

Let `h,e,c` be the numbers of touched blocks, touched actual-empty blocks,
and touched complete blocks. There are exactly three touched singleton
blocks, so

$$
h=e+3+c.
$$

Because `d_root=0`, the touched complete triangle rows are independent.
The committed face-local containment of the four external relation directions
gives

$$
\operatorname{rank}H(T)-\operatorname{rank}H(C)\ge4.
$$

The triangle boundary space on seven labels has rank at most 15. Hence

$$
c\le11,\qquad e\ge h-14.
$$

Each selected singleton has at least two touches, so the three singleton
blocks contribute at least six incidences. Complete touched blocks contribute
at least one incidence each. The eight no-root four-cycles contribute exactly
32 cycle-block incidences. Combining this with Section 5 gives

$$
32\ge (3e-2)+6+c.
$$

Using `h=e+3+c`,

$$
32\ge h+2e+1.
$$

Since `e>=h-14`,

$$
32\ge 3h-27,
$$

and therefore

$$
\boxed{h\le19.}
$$

This improves the previous coarse r=2 bound `h<=21` by two touched blocks.

## 7. Remaining r=2 task

The r=2 branch is not closed by this note. The exact finite support search can
now be restricted to support multisets with at most 19 touched root blocks.
For each such support state it is enough to impose two disjoint weight-two
supports, the quotient-code conditions above, the sharp singleton conditions,
complete-row independence, face-local capacity, coefficient generation, and
`d_4(P)>=7`.

A zero-survivor certificate over that reduced state space would close r=2.
