<!-- theorem-state: {"artifact_id":"ART-1A315CD76C68","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: a universal contact bridge makes the full core diameter graph a one-cap pseudoforest

**Date:** 2026-08-31
**Repository branch:** `research/target-c-no-neutral-corridors-2026-08-31`
**Run type:** proof / C-II common-bridge geometry
**Target:** C-II
**Depends on:** C24-C26, the planar diameter-thrackle property, and C17
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C25 classifies the positive diameter graph `H_+` when the C24 common route is a contact bridge. C26 has since sharpened that route: in the fully force-visible branch it is either one block or exactly one bridge.

The full source diameter graph may contain zero-`beta` edges, so `H_+` cannot simply be substituted for the full diameter graph. Nevertheless, in the one-universal-bridge phase the common cut almost determines the full diameter graph on the nonisolated core.

Let the bridge split the positively loaded force-hull boundary into complementary cyclic intervals

\[
A=(a_1,\ldots,a_p),\qquad B=(b_1,\ldots,b_q).
\]

Then every full diameter edge whose endpoints are nonisolated crosses the cut `A|B`, with at most one exception: one interval may have a single **cap edge** joining its two extreme vertices. The two intervals cannot both have caps.

Consequently, after deleting that possible cap, the full core diameter graph is a caterpillar forest. With the cap restored it has at most one cycle, and any such cycle is the cap plus the unique alternating cross-cut path between its endpoints. C17 forces that unique cycle, when present, to have length `Omega(sqrt(D))`.

---

## 1. Setup

Assume C-II and choose a relative-interior normalized KKT stress. By C26,

\[
Q^circ=B_+,
\tag{C32.1}
\]

so every source diameter endpoint belonging to the nonisolated contact core is a vertex of `B_+`, and every point of `B_+` is a convex vertex of the force hull.

Assume the C24 common positive-diameter route is the nontrivial C26 case: exactly one positive contact bridge `e`. Removing it partitions `B_+` into complementary boundary intervals

\[
A=(a_1,\ldots,a_p),\qquad
B=(b_1,\ldots,b_q),
\tag{C32.2}
\]

listed in the same cyclic direction around the convex force hull.

C24 gives

\[
H_+\subseteq A\times B,
\tag{C32.3}
\]

and by definition

\[
V(H_+)=B_+=A\sqcup B.
\tag{C32.4}
\]

Let `H^circ` denote the full source diameter graph induced by the nonisolated core. By C32.1,

\[
V(H^circ)=B_+,
\tag{C32.5}
\]

although `E(H^circ)` can strictly contain `H_+` because some full diameter edges may have zero `beta` weight.

---

## 2. A same-side full diameter must span its whole interval

### Lemma C32.1 (cap lemma)

If

\[
a_i a_k\in E(H^circ),\qquad 1\le i<k\le p,
\tag{C32.6}
\]

then

\[
\boxed{i=1,\qquad k=p.}
\tag{C32.7}
\]

Symmetrically, if `b_jb_l` is a full diameter edge with `j<l`, then `j=1` and `l=q`.

#### Proof

Take any `a_r in A\setminus\{a_i,a_k\}`. By C32.4, `a_r` is incident to a positive diameter edge

\[
a_r b_s\in H_+
\]

for some `b_s in B`.

The full diameter edges `a_i a_k` and `a_r b_s` have four distinct endpoints. The planar diameter-graph thrackle property therefore says their straight chords cross in their interiors.

The force-hull vertices occur in convex cyclic order with all of `A` consecutive and all of `B` consecutive. For `i<k`, the chord `a_i a_k` cuts the boundary into two arcs. The arc from `a_i` to `a_k` through increasing `A` indices contains exactly

\[
a_i,a_{i+1},\ldots,a_k,
\]

while every `B` vertex lies on the complementary arc. Two chords of a convex polygon cross exactly when their endpoints alternate. Since `b_s` lies on the complementary arc, crossing forces `a_r` to lie strictly on the first arc:

\[
i<r<k.
\tag{C32.8}
\]

This must hold for every `r` distinct from `i,k`. Hence there is no `A` vertex before `a_i` or after `a_k`. Therefore `i=1` and `k=p`. `square`

Thus each side has at most one possible same-side full diameter, namely its interval cap.

---

## 3. The two sides cannot both have caps

### Lemma C32.2 (one-cap theorem)

At most one of

\[
a_1a_p,\qquad b_1b_q
\tag{C32.9}
\]

is a full diameter edge.

#### Proof

If both existed, they would be vertex-disjoint diameter edges. Their endpoints occur in boundary order `A,A,B,B`, not alternating order, so the two convex-polygon chords do not cross. This contradicts the diameter-thrackle property that every pair of vertex-disjoint diameter edges must cross. `square`

Therefore

\[
\boxed{
E(H^circ)\subseteq (A\times B)\cup\{e_{cap}\}
}
\tag{C32.10}
\]

for at most one cap edge `e_cap`.

---

## 4. The full cross-cut diameter graph is a caterpillar forest

Define

\[
K:=H^circ\cap(A\times B).
\tag{C32.11}
\]

### Lemma C32.3

`K` is a forest.

#### Proof

`K` is bipartite with parts `A,B`, so every graph cycle in `K` would be even. But every cycle in a planar diameter graph is odd. Hence `K` has no cycle. `square`

The C25 order argument applies verbatim to `K`, because it uses only convex boundary order and the fact that vertex-disjoint **diameter** edges cross; positivity of their `beta` weights is irrelevant.

### Lemma C32.4 (order monotonicity)

If `a_i b_j` and `a_k b_l` are vertex-disjoint edges of `K` and `i<k`, then

\[
\boxed{j<l.}
\tag{C32.12}
\]

### Theorem C32.5 (full cross-cut caterpillar forest)

Every connected component of `K` is a caterpillar.

#### Proof

As in C25, order monotonicity forbids any vertex from having three non-leaf neighbors: if `a_i` had three non-leaf neighbors `b_{j_1}<b_{j_2}<b_{j_3}`, a second neighbor `a_k` of the middle vertex would invert against one of the two outer edges, depending on whether `k<i` or `i<k`. The same argument applies on the `B` side.

Since `K` is a forest, deleting the leaves from any connected component leaves a connected acyclic graph of maximum degree at most two, hence a path. Therefore each component is a caterpillar. `square`

So C25's caterpillar theorem extends from the positive diameter support to **every cross-cut full diameter edge of the nonisolated core**.

---

## 5. The full core diameter graph has at most one cycle

### Theorem C32 (one-cap pseudoforest theorem)

In the one-universal-contact-bridge C-II phase, the full diameter graph `H^circ` of the nonisolated core is obtained from the cross-cut caterpillar forest `K` by adding at most one cap edge. Consequently:

1. `H^circ` is a forest if there is no cap or if the cap joins two distinct components of `K`;
2. otherwise `H^circ` has exactly one cycle;
3. that unique cycle consists of the cap plus the unique `K`-path joining its endpoints.

#### Proof

C32.10 gives `H^circ=K` or `K+e_cap`, while Lemma C32.3 says `K` is a forest. Adding one edge to a forest either joins two components and leaves a forest or joins two vertices of one component and creates exactly one cycle, the new edge plus the unique pre-existing path. `square`

Because the cap endpoints lie in the same side of the bipartition, their `K`-path has even length, so the unique full diameter cycle is odd, consistently with the planar diameter-graph theorem.

---

## 6. C17 forces the unique cycle to be long

If the cap creates a cycle of length `r`, C17 applies to that full source diameter cycle and gives

\[
\boxed{
r>
\frac{\pi D}{\sqrt{12(2D+1)}}.
}
\tag{C32.13}
\]

Thus any cyclic full-diameter structure in the universal-bridge phase is unique and has length `Omega(sqrt(D))`.

---

## 7. C-II effect

The universal-bridge phase can now be written more sharply:

```text
positive contact route:
    exactly one universal contact bridge

positive diameter graph H_+:
    common-cut caterpillar forest

full diameter graph of the nonisolated core H^circ:
    cross-cut caterpillar forest K
    + at most one same-side cap edge
    -> at most one full diameter cycle
    -> if present, that cycle has length Omega(sqrt(D))
```

This prevents zero-weight diameter edges from hiding arbitrary same-side chords or additional cycle structure inside the C25 common-cut phase.

It does not control diameter edges incident to contact-isolated source points outside the force-visible core. C26 says precisely that such isolated vertices are the only possible KKT-invisible source diameter endpoints in C-II.

---

## 8. Regression audit

- **Crossing diameter matching:** allowed; `K` can be a matching with many components.
- **Positive diameter star:** allowed; it is a caterpillar.
- **One same-side weak diameter:** allowed only as the unique interval cap.
- **Caps on both sides:** excluded by C32.2.
- **Cap joining two different cross-forest components:** allowed and leaves `H^circ` acyclic.
- **Cap closing one component:** allowed only as one unique full diameter cycle, then subject to C17.
- **Bridge-free / one-hub-block phase:** outside scope.
- **Isolated source diameter endpoints:** outside `H^circ` and untouched.

No KKT lower-weight bound or classification theorem for arbitrary straight-line thrackles is imported.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C32 common-bridge full-diameter theorem:
C26 gives Q^circ=B_+. In the universal-bridge phase, B_+=A sqcup B are complementary
force-hull boundary intervals and H_+ subset A x B.

Any full same-side diameter a_i a_k must be the cap a_1 a_p: every other a_r has a
positive edge a_r b_s, and the two disjoint diameter edges must cross; convex boundary
order forces every r to lie between i and k. Symmetrically for B. Both caps cannot
exist because they would be disjoint noncrossing diameter edges.

Hence H^circ[B_+] is the cross graph K subset A x B plus at most one cap. K is
bipartite, while every diameter cycle is odd, so K is a forest. The C25 order argument
then makes every K component a caterpillar. Adding one cap creates at most one cycle;
if it does, C17 forces its length to be Omega(sqrt(D)).
```
