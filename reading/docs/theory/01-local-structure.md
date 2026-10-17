> Generated reading edition · [exact source](../../../docs/theory/01-local-structure.md) · source SHA-256 `75c539b2281046c49d6c303bda845cb7fb2643d0d9a1106d64e4f737117c54fb`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Theory notes: local structure

> Canonical v1.7.0 module. The original section numbering is preserved for
> cross-references; see the [documentation map](../README.md).

## 4. Exact first-order KKT stress for every minimizer

Let

```math
A=\{p_1,\ldots,p_n\}
```

be any minimizer, and put

```math
T=D(n)^2.
```

Define the active contact and diameter sets

```math
C=\{ij:|p_i-p_j|=1\},\qquad
H=\{ij:|p_i-p_j|^2=T\}.
```

### Theorem 4.1: normalized signed equilibrium stress

There exist multipliers

```math
\alpha_{ij}\ge0\quad(ij\in C),\qquad
\beta_{ij}\ge0\quad(ij\in H)
```

such that

```math
\sum_{ij\in H}\beta_{ij}=1,
\tag{4.1}
```

```math
\sum_{j:ij\in C}\alpha_{ij}(p_i-p_j)
=
\sum_{j:ij\in H}\beta_{ij}(p_i-p_j)
\qquad(i=1,\ldots,n),
\tag{4.2}
```

```math
\sum_{ij\in C}\alpha_{ij}=T,
\tag{4.3}
```

and

```math
\sum_{ij\in C}\alpha_{ij}
(p_i-p_j)(p_i-p_j)^{\mathsf T}
=
\sum_{ij\in H}\beta_{ij}
(p_i-p_j)(p_i-p_j)^{\mathsf T}.
\tag{4.4}
```

Equivalently, if

```math
u_{ij}=p_i-p_j\quad(ij\in C),\qquad
w_{ij}=\frac{p_i-p_j}{D}\quad(ij\in H),
```

then

```math
\boxed{
\sum_{ij\in C}\frac{\alpha_{ij}}{D^2}u_{ij}u_{ij}^{\mathsf T}
=
\sum_{ij\in H}\beta_{ij}w_{ij}w_{ij}^{\mathsf T}.
}
\tag{4.5}
```

Both sides of (4.5) are convex combinations of rank-one projections.

#### Proof

Minimize $`T`$ in the variables $`(p_1,\ldots,p_n,T)`$ subject to

```math
g_{ij}=1-|p_i-p_j|^2\le0,
\qquad
h_{ij}=|p_i-p_j|^2-T\le0.
```

MFCQ holds explicitly. At any feasible point take

```math
v_i=p_i,\qquad \tau=3T.
```

For every active contact,

```math
Dg_{ij}(v)=-2|p_i-p_j|^2=-2<0,
```

and for every active diameter constraint,

```math
Dh_{ij}(v,\tau)=2T-3T=-T<0.
```

Thus ordinary KKT applies. The Lagrangian is

```math
L=T+
\sum_{ij}\alpha_{ij}(1-|p_i-p_j|^2)
+\sum_{ij}\beta_{ij}(|p_i-p_j|^2-T).
```

Stationarity in $`T`$ gives (4.1), while stationarity in every $`p_i`$ gives (4.2).

Multiply (4.2) by $`p_i^{\mathsf T}S`$, sum over $`i`$, and let $`S`$ range over all symmetric $`2\times2`$ matrices. The two endpoint contributions of each edge combine, yielding (4.4). Taking $`S=I`$, using the active lengths, and then using (4.1) gives (4.3). Dividing (4.4) by $`D^2`$ gives (4.5). ∎

With the sign convention of [7], the coefficients

```math
\omega_{ij}=-\alpha_{ij}\quad(ij\in C),\qquad
\omega_{ij}=+\beta_{ij}\quad(ij\in H)
```

form a proper mixed cable-strut equilibrium stress.

---

## 5. Consequences for the positive stress support

Let

```math
C_+=\{ij\in C:\alpha_{ij}>0\},\qquad
H_+=\{ij\in H:\beta_{ij}>0\},
```

and let $`B_+`$ be the vertex set of $`H_+`$.

### Lemma 5.1: diameter endpoints are extreme

Every endpoint of a diameter pair is a vertex of $`\operatorname{conv}A`$.

#### Proof

If $`p_i=\sum_k\lambda_kx_k`$ were a nontrivial convex combination and $`|p_i-p_j|=D`$, then

```math
D=|p_i-p_j|
\le\sum_k\lambda_k|x_k-p_j|
\le D.
```

Equality in the Euclidean triangle inequality would force all vectors $`x_k-p_j`$ occurring with positive coefficient to be the same length-$`D`$ vector, contradicting nontriviality. ∎

### Lemma 5.2: positive diameter load requires positive contact load

Every vertex in $`B_+`$ is incident to an edge of $`C_+`$.

#### Proof

Otherwise (4.2) would express the extreme point $`p_i`$ as a convex combination of its diameter partners. ∎

### Lemma 5.3: unloaded stress vertices are contact barycenters

If $`p_i\notin B_+`$ but is incident to positive contact stress, then

```math
p_i=
\frac{\sum_j\alpha_{ij}p_j}{\sum_j\alpha_{ij}}.
\tag{5.1}
```

Consequently, its $`C_+`$-degree cannot be (1). If its $`C_+`$-degree is (2), its two neighbors are exactly opposite unit contacts, the two stresses agree, and the neighbors are distance (2) apart.

### Proposition 5.4: every stressed contact component is boundary loaded twice

Every nontrivial connected component of $`C_+`$ contains at least two vertices incident to $`H_+`$.

#### Proof

If a component had no $`H_+`$-loaded vertex, choose a direction in which one of its vertices is uniquely extreme. The positive contact forces there all have strictly positive projection in that direction, contradicting equilibrium.

If a component had exactly one loaded vertex $`p_i`$, sum equilibrium over the component. Internal contact forces cancel, leaving

```math
\sum_j\beta_{ij}(p_i-p_j)=0.
```

For any two diameter partners $`p_j,p_k`$,

```math
(p_i-p_j)\cdot(p_i-p_k)
=D^2-\frac{|p_j-p_k|^2}{2}
\ge\frac{D^2}{2}>0.
```

A positive combination of these vectors cannot vanish. ∎

### Proposition 5.5: forest-supported stress

Let $`m=|V(C_+)|`$, let $`c_+`$ be the number of components of $`C_+`$, and let $`L`$ be the unloaded $`C_+`$-degree-(2) vertices. If $`C_+`$ is a forest, then

```math
m-|L|\le2|B_+|-2c_+\le2\pi D-2c_+.
\tag{5.2}
```

Indeed, vertices in $`B_+`$ have degree at least (1), vertices in $`L`$ have degree (2), and all other vertices have degree at least (3). The forest degree sum gives the first inequality. Lemma 5.1, unit-separated hull sides, and Cauchy's perimeter-diameter inequality give

```math
|B_+|\le |V(\operatorname{conv}A)|
\le\operatorname{per}(\operatorname{conv}A)
\le\pi D.
```

