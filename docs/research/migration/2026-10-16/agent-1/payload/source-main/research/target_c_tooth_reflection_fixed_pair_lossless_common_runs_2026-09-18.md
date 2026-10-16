# Target C-II — two extreme FREE modules remove the slow-scale loss from the common-run obstruction

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; proof-only refinement of the all-inactive FREE branch  
**Scope:** slow-scale reflection family after the module ANCHORED/FREE dichotomy  
**Dependencies:** slow-scale central reflection braid; module anchor dichotomy; multi-module lower-edge reuse; upper-gate injection into `A\setminus F`; common-run Euler-characteristic fork; two-normal common-trunk cone theorem  
**Certificate:** `research/verify_target_c_tooth_reflection_fixed_pair_lossless_common_runs_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding same-orientation heavy-reuse argument used a growing family of modules and paid a slow factor in order to manufacture a sufficiently separated pair. That is unnecessary on the FREE side of the module dichotomy. The slow-scale family already contains linearly ordered FREE modules spread over a fixed angular interval. Taking the first and last FREE modules gives a pair with a **constant** normal gap. Applying the lower-edge reuse theorem to only those two modules removes the `omega_D^(5/2)` loss and also removes the degree-six matching loss from the heavy branch.

Fix

\[
c_*:=0.129220199818177\ldots,
\qquad
h_*:=\frac{\sqrt{303}}{52}=0.334747984337100\ldots,
\]

and any fixed

\[
K>h_*,
\qquad
\alpha_K:=1-\frac{h_*}{K}>0.
\tag{FP.1}
\]

Let `kappa_D -> infinity`, `kappa_D=o(D^(1/4))`, and suppose the slow-scale module dichotomy lands on the FREE side rather than the exact-diameter braid side. Then there are at least

\[
\left(\frac{c_*}{2}-o(1)\right)\frac{D^{1/4}}{\kappa_D}
\tag{FP.2}
\]

all-inactive FREE modules, inherited from the ordered slow-scale family.

The conclusion below is finite up to the displayed `o(1)` terms and does not require any new canonical theorem-state input.

## 1. The extreme FREE modules have a fixed positive normal gap

Consecutive selected slow-scale normals differ by at least

\[
(2-o(1))\kappa_DD^{-1/4}.
\tag{FP.3}
\]

List the FREE modules in normal order and choose the first and last, with normals `N_1,N_2`. Combining (FP.2) and (FP.3),

\[
\boxed{
\theta_D:=\angle(N_1,N_2)\ge c_*-o(1).
}
\tag{FP.4}
\]

The underlying selected base normals lie in one quadrant, while each canonical support normal differs from its base normal by `O(D^-1/4)`. Hence

\[
\boxed{
\theta_D\le\frac\pi2+o(1).
}
\tag{FP.5}
\]

Thus a hard FREE survivor already contains two modules whose support directions are separated by a universal positive angle. No growing-module threshold is needed to create that separation.

## 2. Apply the reuse theorem with exactly two modules

Apply the multi-module lower-edge reuse theorem to these two FREE modules with

\[
m=2,
\qquad
R=1.
\]

For each module the theorem supplies at least `(alpha_K-o(1))D` original lower-gate edges of length

\[
1<|e|\le1+\frac KD.
\tag{FP.6}
\]

The two-module incidence fork becomes:

### LINEAR-MATCHING

The original source contains a vertex-disjoint matching of old fully inactive outer-face pairs of size

\[
\boxed{
\left(\frac{\alpha_K}{11}-o(1)\right)D
}
\tag{FP.7}
\]

satisfying (FP.6).

### PAIR-REUSE

There are at least

\[
\boxed{
\left(\frac{\alpha_K}{2}-o(1)\right)D
}
\tag{FP.8}
\]

distinct original lower-gate edges satisfying (FP.6) which occur in **both** chosen FREE ancestries.

The second conclusion follows because `R+1=2` and there are only two modules: every heavy edge is common to the pair. Unlike the previous growing-family extraction, no pair-pigeonhole, orientation-majority thinning, or degree-six matching is needed on the heavy side.

## 3. Direct lower-run pigeonhole keeps all common edges

Put

\[
Z_D:=|A\setminus F|,
\qquad
F=\operatorname{conv}B.
\]

Every upper gate in one all-inactive FREE ancestry activates a distinct source point outside `F`. Hence each of the two ancestries has at most

\[
Z_D+1
\tag{FP.9}
\]

maximal all-lower runs.

In PAIR-REUSE, distribute the common edges from (FP.8) among the at most `(Z_D+1)^2` ordered lower-run pairs. One pair of maximal lower runs

\[
P\subset\mathcal A_1,
\qquad
Q\subset\mathcal A_2
\]

therefore shares a set `E_*` of **distinct** original edges with

\[
\boxed{
q:=|E_*|
\ge
\left(\frac{\alpha_K}{2}-o(1)\right)
\frac{D}{(Z_D+1)^2}.
}
\tag{FP.10}
\]

Every edge of `E_*` satisfies (FP.6). All endpoints are old fully inactive outer-face source points.

No matching extraction is required for the remaining argument. This is the second loss removed by using the fixed extreme pair.

## 4. Componentwise traversal parity removes orientation thinning

Let

\[
I:=P\cap Q.
\]

Because `P` and `Q` are simple paths, every edge-containing component of `I` is a path. On one such component the two path traversals are automatically either in the same direction throughout that component or in opposite directions throughout it.

Thus the two-normal cone theorem can be applied **component by component** without first selecting one global relative orientation class.

For any real `s>=1`, either some component of `I` contains at least `s` edges of `E_*`, or no component does.

If no component contains `s` selected edges, then the selected edges occupy at least `q/s` distinct components of `I`. The exact two-path Euler-characteristic identity gives

\[
\boxed{
\beta(P\cup Q)\ge\frac qs-1.
}
\tag{FP.11}
\]

Because all lower-gate edges lie in the common plane short-edge graph, this is also the number of bounded faces of `P\cup Q`.

Suppose instead that a component `C` contains at least `s` selected edges. Let `L` be its total number of path edges. Since the selected edges are distinct,

\[
L\ge s.
\tag{FP.12}
\]

If the two paths traverse `C` in the SAME direction, the cone theorem gives, for the internal bisector

\[
B=\frac{N_1+N_2}{|N_1+N_2|},
\]

endpoint displacement `X` satisfying

\[
X\cdot B>L\sin(\theta_D/2).
\tag{FP.13}
\]

If they traverse `C` in OPPOSITE directions, the difference direction

\[
T=\frac{N_1-N_2}{|N_1-N_2|}
\]

satisfies

\[
X\cdot T>L\cos(\theta_D/2).
\tag{FP.14}
\]

By (FP.4)--(FP.5), both alternatives have the common asymptotic lower coefficient

\[
\boxed{
b_*:=\sin(c_*/2)=0.0645651571904745\ldots .}
\tag{FP.15}
\]

Indeed `sin(theta_D/2)>=b_*-o(1)`, while `cos(theta_D/2)>=cos(pi/4)-o(1)>b_*` for all sufficiently large `D`.

Hence every `s`-edge common component has actual Euclidean displacement at least

\[
\boxed{
(b_*-o(1))s
}
\tag{FP.16}
\]

in its appropriate two-normal axis.

## 5. Lossless square-root minimax

Choose

\[
s=\sqrt{q/b_*}
\]

up to integer rounding. Combining (FP.11) and (FP.16) gives

\[
\boxed{
\text{either }
\beta(P\cup Q)\ge\sqrt{b_*q}-O(1),
\quad\text{or one common component has two-normal drift }
\ge\sqrt{b_*q}-O(1).
}
\tag{FP.17}
\]

Substituting (FP.10),

\[
\boxed{
\text{COMMON-RUN CURRENCY}
\ge
\left(
\sqrt{\frac{b_*\alpha_K}{2}}-o(1)
\right)
\frac{\sqrt D}{Z_D+1}.
}
\tag{FP.18}
\]

This is the same natural scale

\[
S_D:=\frac{\sqrt D}{Z_D+1}
\]

with no auxiliary slowly diverging denominator.

In particular, if

\[
Z_D=o(\sqrt D),
\tag{FP.19}
\]

then the right side of (FP.18) tends to infinity.

For the concrete choice `K=1`,

\[
\alpha_1=0.6652520156628998\ldots,
\]

so LINEAR-MATCHING gives

\[
\boxed{
(0.0604774559693545\ldots-o(1))D
}
\tag{FP.20}

vertex-disjoint original pairs with length at most `1+1/D`, while PAIR-REUSE gives a fixed run pair with at least

\[
\boxed{
(0.332626007831450\ldots-o(1))
\frac{D}{(Z_D+1)^2}
}
\tag{FP.21}

common distinct edges and therefore

\[
\boxed{
(0.146547093049564\ldots-o(1))
\frac{\sqrt D}{Z_D+1}
}
\tag{FP.22}

bounded-face cycle rank or actual common-trunk Euclidean drift.

## 6. Source-wide fork and frontier effect

Combining this note with the module ANCHORED/FREE dichotomy gives the following proof-only source-wide normal form at any admissible slow scale:

1. **EXACT-BRAID:** a full-order subfamily of tagged actual diameter edges forms the previously proved central crossing braid; or
2. **LINEAR-MATCHING:** the original source contains the linear inverse-`D` matching (FP.7); or
3. **FIXED-PAIR COMMON-RUN:** two FREE modules with normal separation at least `c_*-o(1)` have a lower-run pair satisfying (FP.10), and that run pair obeys the cycle-rank/drift minimax (FP.17)--(FP.18).

Compared with the preceding same-orientation far-pair theorem, the heavy FREE branch improves from

\[
\Omega\left(
\frac{\sqrt D}{(Z_D+1)\omega_D^{5/2}}
\right)
\]

to

\[
\boxed{
\Omega\left(\frac{\sqrt D}{Z_D+1}\right).
}
\tag{FP.23}
\]

The improvement is structural rather than a choice of a faster slow scale: the extreme FREE pair already has a constant normal gap, and the two-module heavy branch consists entirely of edges common to that pair.

This does **not** close C-II. The new claim remains proof-only and is not promoted into the theorem ledger. The unresolved bridge is now cleaner: in the sub-square-root external regime, a surviving FREE branch must produce either a linear inverse-`D` inactive matching or a fixed pair of outer-face inactive lower runs with `Theta(sqrt(D)/(Z_D+1))` cycle-rank/drift currency. A closure still has to convert that currency into the canonical §§122--123 outer-walk/force-hull ledger, an exact unit triangle, or a source-preserving strict diameter decrease.

**Disposition:** selected the extreme FREE modules to obtain a universal normal separation, applied the existing reuse theorem with `m=2,R=1`, retained the entire heavy common-edge population through the lower-run pigeonhole, and optimized the componentwise cycle-rank/two-normal-drift fork. This removes the previous slow-scale and matching losses from the small-external common-run obstruction.