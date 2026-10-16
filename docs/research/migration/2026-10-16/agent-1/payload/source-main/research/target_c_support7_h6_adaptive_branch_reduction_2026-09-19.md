# Target C: generic H6 adaptive-branch reduction to 4,944 cells

Date: 2026-09-19

Status: exact finite reduction inside the generic H6 branch. The theorem-state authority is unchanged. C-II remains open.

## Result

The committed generic H6 endpoint before this step is

\[
4976=3972\,C_7+1004\,(C_3\sqcup C_4).
\]

Retaining the full physical-pentagon order/median disjunction and the exact branch-adaptive closure secants excludes 32 additional cells:

\[
\boxed{4976\longrightarrow4944}
\]

with

\[
\boxed{4944=3940\,C_7+1004\,(C_3\sqcup C_4).}
\]

All 32 new exclusions are `C7` missing-graph cells. No `C3+C4` cell is removed at this layer.

The remaining ground-pattern census is

```text
145      4
156     16
235    674
236   1282
237     16
245    484
256   1282
345     24
346    484
347      4
356    674
```

These counts sum to 4,944.

## Local branch system

Fix one physical pentagon face and one of the ten admissible cyclic gap orders

\[
x_a\le x_b\le x_c\le x_d\le x_e.
\]

Unlike the previous order-hull reduction, do not convexify across the median threshold. Keep both closed branches

\[
x_c\le\frac25
\qquad\text{and}\qquad
x_c\ge\frac25.
\]

The equality case is contained in both branches, so the two branches cover the complete order cone.

On each branch use the five rank-specific rational secants proved in `target_c_pentagon_branch_adaptive_secants_2026-09-19.md` and checked by `verify_target_c_pentagon_branch_adaptive_secants_2026_09_19.py`.

For the median-low branch the rankwise upper lines for the sharp two-gap closure function `M` are

\[
\begin{aligned}
M(x_a)&\le \frac23+\frac{x_a}{3},\\
M(x_b)&\le \frac{214257}{400000}x_b+\frac{585743}{1000000},\\
M(x_c)&\le \frac{115689}{200000}x_c+\frac{284311}{500000},\\
M(x_d)&\le \frac12+\frac{3x_d}{4},\\
M(x_e)&\le \frac12+\frac{3x_e}{4}.
\end{aligned}
\]

For the median-high branch they are

\[
\begin{aligned}
M(x_a)&\le \frac{387939}{1000000}x_a+\frac{1612061}{2500000},\\
M(x_b)&\le \frac{325671}{700000}x_b+\frac{1074329}{1750000},\\
M(x_c)&\le \frac{67191}{100000}x_c+\frac{132809}{250000},\\
M(x_d)&\le \frac{144043}{200000}x_d+\frac{255957}{500000},\\
M(x_e)&\le \frac12+\frac{3x_e}{4}.
\end{aligned}
\]

Thus one physical face has twenty closed local branches: ten admissible gap orders times two median sides. A generic H6 cell is impossible if all twenty branches at one face contradict the global 85-variable complete-angle system.

## Discovery census

The exhaustive numerical discovery pass over the 4,976-cell endpoint was split into four chunks. It inspected 121,297 branch LPs with zero solver failures. Early exit was used as soon as one branch at a face had positive common strict margin.

Exactly 32 cells had a physical face for which all twenty branches had nonpositive numerical margin. Their witness-face counts are

```text
face 2   14
face 4   14
face 6    2
face 7    2
```

Their ground-pattern counts are

```text
145    2
236    4
245   10
256    4
346   10
347    2
```

The numerical scan is only candidate discovery. The reduction does not depend on accepting a floating-point infeasibility result.

## Exact certificate layer

`verify_target_c_support7_h6_adaptive_branch_reduction_2026_09_19.py` checks the 32 discovered cells independently against the committed state ordering and the previous order-hull rule. For each cell it then exactifies every one of the twenty adaptive branches at the witness face.

There are

\[
32\cdot20=640
\]

exact rational Farkas certificates. Of these, 480 have a strictly negative forced constant and 160 have forced constant exactly zero. The largest denominator among accepted active dual coefficients is

\[
41150022497377.
\]

The LP dual is used only to guess an active support. For acceptance, the verifier solves on that support over `fractions.Fraction` and then checks all of the following exactly:

- every multiplier on a strict or closed inequality is nonnegative;
- the weights on the original strict facets sum to one;
- the weighted variable coefficients cancel in all 85 variables;
- equality multipliers are unrestricted;
- the resulting forced constant is nonpositive.

Because the normalized strict contribution is strictly positive while all added order, median, and secant facets are closed and nonnegative, a forced constant `<=0` is impossible for a feasible branch. Therefore all twenty branches at the witness face are impossible, and so is the cell.

## What this does and does not prove

This is another necessary-condition reduction. It does not prove any of the remaining 4,944 generic H6 cells are geometrically realizable, and it does not address the reciprocal-collinearity walls outside the generic branch.

The one-face affine disjunction is now close to saturation. The next finite layer should combine local branches from two or more physical faces. For a fixed pair of faces, first exact-certify locally impossible one-face branches, then test only the surviving Cartesian branch products. A cell dies when every product branch is covered by either a one-face certificate or a two-face exact Farkas certificate. This avoids a blind `20^7` enumeration.

After the affine branch-and-bound layer is exhausted, the remaining cells still have to satisfy the fifteen independent complete reciprocal sine-law metric consistency equations. Those nonlinear metric equations are the next qualitatively different obstruction if multi-face affine branching stops producing useful cuts.