In particular, if $`V(C_+)=A`$, $`L=\varnothing`$, and $`C_+`$ is a forest, then

```math
n\le2\pi\sqrt{\frac n{\Delta_2}}-2c_+,
```

which is impossible for $`n\ge44`$.

### Proposition 5.6: cyclic stress components

If the full contact graph is triangle-free, every cyclic component of $`C_+`$ has at least four vertices in $`B_+\cup L`$.

This follows by applying Eppstein's Lemma 2 to that component and then using Lemma 5.3 at every low-degree vertex.

### Exact warning example: the unit square

For the unit square, put weight $`\alpha=1/2`$ on each of the four contact sides and weight $`\beta=1/2`$ on each of the two diameter diagonals. Then

```math
\sum\beta=1,
\qquad
\sum\alpha=2=D(4)^2,
```

and equilibrium holds at every vertex. Thus triangle-free (2)-degeneracy, a normalized positive mixed stress, and exact global optimality are mutually compatible. Any argument asserting that a contact-degree-(2) vertex is automatically movable is already false at $`n=4`$: the diameter cables can supply the missing reactions.

These propositions explain the precise limitation of stress plus (2)-degeneracy: stress may travel through exact straight unit chains, and sparse boundary diameter forces may support a large interior network.

---

## 6. A contact-minimal normal form

Assume that, for a fixed $`n`$, at least one triangle-free minimizer exists. Among all triangle-free minimizers choose $`A^*`$ with the minimum number of unit contacts. Let

```math
Q=\{p_i:\exists j,\ |p_i-p_j|=D(n)\}
```

be the full set of diameter endpoints.

### Theorem 6.1: local trapping after contact minimization

For $`A^*`$:

1. Every non-diameter, nonisolated vertex is strictly surrounded by its unit contacts: its contact vectors positively span $`\mathbb R^2`$.
2. Every such vertex has contact degree (3), (4), or (5).
3. Every nonisolated contact vertex of degree (1) or (2) belongs to $`Q`$.

#### Proof

Let $`p_i\notin Q`$ have at least one contact. If its contact vectors do not positively span the plane, finite-dimensional separation gives a nonzero vector $`w`$ satisfying

```math
(p_i-p_j)\cdot w\ge0
```

for every contact $`ij`$. Move only $`p_i`$:

```math
p_i(t)=p_i+tw.
```

For every old contact,

```math
|p_i(t)-p_j|^2
=1+2t(p_i-p_j)\cdot w+t^2|w|^2>1.
\tag{6.1}
```

The quadratic term handles two exactly opposite contacts: a perpendicular motion has zero first derivative but strictly increases both lengths.

All noncontacts involving $`p_i`$ have positive slack above (1), and because $`p_i\notin Q`$, all its distances have positive slack below $`D`$. Hence, for sufficiently small $`t>0`$, feasibility and diameter $`D`$ are preserved while every contact at $`p_i`$ is broken.

If another contact remains elsewhere, this contradicts contact minimality. If no contact remains, the new minimum distance is $`>1`$, and rescaling produces diameter $`<D(n)`$, contradicting global optimality. Thus the contact vectors positively span the plane.

Positive spanning requires at least three directions. Triangle-freeness gives at most five unit neighbors, because equality in a $`60^\circ`$ angular gap would make a unit triangle, while six gaps strictly larger than $`60^\circ`$ cannot fit around $`360^\circ`$. ∎

### Corollary 6.2: boundary count

Every diameter endpoint is a convex-hull vertex, and

```math
|Q|\le\pi D(n)
\le
\sqrt{2\pi\sqrt3}\,\sqrt n.
\tag{6.2}
```

Write

```math
C_0:=\sqrt{2\pi\sqrt3}=3.298908\ldots.
```

Then $`|Q|\le C_0\sqrt n`$.

### Corollary 6.3: tree components

If $`T`$ is a nontrivial tree contact component and

```math
b_T=|Q\cap V(T)|,
```

then

```math
|V(T)|\le2b_T-2.
\tag{6.3}
```

Therefore all nontrivial tree components together contain $`O(\sqrt n)`$ vertices.

### Corollary 6.4: cyclic components

Every cyclic contact component contains at least four vertices of $`Q`$. Thus there are at most $`|Q|/4=O(\sqrt n)`$ cyclic components.

### Corollary 6.5: cyclomatic number

Let $`z`$ be the number of contact-isolated vertices, $`m=n-z`$, $`e`$ the number of contact edges, and $`c_*`$ the number of nontrivial contact components. Then

```math
e\ge\frac32m-|Q|,
```

and the cyclomatic number

```math
\kappa=e-m+c_*
```

satisfies

```math
\boxed{
\kappa\ge\frac{n-z}{2}-C_0\sqrt n+c_*.
}
\tag{6.4}
```

Thus a contact-minimal triangle-free counterexample is either rattler dominated or has a linear number of independent contact cycles anchored to only $`O(\sqrt n)`$ diameter vertices.

---

## 7. The pinned expansive-cone dichotomy

The strongest framework statement can be proved without invoking any external rigidity theorem.

For a triangle-free minimizer $`A`$, let $`Q`$ be all diameter endpoints and define

```math
\mathcal E_Q(A)=
\left\{
v=(v_i):
v_i=0\ (p_i\in Q),\quad
(p_i-p_j)\cdot(v_i-v_j)\ge0\ (ij\in C)
\right\}.
\tag{7.1}
```

### Theorem 7.1: exact dichotomy

Exactly one of the following holds.

#### Flexible branch

If $`\mathcal E_Q(A)\ne\{0\}`$, then $`A`$ belongs to a nonconstant continuous family of noncongruent triangle-free global minimizers of diameter $`D(n)`$, with all points in $`Q`$ fixed.

#### First-order-jammed branch

If $`\mathcal E_Q(A)=\{0\}`$, let $`e^\circ`$ denote the number of contact edges that do not have both endpoints in $`Q`$. Then the reduced contact rigidity matrix has full column rank and

```math
\boxed{e^\circ\ge2(n-q).}
\tag{7.2}
```

In particular, $`e\ge2(n-q)`$, where $`q=|Q|`$.

#### Proof

If $`v\in\mathcal E_Q(A)\setminus\{0\}`$, take the straight motion

```math
p_i(t)=p_i+tv_i.
```

For each contact,

```math
|p_i(t)-p_j(t)|^2
=1+2t(p_i-p_j)\cdot(v_i-v_j)
+t^2|v_i-v_j|^2\ge1.
```

Every active diameter pair has both endpoints fixed. All initially noncontact and nondiameter pairs have strict slack, so sufficiently small $`t`$ preserves feasibility, diameter $`D`$, and triangle-freeness. Because two distinct diameter endpoints are fixed, a nonzero continuous motion cannot be a nontrivial Euclidean congruence.

If the cone is zero, any vector in the kernel of the reduced contact rigidity matrix would belong to the cone together with its negative. Hence the kernel is zero and the matrix has rank $`2(n-q)`$. A contact joining two pinned vertices gives a zero row, so only the $`e^\circ`$ remaining rows can contribute to this rank. This proves (7.2). ∎

