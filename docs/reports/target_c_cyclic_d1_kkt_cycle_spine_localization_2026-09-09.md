<!-- theorem-state: {"artifact_id":"ART-4A83C1364FFF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — `d_H=1` KKT variation is confined to the canonical odd-cycle spine

**Date:** 2026-09-09  
**Repository branch:** PR #118 after AC/LF  
**Run type:** exact KKT-face / antipodal-graph localization  
**Target:** cyclic primitive phase `d_H=1`, S1 branch  
**Depends on:** AC canonical antipodal completion, LF leaf-edge forcing, DC spanning-tree topology  
**Computation:** small convex-thrackle enumeration used only as a regression check; not a proof dependency

## LEVEL I STATUS

`STILL OPEN`

AC identifies the complete vertex-antipodal graph in S1 as a canonical maximal convex thrackle

\[
\mathcal A(F)=H+g,
\]

where `g` is the unique short antipodal pair and lies on the unique odd cycle `C_*` of `A(F)`. The full diameter graph is

\[
H=\mathcal A(F)-g,
\]

so the odd cycle opens into a path while every off-cycle edge remains a direct pendant edge.

LF now has an exact interpretation: all KKT-polytope support variation is confined to the retained edges of this opened odd cycle.

### Theorem CS — canonical cycle-spine localization

Let `S` be the one-dimensional normalized KKT polytope in the cyclic S1 `d_H=1` phase. Then:

1. every diameter edge of `H` outside `C_*` has strictly positive beta coefficient for every stress in `S`;
2. every diameter coordinate that vanishes anywhere on `partial S` is a retained edge of
   \[
   C_*\setminus\{g\};
   \]
3. in particular the two distinct coordinate facets required by LF are supplied by two distinct actual diameter edges
   \[
   e_-,e_+\in E(C_*)\setminus\{g\};
   \]
4. for either endpoint-zero edge `e`, deleting `e` from `H` cuts the opened odd-cycle path into two subpaths, together with the pendant leaves attached to those subpaths;
5. the canonical short chord `g` is the unique edge of `A(F)` other than `e` that reconnects the two cycle-path sides through the deleted cycle.

Thus the `d_H=1` stress interval is not supported by arbitrary tree edges. Its face changes occur entirely on one canonical odd cycle of the antipodal graph, with the short D1 defect edge `g` closing that cycle.

---

## 1. Off-cycle edges are full-H leaf edges

The maximal-convex-thrackle structure of `A(F)` consists of one odd cycle `C_*`, with every vertex outside `C_*` a degree-one leaf attached directly to a cycle vertex.

AC proves that the deleted short edge `g` lies on `C_*`. Therefore deleting `g` does not alter any off-cycle pendant edge. Hence every edge

\[
h\in E(\mathcal A(F))\setminus E(C_*)
\]

remains a pendant edge in the full diameter tree

\[
H=\mathcal A(F)-g.
\]

In particular each such edge is incident to a vertex of full-H degree one.

LF.1 therefore applies:

\[
\boxed{
\beta_h(s)>0
\quad
\text{for every }s\in\mathcal S,
\qquad
h\notin C_*.
}
\tag{CS.1}
\]

This proves item 1.

---

## 2. Every KKT face coordinate is a retained cycle edge

CG says every proper face of the cyclic KKT polytope is induced by diameter coordinates reaching zero. LF says no full-H leaf edge can do so.

Section 1 identifies every edge outside `C_*` as a full-H leaf edge. Therefore any diameter edge `e` satisfying

\[
\beta_e(s)=0
\]

for some boundary stress `s` must lie on the retained cycle path

\[
C_*\setminus\{g\}.
\]

Thus

\[
\boxed{
\{e\in H:\exists s\in\partial\mathcal S,\ \beta_e(s)=0\}
\subseteq E(C_*)\setminus\{g\}.
}
\tag{CS.2}
\]

This proves item 2.

Since `dim S=1`, LF.2 requires at least two distinct nonleaf diameter coordinates defining the two endpoint facets. They are therefore two distinct retained odd-cycle edges. This proves item 3.

---

## 3. The endpoint cut is literally a cut of the opened odd cycle

Fix one endpoint-zero edge

\[
e\in E(C_*)\setminus\{g\}.
\]

The graph `C_*-g` is a path through all cycle vertices. Removing the additional edge `e` splits this path into exactly two path components.

Every off-cycle vertex of `A(F)` is a direct leaf attached to one cycle vertex. Therefore in

\[
H-e=(\mathcal A(F)-g)-e
\]

each pendant leaf remains attached to whichever of the two cycle-path components contains its attachment vertex.

Consequently the two tree components from corrected EU/TC are exactly:

```text
one subpath of C_*-{g,e} + all leaves attached to that subpath,

the complementary subpath + all leaves attached there.
```

No other topological decomposition is possible. This proves item 4.

---

## 4. The short edge is the canonical reconnection of the cut

In the maximal antipodal graph `A(F)`, the only two cycle edges removed from the cycle when we pass to `H-e` are

\[
g
\quad\text{and}\quad
e.
\]

Restoring `e` gives the diameter tree `H`; restoring `g` instead gives the alternate spanning tree

\[
\mathcal A(F)-e.
\]

Both connect the two path sides of `C_*-\{g,e\}`. All pendant edges are internal to one side.

Therefore `g` is a cross-cut chord for the `H-e` component partition. This recovers the MT/EU cross-cut conclusion, but now canonically: the cross-cut short chord is exactly the unique D1 antipodal defect, not an arbitrarily chosen maximal-completion edge.

This proves item 5.

---

## 5. Four-block consequence

TC/corrected EU gives four alternating cyclic blocks for the component partition of `H-e`. CS identifies their graph-theoretic origin: they are the shell traces of two complementary arcs of the canonical odd cycle, with attached antipodal leaves inserted into the corresponding maximal-thrackle wedges.

The actual zeroed diameter chord `e` and the canonical short chord `g` both cross the component cut and both are edges of `C_*`.

The corner theorem therefore applies to both: each is one of the admissible opposite-corner chords for the same four-block partition.

A finite combinatorial regression check shows that `e` and `g` need not be vertex-disjoint. They may share a cycle vertex. Hence no stronger universal claim that they are the two disjoint complementary diagonals is made here.

---

## 6. Stress-family consequence

Every off-cycle beta coordinate has a fixed-source positive floor by LF:

\[
\min_{s\in\mathcal S}\beta_h(s)>0,
\qquad h\notin C_*.
\]

Thus any affine parameterization

\[
s(t)=s_0+t\dot s
\]

of the one-dimensional stress polytope can hit coordinate hyperplanes only among the retained cycle-edge beta coordinates.

This sharply separates the roles of the diameter skeleton:

- pendant diameter edges are mechanically mandatory throughout the KKT family;
- retained odd-cycle edges carry all support degeneration;
- the one missing odd-cycle edge is the canonical short antipodal chord `g` and never enters the KKT support because `|g|<D`.

---

## 7. Regression audit

### Completion nonuniqueness

AC removes it in S1: the relevant maximal completion is the complete antipodal graph itself.

### Endpoint edge could be pendant in the maximal graph

Impossible. A pendant edge of `A(F)` remains a full-H leaf edge after deleting the cycle edge `g`, and LF forbids its coefficient from vanishing.

### `e` and `g` must be disjoint

False. Small exact convex-thrackle examples contain retained cycle edges sharing a cycle endpoint with the deleted completion edge. CS deliberately does not assume disjointness.

### Additional beta zeros at one KKT endpoint

Allowed. CS says any such extra zero coordinates must also be retained cycle edges. It does not assume one zero per endpoint.

---

## 8. What this changes

The S1 `d_H=1` endpoint problem now lives on one finite cyclic core:

```text
canonical odd antipodal cycle C_*
  one short edge g removed -> full diameter tree H
  two or more retained cycle edges can define KKT boundary faces
  all off-cycle pendant diameter edges stay beta-positive forever
```

For any endpoint-zero retained cycle edge `e`, the four-block cut is the cut obtained by deleting the pair `{g,e}` from the odd cycle and distributing the pendant leaves to the two resulting cycle paths.

This is the correct topology for the next WT/wrench calculation.

---

## 9. Next theorem

The next target should use the **two marked cycle edges** `g` and `e` rather than an arbitrary four-block forest.

For the cut of `C_*-{g,e}`:

1. identify the four shell transition contacts from the two antipodal cycle arcs;
2. express the WM cofactor ratios in terms of those marked cycle endpoints;
3. use D1's exact formula for `|g|` and `|e|=D`;
4. insert the resulting transition resistances into WT's four-arc product formulas.

The goal is a sign or equality incompatible with C56-G at one or both endpoints of the KKT segment.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

S1 canonical antipodal graph:
  A(F)=H+g = one odd cycle C_* plus direct leaves,
  g is the unique short antipodal cycle edge,
  H=A(F)-g is the spanning diameter tree.

Every edge outside C_* remains a full-H leaf edge. LF therefore forces its beta
coefficient positive for every stress in the 1D KKT polytope. Hence every coordinate
that can vanish lies on C_*-{g}; the two endpoint facets require two distinct retained
actual-diameter cycle edges e_-,e_+.

For an endpoint-zero edge e, deleting {g,e} from C_* splits the cycle into two paths;
H-e consists of those two paths plus their attached leaves. Thus the corrected-EU
four-block cut is canonically the two-marked-edge cut of C_*. Both e (length D) and g
(short, explicit D1 length) cross the same component cut and are admissible corner
chords. They need not be disjoint, so no fake complementary-diagonal claim is used.

Next: compute WM/WT on this two-marked-cycle cut.
```
