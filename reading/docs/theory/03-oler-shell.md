> Generated reading edition · [exact source](../../../docs/theory/03-oler-shell.md) · source SHA-256 `a6cf18f38fa01c6969e2aecd8211278a0dcd1530efb190551d815ed0e86c0521`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Shared theory: Oler shell and boundary surplus

> Canonical v1.7.0 module. The original section numbering is preserved for
> cross-references; see the [documentation map](../README.md).

## 21. Addendum: an exact Oler-surplus decomposition for the defect shell

This addendum records the strongest new boundary-capacity result obtained in the
subsequent investigation.  It does not close Level I.  Its point is that the area,
perimeter, topology, holes, rhombic components, and vertices outside the rhombic
complex can be placed in one exact inequality with no unspecified boundary-order
constant.

Put

$$
a_0=\frac{\sqrt3}{2},\qquad c_0=\frac{\sqrt3}{4},\qquad
c=\frac{2\sqrt3}{\pi},\qquad
C_0=\pi\sqrt c=\sqrt{2\pi\sqrt3}.
$$

### 21.1 The finite Oler inequality and an improved universal diameter bound

The following finite packing inequality is the unsummed cell inequality relevant to
the present boundary problem.

**Lemma 21.1 (Oler inequality).**  If $X\subset K\subset\mathbb R^2$, where
$K$ is convex, $|X|=N$, and the mutual distances in $X$ are at least $1$,
then

$$
\boxed{
N\le \frac{2}{\sqrt3}\operatorname{area}(K)
       +\frac12\operatorname{per}(K)+1.
}
\tag{21.1}
$$

Equivalently,

$$
\boxed{
\operatorname{area}(K)+c_0\operatorname{per}(K)
\ge a_0(N-1).
}
\tag{21.2}
$$

For completeness, the standard proof is the Dirichlet-cell proof of the finite
hexagonal packing inequality before its boundary terms are discarded.  Intersect the
Voronoi cells of $X$ with a polygonal approximation to $K$, and join each cell
center to the consecutive vertices of its clipped cell.  Every internal Voronoi side
is at distance at least $1/2$ from each of its two centers.  On the resulting
triangles, symmetrization about the side and

$$
\tan u+\tan v\ge2\tan\frac{u+v}{2}
$$

give the regular circumscribed-hexagon value $a_0$ for each full cell after the
cell angles are summed.  Internal side terms cancel in pairs.  The uncancelled
boundary triangles contribute at worst $c_0$ times their total base length, and the
outer-face term in Euler's formula contributes one further $a_0$.  Thus

$$
a_0N\le \operatorname{area}(K)+c_0\operatorname{per}(K)+a_0.
$$

Passing from polygonal approximations to an arbitrary convex $K$ proves (21.2).
This is also sharp: collinear unit chains and convex triangular-lattice patches give
equality.

Applying (21.2), the isodiametric inequality, and Cauchy's perimeter inequality gives
a universal improvement of (2.2):

$$
a_0(n-1)
\le \frac{\pi D(n)^2}{4}+c_0\pi D(n).
$$

Consequently,

$$
\boxed{
D(n)\ge
\sqrt{\frac{2\sqrt3}{\pi}(n-1)+\frac34}
-\frac{\sqrt3}{2}.
}
\tag{21.3}
$$

Thus the additive loss in the universal planar lower bound improves from $1$ to
$\sqrt3/2=0.8660254037\ldots$.  The constant check is important: this remains a
positive constant below the strict lattice-averaging upper bound
$D(n)<\sqrt{cn}$, so (21.3) alone cannot prove Erdős #99.

### 21.2 Exact topology-corrected shell window

Let $A$ be an $n$-point unit-separated set and put
$K=\operatorname{conv}A$, $P=\operatorname{per}K$.  Let $\mathcal R$ be
any finite edge-to-edge complex of strict unit-rhombus faces whose vertices belong to
$A$.  Write

$$
R=|\mathcal R|,
\qquad B=B_{\mathcal R},
\qquad v=|V(\mathcal R)|,
\qquad t=n-v,
$$

