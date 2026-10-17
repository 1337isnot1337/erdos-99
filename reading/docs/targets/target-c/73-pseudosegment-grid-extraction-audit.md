> Generated reading edition · [exact source](../../../../docs/targets/target-c/73-pseudosegment-grid-extraction-audit.md) · source SHA-256 `5185283ec35ab657bb030f75a901e00cdb5fcf1433501e5535143c2ca91bbd6a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — pseudosegment grid-extraction audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module advances the quadratic positive-core branch after canonical Section 69.
Its purpose is narrow: holes and boundary-order interfaces do not prevent extraction
of a linear-by-linear complete train grid from the quadratic coherent physical grain.
It does not yet prove the subsequent penetration/common-order theorem needed for a
diameter contradiction.

The proof uses:

- canonical Section 69 for one physically connected `epsilon`-coherent grain with
  `R=Omega(D^2)` retained strict unit rhombi and perimeter `P=O_epsilon(D)`;
- canonical Theorem 10.6 in `docs/theory/01-local-structure.md`, which applies to
  arbitrary finite edge-to-edge strict-rhombus complexes, including complexes with
  holes, and makes their train centerlines pseudosegments;
- Fox--Pach--Suk, *A structure theorem for pseudo-segments and its applications*,
  arXiv:2312.01028, Theorem 2.12, which records the Fox--Pach pseudosegment density
  theorem: `N` pseudosegments with at least `eta N^2` crossing pairs contain two
  all-crossing subcollections, each of size at least `c_PS eta N` for one absolute
  constant `c_PS>0`.

The external theorem statement was checked directly. Its hypothesis counts crossing
pairs, and its conclusion is linear in `eta N`; there is no logarithmic loss.

Canonical Sections 70--72 are not dependencies of this theorem.

---

# 73. Dense coherent train grains contain linear complete crossing grids

Fix one `epsilon`-coherent physical grain `G` supplied by Section 69. Write

- `R` for its retained strict unit-rhombus faces;
- `T` for its local train segments;
- `P` for its physical perimeter, including hole boundaries.

Section 69 gives exactly

```math
\boxed{2T=P.}
\tag{73.1}
```

The endpoint convention in the Section-69 phase-bin cut is understood in the
endpoint-safe form: choose a nonexceptional shift for which no train potential lies
on a bin boundary and delete exactly the crossings whose two endpoint potentials lie
in different half-open bins. There are only finitely many exceptional shifts, so this
changes neither the coarea integral nor any `O_epsilon(D)` bound. Thus every train
vertex belonging to the physical grain lies in one well-defined phase bin.

## 73.1 Train centerlines are pseudosegments, with exactly `R` crossing pairs

Apply Theorem 10.6 to the rhombi of `G`. It does not require simple connectedness.
Each local train centerline is a simple arc; two train centerlines cross in at most
one rhombus; no train closes; and

```math
\boxed{R\le {T^2\over4}.}
\tag{73.2}
```

Every retained rhombus is the proper transverse crossing of its two local train
centerlines. Conversely two train centerlines can meet only in such a rhombus.
Because a pair crosses at most once, the collection of `T` train centerlines has
**exactly `R` crossing pairs**.

Theorem 10.6 also proves that the train-crossing graph is triangle-free. In
particular no three train centerlines are pairwise crossing.

Thus the centerlines are a collection of pseudosegments in the exact sense needed by
the external density theorem.

## 73.2 Fox--Pach gives a linear complete topological grid

Set

```math
\eta={R\over T^2}.
\tag{73.3}
```

The Fox--Pach theorem gives subfamilies `C_1,C_2` of the local train centerlines such
that every member of `C_1` crosses every member of `C_2` and

```math
\boxed{|C_1|,|C_2|\ge c_{PS}{R\over T}.}
\tag{73.4}
```

The two shores are automatically disjoint: a curve cannot cross itself. More
importantly, they are automatically internally pairwise noncrossing. If two members
of `C_1` crossed, then together with any member of nonempty `C_2` they would form a
triangle in the train-crossing graph, contradicting Theorem 10.6. The same argument
applies to `C_2`.

Therefore (73.4) is already a genuine complete topological train grid with two
internally noncrossing shores. No disk topology, complement-dual tree, endpoint order,
or minimum-degree pruning is used.

## 73.3 Phase purification loses only a factor three

Section 69 gives the grain one `epsilon`-wide three-phase frame with

```math
0<\epsilon<\pi/6.
\tag{73.5}
```

Every local train inherits a label `ell in Z/3`. Because the whole physical grain is
contained in one retained train component, all train potentials lie in one phase bin
of width at most `epsilon`. Consequently two trains carrying the same label have
projective directions separated by at most `epsilon<pi/6`.

An actual strict unit-rhombus crossing has acute projective separation strictly
larger than `pi/3`. Hence two same-label trains cannot cross.

Let `L_1,L_2 subset Z/3` be the phase-label supports used by `C_1,C_2`. Since
every member of `C_1` crosses every member of `C_2`, while same-label trains cannot
cross, the two supports are disjoint:

```math
L_1\cap L_2=\varnothing.
```

Both supports are nonempty subsets of a three-element set, so each has size at most
two. Choose the largest phase class in each shore and call the resulting families
`A subset C_1` and `B subset C_2`. Then the labels of `A,B` are distinct and

```math
|A|\ge {|C_1|\over2},
\qquad
|B|\ge {|C_2|\over2}.
```

Thus the sharper phase-purification bound is

```math
\boxed{
|A|,|B|\ge {c_{PS}\over2}{R\over T}.
}
\tag{73.6}
```

Both shores are internally noncrossing, the two shores have distinct actual phase
labels, and every `A`-train crosses every `B`-train in a retained rhombus. This is an
actual phase-pure complete grid in the contact geometry, not a virtual graph biclique.

## 73.4 Quadratic Section-69 grains yield linear-by-linear grids

Suppose a survivor subsequence is in the quadratic positive-core branch. Section 69
gives fixed constants `r,C>0` (after fixing `epsilon`) and one physical grain with

```math
R\ge rD^2,
\qquad
P\le CD.
\tag{73.7}
```

Equation (73.1) gives

```math
T\le {C\over2}D.
```

Equation (73.2) gives the complementary lower bound

```math
T\ge2\sqrt R\ge2\sqrt r\,D,
```

so `T=Theta(D)`. Substitution into (73.4) and (73.6) yields

```math
\boxed{
|C_1|,|C_2|
\ge {2c_{PS}r\over C}D,
}
\tag{73.8}
```

and

```math
\boxed{
|A|,|B|
\ge {c_{PS}r\over C}D.
}
\tag{73.9}
```

Therefore every quadratic coherent Section-69 grain contains both

1. a linear-by-linear complete topological train grid, and
2. a linear-by-linear complete **phase-pure** train grid.

The constants need not be numerically effective for the asymptotic conclusion.

## 73.5 What holes no longer obstruct

The older Target B grid extraction used a complement-dual tree and interval
neighborhoods in a topological disk. A Section-69 grain may have holes, so that route
cannot simply be quoted.

Equations (73.8)--(73.9) remove that obstruction completely at the extraction stage.
The proof sees only the actual train pseudosegments and their crossing density. Hole
boundaries can change how a train terminates, but they do not prevent the complete
linear grid from existing.

The remaining topology issue is downstream. A pure-disk penetration argument may use
that a train crossing deep into a grid cannot escape before meeting many more grid
lines, or that all crossings appear in one common order along every shore. In a holed
grain a train can terminate on a hole/deleted/interface boundary. Section 69 bounds
the **total** physical boundary by `O(D)`, but Section 73 does not yet turn that budget
into a penetration theorem.

Likewise, the additive Cartesian grid hypothesis used by Theorem 10.9 is not asserted
here. A complete pseudosegment grid does not by itself identify the crossing positions
with one global additive array `p+x_i+y_j`.

## 73.6 Exact interaction with the Section-69 branch split

Section 69 proves

```math
\boxed{m=R_4+O(D)}.
\tag{73.10}
```

Hence:

- if `m=Omega(D^2)`, Section 69 gives a quadratic coherent physical grain and Section
  73 gives the linear complete phase-pure grid (73.9);
- if `m=o(D^2)`, the grid theorem is not the relevant mechanism: asymptotically almost
  all source points lie outside the positive KKT contact core.

The quadratic branch has therefore advanced from

```text
quadratic coherent grain with O(D) physical boundary
```

to

```text
linear A x B complete phase-pure pseudosegment grid
inside that actual holed grain.
```

The next high-value theorem is a **boundary-budget penetration theorem**: show that
an `a x b` complete phase-pure train grid with `a,b=Omega(D)` inside a grain whose
total physical boundary is `O(D)` either contains a large trimmed subgrid with the
common-order/penetration behavior needed by Target B, or already forces a strict
sub-`D` competitor / diameter contradiction.

## 73.7 Dependency and regression audit

- **External theorem:** Fox--Pach--Suk Theorem 2.12 was checked directly; it states
  linear shore size `c_PS eta N` from `eta N^2` crossing pairs of pseudosegments.
- **Pseudosegment hypothesis:** canonical Theorem 10.6 proves simplicity and at-most-
  one crossing per train pair with no simple-connectedness assumption.
- **Crossing count:** every retained rhombus is one train-pair crossing and no train
  pair repeats, so the number of crossing pairs is exactly `R`.
- **Internal noncrossing:** the two Fox--Pach shores are automatically independent in
  the triangle-free train-crossing graph; this strengthens the stale PR #229 handoff.
- **Phase purification:** same-label trains cannot cross because their direction
  separation is `<pi/6`, while each strict rhombus crossing has separation `>pi/3`.
- **Endpoint-safe phase bins:** exclude the finite set of shifts placing a train
  potential on a bin boundary; this repairs the otherwise ambiguous boundary-vertex
  convention without changing the coarea estimate.
- **Holes:** retained. They are irrelevant to extraction but remain relevant to
  common-order and penetration.
- **Sections 70--72:** canonical but not used here.

## 73.8 Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Section 69:
    quadratic positive core
      -> one epsilon-coherent physical grain G,
         R>=rD^2 rhombi,
         P<=CD total physical perimeter,
         T=P/2=Theta(D) local train segments.

Theorem 10.6:
    train centerlines are pseudosegments;
    exactly R crossing pairs;
    train-crossing graph triangle-free.

Fox--Pach:
    C1,C2 all-crossing,
    |C1|,|C2| >= c_PS R/T = Omega(D).
Triangle-free crossing graph:
    each shore is internally noncrossing.

Section-69 phase frame:
    purify to distinct phase labels A,B,
    |A|,|B| >= (c_PS/2) R/T = Omega(D),
    every A crosses every B.

Remaining quadratic-core obstruction:
    convert O(D) total boundary into common-order / penetration control,
    or derive a direct diameter contradiction from the complete holed grid.

Complementary branch:
    m=o(D^2), with almost all source population outside the positive KKT core.
```
