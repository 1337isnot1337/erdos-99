# Erdős Problem #99 — outer-flat hinge and local-flex amplification

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** actual-outer / flat-pentagon train gate; low-`t` pentagon train-star packing; audited §156 face-closure coordinates and mixed rigidity
**Claim class:** proof-only structural composition awaiting independent audit

## LEVEL I STATUS

`STILL OPEN`

The actual-outer / flat-pentagon gate forces one of two large train families. The outer-to-flat branch has additional source and rigidity structure because every such train has exactly one bounded endpoint, hence its train-angle column is private to that bounded face.

Put
\[
\Delta_2={\pi\over2\sqrt3},\qquad C_0:=2\sqrt{\Delta_2}+0.00042,
\]
and define
\[
m(t):={1\over3}\left(7\pi+3C_0-{27t\over2}\right)
={7\pi\over3}+C_0-{9t\over2},
\tag{OH.1}
\]
\[
q_0(t):=2t-\pi.
\tag{OH.2}
\]
On an `R_F=o(D)` low-`t` subsequence, after passing further if necessary, the outer-flat gate yields one of
\[
{L_{OO}\over D}\ge m(t)-o(1)
\tag{OH.3}
\]
or
\[
{L_{OF}\over D}\ge m(t)-o(1).
\tag{OH.4}
\]

Assume the second branch. Let `G` be the number of metrically good flat pentagons and let `d_O(P)` be the number of their terminal trains whose other terminal occurrence lies on the actual outer face. Define
\[
N_j:=|\{P:d_O(P)\ge j\}|.
\]
Then
\[
\boxed{
{N_2\over D}\ge {m(t)-q_0(t)\over4}-o(1),
}
\tag{OH.5}
\]
and
\[
\boxed{
{N_3\over D}\ge {m(t)-2q_0(t)\over3}-o(1),
}
\tag{OH.6}
\]
whenever the displayed right sides are positive.

At the current proof-only floor
\[
t_{42}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0013751,
\]
this gives
\[
\boxed{{N_2\over D}\ge0.1353112447068753\ldots-o(1),}
\tag{OH.7}
\]
\[
\boxed{{N_3\over D}\ge0.0136867854861351\ldots-o(1).}
\tag{OH.8}
\]
Thus near `t_42` either there are at least `1.0414296...D` actual outer-to-outer trains, or there are at least `0.1353112...D` flat pentagons each receiving at least two actual outer trains and at least `0.0136867...D` flat pentagons each receiving at least three.

Even throughout the conditional band `t<=1.8585`, the outer-flat branch forces
\[
\boxed{{N_2\over D}\ge0.0741927814234730\ldots-o(1).}
\tag{OH.9}
\]

## 1. Endpoint multiplicity count

Every outer-to-flat train contributes to exactly one `d_O(P)`, so
\[
\sum_P d_O(P)=L_{OF}.
\tag{OH.10}
\]
The number of good pentagons satisfies
\[
G\le p_5\le f\le Q.
\tag{OH.11}
\]
The exact outer-walk identity gives
\[
{Q\over D}=2t-\pi-\delta+o(1)\le q_0(t)+o(1).
\tag{OH.12}
\]

Pentagons outside `N_2` contribute at most one outer terminal, while those in `N_2` contribute at most five. Hence
\[
L_{OF}\le G+4N_2,
\]
which together with (OH.4), (OH.11), and (OH.12) proves (OH.5).

Likewise pentagons outside `N_3` contribute at most two outer terminals and those in `N_3` at most five, so
\[
L_{OF}\le2G+3N_3,
\]
proving (OH.6).

## 2. Pairwise train-disjoint outer hinges

For every pentagon counted by `N_2`, choose any two of its outer-to-flat terminal trains. Pairs chosen at different pentagons are automatically train-disjoint: a complete outer-to-flat train has only one bounded terminal occurrence.

In the flat-trapezoid limit the five pentagon edge axes lie on three projective triangular-lattice axes. Therefore the two selected axes are either `o(1)` apart or `pi/3+o(1)` apart. Classifying each selected pair by these two cases and pigeonholing gives a pairwise train-disjoint subfamily of one type of size at least `N_2/2`.

