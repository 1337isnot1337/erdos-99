> Generated reading edition · [exact source](../../research/target_c_inactive_contact_wall_repacking.md) · source SHA-256 `77aeb1e873bbf51e00aefa76fbea88dd7bad04eb558e08af71a95b9d5045057c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — contact-wall repacking for an internal inactive face

**Date:** 2026-09-12  
**Status:** proof-only research candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note strengthens the proof-only diameter-vertex-cover repacking route for the
case in which the macroscopic inactive chamber is an **internal bounded
nonquadrilateral contact face**.

The current repacking theorem works in the full inner parallel body `C_{-1}`. The
unit collar is used only to guarantee that newly inserted points stay unit-separated
from source points outside the chamber. For a bounded contact face that collar is
unnecessary: its boundary is a closed chain of actual unit contacts, and those unit
edges form an exact geometric barrier.

The resulting criterion is finite and source-preserving. A replacement packing need
only be unit-separated from the face boundary vertices; it need not stay one unit away
from the geometric boundary. This changes the internal inactive branch from an
eroded-body capacity problem to a fixed-boundary packing-extension problem.

The note also identifies the exact residual capacity currency. If the face has `m`
unit boundary edges, area `A_C`, and `z_C` assigned contact-isolated source points,
then

$$
 r_\partial(C):={A_C\over a_0}-{m\over2}+1-z_C\ge0,
 \qquad a_0={\sqrt3\over2}.
$$

If

$$
 \sigma_C={A_C\over a_0}+{m\over2}+1-z_C
$$

is the isolate-only Oler slack used in the chamber ledger, then

$$
 \boxed{r_\partial(C)=\sigma_C-m.}
$$

Thus the full perimeter term in `sigma_C` is not free spare capacity: the prescribed
unit boundary itself consumes exactly `m` units of Oler slack.

---

## 1. Setup

Let `A` be the canonical triangle-free global diameter minimizer, with

$$
 |A|=n,\qquad \min_{x\ne y}|x-y|\ge1,\qquad \operatorname{diam}A=D=D(n).
$$

Let `K=conv(A)` and let `H` be the complete actual diameter graph.

Let `C` be one bounded nonquadrilateral face of the positive contact graph used as an
inactive chamber in canonical Section 77. Canonical face convexity gives

$$
 C=\operatorname{conv}\{p_1,\ldots,p_m\},
$$

where the boundary is a simple convex polygon and

$$
 |p_i-p_{i+1}|=1
$$

cyclically. Hence

$$
 \operatorname{per}(C)=m.
\tag{1.1}
$$

Let

$$
 Z_C=A\cap\operatorname{int}C,
 \qquad z_C=|Z_C|.
$$

In the canonical inactive-face assignment, every point in `Z_C` is contact-isolated,
and every source point not in `Z_C` lies outside `int C`.

Because `C` is a bounded face of the positive contact graph, `int C` lies in the
interior of the force hull and hence in `int K`.

---

## 2. A unit contact edge is an exact crossing barrier

### Lemma 2.1 — two-endpoint crossing barrier

Let `p,q,x,y` be planar points with

$$
 |p-q|=1,
 \qquad |x-p|\ge1,
 \qquad |x-q|\ge1,
 \qquad |x-y|<1.
$$

If the open segments `xy` and `pq` cross properly, then

$$
 |y-p|<1,
 \qquad |y-q|<1.
\tag{2.1}
$$

#### Proof

Let `r` be the crossing point. Since `r` lies on both segments,

$$
\begin{aligned}
 |x-p|+|y-q|
 &\le |x-r|+|r-p|+|y-r|+|r-q|\\
 &=|x-y|+|p-q|<2.
\end{aligned}
$$

The first term on the left is at least one, so `|y-q|<1`. Interchanging `p,q`
gives `|y-p|<1`. `square`

This is the same Euclidean crossing inequality used by the audited contact-edge lens
shield; no response-lattice hypothesis is used.

---

## 3. The whole boundary cycle shields the face interior

### Theorem 3.1 — contact-wall shield

Let `y in int C` satisfy

$$
 |y-p_i|\ge1
 \qquad(1\le i\le m).
\tag{3.1}
$$

Let `x` be any source point outside `int C`. Then

$$
 \boxed{|x-y|\ge1.}
\tag{3.2}
$$

#### Proof

If `x` is one of the boundary vertices `p_i`, (3.2) is exactly (3.1). Assume now that
`x` is distinct from every boundary vertex. Source unit separation gives

$$
 |x-p_i|\ge1
\tag{3.3}
$$

for all `i`.

Suppose for contradiction that `|x-y|<1`. Follow the segment from `y` toward `x` and
let `r` be its first point on `partial C`.

If `r=p_i` is a boundary vertex, then `p_i` lies strictly between `x` and `y`, so

$$
 |x-y|=|x-p_i|+|p_i-y|\ge2,
$$

contradicting `|x-y|<1`.

Otherwise `r` lies in the relative interior of one boundary edge
`[p_i,p_{i+1}]`. Because `C` is convex and `y` lies in its interior, the segment
`xy` crosses that supporting edge properly at `r`. Lemma 2.1, applied with the
outside endpoint `x`, gives

$$
 |y-p_i|<1,
 \qquad |y-p_{i+1}|<1,
$$

contradicting (3.1). `square`

### Corollary 3.2 — simultaneous wall shield

Let `Y subset int C` be unit-separated and suppose

$$
 |y-p_i|\ge1
 \qquad(y\in Y,\ 1\le i\le m).
\tag{3.4}
$$

Then every point of `Y` is unit-separated from every source point outside `int C`.
Thus, after removing the original chamber interior population, the only
unit-separation checks for a replacement in `C` are pairwise distances in `Y` and
distances from `Y` to the boundary vertices.

---

## 4. Fixed-boundary packing capacity

For an integer `N`, say that `C` has fixed-boundary capacity at least `N` if there is
an `N`-point set `Y subset int C` with

$$
 |y-y'|\ge1,
 \qquad |y-p_i|\ge1.
\tag{4.1}
$$

Write `M_partial(C)` for the supremum of such integers. This existential definition
avoids an irrelevant compactness issue caused by the open set `int C`.

The original isolate set is admissible because its points are contact-isolated, so

$$
 M_\partial(C)\ge z_C.
\tag{4.2}
$$

Let `U` be any vertex cover of the complete actual diameter graph `H`. Suppose

$$
 M_\partial(C)\ge z_C+|U|.
\tag{4.3}
$$

Choose an admissible `Y` of that size and define

$$
 A':=(A\setminus(Z_C\cup U))\cup Y.
\tag{4.4}
$$

### Theorem 4.1 — contact-wall cover repacking

Under (4.3),

$$
 \boxed{
 |A'|=|A|,
 \qquad \min_{a\ne b\in A'}|a-b|\ge1,
 \qquad \operatorname{diam}A'<D.
 }
\tag{4.5}
$$

Hence (4.3) is impossible in a global minimizer.

#### Proof

No point of `Z_C` is a diameter endpoint: `Z_C subset int K`, and the strict interior
diameter lemma gives distance `<D` from each of its points to every point of `K`.
Hence `Z_C` and `U subset V(H)` are disjoint, so (4.3) makes (4.4)
cardinality-preserving.

Retained old points remain mutually unit-separated. The new set `Y` is unit-separated
by definition. Every retained old source point lies outside `int C`; Corollary 3.2
gives unit separation between every new point and every retained old point.

Because `U` is a vertex cover of the complete diameter graph, every retained old-old
pair has distance strictly below `D`.

Every new point lies in `int C subset int K`. For every `x in K` and `y in int K`,

$$
 |x-y|<D.
\tag{4.6}
$$

Indeed `K subseteq closed B(x,D)` and an interior point of `K` cannot lie on the
boundary circle of that disk. Thus every new-old and new-new distance is strictly
below `D`. Since `A'` is finite, its maximum pair distance is strictly below `D`,
contradicting the definition of `D(n)`. `square`

