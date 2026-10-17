# Target C-II — all lower runs remove the external-population loss from the fixed FREE pair

**Date:** 2026-09-18
**Status:** proved candidate awaiting promotion; proof-only strengthening of the fixed-pair FREE common-run theorem
**Scope:** the `PAIR-REUSE` branch for the two extreme all-inactive FREE modules
**Dependencies:** fixed-pair lossless common runs; two-sided gate absorption; two-sided outer-face localization; short-edge planarity; two-normal common-trunk cone theorem
**Certificate:** `research/verify_target_c_tooth_reflection_all_run_forest_union_2026_09_18.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The fixed-pair theorem pigeonholes the common lower edges into one pair of maximal lower runs. That pays a factor `(Z_D+1)^2`, where

\[
Z_D=|A\setminus F|.
\]

The loss is unnecessary on the cycle-rank side. Keep **all** maximal lower runs from the two extreme FREE ancestries which contain a reused edge. Each ancestry contributes a disjoint path forest with at most `Z_D+1` components. The intersection of the two forests is itself a forest. Euler characteristic then counts all common-path components at once.

This replaces the previous small-external currency

\[
\Theta\!\left({\sqrt D\over Z_D+1}\right)
\]

by

\[
\boxed{\Theta(\sqrt D)}
\]

throughout the entire regime `Z_D=o(sqrt(D))`.

Fix

\[
c_*:=0.129220199818177\ldots,
\qquad
h_*:={\sqrt{303}\over52},
\qquad
K>h_*,
\qquad
\alpha_K:=1-{h_*\over K}>0.
\tag{FU.1}
\]

Suppose the slow-scale module dichotomy is on the FREE side and the fixed extreme-pair reuse theorem is in its `PAIR-REUSE` branch. Let the two extreme canonical support normals be `N_1,N_2` and put

\[
\theta_D=\angle(N_1,N_2).
\]

The fixed-pair theorem gives

\[
\boxed{
 c_*-o(1)\le\theta_D\le{\pi\over2}+o(1).
}
\tag{FU.2}
\]

It also gives a set `E_*` of distinct original lower-gate edges which occur in **both** extreme ancestries, with

\[
\boxed{
E:=|E_*|\ge
\left({\alpha_K\over2}-o(1)\right)D,
}
\tag{FU.3}
\]

and

\[
1<|e|\le1+{K\over D}
\qquad(e\in E_*).
\tag{FU.4}
\]

All endpoints are old fully inactive source points in the original outer contact face.

Put

\[
R_D:=Z_D+1.
\tag{FU.5}
\]

## 1. Keep every lower run which carries a common edge

For ancestry `1`, let

\[
P_1,\ldots,P_p
\]

be all maximal consecutive lower-gate runs containing at least one edge of `E_*`. For ancestry `2`, define analogously

\[
Q_1,\ldots,Q_q.
\]

An activation ancestry is a simple sequence of distinct source vertices. Distinct maximal lower runs in the same ancestry are separated by at least one upper gate and therefore have disjoint vertex sets. Hence

\[
\mathcal P:=\bigcup_{a=1}^p P_a,
\qquad
\mathcal Q:=\bigcup_{b=1}^q Q_b
\]

are forests, each a disjoint union of paths, with

\[
\boxed{p,q\le R_D.}
\tag{FU.6}
\]

The upper-gate injection into `A\setminus F` is exactly what gives this component bound.

Every lower ancestry edge has original length at most

\[
1+t_D<1+h_*+o(1)<\sqrt2.
\tag{FU.7}
\]

Therefore all edges of `\mathcal P\cup\mathcal Q` lie in the common short-edge plane source graph. Let

\[
H:=\mathcal P\cup\mathcal Q,
\qquad
I:=\mathcal P\cap\mathcal Q.
\tag{FU.8}
\]

Since `I` is a subgraph of the forest `\mathcal P`, it is itself a forest.

## 2. Exact Euler characteristic for two path forests

Write `c_H` and `c_I` for the numbers of connected components of `H` and `I`, counting isolated intersection vertices in `c_I` when present. Since `\mathcal P`, `\mathcal Q`, and `I` are forests,

\[
|V(\mathcal P)|-|E(\mathcal P)|=p,
\qquad
|V(\mathcal Q)|-|E(\mathcal Q)|=q,
\qquad
|V(I)|-|E(I)|=c_I.
\]

Vertex/edge inclusion-exclusion gives

\[
|V(H)|-|E(H)|=p+q-c_I.
\tag{FU.9}
\]

For an arbitrary finite graph,

\[
|V(H)|-|E(H)|=c_H-\beta(H),
\]

where `beta(H)` is its cyclomatic number. Therefore

\[
\boxed{
\beta(H)=c_H-p-q+c_I.
}
\tag{FU.10}
\]

Because `E_*` is nonempty, `H` is nonempty, so `c_H>=1`. Combining with (FU.6),

\[
\boxed{
\beta(H)\ge c_I-2R_D+1.
}
\tag{FU.11}

Since `H` is plane, `beta(H)` is exactly the number of bounded faces of `H`.

This is the point that removes the `(Z_D+1)^2` pigeonhole loss: every common intersection component contributes globally before the `2R_D` forest-component correction is paid.

## 3. Many intersection components or one long compatible trunk

Every edge of `E_*` belongs to `I`. An edge-containing component of `I` is a path lying in one `P_a` and one `Q_b`. Along that entire component, the two ancestry traversals are either SAME throughout or OPPOSITE throughout.

Fix a threshold `s>=1`.

If every component of `I` contains fewer than `s` selected edges from `E_*`, the selected population occupies more than `E/s` distinct components of `I`. Hence (FU.11) gives

\[
\boxed{
\beta(H)>{E\over s}-2R_D+1.
}
\tag{FU.12}

Otherwise one common component `C` contains at least `s` selected edges. Since those selected edges are distinct, the path `C` has at least `s` path edges. Let `X_C` be its endpoint displacement.

Define

\[
b_*:=\sin(c_*/2)
=0.0645651571904745\ldots .
\tag{FU.13}
\]

If `C` is SAME-oriented, the two-normal cone theorem gives

\[
X_C\cdot {N_1+N_2\over|N_1+N_2|}
>
|E(C)|\sin(\theta_D/2)
\ge(b_*-o(1))s.
\tag{FU.14}
\]

If `C` is OPPOSITE-oriented, it gives

\[
X_C\cdot {N_1-N_2\over|N_1-N_2|}
>
|E(C)|\cos(\theta_D/2)
\ge(\cos(\pi/4)-o(1))s.
\tag{FU.15}
\]

Since `cos(pi/4)>b_*`, both cases imply that for the appropriate two-normal axis `U_C`,

\[
\boxed{
X_C\cdot U_C\ge(b_*-o(1))s.
}
\tag{FU.16}

## 4. Finite forest-union minimax

Ignore only integer-rounding and the displayed vanishing terms for the moment. The two competing lower bounds are

\[
{E\over s}-2R_D
\qquad\text{and}\qquad
b_*s.
\]

They balance when

\[
b_*s^2+2R_Ds-E=0.
\]

Thus define

\[
\boxed{
\Phi(E,R_D)
:=\sqrt{R_D^2+b_*E}-R_D.
}
\tag{FU.17}

At

\[
s={\Phi(E,R_D)\over b_*},
\]

one has exactly

\[
{E\over s}-2R_D=b_*s=\Phi(E,R_D).
\tag{FU.18}
\]

The threshold argument requires `s>=1`. Accordingly, the conclusion below is used whenever `Phi(E,R_D)/b_*>=1`; in every asymptotic regime considered in Sections 5--6, `Phi(E,R_D)->infinity`, so this condition and integer rounding are harmless.

Consequently the `PAIR-REUSE` branch forces, up to integer rounding and `o(1)` cone errors,

\[
\boxed{
\text{either}\quad
\beta(H)\ge\Phi(E,R_D)-O(1),
}
\tag{FU.19}
\]

or one common inactive trunk has actual two-normal displacement

\[
\boxed{
X_C\cdot U_C\ge\Phi(E,R_D)-o(\Phi(E,R_D))-O(1).
}
\tag{FU.20}

Substituting (FU.3), a convenient asymptotic lower form is

\[
\boxed{
\Phi(E,R_D)
\ge
\sqrt{
R_D^2+
\left({\alpha_Kb_*\over2}-o(1)\right)D
}
-R_D.
}
\tag{FU.21}

This formula is useful outside the strictly sub-square-root regime as well.

## 5. The small-external loss disappears completely

Assume

\[
Z_D=o(\sqrt D).
\tag{FU.22}
\]

Then `R_D=o(sqrt(D))`, and (FU.21) simplifies to

\[
\boxed{
\Phi(E,R_D)
\ge
\left(
\sqrt{{\alpha_Kb_*\over2}}-o(1)
\right)\sqrt D.
}
\tag{FU.23}

Therefore the fixed extreme FREE pair has the stronger proof-only fork

\[
\boxed{
\begin{array}{ll}
\text{LINEAR-MATCHING:}
&\displaystyle
\left({\alpha_K\over11}-o(1)\right)D
\text{ vertex-disjoint old inactive }(1+K/D)\text{-pairs};\\[3mm]
\text{or}\quad\text{FOREST-UNION CURRENCY:}
&\displaystyle
\left(
\sqrt{{\alpha_Kb_*\over2}}-o(1)
\right)\sqrt D
\text{ bounded faces or actual two-normal trunk drift.}
\end{array}
}
\tag{FU.24}

There is no remaining factor of `Z_D+1` in the second line.

For `K=1`,

\[
\alpha_1=0.6652520156628998\ldots
\]

and

\[
\boxed{
\sqrt{{\alpha_1b_*\over2}}
=0.146547093049564\ldots .
}
\tag{FU.25}

Thus a sub-square-root-external `PAIR-REUSE` survivor forces at least

\[
\boxed{
(0.146547093049564\ldots-o(1))\sqrt D
}
\]

bounded faces in the inactive lower-run union or the same amount of actual compatible-trunk displacement.

The coefficient in (FU.25) is numerically the same constant which appeared in the old fixed-cell theorem, but its scale has changed from

\[
0.146547\,{\sqrt D\over Z_D+1}
\]

to

\[
0.146547\,\sqrt D.
\]

## 6. A finite `Z_D=O(sqrt(D))` interpolation

More generally, if for some fixed `z>=0`,

\[
Z_D\le(z+o(1))\sqrt D,
\tag{FU.26}
\]

then monotonicity of `r -> sqrt(r^2+c)-r` gives

\[
\boxed{
{\Phi(E,R_D)\over\sqrt D}
\ge
\sqrt{z^2+{\alpha_Kb_*\over2}}-z-o(1).
}
\tag{FU.27}

For every finite `z`, this coefficient is strictly positive. Thus the forest-union argument actually forces `Omega(sqrt(D))` cycle-rank/drift throughout the whole regime

\[
Z_D=O(\sqrt D),
\]

with an explicit coefficient depending on the external-population constant.

## 7. What remains

This does not close C-II. It changes the residual bridge materially.

Previously, when `Z_D` was allowed to grow below `sqrt(D)`, the strongest fixed-pair common-run output could be as small as a slowly diverging quantity. After (FU.24), a hard FREE survivor with `Z_D=o(sqrt(D))` must instead carry a **square-root-size** source-level obstruction:

- either a linear vertex-disjoint inverse-`D` matching, or
- at least `Theta(sqrt(D))` bounded inactive faces in the union of the two extreme lower-run forests, or
- one common inactive trunk with `Theta(sqrt(D))` Euclidean displacement in its two-normal axis.

The next closure step should use this square-root population directly against the canonical outer-walk / force-hull currencies, or use the long common trunk for a protected source deformation. The old `(Z_D+1)^2` run-cell pigeonhole is no longer a genuine bottleneck.

C-II remains open. No theorem-state authority is changed.

**Disposition:** retained every reused lower edge across all maximal lower runs of the two extreme FREE ancestries; used the exact Euler characteristic of the union of two path forests; optimized the resulting global component-count versus two-normal trunk drift; and removed the external-population denominator from the sub-square-root FREE common-run currency.