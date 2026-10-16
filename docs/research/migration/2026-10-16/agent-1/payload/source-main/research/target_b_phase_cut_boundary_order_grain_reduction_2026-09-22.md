# Target B: phase-cut boundary-order grain reduction

**Phase 2 preservation provenance:** PR #561, branch astra-b-phase-interface-20260921-a, audited source head 28256015fbb9343691446563f84e79745c22fcb4. Preserve as an unreviewed proof-only candidate; it yields an existential quadratic retained grain and does not establish the Target B shell inequality or one dominant grain.

**Date:** 2026-09-22
**Classification:** proved candidate awaiting independent audit
**Target:** the multi-grain/globalization obstruction in Target B
**Level I status:** open; Target B status unchanged

## 1. Candidate implication

The candidate lemma is

```text
canonical phase cut + strict pure-disk shell window
    -> O(D) deleted physical rhombi
    -> O(D) total retained-grain interface perimeter
    -> at least one quadratic retained phase-cut grain
    -> reduce the multi-grain branch to a bounded-interface macroscopic grain
       plus the still-missing coupling to the global diameter/shell inequality.
```

The exact canonical quantity strengthened is the physical interface budget in the
multi-grain obstruction.  The result does not by itself imply the Target B shell
inequality, because a finite collection of macroscopic grains can still partition a
near-disk through interfaces of length `O(D)`.

The argument uses only the canonical Target B phase-cut theorem (PC) from
`docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md`, the canonical strict
pure-rhombic shell window `G+E<c_0 B` from Sections 25/36 of the Target B module,
and elementary planar isoperimetry.  It does not use the unpromoted multi-grain
report as a premise.

## 2. Setup

Consider a triangle-free, pure, simply connected strict-rhombic-disk global
minimizer in the jammed Target B branch.  Use the following notation:

* `R` is the number of rhombi;
* `T` is the number of trains, so the rhombic outer boundary has `B=2T` unit
  edges;
* `a_0=sqrt(3)/2` and `c_0=sqrt(3)/4=a_0/2`;
* `E=sum_F(sin(theta_F)-a_0)` is the rhombic angular-area surplus;
* `G=area(K)-sum_F area(F)` is the convexification/pocket area, so `G>=0`;
* `kappa=2+sqrt(3)`.

Triangle-freeness makes every acute rhombus angle strictly larger than `pi/3`,
so `E>=0`.  The strict translated-triangular-lattice comparison gives the
canonical pure-disk shell window

```text
G+E < c_0 B = a_0 T.                         (2.1)
```

In particular,

```text
E < a_0 T.                                   (2.2)
```

## 3. Boundary-order phase cut

The canonical PC theorem supplies a set `F` of train-crossing edges such that

```text
|F| <= floor(3 Delta/pi) <= kappa E,          (3.1)
```

where `Delta` is the total angular defect.  Each train-crossing edge is one
physical rhombus, so `F` can be deleted as a set of physical rhombi.  The retained
train-crossing graph has a real phase potential and three modulo-`pi/3` labels on
every retained edge.  No physical source point is deleted by this operation; only
the selected rhombus faces are removed from the grain decomposition.

Combining (2.2) and (3.1) gives the boundary-order estimate

```text
|F| < kappa a_0 T = O(T).                     (3.2)
```

The canonical jammed estimates give `T=O(D)`, hence

```text
|F|=O(D).                                     (3.3)
```

This is the missing scale improvement over the raw Section-50 minimum-degree
pruning cost `O(lambda D^2)`.  It is important that (3.3) uses the global shell
window; PC alone only gives `O(Delta)`.

## 4. Exact retained-grain perimeter budget

Let `H_1,...,H_m` be the nonempty connected components of the retained
train-crossing graph.  Let `U_j` be the union of retained rhombi whose crossing
edges lie in `H_j`, allowing `U_j` to have several Euclidean connected components,
and let `P_j` be the sum of the Euclidean perimeters of those components.  Let
`R_j` be the number of retained rhombi in `U_j`.

### Lemma 4.1 (adjacency respects retained train components)

If two retained rhombi share a unit edge, their train-crossing edges lie in the
same `H_j`.

**Proof.**  The train passing through their common unit edge also passes through
both rhombi.  Their two crossing edges in the train-crossing graph therefore share
that train vertex.  Since neither crossing edge was deleted, they are in the same
connected component. `square`

### Lemma 4.2 (exact interface budget)

```text
sum_j P_j <= B+4|F| = 2T+4|F|.                (4.1)
```

**Proof.**  A boundary edge of a retained rhombus union is either an original
outer boundary edge or is adjacent, on its other side, to a deleted rhombus.
Lemma 4.1 rules out an interface edge directly separating two different retained
train components.  Each original outer edge is counted at most once among the
`P_j`, and each deleted rhombus has four sides, each of which can contribute to at
most one retained boundary edge.  Summing gives (4.1). `square`