### Lemma 7.2: direct local witnesses for the flexible branch

The following statements hold for every minimizer $`A`$.

1. If a convex-hull vertex $`p`$ is not in $`Q`$, then $`\mathcal E_Q(A)\ne\{0\}`$.
2. If a vertex $`p\notin Q`$ has contact degree at most $`2`$, then $`\mathcal E_Q(A)\ne\{0\}`$.

Consequently, in the first-order-jammed triangle-free branch,

```math
\boxed{Q=V(\operatorname{conv}A)}
\tag{7.3}
```

and every vertex outside $`Q`$ has contact degree $`3`$, $`4`$, or $`5`$. In particular, every contact-isolated vertex belongs to $`Q`$.

#### Proof

For the first statement, choose a strict supporting normal $`u`$ at the hull vertex $`p`$, so

```math
u\cdot(p-x)>0\qquad(x\in A\setminus\{p\}).
```

Moving only $`p`$ with velocity $`u`$ strictly expands every incident contact. Because $`p\notin Q`$, all distances from $`p`$ have strict slack below $`D`$, while a diameter pair not using $`p`$ remains fixed. Thus this velocity lies in the pinned expansive cone and produces the same-diameter flex of Theorem 7.1. Lemma 5.1 gives the reverse inclusion $`Q\subseteq V(\operatorname{conv}A)`$, proving (7.3) in the zero-cone branch.

For the second statement, degree $`0`$ is immediate. At degree $`1`$, move $`p`$ perpendicular to its unique contact direction; that contact expands quadratically. At degree $`2`$, let $`a,b`$ be the two unit vectors from the neighbors toward $`p`$. If $`a\ne-b`$, the velocity $`w=a+b`$ satisfies

```math
a\cdot w=b\cdot w=1+a\cdot b>0.
```

If $`a=-b`$, move perpendicular to them and both contacts expand quadratically. Since $`p\notin Q`$, all upper constraints incident to it have slack. Triangle-freeness supplies the upper degree bound $`5`$. ∎

### Corollary 7.3: cycle count and size of the diameter boundary

Let $`c`$ be the number of contact-graph components and

```math
\kappa=e-n+c
```

its cyclomatic number. In the first-order-jammed branch,

```math
\boxed{
\kappa\ge n-2q+c
\ge n-2\sqrt{2\pi\sqrt3}\,\sqrt n+1.
}
\tag{7.4}
```

Thus

```math
\kappa\ge n-6.597816\ldots\sqrt n+1,
```

and in particular $`\kappa=n-O(\sqrt n)`$.

Eppstein's bound (2.4) and (7.2) imply

```math
q\ge\frac14\sqrt{2\pi\sqrt3\,n}-O(1)
=0.824727\ldots\sqrt n-O(1).
\tag{7.5}
```

Together with (6.2),

```math
q=\Theta(\sqrt n),\qquad e=2n-\Theta(\sqrt n).
\tag{7.6}
```

If the contact graph is connected, (2.3) yields

```math
q\ge\frac{d_G+2}{2}
\ge\frac{D(n)+2}{2}
\ge\frac12\left(\sqrt{\frac n{\Delta_2}}+1\right),
\tag{7.7}
```

where the last step uses the sharper planar lower bound (2.2).

---

## 8. Strict pinned stress and interior trapping

Lemma 7.2 already identifies the hull geometrically. Cone duality gives additional exact information: every unpinned vertex is strictly trapped by a positive stress on every incident contact. This replaces the imported reliance on an all-strut theorem that is only quoted, not proved, in [7].

### Lemma 8.1: strict positive dependence from a zero expansive cone

Let $`R`$ be a real matrix. If

```math
\{x:Rx\ge0\}=\{0\},
\tag{8.1}
```

then $`R`$ has full column rank and there exists a vector $`c`$ with every coordinate strictly positive such that

```math
R^{\mathsf T}c=0.
\tag{8.2}
```

#### Proof

The kernel is zero because both $`x`$ and $`-x`$ satisfy $`Rx=0`$. Let $`r_1,\ldots,r_e`$ be the rows. Condition (8.1) says that the dual cone of $`\operatorname{pos}\{r_1,\ldots,r_e\}`$ is $`{0}`$, hence the positive hull of the rows is the full column space.

For every nonzero row $`r_i`$, express $`-r_i`$ as a nonnegative combination of the rows. This produces a nonnegative linear dependence with a positive coefficient on $`r_i`$. Summing these dependences over $`i`$, and assigning arbitrary positive coefficients to any zero rows, gives (8.2) with $`c_i>0`$ for every $`i`$. ∎

### Theorem 8.2: strict positive pinned stress and local trapping

Assume $`\mathcal E_Q(A)=\{0\}`$. Then:

1. Every contact edge admits a strictly positive pinned equilibrium stress.
2. At every unpinned vertex $`p_i\notin Q`$,

   
   ```math
   \sum_{j\sim i}c_{ij}(p_j-p_i)=0,
   \qquad c_{ij}>0.
   \tag{8.3}
   ```


3. The contact neighbors of every unpinned vertex affinely span the plane.
4. Every unpinned vertex lies in the strict interior of the convex hull of its contact neighbors and has contact degree at least (3).
5. The diameter endpoints are exactly the convex-hull vertices:

   
   ```math
   \boxed{Q=V(\operatorname{conv}A).}
   \tag{8.4}
   ```


#### Proof

Apply Lemma 8.1 to the reduced contact rigidity matrix whose columns correspond to unpinned coordinates. Equation (8.2) is exactly (8.3). It first places $`p_i`$ in the affine hull of its contact neighbors. If those neighbors failed to span the plane, they and $`p_i`$ would lie on one line, and moving only $`p_i`$ perpendicular to that line would give a nonzero vector in the kernel of the reduced matrix, contrary to full column rank. Thus the neighbors affinely span the plane, and the positive equilibrium relation makes $`p_i`$ a strict convex combination of them.

No equilibrium equation is asserted at a pinned vertex; the missing force there is the pin reaction. Contacts joining two pinned vertices give zero rows in the reduced matrix and may be assigned arbitrary positive coefficients without affecting the unpinned equations.

An unpinned point therefore cannot be extreme in $`\operatorname{conv}A`$. Hence every hull vertex lies in $`Q`$. Lemma 5.1 gives the reverse inclusion, consistently with the direct proof in Lemma 7.2. ∎

Under the triangle-free hypothesis, every unpinned vertex consequently has degree (3), (4), or (5).

This theorem is stronger than the earlier estimate $`Q\subseteq V(\operatorname{conv}A)`$: in the first-order-jammed branch, **all** hull vertices are diameter endpoints.

---

## 9. The forest exclusion and boundary anchoring

### Proposition 9.1: component anchoring in every jammed counterexample

In the first-order-jammed triangle-free branch:

1. If $`T`$ is a nontrivial tree contact component with $`n_T`$ vertices and $`q_T=|Q\cap V(T)|`$, then

   
   ```math
   \boxed{n_T\le2q_T-2.}
   \tag{9.1}
   ```


