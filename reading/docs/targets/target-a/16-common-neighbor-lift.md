> Generated reading edition · [exact source](../../../../docs/targets/target-a/16-common-neighbor-lift.md) · source SHA-256 `411c1dd9f972979029c541ef65c9c249722ac385369d4bb0bf6cdfd7a59c46c7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — triangular-lattice common-neighbor lift

This audited addendum continues Section 163. Section 163 couples the two separately
constructed source shadows by noncrossing geometry and common-source V-paths. The result
below is stronger in a different direction: a strict-conflict edge from the smaller
optimum to the source can be lifted locally to an actual scaffold conflict through a
common triangular-lattice site. A bounded-degree selection then gives a linear-size
family of vertex-disjoint source-certified scaffold edges.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 164. Common-neighbor lift for the triangular lattice

Let `Lambda` be the unit triangular lattice. For a point `z` put
$$
N_\Lambda(z)=\{\lambda\in\Lambda:|z-\lambda|<1\}.
\tag{164.1}
$$
Call `z` generic when no lattice distance is exactly one and `z` is not a lattice
point. Section 79 proves that for generic `z`, the set `N_Lambda(z)` has three or four
vertices and its convex hull is respectively an elementary unit triangle or a unit
lozenge containing `z` in its interior.

## 164.1 A unit-distance Helly property

> **Theorem 164.1 (common triangular-lattice neighbor).** Let `x` be generic with
> respect to the unit triangular lattice, and let `a` be any point satisfying
> 

$$

> |x-a|<1.
> \tag{164.2}
> 
$$


> Then
> 

$$

> \boxed{N_\Lambda(x)\cap N_\Lambda(a)\ne\varnothing.}
> \tag{164.3}
> 
$$


> Equivalently, there is a lattice site `y` such that
> 

$$

> |x-y|<1,
> \qquad
> |a-y|<1.
> \tag{164.4}
> 
$$



### Proof

By a lattice isometry, there are only the two Section-79 cell types.

### Triangle cell

Put
$$
A=(0,0),\quad B=(1,0),\quad
C=\left(\frac12,\frac{\sqrt3}{2}\right),
\tag{164.5}
$$
and suppose
$$
N_\Lambda(x)=\{A,B,C\}.
$$
Then `x` lies in the interior of `ABC`. The three lattice vertices immediately across
the sides are
$$
D=\left(\frac12,-\frac{\sqrt3}{2}\right),\quad
E=\left(-\frac12,\frac{\sqrt3}{2}\right),\quad
F=\left(\frac32,\frac{\sqrt3}{2}\right).
\tag{164.6}
$$
Because the strict neighborhood is exactly `{A,B,C}`,
$$
|x-D|\ge1,
\qquad |x-E|\ge1,
\qquad |x-F|\ge1.
\tag{164.7}
$$

Let
$$
U=B(A,1)\cup B(B,1)\cup B(C,1)
\tag{164.8}
$$
be the union of the three open unit disks. Its outer boundary consists of the three
exposed circular arcs joining `D,E,F`: the arc centered at `A` joins `D` to `E`, the
arc centered at `B` joins `F` to `D`, and the arc centered at `C` joins `E` to `F`.
For a point inside `ABC`, the closest point on each exposed arc is one of that arc's
endpoints. This follows directly from polar angles: at each center, the directions to
points of `ABC` lie in the inward `60 degree` vertex cone, while the exposed arc lies
in the complementary outward angular interval, so the cosine in the squared-distance
formula is maximized at an endpoint. Hence
$$
\operatorname{dist}(x,\mathbb R^2\setminus U)
=\min\{|x-D|,|x-E|,|x-F|\}\ge1.
\tag{164.9}
$$
Therefore every point at distance strictly less than one from `x`, in particular `a`,
lies in `U`. Thus `a` lies strictly inside at least one of the three unit disks in
(164.8), proving (164.3).

### Lozenge cell

After reflection if necessary, put
$$
D=\left(\frac12,-\frac{\sqrt3}{2}\right)
$$
and suppose
$$
N_\Lambda(x)=\{A,B,C,D\}.
\tag{164.10}
$$
Then `x` lies in the interior of the unit lozenge with those four vertices. The four
outer adjacent lattice vertices are
$$
E=\left(-\frac12,\frac{\sqrt3}{2}\right),\quad
F=\left(\frac32,\frac{\sqrt3}{2}\right),\quad
G=\left(-\frac12,-\frac{\sqrt3}{2}\right),\quad
H=\left(\frac32,-\frac{\sqrt3}{2}\right).
\tag{164.11}
$$
They do not belong to `N_Lambda(x)`, so
$$
|x-E|,|x-F|,|x-G|,|x-H|\ge1.
\tag{164.12}
$$

Let
$$
U=B(A,1)\cup B(B,1)\cup B(C,1)\cup B(D,1).
\tag{164.13}
$$
Its exposed boundary has four arcs, with consecutive endpoint pairs
$$
(E,G),\quad(G,H),\quad(H,F),\quad(F,E),
\tag{164.14}
$$
centered respectively at the four lozenge vertices. For a point in the lozenge, the
same polar-angle check shows that the nearest point on each exposed arc is one of its
endpoints: the vector from a lozenge vertex to `x` lies in its inward vertex cone,
whereas the exposed arc occupies the opposite outer angular interval. Consequently
$$
\operatorname{dist}(x,\mathbb R^2\setminus U)
=\min\{|x-E|,|x-F|,|x-G|,|x-H|\}\ge1.
\tag{164.15}
$$
Again `B(x,1) subset U`, so (164.2) puts `a` in a unit disk centered at one of
`A,B,C,D`. That center belongs to both strict neighborhoods. $\square$

No equality-case sharpness statement is needed here; every later application uses the
strict hypothesis `|x-a|<1`.

## 164.2 Source-certified scaffold conflicts

Return to the Section-155 common placement. Let `Lambda'` be the actual generic
triangular-lattice phase used for the compatible scaffold. Section 79 makes every
`x in X_m` generic for this phase. Put
$$
Y_{\rm in}=\Lambda'\cap\operatorname{int}(K_m+\mathbb B).
\tag{164.16}
$$
As before, write
$$
p=\widehat p_H.
\tag{164.17}
$$
Section 155 gives a strict-conflict matching `M_X` from `X_m` into the genuine source
`A` with
$$
|M_X|\ge m-p.
\tag{164.18}
$$

