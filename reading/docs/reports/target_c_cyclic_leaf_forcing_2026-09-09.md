> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_leaf_forcing_2026-09-09.md) · source SHA-256 `27cdf6167c443f03d73d50b798cdc96634bb2147fb79e48beb33f4b3a5f2b224`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-FF5ED9DF3604","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic endpoint: diameter leaves are KKT-face rigid

**Date:** 2026-09-09  
**Repository base:** PR #118 after CY/CG  
**Run type:** exact KKT-polytope / diameter-topology refinement  
**Target:** Target C cyclic primitive endpoint  
**Depends on:** CY selected diameter edge-cover theorem, CG diameter-only KKT face lattice, CY `dim S=s_Z=2-d_H`  
**External web search:** not used  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

In the cyclic primitive endpoint every selected positive diameter graph covers all `q` loaded terminals. This makes every edge incident to a leaf of the **full** diameter graph unavoidable in every normalized KKT stress.

Let `H` be the full actual diameter graph and let

$$
L_H^{leaf}:=\{h\in E(H): h\text{ has an endpoint of full-H degree }1\}.
$$

Then:

$$
\boxed{
\beta_h(s)>0
\quad
(h\in L_H^{leaf},\ s\in\mathcal S).}
\tag{LF.1}

Thus full-H leaf edges never define KKT-polytope boundary faces.

If

