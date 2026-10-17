> Generated reading edition · [exact source](../../../docs/reports/target_c_inactive_chamber_core_coupling_regression_2026-09-12.md) · source SHA-256 `072b4fe5aa59381a6968e5154b3637ba1749e0b30d96e4235a1dc35e63dc3b10`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F1B8526DDC40","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_inactive_chamber_core_coupling_regression_2026-09-12.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=398099865614ee39ea028fea00d589f50e8bc2ec; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — inactive chamber co-embedded with a triangle-free contact core

**Date:** 2026-09-12  
**Repository commit:** `ce45eb3` at the start of this subrun  
**State version:** `2026-09-12.audit.44`  
**Run type:** hostile regression / inactive-container closure attack  
**Target:** C-II, macroscopic inactive-container branch  
**Computation:** `research/verify_target_c_inactive_chamber_core_coupling_regression.py`

## STATUS

`REGRESSION — PROVED FINITE FAMILY, NONCANONICAL`

**September 12 continuation correction:** the former scale `1+1/m` did not
give a unit-separated family: at `m=20`, the shell point `(10,10)` and the
scaled inner point `(9,9)` have squared distance `363/400<1`. The former
support argument omitted the factor `sqrt(3)/2` converting axial coordinates
to Euclidean normal distance. The construction below uses the repaired scale
`1+1/(2m)`. The certificate now exhausts every shell/interior pair with integer
arithmetic. Only the repaired family is asserted here.

This is an exact family showing that a triangle-free positive-contact core can be
co-embedded with a genuine macroscopic inactive face whose isolated population is
near Oler capacity and has many deep near-unit pairs. It is not asserted to be a
global minimum-diameter source. It therefore does not close C-II; it rules out a
container/core closure based only on the current local chamber statistics.

## 1. Exact construction

Use the unit triangular lattice with axial basis vectors (u,v) making angle
(pi/3). For an integer (rge0), write

$$
 H_r:=\{iu+jv:\max(|i|,|j|,|i+j|)\le r\}.
$$

The convex hull of (H_r) is a regular hexagon of side length (r), and

$$
 |H_r|=1+3r(r+1).
\tag{IC.1}
$$

For (mge8), let the positive-contact core be the outer lattice shell

$$
 B_m:=\{iu+jv:\max(|i|,|j|,|i+j|)=m\}.
$$

Its induced unit-contact graph is a single cycle with (6m) vertices and (6m)
unit edges. At every shell corner the two neighboring shell vertices are at
distance (sqrt3), not one, so the cycle contains no unit equilateral triangle.

Set

$$
 r=m-2,
 \qquad s_m=1+{1\over 2m},
 \qquad I_m:=s_m H_r.
\tag{IC.2}
$$

The full finite source is

$$
 A_m:=B_m\cup I_m.
\tag{IC.3}
$$

The homothetic inner hexagon has support distance

$$
 {\sqrt3\over2}\bigl(m-s_m(m-2)\bigr)
 ={\sqrt3\over2}\left({3\over2}+{1\over m}\right)>1
\tag{IC.4}
$$

from every side of (\operatorname{conv}B_m). Thus every point of (I_m) is more
than one unit from every shell point. Distinct points of (I_m) have squared
distance

$$
 s_m^2(a^2+ab+b^2)>1
$$

for every nonzero axial difference ((a,b)). Hence all points of (I_m) are
contact-isolated in the full source.

The contact graph of (A_m) is exactly the shell cycle (B_m). It is triangle-free,
and (A_m) contains no exact unit equilateral triangle.

Since (A_m\subset H_m) and opposite shell vertices are (2m) apart,

$$
\operatorname{diam}A_m=2m.
\tag{IC.5}
$$

The bounded face of the shell cycle is an actual inactive chamber containing all of
(I_m). The positive-contact core has (6m=O(\operatorname{diam}A_m)) vertices,
whereas the inactive population is quadratic.

## 2. Exact chamber scale and Oler slack

The regular hexagon (H_m) has area

$$
 \operatorname{area}(H_m)={3\sqrt3\over2}m^2,
\qquad
 {\operatorname{area}(H_m)\over a_0}=3m^2,
 \qquad a_0={\sqrt3\over2},
\tag{IC.6}
$$

and perimeter (6m). The number of isolated chamber points is, by (IC.1),

$$
 |I_m|=1+3(m-2)(m-1)=3m^2-9m+7.
\tag{IC.7}
$$

Therefore the Oler slack of the actual chamber (H_m), computed using the isolated
population, is exactly

$$
\begin{aligned}
 \Sigma_m
 &:={\operatorname{area}(H_m)\over a_0}
   +{\operatorname{per}(H_m)\over2}+1-|I_m|\\
 &=3m^2+3m+1-(3m^2-9m+7)\\
 &=12m-6.
\end{aligned}
\tag{IC.8}
$$