2. All nontrivial tree components together contain at most $`2q=O(\sqrt n)`$ vertices.
3. Every cyclic contact component contains at least four diameter endpoints.
4. Every isolated contact vertex is a diameter endpoint.

#### Proof

Every non-$`Q`$ vertex has degree at least $`3`$ by Lemma 7.2, while every vertex of a nontrivial tree has degree at least $`1`$. Therefore

```math
2(n_T-1)
=\sum_{v\in T}\deg v
\ge3(n_T-q_T)+q_T,
```

which gives (9.1). Sum over the tree components. For a cyclic component, Eppstein's Lemma 2 supplies four non-articulation vertices of degree at most $`2`$; Lemma 7.2 puts all four in $`Q`$. Its degree-$`0`$ case also proves the last assertion. ∎

### Corollary 9.2: no forest for $`n\ge44`$

If $`A`$ is a triangle-free minimizer in the first-order-jammed branch and $`n\ge44`$, then its contact graph is not a forest.

#### Proof

Let $`h=|Q|`$, which equals the number of hull vertices by (8.4). Let $`U`$ be the unpinned vertices, $`Q'\subseteq Q`$ the nonisolated pinned vertices, and $`c`$ the number of nontrivial forest components.

Every vertex in $`U`$ has degree at least (3), and every vertex in $`Q'`$ has degree at least (1). Since a forest on $`|U|+|Q'|`$ nonisolated vertices with $`c`$ components has $`|U|+|Q'|-c`$ edges,

```math
2(|U|+|Q'|-c)
\ge3|U|+|Q'|.
```

Thus

```math
|U|\le|Q'|-2c,
```

and therefore

```math
n=|U|+h\le2h.
\tag{9.2}
```

Every hull side has length at least (1), while Cauchy's inequality gives

```math
h\le\operatorname{per}(\operatorname{conv}A)
\le\pi D(n).
```

Using the upper bound in (2.2),

```math
n\le2\pi\sqrt{\frac n{\Delta_2}},
```

so

```math
n\le\frac{4\pi^2}{\Delta_2}=8\pi\sqrt3=43.531\ldots.
```

Hence $`n\ge44`$ is impossible. ∎

### Corollary 9.3: four low-degree diametral hull vertices

For $`n\ge44`$, every triangle-free minimizer in the first-order-jammed branch has a cyclic contact component. Eppstein's Lemma 2 supplies at least four non-articulation vertices of contact degree at most (2) in that component. Lemma 7.2 forces all four to be diameter endpoints on the convex hull.

Thus a hypothetical large jammed counterexample must simultaneously have:

- every hull vertex diametral;
- every interior vertex strictly surrounded by at least three contacts;
- at least four hull vertices of contact degree at most (2); and
- $`\Theta(\sqrt n)`$ hull/diameter vertices in total.

---

## 10. The almost-rhombic structure theorem

Continue in the triangle-free first-order-jammed branch. Let $`e`$ be the number of contact edges, $`c`$ the number of contact-graph components, and $`k`$ the number of edge incidences with the unbounded face.

Euler's formula gives the number of bounded faces:

```math
f_b=e-n+c.
\tag{10.1}
```

Every bounded face has length at least (4). Define its total excess over quadrilateral length by

```math
X=\sum_{F\text{ bounded}}(|\partial F|-4).
```

Counting edge-face incidences gives

```math
X=2e-k-4f_b=4n-2e-k-4c.
\tag{10.2}
```

Using $`e\ge2(n-q)`$,

```math
0\le X\le4q-k-4c\le4q.
\tag{10.3}
```

Let $`F_4`$ be the number of bounded faces of length (4). Since every other bounded face contributes at least (1) to $`X`$,

```math
F_4\ge f_b-X
=3e-5n+k+5c
\ge n-6q+k+5c.
\tag{10.4}
```

In particular,

```math
F_4=n-O(\sqrt n).
\tag{10.5}
```

### Lemma 10.1: geometry of a four-face

Every bounded four-face is a simple unit rhombus. If $`\theta_F\in(0,\pi/2]`$ is its acute angle, then

```math
\boxed{
\frac\pi3<\theta_F\le\frac\pi2.
}
\tag{10.6}
```

Indeed, the short diagonal has length $`2\sin(\theta_F/2)\ge1`$. Equality would add the short diagonal as a unit contact and form unit equilateral triangles. Therefore equality is forbidden in a triangle-free contact graph.

The face area is

```math
\operatorname{area}(F)=\sin\theta_F>\frac{\sqrt3}{2}.
\tag{10.7}
```

### Theorem 10.2: total rhombus defect

Define

```math
\eta_F=\sin\theta_F-\frac{\sqrt3}{2}>0.
```

Then

```math
\boxed{
\sum_{F\in\mathcal F_4}\eta_F
\le
\frac{\sqrt3}{2}(n-F_4)
\le
\frac{\sqrt3}{2}(6q-k-5c).
}
\tag{10.8}
```

#### Proof

The bounded contact faces have disjoint interiors and lie in $`\operatorname{conv}A`$. Therefore

```math
\sum_{F\in\mathcal F_4}\operatorname{area}(F)
\le\operatorname{area}(\operatorname{conv}A).
```

The isodiametric inequality and the BHS upper bound give

```math
\operatorname{area}(\operatorname{conv}A)
\le\frac{\pi D^2}{4}
\le\frac\pi4\frac n{\Delta_2}
=\frac{\sqrt3}{2}n.
```

Substitute (10.7) and then use (10.4). ∎

### Corollary 10.3: almost every rhombus is nearly equilateral

For fixed $`0<\varepsilon\le\pi/6`$, the number $`N_\varepsilon`$ of four-faces satisfying

```math
\theta_F\ge\frac\pi3+\varepsilon
```

obeys

```math
N_\varepsilon
\le
\frac{(\sqrt3/2)(6q-k-5c)}
{\sin(\pi/3+\varepsilon)-\sqrt3/2}
=O_\varepsilon(\sqrt n).
\tag{10.9}
```

Hence all but $`O_\varepsilon(\sqrt n)`$ bounded faces have acute angle in

```math
60^\circ<\theta_F<60^\circ+\varepsilon.
```

### Corollary 10.4: total angular excess is boundary order

Put

```math
\delta_F=\theta_F-\frac\pi3\in(0,\pi/6].
```

The concave function

```math
f(\delta)=\sin\left(\frac\pi3+\delta\right)-\frac{\sqrt3}{2}
```

lies above the chord joining its endpoint values on $`[0,\pi/6]`$. Hence

```math
f(\delta)
\ge
\frac6\pi\left(1-\frac{\sqrt3}{2}\right)\delta.
```

Together with (10.8), this gives the explicit estimate

```math
\boxed{
\sum_{F\in\mathcal F_4}
\left(\theta_F-\frac\pi3\right)
\le
\frac{\pi\sqrt3}{12(1-\sqrt3/2)}(6q-k-5c)
=O(\sqrt n).
}
\tag{10.10}
```

Since $`F_4=n-O(\sqrt n)`$, the mean angular excess is $`O(n^{-1/2})`$.

