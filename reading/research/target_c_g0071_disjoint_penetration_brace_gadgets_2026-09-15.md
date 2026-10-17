> Generated reading edition · [exact source](../../research/target_c_g0071_disjoint_penetration_brace_gadgets_2026-09-15.md) · source SHA-256 `89dd11f66737b2f3719e0f96654f94fe04c92b08069002993b9fc837e77eb3d2`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 6 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "4e89be6dffd52510b201d3f13c67c00b07f08bc6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_g0071_disjoint_penetration_brace_gadgets_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b0c2cc0e85f8cba9a35c2924b61814b22a36b57f06eb90680fae0e07d10e7237"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — distributed reflection blockers yield disjoint penetration/brace gadgets

**Date:** 2026-09-15  
**Status:** proof-only full-core Type-II corollary; theorem-state authority unchanged  
**Scope:** reflection/blocker alternative at the current `g=0.0071` frontier  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current reflection normal form supplies a linear family of distinct physical
unloaded shallow route vertices `x`, each with a source point `y` satisfying

```math
|x-y|>D-1.
```

The convex-route penetration theorem supplies a different piece of geometry at the
same selected occurrences: an actual unit contact from `x` into the core with signed
inward component bounded away from zero.  These two structures can be made physically
disjoint simultaneously.

Fix

```math
\beta_0={\pi\over6}-10^{-4},
\qquad
\gamma_0:=\sin\left({\pi\over3}-\beta_0\right)>1/2.
```

### Theorem PB.1 — unbounded disjoint two-scale gadgets

Along every Type-II sequence in the blocker alternative there is a family

```math
\mathcal G_D
=\{(y_j,x_j,w_j)\}
```

whose cardinality tends to infinity and whose triples are pairwise vertex-disjoint,
such that

1. `x_j` is an unloaded positive-contact-core vertex with `3<=deg_C(x_j)<=4`;
2. `x_jw_j` is an actual unit contact;
3. relative to the loaded side occurrence selected at `x_j`, the vector from `x_j` to
   `w_j` has signed inward component greater than `gamma_0>1/2`;
4. `y_j` is an actual source point with
   
   ```math
   |x_j-y_j|>D-1.
   ```


Thus the blocker branch does not merely contain an unbounded near-diameter matching.
It contains an unbounded family of physically disjoint **braced boundary gadgets**

```text
       unit inward contact
    w ---------------- x
                         \
                          \  > D-1
                           \
                            y
```

with `x` an unloaded degree-three/four contact-core vertex.

No rate for `|mathcal G_D|` is claimed because blocker reuse is currently known only
to be `o(D)`.

---

## 1. Start with linearly many distinct physical tails

The current `g=0.0071` reflection theorem gives

```math
B_{\beta_0}
\ge0.19290930455816248D-o(D)
```

in the blocker branch.  The local degree-four theorem says one physical beta-straight
route vertex can account for at most four selected side occurrences.  Hence there is
a distinct physical tail set `X_D` with

```math
\boxed{
|X_D|
\ge0.04822732613954062D-o(D).
}
\tag{PB.1}
```

Every `x in X_D` is unloaded and has contact degree three or four.

Choose one original selected route occurrence for every `x in X_D`.  It comes with at
least one blocker `y(x)` satisfying

```math
|x-y(x)|>D-1.
\tag{PB.2}
```

---

## 2. Choose edge-injective inward penetration contacts

The hostile-audited convex-route signed-penetration theorem applies to the chosen
beta-straight occurrences.  It permits a simultaneous choice of one non-route contact
edge

```math
e_x=xw(x)
```

at every chosen occurrence such that

```math
|x-w(x)|=1
```

and the signed inward component relative to that occurrence's loaded-side normal is
strictly greater than

```math
\gamma_0
=\sin(\pi/3-\beta_0)>1/2.
\tag{PB.3}
```

Moreover the selected physical contact edges are globally distinct.  Restricting the
global selection to one occurrence per physical tail preserves that edge injectivity.
Thus there are `|X_D|=Omega(D)` distinct selected penetration contacts.

---

