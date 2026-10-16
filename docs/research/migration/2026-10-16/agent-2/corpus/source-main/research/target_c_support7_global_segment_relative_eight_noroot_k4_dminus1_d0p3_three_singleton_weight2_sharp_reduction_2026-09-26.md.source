# Target C: weight-two sharp-shadow reduction for the final k=4 p=3 profile

Date: 2026-09-26

Status: proof-level reduction of the remaining eight-no-root
`k=4,D=-1,d_root=0,p=3` three-singleton profile. This does not close the
profile, Target C-II, or Erdos Problem #99.

Current main gives a rank-four coefficient space `P<=Q^8` with
`(d1,d2,d3,d4)>=(2,4,5,7)`. The mixed singleton-plus-pair profile is closed,
so the actual incomplete-root state consists of three singleton blocks.

## 1. A weight-two line forces sharp five-row descendants

Let `M` be the support of a weight-two line of `P`, and let
`j notin M`. Delete `S=M union {j}`.

The weight-two line gives puncture rank loss `q_S>=1`. Since `d2(P)>=4`,
no two-dimensional subspace can be supported on the three coordinates of
`S`, so `q_S<=1`. Hence `q_S=1`.

The all-depth deletion identity gives
`D(B\S)=-1+2*3-3=2`. The punctured coefficient rank is three, so the
five-row shadow has `k=2`; its unstripped incomplete-root cost is still
`p=3`.

The committed sharp five-row `D=2,k=2,p=3` theorem therefore applies for
all six choices of `j notin M`.

## 2. Every singleton becomes parent-sharp

Fix one of the three actual singleton blocks `b`, with local empty space
`E_b`, singleton line `L_b<=E_b`, and touch set `I_b`.

The sharp five-row theorem says that after every deletion
`M union {j}`:

- `b` remains touched;
- `pi_S(E_b) not subset pi_S(P)`.

The first statement is equivalent to
`|I_b\M|>=2`.

For the second, puncturing has kernel the coordinate subspace `K_S`, so
`pi_S(E_b) subset pi_S(P)` iff `E_b subset P+K_S`. Thus, for every
`j notin M`,
`E_b not subset P+K_{M union {j}}`.
In particular `E_b not subset P`.

The standard local singleton calculation then gives
`dim((E_b+P)/P)=1`: if `rank E_b=1`, noncontainment gives
`E_b intersect P=0`; if `rank E_b=2`, the actual singleton constraint is
the nonzero local determinant line `L_b<=E_b intersect P`, so the
intersection has dimension exactly one.

Therefore the existence of one weight-two line makes all three singleton
blocks parent-level sharp and gives each a distinguished quotient line
`W_b=(E_b+P)/P`.

## 3. Split by the number of weight-two lines

Current main already proves that distinct projective weight-two lines of this
`D=-1` rank-four code have disjoint supports. Hence there are at most four.

Thus the remaining profile splits as follows:

- no weight-two line: `d1(P)>=3`;
- one to three weight-two lines: their supports are pairwise disjoint and
  every singleton satisfies the sharp-puncture condition above for each one;
- four weight-two lines: their supports partition the eight coordinates and
  they form a basis of `P`.

The last case is the perfect-matching coefficient code.

## 4. Perfect-matching quotient geometry

Assume the four support pairs are `M_1,...,M_4`, with basis vectors
`g_i` supported on `M_i`. Then
`P=<g_1> direct_sum ... direct_sum <g_4>`, and

`Q^8/P = Q_1 direct_sum ... direct_sum Q_4`,

where `Q_i=Q^{M_i}/<g_i>` is one-dimensional.

For distinct `i,k` and `j in M_k`, the image of
`K_{M_i union {j}}` in the quotient is exactly `Q_i direct_sum Q_k`.
The sharp-puncture condition says that each singleton quotient line `W_b`
is contained in none of these coordinate two-planes.

Hence every `W_b` has nonzero projection to at least three of the four
matched-pair quotient summands. Equivalently, its distinguished coset has
Hamming distance at least three from `P`. In particular each singleton
block is touched in at least three matched pairs.

## 5. Empty blocks in the perfect-matching case

If `a` is an actual-empty touched block, compatibility gives `E_a<=P`.
The generalized support of `E_a` is its touch set `I_a`.

Every subspace of the direct-sum perfect-matching code has generalized support
equal to a union of whole matched pairs. Therefore `I_a` is a union of
whole `M_i`.

So a rank-one empty block uses at least one complete matched pair, and a
rank-two empty block uses at least two complete matched pairs.

## 6. Consequence

The final three-singleton branch no longer needs to be searched as one
undifferentiated rank-four problem.

The no-weight-two case may impose the stronger code profile
`(d1,d2,d3,d4)>=(3,4,5,7)`.

If weight-two lines exist, all three singleton blocks are sharp in the parent,
with explicit three-coordinate puncture exclusions. In the four-line
perfect-matching case, singleton quotient lines use at least three matched
pairs and every empty touch set is a union of matched pairs.

The companion checker verifies the finite support statements used here:
maximum four disjoint two-supports, the equivalence
`survival after all M+{j} deletions <=> |I\M|>=2`, the perfect-matching
two-plane criterion, and the union-of-pairs support property.