### Corollary 10.5: almost every vertex has degree four

Only $`O(q)`$ vertices are isolated, lie on the unbounded contact face, or are incident to a nonquadrilateral bounded face. Every other vertex is surrounded by rhombi whose angles lie strictly between $`60^\circ`$ and $`120^\circ`$, so its degree is (4) or (5).

Moreover,

```math
0\le\sum_v(4-\deg v)=4n-2e\le4q.
```

The left inequality follows, for example, from Eppstein's (2)-degeneracy bound $`e\le2n-3`$ on every nonempty graph with at least two vertices. Let $`E_0`$ be the exceptional vertex set and let $`N_5`$ count the nonexceptional degree-(5) vertices. The nonexceptional vertices have degree (4) or (5), while triangle-freeness gives degree at most (5) everywhere. Hence

```math
0\le \sum_{v\in E_0}(4-\deg v)-N_5
\le 4|E_0|-N_5,
```

so $`N_5\le4|E_0|=O(q)`$. Consequently,

```math
\boxed{
\text{all but }O(\sqrt n)\text{ vertices have degree }4
\text{ and are incident only with unit-rhombus faces.}
}
\tag{10.11}
```

For each fixed $`\varepsilon>0`$, excluding also the vertices incident to the $`O_\varepsilon(\sqrt n)`$ exceptional rhombi in Corollary 10.3 shows that all but $`O_\varepsilon(\sqrt n)`$ vertices are surrounded by rhombi whose acute angles lie between $`60^\circ`$ and $`60^\circ+\varepsilon`$.

The estimate remains asymptotic. It does not force any exact equality $`\theta_F=60^\circ`$.

### Theorem 10.6: exact train-track bounds

Let $`\mathcal R`$ be any finite collection of the bounded four-faces from Lemma 10.1, regarded as an edge-to-edge rhombic complex. It may be disconnected and may have holes. Write

```math
R=|\mathcal R|
```

and let $`B_{\mathcal R}`$ be the number of contact edges incident to exactly one face of $`\mathcal R`$.

Declare opposite edges of a rhombus equivalent and take the transitive closure. The resulting equivalence classes are the **train tracks** of $`\mathcal R`$. If $`T`$ is their number, then

```math
\boxed{
B_{\mathcal R}=2T,
\qquad
R\le \frac{T^2}{4}=\frac{B_{\mathcal R}^2}{16}.
}
\tag{10.12}
```

Consequently,

```math
\boxed{B_{\mathcal R}\ge4\sqrt R.}
\tag{10.13}
```

#### Proof

All edges belonging to one track are parallel. Orient a unit vector $`u`$ along them and draw the track centerline by joining midpoints of opposite track edges across each rhombus. Orient this centerline so that

```math
h_u(x)=\det(u,x)
```

increases. It increases strictly across every rhombus. At a shared edge the next rhombus lies on the other side, so the same orientation continues. A track therefore cannot close or self-intersect. Since the complex is finite, it is a path with two boundary edges. Conversely, every boundary edge ends exactly one track. Hence $`B_{\mathcal R}=2T`$.

Two tracks can cross only in a rhombus, and they cross at most once. Here the strict angle bound is essential. Every directed segment of the $`u`$-track has angle from $`u`$ in

```math
\left(\frac\pi3,\frac{2\pi}3\right).
\tag{10.14}
```

Therefore every forward displacement along it belongs to the open convex cone $`C_u`$ with that angular interval. If a $`v`$-track crosses it, orient $`v`$ so that its direction at the crossing belongs to $`C_u`$, and write $`\phi=\arg_u v`$. Then

```math
\frac\pi3<\phi<\frac{2\pi}3,
```

while the forward-displacement cone of the $`v`$-track has angular interval

```math
\left(\phi+\frac\pi3,\phi+\frac{2\pi}3\right).
```

This interval is disjoint from both $`C_u`$ and $`-C_u`$. If the tracks crossed at two points $`P,Q`$, label them so that $`Q-P`$ is a forward displacement on the $`v`$-track. According to their order on the $`u`$-track, the same vector would lie in $`C_u`$ or $`-C_u`$, a contradiction. This argument does not use simple connectedness.

Form the graph whose vertices are tracks and whose edges are their crossings. It is simple by the preceding paragraph. It is triangle-free: three pairwise crossing tracks would give three points on the projective direction circle, of circumference $`\pi`$, whose three pairwise circular separations were all strictly greater than $`\pi/3`$. The three circular gaps cannot then sum to $`\pi`$.

Mantel's inequality gives at most $`T^2/4`$ crossing pairs. Every rhombus is one crossing, proving (10.12) and (10.13). ∎

### Corollary 10.7: almost every track enters the defect network

Return to the jammed hypotheses, and take $`\mathcal R=\mathcal F_4`$. Let $`h_{\mathcal R}`$ count its boundary edges lying on $`\partial\operatorname{conv}A`$, and put

```math
b_{\mathcal R}=B_{\mathcal R}-h_{\mathcal R}.
```

At most two train tracks have both end edges on the convex hull. Therefore

```math
\boxed{
b_{\mathcal R}
\ge \frac{B_{\mathcal R}}2-2
\ge2\sqrt{F_4}-2
=2\sqrt n-O(1).
}
\tag{10.15}
```

Also $`h_{\mathcal R}\le q`$, and hence

```math
b_{\mathcal R}\ge4\sqrt{F_4}-q.
\tag{10.16}
```

Every edge counted by $`b_{\mathcal R}`$ either borders a bounded nonquadrilateral face or lies on a non-hull boundary component or indentation of the rhombic complex.

#### Proof

Theorem 8.2 makes every point of $`A`$ on the convex hull an extreme vertex, so directed hull-edge angles turn strictly. A directed track centerline enters the rhombic complex through one end edge and leaves through the other; the two parallel end edges consequently have opposite induced boundary orientations. Strict turning also means that two different hull-to-hull tracks cannot use the same unoriented direction. Thus the end edges of any two such tracks alternate in the cyclic hull order. Their centerlines are arcs in the convex disk with alternating endpoints and must cross. The crossing graph induced by hull-to-hull tracks is therefore complete; Theorem 10.6 makes it triangle-free, so it has at most two vertices.

Every remaining track supplies at least one non-hull end edge. This proves (10.15). A hull contact edge joins consecutive hull vertices, so there are at most $`q`$ such edges; (10.13) now gives (10.16). ∎

There is also an exact convex exception theorem. If the closed strict rhombi tile a convex polygon and every boundary vertex is extreme, then every track is hull-to-hull, so the preceding proof leaves two tracks and one crossing: the complex is one rhombus. Under the jammed hypotheses, if the rhombi tile all of $`\operatorname{conv}A`$, all four vertices of that rhombus belong to $`Q`$. A nonsquare rhombus has only the endpoints of its longer diagonal in $`Q`$, so the rhombus must be the unit square.

For comparison with the planar excess variables, if $`s`$ is the number of bounded nonquadrilateral faces, then

```math
B_{\mathcal R}
\le k+\sum_{F\notin\mathcal R}|\partial F|
=k+4s+X
\le k+5X
\le20q-4k-20c.
\tag{10.17}
```