Thus the chamber has area (Theta(D^2)), isolated population (Theta(D^2)),
perimeter (O(D)), and Oler slack (O(D)), with (D=2m). Moreover

$$
 |A_m|=6m+(3m^2-9m+7)=3m^2-3m+7=|H_{m-1}|+6.
\tag{IC.10}
$$

So the full source has the cardinality of a unit triangular-lattice hexagon of radius
one less, up to only six points, while its interior population has no unit contacts.
These are the exact scales in the surviving inactive-container branch.

## 3. Deep near-unit pairs

Every pair of adjacent points in the unscaled shell-interior lattice (H_r) has
distance (s_m=1+1/(2m)) after the homothety. Restrict a greedy matching to the
strictly smaller lattice hexagon (H_{m-3}). It still gives
(Omega(m^2)=Omega(D^2)) vertex-disjoint pairs, and their endpoints have support
gap

$$
 {\sqrt3\over2}\bigl(m-s_m(m-3)\bigr)
 ={\sqrt3\over2}\left({5\over2}+{3\over2m}\right)>2
$$

from the chamber boundary. For an arbitrary prescribed fixed Euclidean depth
`w`, use `H_{m-k}` instead, with a fixed integer `k>=3` chosen so that
`(sqrt(3)/2)(k-1/2)>w`. Its matched population is still quadratic in `m`.

All those pairs satisfy

$$
1<|x-y|=1+{1\over 2m}=1+{1\over D}.
\tag{IC.9}
$$

The first-contact motions of such pairs therefore exist locally, but they only create
zero-stress contact components when the shell core is held fixed, exactly as in the
protected-contact obstruction. The construction makes this failure occur in a
chamber that is genuinely bounded by a positive contact core, not merely in an
isolated abstract container.

## 4. What this regression rules out

It is a finite exact counterexample to the local implication

```text
triangle-free contact core
+ actual bounded inactive face
+ quadratic isolated population
+ area and population agree to boundary order
+ linear perimeter/Oler slack
+ quadratic deep near-unit matching
    => exact unit triangle or positive KKT activation forced by the chamber data.
```

It also rules out obtaining a strict sub-(D) competitor by moving only the protected
interior population: the shell vertices already realize the diameter, and the
interior points are separated from the shell by a fixed margin. A same-cardinality
strict competitor would have to alter the diameter-carrying shell/core or use a new
source-level global argument.

## 5. Exact strict competitor for this model

The family is not a global-minimum counterexample, and in this regular model the
missing source-level comparison can be exhibited exactly. Let

$$
 L_m:=H_{m-1}\cup\{(m-i)u+iv:0\le i\le5\}.
\tag{IC.11}
$$

The six added points lie on one side of the radius-(m) hexagon. They are mutually
unit-separated, and every point of (H_{m-1}) is at least unit distance from them
because all points belong to the unit triangular lattice. Hence (L_m) is
unit-separated. Its cardinality is

$$
 |L_m|=|H_{m-1}|+6=|A_m|.
\tag{IC.12}
$$

Every point of (H_{m-1}) has norm at most (m-1), while every added point has norm
at most (m). Thus a cross-distance is at most (2m-1); two points in (H_{m-1})
are at distance at most (2m-2), and two added points on the same side are at
distance at most five. For (m\ge8),

$$
 \operatorname{diam}L_m\le2m-1<2m=\operatorname{diam}A_m.
\tag{IC.13}
$$

Therefore this exact co-embedded regression family does admit a same-cardinality
strict-diameter competitor. The competitor is allowed to contain unit equilateral
triangles, as it must be in a global-minimality comparison. This calculation removes
the specific family from the global survivor set, but it does not provide the needed
replacement theorem for arbitrary inactive chambers.

## 6. Hostile scope audit

* (A_m) is a regression family, not a global minimizer and not a counterexample to
  Erdős #99. Its diameter may be improved by a different global arrangement.
* The positive core is the shell cycle; no full-source ZR/ZF affine-kernel statement
  is used, and no isolated point is assigned a core coordinate.
* The construction is exact in the quadratic form (a^2+ab+b^2); the verifier checks
  the shell contact graph, absence of triangles, cross-separation, diameter, chamber
  count, the sharpened (12m-6) Oler slack, and a deep matching by exact rational
  arithmetic.
* The regression attacks local chamber-to-core mechanisms only. It does not address
  the still-missing global-minimality theorem that could rule out this geometry as an
  optimal source.
* The exact competitor in (IC.11)--(IC.13) rules out this particular family as a
  global minimizer, but it relies on its regular lattice scaffold and says nothing
  about arbitrary saturated inactive chambers.

The exact surviving obstruction is therefore source-level: prove that a saturated
inactive face cannot coexist with the diameter-carrying positive core in a global
minimum-diameter configuration, or construct a strict source-preserving competitor
that necessarily moves/locks that core. The local chamber statistics are insufficient.