This is an exact finite statement; no phase coherence, minimum-degree, or
asymptotic assumption is hidden in it.

## 5. Isoperimetric population bound

Every retained rhombus has area at least `a_0`, so `area(U_j)>=a_0 R_j`.  Apply
the planar isoperimetric inequality to each Euclidean connected component of
`U_j`, then sum:

```text
P_j >= 2 sqrt(pi) sum_r sqrt(area(U_{j,r}))
    >= 2 sqrt(pi area(U_j))
    >= 2 sqrt(pi a_0 R_j).                      (5.1)
```

Combining (4.1) and (5.1) yields the exact finite candidate theorem

```text
boxed{
  sum_j sqrt(R_j) <= (T+2|F|)/sqrt(pi a_0).
}                                                (5.2)
```

This is the physical interface version of the phase cut.  It remains valid when a
retained train component has several Euclidean pieces or holes, since those only
increase the perimeter counted in (5.1).

## 6. A forced quadratic grain

Let `R_ret=sum_j R_j=R-|F|` and `R_max=max_j R_j`.  Since

```text
R_ret = sum_j sqrt(R_j)sqrt(R_j)
       <= sqrt(R_max) sum_j sqrt(R_j),
```

(5.2) gives

```text
boxed{
 R_max >= pi a_0 (R-|F|)^2/(T+2|F|)^2.
}                                                (6.1)
```

For an unbounded sequence of pure-disk survivors, the canonical jammed asymptotics
give `R/D^2 -> 1/c`, with `c=2sqrt(3)/pi`, while `T=O(D)` and (3.3) gives
`|F|=O(D)`.  Therefore every such sequence contains a retained grain with

```text
R_max = Omega(D^2),                              (6.2)
```

and its Euclidean retained union has area `Omega(D^2)` and perimeter `O(D)`.
More explicitly, on any subsequence for which

```text
T/D -> x in (0,infinity),   |F|/D -> f,
```

the exact finite bound gives

```text
liminf R_max/D^2
 >= pi a_0/c^2 /(x+2f)^2.                         (6.3)
```

Using only PC and the shell window, `f<=kappa a_0 x` along such a subsequence,
so the weaker parameter-only form is

```text
liminf R_max/D^2
 >= pi a_0 /
    (c^2 x^2 (1+2 kappa a_0)^2) > 0.              (6.4)
```

The grain is a component of the boundary-order phase cut: all of its retained
crossings obey the exact PC real-potential/three-label relation.  Thus (6.2) is
stronger than merely finding an arbitrary dense subgraph after quadratic pruning.

## 7. What this closes and what remains

This proves the upstream target identified in the multi-grain handoff: a coherent
phase-cut decomposition with only boundary-order physical deletion cost exists in
the pure-disk global-minimizer branch.  In particular, the previous `O(lambda D^2)`
interface loss is not necessary for obtaining a macroscopic retained grain.

It does **not** prove any of the following:

* that the quadratic grain carries all but `o(D^2)` rhombi;
* that its local phase deficit is small enough for GPI;
* that interfaces between several quadratic grains force a strict diameter decrease;
* the joint Oler/isodiametric shell inequality;
* Target B or Level I closure.

The exact remaining bridge is now narrower:

```text
quadratic PC grain(s), total interface perimeter O(D)
    -> either one grain carries the global density needed by GPI,
       or a finite-interface multi-grain diameter/shell contradiction.
```

The first alternative is not automatic: (6.4) has a potentially small constant, and
the global cardinality may be split among several grains.  The second alternative
requires a relative-isoperimetric or train-interface estimate that uses the active
diameter constraints; plain area bookkeeping permits finitely many macroscopic
grains separated by an `O(D)` seam.

## 8. Hostile audit

* `F` is a set of crossing edges/rhombi, not a set of source points.  No source
  deletion or global-minimizer replacement is inferred.
* `G>=0` follows from disjoint rhombus interiors lying in `K`; no unproved pocket
  convexity is used.
* `E>=0` uses strict triangle-freeness of every rhombus, not merely local
  almost-rhombicity.
* The shell input is the strict pure-disk global-minimizer inequality (2.1), not
  the weaker unpromoted area estimate.
* A retained train component may have several Euclidean components; (5.1) is
  applied componentwise, so no connectedness shortcut is present.
* A deleted rhombus has four sides, giving an upper bound on interface perimeter;
  the proof does not assume every deleted side is exposed.
* The conclusion is existential in the retained grain.  It does not assert that
  every global minimizer has one selected grain, nor that one grain is a global
  minimizer for its own cardinality.

## 9. Status

The finite inequalities (3.1), (4.1), (5.1), and (6.1) are proved candidates.
The asymptotic `Omega(D^2)` consequence is a proved candidate under the canonical
pure-disk jammed hypotheses.  Independent audit and promotion would need to register
this as a corollary of `TB-DENSE-GRID`; no theorem-state or route-map mutation is
made here because the global Target B endpoint remains open.
