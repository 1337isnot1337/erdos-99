> Generated reading edition · [exact source](../../../../docs/targets/target-a/11-activation-coloops-and-locked-boundary.md) · source SHA-256 `eb6899fe13346d481493548bb9a5f59c129472c7067428fed275b7c2d4d2b00e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — activation coloops and locked-boundary stress

This audited addendum continues Sections 154–157. It extracts two exact consequences
that are not present in the earlier activation/KKT audit: all activation constraints
are relative coloops and can be opened simultaneously, while a universally locked
first-transition triangle carries a nonnegative contact/facet stress to at least two
distinct points of the fixed hull boundary. Neither statement identifies the source
with the plateau scaffold, so the Level I endpoint remains open.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 158. Activation edges are relative coloops and are simultaneously releasable

Use the monotone activation sequence of Theorem 142.1, written as

```math
A_0,A_1,\ldots,A_\ell,
```

where step $`i`$ moves the strict point $`r_i`$ and creates exactly one active pair

```math
e_i=r_iq_i.
```

Let $`E_0`$ be the active unit and diameter pairs of $`A_0`$, let
$`E_{\rm new}=\{e_1,\ldots,e_\ell\}`$, and let $`V_0`$ be the vertices incident
with $`E_0`$. For a terminal pair $`xy`$, write its position-coordinate rigidity
functional as

```math
\mathsf r_{xy}(v)=(p_x-p_y)\mathbin{\cdot}(v_x-v_y).
```

> **Theorem 158.1 (relative-coloop and simultaneous-release theorem).** Assume
> $`D>1`$. Then:
>
> 1. $`E_{\rm new}`$ is a forest, every one of its components meets $`V_0`$ in at
>    most one vertex, and
>    

```math
>    \boxed{\operatorname{rank}\{\mathsf r_e:e\in E_0\cup E_{\rm new}\}
>    =\operatorname{rank}\{\mathsf r_e:e\in E_0\}+\ell.}
>    \tag{158.1}
>    
```
> 2. The edge-derivative map on the activation forest is onto: after fixing all
>    velocities on $`V_0`$, and one arbitrary root in each activation component
>    disjoint from $`V_0`$, the values
>    

```math
>    \mathsf r_e(v)_{e\in E_{\rm new}}
>    
```
>    can be prescribed arbitrarily.
> 3. There is a velocity $`v`$ and $`t_0>0`$ such that, for every
>    $`0<t<t_0`$, $`A^*+tv`$, where $`A^*=A_\ell`$, is a triangle-free global
>    minimizer of diameter $`D`$, has exactly the old active pairs $`E_0`$, and
>    every vertex outside $`V_0`$ is a strict rattler.

### Proof

Immediately before step $`i`$, $`r_i`$ is strict and is therefore isolated in the
current active graph. The new edge $`e_i`$ attaches that isolated vertex to one
other vertex. Persistence of active pairs makes $`r_i`$ permanently non-strict, so
the creators are distinct. If $`q_i`$ is itself a creator, it was created earlier:
if it were still strict at step $`i`$, the new edge would make it non-strict and it
could not be moved later. Consequently each created edge attaches a new vertex to an
earlier vertex or to a vertex never subsequently moved. Induction gives the forest
and the one-root-per-component assertions.

At the terminal configuration, no creator is incident with an old active pair: every
old active pair persists and would have prevented that creator from being strict when
it moved. Hence the old rigidity rows have zero coordinate blocks at every leaf of
the activation forest outside $`V_0`$. In any linear relation among old and new rows,
inspect such a leaf. Its unique incident activation row has a nonzero block there,
so its coefficient is zero. Remove that edge and iterate. Every activation
coefficient vanishes, proving (158.1). This is the relative-coloop statement; it
also proves the forest row independence without assuming generic coordinates.

For the derivative assertion, orient each activation tree away from its unique
vertex in $`V_0`$, when it has one, and otherwise choose and fix an arbitrary root.
Set the root velocity to zero. Given arbitrary scalars $`\lambda_e`$, recursively set
for an oriented edge $`u\to w`$

```math
v_w-v_u=\lambda_e\frac{p_w-p_u}{|p_w-p_u|^2}.
\tag{158.2}
```

Extend by zero on labels outside the forest and $`V_0`$. Then
```math
\mathsf r_e(v)=\lambda_e
```
for every created edge, while every old active derivative is zero because its
endpoints lie in $`V_0`$. This proves surjectivity.

Choose $`\lambda_e=1`$ for a created unit pair and $`\lambda_e=-1`$ for a created
diameter pair. For a sufficiently small positive $`t`$, every created unit edge has

```math
|p_x+tv_x-p_y-tv_y|^2
=1+2t+t^2|v_x-v_y|^2>1,
\tag{158.3}
```

and every created diameter edge has squared length strictly below $`D^2`$. Every
pair inactive at $`A^*`$ has a strict margin from both $`1`$ and $`D`$, so all such
inequalities persist after shrinking $`t_0`$. The old active pairs are fixed. An old
diameter pair exists and is fixed, hence the perturbed configuration still has
diameter exactly $`D=D(|A^*|)`$, and is therefore globally optimal. Its unit-contact
graph is the old contact graph with activation edges deleted, so it is triangle-free.
Every active pair incident with a vertex outside $`V_0`$ was created, and is now
strictly opened or shortened; those vertices are consequently strict rattlers.
This proves item 3. $`\square`$

The theorem strengthens Section 153 in a different direction. Section 153 says that
created pairs have zero coefficient in every nonnegative normalized KKT stress. Here
they have zero coefficient in every signed relation among the active-pair rigidity
rows, and the critical
cone contains one finite direction that is strict on all created inequalities at once.
Thus activation rank alone cannot force a universal first-order blockage or a
positive stress load.

## 158.1 Exact relation to the fixed-hull flat

The simultaneous-release direction need not stay inside the terminal hull. The
fixed-hull family of Section 156 is complementary: it freezes terminal boundary
creators and imposes zero first derivative only on created unit edges, giving a
super-boundary-dimensional same-hull family when the interior creator count is large.
The two constructions therefore imply the following precise no-go:

```math
\boxed{
\text{created activation rows provide neither a universal KKT load nor a universal
critical-cone lock.}}
\tag{158.4}
```

They do not imply that the rows are irrelevant to all higher-order or global
arguments; a source-to-scaffold transport theorem could still use the finite paths
or the fixed-hull family.

---

# 159. A universally locked triangle transmits stress to the hull boundary

We now sharpen the locked branch of Theorem 138.1. Let $`H`$ be a full-dimensional
convex polygon with outward facet normals $`n_f`$, so

```math
n_f\mathbin{\cdot}z\le c_f.
```

Let $`P\subset H`$ be a finite unit-separated set. For a velocity field $`v`$, put

```math
a_{ij}(v)=(p_i-p_j)\mathbin{\cdot}(v_i-v_j),
\qquad
b_{if}(v)=-n_f\mathbin{\cdot}v_i
```

for an active unit edge $`ij`$ and a point $`p_i`$ on facet $`f`$. Let

```math
\mathcal C_H(P)=\{v:a_{ij}(v)\ge0, b_{if}(v)\ge0\}
```

be the fixed-container expansive cone. Suppose a unit equilateral triangle $`T`$ in
$`P`$ is universally locked:

```math
a_e(v)=0\qquad(e\in E(T),\ v\in\mathcal C_H(P)).
```

> **Theorem 159.1 (boundary-transmitting locked-triangle certificate).** There are
> coefficients $`\alpha_{ij}\ge0`$ on the unit-contact edges and
> $`\mu_{if}\ge0`$ on active facet incidences such that
> 

```math
> \alpha_e>0\quad(e\in E(T)),
> 
```
> and, at every vertex $`p_i`$,
> 

```math
> \boxed{
> \sum_{j:ij\in E_1(P)}\alpha_{ij}(p_i-p_j)
> -\sum_{f:n_f\cdot p_i=c_f}\mu_{if}n_f=0.}
> \tag{159.1}
> 
```
> If $`K`$ is the connected component of the positive-contact graph containing $`T`$,
> then at least two distinct points of $`P\cap\partial H`$ in $`K`$ carry nonzero
> facet reaction. In particular, $`K`$ contains contact paths from $`T`$ to two
> distinct hull-boundary points.

### Proof

The cone is given by finitely many linear inequalities. By the finite-dimensional
Farkas/polar-cone theorem, a functional nonnegative on this cone is a nonnegative
linear combination of the defining functionals. Since $`a_e`$ vanishes on the cone,
both $`a_e`$ and $`-a_e`$ are nonnegative there. Hence, for every $`e\in E(T)`$,

```math
-a_e=\sum_g\lambda_g^{(e)}a_g+\sum_{i,f}\nu_{if}^{(e)}b_{if},
\qquad
\lambda_g^{(e)},\nu_{if}^{(e)}\ge0.
\tag{159.2}
```

Add (159.2) over the three triangle edges and move the left side to the right. The
result is the zero functional

```math
0=\sum_g\alpha_g a_g+\sum_{i,f}\mu_{if}b_{if},
\tag{159.3}
```

with $`\alpha_e\ge1`$ on all three edges of $`T`$. Reading the coefficient of each
velocity block gives (159.1).

Let $`K`$ be the positive-contact component containing $`T`$. Summing (159.1) over
vertices of $`K`$ cancels all internal contact forces and leaves

```math
\sum_{i\in K,f}\mu_{if}n_f=0.
\tag{159.4}
```

There must be a nonzero reaction in $`K`$. Otherwise the positive contact forces on
$`K`$ would form a nonzero self-equilibrium. Choose a direction having a unique
maximizer among the finite set of points in $`K`$; dotting equilibrium at that
maximizer with the direction gives a strictly positive number, a contradiction.

Those reactions cannot all be supported at one boundary point. At a point of a
full-dimensional convex polygon, its active outward normals form a pointed normal
cone: a single facet gives one ray, and a vertex gives the cone spanned by two
normals with angle strictly less than $`\pi`$. A nonzero nonnegative combination of
vectors in a pointed cone cannot vanish, contradicting (159.4). Thus at least two
distinct boundary points in $`K`$ carry reaction, and connectivity of $`K`$ gives
the asserted contact paths. $`\square`$

The certificate is a fixed-container global dual statement, not the held-cage local
regression of Section 139. It also does not imply a Schur separator: its boundary
points belong to $`P\cap\partial H`$, whereas the response terminals are the
independently constructed scaffold boundary set $`C^\partial`$.

## 159.1 Target A implication and exact remaining bridge

The activation-coloop theorem removes the possibility that a large activation rank
alone locks the critical cone, and Theorem 159.1 replaces a local locked-cage picture
by a boundary-transmitting stress support. The exact endpoint is nevertheless still

```math
\boxed{\dim\ker S\ge s=\Delta_\Lambda-d_{\rm int}.}
```

The remaining lemma can now be stated as a source-to-response transport statement:

> **Locked-support transport lemma.** For the first bad capacity transition rebuilt
> from the terminal activated source, map the two boundary reaction paths supplied by
> Theorem 159.1 (or the finite activation-flat directions of Theorem 156.2) into the
> directed alternating source-to-exterior network. Either one such certificate gives
> an independent saved source terminal, and $`s`$ independent certificates give
> $`\dim\ker S\ge s`$, or the corresponding source replacement has diameter strictly
> below $`D`$.

No map with this rank or strict-diameter conclusion has been proved. The exact source
backbone witness of Section 157, the fixed-hull affine family of Section 156, and the
two-shadow alignment of Sections 154–155 remain compatible with this gap.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**