and let $\chi=\chi(\mathcal R)$ be its Euler characteristic.  For a regular
planar complex with $r$ components and $h$ holes, $\chi=r-h$.  Define

$$
E_{\mathcal R}
=\sum_{F\in\mathcal R}
\left(\sin\theta_F-a_0\right),
\qquad
G_{\mathcal R}
=\operatorname{area}(K)-\sum_{F\in\mathcal R}\sin\theta_F.
\tag{21.4}
$$

The edge-face incidence count and Euler's formula give the exact identity

$$
4R=2e-B,
\qquad
v-e+R=\chi,
\qquad
\boxed{v=R+\frac B2+\chi.}
\tag{21.5}
$$

**Theorem 21.2 (Oler shell window).**  For every such complex,

$$
\boxed{
G_{\mathcal R}+E_{\mathcal R}
\ge
c_0(B-P)+a_0(t+\chi-1).
}
\tag{21.6}
$$

If $A$ is a global diameter minimizer, then additionally

$$
\boxed{
G_{\mathcal R}+E_{\mathcal R}
<
c_0B+a_0(t+\chi).
}
\tag{21.7}
$$

The difference between the right sides of (21.7) and (21.6) is exactly

$$
\boxed{c_0P+a_0.}
\tag{21.8}
$$

In particular, all component, hole, and outside-vertex corrections cancel from the
remaining capacity window.

**Proof.**  Since the rhombi have disjoint interiors,

$$
\operatorname{area}(K)
=a_0R+E_{\mathcal R}+G_{\mathcal R}.
$$

Insert this expression into (21.2), use $n=v+t$, and then use (21.5):

$$
\begin{aligned}
G_{\mathcal R}+E_{\mathcal R}
&\ge a_0(n-R-1)-c_0P\\
&=c_0(B-P)+a_0(t+\chi-1).
\end{aligned}
$$

This proves (21.6).  For a global minimizer, Theorem 10.9 gives
$D(n)^2<cn$, and hence the isodiametric inequality gives
$\operatorname{area}(K)<a_0n$.  Therefore

$$
G_{\mathcal R}+E_{\mathcal R}
<a_0(n-R)
=c_0B+a_0(t+\chi),
$$

which is (21.7).  Subtraction gives (21.8). $\square$

The theorem incorporates, with exact signs, all of the following quantities requested
in Target B: holes, multiple rhombic components, vertices outside the rhombic core,
and the full convex-hull perimeter.  A bridge forest outside the core is counted in
$t$.  The cancellation in (21.8) also shows why area accounting alone cannot prove
the super-boundary forest-capacity theorem: each outside vertex receives exactly one
bulk allowance $a_0$ on both sides.

For an ideal rhombic disk, $t=0$ and $\chi=1$, so (21.6)-(21.7) reduce to

$$
c_0(B-P)
\le G+\sum_F(\sin\theta_F-a_0)
<c_0B+a_0.
\tag{21.9}
$$

This is the exact perimeter-refined version of the ideal budget (10.29).

### 21.3 Convex defect faces, pockets, and a local surplus decomposition

There is a useful local form of Theorem 21.2 in the jammed branch.

**Lemma 21.3 (convexity of simple contact faces).**  In the zero pinned-cone
branch, every simple bounded contact face is a strictly convex equilateral polygon.

Indeed, at a non-hull vertex the positive spanning relation in Theorem 8.2 makes every
angular gap between consecutive contact rays strictly smaller than $\pi$.  At a hull
vertex, every bounded face angle is contained in the strictly smaller-than-$\pi$
interior angle of the convex hull.  Thus every face angle is smaller than $\pi$.

Two immediate specializations of (21.1) are:

1. If $F$ is a convex equilateral $m$-gon whose vertices are unit-separated, then

   $$
   \boxed{
   \operatorname{area}(F)\ge c_0(m-2).
   }
   \tag{21.10}
   $$

2. If $C$ is a convex pocket bounded by a chain of $r$ unit edges and its
   closing hull chord of length $L$, then

   $$
   \boxed{
   \operatorname{area}(C)\ge c_0(r-L).
   }
   \tag{21.11}
   $$