## 3. Extract a linear matching of penetration contacts

Let `P_D` be the graph formed by the selected penetration edges.  It has

```math
|E(P_D)|=|X_D|=\Omega(D).
```

The full triangle-free contact graph has maximum degree at most five by C26, so

```math
\Delta(P_D)\le5.
```

A greedy matching therefore has size at least

```math
{ |E(P_D)|\over2\Delta(P_D)-1}
\ge {|X_D|\over9}.
```

Hence there is a penetration-contact matching `M_D` with

```math
\boxed{
|M_D|
\ge0.00535859179328229D-o(D).
}
\tag{PB.4}
```

For each edge of `M_D`, retain the orientation whose selected tail endpoint is `x` and
retain its chosen blocker `y(x)`.  The pairs `(x,w)` are already vertex-disjoint.

---

## 4. Blocker conflicts have sublinear degree

Build a conflict graph `C_D` on the matched penetration edges.  Two matched edges are
adjacent in `C_D` if their associated triples

```math
\{y(x),x,w(x)\}
```

share a physical source point.

Because `M_D` is a matching, the `x,w` endpoint sets of different vertices of `C_D`
are disjoint.  Therefore conflicts can arise only through blocker points.

The blocker-reuse theorem says one physical source point blocks only `o(D)` of the
original selected loaded sides, uniformly over the source.  Restricting to one
occurrence per physical tail and then to `M_D` can only decrease this multiplicity.
Thus:

- if one gadget's blocker `y` is also the blocker of other gadgets, there are only
  `o(D)` such other gadgets;
- if `y` equals an `x` or `w` endpoint of another matched contact, there is at most one
  such matched contact because `M_D` is a matching;
- if this gadget's `x` or `w` is used as a blocker by other gadgets, each such fixed
  physical point is a blocker for only `o(D)` retained selected sides.

Consequently

```math
\boxed{
\Delta(C_D)=o(D).
}
\tag{PB.5}
```

---

## 5. Greedy independent set gives pairwise vertex-disjoint gadgets

The conflict graph has

```math
|V(C_D)|=|M_D|=\Omega(D),
```

and maximum degree `o(D)`.  Greedy vertex deletion therefore yields an independent set
of size at least

```math
{|M_D|\over\Delta(C_D)+1}
={\Omega(D)\over o(D)}
\longrightarrow\infty.
```

The corresponding triples share no physical source point by the definition of the
conflict graph.  They retain (PB.2)--(PB.3), proving Theorem PB.1.

---

## 6. Geometric orientation of each gadget

The Type-II disk limit and the blocker-reuse proof give more qualitative orientation.
For every retained gadget, `y` is asymptotically antipodal to `x` about the common
near-disk center, while the loaded-side normal at `x` is asymptotically radial.
Therefore the vector from `x` toward `y` is asymptotically in the loaded-side inward
normal direction.

The penetration contact `xw` has inward normal component `>gamma_0>1/2`.  Hence both
long and short legs of each gadget point into the same macroscopic inward half-plane
from `x`:

- `xy` is length `D-O(1)` and asymptotically radial/antipodal;
- `xw` is length one and has a fixed positive projection onto that direction, up to
  `o(1)` angular error.

This orientation statement is qualitative; no finite uniform lower bound stronger than
(PB.3) is needed by the extraction theorem.

---

## 7. Frontier effect

The reflection branch is now localized to a distributed collection of positive-core
boundary gadgets.  It cannot be realized by

- one or finitely many blocker hubs;
- repeated occurrences of a bounded set of physical tails; or
- one high-degree penetration-contact vertex.

The next closing target can therefore be phrased locally but summed globally:

```math
\boxed{
\text{many disjoint unloaded }x
\text{ with a unit inward contact and a }D-O(1)\text{ antipodal partner}
\Longrightarrow
\text{diameter/KKT or finite-motion contradiction}.
}
```

A proof must still use information beyond unit separation and near-circular geometry;
near-regular circular configurations can contain many `D-O(1)` pairs.  The new content
is the simultaneous positive-contact brace at every route endpoint.

C-II remains open.