> **Theorem 164.2 (source-certified scaffold matching).** There are
> pairwise vertex-disjoint triples
> 

$$

> (x_i,a_i,y_i)
> \in X_m\times A\times Y_{\rm in},
> \qquad 1\le i\le q,
> \tag{164.19}
> 
$$


> such that
> 

$$

> \boxed{
> |x_i-a_i|<1,
> \quad |a_i-y_i|<1,
> \quad |x_i-y_i|<1,
> }
> \tag{164.20}
> 
$$


> and
> 

$$

> \boxed{
> q\ge\frac{m-p}{5}
> >\frac m5-\frac{\pi D}{10}.
> }
> \tag{164.21}
> 
$$


> In particular, the edges `x_i y_i` form a matching in the compatible
> `X_m--Y_in` scaffold conflict graph, and every one of those scaffold edges has a
> distinct genuine-source mediator `a_i` that strictly conflicts with both endpoints.

### Proof

For every edge `x-a` of `M_X`, Theorem 164.1 supplies at least one lattice site `y`
with
$$
|x-y|<1,
\qquad |a-y|<1.
\tag{164.22}
$$
Since `x in K_m`, the first strict inequality puts `y` in `Y_in`.

Form an auxiliary bipartite graph whose left vertices are the matching edges of `M_X`
and whose right vertices are `Y_in`; join the left vertex `(x,a)` to every common
lattice neighbor `y` satisfying (164.22). Every left vertex has degree at least one.
A right vertex `y` is adjacent to at most five left vertices, because distinct left
vertices have distinct `X_m` endpoints and Corollary 79.3 gives degree at most five on
the lattice side of the compatible `X_m--Y_in` conflict graph.

Choose one auxiliary neighbor for every left vertex. Since no right vertex is chosen
more than five times, the set of chosen right vertices has size at least `|M_X|/5`.
Retain one left vertex for each distinct chosen right vertex. The retained `x` and `a`
are distinct because `M_X` is a matching, and the retained `y` are distinct by
construction. This gives (164.19)--(164.21). The last strict inequality uses
`p<pi D/2`. $\square$

This is a direct source-to-compatible-scaffold transport theorem. It concerns the
pre-terminalized `m`-point scaffold; Section 165 upgrades the same mechanism to the
actual plateau-terminalized response shore `X^*`.

## 164.3 Diameter-cover obstruction produces rattler-certified scaffold edges

Use the source decomposition
$$
A=P\sqcup R,
\qquad |P|=m,
\tag{164.23}
$$
and let `tau=tau_D(A)` be the source-backbone diameter-cover number. In the Section-155
regime `t>1`, so the radius-one source-backbone theorem applies.

> **Corollary 164.3 (rattler-certified scaffold supply).** Among the triples in the
> construction above one may choose at least
> 

$$

> \boxed{
> q_R\ge\frac{\max\{0,\tau-p\}}5
> }
> \tag{164.24}
> 
$$


> pairwise vertex-disjoint triples
> 

$$

> x_i-r_i-y_i,
> \qquad r_i\in R,
> \tag{164.25}
> 
$$


> satisfying all three strict inequalities in (164.20).

### Proof

The edges of `M_X` whose source endpoint lies in `P` form a matching in the
source-backbone radius-one graph. Theorem 157.1 of that module bounds their number by
`m-tau`. Since `|M_X|>=m-p`, at least `tau-p` edges of `M_X` end in strict rattlers,
when this number is positive. Apply the auxiliary common-neighbor selection from the
proof of Theorem 164.2 only to those edges. The same lattice-side degree-five bound
loses at most the factor five. $\square$

Thus every unit of source diameter-cover obstruction beyond the exact source-hull
capacity slack produces, up to a fixed factor five, a genuine strict-rattler-mediated
edge of the compatible scaffold conflict graph. Section 165 gives the stronger
plateau-amplified count on the actual response shore.

## 164.4 Exact status and next bridge

Theorems 164.1--164.2 replace a purely abstract source matching by a large family of
co-embedded three-shore conflict certificates. They do **not** imply Hall deficiency:
a large matching in the scaffold conflict graph points in the opposite combinatorial
direction from the old Hall-surplus target, and the strained-monomer regressions show
that abundant local monomer incidence can be Hall-neutral. Nor does planarity alone
turn the certificates into Schur nullity.

The exact Target A endpoint remains
$$
\boxed{\dim\ker S\ge\Delta_\Lambda-d_{\rm int}}
\tag{164.26}
$$
or an `N`-point unit-separated configuration of diameter strictly below `D`.

The pre-terminalized theorem is used only as a local lift. Section 165 supplies the
required scope correction: the same construction labels all but at most `p` vertices
of the actual response shore `X^*`, including all but at most `p` Schur terminals.