For (21.10), use $N=m$ and perimeter $m$ in (21.1).  For (21.11), use
$N=r+1$ and perimeter $r+L$.  The vertices of a pocket are a subset of
$A$, so the separation hypothesis is automatic.

Suppose now that the full contact graph is connected, has a simple outer boundary,
and its bounded faces form a topological disk.  Its non-hull outer-boundary vertices
are reflex for the bounded region, because their outer-face angular gaps are smaller
than $\pi$.  Hence the indentation between consecutive hull vertices, together with
the hull chord, is a convex pocket to which (21.11) applies.

If the bounded contact faces have lengths $m_F$, the outer boundary has $k$
unit edges, and there are $f$ bounded faces, Euler and incidence counting give

$$
\sum_F(m_F-2)=2n-k-2.
\tag{21.12}
$$

Writing

$$
s_F=\operatorname{area}(F)-c_0(m_F-2)\ge0,
\qquad
s_C=\operatorname{area}(C)-c_0(r_C-L_C)\ge0,
$$

and noting that $\sum_C(r_C-L_C)=k-P$, one obtains the exact local identity

$$
\boxed{
\operatorname{area}(K)+c_0P-a_0(n-1)
=\sum_Fs_F+\sum_Cs_C.
}
\tag{21.13}
$$

For a rhombus, its summand is exactly
$s_F=\sin\theta_F-a_0$.  Thus the global Oler surplus is literally the sum
of the strict-rhombus, exceptional-face, and indentation-pocket slacks.  This is the
local-cell decomposition that is lost when the finite packing inequality is used only
in its already-summed form.

A nonquadrilateral contact face has $m\ge5$, so (21.10) gives the sharp uniform
track-end charge

$$
\operatorname{area}(F)
\ge \frac{3c_0}{5}m
\ge \frac{3c_0}{5}\,r_F,
\qquad
\boxed{\frac{3c_0}{5}=\frac{3\sqrt3}{20}
=0.2598076211\ldots,}
\tag{21.14}
$$

where $r_F$ is the number of rhombic boundary edges incident with $F$.
The constant is forced by pentagons and cannot be improved using only (21.10).

Let $B$ now denote the boundary-edge count of all rhombic faces in this regular
contact disk, and let

$$
G=\operatorname{area}(K)-\sum_{F\in\mathcal R}\operatorname{area}(F).
$$

Partition the rhombic boundary edges into those incident with bounded
nonquadrilateral faces and those incident with the outer face.  Apply (21.14) to the
first class and (21.11) to the outer pockets.  A two-case comparison according as the
number of outer rhombic edges is at least $P$ gives

$$
\boxed{
G\ge\frac{3\sqrt3}{20}(B-P).
}
\tag{21.15}
$$

If every bounded face is a rhombus, the sharper coefficient $c_0$ holds:

$$
\boxed{G\ge c_0(B-P).}
\tag{21.16}
$$

Finally, in the jammed almost-rhombic regime,

$$
B\ge4\sqrt R=4\sqrt n-O(1),
\qquad
P\le\pi D<C_0\sqrt n.
$$

Therefore

$$
\boxed{
B-P\ge(4-C_0)\sqrt n-O(1)
=0.7010916676\ldots\sqrt n-O(1).
}
\tag{21.17}
$$

Under the regular contact-disk hypotheses, (21.15) yields the unconditional shell
area charge

$$
\boxed{
G\ge0.1821489584\ldots\sqrt n-O(1).
}
\tag{21.18}
$$

In the pure rhombic-disk case, (21.16) improves this to

$$
\boxed{
G\ge0.3035815973\ldots\sqrt n-O(1).
}
\tag{21.19}
$$

These are genuine boundary-order lower bounds.  The five-sector examples escape for
the correct global reason: their boundary perimeter is too large to satisfy
$P<C_0\sqrt n$.  The 11-point sun is below the asymptotic range and remains a
valid finite local regression example.

### 21.4 Constant audit and exact remaining lemma

The new estimates do not close Target B.  Define the Oler surplus

