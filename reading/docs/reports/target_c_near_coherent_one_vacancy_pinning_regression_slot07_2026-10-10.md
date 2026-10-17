> Generated reading edition · [exact source](../../../docs/reports/target_c_near_coherent_one_vacancy_pinning_regression_slot07_2026-10-10.md) · source SHA-256 `56891e8f8e3af9a64b02d10ee3b7e7387f8d3238008851304a8b8646f5b46c53`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C18D2BBA98D5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: arbitrarily small train variation can pin one-vacancy grids

**Worker:** 07. **Date:** 2026-10-10. **Base:** main `ab6dd3336f9f8d440f2bada76edb32153391cddc`, state `2026-10-10.audit.234`.

**Classification:** regression proved candidate awaiting independent audit. No promotion. C-II and Level I remain open.

## 1. Proposition falsified and its exact scope

The failed extension is:

> A complete embedded grid of unit rhombi sufficiently close to one coherent oblique grid admits a continuous strictification of all interior labels after one interior vacancy, with its complete old boundary fixed.

It fails for arbitrarily small train-angle variation, at arbitrary grid dimensions `m,n>=3`, even though all sites are unit-separated, all cells are nondegenerate unit rhombi, all cell angles are strictly between `pi/3` and `2pi/3`, there are no unit triangles, and the vacancy is a genuine interior label. The punctured grid can be locally isolated in its full pinned lower-constraint space. Therefore no nonconstant continuous fixed-wall motion starts from it.

This does not contradict canonical Audit 195, which requires an exactly coherent parallelogram grid. Nor does it disprove a motion that actually moves the boundary, a disconnected finite replacement, or a source-level endpoint using all actual diameter constraints. The boundary here is simple but generally nonconvex; this is part of the explicit geometry, not an unchanged hypothesis of the coherent theorem. No fixture is a canonical global minimizer.

The implication for the worker-07 route is precise: a source extraction giving merely near-coherent complete train crossings cannot be substituted for exact coherence in the new one-vacancy full-chart release proof. A variable-chart argument must jointly release the wall or supply a different finite replacement.

## 2. Exact parametric construction

Fix `phi in (pi/3,2pi/3)`, put `u=(1,0)`, `v=(c,s)=(cos(phi),sin(phi))`, and choose a sufficiently small `epsilon>0`. Let

```text
u_1=Rot(+epsilon)u,  u_i=u for i>=2,
v_1=Rot(-epsilon)v,  v_j=v for j>=2,
U_0=V_0=0, U_i=sum_{r=1}^i u_r, V_j=sum_{r=1}^j v_r,
x_ij=U_i+V_j, 0<=i<=m, 0<=j<=n.
```

Delete `x_11`, fix all boundary sites `i=0,m` or `j=0,n`, and permit every other retained interior label to move. There are `I=(m-1)(n-1)-1` moving labels.

Choose epsilon so that

```text
phi-2epsilon>pi/3,
4sin(epsilon/2)<sqrt(2-2|c|)-1.
```

Both hold for all sufficiently small positive epsilon at each fixed phi. They also permit `phi` to approach `pi/3` with, for example, `epsilon=(phi-pi/3)^2` once the difference is sufficiently small.

### Actual separation and embedding

For a coherent integer grid, the only unit steps are `+/-u,+/-v`; every other pair has distance at least `d_0=sqrt(2-2|c|)>1`. For both nonzero integer increments `r,t`,

```text
|r u+t v|^2 >= r^2+t^2-2|c||rt|
 = (|r|-|t|)^2+2(1-|c|)|rt| >= 2-2|c|.
```

For a nonbasis increment along just one axis its length is at least two. Between any two deformed sites the displacement differs from the coherent displacement by at most `|u_1-u|+|v_1-v|=4sin(epsilon/2)`. Thus every old nonbasis pair stays strictly greater than one, uniformly in `m,n`. Every basis-neighbor edge remains exactly unit by construction. Consequently the contact graph is precisely the rectangular grid with the chosen label removed; it is bipartite and has no unit triangles.

