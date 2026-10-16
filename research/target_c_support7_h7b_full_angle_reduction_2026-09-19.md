<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "946c922d132049f92d465093129297e90efe06f0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h7b_full_angle_reduction_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d4393b65775f82c7873c6a6a9b9adf529fad4a01022236fdc05c85c9b832cf52"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — full reciprocal-angle consistency cuts generic interior-ground H7b to 27 C7 orbits

**Date:** 2026-09-19  
**Claim class:** exact finite affine exclusion inside the generic interior-ground support-seven branch  
**Scope:** `H7b`: `y_0=0` strictly inside a strict convex heptagon `y_1,...,y_7`, with no reciprocal collinear triple  
**Depends on:** the audited 184-orbit generic `H7b` order/sign census; the audited physical equilateral-pentagon turn simplex; the exact force-to-raw-angle conversion  
**Certificate:** `research/verify_target_c_support7_h7b_full_angle_reduction_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding exact reduction left

\[
77=47\,C_7+30\,(C_3\sqcup C_4)
\]

generic interior-ground order/sign orbits. That reduction used the physical-pentagon turn simplex and triangle-angle identities only on triangles whose three vertices are non-ground hull vertices.

The full reciprocal order type contains more affine information. Introduce the angular gaps between **all** reciprocal rays at each non-ground hull vertex, including rays belonging to missing reciprocal edges, and impose all Euclidean triangle-angle sums among the eight reciprocal points. This yields exact Farkas contradictions for 157 of the original 184 generic order/sign orbits. The surviving necessary affine cases are

\[
\boxed{27\ C_7\text{ orbits}.}
\]

Thus, relative to the previously committed state,

\[
\boxed{77\longrightarrow27,}
\]

and every generic `C_3\sqcup C_4` interior-ground orbit is excluded.

This is not a support-seven exclusion. The 27 surviving `C7` cells satisfy this affine angular system with positive margin; actual equilateral-pentagon vector closure and reciprocal metric integrability remain nonlinear constraints.

## 1. Full raw-ray variables at the seven hull vertices

Fix a generic `H7b` state. At each hull vertex `i\in\{1,\ldots,7\}`, the six rays to the other hull vertices occur in convex-heptagon order

\[
i+1,i+2,\ldots,i-1\pmod 7.
\]

The interior ray to `y_0` is inserted at the already-enumerated radial slot `k_i\in\{1,\ldots,5\}`. Hence the seven rays from `y_i` to the other reciprocal points have a fixed strict raw order.

Let

\[
r_{i,0},\ldots,r_{i,5}
\]

be the six consecutive raw angular gaps in this seven-ray order, normalized by `pi`. Strict convexity and strict interiority of `y_0` give

\[
r_{i,p}>0,
\qquad
\sum_{p=0}^{5}r_{i,p}<1.
\tag{1.1}
\]

The second inequality is the strict interior-angle bound at a convex hull vertex: every other reciprocal point lies strictly inside the hull interior cone, whose angle is less than `pi`.

These 42 variables retain the two rays that are deleted when forming the five present reciprocal edges at `i`. Those deleted rays correspond to missing reciprocal edges, but they remain ordinary geometric rays between reciprocal points and therefore legitimately participate in triangle geometry.

## 2. Ground radial angles

Let

\[
h_j>0
\]

be the normalized counterclockwise angular gap at `y_0` from ray `0j` to ray `0(j+1)`, with indices cyclic modulo seven. Because the seven hull vertices surround the strictly interior ground point,

\[
\sum_{j=1}^{7}h_j=2.
\tag{2.1}
\]

The radial slot data also determine on which side of each directed hull chord the ground lies. With the convention used by the finite census,

\[
\chi(i,j,0)
=
\operatorname{sgn}\det(y_j-y_i,-y_i)
=
\operatorname{sgn}\det(y_i,y_j).
\tag{2.2}
\]

Therefore the counterclockwise ground arc from ray `0i` to ray `0j` is strictly less than `pi` when `\chi(i,j,0)=+1` and strictly greater than `pi` when `\chi(i,j,0)=-1`. In normalized form these are 21 strict affine inequalities in the `h_j`.

## 3. Tie the full raw angles to the physical force pentagons

At every non-ground vertex, delete the two missing-neighbor rays from the seven-ray raw order. Five present reciprocal rays remain. Their edge signs have the already-proved `2+3` hull pattern, so their signed force-cycle order is fixed.

Let

\[
x_{i,k}=\delta_{i,k}/\pi,
\qquad k=0,\ldots,4,
\]

be the five normalized consecutive force gaps. The physical equilateral-pentagon theorem gives

\[
\sum_{k=0}^{4}x_{i,k}=2
\tag{3.1}
\]

and the complete local affine turn-simplex inequalities

\[
q_{i,k}:=x_{i,k}+x_{i,k+1}-x_{i,k+3}>\frac13.
\tag{3.2}
\]

For each of the four consecutive pairs of present rays in raw order, the ordinary raw angle computed by summing the appropriate `r_{i,p}` is set equal to the exact affine angle obtained from the signed force gaps. If the two reciprocal-edge signs agree, the raw-forward angle is the corresponding force arc. If they differ, it is that force arc minus `pi`. These give 28 exact tie equalities.

No metric length or coordinate approximation enters these ties.

## 4. Impose every reciprocal triangle angle sum

Because the branch is generic, no three of the eight reciprocal points are collinear. Hence every unordered triple

\[
\{a,b,c\}\subset\{0,1,\ldots,7\}
\]

forms an ordinary Euclidean triangle and its three interior angles sum to `pi`.

There are

\[
\binom83=56
\]

such equations. At a non-ground hull vertex, the triangle angle is the sum of the appropriate consecutive `r_{i,p}` because all seven rays lie in the strict hull cone of width less than `pi`. At the ground, the radial chirotope in (2.2) determines whether the interior angle is the counterclockwise `h`-arc or its complement `2pi` minus that arc.

Thus all 56 triangle sums are exact affine equations in the 84 variables

\[
35\ x\text{-variables}
+42\ r\text{-variables}
+7\ h\text{-variables}.
\]

The complete equality system has 92 rows:

- 7 pentagon turn sums;
- 1 ground radial sum;
- 28 raw/force tie equations;
- 56 triangle angle sums.

The strict inequality system has 112 rows:

- 35 pentagon turn-simplex facets;
- 42 positive full raw gaps;
- 7 strict hull-interior-angle bounds;
- 7 positive ground radial gaps;
- 21 ground chirotope arc inequalities.

## 5. Exact Farkas certificates exclude 157 of the 184 generic orbits

Write the strict inequalities as

\[
A_r z<b_r
\]

and the equalities as

\[
E_s z=d_s.
\]

For 157 of the 184 order/sign orbits, the verifier stores rational multipliers `lambda_r>=0`, normalized by

\[
\sum_r\lambda_r=1,
\]

and unrestricted rational equality multipliers `mu_s` such that

\[
\sum_r\lambda_r A_r-\sum_s\mu_s E_s=0
\tag{5.1}
\]

but

\[
\sum_r\lambda_r b_r-\sum_s\mu_s d_s\le0.
\tag{5.2}
\]

If a strict feasible point existed, (5.1) and the strict inequalities would force the quantity in (5.2) to be strictly positive. This contradicts (5.2).

The committed verifier rebuilds the entire 184-orbit census and every affine row using integers and `fractions.Fraction`, then checks every certificate by exact coefficient cancellation. Numerical linear programming was used only to discover candidate multipliers; it is not part of the proof.

The exact census is

\[
\boxed{157\text{ excluded}=93\,C_7+64\,(C_3\sqcup C_4).}
\tag{5.3}
\]

All 64 generic `C_3\sqcup C_4` orbits are therefore impossible. Among the 157 certificates, 38 have zero final Farkas right-hand side; strictness of the weighted inequality still gives the contradiction. The most negative exact right-hand side occurring in the stored certificates is

\[
-\frac5{42}.
\]

The surviving 27 necessary affine cases are the one-based orbit indices

\[
\boxed{
115,118,129,130,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,169,170,171,172,173,174,175,176.
}
\tag{5.4}
\]

Every one has missing-graph type `C7`.

## 6. Relation to the previous 77-orbit endpoint

The previous exact generic `H7b` endpoint was

\[
77=47\,C_7+30\,(C_3\sqcup C_4).
\]

All 27 survivors in (5.4) are contained in that set. Hence the new full-angle layer removes exactly 50 additional previously surviving orbits:

\[
\boxed{50=20\,C_7+30\,(C_3\sqcup C_4).}
\]

No old exclusion is weakened or replaced.

## 7. Remaining bottleneck

The 27 survivors are not realizations. They still must satisfy several nonlinear compatibility conditions simultaneously:

1. each of the seven five-direction systems must close as an actual equilateral force pentagon, not merely satisfy the convex hull of its turn vectors;
2. the seven signed unit directions at the ground must have zero vector sum;
3. reciprocal radius ratios obtained from the law of sines must be globally integrable around the eight independent cycles of the 14-edge relation graph;
4. the resulting angle/radius data must reconstruct one common planar reciprocal point configuration.

The next finite target is therefore the 27 `C7` cells with nonlinear equilateral-pentagon closure plus law-of-sines cycle integrability. A rigorous interval or monotonicity certificate is preferable to another unconstrained numerical search.

The reciprocal-collinearity walls, ground-on-hull `H7a`, `H6`, and the surviving `H8` cases remain separate branches.

No theorem-state file is changed.

**Disposition:** generic interior-ground support seven is reduced exactly from 77 previously surviving order/sign orbits to 27, all of missing-graph type `C7`. C-II remains open.