$$
\mathscr O(A)
=\operatorname{area}(K)+c_0P-a_0(n-1).
\tag{21.20}
$$

Equation (21.13) decomposes it into nonnegative local face and pocket slacks.  For a
global minimizer,

$$
\mathscr O(A)
<c_0\pi D+a_0
<c_0C_0\sqrt n+a_0,
$$

where

$$
\boxed{
c_0C_0
=\frac{\sqrt3}{4}\sqrt{2\pi\sqrt3}
=1.4284692103\ldots.
}
\tag{21.21}
$$

Thus an affirmative closure by this route requires the genuinely new large-scale
stability estimate

$$
\boxed{
\mathscr O(A)\ge c_0\pi D+a_0
}
\tag{21.22}
$$

for every sufficiently large triangle-free minimizer in the normalized rhombic/forest
regime, with the forest contribution included.  Equation (21.22) would imply

$$
\operatorname{area}(K)\ge a_0n+c_0(\pi D-P)\ge a_0n,
$$

contradicting $D^2<cn$.

The bad train-track count by itself cannot prove (21.22).  The local constants
$3\sqrt3/20$, (21.18), and (21.19) are all below the required coefficient
(21.21), and the face and pocket inequalities can be approached arbitrarily closely
by near-triangular geometry.  What remains is a quantitative *simultaneous stability*
theorem: near equality in the local Oler cells must be incompatible, at large scale,
with both the diametral-hull condition and near equality in the isodiametric bound.

This addendum therefore narrows Target B and supplies its exact topology-corrected
bookkeeping, but it closes neither Target A nor Target B.  The most promising next
step is to prove a joint Oler/isodiametric stability inequality in which shallow
pockets with near-unit hidden diagonals are charged either to a definite support-width
loss or to a feasible diameter-decreasing boundary motion.  Target A must enter that
same inequality, since (21.8) proves that plain area accounting assigns a forest vertex
exactly the same bulk allowance as a core vertex.

---

## 22. Exact track-end depth and defect-extended span

This section incorporates the second continuation run. It does not solve Level I, but it removes one previously unquantified class of train-track terminations from Target B and complements the Oler-surplus bookkeeping of Section 21. Its first lemma strengthens Lemma 21.3 by proving that every bounded contact face has a single simple boundary cycle, rather than assuming simplicity.

Continue in the triangle-free first-order-jammed branch and let
$\mathcal R=\mathcal F_4$ be the full strict-rhombus face complex.  A boundary
edge of $\mathcal R$ is called **face-terminated** if the contact face on its
non-rhombic side is bounded.  Let $b_F$ be the number of face-terminated
rhombic boundary edges.

If a rhombic boundary edge $e$ instead borders the unbounded contact face,
orient its unit normal $\nu_e$ away from its incident rhombus and put

$$
 \rho_e=
 \max_{x\in A}\nu_e\cdot(x-m_e),
$$

where $m_e$ is the midpoint of $e$.  Thus $\rho_e=0$ for a hull edge,
whereas $\rho_e>0$ for a non-hull edge on the unbounded contact face.  Put

$$
 H_\infty=\sum_{e\text{ bordering the unbounded face}}\rho_e.
$$

### Lemma 22.1: bounded contact faces are strictly convex

Every bounded face of the contact graph has one simple boundary cycle and is a
strictly convex unit-sided polygon.

#### Proof

The straight unit-contact graph is plane.  At a vertex $v\notin Q$, Theorem
8.2 says that the contact directions positively span the plane.  Equivalently,
every angular gap between consecutive contact rays is strictly smaller than
$\pi$.  Every face angle at $v$ is one of these gaps and is therefore less
than $\pi$.

At a vertex $v\in Q=V(\operatorname{conv}A)$, the tangent cone of the convex
hull has angle strictly smaller than $\pi$, because $v$ is an extreme
polygon vertex.  A bounded face lies locally inside the convex hull, so its
face angle at $v$ is again smaller than $\pi$.