The competitor is not required to be triangle-free.

Taking `U` to be a minimum vertex cover gives the exact survivor condition

$$
 \boxed{M_\partial(C)-z_C<\tau(H).}
\tag{4.7}
$$

The audited Woodall argument gives

$$
 \tau(H)\le\left\lceil{q\over2}\right\rceil\le {\pi D\over2}+1.
\tag{4.8}
$$

Compared with the existing protected-cover theorem, (4.7) replaces the capacity of
`C_{-1}` by the fixed-boundary capacity of the full face and removes the full
one-unit collar from the separation argument.

---

## 5. Exact Oler boundary credit

The boundary vertices and assigned isolates are all original source points, so

$$
 P_C\cup Z_C,
 \qquad P_C:=\{p_1,\ldots,p_m\},
$$

is unit-separated, with convex hull exactly `C`. Finite Oler gives

$$
 z_C+m\le {A_C\over a_0}+{m\over2}+1,
\tag{5.1}
$$

where `A_C=area(C)`. Hence

$$
 \boxed{z_C\le {A_C\over a_0}-{m\over2}+1.}
\tag{5.2}
$$

Define the isolate-only chamber slack from Section 77 by

$$
 \sigma_C:={A_C\over a_0}+{m\over2}+1-z_C.
\tag{5.3}
$$

