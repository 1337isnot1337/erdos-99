# Hostile audit — exact convex hull of physical pentagon turn vectors

**Date:** 2026-09-19  
**Audited source:** `target_c_pentagon_turn_convex_hull_2026-09-19.md`  
**Verdict:** passes. The conclusion concerns the closed convex hull, not an exact characterization of the nonlinear physical turn set.

## 1. The linear transform is correct

For

\[
q_i=x_i+x_{i+1}-x_{i+3},
\]

the coefficient matrix has determinant one. Direct multiplication verifies

\[
x_i=q_{i+1}-q_{i+2}+q_{i+3}.
\]

Summing either side gives `sum q=sum x`. The exact certificate checks these facts over `Q`.

## 2. The simplex statement is exact

Under `sum x=2`, the inequalities `q_i>=1/3` are equivalent, through the invertible `q` transform, to

\[
t_i=q_i-1/3\ge0,
\qquad
\sum_it_i=1/3.
\]

This is a four-simplex with exactly five vertices. Applying the exact inverse gives the five cyclic rotations of `(0,2/3,1/3,1/3,2/3)`.

No numerical convex-hull computation is used in the theorem.

## 3. Boundary vertices really are physical limits

The approximating family uses directions

\[
\varepsilon,\ \pi-\alpha,\ \pi,\ \pi+\alpha,\ 2\pi-\varepsilon,
\qquad
\cos\alpha=\cos\varepsilon-1/2.
\]

Its vector sum is exactly

\[
2\cos\varepsilon-(1+2\cos\alpha)=0.
\]

For `0<epsilon<pi/6`, the five directions are distinct. The displayed proof of `alpha<pi/3+epsilon` makes the two adjacent sums that converge to `2pi/3` strict on the physical side. The other one-turn and adjacent-turn inequalities are immediate from `pi/3<alpha<pi/2` and positive `epsilon` in the stated interval.

The limiting gap vector is `(2/3,1/3,1/3,2/3,0)`. Cyclic relabeling reaches all simplex vertices.

## 4. Convex-hull logic is one-way where it should be

The source proves

\[
S\subset\operatorname{int}P
\]

from the strict three-gap theorem, and proves that every vertex of `P` lies in `closure(S)`. This is sufficient for

\[
\overline{\operatorname{conv}}S=P.
\]

It does **not** claim that every interior point of `P` is itself a physical equilateral-pentagon turn vector. That would be false dimensionally: local closure is nonlinear and imposes additional equations.

## 5. Meaning of "no stronger linear inequality"

Any affine inequality valid on `S` is valid on `closure(conv S)=P` by continuity and convexity. Therefore it cannot cut `P` beyond the five simplex facets and the affine angle-sum hyperplane. This statement is about affine inequalities in the five local turn coordinates only. It does not preclude stronger nonlinear inequalities, inter-face linear identities, or inequalities involving reciprocal lengths/coordinates.

**Disposition:** the convex-hull theorem is sound and sharply limits the remaining local-linear strategy. C-II remains open.