A bounded plane-graph face with an inner boundary component, a bridge slit, or
a repeated boundary vertex necessarily has a reflex corner on one of its
boundary walks.  The preceding paragraph excludes this.  Hence the boundary
is one simple cycle, and all its interior angles are smaller than $\pi$.
The face is therefore strictly convex.  Every one of its boundary edges is a
unit contact. $\square$

### Lemma 22.2: sharp width of a convex contact face

Let $P$ be a convex unit-sided polygon whose distinct vertices are mutually
at distance at least $1$.  Then

$$
 \boxed{\operatorname{width}(P)\ge\frac{\sqrt3}{2}.}
 \tag{22.1}
$$

In particular, measured normally from any side of $P$, the opposite support
line is at distance at least $\sqrt3/2$.

#### Proof

A minimum-width direction of a convex polygon is normal to one of its sides.
Put that unit side at

$$
 A=(0,0),\qquad B=(1,0),
$$

and suppose that the polygon lies in the strip $0\le y\le w$.  If
$w<\sqrt3/2$, set

$$
 a=\sqrt{1-w^2}>\frac12.
$$

For any two vertices, their vertical separation is at most $w$, while their
Euclidean separation is at least $1$.  Their horizontal coordinates are
therefore separated by at least $a$.  No third vertex can have horizontal
coordinate strictly between those of $A$ and $B$, since it would be within
horizontal distance at most $1/2<a$ of one of them.  Thus $A,B$ are
consecutive in the ordering of all vertex coordinates by $x$.

If the polygon has $m$ vertices and horizontal span $L$, the one gap from
$A$ to $B$ has length $1$, and the other $m-2$ gaps have length at
least $a$.  Hence

$$
 L\ge1+(m-2)a.
$$

The two boundary arcs between a leftmost and a rightmost vertex each have
length at least $L$.  Since the perimeter is $m$,

$$
 m\ge2L\ge2+2(m-2)a.
$$

As $m\ge3$, this implies $a\le1/2$, a contradiction.  This proves
(22.1).  The constant is sharp, already for the unit equilateral triangle and
as a limiting constant for admissible equilateral polygons. $\square$

### Theorem 22.3: exact defect-extended train-span inequality

For each train track $\tau$, let

$$
 L_\tau=\sum_{F\in\tau}\sin\theta_F.
$$

If $s_F(\tau)\in\{0,1,2\}$ is the number of its end edges that are
face-terminated, then

$$
 \boxed{
 L_\tau+\frac{\sqrt3}{2}s_F(\tau)
 +\sum_{e\in\partial\tau,\ e\text{ on the unbounded face}}\rho_e
 \le D.
 }
 \tag{22.2}
$$

Consequently, since there are $T=B_{\mathcal R}/2$ tracks and every rhombus
belongs to two tracks,

$$
 \boxed{
 \frac{B_{\mathcal R}}2D
 \ge
 2\sum_{F\in\mathcal R}\sin\theta_F
 +\frac{\sqrt3}{2}b_F+H_\infty,
 }
 \tag{22.3}
$$

or equivalently

$$
 \boxed{
 B_{\mathcal R}D
 \ge
 4\sum_{F\in\mathcal R}\sin\theta_F
 +\sqrt3\,b_F+2H_\infty.
 }
 \tag{22.4}
$$

This strictly refines (10.18).

#### Proof

Orient the transverse coordinate of a train as in Theorem 10.6.  Crossing a
rhombus increases that coordinate by exactly $\sin\theta_F$, so the two end
edge midpoints differ in transverse coordinate by $L_\tau$.

At a face-terminated end, Lemmas 22.1 and 22.2 provide a vertex of the bounded
contact face at transverse distance at least $\sqrt3/2$ beyond the end-edge
line.  At an end bordering the unbounded contact face, the definition of
$\rho_e$ provides a vertex of $A$ at transverse distance $\rho_e$ beyond
that line.  Choosing such a vertex at each end gives two points of $A$ whose
transverse separation is at least the left side of (22.2).  Their Euclidean
distance is at most $D$, proving (22.2).

Sum over all tracks.  Each rhombus is counted on its two tracks, every
face-terminated edge is one track end, and every unbounded-face end contributes
its $\rho_e$ once.  This gives (22.3) and (22.4). $\square$

