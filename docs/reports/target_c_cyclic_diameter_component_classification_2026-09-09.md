<!-- theorem-state: {"artifact_id":"ART-AFA0D18A6E72","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact diameter-component classification in the cyclic endpoint

**Date:** 2026-09-09  
**Repository branch:** PR #118 after CY/TC/RE  
**Run type:** exact convex-thrackle component reduction  
**Target:** cyclic primitive endpoint  
**Depends on:** canonical planar diameter-thrackle structure and CY identity `d_H=q-h in {0,1,2}`  
**External literature:** none  
**Computation:** small-q enumeration was used only as a regression against a stronger false conjecture; it is not a proof dependency

## LEVEL I STATUS

`STILL OPEN`

CY leaves three finite cyclic phases

\[
(d_H,s_Z)=(0,2),(1,1),(2,0).
\]

The canonical planar diameter-graph theorem says every component is a caterpillar whose spine is a path or one odd cycle, with at most one unicyclic component. The following elementary thrackle observation sharpens this substantially whenever the full diameter graph is disconnected.

### Theorem DC — an odd diameter cycle is the whole diameter graph

If a planar diameter graph `H` contains an odd cycle, then every edge of `H` belongs to the same connected component as that cycle. Since the canonical structure has no isolated diameter vertices in the force-visible cyclic endpoint, the odd-unicyclic component is the **only** component of `H`.

Consequently:

\[
\boxed{
d_H=0
\Longrightarrow
H\text{ is one odd-unicyclic caterpillar},}
\tag{DC.1}
\]

\[
\boxed{
d_H=1
\Longrightarrow
H\text{ is one connected spanning tree},}
\tag{DC.2}
\]

\[
\boxed{
d_H=2
\Longrightarrow
H\text{ is a forest of exactly two tree components}.}
\tag{DC.3}
\]

In particular, the “connected-tree subcase” in the existing cyclic tree-cut report TC is not a subcase: it is the entire `d_H=1` phase.

---

## 1. Odd cycle versus a disjoint diameter edge

Suppose

\[
v_0v_1,\ v_1v_2,\ldots,\ v_{2r}v_0
\]

is an odd cycle in one component of `H`, and suppose for contradiction that another component contains an edge

\[
xy.
\]

The components are vertex-disjoint, so `xy` shares no endpoint with any cycle edge.

All diameter endpoints lie on the convex force hull. The diameter graph is a geometric thrackle: every two vertex-disjoint diameter edges cross in their relative interiors.

Therefore every cycle edge

\[
v_iv_{i+1}
\]

crosses the fixed chord `xy`.

Let `L` be the supporting line through `x,y`. Two chords of a strictly convex polygon with no shared endpoint cross only if their endpoints lie on opposite sides of the other's supporting chord. Hence the endpoints of every cycle edge lie in opposite open half-planes determined by `L`.

Color each cycle vertex according to which side of `L` contains it. Every cycle edge joins opposite colors. This gives a proper 2-coloring of the odd cycle, impossible.

Thus no such edge `xy` exists. `square`

---

## 2. No isolated diameter component remains

In the cyclic C-II endpoint every loaded force-hull vertex is an actual diameter endpoint, so the full actual diameter graph has no isolated vertices.

Theorem DC therefore implies that once an odd-unicyclic component exists there are no other vertices outside it. Hence it spans all `q` terminals and is the unique component.

For a connected odd-unicyclic graph on `q` vertices,

\[
h=q,
\]

so

\[
d_H=q-h=0.
\]

Conversely, if `d_H>0`, no odd cycle exists. The canonical pseudoforest is then a forest.

For a forest on all `q` vertices with `c` connected components,

\[
h=q-c,
\]

so

\[
d_H=q-h=c.
\]

This immediately gives DC.2-DC.3.

---

## 3. Upgrade of the `d_H=1` endpoint

CY gives

\[
d_H=1,
\qquad
s_Z=1.
\]

DC now says the full diameter graph is necessarily one connected spanning tree with

\[
h=q-1.
\]

Therefore all conclusions in the existing TC report that were stated under its connected-tree hypothesis apply to the complete `d_H=1` branch.

In particular:

1. every full-H diameter edge separates the tree into two connected vertex sets;
2. each side occupies at most two cyclic intervals on the force-hull order;
3. LF gives at least
   \[
   s_Z+1=2
   \]
   full diameter edges joining nonleaf vertices;
4. whenever such a nonleaf tree edge has zero coefficient at an endpoint of the one-dimensional normalized KKT segment, its two tree-cut sides must both occupy exactly two cyclic intervals;
5. the four resulting boundary contact-force vectors satisfy the TC reciprocal parallelogram relation.

There is no longer a disconnected odd-unicyclic-plus-tree branch to audit separately.

This makes TC + WT the exact finite endpoint for `d_H=1`.

---

## 4. Exact `d_H=2` topology

CY gives

\[
d_H=2,
\qquad
s_Z=0,
\qquad
h=q-2.
\]

DC excludes an odd-unicyclic component. Hence `H` is a forest. The forest identity then forces exactly two connected components.

The mixed active graph has

\[
|C|+|H|=q+(q-2)=2q-2
\]

rows and, by CY/CG, rigidity rank `2q-3` with one full-support dependence. Thus it is a rigidity circuit at the realized configuration.

A tempting stronger conjecture was that no two-component convex-thrackle forest can be compatible with Laman-circuit sparsity. Exact enumeration of abstract convex-thrackle forests for `q<=10` disproves that shortcut: examples exist, including bounded-degree examples. No such false combinatorial exclusion is claimed here.

The correct `d_H=2` target must use Euclidean diameter geometry, KKT signs, or global optimality beyond abstract rigidity sparsity.

---

## 5. Regression audit

### Odd regular shell

Its diameter graph is one odd cycle, consistent with `d_H=0` and DC.1.

### Odd cycle plus a disjoint chord

Impossible by the proof: the disjoint chord would force the odd cycle to alternate sides of its supporting line.

### Connected convex-thrackle tree

Allowed and is exactly the `d_H=1` topology.

### Two convex-thrackle trees

Allowed abstractly and is the only `d_H=2` topology. Small exact enumeration confirms that Laman-circuit counting alone does not remove it.

---

## 6. What this changes

The cyclic campaign no longer has hidden component alternatives:

```text
d_H=0, s_Z=2:
    one spanning odd-unicyclic caterpillar
    -> RE/US/RC/RD/FB exact Reinhardt branch

d_H=1, s_Z=1:
    one spanning convex-thrackle tree
    -> TC four-interval/parallelogram endpoint + WT transfer formulas

d_H=2, s_Z=0:
    exactly two convex-thrackle tree components
    -> unique normalized stress / realized rigidity circuit
```

This is a genuine three-way exact normal form.

---

## 7. Next theorem

For `d_H=1`, attack the now-universal TC endpoint:

> show that the reciprocal parallelogram forced when a nonleaf tree edge vanishes at a KKT endpoint is incompatible with the WT weighted-cycle transfer formulas and the C56-G strict Robinson kernel.

For `d_H=2`, exploit the two-component geometry rather than circuit sparsity alone. Every edge of one tree crosses every edge of the other; a useful target is an exact cyclic-interval classification strong enough to feed the unique KKT stress equations.

---

## 8. Promotion recommendation

**Hold as report pending independent audit.**

The component argument itself is elementary and exact, but its cyclic consequences are downstream of report-level CY.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Odd-cycle component lemma:
If H contains an odd cycle C and another component has edge xy, then every edge of C
is vertex-disjoint from xy and hence crosses xy by the diameter-thrackle property.
Therefore endpoints of every C-edge lie on opposite sides of line(xy), 2-coloring C.
Contradiction. Thus an odd-unicyclic component is the whole H.

Hence in the cyclic endpoint:
  d_H=0 -> one spanning odd-unicyclic caterpillar;
  d_H=1 -> one connected spanning tree;
  d_H=2 -> exactly two tree components.

So TC's connected-tree hypothesis is automatic throughout d_H=1. Its 2+2 cyclic
interval cut and reciprocal parallelogram are now the exact d_H=1 endpoint.
Abstract Laman-circuit sparsity does NOT eliminate d_H=2; small convex-thrackle
enumeration found valid combinatorial examples, so the next d_H=2 theorem must use
geometry/KKT/global optimality.
```