At `t=t_42`, the outer-flat branch therefore contains at least
\[
\boxed{0.0676556223534376\ldots D-o(D)}
\tag{OH.13}
\]
pairwise train-disjoint actual outer hinges of one coherent type: almost-parallel or near-60-degree. For `t<=1.8585`, the corresponding coefficient is at least
\[
0.0370963907117365\ldots .
\tag{OH.14}
\]

## 3. Three-outer pentagons give exact localized contact flexes

Fix a good pentagon `P` counted by `N_3` and choose three of its outer-to-flat trains. In audited §156 train-angle coordinates, a train column contributes to the two closure rows of each bounded face at which it terminates. Since each chosen train has its other endpoint on the actual outer face, these three columns occur in no bounded-face closure rows except the two rows of `P`.

The local closure block is a `2 x 3` real matrix whose columns are the corresponding vectors `J r_e`. It has a nonzero kernel vector. Extend that vector by zero on every other train coordinate. The result lies in the global kernel of `C_face`; by §156.6 it integrates to an infinitesimal contact flex modulo translations.

Selections from different pentagons use disjoint train supports, so the resulting flexes are linearly independent.  The earlier shorthand `3N_3=o(T)` is not valid: both quantities can be linear in `D`.  What is needed, and what the exact ledgers give, is a strict support gap.  The union of the selected supports uses at most `3N_3<=3G<=3Q` train coordinates.  Meanwhile the complete-train floor gives

\[
{T\over D}\ge C_0+{t\over2}+{\kappa\over2}-o(1),
\]

while the outer ledger gives

\[
{3Q\over D}=6t-3\pi-3\delta+o(1).
\]

Therefore the number of train coordinates omitted by the union is at least

\[
\boxed{
{T-3N_3\over D}
\ge C_0+3\pi-{11t\over2}+{\kappa\over2}+3\delta-o(1).
}
\tag{OH.15}
\]

After dropping the nonnegative bonuses, the right side is still greater than `1.108` throughout `t<=1.8585` (and greater than `1.31` at `t_42`).  Thus the union omits linearly many train coordinates.  Every vector in the localized span vanishes on those coordinates, whereas the Euclidean rotation vector is the all-ones train-angle vector.  Hence the span does not contain the rotation vector.  The localized kernels therefore form a subspace `W_OF` of genuinely non-Euclidean contact flexes with
\[
\boxed{\dim W_{OF}\ge N_3.}
\tag{OH.16}
\]
Thus in the outer-flat branch at `t_42`,
\[
\boxed{\dim W_{OF}\ge0.0136867854861351\ldots D-o(D).}
\tag{OH.17}
\]

Canonical mixed rigidity makes the active-diameter derivative map injective on `W_OF`: a contact flex annihilating all active diameter derivatives would be Euclidean. KKT stationarity and strict positivity of the relative-interior diameter weights then imply that every nonzero `w in W_OF` has at least one positive and at least one negative active-diameter first variation. Therefore the localized three-train pentagon flexes require genuine two-sided diameter blocking, not merely one active diameter row of one sign.

## 4. Frontier effect

The current-floor small-residual branch now has a sharper dichotomy:

```text
>= 1.0414296 D actual outer-to-outer trains,
    each individually two-sidedly diameter braced,

or

>= 0.1353112 D flat pentagons with two actual outer trains,
>= 0.0676556 D disjoint coherent outer hinge pairs of one type,
>= 0.0136867 D flat pentagons with three actual outer trains,
>= 0.0136867 D independent localized non-Euclidean contact flexes,
    each requiring active diameter derivatives of both signs.
```

This still does not bound how many localized flexes one diameter row can block. The remaining useful theorem is now very specific: a block-local locking bound for the near-extremal Woodall diameter thrackle acting on these disjoint outer-hinge / three-train face modes.

## 5. Scope audit

- The theorem is conditional on the `R_F=o(D)` low-`t` branch and the proof-only AG42 input inherited by the outer-flat gate.
- `L_OF` trains have exactly one bounded endpoint; this is essential both for train-disjointness across pentagons and for the private-column argument in §3.
- The local `2 x 3` kernel argument is exact; only the phase description of the two-train hinges is asymptotic.
- No claim is made that distinct localized flexes require distinct diameter rows.
- No exact hidden contact, unit triangle, or strict sub-`D` competitor is produced.

C-II and Level I remain open.