### Exact consequence and limitation

Every bad track end now has an explicit disposition:

1. a bounded-face end costs at least $\sqrt3/2$ of additional transverse
   span;
2. a non-hull end on the unbounded contact face costs its exact positive depth
   $\rho_e$;
3. a hull end has zero additional depth.

Thus bounded nonquadrilateral faces and bounded holes are no longer merely
combinatorial defect objects: they carry the sharp metric charge
$\sqrt3/2$ per incident train end.  The five-sector complexes and the
11-point sun evade this conclusion in precisely the correct way: their hard
train ends lie on the nonconvex unbounded boundary, rather than in bounded
defect faces.

The new term is boundary order and does not by itself finish Target B.  With
$B_{\mathcal R}\ge4\sqrt{F_4}$, the old product bound has order-$n$ slack,
whereas the new contribution in (22.4) is only order $\sqrt n$.  A closing
argument must therefore combine $H_\infty$ and the bounded-face term with
actual convex-hull perimeter or parallel-body area; substituting only
$\operatorname{span}(\tau)\le D$ still loses too much.

The exact remaining metric lemma after this continuation is an aggregate
outer-shell inequality that charges the compulsory non-hull unbounded-face
edges through their depths $\rho_e$, their convexification area, and the
actual perimeter of $\operatorname{conv}A$, with a coefficient strong enough
to beat the finite packing boundary slack.  Target A, the super-boundary
bridge-forest alternative, is unchanged.

---

## 23. Combined continuation frontier

Sections 21 and 22 attack the same boundary-scale obstruction from complementary sides. This section records the exact synthesis that should be treated as the current research frontier. It is a reduction and bookkeeping statement, not a Level I solution.

### 23.1 The bad train ends now have only two nontrivial dispositions

Continue in the triangle-free first-order-jammed branch and take the full strict-rhombus complex $\mathcal R=\mathcal F_4$. Let $b_F$ be the number of rhombic boundary edges whose non-rhombic side is a bounded contact face, and let $b_\infty$ be the number of non-hull rhombic boundary edges on the unbounded contact face. Then

$$
 b_F+b_\infty=b_{\mathcal R}\ge2\sqrt{F_4}-2=2\sqrt n-O(1).
\tag{23.1}
$$

A bounded-face end has a universal metric charge $\sqrt3/2$ in the transverse train-span inequality. An unbounded non-hull end has an exact positive depth $\rho_e$, and their aggregate is

$$
H_\infty=\sum_{e\text{ on the unbounded face}}\rho_e.
\tag{23.2}
$$

Thus the defect network can no longer hide a train end in an unquantified bounded face. The only soft escape is through many shallow non-hull ends on the unbounded face.

### 23.2 Directional train-width refinement

The proof of Theorem 22.3 yields a strictly stronger per-track inequality than the displayed diameter bound. Let $\nu_\tau$ be the oriented transverse unit normal of a train track and let

$$
w_K(\nu)=\max_{x\in K}\nu\cdot x-\min_{x\in K}\nu\cdot x
$$

be the width of $K=\operatorname{conv}A$ in direction $\nu$. The two witness points used in the proof of Theorem 22.2 belong to $A\subset K$, so their transverse separation is at most $w_K(\nu_\tau)$. Hence

$$
\boxed{
L_\tau+\frac{\sqrt3}{2}s_F(\tau)
+\sum_{e\in\partial\tau,\ e\text{ on the unbounded face}}\rho_e
\le w_K(\nu_\tau)\le D.
}
\tag{23.3}
$$

Summing over tracks gives the exact directional form

$$
\boxed{
\sum_\tau w_K(\nu_\tau)
\ge
2\sum_{F\in\mathcal R}\sin\theta_F
+\frac{\sqrt3}{2}b_F+H_\infty.
}
\tag{23.4}
$$

This is the most direct bridge between the two continuation runs. Cauchy's formula

$$
P=\int_0^\pi w_K(\phi)\,d\phi
\tag{23.5}
$$

controls the integral of the same width function, while the train geometry supplies a highly structured discrete multiset of directions. A closing argument may therefore be formulated as a sharp discrete-to-continuous width inequality rather than as another estimate involving only $D$.

