> Generated reading edition · [exact source](../../../docs/reports/target_c_physical_hull_end_capacity_and_high_t_audit_2026-10-03.md) · source SHA-256 `9c1222c7db54a7fa9cb1a489c724a65902236997be4fac60dda07451e8b22535`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F64592A29AAB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — physical hull-end capacity and the high-t hypothesis audit

**Date:** 2026-10-03
**Base:** `7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d`
**State:** `2026-09-14.audit.51`
**Target:** C-II only
**Classification:** proved candidate awaiting promotion; compatibility audit
**Literature/computation:** none
**LEVEL I STATUS: STILL OPEN. C-II remains open.**

## 1. Claim and implication chain

Use a canonical normalized C-II source. All source points, including contact
isolates, remain in the configuration. Let `F` be its strictly convex loaded
force hull, `q` its number of vertices, `P_F=per(F)`, `b=q+x_B` its
occurrence-counted outer contact walk, and `m` its number of nonunit hull
sides. Write `P_exc=4f+Q` for the **global** bounded exceptional-face
perimeter, and `k=d_H+s_Z`, `t_D=(q-k)/D`.

The new finite refinement is

```math
\boxed{P_{exc}\ge q-x_B-2m-4,}\tag{H.1}
```

and hence

```math
\boxed{5t_DD+x_B+m+2\ge3P_F.}\tag{H.2}
```

The Section-61 interval estimate only gives `P_exc>=q-3x_B-4`.
Thus (H.1) improves its right side by `2u_B`, where `u_B=x_B-m`.
The following chain does not reach Level I:

```text
physical hull-end capacity -> same global P_exc and Q ledger
 -> necessary t_D / x_B / m tradeoff
 -> exclude t_D<=1.860+o(1), x_B=o(D), P_F/D->pi
 -> no general C-II conclusion: linear x_B and the container branch survive.
```

The exclusion on the third line is **already a consequence of canonical
Section 61**, as shown in Section 4; it is not claimed as a new theorem.

## 2. Complete finite proof

Use the canonical Section-61 train-link forest on **all contact edges**.
Each strict rhombus links its two opposite edge pairs. Every component is
a path, with singleton contact edges included. Each path has two terminal
face incidences. A singleton has its two incident non-rhombic face
incidences, with distinct occurrences when the edge is a bridge. The exact
identities are

```math
2T=b+P_{exc},\qquad b+Q=2(q-k).\tag{H.3}
```

There are `g=q-m` physical unit hull sides. Such an edge is a contact and
has at least one outer-face incidence, since the entire contact core lies
in `F`. For each such side choose **one** outer incidence as distinguished.
This gives exactly `g` distinguished outer train ends. All other outer
ends number `b-g=x_B+m`. If a hull side is a bridge, its second occurrence
is in this latter count. No occurrence is deleted.

At most two trains have two distinguished ends. A singleton cannot have
two: there is only one distinguished occurrence on its physical edge.
For a nonsingleton, the two terminal hull sides are parallel and occur
with opposite oriented boundary directions. Strict convexity permits
at most one side in each oriented direction. Two distinct such trains
therefore have distinct projective directions and alternating endpoint
pairs on the convex boundary. Their simple midpoint arcs must cross.
Three such trains would give a triangle in the train-intersection graph,
contrary to canonical Section 61.2 / shared Theorem 10.6.

Every other train consumes at least one nondistinguished terminal
incidence. Those incidences comprise `b-g` outer ends and `P_exc`
bounded-face ends. Terminal incidences of different trains are distinct,
so

```math
T-2\le b-g+P_{exc}.\tag{H.4}
```

Substitute `2T=b+P_exc`, rearrange, and use `g=q-m`:

```math
P_{exc}\ge2g-b-4=q-x_B-2m-4.
```

This proves (H.1), including graphs with bridges, repeated face vertices,
disconnected rhombic regions, and no rhombi at all.

Every exceptional bounded face has degree at least five, so `f<=Q` and
`P_exc=4f+Q<=5Q`. By (H.3), `Q=2t_DD-b`. Consequently

```math
5(2t_DD-b)\ge2g-b-4,
```

or

```math
5t_DD\ge 2b+g-2=3q+2x_B-m-2.
```

As `P_F<=b=q+x_B`, this gives (H.2). More precisely its complete
nonnegative-slack identity is

```math
\begin{aligned}
5t_DD+x_B+m+2-3P_F
={}&\tfrac12[P_{exc}-(2g-b-4)]\\
&+2(Q-f)+3(b-P_F)\ge0.
\end{aligned}\tag{H.5}
```