Thus (10.15) is a real boundary-order demand, but the existing face-excess budget is still large enough to absorb it.

### Theorem 10.8: track width and exact angular-defect charge

Let

```math
D_{\mathcal R}=\operatorname{diam}V(\mathcal R),
\qquad
\chi_*=\frac{6-3\sqrt3}{\pi}.
```

Then, with no connectedness or disk assumption,

```math
\boxed{
B_{\mathcal R}D_{\mathcal R}
\ge4\sum_{F\in\mathcal R}\sin\theta_F
\ge2\sqrt3R+4\chi_*\sum_{F\in\mathcal R}\delta_F.
}
\tag{10.18}
```

If $`\mathcal R`$ is a topological disk and $`v=|V(\mathcal R)|`$, then

```math
v=R+\frac{B_{\mathcal R}}2+1
```

and

```math
\boxed{
v\ge R+2\sqrt R+1=(\sqrt R+1)^2,
\qquad
R\le(\sqrt v-1)^2.
}
\tag{10.19}
```

#### Proof

Across a rhombus $`F`$, the increase of the track coordinate $`h_u`$ in the proof of Theorem 10.6 is exactly $`\sin\theta_F`$. The two endpoint midpoints lie in $`\operatorname{conv}V(\mathcal R)`$, so every track $`\tau`$ satisfies

```math
\sum_{F\in\tau}\sin\theta_F\le D_{\mathcal R}.
```

There are $`B_{\mathcal R}/2`$ tracks and every rhombus belongs to two of them. This proves the first inequality in (10.18). Concavity of sine on $`[\pi/3,\pi/2]`$ gives the chord estimate

```math
\sin\left(\frac\pi3+\delta\right)
\ge\frac{\sqrt3}{2}+\chi_*\delta,
```

which proves the second.

For a disk quadrangulation, Euler and edge-face incidence counting give

```math
v-e+R=1,
\qquad
4R=2e-B_{\mathcal R}.
```

Eliminate $`e`$ and use (10.13) to obtain (10.19). ∎

### Theorem 10.9: a global restriction on Cartesian train grids

Suppose a rhombic complex contains an additive $`a\times b`$ train-grid block with vertices

```math
p_{ij}=p+x_i+y_j,
\qquad
0\le i\le a,\qquad 0\le j\le b,
```

where

```math
u_i=x_i-x_{i-1},\quad |u_i|=1,
\qquad
v_j=y_j-y_{j-1},\quad |v_j|=1,
```

and all cell orientations are consistent:

```math
\det(u_i,v_j)=\sin\theta_{ij}>0.
```

Here $`\theta_{ij}`$ denotes the acute angle between the two edge directions, and
the coherent orientation hypothesis includes
$`\theta_{ij}\in(\pi/3,\pi/2]`$ for every cell. The determinant condition by
itself is not enough: it also permits an obtuse oriented angle, for which the
chord estimate used below is not valid.

Then

```math
\boxed{
D_{\mathcal R}^2
\ge2\sum_{i=1}^a\sum_{j=1}^b\sin\theta_{ij}
\ge\sqrt3ab+2\chi_*\Delta_{a,b},
}
\tag{10.20}
```

where $`\Delta_{a,b}=\sum_{i,j}(\theta_{ij}-\pi/3)`$. Moreover, for every $`n`$,

```math
\boxed{D(n)^2<\frac{2\sqrt3}{\pi}n.}
\tag{10.21}
```

Consequently every such block in an $`n`$-point global minimizer obeys

```math
\boxed{
ab+\frac{4\sqrt3-6}{\pi}\Delta_{a,b}
<\frac2\pi n.
}
\tag{10.22}
```

In particular $`ab<2n/\pi`$.

#### Proof

Put $`U=\sum_i u_i`$ and $`V=\sum_jv_j`$. The block contains

```math
p,\qquad p+U,\qquad p+V,\qquad p+U+V,
```

and

```math
\det(U,V)=\sum_{i,j}\sin\theta_{ij}.
```

Both $`U+V`$ and $`U-V`$ are differences of block vertices. Hence

```math
2|\det(U,V)|
=|\det(U+V,U-V)|
\le|U+V|\,|U-V|
\le D_{\mathcal R}^2.
```

This proves (10.20).

For (10.21), average the number of points of the unit triangular lattice in an **open** radius-$`r`$ disk over translations modulo a fundamental cell. The average is

```math
\frac{\pi r^2}{\sqrt3/2}.
```

Choose $`r`$ so that this average is $`n`$. Some translate contains at least $`n`$ lattice points. Any chosen $`n`$ of them form a finite subset of the open disk and therefore have diameter strictly less than $`2r`$. This proves (10.21). Combining it with (10.20), and using

```math
\frac{2\chi_*}{\sqrt3}=\frac{4\sqrt3-6}{\pi},
```

gives (10.22). ∎

The additive block hypothesis is substantive. A dense triangle-free train-crossing graph need not contain a Cartesian block holding a comparable fraction of all its crossings.

### Proposition 10.10: a five-sector boundary-pinned countermodel

The local train-track, defect, stress, and pinned-jamming conclusions still do not use the decisive diametral-hull condition.

Fix $`s\ge2`$ and $`0<\varepsilon<\pi/24`$. Choose unit vectors $`w_0,\ldots,w_4`$ in counterclockwise order with successive oriented gaps

```math
\gamma_0=\gamma_1=\gamma_2=\gamma_3
=\frac\pi3+\varepsilon,
\qquad
\gamma_4=\frac{2\pi}3-4\varepsilon,
```

where $`w_5=w_0`$. Define

```math
S_{s,\varepsilon}
=\bigcup_{i\in\mathbb Z/5\mathbb Z}
\left\{aw_i+bw_{i+1}:0\le a,b\le s, a,b\in\mathbb Z\right\}.
\tag{10.23}
```

The five sector grids meet along their radial sides. Their union is an edge-to-edge disk complex with

```math
\boxed{
n=5s^2+5s+1,
\qquad
R=5s^2,
\qquad
B_{\mathcal R}=10s.
}
\tag{10.24}
```

Its $`T=5s`$ tracks fall into five classes of size $`s`$, one for each direction $`w_i`$. Every track crosses precisely the tracks in the two adjacent direction classes. Thus the crossing graph is the balanced blow-up of $`C_5`$. Its largest complete bipartite subgraph contains only

```math
2s^2=\frac{2R}{5}
```

crossings.

Four sectors have rhombus defect $`\varepsilon`$ and the fifth has defect $`4\varepsilon`$, so

```math
\boxed{
\sum_F\delta_F=8\varepsilon s^2.
}
\tag{10.25}
```

The vertex set is unit-separated, its contact graph consists exactly of the grid edges, and it is triangle-free. All but $`O(s)`$ vertices have degree four, and its diameter is $`O(s)=O(\sqrt n)`$.

If every vertex on the boundary of this five-sector complex is pinned, its expansive cone is zero and it admits a stress positive on every contact edge. In particular, choosing

```math
\varepsilon_s=s^{-3}
```