\[
d:=\dim\mathcal S=s_Z=2-d_H,
$$

then a `d`-dimensional compact polytope has at least `d+1` facets, and CG says every facet is created by a diameter coefficient reaching zero. Consequently the full diameter graph contains at least `d+1` edges that are **not** incident to a full-H leaf:

$$
\boxed{
|\{uv\in E(H):\deg_Hu\ge2,\ \deg_Hv\ge2\}|
\ge s_Z+1=3-d_H.}
\tag{LF.2}

This is a finite topological restriction on the full diameter pseudoforest.

---

## 1. Leaf-edge forcing

Let `u` be a terminal with

\[
\deg_H(u)=1
$$

in the full actual diameter graph, and let its unique incident diameter edge be

$$
h=uv.
$$

Fix any normalized KKT stress `s`. CY.2 says the selected positive diameter support `H_s` is an edge cover of the complete terminal set `B_+`. Hence `u` must be incident to some edge of `H_s`.

But `H_s\subseteq H`, and `h` is the only full diameter edge at `u`. Therefore

$$
h\in H_s,
$$

so

$$
\beta_h(s)>0.
$$

This proves LF.1. `square`

Because `S` is compact and `beta_h` is continuous, every full-H leaf edge in fact has a fixed-source positive floor

$$
\boxed{
\min_{s\in\mathcal S}\beta_h(s)>0.}
\tag{1.1}

No uniform-in-`D` lower bound is claimed.

---

## 2. Facets require nonleaf diameter edges

CG proves two facts throughout the cyclic KKT polytope:

1. every cycle contact coefficient stays strictly positive;
2. every proper face is induced solely by one or more equations `beta_h=0`.

Let `d=dim S`. A full-dimensional compact `d`-polytope has at least `d+1` distinct facets.

Take one facet `F`. By CG it lies in at least one coordinate hyperplane

\[
\beta_h=0.
$$

The set

$$
\mathcal S\cap\{\beta_h=0\}
$$

is itself a face. Since it contains the facet `F`, maximality of a facet implies that this coordinate face equals `F`.

Therefore two distinct facets cannot be supplied solely by the same diameter coordinate: one coordinate hyperplane cuts out one convex coordinate face. Hence at least `d+1` distinct diameter edges vanish somewhere on the KKT-polytope boundary.

By LF.1 none of those edges is incident to a full-H leaf. Thus the full graph has at least `d+1` nonleaf-nonleaf edges. Since CY gives

$$
d=s_Z=2-d_H,
$$

we obtain LF.2. `square`

---

## 3. Three full cyclic subcases

Recall

$$
(d_H,s_Z)\in\{(0,2),(1,1),(2,0)\}.
$$

### `d_H=0`, `s_Z=2`

The normalized stress polytope is two-dimensional. Therefore the full diameter graph has at least

$$
3
$$

edges joining two nonleaf diameter vertices.

### `d_H=1`, `s_Z=1`

The stress polytope is a line segment. Therefore the full diameter graph has at least

$$
2
$$

nonleaf-nonleaf edges.

In particular, if the full diameter graph is a connected tree, its caterpillar spine contains at least two edges and at least three nonleaf vertices. Hence the tree is neither

1. a star; nor
2. a double star whose nonleaf spine consists of one edge.

### `d_H=2`, `s_Z=0`

The KKT polytope is a singleton, so the facet argument is vacuous. CY already gives the stronger rigidity-circuit description.

---

## 4. Stress-family motion is confined to the diameter core

Let

$$
H^{core}
:=H[\{v:\deg_H(v)\ge2\}]
$$

with its edge set consisting of full diameter edges whose two endpoints are nonleaves.

LF.1 says every leaf edge coefficient remains positive throughout `S`. Therefore all KKT-polytope support changes occur inside `H^{core}`.

More precisely, if `s_0,s_1 in S`, every full-H leaf edge belongs to

$$
H_{s_0}\cap H_{s_1}.
$$

Thus the one- or two-dimensional stress freedom in the cyclic endpoint is carried entirely by reweighting and deleting edges inside the nonleaf diameter spine/cycle.

This is useful because the canonical planar diameter graph is a caterpillar pseudoforest: the leaf forest is now frozen, while only the path/odd-cycle core participates in the KKT face lattice.

---

## 5. Regression audit

### Regular odd shell

Its full diameter graph is an odd cycle, so every diameter edge is nonleaf. LF.2 is satisfied and does not falsely exclude the shell.

### Even shell with opposite matching selected support

The full diameter graph of the source, not one selected support, controls LF.1. A selected matching edge may vanish elsewhere only if its endpoints have alternative full diameter edges. No conflict arises.

### Diameter star

Every star edge is incident to a leaf. Therefore all beta coordinates would stay positive throughout `S`. A positive-dimensional compact cyclic KKT polytope cannot then have any boundary facet, so a star is excluded whenever `s_Z>0`. This is consistent with the stronger existing full-support star exclusions.

### One-spine-edge double star

The unique spine edge is the only nonleaf-nonleaf edge. It cannot support the two distinct coordinate facets required when `s_Z=1`, so the cyclic `d_H=1` family excludes this topology.

---

## 6. Next theorem

For `d_H=1`, the stress polytope is an interval. Its two endpoints set at least two distinct nonleaf diameter coefficients to zero. If the full diameter graph is a tree, each such zeroed edge disconnects that tree into two vertex sets, while no other full diameter edge crosses the cut.

Summing the selected KKT equilibrium over either component then forces the positive contact-cycle forces crossing that vertex cut to have zero resultant.

The next target is therefore a convex-thrackle cut theorem:

> classify the cyclic interval structure of the two components obtained by deleting a nonleaf edge of a convex straight-line thrackle tree, and combine it with the impossibility of a proper consecutive zero-resultant side block in the reciprocal force polygon.

This may exclude the connected-tree `d_H=1` cyclic subcase.

---

## 7. Promotion recommendation

**Hold as report pending independent audit.**

The argument is exact downstream of report-level CY/CG.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

In the cyclic endpoint every selected H_s edge-covers all q terminals.
Therefore if u is a leaf of the full diameter graph H, its unique incident edge h
must belong to H_s for every normalized stress s:
  beta_h(s)>0 on all of S.
So leaf edges never define KKT faces.

CG says all proper KKT faces are diameter-coordinate faces. A d-dimensional compact
polytope needs at least d+1 distinct facets, hence at least d+1 distinct diameter
edges that can vanish. None can be a leaf edge.

Since d=s_Z=2-d_H:
  number of nonleaf-nonleaf full diameter edges >= 3-d_H.
Thus:
- d_H=0: at least 3 such edges;
- d_H=1: at least 2;
- d_H=2: singleton stress, no facet requirement.

All stress-polytope support motion is confined to the caterpillar/odd-cycle core of H;
the leaf forest is frozen.

Next: in the d_H=1 tree subcase, zero a nonleaf edge at a KKT endpoint, sum equilibrium
over the resulting tree component, and use convex-thrackle cut order + reciprocal
polygon geometry to forbid the required zero resultant.
```
