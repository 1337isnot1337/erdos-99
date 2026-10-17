> Generated reading edition · [exact source](../../../docs/reports/target_c_harmonic_attachment_hulls_2026-08-31.md) · source SHA-256 `dec6a6bec869c93d7164be9fcce1d34a4b9223c8742ca88a541e3d1b20c2b32f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F2152410F015","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_harmonic_attachment_hulls_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=532b53a06f3ed26ef162ad0bb3592203181c14b6; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C C36: unpinned components lie in noncrossing harmonic attachment hulls

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C26, C35, positive KKT equilibrium and planar noncrossing  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

For an unpinned component `I_r` of `C[V(C)\setminus B_+]`, let

```math
A_r:=\{b\in B_+: \exists x\in I_r\text{ with }bx\in C\}
```

be its distinct loaded attachment vertices.

Positive contact equilibrium makes both coordinate functions harmonic at every vertex of `I_r`. The discrete maximum principle gives

```math
\boxed{I_r\subseteq\operatorname{conv}A_r.}
```

One or two distinct attachment vertices are impossible; therefore

```math
\boxed{|A_r|\ge3.}
```

Moreover attachment sets of distinct components are noncrossing in the cyclic order on the force-hull boundary: there cannot be four distinct vertices `a,c in A_r`, `b,d in A_s` occurring as `a,b,c,d` cyclically.

---

## 1. Harmonic maximum principle

At every `x in I_r`, C26 gives zero positive diameter reaction, so

```math
\sum_{xy\in C}\alpha_{xy}(x-y)=0,
\qquad \alpha_{xy}>0.
\tag{C36.1}
```

Equivalently, `x` is a strict weighted average of its contact neighbors.

Fix a linear functional `ell`. Suppose `ell(x)` exceeds `max_{b in A_r}ell(b)` for some `x in I_r`. Choose a component vertex where `ell` is maximal. The strict weighted-average identity forces every contact neighbor in the component to have the same maximal value. Connectedness propagates this value to an attachment vertex in `A_r`, contradiction.

Thus for every linear functional,

```math
ell(x)\le\max_{b\in A_r}\ell(b).
\tag{C36.2}
```

The separating-hyperplane characterization of convex hulls gives:

### Theorem C36.1

```math
\boxed{V(I_r)\subseteq\operatorname{conv}A_r.}
\tag{C36.3}
```

---

## 2. At least three distinct pins

If `|A_r|=1`, C36.3 collapses every component vertex to one point, impossible for distinct unit-separated source points.

If `|A_r|=2`, C36.3 places every component vertex on the line segment joining the two loaded pins. Every contact neighbor of a component vertex lies either in the same component or in those two pins, hence on the same line. A unit-separated point on a line has at most two unit-distance neighbors. Thus every component vertex has full contact degree at most two, contradicting C26.

### Theorem C36.2

```math
\boxed{|A_r|\ge3.}
\tag{C36.4}
```

This strengthens C35's three-edge attachment theorem to three distinct loaded pins.

---

## 3. Noncrossing attachment hypergraph

All vertices of `B_+` occur in cyclic order on the boundary of the convex force hull `F`.

Suppose distinct components `I_r,I_s` had four distinct attachments `a,c in A_r` and `b,d in A_s` alternating as `a,b,c,d` around `partial F`.

Because `I_r` is connected and both `a,c` have contacts into it, there is a contact path from `a` to `c` with internal vertices in `I_r`. Similarly there is a vertex-disjoint contact path from `b` to `d` through `I_s`. Both lie in the convex disk `F`. Two vertex-disjoint plane paths cannot join alternating boundary pairs. Contradiction.

### Theorem C36.3

The family `{A_r}` is noncrossing in cyclic boundary order: no two distinct attachment sets contain four distinct alternating boundary vertices.

Attachment sets may overlap at loaded vertices and may be nested; no interval or disjointness claim is made.

---

## 4. Distinct incidence budget

Let `a_r=|A_r|`. A loaded vertex can belong to at most `deg_C(b)` attachment sets, because each membership requires a distinct contact edge to that component. C35 gives `deg_C(b)<=3`. Therefore

```math
\boxed{3c_I\le\sum_r a_r\le3q.}
\tag{C36.5}
```

The upper bound counts distinct attachment incidences, not contact edges.

---

## 5. Regression audit

- One interior vertex attached to three loaded pins is allowed; it lies in their triangle as predicted.
- Two-pin straight chains are excluded by C36.2/C26.
- Two components may share one or two loaded pins; C36 only forbids alternating four-distinct-vertex patterns.
- Nested noncrossing attachment sets remain possible.

```text
C36:
For each unpinned component I_r, positive KKT equilibrium is harmonic.  The discrete
maximum principle gives I_r subset conv(A_r), where A_r is its distinct loaded
attachment set.  One pin collapses the component; two pins make it collinear and force
contact degree <=2, contradicting C26.  Thus |A_r|>=3.  Distinct attachment sets are
noncrossing in cyclic boundary order by planar alternating-path obstruction.
```