gives arbitrarily large, triangle-free, boundary-pinned jammed complexes with

```math
R=n-O(\sqrt n),
\qquad
\sum_F\delta_F=\frac8s=o(1).
\tag{10.26}
```

#### Proof

Within one sector, the difference of two vertices is $`aw_i+bw_{i+1}`$ with integers $`a,b`$. Let $`\gamma\in(\pi/3,2\pi/3)`$ be the oriented angle between the two generators. If $`ab\ge0`$ and both coefficients are nonzero, the shortest case is their unit sum and has squared length $`2+2\cos\gamma>1`$. If $`ab<0`$ and $`\cos\gamma>0`$, writing $`r=|a|`$ and $`t=|b|`$ gives

```math
r^2+t^2-2rt\cos\gamma
=(r-t)^2+2rt(1-\cos\gamma)>1.
```

The case $`\cos\gamma\le0`$ is immediate. Equality therefore occurs only for a coordinate unit vector.

For adjacent sectors, points off their shared radial ray lie on opposite sides of it, each at perpendicular distance at least $`\sin(\pi/3)`$; if one point lies on the ray, the same two-generator calculation applies. Two nonadjacent sector cones are separated by an angle $`\alpha>\pi/3`$. Their nonzero lattice points have norms $`r,t\ge1`$, and

```math
|x-y|^2=(r-t)^2+2rt(1-\cos\alpha)>1.
```

This proves unit separation and identifies all contacts. The five sector cones have disjoint interiors, so their rhombi do not overlap. Gluing five $`(s+1)\times(s+1)`$ grids along their radial chains gives (10.24), and (10.25) is immediate.

Across a radial seam, the $`s`$ half-tracks of direction $`w_i`$ in its two adjacent sectors join pairwise. Hence there are exactly $`s`$ complete tracks in each of the five direction classes. A class-$`i`$ track crosses all $`s`$ tracks in classes $`i-1`$ and $`i+1`$ and no others. This proves the asserted balanced $`C_5`$ crossing graph. In a $`C_5`$ blow-up, a complete bipartite subgraph is maximized by taking one full class on one side and its two neighboring classes on the other, giving $`2s^2`$ crossings.

To see full rank after the outer boundary is pinned, first consider a contact-preserving infinitesimal motion. In each sector the vertex $`(s-1)w_i+(s-1)w_{i+1}`$ has two nonparallel contacts to pinned outer-side vertices, so its velocity is zero. The same two-direction argument fixes the rest of the layer $`\max\{a,b\}=s-1`$. Induction on the layers fixes the whole complex.

It remains to construct a positive pinned equilibrium stress. At the radial seam in direction $`w_i`$, the vector $`w_i`$ lies strictly inside the cone generated by $`w_{i-1}`$ and $`w_{i+1}`$, because

```math
\gamma_{i-1}+\gamma_i<\pi.
```

Choose positive $`a_i^-,a_i^+,\lambda_i`$ such that

```math
a_i^-w_{i-1}+a_i^+w_{i+1}=\lambda_iw_i.
\tag{10.27}
```

Give every off-seam grid line ending at that seam its corresponding weight $`a_i^-`$ or $`a_i^+`$. Opposite edges then cancel at every ordinary grid vertex. Give the radial edge from $`rw_i`$ to $`(r+1)w_i`$ weight $`\rho_{i,r}`$. At an internal seam vertex equilibrium is exactly

```math
\rho_{i,r-1}=\rho_{i,r}+\lambda_i.
\tag{10.28}
```

Because the five rays surround the origin with every gap less than $`\pi`$, there are $`d_i>0`$ with $`\sum_i d_iw_i=0`$. Scale them until $`d_i>s\lambda_i`$, put $`\rho_{i,0}=d_i`$, and define $`\rho_{i,r}=d_i-r\lambda_i`$. All weights are positive, (10.28) holds, and the center is in equilibrium.

For an expansive velocity pinned on the boundary, multiply every contact inequality by this positive stress and sum. Interior equilibrium makes the sum zero, so every contact derivative is zero. The full-rank argument in the preceding paragraph then makes the velocity zero. ∎

There is also a useful exact finite regression test in which the pins really are the diameter endpoints. Let $`w_0,\ldots,w_4`$ be the five unit vectors at successive angles $`2\pi/5`$ and take

```math
S=\{0\}\cup\{w_i:0\le i<5\}
\cup\{w_i+w_{i+1}:0\le i<5\}.
\tag{10.27a}
```

This is an 11-point, triangle-free union of five $`72^\circ`$ unit rhombi. Its five outer points $`w_i+w_{i+1}`$ form a regular pentagon, are exactly the convex-hull vertices, and every one is a diameter endpoint. Pinning only these five points gives zero expansive cone. Indeed, at each radial point $`w_i`$, its two contacts to the pinned hull have directions $`w_{i-1}`$ and $`w_{i+1}`$; a positive stress with weight (1) on those edges and weight $`2\cos(2\pi/5)`$ on the edge to the center is in equilibrium. The five center-edge forces sum to zero. Positivity turns every expansive derivative into an equality, the two nonparallel pinned contacts fix each $`w_i`$, and the radial contacts then fix the center.

For an exact distance check, put $`\varphi=(1+\sqrt5)/2`$ and $`z_i=w_i+w_{i+1}`$. Then $`|z_i|=\varphi`$, the inner pentagon has side length $`2\sin(\pi/5)>1`$, and every outer-pentagon side is also longer than (1). Rotational symmetry reduces the mixed distances to

```math
|z_j-w_i|^2=
\begin{cases}
1,&j-i\equiv0,-1\pmod5,\\[2mm]
(7+\sqrt5)/2,&j-i\equiv1,3\pmod5,\\[2mm]
(7+3\sqrt5)/2,&j-i\equiv2\pmod5.
\end{cases}
```

Thus the displayed edges are exactly all unit contacts. The outer pentagon has inradius $`\varphi^2/2>1`$, so it contains the five $`w_i`$ strictly. Its diagonals are the unique longest distance class and have squared length $`5+2\sqrt5`$. This verifies the hull and diameter assertions.

Thus even the exact conditions $`Q=V(\operatorname{conv}A)`$, positive pinned stress, zero pinned cone, and strict rhombic faces do not force a $`60^\circ`$ face at finite size. Its diameter is

```math
\sqrt{5+2\sqrt5}>3,
```

whereas the unit triangular lattice contains the following 12-point set of diameter (3):

```math
\{(a,b):
(a,b)\in
\{(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),
(2,0),(2,1),(2,2),(3,0),(3,1)\}\},
\tag{10.27b}
```

where $`(a,b)`$ denotes $`a(1,0)+b(1/2,\sqrt3/2)`$. For every nonzero integer difference, $`a^2+ab+b^2\ge1`$, while a direct check of the finitely many displayed differences gives $`a^2+ab+b^2\le9`$, with equality for $`(0,1)`$ and $`(3,1)`$. Thus the set is unit-separated and has diameter (3). Any 11 of these points beat the sun. The sun is therefore an exact adversarial test of local arguments, not a candidate for Target C.

