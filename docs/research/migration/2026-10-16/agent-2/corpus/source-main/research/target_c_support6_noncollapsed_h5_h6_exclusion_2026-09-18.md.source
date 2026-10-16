# Target C-II — noncollapsed degree-pure support-six blocks are impossible

**Date:** 2026-09-18  
**Status:** proved candidate; theorem-state authority unchanged  
**Scope:** a degree-pure six-face one-anchor component with relation graph `K_6` minus a perfect matching, excluding the collapsed dual-value branch  
**Depends on:** the one-anchor support-six reciprocal construction; `target_c_reciprocal_source_gap_forces_convex_hexagon_2026-09-18.md`; `target_c_support6_reciprocal_h6_exclusion_2026-09-18.md`  
**Certificate:** `research/verify_target_c_support6_noncollapsed_h5_h6_exclusion_2026_09_18.py`  
**Classification:** proved candidate awaiting independent promotion; C-II remains open

The degree-pure support-six one-anchor endpoint has relation graph

\[
R=K_6\setminus M,
\]

with `M` a perfect matching. In the noncollapsed branch, the six non-ground dual
vectors are distinct and, after adding the common zero outer value, produce a signed
unit-force equilibrium on

\[
H=K_7\setminus M.
\]

The noncollapsed branch is impossible:

\[
\boxed{\text{a degree-pure support-six block is either collapsed or does not exist}.}
\]

## 1. Metric H5 exclusion

At any non-ground reciprocal hull vertex, the five raw reciprocal rays lie in the
interior cone of hull angle `phi<pi`. The source contact pentagon supplies the strict
force-direction gap

\[
\delta<2\pi/3
\]

between every pair of consecutive force sides.

Assume the local sign split is `2+3` and suppose `phi<=2pi/3`. Reverse all signs if
needed and rotate so the two same-sign raw rays have arguments `-p,p`, with
`0<p<pi/3`. Write the other three raw arguments as `a<b<c`, choosing lifts in the
same cone. Their resultant equation is

\[
e^{ia}+e^{ib}+e^{ic}=2\cos p.
\tag{1}
\]

With `s=(a+c)/2` and `d=(c-a)/2`, the two force gaps separating the positive cluster
from the antipodal negative cluster are

\[
\pi+a-p,
\qquad
\pi-p-c.
\]

The strict source gap gives

\[
d>\pi/3-p+|s|.
\tag{2}
\]

On the other hand, taking the modulus of
`e^{ib}=2 cos(p)-2 cos(d)e^{is}` gives

\[
4\cos^2p+4\cos^2d-8\cos p\cos d\cos s=1.
\tag{3}
\]

Set `u=pi/3-p` and `v=pi/3-d`. Under the assumed cone bound, `u,v>=0`; under (2),
`p+d>pi/3`. Substitution of (3) gives the exact identity

\[
8\cos p\cos d
\left[\cos(p+d-\pi/3)-\cos s\right]
=8\cos(u+v)\sin u\sin v\ge0.
\tag{4}
\]

Since `0<=|s|<pi` and `0<=p+d-pi/3<pi`, (4) implies

\[
|s|\ge p+d-\pi/3,
\tag{5}
\]

contradicting the strict reverse inequality in (2). Therefore every non-ground hull
angle is strictly larger than `2pi/3`.

The signed unit-force equilibrium also gives every hull angle strictly larger than
`arccos(-1/4)>pi/2`. If the reciprocal hull had five vertices, then either all five
were non-ground, giving angle sum `>10pi/3`, or the ground vertex was on the hull,
giving angle sum `>8pi/3+pi/2=19pi/6`. Both contradict the pentagon angle sum `3pi`.
Thus the H5 branch is impossible, without numerical solving or order-type enumeration.

## 2. Exact H6 exclusion

The only remaining noncollapsed reciprocal hull is a strictly convex hexagon. The exact
H6 certificate exhausts the 26 uniform rank-three extensions of a convex hexagon by the
ground sign word, all perfect matchings, and all local `2+3` alternation phases. It
finds no compatible signing:

\[
26\text{ uniform order types},\qquad 0\text{ compatible signings}.
\]

The certificate also checks the 14 possible simple ground-collinearity walls, although
such walls are not part of a strictly convex hexagon; none survives either. No
floating-point geometry is used in this finite step.

Therefore the noncollapsed H6 branch is excluded as well.

## 3. Propagation and exact remaining obstruction

The dependency chain is

\[
\text{one-anchor support six}
\to
\text{collapsed/noncollapsed reciprocal dichotomy}
\to
\text{H5 or H6 in the noncollapsed branch}
\to
\text{H5 angle-sum contradiction or exact H6 enumeration}
\to
\text{collapsed branch only}.
\]

This does not yet improve the universal one-anchor coefficient from `n_1/6` to
`n_1/7`, because the certified collapsed six-face local closure remains viable. Such
an improvement requires a global exclusion of the collapsed branch, or a theorem that
turns its regular local two-parameter family into an actual diameter-unlocking motion.

No theorem-state file is changed.

**Disposition:** excluded the complete noncollapsed support-six reciprocal endpoint;
the collapsed six-face branch is now the smallest remaining one-anchor obstruction.
