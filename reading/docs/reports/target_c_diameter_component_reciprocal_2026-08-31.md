> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_component_reciprocal_2026-08-31.md) · source SHA-256 `be1853b0c0ea541e74bd3b6e90cb5e547fdb41d1856764bdd213a3d7e29a2ffe`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4E7BF3E3D90F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: diameter-component reciprocal decomposition

**Date:** 2026-08-31  
**Run type:** proof / exact convex decomposition  
**Target:** C-II  
**Depends on:** Target C reciprocal force polygon, C18 diameter-angle gap, and C24 diameter-class stress  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The full diameter components introduced in C23--C24 also decompose the reciprocal
force polygon.  For a relative-interior C-II stress, every contact-component endpoint
of the full diameter graph is a positive reaction vertex.  Group the reciprocal side
vectors `J g_b` by the connected component of the full diameter graph containing
`b`.  Each group has zero vector sum and retains the global cyclic order, so it closes
to a convex reciprocal subpolygon.  The global reciprocal polygon is the Minkowski
sum of these component polygons.

The decomposition is exact at the mixed-area level.  If `beta_Q` is the total positive
KKT diameter mass carried inside full-diameter component `Q`, then

$$
\boxed{2V(F,F_Q^*)=D^2\beta_Q.}
$$

After rescaling `F_Q^*` by `1/beta_Q`, every component has the same mixed area
`D^2/2` with the force hull.  Its perimeter lies in the same narrow global interval
between the C18 angle bound and the matching endpoint.  Thus the global reciprocal
polygon is a Minkowski barycenter of independently normalized component responses.

This does not yet contradict the matching-like near-disk escape: a full diameter
component may connect several positive matching edges using KKT-weak diameter chords.
The theorem isolates that escape exactly.

---

## 1. Setup and diameter-component weights

Work in the C-II branch and choose a relative-interior normalized KKT stress.  Then
`C_+=C`, `H_+=H_*`, and
$$
F=\operatorname{conv}V(C)=\operatorname{conv}B_+
\tag{C25.1}
$$
for this same stress.  For `b in B_+`, put
$$
g_b=\sum_{bk\in H_+}\beta_{bk}(b-k).
\tag{C25.2}
$$
The reciprocal polygon `F^*` has side vectors
$$
e_b=Jg_b
\tag{C25.3}
$$
in the cyclic order of the force-hull vertices.

Let
$$
\mathscr D=\{Q_1,\ldots,Q_c\}
\tag{C25.4}
$$
be the connected components of the **full** diameter graph that meet the contact
component `V`.  C24.1 says precisely that
$$
B_+=V\cap V(H),
\tag{C25.5}
$$
so the nonempty sets
$$
B_Q=B_+\cap Q
\tag{C25.6}
$$
partition `B_+`.

Every positive diameter edge belongs to one full-diameter component.  Define
$$
\boxed{
\beta_Q
=\sum_{h\in H_+,\ h\subset Q}\beta_h.
}
\tag{C25.7}
$$
Since every `b in B_+` is incident with a positive diameter edge, every
`Q in mathscr D` has `beta_Q>0`, and normalization gives
$$
\boxed{
\sum_{Q\in\mathscr D}\beta_Q=1.
}
\tag{C25.8}

---

## 2. Each diameter component closes its own reciprocal polygon

### Lemma C25.1 (component resultant vanishes)