The large five-sector family is an exact warning. It defeats any proposed quantization of positive rhombus defect, any maximum principle based only on a pinned boundary, and any argument using only positive equilibrium stress. What that large family does **not** satisfy is Theorem 8.2: most pinned boundary points are nonextreme and nondiametral. The 11-point sun shows in turn that the diametral-hull condition alone is not a finite local contradiction. Global capacity, or an equivalent large-scale extremality input, remains indispensable.

### Corollary 10.11: the exact ideal-disk boundary budget

Suppose an $`n`$-point global minimizer is exactly the vertex set of a topological-disk rhombic complex $`\mathcal R`$. Put

```math
G=\operatorname{area}(\operatorname{conv}A)
-\sum_{F\in\mathcal R}\operatorname{area}(F),
\qquad
\Delta=\sum_F\delta_F.
```

Then

```math
\boxed{
4G+4\chi_*\Delta
<\sqrt3B_{\mathcal R}+2\sqrt3.
}
\tag{10.29}
```

Indeed, Theorem 10.8 gives $`n=R+B_{\mathcal R}/2+1`$, while (10.21), the isodiametric inequality, and the sine chord estimate give

```math
\frac{\sqrt3}{2}R+\chi_*\Delta+G
\le\operatorname{area}(\operatorname{conv}A)
<\frac{\sqrt3}{2}n.
```

Thus a reverse boundary-shell inequality, with exact correction terms for exceptional faces, holes, components, and vertices outside the rhombic core, would eliminate the jammed branch. Proposition 10.10 proves that no such reverse inequality follows from strict defects, positive stress, and boundary-pinned jamming alone.

### Theorem 10.12: support cost and classification for two fixed directions

Let $`\mathcal R`$ be a connected finite unit-rhombus complex whose cell union has a simple outer boundary, with holes allowed but no pinched boundary vertices. Assume all edges use two fixed unoriented directions. Let $`K_\partial`$ consist of all hole-boundary incidences together with selected outer-boundary incidences only at vertices that are not vertices of $`\operatorname{conv}V(\mathcal R)`$, chosen so that:

1. every incidence on a hole boundary belongs to $`K_\partial`$; and
2. every outer-boundary vertex that is not a vertex of $`\operatorname{conv}V(\mathcal R)`$ and is uncharged admits a strictly positive equilibrium using only the incident edges of $`\mathcal R`$.

Thus any non-hull vertex that needs a contact outside $`\mathcal R`$ or another external reaction must be charged to $`K_\partial`$. Put $`k=|K_\partial|`$. Then

```math
\boxed{
R\le(k+3)^2,\qquad k\ge\sqrt R-3.
}
\tag{10.30}
```

If $`k=0`$, there is a complete classification:

```math
\boxed{
\mathcal R\text{ is either one rhombus or the five-rhombus cross.}
}
\tag{10.31}
```

#### Proof

Apply an invertible affine map carrying the two unit edge vectors to the coordinate vectors. The complex becomes a finite union of unit squares. Positive linear equilibrium and convexity are preserved.

At a locally convex outer-boundary vertex, all incident internal edge vectors lie in a closed half-plane and at least one points strictly inward, so no strictly positive combination can vanish. At a straight boundary vertex, the two tangent directions may cancel but every remaining internal edge points strictly inward. Hence every outer-boundary vertex outside $`K_\partial`$ is either a convex-hull vertex or a reflex vertex with all four coordinate edge directions present.

Consider the boundary path between two consecutive convex-hull vertices. If its interior contains no incidence from $`K_\partial`$, every internal turn is reflex. There can be at most two such turns: three consecutive right-angle reflex turns produce four successive unit coordinate vectors whose sum is zero, returning to the initial vertex before reaching the next hull vertex. The hull chord is therefore a sum of one, two, or three successive coordinate unit vectors. Its direction is one of

```math
\pm e_1,\quad\pm e_2,\quad
\pm(e_1+e_2),\quad\pm(e_1-e_2).
\tag{10.32}
```

A convex polygon has at most one side in each of these eight oriented directions. If $`q`$ is its number of vertices and $`k_{\rm out}`$ is the number of charged outer-boundary incidences, at most eight of the $`q`$ gaps between consecutive hull vertices are uncharged. Therefore

```math
q\le k_{\rm out}+8.
\tag{10.33}
```

Let $`C,L,Z`$ denote the numbers of convex, reflex, and straight incidences of the outer orthogonal boundary. Then

```math
C-L=4,\qquad
B_{\rm out}=C+L+Z=2C+Z-4.
```

Write $`C=q+C_K`$, where $`C_K`$ counts the charged non-hull convex incidences. Since every straight incidence is also charged, (10.33) gives

```math
B_{\rm out}
\le12+2k_{\rm out}+2C_K+Z
\le12+4k_{\rm out}.
```

All inner-boundary incidences are charged, and a simple orthogonal inner boundary has the same number of edge and vertex incidences. Consequently

```math
B_{\mathcal R}\le12+4k.
\tag{10.34}
```

The tracks split into two straight families of sizes $`m`$ and $`r`$. Tracks in one family do not cross, and an opposite-family pair crosses at most once. Hence

```math
R\le mr
\le\frac{(m+r)^2}{4}
=\frac{B_{\mathcal R}^2}{16}
\le(k+3)^2,
```

proving (10.30).

It remains to classify equality-free support, $`k=0`$. There are no holes or straight boundary vertices; every convex boundary vertex is a hull vertex and every other boundary vertex is reflex. Between consecutive convex turns let $`r_i\in\{0,1,2\}`$ be the number of reflex turns. Total turning and (10.33) give

```math
\sum_{i=1}^{C}(1-r_i)=4,\qquad 4\le C\le8.
\tag{10.35}
```

This leaves a finite exact closure check. Start with $`d_1=e_1`$, let $`J`$ be a positive quarter-turn, and set

```math
d_{i+1}=J^{1-r_i}d_i,\qquad
s_i=\sum_{j=0}^{r_i}J^{-j}d_i.
\tag{10.36}
```

Here $`s_i`$ is the hull chord between consecutive convex turns. Impose $`\sum_i s_i=0`$, no repeated proper partial sum of the individual unit steps, and strict consistent turning of the hull chords. Direct substitution of $`r_i\in\{0,1,2\}`$ gives, up to cyclic shift and reversal,

```math
\begin{array}{c|c|c}
C&\text{closed words}&\text{simple word with strict hull}\\ \hline
4&0000&0000\\
5&-&-\\
6&001001&-\\
7&-&-\\
8&00020002,\ 00101002,\ 00110011,\ 01010101
&01010101.
\end{array}
```

The word $`0000`$ bounds one square. The alternating word bounds the plus-shaped union of a central square and its four edge-neighbors. Applying the inverse affine map proves (10.31). ∎

Thus a large two-direction oblique-lattice core cannot be supported only at its diametral hull vertices. An $`R`$-face core needs at least $`\sqrt R-3`$ non-hull interface supports. The general $`O(\sqrt n)`$ defect shell can pay this cost, so the theorem sharply constrains but does not eliminate the jammed branch.

---