Each cell is a unit rhombus with angle `phi`, `phi-epsilon`, or `phi-2epsilon`, all in `(pi/3,2pi/3)`. For completeness the cells embed simultaneously. Extend `U,V` linearly on each index interval. A nonzero positive increment of `U` lies in the angular cone `[0,epsilon]`, and a positive increment of `V` lies in `[phi-epsilon,phi]`. These disjoint cones have union in an open half-plane because `phi<pi`. Sums of increments of the same sign cannot vanish; increments of opposite signs cannot cancel because the two cones are disjoint. Hence `(r,t)->U(r)+V(t)` is injective on the entire parameter rectangle. Its boundary is simple and its cells have positive area.

## 3. Strictly positive pinned equilibrium after the vacancy

Define

```text
alpha=sin(epsilon)/s>0,
gamma=sin(phi-epsilon)/s>0.
```

The exact vector identities are

```text
v_1=alpha u+gamma v,
u_1=gamma u+alpha v.
```

Assign weights to every retained unit edge incident to a moving label as follows. Boundary-boundary edges may be discarded.

**Horizontal edges `(i,j)--(i+1,j)`:**

- On row `j=1`, for `2<=i<=m-1`, use `alpha(i-1)`; the edge from the vacancy is absent.
- For `2<=j<=n-1`, use weight one on `i=0`, and weight `gamma` on `1<=i<=m-1`.

**Vertical edges `(i,j)--(i,j+1)`:**

- On column `i=1`, for `2<=j<=n-1`, use `alpha(j-1)`; the edge from the vacancy is absent.
- For `2<=i<=m-1`, use weight one on `j=0`, and weight `gamma` on `1<=j<=n-1`.

Every retained moving-incident unit edge has a strictly positive weight. At a moving label `(i,1)`, `i>=2`, the horizontal force difference is `-alpha u`, and the vertical contribution is `v_1-gamma v`; their sum is zero. At `(1,j)`, `j>=2`, the horizontal contribution is `u_1-gamma u`, and the vertical difference is `-alpha v`; their sum is zero. At `(i,j)` with `i,j>=2`, opposite horizontal weights are both gamma and opposite vertical weights are both gamma, so both cancel.

Thus if `R` is the radial unit-edge matrix restricted to moving columns, its strictly positive weight vector `lambda` obeys `lambda^T R=0`. This is a pinned contact equilibrium, not a normalized full-source contact/diameter KKT stress; forces at pinned boundary labels are unrestricted.

## 4. Full column rank and finite local isolation

Suppose `R delta=0`, with every boundary displacement zero. From any surviving moving label, follow its horizontal unit chain to the right boundary. Every edge on this chain has direction `u`; the exceptional `u_1` edge lies to the left and is not needed. Telescoping gives `u dot delta_ij=0`. Follow its vertical unit chain to the top boundary. Every edge there has direction `v`; the exceptional `v_1` edge lies below and is not needed. Telescoping gives `v dot delta_ij=0`. The vacancy does not meet either selected chain: its row begins at `i>=2` and its column begins at `j>=2`. Since `s>0`, the two projections imply `delta_ij=0`. Therefore `rank(R)=2I`.

In particular a weak first-order direction `R delta>=0` is zero: positive equilibrium makes every row zero, then full column rank kills the displacement. The next estimate proves finite isolation and does not assume a first-order obstruction alone suffices.

Put

```text
lambda_min=min(1,alpha,gamma),
W=sum_e lambda_e
 = alpha*((m-2)(m-1)+(n-2)(n-1))/2
   +(m+n-4)
   +gamma*((n-2)(m-1)+(m-2)(n-1)),
rho=s lambda_min/(2I(m+n)W)>0.
```

Let `delta` be any finite placement displacement of the moving labels, with boundary fixed, satisfying all old unit-contact lower bounds. Each edge gives

```text
L_e=(R delta)_e >= -|delta_p-delta_q|^2/2 >= -||delta||^2.
```

Pinned equilibrium gives `sum_e lambda_e L_e=0`. Therefore

```text
|L_e| <= (W/lambda_min)||delta||^2 = M
```

for every edge. The same horizontal and vertical anchored chains now give `|u dot delta_ij|<=m M` and `|v dot delta_ij|<=n M`. In coordinates `u=(1,0),v=(c,s)`, this implies

```text
|delta_ij| <= |delta_x|+|delta_y|
 <= m M+(n+|c|m)M/s <= 2(m+n)M/s.
```

