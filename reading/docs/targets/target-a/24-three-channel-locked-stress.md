> Generated reading edition · [exact source](../../../../docs/targets/target-a/24-three-channel-locked-stress.md) · source SHA-256 `8b2605132bd24627a54f06442b69e07c92b50a9d7426bdf12d1cd01dcffc581f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target A — three-channel transmission from a locked response triangle

The Section-159 locked-triangle certificate gives a nonnegative contact/facet
stress.  Section 171 used block structure to obtain a proper contact crosscut.  The
stress actually implies a stronger vertex-connectivity statement: the locked triangle
cannot be separated from the reaction support by fewer than three vertices.  Hence all
three triangle vertices have vertex-disjoint positive-contact channels to three
distinct response-hull reaction vertices.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 172. Harmonic convex-hull principle and three disjoint stress channels

Retain the actual-response locked branch and notation of Sections 169 and 171.  Let
`G_+` be the positive-contact component containing the locked unit equilateral triangle
```math
T_*=\{t_1,t_2,t_3\},
\tag{172.1}
```
and let
```math
R_+=\{r\in V(G_+):r\text{ carries nonzero facet reaction}\}.
\tag{172.2}
```
Theorem 159.1 gives `|R_+|>=2`; the result below strengthens this automatically.

For a nonreaction vertex `i`, the equilibrium equation is
```math
\sum_{j}\alpha_{ij}(p_i-p_j)=0,
\qquad \alpha_{ij}>0
\tag{172.3}
```
over its positive-contact neighbors.  Hence
```math
p_i=
\frac{\sum_j\alpha_{ij}p_j}{\sum_j\alpha_{ij}}.
\tag{172.4}
```
Thus every nonreaction vertex is a strict weighted barycenter of its positive-contact
neighbors.

## 172.1 Discrete maximum principle with an arbitrary vertex boundary

> **Lemma 172.1 (harmonic convex-hull lemma).**  Let `W subset V(G_+)`, and let `H`
> be a connected component of `G_+-W` containing no reaction vertex.  If `H` has a
> graph neighbor in `W`, then
> 

```math
> \boxed{
> \{p_h:h\in H\}
> \subseteq
> \operatorname{conv}\{p_w:w\in N(H)\cap W\}.
> }
> \tag{172.5}
> 
```

### Proof

Put `B=N(H) cap W`.  Every positive-contact neighbor of a vertex in `H` lies in
`H sqcup B`, and every vertex of `H` has zero reaction.  Let `ell` be any linear
functional.  Suppose
```math
\max_{h\in H}\ell(p_h)>\max_{b\in B}\ell(p_b).
\tag{172.6}
```
Choose a vertex `h_0` maximizing `ell` on `H`.  Equation (172.4) says its value is a
positive weighted average of neighbor values, all at most the same maximum.  Hence
every positive-contact neighbor of `h_0` also has the maximum value.  Propagating
through the connected component `H`, every vertex of `H` has that value.  Since `H`
has a neighbor in `B`, applying (172.4) at a boundary-adjacent vertex forces that
neighbor in `B` to have the same value, contradicting (172.6).  Therefore
```math
\max_H\ell\le\max_B\ell.
\tag{172.7}
```
Applying the same statement to `-ell` gives the corresponding lower bound.  Since
these inequalities hold for every linear functional, the finite-dimensional
separation theorem gives (172.5).  $`\square`$

## 172.2 No two-vertex separator can isolate the locked triangle

> **Theorem 172.2 (three-vertex reaction connectivity).**  If a vertex set
> `W subset V(G_+)` separates all vertices of `T_*\setminus W` from
> `R_+\setminus W`, then
> 

```math
> \boxed{|W|\ge3.}
> \tag{172.8}
> 
```

### Proof

Assume `|W|<=2`.  Since `T_*` is a three-cycle, the nonempty set `T_*\setminus W`
lies in one connected component `H` of `G_+-W`.  By the separation assumption, `H`
contains no reaction vertex outside `W`.  The full graph `G_+` is connected and has a
reaction vertex by Theorem 159.1, so unless `W` is empty and already impossible, `H`
has a graph neighbor in `W`.  Lemma 172.1 gives
```math
\{p_h:h\in H\}
\subseteq\operatorname{conv}p(W).
\tag{172.9}
```
For `W=emptyset`, a finite connected graph all of whose vertices satisfy the strict
barycentric relation (172.4) is impossible by the same maximum-principle argument, so
this case is excluded directly.

It remains to show that (172.9) contradicts the equilateral triangle for every
`1<=|W|<=2`.

If `|W|=1`, the right side of (172.9) is one point, while
`T_*\setminus W` contains at least two distinct triangle vertices unless the sole
separator vertex is outside `T_*`, in which case it contains all three.  Either way
(172.9) is impossible.

Let `|W|=2`.  If `W` contains no triangle vertex, all three noncollinear vertices of
`T_*` lie in `H`, but `conv p(W)` is a line segment.  If `W` contains exactly one
triangle vertex, the other two triangle vertices lie in `H`.  The segment joining the
two separator points cannot contain both of those vertices: one separator endpoint is
the third vertex of the equilateral triangle, which is not collinear with the other
two.  Finally, if `W` contains two triangle vertices, the remaining third triangle
vertex lies in `H` but is not on the segment joining those two separator vertices.
All possibilities contradict (172.9).  Therefore `|W|>=3`.  $`\square`$

This argument permits the separator to contain triangle vertices or reaction vertices;
there is no hidden terminal-exclusion convention.

## 172.3 Three vertex-disjoint reaction channels

The terminal sets `T_*` and `R_+` may overlap, so use an explicit vertex-capacitated
network rather than a convention-dependent set-Menger statement.  Split every vertex
`x of G_+` into `x^- -> x^+` with capacity one.  Replace each undirected
positive-contact edge `xy` by infinite-capacity arcs `x^+ -> y^-` and
`y^+ -> x^-`.  Add a supersource joined by infinite-capacity arcs to `t_i^-` for the
three vertices `t_i in T_*`, and join every `r^+`, `r in R_+`, to a supersink by an
infinite-capacity arc.  When a triangle vertex is itself a reaction vertex, the route
through its own capacity-one split edge represents the corresponding zero-contact-edge
channel.

Any finite source--sink cut of capacity at most two consists of at most two vertex
split edges and therefore corresponds to a set `W subset V(G_+)`, `|W|<=2`, that
separates `T_*\setminus W` from `R_+\setminus W`.  Theorem 172.2 excludes such a cut.
On the other hand the three split edges belonging to `T_*` form a cut of capacity
three.  Hence the minimum cut has capacity exactly three.  Integral max-flow gives
three vertex-disjoint `T_*`--`R_+` channels in the original graph, with a trivial
length-zero channel allowed exactly when its triangle endpoint is already a reaction
vertex.

> **Corollary 172.3 (three-channel locked stress).**  There exist three pairwise
> vertex-disjoint positive-contact paths
> 

```math
> P_i:t_i'\leadsto r_i
> \qquad(i=1,2,3)
> \tag{172.10}
> 
```
> with
> 

```math
> \{t_1',t_2',t_3'\}=T_*,
> \qquad
> r_1,r_2,r_3\in R_+
> \tag{172.11}
> 
```
> and the three reaction endpoints `r_i` distinct.  A path is permitted to have zero
> edges only when `t_i'=r_i`.  In particular
> 

```math
> \boxed{|R_+|\ge3.}
> \tag{172.12}
> 
```
> and all three `r_i` lie in
> 

```math
> X^*\cap\partial K^*\subseteq X^\partial.
> \tag{172.13}
```

For each path, stop at its first vertex on `partial K^*`.  The resulting three paths
remain pairwise vertex-disjoint, have distinct boundary endpoints, and have no other
boundary vertex.  Whenever their starting triangle vertex is interior, their open
polygonal arcs lie in `int K^*`.

## 172.4 Crosscut fan consequences

If all three locked-triangle vertices lie in `int K^*`, the three truncated paths are
three internally disjoint spokes from the triangle to three distinct boundary points.
For every pair `i!=j`, concatenate the `i`-th spoke, the unit triangle edge
`t_i't_j'`, and the reverse of the `j`-th spoke.  The unit-contact graph is plane, so
this is a simple positive-contact crosscut.  Thus the locked stress supplies three
pairwise related crosscuts surrounding the central triangle.

If one or two triangle vertices lie on the hull boundary, the same construction gives
at least two proper crosscuts.  If all three lie on the boundary, Theorem 171.3 still
guarantees at least one proper triangle-edge crosscut for `m^*>3`; additional spokes
may or may not be nontrivial.

These multiple channels are stronger input for the Section-170 separator inequality
than a single arbitrary boundary path.  They still do not by themselves control the
side population imbalance or the total shielding cost.

## 172.5 New exact locked-branch target

The qualitative stress transport is now complete at vertex-connectivity level:

1. the locked triangle is in the actual response point set;
2. its positive stress reaches the actual response boundary;
3. the triangle and reaction support have vertex connectivity at least three;
4. three disjoint positive-contact channels reach three distinct boundary vertices;
5. at least one proper contact crosscut exists, and in the interior-triangle case a
   three-crosscut fan is available.

The remaining theorem is quantitative: use this three-channel fan, rather than one
crosscut in isolation, to force
```math
\boxed{\zeta\ge s=\Delta_\Lambda-d_{\rm int}}
\tag{172.14}
```
or a strict-diameter replacement.  A promising exact formulation is a
**three-sector imbalance theorem** in which the three spokes partition the response
hull and the sum of sector terminal deficits is compared with the union of their
lattice shielding neighborhoods.