### 23.3 Exact simultaneous inequalities for a surviving jammed counterexample

Such a counterexample must satisfy the Oler shell window

$$
G_{\mathcal R}+E_{\mathcal R}
\ge c_0(B-P)+a_0(t+\chi-1),
\tag{23.6}
$$

$$
G_{\mathcal R}+E_{\mathcal R}
<c_0B+a_0(t+\chi),
\tag{23.7}
$$

whose remaining allowance is exactly $c_0P+a_0$, together with the refined train inequality

$$
BD
\ge
4\sum_{F\in\mathcal R}\sin\theta_F
+\sqrt3\,b_F+2H_\infty.
\tag{23.8}
$$

For regular contact disks, the Oler surplus

$$
\mathscr O(A)=\operatorname{area}(K)+c_0P-a_0(n-1)
\tag{23.9}
$$

has the exact local decomposition

$$
\mathscr O(A)=\sum_F s_F+\sum_C s_C,
\tag{23.10}
$$

where the summands are nonnegative face and indentation-pocket slacks. For global minimizers,

$$
\mathscr O(A)<c_0\pi D+a_0,
\tag{23.11}
$$

and proving the reverse inequality for every sufficiently large triangle-free survivor would close the jammed branch.

### 23.4 The precise missing Target B theorem

The current Target B is no longer merely a generic ``sharp boundary-capacity theorem.'' A sufficient focused statement is:

> **Joint outer-shell stability theorem.** For every sufficiently large triangle-free global minimizer in the normalized jammed/almost-rhombic regime, the compulsory train-end data satisfy a quantitative inequality coupling $b_F$, $H_\infty$, the indentation-pocket slacks, the convexification area, and the actual hull perimeter strongly enough to force
> 

$$

> \mathscr O(A)\ge c_0\pi D+a_0.
> 
$$



Equivalently, near equality in the local Oler cells must be incompatible at large scale with both the diametral-hull condition $Q=V(\operatorname{conv}A)$ and near equality in the isodiametric/perimeter bounds.

A particularly promising route is to replace the final use of $\operatorname{span}(\tau)\le D$ by the actual hull width in the train's transverse direction and then aggregate those directional widths through the support function or Cauchy perimeter formula. The unbounded-face depth $\rho_e$ is already a support-function deficit:

$$
\rho_e=h_K(\nu_e)-\nu_e\cdot m_e
$$

for a non-hull outer train end. The missing step is therefore to convert the sum of these support deficits, together with the bounded-face charges, into the Oler/pocket surplus with a sharp enough coefficient.

### 23.5 Target A is now cleanly separated from plain area bookkeeping

The bridge-forest alternative remains:

$$
\ell=\dim\mathcal L_{\widehat Q}=\omega(\sqrt n).
\tag{23.12}
$$

Section 21 shows why simply adding forest vertices to the Oler area count cannot eliminate this branch: the topology/outside-vertex terms cancel from the global shell window. A successful Target A argument must therefore exploit information not visible to plain area alone, for example the configuration-space dimension of the forest, free volume, saturation by new constraints, or a coupling between forest occupancy and the same outer-shell support resources charged in Target B.

The most attractive unified endpoint would prove that every forest degree of freedom or every forest vertex consumes a definite amount of the same support-function/pocket budget appearing in the joint outer-shell stability theorem. Such a theorem would simultaneously force $\ell=O(\sqrt n)$ and close Target B on the resulting $n-O(\sqrt n)$ jammed core.

### 23.6 Current exact status

No Level I proof or disproof is established. The two remaining tasks are now:

1. **Target A:** rule out super-boundary-dimensional bridge-forest lineality, preferably by charging forest freedom to finite shell capacity;
2. **Target B:** prove the joint Oler/isodiametric/track-depth stability theorem above, with constants strong enough to exceed the global-minimizer allowance.

Sections 21--23 supersede the less quantitative formulation of the Target B endpoint in Sections 18--19. The older statements remain valid, but the present formulation is the sharper continuation state.

---