This also checks the finite constants and separates the end, face-degree,
and metric slacks without counting a defect twice.

## 3. Asymptotic consequences and surviving regimes

In the full-core near-disk branch `P_F/D->pi`. Along any sequence with
`t_D->t`, (H.2) gives

```math
\liminf\frac{x_B+m}{D}\ge3\pi-5t.\tag{H.6}
```

In particular `m<=x_B` gives

```math
\liminf\frac{x_B}{D}\ge\frac{3\pi-5t}{2}
\quad\hbox{when }t<3\pi/5.\tag{H.7}
```

At `t<=93/50=1.860`, the right side is at least
`(3pi-93/10)/2=0.06238898038...`. Thus `x_B=O(sqrt(D))` is
incompatible with that endpoint. If `m=o(D)`, (H.6) instead forces the
twice larger floor `x_B/D>=3pi-93/10-o(1)`.

The **new** improvement is finite and most useful when `u_B=x_B-m`
is large. It does not exclude `t>=3pi/5`, nor positive linear
`x_B+m`, nor a macroscopic inactive container. It yields no finite source
motion and makes no claim about the local `sum Q_r^+ +2d_tile` currency.

## 4. Audit of the proposed October collar window

Even without the new refinement, canonical Section 61 gives

```math
q\le3x_B+5Q+4.
```

Substitute `Q=2t_DD-q-x_B` to obtain

```math
5t_DD\ge3q+x_B-2\ge3P_F-2x_B-2.\tag{H.8}
```

Therefore the simultaneous assumptions

```math
P_F/D\to\pi,\quad x_B=O(\sqrt D),\quad
t_D\le1.860+o(1)
```

are already impossible in the canonical source. Indeed (H.8) gives
`liminf t_D>=3pi/5>93/50`. The strict comparison needs no decimal:
`pi>157/50` gives `3pi/5>471/250>465/250=93/50`.

This applies to the **stated specialization** of the October high-t fan,
boundary collar, good-end charge, and augmented-defect reports. Their
finite fan/collar inequalities are not refuted; the displayed positive
asymptotic populations in that jointly assumed parameter window have
an empty antecedent. The correct closing task cannot use those
populations as a nonempty canonical branch. No canonical claim or
manifest entry needs rejection: those reports are unpromoted.

## 5. Dependencies, novelty and hostile checks

- Canonical `C-LINEAR-NONMATCH`,
  [Section 61](../targets/target-c/61-linear-nonmatching-excess-audit.md):
  exact train forest, terminal occurrences, crossing restriction, and
  `b+Q=2(q-k)`.
- Canonical `C-LOADED-HULL`,
  [Section 63](../targets/target-c/63-loaded-hull-slack-audit.md):
  actual loaded hull, `P_F<=b`, and `0<=m<=x_B`.
- [Shared Theorem 10.6](../theory/01-local-structure.md): strict-rhombus
  midpoint arcs and triangle-free train crossing graph.
- The [September 25 surplus tradeoff](target_c_outerwalk_surplus_mu_tradeoff_2026-09-25.md)
  is an unpromoted predecessor. Its underlying canonical end estimate
  is rederived here; neither its report status nor its other conclusions
  is used as a premise.

Targeted searches found the coarse `q<=3x_B+5Q+4` and its `mu_D`
tradeoff. The refinement replaces bad *interval* occurrences by the
exact complement of all distinguished physical unit hull sides.
Only this `m`-sensitive refinement is claimed as new.

Bridges are counted twice as facial incidences and once as a physical
side; a singleton bridge cannot become a two-distinguished-ended train.
The regular odd shell has no rhombi, but its singleton side trains end
on the exceptional interior face, so the charge still holds. Convex
square-grid boundary vertices with collinear intermediate points cannot
all be declared loaded extreme vertices. Neither a shear floor, a KKT
multiplier floor, an Euler diameter traversal, nor a full-source affine
kernel is assumed. No finite deformation or source deletion occurs.

## 6. Disposition and next obligation

Preserve (H.1)--(H.5) as a proved candidate awaiting independent promotion
audit. Preserve (H.8) as a compatibility audit of the current proposed
research window. The canonical state stays unchanged.

The remaining full-core obligation is genuinely in the linear outer-walk
regime or at `t>=3pi/5`; it requires an actual-source payment or a finite
strict move. The open-cell phase-flux branch must be inspected under
its own hypotheses, without importing the empty collar specialization.
