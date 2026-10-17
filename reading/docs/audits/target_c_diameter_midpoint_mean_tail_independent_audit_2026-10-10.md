> Generated reading edition · [exact source](../../../docs/audits/target_c_diameter_midpoint_mean_tail_independent_audit_2026-10-10.md) · source SHA-256 `a815cfd48e4f208a1891b853726897069909704fa0f359dad9f828c12668d797`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-42DB85DAAB5F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C Audit.246 — mean midpoint tails and near-diameter localization

> **Publication lifecycle:** this is an unreviewed proposal from source PR #947.
> Its historical PASS/promote language requests a change; the current publication
> manifest does not grant the proposed promotion or stronger scope. Use the exact
> current manifest entry for any inherited canonical premise.


Date: 2026-10-10\
Audit base: origin/main ab6dd3336f9f8d440f2bada76edb32153391cddc, state 2026-10-10.audit.234\
Frozen source: origin/research/level-i-fused-review-20261009 at 6132201c1d3056ca68a222217094acb819f5b4d7\
Source artifact: Sections 17.1–17.3 of docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md, SHA-256 2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd.

## Verdict

**PASS — promote three scoped full-source geometry claims.**

1. For every noncollinear global minimum-diameter unit-separated source with D>=216, choose one actual diameter partner independently for each actual diameter endpoint. If m_p is the midpoint of that chosen pair and o is a circumcenter of the full-source convex hull, then uniformly over all partner choices,

```math
\#\{p: |m_p-o|\ge s\}\le C D^2/s^2
\quad\text{for }s\ge4\,3^{1/4}\sqrt D,
```

```math
\sum_p|m_p-o|=O(D^{3/2}),\qquad
\sum_p|m_p-o|^2=O(D^2\log D).
```

2. In the canonical C-II source, the same tail and moment estimates hold when the sum and count range over every edge of the full actual diameter graph, with its actual edge midpoints. This uses the canonical Woodall topology only to inject the edges into distinct endpoints.

3. For any two distinct source points p,x with d=|p-x| at least D-s, put ν=(p-x)/d, η=3^{1/4}sqrt(D), and m=(p+x)/2. For every D>=216,

```math
|(p-o)\cdot J\nu|,\ |(x-o)\cdot J\nu|
\le13D^{2/3}+2sD^{1/3},
\qquad
|(m-o)\cdot\nu|\le2\eta+s/2.
```

Thus pairs with bounded diameter deficit have midpoint distance O_s(D^{2/3}) from o. The estimate gives no count of almost-diameter pairs.

The source report's further loaded-leaf anchor conclusion (17.7) is not included: its application through the intersection-of-balls boundary needs a separate audit. None of the promoted claims gives stress-weighted midpoint control, a finite source motion, or a C-II / Level-I closure.

## Independent reconstruction

Let h be the support function of the full-source hull about o, with angular variable θ. The canonical full-source geometry gives

```math
D/2-2\eta\le h\le D/2+\eta,\quad
P\le\pi D,\quad
A(K)>\pi D^2/4-(\sqrt3/4)P,
```

and for D at least 7 the circumradius is at most D. The curvature-measure identity h''+h≥0 therefore gives h''≥-D distributionally. The canonical support-function area identity gives

```math
E:=\int_0^{2\pi}(h')^2
=\int h^2-2A(K)
<\frac{17\pi\sqrt3}{2}D=:C_E D.
```

These are full-source bounds: every point, including contact-isolated points, remains in K. For any actual diameter pair p,p', its normal ν=(p-p')/D strictly exposes p and p'. Indeed,

```math
\nu\cdot(y-p)\le-|y-p|^2/(2D)<0
\quad(y\ne p).
```