For every `Q in mathscr D`,
\[
\boxed{
\sum_{b\in B_Q}g_b=0.
}
\tag{C25.9}

#### Proof

Use the diameter formula (C25.2).  Every positive diameter edge with one endpoint in
`B_Q` has its other endpoint in the same full-diameter component `Q`; the two endpoint
contributions are opposite and cancel. `\square`

The directions of the global reciprocal side vectors `e_b=Jg_b` are strictly cyclic,
because `g_b` lies in the relative interior of the outward normal cone of `F` at `b`.
A subsequence indexed by `B_Q` therefore retains cyclic order.

### Theorem C25.2 (component reciprocal polygon)

For every `Q in mathscr D`, the vectors
\[
\{e_b=Jg_b:b\in B_Q\}
\tag{C25.10}
$$
in their inherited cyclic order are the side vectors of a convex polygon
`F_Q^*`, unique up to translation.  The polygon may be degenerate to a segment when
`|B_Q|=2`.

Moreover, up to translation,
$$
\boxed{
F^*=\sum_{Q\in\mathscr D}F_Q^*
}
\tag{C25.11}
$$
where the right side is Minkowski addition.  In particular
$$
\boxed{
P_*=\sum_Q P_Q^*,
\qquad
P_Q^*=\operatorname{per}(F_Q^*)=\sum_{b\in B_Q}|g_b|.
}
\tag{C25.12}

#### Proof

Lemma C25.1 gives zero vector sum.  The inherited edge directions are cyclically
ordered, so the closed polygonal chain is convex; with two antiparallel vectors it is
the standard degenerate segment case.

For planar convex polygons, the cyclic edge-vector sequence of a Minkowski sum is the
merge of the cyclic edge-vector sequences of the summands, with co-directed edges
added.  Here the global reciprocal edge directions are distinct because the vectors
`g_b` lie in disjoint relative interiors of the force-hull vertex normal cones.  The
component edge sequences partition the global sequence.  Their Minkowski merge is
therefore exactly the edge sequence of `F^*`, proving (C25.11).  Perimeter additivity
follows directly from the disjoint edge partition. `\square`

Thus the full-diameter connectivity classes are literal Minkowski summands of the KKT
reciprocal geometry.

---

## 3. Componentwise mixed-area identity

### Theorem C25.3 (diameter mass = component mixed area)

For every `Q in mathscr D`,
\[
\boxed{
2V(F,F_Q^*)
=
\sum_{b\in B_Q}b\cdot g_b
=
D^2\beta_Q.
}
\tag{C25.13}

#### Proof

The side of `F_Q^*` indexed by `b` has vector `Jg_b`, length `|g_b|`, and outward
normal `g_b/|g_b|`.  This normal supports `F` uniquely at `b`.  The polygonal mixed
area formula therefore gives
\[
2V(F,F_Q^*)
=
\sum_{b\in B_Q}|g_b|
 h_F\!\left(\frac{g_b}{|g_b|}\right)
=
\sum_{b\in B_Q}b\cdot g_b.
\tag{C25.14}
$$
Group the last sum by positive diameter edges inside `Q`.  An edge `bk` contributes
$$
\beta_{bk}\bigl[b\cdot(b-k)+k\cdot(k-b)\bigr]
=
\beta_{bk}|b-k|^2
=
D^2\beta_{bk}.
\tag{C25.15}
$$
Summing over `H_+ cap Q` proves (C25.13). `\square`

Summing C25.13 over all components recovers the global identity
`2V(F,F^*)=D^2` by mixed-area linearity and (C25.8), as it must.

Define the normalized component polygon
$$
\widetilde F_Q^*=\beta_Q^{-1}F_Q^*.
\tag{C25.16}
$$
Then
$$
\boxed{
2V(F,\widetilde F_Q^*)=D^2
}
\tag{C25.17}
$$
for **every** full-diameter component, while
$$
\boxed{
F^*=\sum_Q\beta_Q\widetilde F_Q^*.
}
\tag{C25.18}

Thus the global reciprocal is a Minkowski barycenter of component responses all lying
on the same mixed-area level set.

---

## 4. Every component obeys the global force-perimeter interval

Let `Theta(D)` denote the finite shared-endpoint diameter-angle upper bound from C18,
truncated at `pi/3` when the explicit bound is weaker than the elementary one.  For
`b in B_+`, put
\[
s_b=\sum_{bk\in H_+}\beta_{bk}.
\tag{C25.19}
$$
All vectors `b-k` in (C25.2) have length `D` and lie in an angular interval of width at
most `Theta(D)`.  Projection onto the interval bisector gives
$$
|g_b|
\ge
D\cos\frac{\Theta(D)}2\,s_b,
\tag{C25.20}
$$
while the triangle inequality gives `|g_b|<=Ds_b`.

Since every positive diameter edge in `Q` is counted at both endpoints,
$$
\sum_{b\in B_Q}s_b=2\beta_Q.
\tag{C25.21}
$$
Hence:

### Theorem C25.4 (component perimeter interval)

For every full-diameter component,
$$
\boxed{
2D\beta_Q\cos\frac{\Theta(D)}2
\le
P_Q^*
\le
2D\beta_Q.
}
\tag{C25.22}

Equivalently, every normalized response obeys
\[
\boxed{
2D\cos\frac{\Theta(D)}2
\le
\operatorname{per}(\widetilde F_Q^*)
\le
2D.
}
\tag{C25.23}

As `D->infinity`, the lower coefficient tends to
\[
2\cos\left(\frac{5\pi}{12}-\frac{\sqrt3}{2}\right)
=1.8069639529\ldots.
\tag{C25.24}
$$

Thus the narrow global force-perimeter window holds component-by-component after
normalization; a small KKT mass cannot hide a geometrically poor component merely by
being small.

---

## 5. Exact matching endpoint for one component

### Proposition C25.5 (component upper equality)

For `Q in mathscr D`,
$$
\boxed{P_Q^*=2D\beta_Q}
\tag{C25.25}
$$
if and only if every vertex of `B_Q` has positive-diameter degree one.  Equivalently,
the positive diameter graph `H_+` restricted to `B_Q` is a matching.

In this equality case `F_Q^*` is centrally symmetric: it is the Minkowski sum of the
degenerate reciprocal segments associated with the positive matching edges in `Q`.

#### Proof

The upper bound in C25.22 is the sum over `b in B_Q` of Euclidean triangle
inequalities applied to the positive vectors `beta_{bk}(b-k)`.  Equality holds exactly
when, at every `b`, all incident positive diameter vectors have the same direction.
They all have the same length `D`; distinct partners cannot occupy the same ray at
that distance.  Hence every `b` has exactly one positive diameter partner.

Conversely a positive matching has no local vector cancellation and attains the upper
bound.  Each matching edge contributes an opposite pair of reciprocal vectors, i.e. a
degenerate segment summand.  Their Minkowski sum is centrally symmetric and has the
same edge sequence as `F_Q^*`. `\square`

Crucially, the **full** diameter component `Q` need not be a matching in this equality
case.  Several positive matching edges may be connected by KKT-weak full-diameter
chords.  This is precisely the near-disk escape left open by C23--C24.

---

## 6. New exact C-II split

C23--C25 now separate three layers that had previously been conflated:

1. the full diameter graph supplies the translation-class rank required by contact
   minimality;
2. the positive diameter graph supplies the KKT reaction and reciprocal geometry;
3. weak full-diameter edges can connect several positive reciprocal components without
   contributing KKT mass.

Every full-diameter class `Q` carries a normalized reciprocal response
`tilde F_Q^*` with the same mixed area `D^2/2` and perimeter in the narrow interval
(C25.23).  If its normalized perimeter is exactly `2D`, the positive part is a
matching and any additional full-diameter connectivity inside `Q` is necessarily weak.

A high-value continuation is therefore a **weak-diameter glue theorem**:

> Show that a contact-minimal C-II source cannot obtain the macroscopic full-diameter
> connectivity rank required by C23 primarily from KKT-weak diameter chords joining
> matching-like positive reaction pairs, unless a common-rate finite motion releases a
> contact/diameter constraint or the source enters an asymptotically near-disk branch
> that can be attacked by the zero-slack Target A machinery.

No such theorem is proved here.  The component decomposition makes the obstruction
exact and coordinate-free.