Then

$$
 \boxed{\sigma_C\ge m.}
\tag{5.4}
$$

The residual

$$
 \boxed{
 r_\partial(C)
 :=\sigma_C-m
 ={A_C\over a_0}-{m\over2}+1-z_C
 \ge0
 }
\tag{5.5}
$$

is the Oler slack of the full face source set `P_C union Z_C`.

For every admissible replacement `Y`, `P_C union Y` is also unit-separated in `C`, so

$$
 |Y|\le {A_C\over a_0}-{m\over2}+1.
\tag{5.6}
$$

Consequently

$$
 \boxed{
 0\le M_\partial(C)-z_C\le r_\partial(C)=\sigma_C-m.
 }
\tag{5.7}
$$

Thus the entire isolate-only Oler slack `sigma_C` cannot be interpreted as possible
repacking spare: `m` units are already forced by the prescribed unit contact boundary.
A capacity proof through this route must use the residual `r_partial`, not `sigma_C`.

---

## 6. Aggregate consequence for internal exceptional faces

Let the bounded nonquadrilateral faces be `C_j`, with degrees `m_j`, assigned isolate
counts `z_j`, and residuals `r_partial(C_j)`. Their total boundary length is

$$
 \sum_jm_j=4f+Q.
\tag{6.1}
$$

Applying (5.4) face-by-face gives

$$
 \boxed{
 \sum_{j\in\mathrm{exc}}\sigma_j\ge4f+Q.
 }
\tag{6.2}
$$

Equivalently,

$$
 \sum_{j\in\mathrm{exc}}r_\partial(C_j)
 =\sum_{j\in\mathrm{exc}}\sigma_j-(4f+Q)\ge0.
\tag{6.3}
$$

This is the face-level boundary credit hidden in the canonical exceptional-face Oler
ledger. It does not by itself force positive spare capacity.

---

## 7. Scope and exact remaining obstruction

The theorem removes one genuine loss from the inactive-container route, but it does
not close the branch.

- It applies directly to an internal bounded exceptional face. A convex outer pocket
  has an artificial force-hull chord on part of its boundary, so the closed unit-wall
  argument does not apply across that chord without an additional shield or collar.
- `M_partial(C)` is a non-strict packing capacity. Contact-minimality does not imply
  that it exceeds the current isolated population; a maximum-cardinality packing can
  lie on an integer plateau while admitting a strictly separated representative.
- Equation (5.7) is an upper bound on spare capacity, not a lower bound. No claim
  reverses Oler.
- No contact-isolated point is inserted into the Section-57 affine-kernel theorem.
- Every deleted source point is replaced in (4.4).
- The direct competitor may contain unit triangles; this is allowed because global
  diameter minimality supplies the contradiction.

The exact internal-face handoff is:

> Prove `M_partial(C)-z_C >= tau(H)` for one canonical macroscopic exceptional face,
> or prove a smaller multi-vertex exchange using the same contact-wall shield. The
> available Oler currency is `r_partial(C)=sigma_C-m`, not the coarse `sigma_C`.

A successful continuation must use global minimality, active diameter topology, or
additional structure of the near-capacity inactive packing. Oler density alone is
insufficient.