So h is differentiable at ν, and for m_p=(p+p')/2,

```math
m_p\cdot J\nu=h'(\nu),\qquad |m_p\cdot\nu|\le\eta.
```

The second inequality follows because h(ν)+h(-ν)=D and each support value is within the displayed full-source interval.

Here is the normal-window count needed below. If a selected set of actual diameter endpoints has chosen midpoint norms at most L, then the number whose strict normals lie in an angular interval of width w≤1/2 is at most C(1+Dw+L), for an absolute C. Order the selected extreme points along the corresponding convex hull arc. Consecutive selected points are at least unit distance apart. Their chords advance by at least cos(w/2) in the central tangent direction. The total tangent projection range is at most D sin(w/2)+2L, since p=m_p+(D/2)ν_p. Dividing gives the claimed count. The argument applies to any selected subset and any independent partner choices.

Fix a≥η and count chosen endpoints for which a≤h'(ν)<2a. Such a normal belongs to an open component of h'>a/2. The total length of these components is at most 4E/a². Each component containing a counted normal contains a value at least a. Since h''≥-D and h' has only upward jumps at polygon side normals, h' stays at least a/2 for the next a/(2D) radians. That component therefore consumes at least a³/(8D) of E. There are at most 8DE/a³ such components. The same length and component estimates hold for negative bands h'<-a/2 by running the semiconvex ramp backwards.

For a counted positive-band endpoint, its midpoint has tangential coordinate below 2a and normal coordinate at most η≤a, hence norm below 3a. For D>=216 the canonical derivative bound |h'|<6D^{2/3}≤D puts every nonempty band in a<D. Subdivide each relevant component arc into windows of width at most δ_a=a/(2D)≤1/2. On one such window, the normal-window count is O(1+Dδ_a+a)=O(a+1). If Λ is the total length of the superlevel components and N_c their number, the total window count is O(DΛ/a+N_c). Therefore the counted band contains

```math
O\bigl((a+1)(D\Lambda/a+N_c)\bigr)
=O\bigl(DE/a^2+(a+1)DE/a^3\bigr),
```

using Λ≤4E/a² and N_c≤8DE/a³. This is bounded by the displayed looser expression C{DE/a²+(a+1)(DE/a³+E/a²)}. With E≤C_E D and a≥η, it is O(D²/a²). The negative bands obey the same estimate. Summing dyadic bands gives

```math
\#\{p:|h'(\nu_p)|\ge a\}\le C D^2/a^2
\quad(a\ge\eta).
```

If |m_p|≥s≥4η, then |h'(ν_p)|²=|m_p|²-(m_p·ν_p)²≥s²-η², so |h'(ν_p)|≥s/2. This proves the midpoint tail. The endpoint set has size at most the hull perimeter, hence at most πD. Also the canonical midpoint bound is |m_p|≤7D^{2/3}. Integrating the endpoint count up to 4η and the tail above 4η yields the first moment O(Dη)+O(D²/η)=O(D^{3/2}). Integrating 2s times the count yields O(Dη²)+O(D² log D)=O(D² log D).

For the C-II edge statement, the canonical Woodall graph is either one odd cycle with pendant leaves or a union of caterpillar trees. Root each tree and assign every edge to its child endpoint. On the odd cycle assign each cycle edge to its head in cyclic order and each pendant edge to its leaf. This is an injection of all actual diameter edges into their endpoints. Choose each assigned endpoint's partner to be the edge assigned to it, and extend the choice arbitrarily to other endpoints. The endpoint tail and moments then dominate the corresponding sums over all edge midpoints.

For the almost-diameter estimate, write the two support deficits as

```math
\delta_p=h(\nu)-(p-o)\cdot\nu,\qquad
\delta_x=h(-\nu)+(x-o)\cdot\nu.
```

They are nonnegative and sum to h(ν)+h(-ν)-d≤D-d≤s, so each is at most s. The canonical derivative estimate makes h 6D^{2/3}-Lipschitz in angle. With ε=D^{-1/3}, let θ be the angular coordinate of ν. Support at the tilted normal gives

```math
(p-o)\cdot\nu\cos\epsilon+
(p-o)\cdot J\nu\sin\epsilon
\le h(\theta+\epsilon).
```

Using (p-o)·ν≥h(ν)-s, h(ν)≤D, |h(θ+ε)-h(θ)|≤6D^{2/3}ε, 1-cos ε≤ε²/2, and sin ε≥ε/2 gives the upper tangent bound 13D^{2/3}+2sD^{1/3}. Tilting by -ε gives the lower bound. Applying the same argument at -ν gives the bound for x. Finally, the support interval above implies |h(ν)-h(-ν)|≤3η. Combining this with δ_p+δ_x≤s gives

```math
|(m-o)\cdot\nu|
\le(3\eta+s)/2
\le2\eta+s/2.
```

## Canonical dependencies

The universal midpoint-tail and near-diameter claims depend directly on C-FS-DIAMETER-MIDPOINT-D2-3, which depends on C-FS-GEOM. The actual-edge transfer additionally uses C-WOODALL for the complete full-source diameter-graph topology. No unreviewed report is a premise.

## Scope checks and disposition

- The tail estimate is uniform over all partner selections; no selected-stress weighting is used.
- Strict supporting normals are checked against the entire source. Contact-isolated points are retained in the hull and the support inequalities.
- The edge statement concerns every edge of the full actual C-II diameter graph. The injection depends on the canonical Woodall classification; no selected-edge graph is substituted.
- Almost-diameter localization does not assert how many such pairs exist.
- No finite verifier encodes the support-energy or asymptotic counting proof. No script or lattice checker is used as evidence.
- The loaded-leaf conclusion (17.7), packet extraction, payment, source motion, and C-II / Level-I closure are not promoted.

**Frontier effect: none.** These are sharper full-source localization bounds. They do not establish the source-compatible capacity or strict-diameter competitor still required by Target C.