Summing over the `I` labels and using `sqrt(I)<=I` gives

```text
||delta|| <= 2I(m+n)W ||delta||^2/(s lambda_min).
```

Hence every feasible displacement is zero or has norm at least `rho`. The old punctured source is locally isolated even under just its old contact lower bounds. Adding the remaining nonunit lower bounds, confinement constraints, or diameter upper bounds cannot remove this isolation.

There is therefore no nonconstant continuous fixed-boundary feasible motion starting from the old punctured source. If one existed, continuity would give a displacement norm strictly between zero and rho before its first nonzero displacement of norm at least rho. A disconnected endpoint at distance at least rho is not ruled out.

## 5. Necessary wall-motion rate

The same exact stress also supplies a quantitative moving-wall condition. Let `eta` be the displacement vector of all pinned boundary labels and let `delta` be the interior displacement. Keep the original `R` restricted to moving columns. Unit feasibility and the linear contribution of the boundary give

```text
(R delta)_e >= -(2||eta||+||delta||^2+||eta||^2).
```

Indeed the boundary part of any unit radial row has absolute value at most `sqrt(2)||eta||<=2||eta||`, and half the squared relative displacement is at most `||delta||^2+||eta||^2`. Positive pinned equilibrium bounds the absolute values of all restricted rows by `W/lambda_min` times that right-hand magnitude. The anchored-chain estimate therefore gives

```text
||delta|| <= (2||eta||+||delta||^2+||eta||^2)/rho.
```

If `||delta||<=rho/2` and `||eta||<=1`, absorb the quadratic interior term to obtain

```text
||delta|| <= 6||eta||/rho,
equivalently ||eta|| >= rho ||delta||/6.
```

Thus at fixed positive epsilon every convergent moving-wall motion has interior displacement of order at most its boundary displacement, with an explicit constant. That constant diverges as epsilon tends to zero; this does not supply a uniform phase estimate, obstruct a macroscopic wall move, or establish any diameter payment. The inequality is a necessary full finite lower-constraint condition, not an assertion that its first-order cone integrates.

## 6. Hostile checks and what changes

- At `epsilon=0`, alpha vanishes, strict positivity is lost, and Audit 195's two-stage finite release is possible. This is the exact singular limit; an open stability neighborhood cannot be inferred from the coherent theorem.
- The gap is source-dependent and may shrink to zero with epsilon or with grid size. No uniform asymptotic radius is asserted.
- One vacancy is at `(1,1)` and is interior for every `m,n>=3`. A theorem about every interior vacancy is disproved by this placement; other vacancy positions are not classified here.
- All original cells are genuine unit rhombi and every retained label is modeled. No additional source isolate is removed or treated as part of a kernel.
- The boundary is fixed. A joint actual-source moving-wall strategy remains viable and is the exact next theorem to pursue. The source-normal proof for a coherent wall cannot be transferred without checking its required four-site parallelogram pattern.
- The pinned equilibrium is not a full-source KKT certificate, the fixtures are not globally optimal, and the regression does not settle any global quantifier of Erdős #99.

The meaningful killed implication is `near-coherent grid extraction -> coherent fixed-wall one-vacancy strictification`. The stronger original full-chart moving-wall proof remains valid under its exact-coherence hypotheses, and its last-label restoration remains open.

## 7. Exact verifier

Run `python3 research/verify_target_c_near_coherent_one_vacancy_pinning_slot07_2026_10_10.py`. It passed 48 fixtures: eight acute/right/obtuse base angles, two rational rotation parameters, and dimensions `(3,3),(4,5),(8,6)`. Counts are 40,128 source pairs, 1,808 strictly positive moving-edge weights, 768 exact moving-vertex equilibria, 4,608 anchored-chain rows, 16 independently row-reduced full-column-rank smallest fixtures, and 40,128 smaller-competitor pairs. Its JSON certificate records dimensions, rational rotation parameters, exact equilibrium weights, positive gap bounds, full pair checks, and anchored-chain rank checks. It uses rational and `Q(sqrt(15))` arithmetic and verifies explicit square-grid smaller-diameter competitors for every finite source. The all-dimension regression, finite isolation proof, and moving-wall rate are analytic; finite tests do not establish global optimality or rule out a disconnected replacement or moving-wall endpoint.
