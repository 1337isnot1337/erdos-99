# Target C-II — a Helly hub for the high-`t` dominant same-phase O--O family

**Date:** 2026-09-15  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** any pairwise noncrossing family of outer-to-outer complete stopped trains; applied below to the dominant exact-phase family through `t<=1.860`  
**Dependencies:** audited O--O Jordan crosscuts and complement dual tree; planar diameter-thrackle theorem; C65 full actual-diameter visibility; Section 157 KKT cut resultants  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current high-`t` staircase gives a linear family of dominant outer-to-outer trains in one exact projective phase, but it is not legitimate to assume that all of those noncrossing trains form one dual-tree path.  The complement dual can branch.

There is nevertheless a global tree normal form.  Every actual diameter pair determines the unique path in the complement dual tree between the regions containing its two endpoints.  The geometric diameter-thrackle property forces those tree paths to be pairwise intersecting.  Tree Helly therefore gives one common dual region through which **every actual diameter path is routed**.

This converts the entire same-phase O--O family, including all of its branching, into a rooted endpoint-mass flow.

---

## 1. Complement dual tree of a noncrossing O--O family

Let

\[
\mathcal L=\{\tau_1,\ldots,\tau_m\}
\]

be pairwise noncrossing outer-to-outer complete stopped trains.  Use their audited proper centerline crosscuts in the closed outer-face disk.  Cutting the disk along these disjoint crosscuts gives a finite collection of regions.  Its complement dual

\[
T_{\mathcal L}
\]

has one vertex per region and one edge per selected train.  Because the crosscuts are proper and pairwise disjoint, `T_L` is a tree.

A source vertex never lies on a train centerline, whose segments run through contact-edge midpoints and rhombus interiors.  Hence every source vertex `x` belongs to one well-defined complementary region; write

\[
\rho(x)\in V(T_{\mathcal L}).
\]

For an actual diameter pair

\[
h=xy\in H,
\]

let

\[
P_h=[\rho(x),\rho(y)]_{T_{\mathcal L}}
\tag{DH.1}
\]

be the unique tree path between its endpoint regions.  A selected train edge belongs to `P_h` exactly when its Jordan shore split separates `x` from `y`.  Thus `P_h` is precisely the support path of row `h` in the exact global O--O multishear.

---

## 2. Diameter support paths are pairwise intersecting

### Lemma DH.1

For any two actual diameter pairs `h,g in H`,

\[
\boxed{P_h\cap P_g\ne\varnothing.}
\tag{DH.2}
\]

### Proof

If `h` and `g` share a source endpoint, their tree paths contain the complementary region of that endpoint, so they intersect.

Assume they have four distinct endpoints.  Write

\[
h=ac,
\qquad
g=bd.
\]

All actual diameter endpoints are extreme vertices of the convex force hull.  The planar diameter-graph theorem says that two vertex-disjoint diameter edges cross properly; equivalently the four hull vertices occur in alternating cyclic order

\[
a,b,c,d
\]

(up to reversal).

Suppose for contradiction that `P_ac` and `P_bd` were vertex-disjoint in the dual tree.  Since they are disjoint connected subtrees of a tree, some dual edge `e` on the unique connector between them separates the whole path `P_ac` from the whole path `P_bd`.

The dual edge `e` is one selected proper O--O crosscut.  Its two Jordan shores meet the outer boundary in the two complementary boundary intervals between its endpoints.  Because `P_ac` lies entirely on one side of `e`, both `a,c` belong to the same shore boundary interval.  Because `P_bd` lies entirely on the other side, both `b,d` belong to the complementary interval.

But two pairs lying in two disjoint boundary intervals cannot occur in alternating cyclic order.  This contradicts the diameter-thrackle order.  Hence the two tree paths intersect. `square`

The argument is purely topological after the alternating endpoint order is known.  It does not assume that the selected O--O family itself is a path.

---

## 3. Tree Helly gives one common diameter-routing hub

Finite connected subgraphs of a tree have the Helly property.  Applying it to the pairwise-intersecting family

\[
\{P_h:h\in H\}
\]

gives the main theorem.

### Theorem DH — dominant O--O dual-tree Helly hub

There exists a complementary region

\[
\boxed{R_*\in V(T_{\mathcal L})}
\tag{DH.3}
\]

such that

\[
\boxed{R_*\in P_h\qquad(h\in H).}
\tag{DH.4}
\]

Root `T_L` at `R_*`.  Then no actual diameter edge has both endpoint regions in one component of

\[
T_{\mathcal L}-R_*.
\tag{DH.5}
\]

More generally, if `e` is any selected train edge and `T_e` is the component of `T_L-e` not containing the root, then

\[
\boxed{
\text{no }h\in H\text{ has both endpoint regions in }T_e.
}
\tag{DH.6}
\]

Indeed, such an edge would have support path wholly inside `T_e` and could not contain the hub.

Thus arbitrary branching of the same-phase family is allowed, but **every branch is diameter-edge-free internally**: all actual diameter incidence carried by that branch exits through its rootward selected train.

---

## 4. Exact scalar endpoint flow on the rooted O--O tree

Use the canonical C65 relative-interior stress, normalized by

\[
\sum_{h\in H}\beta_h=1,
\qquad
\beta_h>0\quad(h\in H).
\]

For each loaded source vertex `b`, put

\[
s_b:=\sum_{bk\in H}\beta_{bk}.
\tag{DH.7}
\]

Then

\[
\sum_b s_b=2.
\tag{DH.8}
\]

Let `e` be a selected O--O train edge, oriented away from the hub, and let `S_e` be the source vertices whose complementary regions lie in the descendant component `T_e`.  Define

\[
\boxed{
w_e:=\sum_{b\in S_e}s_b.}
\tag{DH.9}
\]

By (DH.6), no actual diameter edge is internal to `S_e`.  Consequently every endpoint incidence counted in `w_e` belongs to an edge crossing the train cut exactly once, and

\[
\boxed{
w_e
=\sum_{\substack{bk\in H\\b\in S_e,\ k\notin S_e}}\beta_{bk}.}
\tag{DH.10}
\]

This is an exact scalar flow, not merely an inequality.

The Section-157 KKT cut resultant for the same rooted shore orientation is

\[
A_eu_e
=\sum_{\substack{bk\in H\\b\in S_e,\ k\notin S_e}}
\beta_{bk}(p_b-p_k),
\qquad A_e>0,
\tag{DH.11}
\]

where `u_e` is the correspondingly oriented unit train contact direction.  Since every diameter vector has length `D`,

\[
\boxed{A_e\le D w_e.}
\tag{DH.12}
\]

For an exact same-projective-phase family there is one unit vector `u` with

\[
u_e\in\{u,-u\}
\]

for every selected edge.  Therefore **every rooted branch resultant is parallel to one fixed projective direction**:

\[
\boxed{
\sum_{h\text{ crossing }e}\beta_h r_h
\parallel u.
}
\tag{DH.13}
\]

This parallel rooted-flow constraint is the extra structure supplied by exact phase purity.

---

## 5. Antichain and depth identities

If `A` is any antichain of rooted selected edges, the descendant source sets `S_e` are pairwise disjoint.  Hence

\[
\boxed{
\sum_{e\in\mathcal A}w_e\le2.
}
\tag{DH.14}
\]

Summing (DH.9) over all selected edges gives the exact layer-cake identity

\[
\boxed{
\sum_{e\in E(T_{\mathcal L})}w_e
=
\sum_b s_b\,d_{T_{\mathcal L}}(\rho(b),R_*).
}
\tag{DH.15}
\]

Combining with (DH.12),

\[
\boxed{
\sum_{e\in E(T_{\mathcal L})}A_e
\le
D\sum_b s_b\,d_{T_{\mathcal L}}(\rho(b),R_*).
}
\tag{DH.16}
\]

No individual lower bound on `beta_h`, `s_b`, `w_e`, or `A_e` is asserted.

---

## 6. High-`t` consequence through `t<=1.860`

The dominant O--O staircase supplies a same-exact-phase pairwise-noncrossing family of size

\[
\begin{array}{c|c}
\text{window} & |\mathcal L|/D\\ \hline
 t\le1.850 & >0.0700-o(1)\\
 t\le1.855 & >0.0466-o(1)\\
 t\le1.860 & >0.0246-o(1).
\end{array}
\tag{DH.17}
\]

(The stronger `t<=1.844` line is now excluded by the separate full-core remainder theorem and is omitted from the live consequence.)

For each of these surviving windows, Theorem DH applies to a **linear-edge dual tree**.  Thus every sufficiently large full-core survivor in the corresponding window has the following exact normal form:

```text
linear many same-phase O-O train cuts
+ arbitrary complement-dual branching allowed
+ one common dual region R_* on every actual diameter support path
+ no actual diameter edge internal to any rooted branch
+ exact scalar beta endpoint flow toward R_*
+ every selected cut resultant parallel to the same projective train direction.
```

This is stronger than a path extraction and does not require a dense transverse train family.

---

## 7. Remaining obstruction

The theorem does not bound the degree of `R_*` or force a long dual-tree path.  A star-like family with many tiny endpoint masses remains possible abstractly.  Nor does (DH.16) give a useful lower bound without additional information on the train contact stresses `A_e`.

The next high-value step is therefore precise: combine the **parallel rooted branch resultants** (DH.13) with the convex-hull locations of the loaded endpoints and the Woodall diameter graph.  A successful theorem should either

1. bound the number of macroscopic hub branches compatible with one common projective resultant direction;
2. force a linear-depth branch, recovering an interval-shear backbone in the high-`t` window; or
3. convert the hub flow directly into a forbidden diameter-chord / endpoint-order pattern.

No C-II closure is claimed.

**Disposition:** proved proof-only high-`t` dual-tree hub normal form for the dominant same-phase O--O family. C-II and Level I remain open.
