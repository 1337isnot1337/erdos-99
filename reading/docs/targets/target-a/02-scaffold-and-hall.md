> Generated reading edition · [exact source](../../../../docs/targets/target-a/02-scaffold-and-hall.md) · source SHA-256 `18b0297422f207a1b3afdea166b413ccd86d9a5d9c26d26da9794d3e6ac39548`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A: scaffold capacity and Hall reductions

> Canonical v1.7.0 route module. The original section numbering is preserved for
> cross-references; see the [route map](../README.md).

# 70. Version history and provenance through v1.2.0

> **HISTORICAL VERSION LEDGER.** This section was the v1.2 endpoint. The current
> version ledger is Section 78.

- **v1.0.0 (2026-08-26):** canonical synthesis and second-pass audit through the
  translated-lattice, phase-atomic, first-order cusp, backward-flip, tangent-quartic,
  support-turning, and hybrid-forest reductions.
- **v1.1.0 (2026-08-26):** promotes the minimal-face harmonic--Dirichlet,
  peripheral-dual, terminal direction-network/turn, boundary-velocity, exact plateau,
  and optimal-flat results; rejects the cycle-lift shortcut; corrects facial peeling.
- **v1.2.0 (2026-08-26):** promotes the rooted-forest self-stress identity,
  root-skeleton exactification, affine triangle-factor exclusion, forest
  rattlerization, same-diameter saturation, strict replacement/collar reduction,
  terminal-component Minkowski splitting, componentwise closure/equality theorem, and
  stochastic-width control of component rotations.  The authoritative remaining
  branches are saturated rattler capacity and internal terminal-component blocker
  rank.

The only supplied external literature remains:

1. `mp05-2-261-269.pdf`;
2. `1951-03.pdf`;
3. `1-s2.0-S0097316598928898-main.pdf`;
4. `s00454-002-0747-6.pdf`;
5. `1204.4403v1.pdf`;
6. `463.pdf`;
7. `10.1007_PL00009374.pdf`.

No internet source is part of this theorem-state file.

---

# 71. Compatible collar and exact safe-scaffold population

This section upgrades the population-only replacement of Section 63 to a scaffold
that is already geometrically compatible with an independently chosen smaller
optimum.

Keep the saturated Target A normalization. Thus

```math
|A|=N,
\qquad
\operatorname{diam}(A)=D,
\qquad
\rho=|\mathscr R|,
```

where $`\mathscr R`$ is the retained strict-rattler set. Put

```math
m=N-\rho,
\qquad
d=D(m),
\qquad
t=\frac{D-d}{2}.
\tag{71.1}
```

Let $`X_m`$ be an independently chosen $`m`$-point optimum, let
$`K_m=\operatorname{conv}X_m`$, and write

```math
P_m=\operatorname{per}K_m,
\qquad
\varepsilon_m=\pi d-P_m.
\tag{71.2}
```

The trusted perimeter-deficit theorem gives

```math
0\le\varepsilon_m<2\pi c_0=\pi a_0,
\qquad
a_0=\frac{\sqrt3}{2}.
\tag{71.3}
```

Define

```math
\boxed{
C_{\rm col}
:=
\pi\left(\frac12+\frac2{\sqrt3}\right)
=
5.198395055263\ldots .
}
\tag{71.4}
```

## 71.1 Unconditional compatible-collar dichotomy

> **Theorem 71.1 (compatible-collar dichotomy).**
> One has
> 

```math
> \boxed{
> \rho<C_{\rm col}D
> }
> \tag{71.5}
> 
```
> or else $`t>1`$ and there is a translated unit triangular-lattice set
> $`S`$ such that
> 

```math
> X:=X_m\cup S
> \subset
> \operatorname{int}(K_m+t\mathbb B),
> \tag{71.6}
> 
```
> $`X`$ is unit-separated,
> 

```math
> \boxed{\operatorname{diam}(X)<D,}
> \tag{71.7}
> 
```
> and
> 

```math
> \boxed{
> |X|>N-C_{\rm col}D+\frac{2\pi}{\sqrt3}.
> }
> \tag{71.8}
> 
```
> In particular, the weaker but cleaner statement
> 

```math
> |X|>N-C_{\rm col}D
> \tag{71.9}
> 
```
> always holds in the second alternative.

### Proof

If $`t\le1`$, then

```math
D^2-d^2
=(D-d)(D+d)
=2t(D+d)
\le4D.
\tag{71.10}
```

The trusted collar inequality (63.7) says

```math
D^2-d^2
>
c\left(\rho-\frac{\pi D}{2}\right),
\qquad
c=\frac{2\sqrt3}{\pi}.
\tag{71.11}
```

Hence

```math
\rho
<
\frac{\pi D}{2}+\frac{4D}{c}
=
\pi\left(\frac12+\frac2{\sqrt3}\right)D
=C_{\rm col}D.
\tag{71.12}
```

Thus $`\rho\ge C_{\rm col}D`$ forces $`t>1`$.

Assume now $`t>1`$ and define the safe collar

```math
\Omega
:=
\operatorname{int}(K_m+t\mathbb B)
\setminus
(K_m+\mathbb B).
\tag{71.13}
```

Every point of $`\Omega`$ is at distance strictly greater than $`1`$ from every
point of $`X_m`$. Steiner's formula gives

```math
\begin{aligned}
|\Omega|
&=P_m(t-1)+\pi(t^2-1)\\
&=\frac{\pi}{4}(D^2-d^2)-\pi(d+1)-\varepsilon_m(t-1).
\end{aligned}
\tag{71.14}
```

Using (71.3), (71.11), and $`\pi c/4=a_0`$,

```math
\frac{|\Omega|}{a_0}
>
\rho-
\left[
\frac{\pi D}{2}
+
\frac{\pi(d+1)}{a_0}
+
\pi(t-1)
\right].
\tag{71.15}
```

Since $`d=D-2t`$, the bracket equals

```math
C_{\rm col}D
+
\pi\left(1-\frac4{\sqrt3}\right)t
+
\pi\left(\frac2{\sqrt3}-1\right).
\tag{71.16}
```

Therefore

```math
\boxed{
\frac{|\Omega|}{a_0}
>
\rho-C_{\rm col}D
+
\pi\left(\frac4{\sqrt3}-1\right)t
+
\pi\left(1-\frac2{\sqrt3}\right).
}
\tag{71.17}
```

For $`t\ge1`$, this implies the uniform estimate

```math
\boxed{
\frac{|\Omega|}{a_0}
>
\rho-C_{\rm col}D+\frac{2\pi}{\sqrt3}.
}
\tag{71.18}
```

For completeness, the strictness needed below is a property of this particular
parallel-body collar, not of arbitrary measurable sets.  If

```math
F(v):=|(\Lambda+v)\cap\Omega|,
\qquad v\in\mathbb R^2/\Lambda,
```

then $`F`$ has mean $`|\Omega|/a_0`$ by periodization.  It is also a nonconstant
integer-valued function.  Indeed, $`K_m`$ is the convex hull of finitely many
points, so an outer offset $`\partial(K_m+t\mathbb B)`$ contains a nonempty
circular arc (with the degenerate segment/point cases giving the usual capsule or
circle).  Choose a regular point of such an arc away from the finitely many other
translated boundary sheets in a fundamental cell.  Distinct circular sheets of
the same radius can coincide only when their centers coincide; coincident outer
sheets have the same inside side and therefore contribute with the same sign.
The inner sheets have a different radius, so they cannot cancel this jump.  A
small translation across the chosen point therefore changes $`F`$ by a nonzero
integer.  Consequently some translate has
$`F(v)>|\Omega|/a_0`$: if every value were at most its mean, integrality would
force the mean down to the largest attained integer, while nonconstancy makes
that inequality strict.

The same strict translation-averaging argument used in the translated-lattice
theorem supplies a translate of the unit triangular lattice having

```math
k>
\rho-C_{\rm col}D+\frac{2\pi}{\sqrt3}
\tag{71.19}
```

sites in $`\Omega`$. Let $`S`$ be those sites. The lattice sites are mutually
unit-separated and are strictly more than unit distance from $`X_m`$, so
$`X_m\cup S`$ is unit-separated.

The closed parallel body $`K_m+t\mathbb B`$ has diameter $`d+2t=D`$. No two
interior points can realize that diameter: otherwise one endpoint could be moved a
small positive distance farther along the joining line while remaining in the closed
parallel body, contradicting its diameter. Hence every finite subset of its interior,
in particular $`X_m\cup S`$, has diameter strictly less than $`D`$.
Finally

```math
|X_m\cup S|
=m+k
>
N-C_{\rm col}D+\frac{2\pi}{\sqrt3}.
```

This proves the theorem. $`\square`$

## 71.2 Interpretation

The theorem is stronger than the open-disk population estimate (63.4): the new sites
are already simultaneously compatible with the chosen $`m`$-point optimum. It does
**not** yet provide all $`N`$ points. In a surviving counterexample the exact number
of missing sites after the safe-collar insertion is

```math
j:=N-(m+k)=\rho-k.
\tag{71.20}
```

If $`j\le0`$, the theorem already contradicts $`D(N)=D`$. Hence every survivor must
satisfy

```math
\boxed{
1\le j=\rho-k
<
C_{\rm col}D-\frac{2\pi}{\sqrt3}.
}
\tag{71.21}
```

Thus the remaining compatible-grafting demand is explicitly boundary-order.

---

# 72. Deep Voronoi containment and global clearance budget

Return to the original saturated triangle-free global minimizer $`A`$, with
$`K=\operatorname{conv}A`$. Define the nearest-neighbor clearance

```math
\delta(p):=
\min_{q\ne p}|p-q|-1
\ge0.
\tag{72.1}
```

A crucial warning is already visible here: strictness gives $`\delta(p)>0`$ for a
strict rattler, but there is no uniform lower bound on $`\delta(p)`$.

## 72.1 Deep Voronoi cells remain in the saturated hull

Let

```math
B_\partial
:=
\{p\in A:\operatorname{dist}(p,\partial K)\le1\},
\qquad
b:=|B_\partial|.
\tag{72.2}
```

> **Lemma 72.1 (deep Voronoi containment).**
> If $`p\notin B_\partial`$, then its Voronoi cell satisfies
> 

```math
> \boxed{V_p\subset K.}
> \tag{72.3}
> 
```

### Proof

Suppose some $`x\in V_p`$ lies outside $`K`$. Since $`V_p`$ is convex and contains
$`p`$, the first point

```math
y=[p,x]\cap\partial K
```

also belongs to $`V_p`$. But $`p`$ is more than unit distance from $`\partial K`$, so
$`|p-y|>1`$. Saturation of $`K`$ supplies $`q\in A`$ with $`|q-y|\le1`$, contradicting
the nearest-site inequality defining $`V_p`$. $`\square`$

Consequently every Delaunay face incident to a deep vertex has circumcenter in $`K`$
and circumradius at most $`1`$. In a cocircular degeneracy, triangulate the empty
Delaunay polygon arbitrarily; all resulting triangles share the same admissible
circumcenter.

## 72.2 Sharp local Delaunay clearance inequality

For a Delaunay triangle $`T`$ and a vertex $`v\in T`$, define

```math
\mu_T(v)
:=
\min\{\text{the two side lengths of }T\text{ incident to }v\}-1.
\tag{72.4}
```

> **Theorem 72.2 (local clearance inequality).**
> If $`T`$ has all side lengths at least $`1`$ and circumradius at most $`1`$, then
> 

```math
> \boxed{
> \operatorname{area}(T)-\frac{\sqrt3}{4}
> \ge
> \frac{\sqrt3}{6}
> \sum_{v\in T}\mu_T(v).
> }
> \tag{72.5}
> 
```
> The coefficient $`\sqrt3/6`$ is sharp. Equality holds exactly for the ordered side
> multisets
> 

```math
> \boxed{
> \{1,1,1\}
> \quad\text{or}\quad
> \{1,1,\sqrt3\}.
> }
> \tag{72.6}
> 
```

### Proof

Order the sides $`1\le a\le b\le c`$, and let $`C`$ be the angle opposite $`c`$.
The circumradius bound and the lower side bound force every angle to be at least
$`\pi/6`$. Hence

```math
\frac\pi3\le C\le\frac{2\pi}{3}.
\tag{72.7}
```

Also $`b\le2\le2a`$. Therefore

```math
\operatorname{area}(T)
=\frac12ab\sin C
\ge
\frac{\sqrt3}{4}ab
\ge
\frac{\sqrt3}{12}(2a^2+b^2),
\tag{72.8}
```

because

```math
3ab-2a^2-b^2=(b-a)(2a-b)\ge0.
\tag{72.9}
```

The three local minima in (72.4) are $`a,a,b`$, so

```math
\sum_{v\in T}\mu_T(v)=2(a-1)+(b-1).
\tag{72.10}
```

Applying $`x^2-1\ge2(x-1)`$ to $`a`$ and $`b`$ proves (72.5).
Equality forces $`a=b=1`$ and $`\sin C=\sqrt3/2`$, so
$`C=\pi/3`$ or $`2\pi/3`$, yielding exactly (72.6). $`\square`$

## 72.3 Boundary-layer and global clearance estimates

Let

```math
h:=|A\cap\partial K|.
\tag{72.11}
```

The disjoint radius-$`1/2`$ disks centered at points of $`B_\partial`$ lie in the
radius-$`3/2`$ tube around $`\partial K`$. Its area is at most

```math
3P+\frac{9\pi}{4},
\qquad P=\operatorname{per}K.
```

Hence

```math
\boxed{
b\le\frac{12P}{\pi}+9\le12D+9.
}
\tag{72.12}
```

Consecutive hull sites have boundary-arc separation at least their Euclidean
separation, hence at least $`1`$, so

```math
\boxed{h\le P\le\pi D.}
\tag{72.13}
```

Choose a Delaunay triangulation and let $`f_0`$ be the number of faces whose three
vertices lie in $`B_\partial`$. Planarity gives

```math
\boxed{f_0\le2b.}
\tag{72.14}
```

There are

```math
F=2N-h-2
\tag{72.15}
```

triangulation faces. Let $`E_{\rm deep}`$ be the total excess
$`\operatorname{area}(T)-a_0/2`$ over faces containing a deep vertex. The strict
translated-lattice theorem and isodiametricity give

```math
\operatorname{area}(K)<a_0(N-1).
\tag{72.16}
```

Therefore

```math
\boxed{
E_{\rm deep}
<
\frac{a_0}{2}(h+f_0).
}
\tag{72.17}
```

Every deep vertex is incident to at least three deep faces, and in each such face its
$`\mu_T`$-contribution is at least $`\delta(p)`$. Since
$`\sqrt3/6=a_0/3`$, summing (72.5) gives

```math
a_0\sum_{p\notin B_\partial}\delta(p)
\le E_{\rm deep},
```

hence

```math
\boxed{
\sum_{p\notin B_\partial}\delta(p)
<
\frac{h+f_0}{2}.
}
\tag{72.18}
```

Saturation also gives $`\delta(p)\le1`$ for every $`p\in A`$: if a nearest-neighbor
distance were $`r>2`$, the midpoint of a nearest-neighbor pair would lie in $`K`$
and be farther than $`1`$ from every site, contradicting unit covering.
Combining (72.12)--(72.18) yields the global theorem.

> **Theorem 72.3 (global clearance budget).**
> 

```math
> \boxed{
> \sum_{p\in A}\delta(p)
> <
> \left(24+\frac{\pi}{2}\right)D+18.
> }
> \tag{72.19}
> 
```

Put

```math
L_D:=
\left(24+\frac{\pi}{2}\right)D+18.
\tag{72.20}
```

The theorem says that a super-boundary strict-rattler population can survive only by
becoming overwhelmingly near-contact.

---

# 73. Near-unit Gabriel matching and the two-well theorem

Assume the saturated Target A survivor contains $`\rho`$ retained strict rattlers.
If

```math
\rho\ge20L_D,
\tag{73.1}
```

then at least $`\rho/2`$ of those rattlers satisfy

```math
\delta(p)\le\frac{2L_D}{\rho}.
\tag{73.2}
```

After discarding the boundary layer, at least $`\rho/2-b`$ selected deep rattlers
remain. Join each selected rattler to one nearest neighbor.

## 73.1 Degree six and a linear matching

Under (73.1), every selected edge has length at most $`1.1`$. If a vertex had seven
selected-edge neighbors, two would make angle at most $`2\pi/7`$. Their mutual
distance would satisfy

```math
|q_1-q_2|^2
\le
\frac1{100}
+
\frac{121}{25}\sin^2\frac\pi7
=
0.9211546795\ldots<1,
\tag{73.3}
```

contradicting unit separation. Thus the selected-edge graph has maximum degree at
most six.

A maximal matching edge $`uv`$ accounts for at most
$`|N[u]\cup N[v]|\le12`$ selected rattlers. Therefore:

> **Theorem 73.1 (deep near-unit matching).**
> There is a matching $`M`$ of nearest-neighbor edges, every edge containing a deep
> strict rattler, such that
> 

```math
> \boxed{
> |M|
> \ge
> \frac{\rho}{24}-D-\frac34,
> }
> \tag{73.4}
> 
```
> and
> 

```math
> \boxed{
> 1<|p-q|
> \le
> 1+\frac{2L_D}{\rho}
> \qquad(pq\in M).
> }
> \tag{73.5}
> 
```

## 73.2 Strong Gabriel/Delaunay promotion

If $`pq`$ is one of the selected edges and $`q`$ is nearest to $`p`$, the closed disk
with diameter $`pq`$ contains no third site. Indeed, any third point in that disk is
strictly closer to $`p`$ than $`q`$. At the midpoint $`z`$ of $`pq`$, every third
site satisfies

```math
|z-x|>\frac{|p-q|}{2}.
\tag{73.6}
```

Hence $`V_p\cap V_q`$ contains a nondegenerate segment: $`pq`$ is a strong Gabriel,
and therefore strong Delaunay, edge. All edges of the matching $`M`$ can be included
simultaneously in one Delaunay triangulation. Rechoose such a triangulation from now
on. The global excess estimate (72.17) applies to this triangulation as well.

Because every matching edge contains a deep endpoint, it is not a hull edge and has
two incident deep Delaunay faces. A Delaunay triangle contains at most one matching
edge.

## 73.3 Matched two-well theorem

From (72.12)--(72.14),

```math
E_{\rm deep}
<
\frac{a_0}{2}\bigl((24+\pi)D+18\bigr).
\tag{73.7}
```

Therefore, for every $`\eta>0`$, fewer than

```math
\boxed{
\frac{a_0\bigl((24+\pi)D+18\bigr)}{2\eta}
}
\tag{73.8}
```

matching edges are incident to a Delaunay face whose area excess above
$`\sqrt3/4`$ exceeds $`\eta`$.

> **Theorem 73.2 (matched two-well structure).**
> If $`\rho/D\to\infty`$, choose
> 

```math
> \eta=\sqrt{\frac D\rho}.
> \tag{73.9}
> 
```
> Then
> 

```math
> \boxed{
> \frac{\rho}{24}-o(\rho)
> }
> \tag{73.10}
> 
```
> pairwise vertex-disjoint strong Delaunay edges have length $`1+o(1)`$, and both
> incident Delaunay triangles have side triples at distance $`o(1)`$ from
> 

```math
> \boxed{
> \mathcal E
> :=
> \bigl\{\{1,1,1\},\ \{1,1,\sqrt3\}\bigr\}.
> }
> \tag{73.11}
> 
```

### Proof of the stability conclusion

The admissible side-length triples for deep Delaunay faces lie in a compact set:
all sides are in $`[1,2]`$, the triangle inequalities hold, and the circumradius is
at most $`1`$. By Theorem 72.2, area excess tends to zero only at the equality set
(72.6). Compactness gives the stated two-well stability. $`\square`$

### Essential caveat: both wells survive asymptotically

Triangle-freeness forbids the exact $`\{1,1,1\}`$ unit triangle but does **not** remove
that well from an asymptotic argument. An equilateral triangle of side
$`1+\varepsilon`$ has no unit edge and has circumradius at most $`1`$ for small
$`\varepsilon>0`$, while

```math
\operatorname{area}(T_\varepsilon)-\frac{\sqrt3}{4}
-
\frac{\sqrt3}{6}\sum_v\mu_{T_\varepsilon}(v)
=
\frac{\sqrt3}{4}\varepsilon^2
\to0.
\tag{73.12}
```

Therefore every “low excess implies only the $`120^\circ`$ wedge” assertion is false.
The canonical equality regime is genuinely two-well: near-equilateral and
near-$`120^\circ`$.

Equivalently, for every fixed $`\varepsilon_0>0`$, compactness supplies
$`\kappa(\varepsilon_0)>0`$ such that any admissible deep Delaunay face whose side
triple stays at least $`\varepsilon_0`$ from both wells has area excess at least
$`\kappa(\varepsilon_0)`$. Hence only
$`O(D/\kappa(\varepsilon_0))`$ such exceptional faces can occur.

---

# 74. Exact Hall--Kőnig scaffold obstruction

The matched Delaunay geometry of Section 73 lives in the original saturated minimizer
$`A`$. The scaffold of Section 71 lives around the independently chosen optimum
$`X_m`$. They are not co-embedded. This section records what can nevertheless be
said exactly inside the scaffold itself.

Assume $`t>1`$ and put

```math
L:=\operatorname{int}(K_m+t\mathbb B).
\tag{74.1}
```

Choose the same translated unit triangular lattice used for the safe-collar estimate,
and let

```math
Y:=(\Lambda+v)\cap L.
\tag{74.2}
```

Construct a bipartite conflict graph $`G`$ with parts $`X_m`$ and $`Y`$, joining
$`x\in X_m`$ to $`y\in Y`$ exactly when

```math
|x-y|<1.
\tag{74.3}
```

Let $`\nu`$ be its maximum matching size.

> **Theorem 74.1 (exact Hall--Kőnig conflict inequality).**
> Every surviving triangle-free global minimizer satisfies
> 

```math
> \boxed{
> m+|Y|-\nu\le N-1.
> }
> \tag{74.4}
> 
```
> Equivalently, for every $`S\subseteq Y`$,
> 

```math
> \boxed{
> |S|-|N_G(S)|\le\rho-1.
> }
> \tag{74.5}
> 
```

### Proof

Both $`X_m`$ and $`Y`$ are internally unit-separated. Hence a subset of
$`X_m\cup Y`$ is unit-separated exactly when it is an independent set of the
bipartite conflict graph. Kőnig's theorem gives

```math
\alpha(G)
=|X_m|+|Y|-\tau(G)
=m+|Y|-\nu.
\tag{74.6}
```

Every independent set lies in the open body $`L`$ and therefore has diameter
strictly below $`D`$. Since an $`N`$-point unit-separated subset of diameter below
$`D=D(N)`$ is impossible, $`\alpha(G)\le N-1`$, proving (74.4).
The standard deficiency form of Hall--Kőnig gives (74.5). $`\square`$

## 74.1 Safe collar plus inner-band near-perfect conflict matching

Let

```math
Y_0:=Y\cap\Omega,
\qquad
k:=|Y_0|,
\qquad
Y_{\rm in}:=Y\setminus Y_0.
\tag{74.7}
```

By construction,

```math
N_G(Y_0)=\varnothing.
\tag{74.8}
```

For every $`Q\subseteq Y_{\rm in}`$, apply (74.5) to $`S=Y_0\cup Q`$. Then

```math
k+|Q|-|N_G(Q)|\le\rho-1,
```

so

```math
\boxed{
|Q|-|N_G(Q)|
\le
\rho-k-1
=j-1.
}
\tag{74.9}
```

Hall's deficiency theorem therefore yields:

> **Corollary 74.2 (inner-band near-perfect conflict matching).**
> There is a matching from $`Y_{\rm in}`$ into $`X_m`$ that leaves at most
> 

```math
> \boxed{
> j-1=\rho-k-1
> <
> C_{\rm col}D-\frac{2\pi}{\sqrt3}-1
> }
> \tag{74.10}
> 
```
> inner-band lattice sites unmatched.

This matching is a matching of **conflicts**, not a placement of missing points. It
states that a surviving counterexample must arrange for almost every inner-band
lattice site to be blocked by a distinct point of the smaller optimum.

## 74.2 Exact Hall-surplus contradiction target

The preceding theorem identifies an exact finite contradiction criterion.

> **Target 74.A (inner-band Hall surplus).**
> Produce some $`Q\subseteq Y_{\rm in}`$ satisfying
> 

```math
> \boxed{
> |Q|-|N_G(Q)|\ge\rho-k=j.
> }
> \tag{74.11}
> 
```

Then $`Y_0\cup Q`$ has deficiency at least $`\rho`$, so (74.5) fails. Equivalently,
the conflict graph contains an independent set of at least $`N`$ vertices, yielding an
$`N`$-point unit-separated subset of $`L`$ of diameter strictly below $`D`$.

Thus Target A can now be closed either by constructing the missing $`j`$ sites
directly or by forcing the one-integer Hall surplus (74.11).

---

# 75. Authoritative v1.3 Target A frontier

The forest, exact-bar, triangle-wall, and abstract-rattler stages are no longer the
current obstruction. In a super-boundary survivor $`\rho/D\to\infty`$, the following
facts hold simultaneously:

1. a compatible strict sub-$`D`$ scaffold already contains
   $`N-O(D)`$ points;
2. the exact remaining demand is
   ```math
   1\le j=\rho-k
   <C_{\rm col}D-\frac{2\pi}{\sqrt3};
   \tag{75.1}
   
   ```
3. the original saturated minimizer satisfies
   ```math
   \sum_{p\in A}\delta(p)=O(D);
   \tag{75.2}
   
   ```
4. it carries
   ```math
   \frac{\rho}{24}-o(\rho)
   \tag{75.3}
   
   ```
   disjoint strong-Delaunay near-unit edges with two-well neighborhoods; and
5. the independently constructed scaffold conflict graph has an inner-band matching
   missing only at most $`j-1=O(D)`$ lattice sites.

Since $`|M|=\rho/24-o(\rho)`$ and $`j=O(D)`$, every super-boundary sequence with
$`j>0`$ satisfies the divergent supply-to-demand ratio

```math
\boxed{
\frac{|M|}{j}\longrightarrow\infty.
}
\tag{75.4}
```

The issue is therefore not a shortage of local structures. It is the absence of an
exact theorem transporting the enormous two-well supply in the original minimizer to
capacity in the independently positioned scaffold.

## 75.1 Exact remaining theorem

> **Target A v1.3 (two-well configuration-transfer / inner-band Hall-rigidity
> theorem).**
> In the simultaneous setting of Sections 71--74, prove that a super-boundary
> survivor cannot satisfy both
> 

```math
> |M|=\frac{\rho}{24}-o(\rho)
> \tag{75.5}
> 
```
> with two-well Delaunay neighborhoods in the original saturated minimizer and the
> inner-band conflict deficiency bound
> 

```math
> |Q|-|N_G(Q)|\le j-1
> \quad\text{for all }Q\subseteq Y_{\rm in}
> \tag{75.6}
> 
```
> in the independently constructed scaffold.
>
> It is enough to force one of:
>
> 1. a subset $`Q\subseteq Y_{\rm in}`$ with Hall surplus (74.11);
> 2. $`j`$ genuine pairwise compatible cavities in $`L`$, producing an $`N`$-point
>    strict sub-$`D`$ configuration;
> 3. a macroscopic near-equilateral phase whose interface/defect cost exceeds the
>    global $`O(D)`$ Delaunay-excess budget;
> 4. a macroscopic near-$`120^\circ`$ wedge-chain system whose ordered geometry forces
>    the required scaffold capacity; or
> 5. a mixed two-well interface carrying a positive finite charge per independent
>    obstruction, again exceeding the $`O(D)`$ budget.

The natural combinatorial object is the collection of alternating components of the
near-perfect conflict matching from Corollary 74.2. The natural geometric objects are
the matched two-well Gabriel neighborhoods from Theorem 73.2. A closing proof must
build an invariant or capacity certificate that survives the fact that these live in
different coordinate configurations.

### What is explicitly *not* enough

- using the original rattler Voronoi cells directly as scaffold cavities;
- assuming deletion optimality;
- assuming a uniform rattler clearance;
- discarding the near-equilateral well because the exact unit triangle is forbidden;
- counting candidate cavities without proving simultaneous realizability;
- returning to generic one-ray triangle-wall events or raw wall-normal rank.

---

# 76. Authoritative v1.3 Target B frontier

No new Target B rank theorem was obtained in the v1.3 Target A continuation. The
corrected v1.2 component bookkeeping remains authoritative.

Let $`\mathscr S_\alpha`$ be the component-rotation row span and

```math
\boxed{
r_\alpha=\dim\mathscr S_\alpha\le c(\Theta)-1.
}
\tag{76.1}
```

Let $`\overline{\mathcal B}_\xi`$ be the induced blocker family after quotienting
$`\mathscr S_\alpha`$. Then

```math
\operatorname{rank}\mathcal B
\le
r_\alpha+
\operatorname{rank}\overline{\mathcal B}_\xi.
\tag{76.2}
```

The exact sufficient residual theorem remains

```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le
T-q-r_\alpha.
}
\tag{76.3}
```

The stronger component-count-only sufficient form is

```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le
T-q-c(\Theta)+1.
}
\tag{76.4}
```

Either gives

```math
\operatorname{rank}\mathcal B+I+r\le T-q,
\tag{76.5}
```

contradicting the established lower bound

```math
\boxed{
\operatorname{rank}\mathcal B+I+r\ge T-q+1.
}
\tag{76.6}
```

The proof must remain componentwise:

1. $`s_C=2`$: use both vector-closure equations and the internal turn quotient;
2. cyclic $`s_C=1`$: use the exact two-family ordering and Ferrers staircase theorem;
3. one-direction tree components: no scalar cycle obstruction;
4. common component rotations: reserve exactly the cost $`r_\alpha`$, neither dropping
   nor double-counting it.

The two-family numerical endpoint remains

```math
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2,
\tag{76.7}
```

with gap

```math
\boxed{0.0124073626\ldots D^2.}
\tag{76.8}
```

After the pure inequality, the proof must still pass through nonquadrilateral faces,
holes, multiple components, pinches, and outside vertices with every transfer rank
charged to the exact topology-corrected shell residual. An uncontrolled $`O(D)`$ loss
is fatal.

---

# 77. Version 1.3.0 exact status

**LEVEL I STATUS: STILL OPEN.**

Version 1.3.0 makes a substantial Target A advance and leaves Target B unchanged at
its corrected v1.2 frontier.

## Target A — exact finite conflict obstruction

A super-boundary hybrid survivor can now be normalized to a saturated triangle-free
global minimizer with $`\rho=\omega(D)`$ genuine strict rattlers. It then forces all
of the following simultaneously:

```math
\boxed{
\begin{array}{c}
\text{a compatible strict sub-}D\text{ scaffold with only }O(D)\text{ missing sites},\\[1mm]
\displaystyle \sum_{p\in A}\delta(p)=O(D),\\[2mm]
\displaystyle \rho/24-o(\rho)\text{ disjoint near-unit strong-Delaunay edges},\\[1mm]
\text{two-well local geometry near }\{1,1,1\}\text{ or }\{1,1,\sqrt3\},\\[1mm]
\text{and an inner-band scaffold conflict graph of deficiency at most }j-1=O(D).
\end{array}
}
\tag{77.1}
```

The exact contradiction target is now the one-integer Hall surplus

```math
\boxed{
\exists Q\subseteq Y_{\rm in}:
|Q|-|N_G(Q)|\ge j.
}
\tag{77.2}
```

or an equivalent explicit construction of the $`j`$ missing scaffold sites.

The remaining conceptual gap is **configuration transfer**. The original two-well
Delaunay matching and the smaller-optimum scaffold are logically simultaneous but
geometrically independent. No theorem currently transfers the former into actual
cavities of the latter.

## Target B — exact one-integer internal rank gap

The terminal-component decomposition, vector closure, two-direction equality
classification, and stochastic-width component-rotation formula remain trusted. The
component-rotation cost is explicitly

```math
r_\alpha\le c(\Theta)-1,
```

and the exact unproved internal theorem is (76.3), followed by topology-corrected
transport.

## Unified endgame

A Level I proof now requires one theorem on each side:

1. **Target A:** two-well configuration transfer / inner-band Hall rigidity;
2. **Target B:** internal terminal-component blocker/coforest rank with exact topology
   correction.

Both statements are global finite-capacity theorems. Neither is a missing generic
rigidity count. No infinite family of triangle-free global minimizers is known, so no
disproof is available either.

---

# 78. Current version history and provenance

- **v1.0.0 (2026-08-26):** canonical synthesis and second-pass audit through the
  translated-lattice, phase-atomic, first-order cusp, backward-flip, tangent-quartic,
  support-turning, and hybrid-forest reductions.
- **v1.1.0 (2026-08-26):** minimal-face harmonic--Dirichlet, peripheral-dual,
  terminal direction-network/turn, boundary-velocity, exact plateau, and optimal-flat
  results; rejection of the cycle-lift shortcut; corrected facial peeling.
- **v1.2.0 (2026-08-26):** rooted-forest self-stress, root-skeleton exactification,
  affine factor exclusion, forest rattlerization, saturation, strict replacement and
  collar growth, terminal-component Minkowski splitting, componentwise closure, and
  stochastic-width component-rotation bookkeeping.
- **v1.3.0 (2026-08-26):** unconditional compatible-collar dichotomy, sharp safe-collar
  population, deep Voronoi containment, global clearance budget, degree-six
  near-neighbor matching, strong Gabriel/Delaunay promotion, matched two-well
  structure, exact Hall--Kőnig scaffold conflict theorem, and inner-band near-perfect
  conflict matching. Target A is reduced to two-well configuration transfer / Hall
  rigidity. Target B remains the corrected v1.2 internal blocker/coforest problem.

The only supplied external literature remains:

1. `mp05-2-261-269.pdf`;
2. `1951-03.pdf`;
3. `1-s2.0-S0097316598928898-main.pdf`;
4. `s00454-002-0747-6.pdf`;
5. `1204.4403v1.pdf`;
6. `463.pdf`;
7. `10.1007_PL00009374.pdf`.

No internet source is part of this theorem-state file.

---

# 79. Exact scaffold monomer--dimer structure

This section supersedes the v1.3 claim that configuration transfer is the only
available Target A route.  The original cross-configuration two-well theorem remains
valid, but the conflict scaffold itself has an exact two-well cell structure.

Assume the second branch of Theorem 71.1. Thus

```math
t>1,
\qquad
L=\operatorname{int}(K_m+t\mathbb B),
\qquad
\Omega=L\setminus(K_m+\mathbb B).
\tag{79.1}
```

Choose a triangular-lattice translate $`\Lambda_v=\Lambda+v`$ from the positive-measure
set realizing the strict safe-collar population bound and outside the measure-zero
exceptional set on which a lattice point lies on either parallel-body boundary or a
cross-distance from $`X_m`$ equals $`0`$ or $`1`$. Put

```math
Y=\Lambda_v\cap L,
\qquad
Y_0=Y\cap\Omega,
\qquad
Y_{\rm in}=Y\setminus Y_0.
\tag{79.2}
```

Then

```math
\boxed{
Y_{\rm in}=\Lambda_v\cap\operatorname{int}(K_m+\mathbb B).
}
\tag{79.3}
```

Let $`G`$ be the bipartite conflict graph on $`X_m\sqcup Y_{\rm in}`$, with

```math
x\sim y
\quad\Longleftrightarrow\quad
|x-y|<1.
\tag{79.4}
```

For $`x\in X_m`$, define the full lattice conflict neighborhood and its cell by

```math
N_\Lambda(x)=\{y\in\Lambda_v:|x-y|<1\},
\qquad
C_x=\operatorname{conv}N_\Lambda(x).
\tag{79.5}
```

Because $`x\in K_m`$ and $`t>1`$, every $`y\in N_\Lambda(x)`$ lies in
$`\operatorname{int}(K_m+\mathbb B)\subset L`$. Hence

```math
\boxed{N_G(x)=N_\Lambda(x).}
\tag{79.6}
```

Thus there is no boundary truncation of any left conflict neighborhood.

## 79.1 Full-neighborhood classification

> **Theorem 79.1 (exact triangular-lattice blocker classification).**
> For every $`x\in X_m`$,
> 

```math
> \boxed{|N_G(x)|\in\{3,4\}.}
> \tag{79.7}
> 
```
> If $`|N_G(x)|=3`$, then $`C_x`$ is an elementary unit equilateral triangle.
> If $`|N_G(x)|=4`$, then $`C_x`$ is a unit lozenge.

### Proof

Write

```math
\Lambda=\mathbb Ze_1+\mathbb Ze_2,
\qquad
|e_1|=|e_2|=1,
\qquad
e_1\cdot e_2=\frac12.
\tag{79.8}
```

For a lattice vector $`ae_1+be_2`$,

```math
Q(a,b)=|ae_1+be_2|^2=a^2+ab+b^2.
\tag{79.9}
```

If $`y,y'\in N_\Lambda(x)`$, then

```math
|y-y'|
<|y-x|+|x-y'|<2.
\tag{79.10}
```

Thus every nonzero difference inside one conflict neighborhood has squared norm
$`1`$ or $`3`$. Two lattice sites in the same class modulo $`2\Lambda`$ have
squared distance at least $`4`$. There are four parity classes, so

```math
|N_\Lambda(x)|\le4.
\tag{79.11}
```

Every point of the plane belongs to a closed elementary unit lattice triangle. Its
three vertices are all at distance at most one. Genericity excludes equality and
lattice coincidence for every $`x\in X_m`$, so those three distances are strictly
below one. Hence

```math
|N_\Lambda(x)|\ge3.
\tag{79.12}
```

The possible side-square multisets for three triangular-lattice points with all
pairwise distances below two are

```math
\{1,1,1\},
\qquad
\{1,1,3\},
\qquad
\{3,3,3\}.
\tag{79.13}
```

The last is an equilateral triangle of side $`\sqrt3`$, whose minimum enclosing
radius is one, so it cannot lie in an open unit disk.

A $`\{1,1,3\}`$ triple consists of three vertices of a unit lozenge. Write the
lozenge as

```math
0,u,v,u+v,
\qquad
|u|=|v|=1,
\qquad
u\cdot v=\frac12.
\tag{79.14}
```

If $`p`$ is within unit distance of $`0,u,u+v`$, then

```math
|p-v|^2+|p-u|^2
=|p|^2+|p-u-v|^2-1<1.
\tag{79.15}
```

Thus $`|p-v|<1`$, so the fourth lozenge vertex is also a conflict. Therefore a
**complete** degree-three neighborhood cannot have type $`\{1,1,3\}`$, and must be
an elementary unit triangle.

A finite check of four-cliques in the distance-$`<2`$ triangular-lattice graph gives
only two types: the four vertices of a unit lozenge, or one lattice point together
with three alternating unit neighbors. In the second type the latter three vertices
form an equilateral triangle of side $`\sqrt3`$, again with minimum enclosing radius
one. Hence the second type cannot fit in an open unit disk. Every degree-four
neighborhood is therefore a unit lozenge. $`\square`$

## 79.2 Interior location and cell disjointness

> **Theorem 79.2 (exact monomer--dimer packing).**
> For every $`x\in X_m`$,
> 

```math
> \boxed{x\in\operatorname{int}C_x.}
> \tag{79.16}
> 
```
> If $`x\ne x'`$, then
> 

```math
> \boxed{
> \operatorname{int}C_x\cap\operatorname{int}C_{x'}=\varnothing.
> }
> \tag{79.17}
> 
```
> Consequently the cells $`C_x`$ form an exact monomer--dimer packing on the
> honeycomb dual of the elementary triangular tiling: a degree-three blocker occupies
> one elementary triangle and a degree-four blocker occupies two adjacent elementary
> triangles.

### Proof

Take a boundary edge of $`C_x`$. On the cell side lies an elementary lattice triangle
whose third vertex $`w`$ belongs to $`N_\Lambda(x)`$. Let $`w'`$ be the reflected
lattice vertex across that boundary edge. If $`x`$ lay on or beyond the edge, then

```math
|x-w'|\le|x-w|<1,
\tag{79.18}
```

contradicting the completeness of the neighborhood classification. Hence
$`x\in\operatorname{int}C_x`$.

Each cell is the union of one or two elementary lattice triangles. If two cell
interiors overlapped, they would share an elementary triangle $`\Delta`$. The two
associated points of $`X_m`$ would both lie in the intersection of the three open
unit disks centered at the vertices of $`\Delta`$, the interior of the unit Reuleaux
triangle. That set has diameter one, and two of its interior points have distance
strictly below one. This contradicts the unit separation of $`X_m`$. $`\square`$

## 79.3 Radial planarity and right degree

Join every $`x\in X_m`$ by straight segments to the vertices of $`C_x`$. Since each
radial edge stays in its own convex cell and cell interiors are disjoint, distinct
radial edges do not cross. Genericity excludes coincident cross-vertices and radial
edge degeneracies.

> **Corollary 79.3.** The radial drawing is a simple plane drawing of $`G`$.
> Every lattice-side vertex has degree at most five.

For the degree bound, if six points of $`X_m`$ lay in the open unit disk centered at
a lattice vertex, two consecutive polar angles would differ by at most $`\pi/3`$.
For radii $`r,s<1`$,

```math
|p-q|^2\le r^2+s^2-rs<1,
\tag{79.19}
```

contradicting unit separation.

The two exact scaffold cell motifs already contain both equality wells from the v1.3
Delaunay analysis. A monomer has side multiset $`\{1,1,1\}`$. A three-vertex subset
of a lozenge has side multiset $`\{1,1,1\}`$ or $`\{1,1,\sqrt3\}`$. This is a
new co-embedded occurrence of the wells; it is not a transport of the original
saturated minimizer's Delaunay faces.

---

# 80. Exact Hall charge, leafless reduction, and face-shell identities

Let $`m_3,m_4`$ be the numbers of monomer and dimer cells. Then

```math
m_3+m_4=m.
\tag{80.1}
```

Let

- $`\gamma`$ be the number of connected components of the full radial graph $`G`$,
  including isolated lattice-side vertices;
- $`s`$ be the number of unit lattice edges shared by two distinct cells;
- $`g`$ be the number of bounded complementary gap components of the cell union; and
- $`\delta=|Y_{\rm in}|-m`$.

## 80.1 Full-complex Euler identity

> **Theorem 80.1.**
> 

```math
> \boxed{\mu(G)=s+g}
> \tag{80.2}
> 
```
> and
> 

```math
> \boxed{
> \delta=m_3+2m_4+\gamma-s-g.
> }
> \tag{80.3}
> 
```

### Proof

Add all cell-boundary lattice edges to the radial graph. Within each monomer or dimer
this produces the fan decomposition from its interior point. Deleting the cell
boundary edges has two topological effects. A boundary edge shared by two cells
produces one quadrilateral radial face, and each bounded complementary gap component
produces one radial face after its adjacent fan triangles are merged into the gap.
Thus the bounded faces of the plane graph are in bijection with the $`s`$ shared
edges and the $`g`$ bounded gaps. For a plane graph with $`\gamma`$ components the
number of bounded faces equals its cyclomatic number, proving (80.2).

Also

```math
|E(G)|=3m_3+4m_4,
\qquad
|V(G)|=m+|Y_{\rm in}|=2m+\delta.
\tag{80.4}
```

Hence

```math
\mu(G)=|E|-|V|+\gamma
=m_3+2m_4-\delta+\gamma.
\tag{80.5}
```

Combine with (80.2). $`\square`$

The canonical survivor Hall inequality applied to $`Q=Y_{\rm in}`$ gives

```math
\delta\le j-1.
\tag{80.6}
```

Therefore

```math
\boxed{
 s+g\ge m_3+2m_4+\gamma-j+1.
}
\tag{80.7}
```

Using the v1.3 collar bound

```math
j<C_{\rm col}D-\frac{2\pi}{\sqrt3},
\qquad
C_{\rm col}=\pi\left(\frac12+\frac2{\sqrt3}\right),
\tag{80.8}
```

we obtain the strict quantitative form

```math
\boxed{
 s+g>
 m_3+2m_4+\gamma-C_{\rm col}D+\frac{2\pi}{\sqrt3}+1.
}
\tag{80.9}
```

Thus all but $`O(D)`$ of the elementary-triangle cell mass must be canceled by
shared-edge or bounded-gap faces in every surviving super-boundary scaffold.

## 80.2 Arbitrary Hall sets and the leafless formula

For $`Q\subseteq Y_{\rm in}`$, let

```math
H_Q=G[Q\sqcup N(Q)].
\tag{80.10}
```

Write $`\gamma_Q`$ and $`\mu_Q`$ for its component and cyclomatic numbers, and let
$`b_d(Q)`$ count left vertices of degree $`d`$ in $`H_Q`$.

> **Theorem 80.2 (exact Hall charge).** For every $`Q\subseteq Y_{\rm in}`$,
> 

```math
> \boxed{
> |Q|-|N(Q)|
> =\gamma_Q-\mu_Q-b_1(Q)+b_3(Q)+2b_4(Q).
> }
> \tag{80.11}
> 
```

### Proof

Since

```math
\mu_Q=|E(H_Q)|-|Q|-|N(Q)|+\gamma_Q
\tag{80.12}
```

and

```math
|E(H_Q)|=\sum_{x\in N(Q)}\deg_{H_Q}(x),
\tag{80.13}
```

we have

```math
|Q|-|N(Q)|
=\gamma_Q-\mu_Q
+\sum_{x\in N(Q)}(\deg_{H_Q}(x)-2).
\tag{80.14}
```

Every left degree is between one and four, giving (80.11). $`\square`$

Define the Hall deficiency

```math
h(G)=\max_{Q\subseteq Y_{\rm in}}\bigl(|Q|-|N(Q)|\bigr).
\tag{80.15}
```

> **Theorem 80.3 (leafless maximizing Hall set).** A maximizing $`Q`$ can be chosen
> with $`b_1(Q)=0`$. Consequently
> 

```math
> \boxed{
> h(G)=
> \max_{\substack{Q\subseteq Y_{\rm in}\\ b_1(Q)=0}}
> \bigl(\gamma_Q-\mu_Q+b_3(Q)+2b_4(Q)\bigr).
> }
> \tag{80.16}
> 
```

### Proof

Choose a maximum-deficiency $`Q`$ of minimum cardinality. Suppose a left vertex has
degree one in $`H_Q`$, with unique neighbor $`y\in Q`$. Let $`r\ge1`$ be the number
of left vertices whose only $`Q`$-neighbor is $`y`$. Then

```math
(|Q|-1)-(|N(Q)|-r)
=(|Q|-|N(Q)|)+(r-1).
\tag{80.17}
```

Deleting $`y`$ therefore does not reduce deficiency. It cannot increase deficiency
past the global maximum, so it gives a smaller maximizing set, contradiction.
$`\square`$

The positive local Hall charges in (80.11) and (80.16) are exactly the scaffold's two
crystalline wells. The negative term is cycle rank. Target A has therefore become an
exact branch-versus-cycle problem in one common geometry.

## 80.3 Exact face-shell refinement

Let $`b_\infty`$ be the length, with multiplicity, of the unbounded **radial-graph**
facial boundary walk. Thus $`b_\infty/2`$ is the number, with multiplicity, of
exposed lattice cell edges on the unbounded side. For the bounded gaps, let $`b_i`$
be the number of lattice cell-edge incidences on the boundary of gap $`i`$, and put

```math
\eta=\sum_i(b_i-3)\ge0.
\tag{80.18}
```

> **Theorem 80.4 (face-shell identities).**
> 

```math
> \boxed{
> g=m_3+2\delta-2\gamma-\eta-\frac{b_\infty}{2},
> }
> \tag{80.19}
> 
```
> 

```math
> \boxed{
> s=2m_4-3\delta+3\gamma+\eta+\frac{b_\infty}{2}.
> }
> \tag{80.20}
> 
```
> In particular,
> 

```math
> \boxed{
> s\ge2m_4-3j+3+3\gamma.
> }
> \tag{80.21}
> 
```

### Proof

The total number of cell-boundary edge incidences is

```math
3m_3+4m_4.
\tag{80.22}
```

Every shared edge consumes two incidences. The remaining exposed lattice cell edges
lie either on a bounded gap or on the unbounded side. Hence

```math
3m_3+4m_4-2s
=3g+\eta+\frac{b_\infty}{2}.
\tag{80.23}
```

Combine (80.23) with (80.3) and solve for $`g`$ and $`s`$, obtaining (80.19) and
(80.20). Finally use $`\delta\le j-1`$ and the nonnegativity of $`\eta`$ and
$`b_\infty`$. $`\square`$

Equation (80.21) is the exact dimer endpoint: if $`m_4\gg j`$, nearly the maximum
possible dimer-side mass must be absorbed into shared-edge quadrilateral faces.
Equation (80.19) is the monomer endpoint: absent large outer boundary or
nontriangular gap excess, there is nearly one elementary triangular gap per monomer.

---

# 81. Authoritative v1.4 Target A frontier

The v1.3 configuration-transfer obstruction remains logically correct but is no
longer the unique Target A route. The new scaffold-internal theorem removes the need
to transport the original minimizer's Delaunay neighborhoods if one can control cycle
cancellation directly.

Recall

```math
N=m+\rho=m+k+j,
\qquad
1\le j=\rho-k
<C_{\rm col}D-\frac{2\pi}{\sqrt3}.
\tag{81.1}
```

By Kőnig's theorem, the maximum independent set in the conflict graph on
$`X_m\sqcup Y_{\rm in}`$ has size

```math
m+h(G).
\tag{81.2}
```

Every point of $`Y_0`$ can be added because $`Y_0`$ has no conflicts with $`X_m`$,
and lattice sites are mutually unit-separated. Thus the maximum compatible subset of
$`X_m\cup Y`$ has size

```math
m+k+h(G).
\tag{81.3}
```

Since $`N=m+k+j`$, Target A closes exactly when

```math
\boxed{h(G)\ge j.}
\tag{81.4}
```

Using Theorem 80.3, the exact remaining statement is:

> **Target A v1.4 (monomer--dimer cycle-cut rigidity).**
> For every scaffold arising from a super-boundary triangle-free global minimizer,
> prove
> 

```math
> \boxed{
> \max_{\substack{Q\subseteq Y_{\rm in}\\b_1(Q)=0}}
> \bigl(\gamma_Q-\mu_Q+b_3(Q)+2b_4(Q)\bigr)
> \ge j.
> }
> \tag{81.5}
> 
```

If (81.5) holds, $`X_m\cup Y`$ contains $`N`$ mutually unit-separated points in the
open body $`L`$, while

```math
\operatorname{diam}(L)<D,
\tag{81.6}
```

contradicting $`D=D(N)`$.

A hypothetical survivor must therefore arrange **every** leafless Hall set so that

```math
\mu_Q
\ge
\gamma_Q+b_3(Q)+2b_4(Q)-j+1.
\tag{81.7}
```

This is the exact cycle-cancellation obstruction.

## 81.1 Local zero-charge regressions

Planarity and motif counting alone cannot prove (81.5). There are exact local
crystalline cancellation models:

1. a generic triangular-lattice shift to centers of one orientation of elementary
   triangles yields a monomer phase in which positive branch charge is canceled by
   elementary triangular gap faces;
2. another generic shift yields a lozenge/dimer phase in which positive branch charge
   is canceled by a quadrangulation of shared-edge faces.

These are not known large global diameter extremizers, but their local conflict
combinatorics survive boundary perturbation. Any proof of (81.5) must therefore use
the global-optimality origin of $`X_m`$, the collar parameter $`j`$, or a genuinely
global planar-dual invariant.

## 81.2 Next viable route

A viable next program is the Dulmage--Mendelsohn decomposition of a
maximum-deficiency minimum-cardinality Hall set, coupled to the planar dual of the
monomer--dimer complex.

In a dimer-rich domain, (80.20)--(80.21) force near-maximal shared-edge cancellation.
A new **type-resolved dual-strip theorem** would be needed to cut such a domain into
ordered lozenge strips after paying only the exact Hall defect. Only after proving
that bridge may one invoke the already-audited two-family Ferrers/Cartesian endpoint

```math
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2.
\tag{81.8}
```

In a monomer-rich domain, (80.19) forces almost every bounded face to be an elementary
triangular gap unless outer-boundary or nontriangular-gap excess is large. The needed
new theorem is an exact phase-rigidity/dual-cut statement: a Hall-saturating monomer
phase must either create an augmenting dual cut, force a globally coherent
translated-lattice extremizer, or produce a certified diameter-decreasing
deformation.

Mixed domains must be measured by **absolute** dual-contour/interface charge. Signed
global Euler charge can cancel and is not enough.

The following are research routes, not canonical consequences:

- automatic contraction to a width-one annulus;
- an exact gammoid representation after plateau terminalization;
- automatic import of the Target B Ferrers theorem into scaffold lozenge strips; or
- a Schürmann deformation from a monomer phase without a proved global hypothesis.

The old v1.3 cross-configuration two-well transfer theorem remains an alternate
closure route, but the scaffold-internal cycle-cut theorem (81.5) is now the preferred
Target A endpoint.

---

# 82. Strict stochasticity and atomic terminal components

Return to the pure simply connected strict-rhombic Target B survivor and the terminal
component decomposition of Sections 65--67. Let

```math
c=c(\Theta).
\tag{82.1}
```

For an active diameter bar $`h`$, recall

```math
r_h=De_h,
\qquad
r_h=\sum_Cr_{h,C},
\tag{82.2}
```

and

```math
a_{hC}
=\frac{w_{K_C}(e_h)}D,
\qquad
\sum_Ca_{hC}=1.
\tag{82.3}
```

## 82.1 Strict positivity of every component width

> **Theorem 82.1 (strict stochasticity).** For every active diameter bar $`h`$ and
> every terminal component $`C`$,
> 

```math
> \boxed{a_{hC}>0.}
> \tag{82.4}
> 
```

### Proof

An active diameter direction has a unique support maximizer and a unique support
minimizer in $`K`$. Under the Minkowski decomposition

```math
K=\sum_CK_C,
\tag{82.5}
```

the support face in any direction is the Minkowski sum of the corresponding support
faces of the summands. A singleton support face of $`K`$ therefore forces every
summand support face in that direction to be a singleton; the same holds in the
opposite direction.

Every terminal component contains a train edge and hence contributes a nonzero hull
edge vector, so $`K_C`$ is not a singleton. If
$`w_{K_C}(e_h)=0`$, all points of $`K_C`$ have the same $`e_h`$-coordinate and the
support face in direction $`e_h`$ is the whole nontrivial summand $`K_C`$,
contradicting singleton support. Thus the width is strictly positive. $`\square`$

Hence the stochastic vectors

```math
a_h=(a_{hC})_C
\tag{82.6}
```

have **full support**, not merely nonnegative support.

## 82.2 Atomicity of the s_C=0 class

> **Theorem 82.2 (atomic one-direction component).** If $`s_C=0`$, then $`C`$ has
> exactly two terminal vertices and one train edge $`\tau`$. Its Minkowski summand is
> a unit segment parallel to $`u_\tau`$. For every active diameter bar $`h`$,
> 

```math
> \boxed{
> d_{h\tau}\ne0,
> \qquad
> \lambda_{h\tau}=d_{h\tau}\,r_h\cdot u_\tau
> =D|e_h\cdot u_\tau|>0.
> }
> \tag{82.7}
> 
```
> In particular, an $`s_C=0`$ component can never be the origin component of a
> strict-backward blocker row.

### Proof

By Theorem 66.2, $`C`$ is a tree and all its trains have one oriented unit direction
$`u`$. For $`j\in J_C`$, the vector
$`e_j=z_{j+1}-z_j`$ is a nonzero side between consecutive extreme hull vertices.
The incidence formula therefore gives

```math
e_j=k_ju,
\qquad
k_j\in\mathbb Z\setminus\{0\}.
\tag{82.8}
```

The sides $`e_j`$ occur in cyclic convex order. Since the $`z_j`$ are extreme
hull vertices, collinear boundary subdivisions have already been removed; a convex
hull has at most one side in the oriented direction $`u`$ and at most one in the
opposite direction $`-u`$. Component closure gives
$`\sum_{j\in J_C}e_j=0`$, so both orientations occur and $`|J_C|=2`$. Since
$`C`$ is a connected tree on two vertices, it has one train edge. Its incidence
relation gives the two summand edge vectors $`u`$ and $`-u`$, so $`K_C`$ is a unit
segment.

By Theorem 82.1 the width of this segment in every active diameter direction is
positive, so $`e_h\cdot u\ne0`$. Its support chord is

```math
r_{h,C}=\operatorname{sgn}(e_h\cdot u)u.
\tag{82.9}
```

The train decomposition of the diameter chord gives the same vector as
$`d_{h\tau}u`$; hence $`d_{h\tau}=\pm1`$ with the displayed sign and
$`\lambda_{h\tau}=D|e_h\cdot u|>0`$. $`\square`$

Thus every strict-backward origin lies in a component with

```math
\boxed{s_C>0.}
\tag{82.10}
```

This statement must not be strengthened to "cyclic" without a new theorem.

## 82.3 Atomic component collapses the nonzero minimal-face potential space

> **Corollary 82.3.** Suppose an $`s_C=0`$ component is present and the
> minimal-face equality kernel $`K`$ is nonzero. Then the selected active-bar
> potentials all coincide. In the notation of the harmonic--Dirichlet reduction,
> the terminal-potential count is therefore
> 

```math
> \boxed{r=1.}
> \tag{82.11}
> 
```

### Proof

Let $`\tau`$ be the unique train of the atomic component. By Theorem 82.2,
for every active diameter bar $`h`$,
$`d_{h\tau}=\pm1`$ and $`\lambda_{h\tau}>0`$. Hence $`\tau`$ is
visible to every bar selected in the minimal-face equality system. On that face the
equality relation is $`x_\tau=s_h`$ for every selected $`h`$. Thus all
selected bar potentials $`s_h`$ take the same value on the nonzero equality
kernel. The terminal-potential factorization from the harmonic--Dirichlet theorem
therefore has a single potential class, so $`r=1`$. $`\square`$

This corollary is only asserted in the nonzero minimal-face-kernel branch; it is not a
replacement for the separate $`K=0`$ convention.

---

# 83. Component-rotation variance and strict-backward origin rank

For every active diameter bar $`h`$ and component $`C`$, decompose its support chord
in the orthonormal frame $`(e_h,Je_h)`$:

```math
\boxed{
 r_{h,C}=D(a_{hC}e_h+b_{hC}Je_h).
}
\tag{83.1}
```

Since $`r_h=De_h=\sum_Cr_{h,C}`$,

```math
\boxed{
\sum_Ca_{hC}=1,
\qquad
\sum_Cb_{hC}=0,
\qquad
a_{hC}>0.
}
\tag{83.2}
```

Give every train in component $`C`$ a common angular motion $`t\alpha_C`$. The exact
train-coordinate realization theorem permits independent unit train-vector rotations,
so all rhombic unit contacts remain exact. Put

```math
r_h(t)=\sum_CR_{t\alpha_C}r_{h,C},
\qquad
f_h(t)=\frac12|r_h(t)|^2.
\tag{83.3}
```

## 83.1 Exact second variation

> **Theorem 83.1 (component-rotation variance formula).**
> 

```math
> \boxed{
> f_h'(0)=-D^2\sum_Cb_{hC}\alpha_C.
> }
> \tag{83.4}
> 
```
> If $`f_h'(0)=0`$, then
> 

```math
> \boxed{
> f_h''(0)
> =-D^2\left[
> \sum_Ca_{hC}\alpha_C^2
> -\left(\sum_Ca_{hC}\alpha_C\right)^2
> \right].
> }
> \tag{83.5}
> 
```
> Because every $`a_{hC}>0`$, equality in (83.5) holds if and only if all
> $`\alpha_C`$ are equal.

### Proof

Differentiate (83.3):

```math
r_h'(0)=\sum_C\alpha_CJr_{h,C}
=D\left[-\sum_Cb_{hC}\alpha_C\,e_h
+\sum_Ca_{hC}\alpha_C\,Je_h\right].
\tag{83.6}
```

Since $`r_h(0)=De_h`$, this gives (83.4). Also

```math
r_h''(0)=-\sum_C\alpha_C^2r_{h,C}.
\tag{83.7}
```

If (83.4) vanishes, then

```math
|r_h'(0)|^2
=D^2\left(\sum_Ca_{hC}\alpha_C\right)^2,
\tag{83.8}
```

while

```math
r_h(0)\cdot r_h''(0)
=-D^2\sum_Ca_{hC}\alpha_C^2.
\tag{83.9}
```

Use $`f_h''=|r_h'|^2+r_h\cdot r_h''`$. The bracket in (83.5) is the variance of
$`\alpha`$ under the full-support probability weights $`a_{hC}`$, so it vanishes
only on common rotation. $`\square`$

## 83.2 Positive spanning of the component-rotation quotient

Let

```math
V_\alpha=\mathbb R^c/\langle\mathbf1\rangle
\tag{83.10}
```

and define the active first-derivative covector

```math
L_h(\alpha)=-\sum_Cb_{hC}\alpha_C.
\tag{83.11}
```

> **Theorem 83.2 (positive spanning).** The active covectors $`L_h`$ positively span
> $`V_\alpha^*`$. Equivalently,
> 

```math
> \boxed{
> \{[\alpha]\in V_\alpha:L_h(\alpha)\le0\text{ for every active }h\}
> =\{0\}.
> }
> \tag{83.12}
> 
```
> Consequently their linear rank is exactly
> 

```math
> \boxed{c-1,}
> \tag{83.13}
> 
```
> and if $`c\ge2`$, at least $`c`$ nonzero active restrictions are required for
> positive spanning.

### Proof

Suppose $`[\alpha]\ne0`$ and $`L_h(\alpha)\le0`$ for every active $`h`$. If the
inequality is strict, (83.4) decreases that active squared diameter to first order for
small positive $`t`$. If equality holds, (83.5) is strictly negative because
$`[\alpha]\ne0`$ and every weight is positive. Thus every active diameter becomes
strictly shorter for small positive $`t`$.

The exact component-rotation path preserves all unit rhombic contacts. The realization
is strict, so every inactive lower-distance, upper-diameter, and rhombus-angle
inequality retains its slack for sufficiently small $`t`$. Hence the whole
configuration has diameter strictly below $`D`$, contradicting local, and therefore
global, diameter minimality. This proves (83.12).

The polar-cone theorem now says that the positive cone generated by the $`L_h`$ is all
of $`V_\alpha^*`$. Its span therefore has dimension $`c-1`$. A positive spanning set
of a vector space of dimension $`c-1\ge1`$ requires at least $`c`$ nonzero vectors.
$`\square`$

This is stronger than the v1.2 upper bound on component-rotation blocker rank: the
**active diameter derivatives** themselves are globally full rank on the quotient.
It does not, however, identify the internal $`\xi`$-blocker rank.

## 83.3 Rank consumed by distinct strict-backward origins

A strict-backward blocker row belonging to a train in component $`C`$, supported by
active bar $`h`$, restricts to common component rotations as

```math
\boxed{
 v_{h,C}=e_C^*-a_h,
 \qquad
 a_h=(a_{hC'})_{C'},
 \qquad
 a_{hC'}>0,
 \qquad
 \sum_{C'}a_{hC'}=1.
}
\tag{83.14}
```

Call $`C`$ a **strict-backward origin component** if at least one such row originates
in $`C`$. Let $`\mathcal O`$ be the set of distinct origins and

```math
k_{\rm org}=|\mathcal O|.
\tag{83.15}
```

> **Theorem 83.3 (full-support origin independence).** Choose one strict-backward row
> from each of $`k`$ distinct origin components.
>
> - If $`k<c`$, the selected component-rotation rows are linearly independent.
> - If $`k=c`$, their rank is exactly $`c-1`$.
>
> Therefore
> 

```math
> \boxed{
> r_\alpha\ge\min\{k_{\rm org},c-1\},
> }
> \tag{83.16}
> 
```
> 

```math
> \boxed{k_{\rm org}\le r_\alpha+1,}
> \tag{83.17}
> 
```
> and if $`r_\alpha<c-1`$, then
> 

```math
> \boxed{k_{\rm org}\le r_\alpha.}
> \tag{83.18}
> 
```

### Proof

Suppose rows from distinct origins $`C_i`$ satisfy

```math
\sum_{i=1}^kc_i(e_{C_i}^*-a_i)=0.
\tag{83.19}
```

Then

```math
\sum_ic_ie_{C_i}^*=\sum_ic_ia_i.
\tag{83.20}
```

The $`\ell^1`$-norm of the left side is $`\sum_i|c_i|`$, while

```math
\left\|\sum_ic_ia_i\right\|_1
\le\sum_i|c_i|\|a_i\|_1
=\sum_i|c_i|.
\tag{83.21}
```

Equality must hold. Since every coordinate of every $`a_i`$ is strictly positive,
equality in the coordinatewise triangle inequality forces all nonzero $`c_i`$ to
have the same sign.

If $`k<c`$, take a component coordinate not among the selected origins. The left side
of (83.20) is zero in that coordinate, whereas the right side is a same-sign sum of
strictly positive numbers unless every $`c_i=0`$. Thus the rows are independent.

If $`k=c`$, every proper subset is independent by the first case, while all rows
annihilate common rotation, so their rank is at most $`c-1`$. Hence it is exactly
$`c-1`$. Equations (83.16)--(83.18) follow. $`\square`$

Combining with Theorem 82.2 gives

```math
\boxed{
\mathcal O\subseteq\{C:s_C>0\}.
}
\tag{83.22}
```

No stronger inclusion is currently audited.

## 83.4 The s_C=1 tree correction

The statement

```math
\mathcal O\subseteq
\{\text{cyclic }s_C=1\text{ components}\}\cup\{s_C=2\text{ components}\}
\tag{83.23}
```

is **not proved** and must not be used. Theorem 66.2 classifies cyclic $`s_C=1`$
components but does not exclude $`s_C=1`$ trees.

An abstract consistent local model is a three-vertex path using two train directions
$`u,v`$ whose inherited convex-summand edge vectors are

```math
-u,
\qquad
u-v,
\qquad
v,
\tag{83.24}
```

which close to zero and can form a triangular Minkowski summand. Thus a tree can have
$`s_C=1`$. Any Target B coforest theorem must include this case explicitly rather
than assigning every strict-backward origin to a cyclic or two-dimensional component.

---

# 84. Authoritative v1.4 Target B frontier

The established lower-rank theorem remains

```math
\boxed{
\operatorname{rank}\mathcal B+I+r\ge T-q+1.
}
\tag{84.1}
```

The total desired pure upper bound remains

```math
\boxed{
\operatorname{rank}\mathcal B+I+r\le T-q.
}
\tag{84.2}
```

Let $`\mathscr S_\alpha`$ be the component-rotation restriction row span and

```math
r_\alpha=\dim\mathscr S_\alpha\le c(\Theta)-1.
\tag{84.3}
```

After quotienting it, let $`\overline{\mathcal B}_\xi`$ be the internal relative-angle
row family. Then

```math
\operatorname{rank}\mathcal B
\le
r_\alpha+
\operatorname{rank}\overline{\mathcal B}_\xi.
\tag{84.4}
```

The exact residual theorem is still

> **Target B v1.4 (internal coforest with origin budget).** Prove
> 

```math
> \boxed{
> \operatorname{rank}\overline{\mathcal B}_\xi+I+r
> \le T-q-r_\alpha.
> }
> \tag{84.5}
> 
```

The stronger component-count-only sufficient form remains

```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-c(\Theta)+1.
}
\tag{84.6}
```

The new information is that strict-backward origins themselves consume the reserved
rotation rank:

```math
\boxed{
 r_\alpha\ge\min\{k_{\rm org},c(\Theta)-1\}.
}
\tag{84.7}
```

Hence blocker origins cannot be distributed freely over many terminal components.
If the rotation span is not already full, each distinct origin costs a full independent
unit of $`r_\alpha`$. If an $`s_C=0`$ component is present, then it is not an
origin, so $`\mathcal O`$ is a proper subset of the $`c(\Theta)`$ components.
The proper-origin case of Theorem 83.3 then gives the sharper bound

```math
\boxed{k_{\rm org}\le r_\alpha.}
\tag{84.8}
```

In the nonzero minimal-face-kernel branch the same atomic component also forces
$`r=1`$ by Corollary 82.3.

A closing proof should split the component geometry into at least the following four
classes:

1. $`s_C=0`$: atomic one-edge segment components; never strict-backward origins;
2. $`s_C=1`$ trees: a genuine residual class that must be controlled directly;
3. cyclic $`s_C=1`$: exact two-direction ordered/Ferrers components;
4. $`s_C=2`$: genuine two-dimensional turning components paying both vector-closure
   directions.

The common component rotations must be paid exactly once through $`r_\alpha`$.
The origin concentration theorem may be used to force internal blocker mass into a
small number of non-atomic components, but it does not itself prove the internal
coforest inequality.

The audited two-family numerical endpoint remains

```math
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2,
\tag{84.9}
```

with gap

```math
\boxed{0.0124073626\ldots D^2.}
\tag{84.10}
```

After the pure inequality, all nonquadrilateral faces, holes, multiple components,
pinches, and outside vertices must still be transported through the exact
topology-corrected shell residual. An uncontrolled $`O(D)`$ rank loss remains fatal.

---

# 85. v1.4 regression additions and rejected inferences

All regressions from Section 47 and the v1.3 continuation remain binding. Add the
following v1.4 tests.

1. **Shifted-lattice monomer phase.** One orientation of elementary triangle-center
   blockers can realize local zero Hall charge through triangular gap faces.
2. **Shifted-lattice lozenge phase.** Dimer cells can realize local zero Hall charge
   through shared-edge quadrilateral faces.
3. **Mixed monomer--dimer interfaces.** Signed Euler charge can cancel across
   interfaces; a proof must control absolute interface/dual-contour charge if it
   relies on interfaces.
4. **s_C=1 tree.** A two-direction terminal tree is not excluded by the canonical
   component theorem and cannot be treated as cyclic Ferrers geometry.
5. **Atomic s_C=0 component.** A one-edge segment component is strictly forward for
   every active bar and supplies no strict-backward origin; any theorem demanding a
   backward origin from every component is false.

The following inferences are explicitly rejected unless separately proved:

- planarity of the scaffold conflict graph implies the Hall surplus;
- the full-complex Euler identity alone implies the Hall surplus;
- every positive Hall cell charge survives after cycle cancellation;
- every dimer-rich scaffold automatically contains a Target B Ferrers block;
- every monomer-rich scaffold automatically admits a Schürmann diameter decrease;
- the monomer--dimer complex automatically contracts to a width-one annulus;
- the Hall problem is automatically a gammoid without an explicit directed linkage
  construction and exact rank equivalence;
- every strict-backward origin is cyclic;
- every $`s_C=1`$ component is cyclic; or
- positive spanning of component rotations proves the internal $`\xi`$-rank bound.

---

# 86. Version 1.4.0 exact status

**LEVEL I STATUS: STILL OPEN.**

Version 1.4.0 makes genuine structural advances on both surviving branches but does
not close either one.

## Target A -- exact planar cycle-cancellation gap

The independent compatible scaffold is now itself an exact planar monomer--dimer Hall
complex. Every blocker occupies one elementary triangle or one unit lozenge, cell
interiors are disjoint, and the exact Hall deficiency is

```math
\boxed{
 h(G)=
 \max_{\substack{Q\subseteq Y_{\rm in}\\b_1(Q)=0}}
 \bigl(\gamma_Q-\mu_Q+b_3(Q)+2b_4(Q)\bigr).
}
\tag{86.1}
```

The contradiction threshold is the one integer

```math
\boxed{h(G)\ge j,}
\tag{86.2}
```

while every survivor has

```math
\boxed{h(G)\le j-1.}
\tag{86.3}
```

Thus the preferred new Target A problem is exact cycle-cut rigidity. The v1.3
cross-configuration two-well transfer problem remains an alternate route but is no
longer necessary if (86.2) can be proved scaffold-internally.

## Target B -- strict rotation rigidity and concentrated origins

Every terminal component has strictly positive width in every active diameter
direction. The $`s_C=0`$ class is atomic and never a backward origin; when the
minimal-face equality kernel is nonzero, its presence also forces $`r=1`$. Common
component rotations have a strict weighted-variance second variation modulo global
rotation, forcing active derivative covectors to positively span the full
$`c(\Theta)-1`$-dimensional quotient. Distinct strict-backward origins consume
component-rotation rank according to

```math
\boxed{
 r_\alpha\ge\min\{k_{\rm org},c(\Theta)-1\}.
}
\tag{86.4}
```

The remaining pure theorem is still

```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha,
}
\tag{86.5}
```

now with the residual blocker origins forced into $`s_C>0`$ components and with
$`s_C=1`$ trees explicitly retained. Exact topology-corrected transport still follows
that pure theorem.

## Unified endgame

A Level I proof requires both survivor branches to be eliminated:

1. **Target A:** prove monomer--dimer cycle-cut rigidity (86.2), or close an
   equivalent scaffold-capacity route;
2. **Target B:** prove the internal relative-angle coforest inequality (86.5) with the
   origin budget and then transport it with exact topology correction.

Disproving one proposed Target A or Target B lemma is not a disproof of Erdős #99.
A Level I disproof requires an infinite sequence of triangle-free **global**
minimizers with exact optimal diameter.

No such infinite family is known.

---

# 87. Current version history and provenance through v1.4.0

- **v1.0.0 (2026-08-26):** canonical synthesis and second-pass audit through the
  translated-lattice, phase-atomic, first-order cusp, backward-flip, tangent-quartic,
  support-turning, and hybrid-forest reductions.
- **v1.1.0 (2026-08-26):** minimal-face harmonic--Dirichlet, peripheral-dual,
  terminal direction-network/turn, boundary-velocity, exact plateau, and optimal-flat
  results; rejection of the cycle-lift shortcut; corrected facial peeling.
- **v1.2.0 (2026-08-26):** rooted-forest self-stress, root-skeleton exactification,
  affine factor exclusion, forest rattlerization, saturation, strict replacement and
  collar growth, terminal-component Minkowski splitting, componentwise closure, and
  stochastic-width component-rotation bookkeeping.
- **v1.3.0 (2026-08-26):** unconditional compatible-collar dichotomy, sharp safe-collar
  population, deep Voronoi containment, global clearance budget, degree-six
  near-neighbor matching, strong Gabriel/Delaunay promotion, matched two-well
  structure, exact Hall--Kőnig scaffold conflict theorem, and inner-band near-perfect
  conflict matching.
- **v1.4.0 (2026-08-26):** exact scaffold monomer--dimer blocker classification,
  interior-disjoint cell packing, planar radial conflict graph, exact Hall/Euler and
  leafless deficiency formulas, face-shell identities, strict positivity of all
  terminal-component widths, atomic `s_C=0` components with the nonzero-kernel
  corollary `r=1`, exact component-rotation variance and positive spanning,
  strict-backward origin-rank concentration, and the
  explicit correction retaining `s_C=1` tree components. Target A is reduced to the
  monomer--dimer cycle-cut rigidity inequality `h(G)>=j`; Target B remains the exact
  internal `xi` coforest inequality with the now-concentrated origin budget and exact
  topology transport.

The only supplied external literature remains:

1. `mp05-2-261-269.pdf`;
2. `1951-03.pdf`;
3. `1-s2.0-S0097316598928898-main.pdf`;
4. `s00454-002-0747-6.pdf`;
5. `1204.4403v1.pdf`;
6. `463.pdf`;
7. `10.1007_PL00009374.pdf`.

No internet source is part of this theorem-state file.

---

# 88. Dual Hall nullity and exact lattice-population deficit

Retain the Target A compatible-collar scaffold of Sections 79--81. Put

```math
X=X_m,
\qquad
R=Y_{\rm in},
\qquad
y=|R|,
\tag{88.1}
```

and let $`\nu=\nu(G)`$ be the maximum matching size of the scaffold conflict graph.
Define the **left scaffold Hall nullity**

```math
\boxed{
 d_{\rm sc}
 =\max_{S\subseteq X}\bigl(|S|-|N(S)|\bigr)
 =m-\nu.
}
\tag{88.2}
```

Define also the **lattice population deficit**

```math
\boxed{\Delta_\Lambda=N-|Y|.}
\tag{88.3}
```

Because $`Y\subset L`$ is a triangular-lattice subset, its mutual distances are at
least one. Because $`L`$ is open and $`\operatorname{diam}(L)<D=D(N)`$, no
$`N`$-point subset of $`Y`$ can exist. Hence

```math
|Y|\le N-1,
\qquad
\boxed{\Delta_\Lambda\ge1.}
\tag{88.4}
```

Recall

```math
h(G)=y-\nu,
\qquad
\delta=y-m,
\qquad
N=m+k+j,
\qquad
|Y|=k+y.
\tag{88.5}
```

Therefore

```math
h(G)=\delta+d_{\rm sc},
\tag{88.6}
```

while

```math
\Delta_\Lambda
=N-|Y|
=(m+k+j)-(k+y)
=j-\delta.
\tag{88.7}
```

Subtracting $`j`$ from (88.6) and using (88.7) gives the exact duality identity

> **Theorem 88.1 (dual Hall/lattice-deficit identity).**
> 

```math
> \boxed{
> h(G)-j=d_{\rm sc}-\Delta_\Lambda.
> }
> \tag{88.8}
> 
```
> Consequently the Target A contradiction is equivalent to
> 

```math
> \boxed{d_{\rm sc}\ge\Delta_\Lambda.}
> \tag{88.9}
> 
```

Thus the older right-deficiency target $`h(G)\ge j`$ and the new left-nullity target
$`d_{\rm sc}\ge N-|Y|`$ are exactly the same one-integer theorem.

---

# 89. Cell-complex phase charge and Hall cores

For $`S\subseteq X`$, let $`m_3(S)`$ and $`m_4(S)`$ be the numbers of selected
monomer and dimer cells. Let $`\mathcal P_S`$ be the elementary-triangle complex
occupied by those cells. Put

- $`b(S)`$: the number of elementary lattice edges incident with exactly one occupied
  elementary triangle of $`\mathcal P_S`$;
- $`\chi(S)`$: the combinatorial Euler characteristic of $`\mathcal P_S`$.

The complex has

```math
F=m_3(S)+2m_4(S)
\tag{89.1}
```

elementary triangles. If $`E,V`$ are its lattice-edge and lattice-vertex counts, then

```math
3F=2E-b(S),
\qquad
V=|N(S)|,
\qquad
\chi(S)=V-E+F.
\tag{89.2}
```

Solving for $`V`$ gives

> **Theorem 89.1 (cell-complex Hall formula).**
> 

```math
> \boxed{
> |S|-|N(S)|
> =\frac{m_3(S)-b(S)}2-\chi(S).
> }
> \tag{89.3}
> 
```

At a lattice vertex $`v\in N(S)`$, define

```math
p_v(S)=\#\{\text{selected monomer cells incident with }v\},
\qquad
q_v(S)=\#\{\text{selected dimer cells incident with }v\}.
\tag{89.4}
```

Each selected monomer has three lattice vertices and each selected dimer has four, so

```math
m_3(S)=\frac13\sum_{v\in N(S)}p_v(S),
\qquad
m_4(S)=\frac14\sum_{v\in N(S)}q_v(S).
\tag{89.5}
```

Subtracting $`|N(S)|`$ yields the exact local phase decomposition.

> **Theorem 89.2 (integer phase-charge formula).**
> 

```math
> \boxed{
> |S|-|N(S)|
> =\sum_{v\in N(S)}
> \left(\frac{p_v(S)}3+\frac{q_v(S)}4-1\right)
> =\frac1{12}\sum_{v\in N(S)}\omega_v(S),
> }
> \tag{89.6}
> 
```
> where
> 

```math
> \boxed{\omega_v(S)=4p_v(S)+3q_v(S)-12.}
> \tag{89.7}
> 
```
> Consequently
> 

```math
> \boxed{
> d_{\rm sc}
> =\max_{S\subseteq X}
> \left[\frac{m_3(S)-b(S)}2-\chi(S)\right]
> =\frac1{12}
> \max_{S\subseteq X}
> \sum_{v\in N(S)}\omega_v(S).
> }
> \tag{89.8}
> 
```

## 89.1 Minimum Hall cores

Choose a maximizer $`S`$ of $`|S|-|N(S)|`$ having minimum cardinality. If
$`d_{\rm sc}=0`$, the empty set is allowed and is such a maximizer. Assume now
$`d_{\rm sc}>0`$, so the chosen core is nonempty.

Suppose a lattice vertex has selected incidence degree one, with unique incident cell
$`x`$. Let $`a\ge1`$ be the number of vertices of $`C_x`$ having selected incidence
degree one. Removing $`x`$ changes the deficiency by

```math
(|S|-1)-(|N(S)|-a)
=(|S|-|N(S)|)+(a-1).
\tag{89.9}
```

If $`a>1`$ this contradicts maximality; if $`a=1`$ it preserves deficiency with a
smaller maximizing set. Therefore every lattice vertex of a positive minimum core has
selected incidence degree at least two.

Deficiency is additive over connected incidence components. A component of
nonpositive deficiency could be deleted, increasing total deficiency or preserving it
with fewer selected cells. Hence every component of a positive minimum core has
strictly positive deficiency.

> **Theorem 89.3 (Hall-core normal form).** A positive-deficiency maximizing set may
> be chosen so that:
> 1. every lattice vertex in its neighborhood is incident with at least two selected
>    cells; and
> 2. every connected incidence component has strictly positive Hall deficiency.

The full scaffold lattice degree is at most five, so every lattice vertex of such a
core satisfies

```math
2\le p_v+q_v\le5.
\tag{89.10}
```

Solving

```math
4p_v+3q_v=12
\tag{89.11}
```

over nonnegative integers in this range gives exactly two states:

> **Corollary 89.4 (only zero-charge phases).**
> 

```math
> \boxed{\omega_v=0
> \Longleftrightarrow
> (p_v,q_v)=(3,0)\ \text{or}\ (0,4).}
> \tag{89.12}
> 
```

Thus the only locally Hall-neutral bulk incidence phases are three incident monomers
and four incident dimers. Every other core vertex carries a nonzero integer interface
charge. This does **not** imply that the nonzero charges have one sign; mixed-interface
cancellation remains possible.

---

# 90. Exact Hall peeling and transversal-matroid circuits

Let

```math
U=N_G(X),
\qquad
z=|R\setminus U|.
\tag{90.1}
```

Thus $`z`$ counts inner-band lattice sites conflicting with no scaffold point.
Start with all cells and delete any collection $`D=X\setminus S`$ in any order. Just
before deleting the $`i`$-th cell, let $`\pi_i`$ be the number of its lattice
vertices whose current selected incidence degree is one.

Every lattice vertex in $`U\setminus N(S)`$ is counted exactly once: when its final
incident cell is deleted. Therefore

```math
\sum_i\pi_i=|U|-|N(S)|.
\tag{90.2}
```

Since $`|D|=m-|S|`$ and $`y=z+|U|`$,

```math
\begin{aligned}
z+\sum_i(\pi_i-1)
&=z+|U|-|N(S)|-|D|\\
&=y-|N(S)|-(m-|S|)\\
&=\delta+|S|-|N(S)|.
\end{aligned}
\tag{90.3}
```

Every residual subset $`S\subseteq X`$ can be obtained by some deletion sequence,
and the value in (90.3) depends only on the residual set. Maximizing gives:

> **Theorem 90.1 (exact Hall-peeling identity).**
> 

```math
> \boxed{
> h(G)
> =z+\max_{\rm cell\ deletion\ sequences}
> \sum_i(\pi_i-1).
> }
> \tag{90.4}
> 
```

Deleting one scaffold point costs one point and frees exactly $`\pi_i`$ lattice sites
at that step. Hall deficiency is therefore the maximum cumulative net gain from cell
peeling, plus the lattice sites that were free from the start.

## 90.1 Transversal matroid and charge-12 Hall circuits

The subsets of $`X`$ that can be matched injectively to distinct neighboring lattice
vertices form a transversal matroid $`\mathcal M_{\rm sc}`$. Its rank is $`\nu`$, so

```math
\boxed{
 d_{\rm sc}=|X|-\operatorname{rank}\mathcal M_{\rm sc}.
}
\tag{90.5}
```

Let $`B`$ be a maximum matchable basis. For each $`x\in X\setminus B`$, let
$`C_x\subseteq B\cup\{x\}`$ be its fundamental circuit. Every proper subset of
$`C_x`$ is matchable, while $`C_x`$ is not. Hall's theorem therefore forces the
only deficient subset of the circuit to be the entire circuit, and its deficiency is
exactly one:

```math
\boxed{|C_x|-|N(C_x)|=1.}
\tag{90.6}
```

By Theorem 89.2,

> **Corollary 90.2 (charge-12 fundamental circuits).**
> 

```math
> \boxed{
> \sum_{v\in N(C_x)}
> \bigl(4p_v(C_x)+3q_v(C_x)-12\bigr)=12.
> }
> \tag{90.7}
> 
```

There are $`|X\setminus B|=d_{\rm sc}`$ nonbasis elements and hence
$`d_{\rm sc}`$ fundamental-circuit certificates of unit nullity. However:

> **Permanent circuit-overlap warning.** Fundamental circuits need not be disjoint,
> laminar, or weakly separated. Their charge-12 certificates cannot be summed as
> spatially distinct interface charge without an additional theorem. Any contraction,
> packing, or contour argument using these circuits must preserve transversal-matroid
> nullity exactly and must control circuit overlap explicitly.

---

# 91. Authoritative v1.4.1 Target A frontier

The cycle-cut formula of Section 81 remains correct, but the preferred v1.4.1 endpoint
is now its exact dual nullity/phase-charge/peeling normal form.

The following statements are equivalent:

```math
\boxed{h(G)\ge j,}
\tag{91.1}
```

```math
\boxed{d_{\rm sc}\ge\Delta_\Lambda,}
\tag{91.2}
```

```math
\boxed{
\max_{S\subseteq X}
\sum_{v\in N(S)}
\bigl(4p_v(S)+3q_v(S)-12\bigr)
\ge12\Delta_\Lambda,
}
\tag{91.3}
```

and

```math
\boxed{
 z+\max_{\rm cell\ deletion\ sequences}
 \sum_i(\pi_i-1)
 \ge j.
}
\tag{91.4}
```

Because $`\Delta_\Lambda=N-|Y|\ge1`$, any certificate of (91.2)--(91.3) has positive
nullity and may be taken in the Hall-core normal form of Theorem 89.3.

Thus the exact new Target A statement is:

> **Target A v1.4.1 (global scaffold phase-charge lemma).** For every scaffold arising
> from a super-boundary triangle-free global minimizer, prove that there exists
> $`S\subseteq X_m`$ such that every lattice vertex of $`N(S)`$ has selected
> incidence degree at least two and
> 

```math
> \boxed{
> \sum_{v\in N(S)}
> \bigl(4p_v(S)+3q_v(S)-12\bigr)
> \ge12\bigl(N-|Y|\bigr).
> }
> \tag{91.5}
> 
```

The local obstruction is now exact. There are only two zero-charge incidence phases:

1. monomer phase: $`(p,q)=(3,0)`$;
2. dimer phase: $`(p,q)=(0,4)`$.

A Hall circuit may contain arbitrarily large regions of either zero-charge phase while
carrying only net charge $`12`$ on its interface. Therefore the remaining theorem is
not local motif classification. It must use the global-optimality origin of $`X_m`$,
the exact lattice deficit $`\Delta_\Lambda`$, exact transversal-matroid nullity, or an
exact diameter-decreasing consequence of coherent zero-charge bulk.

## 91.1 Preferred next route

Choose a maximum matchable basis $`B`$. Every nonbasis cell has a fundamental Hall
circuit of charge $`12`$. A viable new theorem would establish an exact alternative for
one or a controlled family of such circuits:

1. its nonzero-charge interface yields an additional independent Hall circuit or
   augmenting planar-dual cut;
2. after a **nullity-preserving** contraction, it contains a coherent monomer-type
   domain to which an audited diameter-decreasing deformation applies; or
3. after a **nullity-preserving** contraction, it contains a coherent dimer-strip
   system satisfying the actual hypotheses of the audited Ferrers/Cartesian endpoint.

Scalar charge preservation is not enough; the contraction must preserve the
transversal-matroid nullity relevant to (91.2). Likewise, the existence of
$`d_{\rm sc}`$ fundamental circuits does not permit their charges to be added unless
circuit overlap is controlled.

---

# 92. Strengthened two-direction theorem for s_C=1 and bounded tree components

Return to the terminal graph $`\Theta`$ in the pure strict-rhombic Target B branch.
For a connected terminal component $`C`$, recall

```math
L_j=
\operatorname{span}
\{J(u_\tau-u_{\rho(j)}):\partial_{j\tau}\ne0\},
\qquad
s_C=\dim\operatorname{span}_{j\in J_C}L_j.
\tag{92.1}
```

> **Theorem 92.1 (all `s_C=1` components are two-directional).**
> If $`s_C=1`$, then all trains of $`C`$ use exactly two unit direction vectors.

### Proof

Let

```math
W=\operatorname{span}_{j\in J_C}L_j,
\qquad
\dim W=1,
\qquad
M=J^{-1}W.
\tag{92.2}
```

At a terminal vertex with $`t_j=1`$, all incident train vectors lie on one affine line
$`A_j`$ parallel to $`M`$. At a vertex with $`t_j=0`$, all incident train vectors
are equal. Choose a vertex $`j_0`$ with $`t_{j_0}=1`$, which exists because
$`s_C=1`$, and let $`A=A_{j_0}`$. Following a path through the connected component,
a $`t_j=0`$ vertex preserves the incoming direction, while at a $`t_j=1`$ vertex
the unique affine line parallel to $`M`$ through the incoming train vector is again
$`A`$. Hence

```math
u_\tau\in A\cap S^1
\qquad(\tau\in E(C)).
\tag{92.3}
```

An affine line meets the unit circle in at most two points. If only one train direction
occurred, then every $`L_j=0`$, contradicting $`s_C=1`$. Hence exactly two occur.
$`\square`$

The cyclic hypothesis in Theorem 66.2 was therefore unnecessary for the
**two-direction** conclusion. It remains necessary for the currently audited automatic
ordered/Ferrers conclusion: a two-direction tree is not thereby a Ferrers system.

## 92.1 Exact size bound for s_C=1 trees

Assume now that $`C`$ is a tree, with its two train directions denoted $`u,v`$. The
canonical terminal divergence vectors are

```math
e_j=\sum_{\tau\ni j}\partial_{j\tau}u_\tau.
\tag{92.4}
```

They are nonzero convex-hull side vectors and occupy distinct oriented rays in their
inherited cyclic order.

At a leaf,

```math
e_j\in\{\pm u,\pm v\},
\tag{92.5}
```

so there are at most four leaves. If $`n_d`$ denotes the number of degree-$`d`$
vertices, the tree identity

```math
n_1=2+\sum_{d\ge3}(d-2)n_d
\tag{92.6}
```

implies that every vertex has degree at most four and there are at most two vertices
of degree at least three.

At a degree-two vertex, two equal train directions yield an edge vector on a ray
$`\pm u`$ or $`\pm v`$, while two different train directions yield a ray among
$`\pm u\pm v`$. Thus leaves and degree-two vertices together use at most the eight
oriented rays

```math
\pm u,
\quad
\pm v,
\quad
\pm u\pm v.
\tag{92.7}
```

Because distinct hull-edge vectors occupy distinct oriented rays,

```math
n_1+n_2\le8.
\tag{92.8}
```

Adding at most two branching vertices gives:

> **Theorem 92.2 (bounded `s_C=1` tree).**
> 

```math
> \boxed{|V(C)|\le10,\qquad |E(C)|\le9.}
> \tag{92.9}
> 
```

The bound is sharp for the abstract terminal-direction/Minkowski data. For example,
with $`u=(1,0)`$, $`v=(0,1)`$, take the ten convexly ordered edge vectors

```math
\begin{aligned}
&(1,0),(2,1),(1,1),(0,1),(-1,1),\\
&(-1,0),(-2,-1),(-1,-1),(0,-1),(1,-1).
\end{aligned}
\tag{92.10}
```

They sum to zero and have distinct cyclic directions. With incidence sign positive at
the head and negative at the tail, they are realized as terminal divergences by the
nine-edge tree whose $`u`$-edges are

```math
7\to9,
\quad6\to0,
\quad6\to1,
\quad5\to1,
\quad4\to2,
\tag{92.11}
```

and whose $`v`$-edges are

```math
9\to1,
\quad8\to2,
\quad7\to3,
\quad6\to4.
\tag{92.12}
```

This is an abstract regression model, not a claimed global minimizer.

---

# 93. Rank budget for s_C=1 tree origins

Let $`k_{1\rm t}`$ be the number of `s_C=1` tree components that occur as distinct
strict-backward origins. Since these components are a subset of all origin components,
Theorem 83.3 gives

```math
\boxed{k_{1\rm t}\le r_\alpha+1.}
\tag{93.1}
```

If the origin set is proper, in particular whenever an atomic $`s_C=0`$ component is
present, then

```math
\boxed{k_{1\rm t}\le r_\alpha.}
\tag{93.2}
```

By Theorem 92.2, the total number of distinct trains lying in these origin components
satisfies

```math
\boxed{|P_{1\rm t}|\le9(r_\alpha+1),}
\tag{93.3}
```

or

```math
\boxed{|P_{1\rm t}|\le9r_\alpha}
\tag{93.4}
```

in the proper-origin case.

Let $`\mathcal A_{1\rm t}`$ be the span, in the internal $`\xi`$-quotient, of the
projected active-bar average functionals $`\bar s_h`$ occurring in blocker rows whose
strict-backward origins lie in `s_C=1` tree components. For one such component the
internal train-coordinate space modulo common rotation has dimension at most

```math
|E(C)|-1\le8.
\tag{93.5}
```

Every projected blocker row has the form

```math
\bar e_\tau^*-\bar s_h.
\tag{93.6}
```

Therefore the coordinate terms from $`k_{1\rm t}`$ components contribute at most
$`8k_{1\rm t}`$ rank, and the remaining bar-average terms contribute at most
$`\operatorname{rank}\mathcal A_{1\rm t}`$.

> **Theorem 93.1 (`s_C=1` tree-origin rank bound).**
> 

```math
> \boxed{
> \operatorname{rank}\overline{\mathcal B}_{\xi,1\rm t}
> \le
> 8k_{1\rm t}+\operatorname{rank}\mathcal A_{1\rm t}.
> }
> \tag{93.7}
> 
```
> Hence
> 

```math
> \operatorname{rank}\overline{\mathcal B}_{\xi,1\rm t}
> \le
> 8(r_\alpha+1)+\operatorname{rank}\mathcal A_{1\rm t},
> \tag{93.8}
> 
```
> with $`8r_\alpha`$ in place of $`8(r_\alpha+1)`$ in the proper-origin case.

Thus `s_C=1` tree origins can no longer hide unbounded train multiplicity. The
remaining tree-specific obstruction is the possible diversity of the active-bar
averages $`\bar s_h`$: many bars may still produce an independent
$`\mathcal A_{1\rm t}`$ even when all backward origins lie among finitely many tree
trains.

---

# 94. Authoritative v1.4.1 Target B frontier

The global pure-branch target itself is unchanged:

```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha.
}
\tag{94.1}
```

The correct component classification for a closing proof is now:

1. $`s_C=0`$: atomic one-edge segment component, strictly forward for every active
   bar, never a strict-backward origin;
2. $`s_C=1`$, tree: exactly two train directions, at most nine trains, and tree-origin
   internal rank controlled by (93.7), with the residual bar-average span
   $`\mathcal A_{1\rm t}`$ still live;
3. $`s_C=1`$, cyclic: exactly two train directions and, with the additional audited
   cyclic ordering hypotheses, the legitimate two-family/Ferrers class;
4. $`s_C=2`$: genuine two-dimensional turning component paying both vector-closure
   directions.

The old v1.4 warning that `s_C=1` trees were an unclassified potentially large class
is superseded. They remain possible, but their coordinate population is uniformly
bounded componentwise.

The next exact Target B subproblem is therefore to charge

```math
\boxed{
\mathcal A_{1\rm t}
=\operatorname{span}
\{\bar s_h:
 h\text{ has a strict-backward incidence in an }s_C=1\text{ tree}\}
}
\tag{94.2}
```

to the terminal coforest/cycle budget or to the already reserved $`I+r`$ dimensions.
A successful theorem here would eliminate repeated-bar diversity as the last
`s_C=1`-tree-specific loophole. It would not by itself finish the `s_C=2` or cyclic
`s_C=1` contributions, nor the topology-corrected transport.

The audited Ferrers numerical endpoint remains unchanged and need not be improved:

```math
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2.
\tag{94.3}
```

---

# 95. v1.4.1 regressions, rejected shortcuts, and next routes

All earlier regression suites remain binding. Add the following v1.4.1 regressions.

1. **Overlapping Hall circuits.** A transversal matroid can have many fundamental
   circuits sharing most of their support. Section 97 proves exact signed-deficiency
   additivity for fixed-basis unions, but one charge-12 certificate per nonbasis
   element still does not imply spatially disjoint or absolute interface charge
   `12 d_sc`.
2. **Large zero-charge bulk inside one Hall circuit.** A minimally unmatchable circuit
   can contain an arbitrarily large locally neutral monomer or dimer region while its
   net charge remains exactly 12.
3. **Empty nullity core.** When `d_sc=0`, the empty set is a legitimate
   minimum-cardinality maximizer; core minimum-degree conclusions are for positive
   nullity.
4. **Ten-vertex `s_C=1` tree.** The abstract example (92.10)--(92.12) shows that the
   `10`-vertex/`9`-train bound is sharp from terminal-direction/Minkowski data alone.
5. **Repeated-bar diversity.** Bounding the number of tree-origin trains does not
   bound the rank of the active-bar averages `A_{1t}`.

The following shortcuts are rejected unless separately proved:

- treating the charge 12 of all fundamental Hall circuits as disjoint or absolute spatial charge;
- contracting an arbitrary zero-charge phase region without one of the exact
  nullity-preserving contraction theorems of Sections 97--100;
- treating scalar phase-charge conservation as equivalent to matching-rank
  conservation;
- inferring a global Hall surplus from the fact that only two local zero-charge phases
  exist;
- treating every two-direction `s_C=1` component as cyclic/Ferrers;
- replacing the residual `rank A_{1t}` by the number of tree-origin trains without a
  theorem; or
- using the `9(r_alpha+1)` train bound as if it were already the full internal
  coforest inequality.

The preferred new Target A route is a nullity-preserving circuit/phase contraction
or planar-dual theorem that either accumulates independent Hall nullity or converts a
coherent zero-charge phase into an actual global diameter improvement.

The preferred new Target B route is an exact bound on `rank A_{1t}` in terms of
terminal coforest/cycle data or the existing `I+r` budget, followed by the residual
componentwise coforest theorem and exact topology transport.

---

# 96. Version 1.4.1 exact status and provenance

**LEVEL I STATUS: STILL OPEN.**

Version 1.4.1 does not close either survivor branch. It sharpens both.

Target A is now equivalently one of the exact statements

```math
h(G)\ge j,
\qquad
 d_{\rm sc}\ge\Delta_\Lambda,
\tag{96.1}
```

```math
\max_{S\subseteq X_m}
\sum_{v\in N(S)}
(4p_v(S)+3q_v(S)-12)
\ge12\Delta_\Lambda,
\tag{96.2}
```

or

```math
z+\max\sum_i(\pi_i-1)\ge j.
\tag{96.3}
```

The two locally neutral phases are exactly `(3,0)` monomer incidence and `(0,4)`
dimer incidence. The missing theorem is global phase-charge/nullity rigidity, not
another local motif classification.

Target B remains

```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha
}
\tag{96.4}
```

followed by exact topology-corrected transport. The new theorem says every `s_C=1`
component is two-directional and every `s_C=1` tree has at most nine trains. The
remaining tree-specific rank obstruction is the projected active-bar-average span
$`\mathcal A_{1\rm t}`$.

Version history:

- v1.0.0: structural synthesis, KKT/stress, almost-rhombic and hybrid normal forms;
- v1.1.0: minimal-face harmonic transport, terminal network, plateau theorem;
- v1.2.0: forest exactification/rattlerization and terminal Minkowski components;
- v1.3.0: compatible collar, clearance matching, two wells, exact Hall scaffold;
- v1.4.0: scaffold monomer--dimer Hall complex plus strict stochasticity and
  strict-backward origin-rank concentration;
- **v1.4.1:** dual Hall/lattice deficit, exact phase-charge and peeling forms,
  transversal-matroid Hall circuits, all-`s_C=1` two-direction theorem, bounded
  `s_C=1` trees, and their internal rank budget.

`erdos_problem_99_1.4.1.md` was the sole canonical theorem-state file at the v1.4.1
stage; Sections 97 onward and the v1.5.0 audit policy now supersede that frontier.

---

# 97. Fixed-basis tight unions, exact full-core contraction, and boundary-order nullity

Retain the Target A scaffold conflict graph
```math
G=(X\sqcup R,E),
\qquad
f(S):=|S|-|N(S)|,
\qquad
d_{\rm sc}=\max_{S\subseteq X}f(S).
\tag{97.1}
```

Let $`B\subseteq X`$ be a maximum matchable basis of the scaffold transversal
matroid. For $`e\in X\setminus B`$, let $`C_e\subseteq B\cup\{e\}`$ be its
fundamental circuit. For $`A\subseteq X\setminus B`$, put
```math
U_A:=\bigcup_{e\in A}C_e.
\tag{97.2}
```

## 97.1 Exact fixed-basis union theorem

> **Theorem 97.1 (tight fundamental-circuit unions).**
> For every $`A\subseteq X\setminus B`$,
> 

```math
> \boxed{f(U_A)=|A|.}
> \tag{97.3}
> 
```
> Consequently
> 

```math
> \boxed{
> \sum_{v\in N(U_A)}
> \bigl(4p_v(U_A)+3q_v(U_A)-12\bigr)=12|A|.
> }
> \tag{97.4}
> 
```

### Proof

Let
```math
B_A:=U_A\cap B.
\tag{97.5}
```
Every $`e\in A`$ lies in the matroid closure of
$`C_e\setminus\{e\}\subseteq B_A`$, while $`B_A`$ is independent. Hence
```math
r(U_A)=|B_A|,
\qquad
|U_A|-r(U_A)=|A|.
\tag{97.6}
```

Any matching of $`U_A`$ can use only vertices in $`N(U_A)`$, so
```math
r(U_A)\le |N(U_A)|.
\tag{97.7}
```
Therefore
```math
f(U_A)
=|U_A|-|N(U_A)|
\le |U_A|-r(U_A)
=|A|.
\tag{97.8}
```

Order $`A=\{e_1,\ldots,e_k\}`$ and put
```math
U_i:=\bigcup_{j\le i}C_{e_j}.
\tag{97.9}
```
Because $`C_{e_i}\subseteq B\cup\{e_i\}`$ and no earlier fundamental circuit contains
$`e_i`$,
```math
U_{i-1}\cap C_{e_i}\subseteq B.
\tag{97.10}
```
Thus the intersection is matchable and has deficiency at most zero. Also
```math
f(C_{e_i})=1.
\tag{97.11}
```

The neighborhood function is submodular, so $`f`$ is supermodular:
```math
f(S\cup T)+f(S\cap T)\ge f(S)+f(T).
\tag{97.12}
```
Inductively, if $`f(U_{i-1})=i-1`$, then
```math
f(U_i)+f(U_{i-1}\cap C_{e_i})\ge i.
\tag{97.13}
```
But (97.8) gives $`f(U_i)\le i`$ and (97.10) gives
$`f(U_{i-1}\cap C_{e_i})\le0`$. Therefore equality holds in both:
```math
\boxed{
f(U_i)=i,
\qquad
f(U_{i-1}\cap C_{e_i})=0.
}
\tag{97.14}
```
This proves (97.3). Equation (97.4) follows from the exact phase-charge identity.
$`\square`$

The important correction is precise:

> Fundamental circuits relative to one fixed maximum basis may overlap heavily, but
> every successive overlap is Hall-tight. Signed Hall deficiency is exactly additive
> along the fixed-basis union flag. This does **not** make the circuit interfaces
> disjoint and does not make absolute/spatial phase charge additive.

## 97.2 Full tight-core contraction

Take
```math
A=X\setminus B,
\qquad
U:=U_A,
\qquad
W:=N(U),
\qquad
d:=d_{\rm sc}.
\tag{97.15}
```
Since
```math
|A|=|X|-r(X)=d_{\rm sc},
\tag{97.16}
```
Theorem 97.1 gives
```math
|U|-|W|=d.
\tag{97.17}
```

Let $`B_U=U\cap B`$. Then
```math
|W|=|U|-d=|B_U|.
\tag{97.18}
```
Any matching saturating $`B`$ maps $`B_U`$ into $`W`$. Equal cardinalities force a
bijection $`B_U\to W`$, and consequently map
```math
B\setminus B_U=X\setminus U
\tag{97.19}
```
into $`R\setminus W`$.

Thus the residual left side is fully matchable.

Moreover $`W=N(U)`$, so there are no conflict edges from $`U`$ to $`R\setminus W`$.
Every independent set in the residual conflict graph therefore lifts by adjoining
all of $`U`$.

Define the residual population data
```math
N^0:=N-|U|,
\qquad
Y^0:=Y\setminus W.
\tag{97.20}
```
Then
```math
\boxed{
N^0-|Y^0|
=\Delta_\Lambda-d_{\rm sc}.
}
\tag{97.21}
```

> **Theorem 97.2 (nullity-zero full-core contraction).**
> The entire scaffold nullity can be extracted as one fixed-basis tight core
> $`U\cup W`$. After deleting that core, the residual left side is fully matchable,
> and the exact surviving lattice-population gap is
> 

```math
> \boxed{g=\Delta_\Lambda-d_{\rm sc}.}
> \tag{97.22}
> 
```

A hypothetical Target A survivor has
```math
d_{\rm sc}\le\Delta_\Lambda-1,
\tag{97.23}
```
so
```math
\boxed{g\ge1.}
\tag{97.24}
```

The residual $`X\setminus U`$ is a subset of a global optimum, but it is **not**
known to be globally optimal for $`N^0`$. No optimum-only theorem may be recursively
applied to it without a separate argument.

## 97.3 Boundary-order bound on all scaffold nullity

Let $`d_m=D(m)`$, $`D=D(N)`$, and
```math
t=\frac{D-d_m}{2}>1.
\tag{97.25}
```
For the same generic triangular-lattice translate, the Voronoi cells centered at
lattice sites in the inner band cover
```math
K_m+\left(1-\frac1{\sqrt3}\right)\mathbb B.
\tag{97.26}
```
Combining the resulting lattice count with Steiner and finite Oler gives, for
```math
\delta=|Y_{\rm in}|-m,
\tag{97.27}
```
the exact lower estimate
```math
\boxed{
\delta\ge
-1-\frac{7-4\sqrt3}{6}P_m
+\frac{8\pi}{3\sqrt3}
-\frac{4\pi}{3}.
}
\tag{97.28}
```

Combining this with the trusted $`t`$-dependent safe-collar estimate yields
```math
\boxed{
\Delta_\Lambda
<
\pi D+\frac{2\pi}{3}d_m
+1+\frac{\pi}{3}-\frac{2\pi}{3\sqrt3}.
}
\tag{97.29}
```
A survivor therefore satisfies
```math
\boxed{
d_{\rm sc}
<
\pi D+\frac{2\pi}{3}d_m
+\frac{\pi}{3}-\frac{2\pi}{3\sqrt3}.
}
\tag{97.30}
```

Since $`t>1`$ implies $`d_m<D-2`$,
```math
\boxed{
\Delta_\Lambda
<
\frac{5\pi}{3}D
+1-\pi-\frac{2\pi}{3\sqrt3},
}
\tag{97.31}
```
and
```math
\boxed{
d_{\rm sc}
<
\frac{5\pi}{3}D
-\pi-\frac{2\pi}{3\sqrt3}
=
5.23598775598\ldots D-4.35079222975\ldots.
}
\tag{97.32}
```

Thus **all scaffold nullity is boundary-order** in every hypothetical survivor.

---

# 98. Phase-selective contraction and six planar gammoid presentations

Fix a lattice basis $`e_1,e_2`$. Write the two orientations of elementary unit
triangles as
```math
T_z^+=\operatorname{conv}\{z,z+e_1,z+e_2\},
\tag{98.1}
```
```math
T_z^-=\operatorname{conv}\{z+e_1,z+e_2,z+e_1+e_2\}.
\tag{98.2}
```

Partition the scaffold blocker cells as
```math
X=\mathcal D\sqcup\mathcal M_+\sqcup\mathcal M_-,
\tag{98.3}
```
where $`\mathcal D`$ are dimers and $`\mathcal M_\pm`$ are monomers of the two
orientations.

## 98.1 Entire crystalline phases are independent

Every dimer contains exactly one $`+`$-triangle and one $`-`$-triangle. Every
$`+`$-monomer contains exactly one $`+`$-triangle. Since distinct blocker cells have
disjoint interiors, distinct cells in
```math
\mathcal I_+:=\mathcal D\cup\mathcal M_+
\tag{98.4}
```
contain distinct $`+`$-triangles.

The map
```math
T_z^+\longmapsto z
\tag{98.5}
```
matches every such triangle to one of its actual conflict vertices and is injective
over the selected cells. Therefore $`\mathcal I_+`$ is independent. Symmetrically,
```math
\mathcal I_-:=\mathcal D\cup\mathcal M_-
\tag{98.6}
```
is independent.

> **Theorem 98.1 (phase-selective independence).**
> 

```math
> \boxed{
> \mathcal D\cup\mathcal M_+,
> \quad
> \mathcal D\cup\mathcal M_-
> \text{ are independent in }\mathcal M_{\rm sc}.
> }
> \tag{98.7}
> 
```

If $`m_\pm=|\mathcal M_\pm|`$, contraction by either independent phase preserves the
entire nullity:
```math
\boxed{
d_{\rm sc}
=
m_-
-r_{\mathcal M_{\rm sc}/\mathcal I_+}(\mathcal M_-)
=
m_+
-r_{\mathcal M_{\rm sc}/\mathcal I_-}(\mathcal M_+).
}
\tag{98.8}
```

This is an exact matroid theorem, not a scalar zero-charge argument.

## 98.2 Alternating-gammoid representation

Fix a matching $`\mu_+`$ of $`\mathcal I_+`$ to the distinguished $`+`$-triangle
vertices and put
```math
T_+:=Y_{\rm in}\setminus\mu_+(\mathcal I_+).
\tag{98.9}
```
Orient the radial conflict graph alternately relative to $`\mu_+`$:

- residual $`-`$-monomer $`\to`$ lattice vertex;
- matched lattice vertex $`\to`$ its $`\mathcal I_+`$-cell;
- every other edge of an $`\mathcal I_+`$-cell points from the cell to the lattice
  vertex.

Let $`\lambda_+`$ be the maximum number of pairwise vertex-disjoint directed paths
from distinct residual $`-`$-monomers to distinct sinks in $`T_+`$.

The usual symmetric-difference argument gives
```math
J\subseteq\mathcal M_-
\text{ independent in }\mathcal M_{\rm sc}/\mathcal I_+
\iff
J\text{ links vertex-disjointly to }T_+.
\tag{98.10}
```
Hence
```math
\boxed{
\nu(G)=|\mathcal I_+|+\lambda_+,
}
\tag{98.11}
```
```math
\boxed{
d_{\rm sc}=m_- -\lambda_+,
\qquad
h(G)=|T_+|-\lambda_+.
}
\tag{98.12}
```
The symmetric equations hold with $`+`$ and $`-`$ exchanged.

In particular
```math
\boxed{
d_{\rm sc}
=
m_- -\lambda_+
=
m_+ -\lambda_-,
}
\tag{98.13}
```
and
```math
\boxed{d_{\rm sc}\le\min(m_+,m_-).}
\tag{98.14}
```

## 98.3 Six anchor choices and layered DAGs

For each orientation there are three choices of distinguished vertex of the
elementary triangle. For the $`+`$-contraction, label the anchors $`a=0,1,2`$.
In lattice coordinates
```math
v=pe_1+qe_2,
\tag{98.15}
```
take the height functions
```math
\ell_0(v)=p+q,
\qquad
\ell_1(v)=-p,
\qquad
\ell_2(v)=-q.
\tag{98.16}
```

For each anchor, every directed alternating arc is nondecreasing in the
corresponding height. Strict arcs raise height. Zero-height transitions are unit
steps along one lattice line and come from dimers. Two oppositely directed
zero-height transitions would force two dimers to occupy the same elementary
triangle, contradicting disjoint cell interiors.

> **Theorem 98.2 (six layered phase-anchor DAGs).**
> Each of the three anchor presentations for either monomer orientation is a planar
> directed acyclic graph, and for every anchor $`a`$
> 

```math
> \boxed{
> d_{\rm sc}=m_- -\lambda_a,
> \qquad
> h(G)=|T_a|-\lambda_a
> }
> \tag{98.17}
> 
```
> in the $`+`$-contraction, with the symmetric statement for the $`-`$-contraction.

## 98.4 Exact directed-contour formula

For a fixed phase-anchor DAG $`\Gamma_a`$, let $`S=\mathcal M_-`$ denote the sources
and $`T_a`$ the free sinks. For $`W\subseteq V(\Gamma_a)`$, define
```math
\partial^+W
=
\{v\notin W:\exists u\in W,\ u\to v\},
\tag{98.18}
```
```math
\partial^-W
=
\{v\notin W:\exists u\in W,\ v\to u\}.
\tag{98.19}
```

Directed vertex-Menger, with source vertices of indegree zero, gives
```math
\boxed{
d_{\rm sc}
=
\max_{W\cap T_a=\varnothing}
\bigl(|S\cap W|-|\partial^+W|\bigr).
}
\tag{98.20}
```
Applying the same argument to the reversed digraph gives
```math
\boxed{
h(G)
=
\max_{W\cap S=\varnothing}
\bigl(|T_a\cap W|-|\partial^-W|\bigr).
}
\tag{98.21}
```

This replaces signed local interface bookkeeping by an exact absolute directed
boundary quantity. It is still not a width-one-annulus terminalization, and abstract
planarity alone does not imply the Target A inequality.

---

# 99. Plateau terminalization and exact boundary-terminal matching

Let $`m`$ be the smaller cardinality arising in Target A and
```math
d=D(m).
\tag{99.1}
```
Define the right endpoint of the $`d`$-plateau by
```math
m^\ast:=\max\{q\ge m:D(q)=d\}.
\tag{99.2}
```
The exact plateau theorem gives
```math
\boxed{
0\le m^\ast-m<\frac{\pi}{2}d.
}
\tag{99.3}
```
Replacing $`m`$ by $`m^\ast`$ costs only $`O(D)`$ points, so a super-boundary
rattler population remains super-boundary.

Choose an $`m^\ast`$-point optimum $`X^\ast`$ and put
```math
K^\ast=\operatorname{conv}X^\ast.
\tag{99.4}
```
By maximality of the plateau,
```math
D(m^\ast+1)>d.
\tag{99.5}
```

## 99.1 Unit-covering saturation at the plateau endpoint

If $`z\in K^\ast`$ satisfied
```math
|z-x|\ge1
\qquad(x\in X^\ast),
\tag{99.6}
```
then $`X^\ast\cup\{z\}`$ would be an $`(m^\ast+1)`$-point unit-separated set of
diameter at most $`d`$, contradicting (99.5). Therefore
```math
\boxed{
\forall z\in K^\ast,\qquad
\min_{x\in X^\ast}|z-x|<1.
}
\tag{99.7}
```

The strict inequality matters.

The same saturated clearance and Delaunay arguments used earlier can therefore be
run on $`X^\ast`$ itself. In particular,
```math
\sum_{x\in X^\ast}
\left(\min_{x'\ne x}|x-x'|-1\right)
<
\left(24+\frac{\pi}{2}\right)d+18.
\tag{99.8}
```
The local equality wells remain
```math
\{1,1,1\},
\qquad
\{1,1,\sqrt3\}.
\tag{99.9}
```
This co-embeds the saturated Delaunay geometry and the exact scaffold geometry on the
same smaller optimum. It does **not** by itself imply the Target A Hall surplus.

## 99.2 The interior lattice has exactly zero right deficiency

For the generic scaffold translate define
```math
Z=(\Lambda+v)\cap\operatorname{int}K^\ast,
\qquad
O=Y_{\rm in}\setminus Z.
\tag{99.10}
```
Genericity excludes lattice points on $`\partial K^\ast`$, so
```math
O\subset
\operatorname{int}(K^\ast+\mathbb B)\setminus K^\ast.
\tag{99.11}
```

Let
```math
G_0=G[X^\ast\sqcup Z].
\tag{99.12}
```
An independent set in $`G_0`$ is exactly a unit-separated subset of $`K^\ast`$. By
(99.5) it has at most $`m^\ast`$ elements, while $`X^\ast`$ itself has $`m^\ast`$
elements. Therefore
```math
\alpha(G_0)=m^\ast.
\tag{99.13}
```
Kőnig gives
```math
\boxed{\nu(G_0)=|Z|.}
\tag{99.14}
```
Equivalently,
```math
\boxed{
|Q|\le|N_{G_0}(Q)|
\qquad(Q\subseteq Z).
}
\tag{99.15}
```

Thus the interior lattice has zero right Hall deficiency.

Because plateau saturation also excludes isolated vertices of $`Z`$, the exact
peeling identity gives
```math
\boxed{
\max_{\text{interior cell deletions}}
\sum_i(\pi_i^{\rm int}-1)=0.
}
\tag{99.16}
```

## 99.3 Exact deep-nullity plus boundary-linkage split

Let $`\mathcal M_Z`$ be the transversal matroid on $`X^\ast`$ represented by
conflicts with $`Z`$. Put
```math
X_{\rm deep}
=
\{x\in X^\ast:N(x)\subseteq Z\}.
\tag{99.17}
```
Define
```math
\boxed{
d_{\rm int}
=
|X_{\rm deep}|-r_{\mathcal M_Z}(X_{\rm deep}).
}
\tag{99.18}
```

Choose a basis $`I_{\rm deep}`$ of the restriction to $`X_{\rm deep}`$, extend it to
a basis $`I_0`$ of $`\mathcal M_Z`$, and choose a matching $`\mu_0`$ of $`I_0`$ onto
all of $`Z`$. Put
```math
U_{\rm int}=X_{\rm deep}\setminus I_{\rm deep},
\tag{99.19}
```
```math
X_\partial=X^\ast\setminus X_{\rm deep},
\qquad
S_\partial=X_\partial\setminus I_0.
\tag{99.20}
```
Then
```math
\boxed{
m^\ast-|Z|
=d_{\rm int}+s_\partial,
\qquad
s_\partial:=|S_\partial|.
}
\tag{99.21}
```

No augmenting path from $`O`$ relative to $`\mu_0`$ can end at a vertex of
$`U_{\rm int}`$. Flipping such a path would match
$`I_{\rm deep}\cup\{x\}`$ into $`Z`$, contradicting maximality of the restricted
basis.

Let $`\lambda_\partial`$ be the maximum number of vertex-disjoint augmenting paths
from distinct $`O`$-vertices to distinct $`S_\partial`$-vertices. Then
```math
\boxed{
\nu(G)=|Z|+\lambda_\partial,
}
\tag{99.22}
```
hence
```math
\boxed{
d_{\rm sc}
=
d_{\rm int}+s_\partial-\lambda_\partial.
}
\tag{99.23}
```
On the right,
```math
\boxed{
h(G)=|O|-\lambda_\partial.
}
\tag{99.24}
```

This is the exact boundary-terminal normal form. Deep unmatched blockers are not
discarded; their exact cost is $`d_{\rm int}`$.

Every $`x\in X_\partial`$ lies within unit distance of $`\partial K^\ast`$, and every
$`y\in O`$ lies in the exterior unit band. Both terminal populations are
boundary-order:
```math
\boxed{
s_\partial\le|X_\partial|\le12d+9,
}
\tag{99.25}
```
and
```math
\boxed{
d_{\rm int}+s_\partial
=m^\ast-|Z|
\le1+\frac{7\pi}{6}d.
}
\tag{99.26}
```

The routing graph may still traverse the $`O(d^2)`$ interior. Boundary terminality
does not imply width-one-annulus routing.

## 99.4 Two-sided plateau normalization

For a genuine super-boundary source survivor, let
```math
N_-:=\min\{q:D(q)=D\},
\qquad
m_+:=\max\{q:D(q)=d\},
\tag{99.27}
```
and put
```math
p_N=N-N_-,
\qquad
p_m=m_+-m.
\tag{99.28}
```
The plateau theorem gives
```math
p_N<\frac{\pi D}{2},
\qquad
p_m<\frac{\pi d}{2}.
\tag{99.29}
```

Since the source contains $`\rho=\omega(D)`$ strict rattlers, sufficiently large
survivors satisfy
```math
\rho>p_N+p_m.
\tag{99.30}
```
Deleting $`p_N`$ non-diametral strict rattlers leaves an $`N_-`$-point
triangle-free global minimizer of the same diameter $`D`$. Designating
```math
\rho^\dagger:=\rho-p_N-p_m
\tag{99.31}
```
further rattlers for removal makes the target smaller cardinality exactly $`m_+`$.

Define the finite-packing defect
```math
E(n)
=
\frac{D(n)^2}{c}
+\frac{\pi D(n)}2
-(n-1).
\tag{99.32}
```
At fixed diameter, $`E`$ decreases by one when the cardinality increases by one, so
```math
\boxed{
E(N_-)=E(N)+p_N,
\qquad
E(m_+)=E(m)-p_m.
}
\tag{99.33}
```
Thus two-sided endpoint normalization improves the defect transfer by exactly
$`p_N+p_m`$.

This normalization is useful, but the sign of the residual defect transfer remains
uncontrolled.

---

# 100. Phase-pure boundary minors and exterior interface charge

Retain the plateau-terminalized scaffold of Section 99 and split
```math
X^\ast=X^\circ\sqcup X^\partial,
\tag{100.1}
```
where
```math
X^\circ=\{x:N(x)\subseteq Z\},
\qquad
X^\partial=X^\ast\setminus X^\circ.
\tag{100.2}
```
Then $`d_{\rm int}`$ is the exact nullity of the deep restriction.

Fix the $`+`$-phase contraction
```math
\mathcal A_+=\mathcal D\cup\mathcal M_+,
\qquad
\mathcal E=\mathcal M_-,
\tag{100.3}
```
and split both sets into deep and boundary parts.

Let
```math
\mathcal L=\mathcal M/\mathcal A_+^\circ.
\tag{100.4}
```
Since $`\mathcal A_+^\circ`$ is independent,
```math
|\mathcal E^\circ|-r_{\mathcal L}(\mathcal E^\circ)=d_{\rm int}.
\tag{100.5}
```

Define the deep-rank transfer
```math
\theta_+
=
r_{\mathcal L}(\mathcal E^\circ)
+
|\mathcal A_+^\partial|
-
r_{\mathcal L}
(\mathcal E^\circ\cup\mathcal A_+^\partial).
\tag{100.6}
```
Submodularity and independence give
```math
\boxed{
0\le\theta_+\le|\mathcal A_+^\partial|.
}
\tag{100.7}
```

After contracting all of $`\mathcal A_+`$,
```math
\boxed{
|\mathcal E^\circ|
-
r_{\mathcal M/\mathcal A_+}(\mathcal E^\circ)
=
d_{\rm int}+\theta_+.
}
\tag{100.8}
```

Choose a basis $`J_+`$ of $`\mathcal E^\circ`$ in the contracted matroid and put
```math
\mathcal Q_+
=
\mathcal M/(\mathcal A_+\cup J_+).
\tag{100.9}
```
The elements of
```math
\mathcal E^\circ\setminus J_+
\tag{100.10}
```
are loops. The only remaining possibly nonloop ground elements are
```math
\mathcal E^\partial
=
\mathcal M_-\cap X^\partial.
\tag{100.11}
```

Define
```math
d_{\partial,-}^{(+)}
=
|\mathcal E^\partial|
-r_{\mathcal Q_+}(\mathcal E^\partial).
\tag{100.12}
```

> **Theorem 100.1 (phase-pure boundary decomposition).**
> 

```math
> \boxed{
> d_{\rm sc}
> =
> d_{\rm int}
> +\theta_+
> +d_{\partial,-}^{(+)}.
> }
> \tag{100.13}
> 
```
> Symmetrically,
> 

```math
> \boxed{
> d_{\rm sc}
> =
> d_{\rm int}
> +\theta_-
> +d_{\partial,+}^{(-)}.
> }
> \tag{100.14}
> 
```

The complete residual ground set obeys
```math
\boxed{
|\operatorname{ground}(\mathcal Q_\pm)|
\le
d_{\rm int}+|X^\partial|
\le
\left(12+\frac{7\pi}{6}\right)d+10
=
15.665191\ldots d+10.
}
\tag{100.15}
```

Thus the exact matroid ground set, not merely its terminal set, can be reduced to
$`O(d)`$ elements. Its alternating routing may still pass through bulk lattice
vertices.

## 100.1 Exterior degree and phase-interface theorem

For generic lattice translate and $`y\in O`$,
```math
\boxed{\deg_G(y)\le3.}
\tag{100.16}
```
Indeed all conflict vectors $`x-y`$ lie in one open semicircle. Four such vectors
would contain two consecutive vectors separated by angle $`<\pi/3`$, and for
lengths $`r,s<1`$,
```math
|x-x'|^2
<
r^2+s^2-rs
<1,
\tag{100.17}
```
contradicting unit separation.

Around one triangular-lattice vertex, the three monomer sectors of one fixed
orientation alternate. Three such sectors cannot all fit into one open semicircle.
Therefore
```math
\boxed{
\deg_{\mathcal M_+}(y)\le2,
\qquad
\deg_{\mathcal M_-}(y)\le2
\qquad(y\in O).
}
\tag{100.18}
```

Let $`S`$ be a connected positive Hall core of deficiency $`r`$. At
$`y\in N(S)\cap O`$, write
```math
p_y=p_y^++p_y^-,
\qquad
\tau_y=p_y^+-p_y^-,
\tag{100.19}
```
and define
```math
\beta_y=12-4p_y-3q_y\ge0.
\tag{100.20}
```
Every outer core vertex has selected degree two or three. If $`\beta_y=0`$, then
$`(p_y,q_y)=(3,0)`$, and (100.18) forces a $`2{:}1`$ orientation split, so
```math
|\tau_y|=1.
\tag{100.21}
```
Hence
```math
\boxed{
\beta_y+|\tau_y|\ge1.
}
\tag{100.22}
```

Splitting the exact phase-charge identity into $`Z`$ and $`O`$ gives
```math
\boxed{
\sum_{z\in N(S)\cap Z}\omega_z
+
\sum_{y\in N(S)\cap O}|\tau_y|
\ge
12r+|N(S)\cap O|.
}
\tag{100.23}
```

Thus the scalar-neutral monomer phase cannot meet the physical exterior boundary as
a pure orientation: every neutral exterior terminal carries an absolute orientation
interface.

---

# 101. Quantized convexification gap for positive Hall cores

Let $`S`$ be a connected positive Hall core of deficiency $`r>0`$. Let

- $`m_3=m_++m_-`$ be the monomer count;
- $`m_4`$ the dimer count;
- $`F=m_3+2m_4`$ the number of occupied elementary triangles;
- $`q`$ the number of holes;
- $`b_0`$ the outer boundary length;
- $`b_h`$ the total hole-boundary length;
- $`b=b_0+b_h`$;
- $`\mathcal P_S`$ the occupied elementary-triangle complex;
- $`H=\operatorname{conv}\mathcal P_S`$.

Put
```math
g_H
=
\frac{\operatorname{area}(H)-\operatorname{area}(\mathcal P_S)}{c_0}.
\tag{101.1}
```
Because $`H`$ is a triangular-lattice polygon,
```math
g_H\in\mathbb Z_{\ge0}.
\tag{101.2}
```

The blocker points lie strictly inside $`H`$. Finite Oler applied to those
$`m_3+m_4`$ points, together with
```math
\operatorname{per}H\le b_0,
\tag{101.3}
```
gives
```math
m_3+m_4-1
<
\frac{F+g_H}{2}+\frac{b_0}{2}.
\tag{101.4}
```
After multiplying by two and using integrality,
```math
g_H\ge m_3-1-b_0.
\tag{101.5}
```

The cell-complex formula for a connected core is
```math
r=\frac{m_3-b}{2}-1+q,
\tag{101.6}
```
so
```math
m_3=b+2r+2-2q.
\tag{101.7}
```
Since
```math
b_h\ge3q,
\tag{101.8}
```
we obtain the exact quantized gap:

> **Theorem 101.1 (convexification-gap theorem).**
> 

```math
> \boxed{
> g_H\ge2r+q+1.
> }
> \tag{101.9}
> 
```

In particular, no positive Hall core has a convex occupied cell complex.

Let
```math
\varepsilon=b-3(q+1)\ge0.
\tag{101.10}
```
Then
```math
b_0\le\varepsilon+3.
\tag{101.11}
```
Isoperimetry gives
```math
c_0(F+g_H)
=
\operatorname{area}(H)
\le
\frac{b_0^2}{4\pi},
\tag{101.12}
```
hence
```math
\boxed{
F+2r+q+1
\le
\frac{(\varepsilon+3)^2}{\pi\sqrt3}.
}
\tag{101.13}
```

For a circuit $`r=1`$. If $`\varepsilon\le6`$, then
```math
\frac{(\varepsilon+3)^2}{\varepsilon+10}
\le
\frac{81}{16}
<
\pi\sqrt3,
\tag{101.14}
```
contradicting (101.13), because
```math
m_3=\varepsilon+q+7
\quad\text{and}\quad
F\ge m_3.
\tag{101.15}
```
Therefore
```math
\boxed{\varepsilon\ge7}
\tag{101.16}
```
for every Hall circuit.

The phase-orientation side count gives
```math
3(m_+-m_-)=b_+-b_-,
\qquad
|m_+-m_-|\le\frac b3.
\tag{101.17}
```
Combining with (101.7) and $`\varepsilon\ge7`$ yields:

> **Corollary 101.2 (strong biphasic circuit kernel).**
> Every scaffold Hall circuit satisfies
> 

```math
> \boxed{
> m_3\ge14,
> \qquad
> m_+\ge6,
> \qquad
> m_-\ge6.
> }
> \tag{101.18}
> 
```

This does not sum convexification gaps over overlapping circuits.

---

# 102. Exact boundary Schur response

Retain the plateau-terminalized scaffold and write
```math
Z=(\Lambda+v)\cap\operatorname{int}K,
\qquad
O=Y_{\rm in}\setminus Z.
\tag{102.1}
```

Use a generic bipartite incidence matrix $`A`$, with algebraically independent
nonzero entries on conflict edges. Generic matrix rank equals matching rank.

Let
```math
X^\circ=\{x\in X:N(x)\subseteq Z\},
\qquad
X^\partial=X\setminus X^\circ.
\tag{102.2}
```
Choose a basis $`I^\circ\subseteq X^\circ`$ for the restricted column matroid on
$`Z`$, and extend it to a basis $`B\subseteq X`$ of the full $`Z`$-row matroid.
Since the $`Z`$-rows have full rank,
```math
|B|=|Z|,
\qquad
A[Z,B]\text{ is invertible}.
\tag{102.3}
```

Put
```math
C=X\setminus B.
\tag{102.4}
```
The deep nonbasis columns
```math
C^\circ=C\cap X^\circ
\tag{102.5}
```
become loops after contracting $`B`$, because they lie in the span of
$`I^\circ`$ and have zero entries on $`O`$. Therefore
```math
|C^\circ|=d_{\rm int},
\tag{102.6}
```
and only
```math
C^\partial=C\cap X^\partial
\tag{102.7}
```
survives.

Define the Schur response matrix
```math
\boxed{
S
=
A[O,C^\partial]
-
A[O,B]A[Z,B]^{-1}A[Z,C^\partial].
}
\tag{102.8}
```

Block Gaussian elimination gives:

> **Theorem 102.1 (boundary-response rank theorem).**
> 

```math
> \boxed{
> \nu(G)=|Z|+\operatorname{rank}S,
> }
> \tag{102.9}
> 
```
> 

```math
> \boxed{
> d_{\rm sc}
> =
> d_{\rm int}
> +|C^\partial|
> -\operatorname{rank}S,
> }
> \tag{102.10}
> 
```
> 

```math
> \boxed{
> h(G)
> =
> |O|-\operatorname{rank}S.
> }
> \tag{102.11}
> 
```

Thus the entire quadratic matching problem contracts to an
$`O(D)`$-by-$`O(D)`$ exact boundary response matrix.

For $`I\subseteq O`$, $`J\subseteq C^\partial`$, and $`|I|=|J|=k`$,
the Schur determinant identity gives
```math
\boxed{
\det S[I,J]
=
\pm
\frac{
\det A[Z\cup I,B\cup J]
}{
\det A[Z,B]
}.
}
\tag{102.12}
```
Therefore a response minor is nonzero exactly when the corresponding induced
conflict system admits a matching saturating $`Z\cup I`$. Relative to a fixed
$`Z`$-perfect matching, the symmetric difference consists of vertex-disjoint
alternating $`I`$-to-$`J`$ paths together with possible alternating cycles.

This is an exact boundary linkage theorem. It does not imply a width-one-annulus
routing graph or an acyclic orientation.

## 102.1 Two-phase connectivity interpretation

After contracting all dimers, the two monomer phases are each independent. Let the
resulting matroid still be denoted $`M`$. Then
```math
r(M_+)=|M_+|,
\qquad
r(M_-)=|M_-|,
\tag{102.13}
```
and
```math
\boxed{
d_{\rm sc}
=
r(M_+)+r(M_-)-r(M_+\cup M_-).
}
\tag{102.14}
```

Thus all scaffold nullity is exactly the matroid connectivity between two
individually matchable crystalline phases.

Split
```math
M_\pm=M_{\pm,0}\sqcup M_{\pm,1}
\tag{102.15}
```
into deep and boundary monomers. For
```math
I(U;V\mid W)
=
r(U\cup W)+r(V\cup W)-r(W)-r(U\cup V\cup W),
\tag{102.16}
```
the matroid chain rule gives
```math
\boxed{
d_{\rm sc}
=
\kappa_{00}+\kappa_{01}+\kappa_{10}+\kappa_{11},
}
\tag{102.17}
```
where
```math
\begin{aligned}
\kappa_{00}&=I(M_{+,0};M_{-,0}),\\
\kappa_{01}&=I(M_{+,0};M_{-,1}\mid M_{-,0}),\\
\kappa_{10}&=I(M_{+,1};M_{-,0}\mid M_{+,0}),\\
\kappa_{11}&=I(M_{+,1};M_{-,1}\mid M_{+,0}\cup M_{-,0}).
\end{aligned}
\tag{102.18}
```
Every $`\kappa_{ij}`$ is a nonnegative integer. Adding one boundary element changes
connectivity by at most one, so
```math
\boxed{
d_{\rm sc}-\kappa_{00}
\le
|M_{+,1}|+|M_{-,1}|
\le12d+9.
}
\tag{102.19}
```

This is the overlap-safe replacement for spatially summing charge-12 circuits.

---

# 103. Source-specific contact-core and rattler-cage structure

The scaffold-only theorems above cannot close Target A. We now record the exact
information that genuinely remembers the triangle-free source minimizer.

The legitimate common representative is the hybrid representative of Theorem 12.4:
it contains, pointwise unchanged, the jammed nonisolated core $`K`$ of a
contact-minimal triangle-free minimizer, while every contact edge outside $`K`$ is a
bridge. Root-skeleton exactification and forest rattlerization act on those bridge
trees while keeping $`K`$ fixed.

This is the bridge that permits source-face and latent-forest statements to be used
together. The unrelated maximal-contact representative is not substituted here.

## 103.1 Exact facial-defect budget of the fixed core

Let the fixed contact-minimal core have

- $`v`$ vertices;
- $`e`$ unit-contact edges;
- $`c`$ connected components;
- $`q`$ diameter endpoints in the core.

Every bounded face has length at least four. Let $`m_F`$ be bounded face length and
let $`b_\infty`$ be the outer facial boundary-walk length, counting bridge
incidences with multiplicity.

Euler and face-edge incidence give
```math
\boxed{
b_\infty+\sum_{F\ {\rm bounded}}(m_F-4)
=
4v-2e-4c.
}
\tag{103.1}
```
The canonical low-degree/contact-core bound gives
```math
e\ge2(v-q),
\tag{103.2}
```
hence
```math
\boxed{
0\le
b_\infty+\sum_F(m_F-4)
\le4(q-c)
\le4\pi D.
}
\tag{103.3}
```

Thus the **total nonquadrilateral facial excess plus the entire outer boundary walk
is boundary-order**.

## 103.2 Strict-rattler cage inequality

Consider a simple convex equilateral bounded face $`F`$ of the fixed core with
$`m_F`$ unit edges, containing $`k_F`$ strict contact-isolated points of the hybrid
configuration. Finite Oler applied to the $`m_F`$ boundary vertices together with
the $`k_F`$ interior rattlers gives
```math
\boxed{
k_F
\le
\frac{
\operatorname{area}(F)-c_0(m_F-2)
}{a_0}.
}
\tag{103.4}
```

Consequently a unit rhombus carries no strict rattler, and
```math
\boxed{
k_F\ge1\Longrightarrow m_F\ge7.
}
\tag{103.5}
```

For the family $`\mathcal F_R`$ of such rattler-bearing bounded faces,
(103.3) and $`m_F\ge7`$ give
```math
\boxed{
\sum_{F\in\mathcal F_R}m_F
\le
\frac{28}{3}(q-c)
\le
\frac{28\pi}{3}D.
}
\tag{103.6}
```

If
```math
\rho_b=\sum_{F\in\mathcal F_R}k_F
\tag{103.7}
```
and $`M=\max_{F\in\mathcal F_R}m_F`$, isoperimetry gives
```math
k_F
<
\frac{m_F^2}{2\pi\sqrt3}.
\tag{103.8}
```
Therefore
```math
\boxed{
M
>
\frac{3\pi\sqrt3}{14(q-c)}\rho_b
\ge
\frac{3\sqrt3}{14}\frac{\rho_b}{D}.
}
\tag{103.9}
```

Hence a super-boundary bounded-face rattler population forces an actual source cage
whose unit-contact perimeter tends to infinity.

## 103.3 Long low-degree boundary run

Let $`\alpha_i`$ be the interior angles of a convex equilateral $`M`$-gon source
cage. Unit separation and triangle-freeness imply
```math
\alpha_i>\frac{\pi}{3}.
\tag{103.10}
```
At most five vertices can satisfy
```math
\alpha_i<\frac{2\pi}{3},
\tag{103.11}
```
because the exterior turns $`\pi-\alpha_i`$ sum to $`2\pi`$.

Therefore some consecutive run has length at least
```math
\boxed{
L_{120}\ge\frac{M-5}{5}.
}
\tag{103.12}
```
Every vertex on such a run has total contact degree at most four. Combining with
(103.9),
```math
\boxed{
L_{120}
>
\frac{3\sqrt3}{70}\frac{\rho_b}{D}-1.
}
\tag{103.13}
```

This is an actual ordered run in the source core. It is **not** automatically a
Schürmann loose edge or a Ferrers strip.

## 103.4 Latent forest confinement

The bridge forest survives inside the same hybrid representative. After
rattlerization, choose the deformation sufficiently small that every opened former
forest edge has length $`<\sqrt3`$.

> **Lemma 103.1 (unit-edge crossing barrier).**
> Let $`ab`$ be a unit segment. Suppose a segment $`pq`$ crosses the relative interior
> of $`ab`$, while
> 

```math
> |p-a|,|p-b|,|q-a|,|q-b|\ge1.
> 
```
> Then
> 

```math
> \boxed{|p-q|\ge\sqrt3.}
> \tag{103.14}
> 
```

### Proof

The closed $`\sqrt3/2`$-tube around the unit segment $`[a,b]`$ lies in
```math
\overline B(a,1)\cup\overline B(b,1).
\tag{103.15}
```
If the orthogonal projection lies inside $`[a,b]`$, one endpoint is horizontally at
distance at most $`1/2`$, giving squared distance at most
```math
\frac14+\frac34=1.
\tag{103.16}
```
Outside the segment, the nearest endpoint is still no farther than the distance to
the segment.

A crossing segment with endpoints outside both unit disks must traverse this tube
from one side to the other, a distance at least $`\sqrt3`$. $`\square`$

Hence no latent opened forest edge can cross a fixed unit edge of the core:
```math
\boxed{
\text{the latent forest is trapped face-by-face in the fixed core embedding.}
}
\tag{103.17}
```

This source-specific topological fact is not present in the independent scaffold.

## 103.5 Thermodynamic cage normal form

After same-diameter saturation, retain the original strict rattlers. The global
clearance theorem gives
```math
\sum_p\delta(p)=O(D),
\tag{103.18}
```
and the global deep Delaunay excess is $`O(D)`$.

For a regular rattler-bearing bounded face $`F`$, let

- $`L_F`$ be the total clearance of its retained rattlers;
- $`E_F`$ be the Delaunay excess of deep Delaunay triangles contained in the face;
- $`r_F`$ be the number of latent rooted-forest components represented in the face.

The total sums of $`m_F`$, $`L_F`$, $`E_F`$, and $`r_F`$ over the regular bounded-face
branch are $`O(D)`$. Therefore, if that branch contains
```math
\rho_b=\omega(D)
\tag{103.19}
```
retained rattlers, some face $`F`$ with $`k_F\to\infty`$ satisfies
```math
\boxed{
\frac{m_F+L_F+E_F+r_F}{k_F}\to0.
}
\tag{103.20}
```

Consequently
```math
m_F=o(k_F),
\qquad
L_F=o(k_F),
\qquad
E_F=o(k_F),
\qquad
r_F=o(k_F).
\tag{103.21}
```

The localized boundary-layer estimate gives only $`o(k_F)`$ rattlers within distance
one of $`\partial F`$. The degree-six nearest-neighbor argument therefore produces
```math
\boxed{
\frac{k_F}{24}-o(k_F)
}
\tag{103.22}
```
pairwise disjoint strong Gabriel/Delaunay edges inside the cage whose lengths are
$`1+o(1)`$. Since $`E_F=o(k_F)`$, both incident Delaunay triangles on all but
$`o(k_F)`$ of these edges approach one of the two equality wells
```math
\boxed{
\{1,1,1\},
\qquad
\{1,1,\sqrt3\}.
}
\tag{103.23}
```

Because $`r_F=o(k_F)`$, the cage also contains a latent rooted tree with unbounded
size; finite Oler forces its graph depth to diverge at least on a square-root scale.

This is a genuine source normal form, but it is not a contradiction. Near-equilateral
triangle-free configurations may approach the equality lattice without ever forming
an exact unit triangle.

The complementary source branches -- outer-face rattlers, pinched/non-simple pockets,
or topology not covered by the regular bounded-face hypothesis -- remain separate and
must not be silently absorbed into (103.20).

---

# 104. Source lattice transversal: almost all strict rattlers are conditionally independent

There is a second exact source theorem which limits what a closing argument can hope
to extract from Hall dependence alone.

Let $`A`$ be a same-diameter saturated triangle-free source minimizer of cardinality
$`N`$, hull $`K`$, and diameter $`D`$. Let
```math
N_+:=\max\{q:D(q)=D\},
\qquad
p:=N_+-N.
\tag{104.1}
```
The plateau theorem gives
```math
p<\frac{\pi D}{2}.
\tag{104.2}
```

Choose a generic triangular-lattice translate and put
```math
Y=(\Lambda+v)\cap\operatorname{int}K.
\tag{104.3}
```
Form the conflict graph on $`A\sqcup Y`$. Every independent set is a unit-separated
subset of $`K`$, hence has at most $`N_+`$ points. Therefore
```math
N+|Y|-\nu\le N_+,
\tag{104.4}
```
or
```math
\boxed{
\nu\ge|Y|-p.
}
\tag{104.5}
```

Let $`M_A`$ be the resulting source transversal matroid and
```math
\Delta_{\rm src}=N-|Y|.
\tag{104.6}
```
Then
```math
n(M_A):=N-r(M_A)
\le\Delta_{\rm src}+p.
\tag{104.7}
```

Choose the translate with more lattice points than its translation mean.
Finite Oler gives
```math
\Delta_{\rm src}
<
1+\frac{P}{2}
\le1+\frac{\pi D}{2}.
\tag{104.8}
```
Together with (104.2),
```math
\boxed{
n(M_A)<\pi D+1.
}
\tag{104.9}
```

Write
```math
A=B\sqcup R,
\tag{104.10}
```
where $`R`$ is the retained strict-rattler population. Define its conditional
transversal nullity over the source core:
```math
\eta_R
=
|R|-
\bigl(r_{M_A}(A)-r_{M_A}(B)\bigr).
\tag{104.11}
```
Conditional nullity is at most total nullity, so

> **Theorem 104.1 (source almost-independence).**
> 

```math
> \boxed{
> 0\le\eta_R<\pi D+1.
> }
> \tag{104.12}
> 
```
> Equivalently,
> 

```math
> \boxed{
> r_{M_A/B}(R)>\rho-\pi D-1.
> }
> \tag{104.13}
> 
```

Thus a super-boundary strict-rattler population is **not** forced to create
super-boundary Hall nullity in the source lattice transversal. All but $`O(D)`$
rattlers may be independent over the source core.

This is a no-go theorem for another tempting closure route.

---

# 105. Strained-monomer regression: boundary-order strain can destroy all exact contacts

The remaining Target A theorem must detect exact global diameter optimality, not
merely local crystallinity.

Choose one open degree-three monomer chamber for the $`+`$-orientation. Fix an
interior offset $`c`$ having positive distance from every chamber boundary and every
additional lattice conflict circle. For an $`L\times L`$ patch $`P_L`$ of lattice
indices, put
```math
p_z=z+c
\qquad(z\in P_L).
\tag{105.1}
```
Choose a patch center $`z_0`$ and define
```math
p'_z
=
z+c
+
\frac{\alpha}{L}(z-z_0),
\tag{105.2}
```
where $`\alpha>0`$ is a sufficiently small fixed constant.

The displacement from $`p_z`$ is $`O(\alpha)`$, uniformly in $`L`$. Choosing
$`\alpha`$ below the chamber margin keeps every $`p'_z`$ in the **same degree-three
monomer chamber** and therefore preserves the exact monomer scaffold combinatorics.

For every pair $`z,w`$,
```math
p'_z-p'_w
=
\left(1+\frac{\alpha}{L}\right)(z-w).
\tag{105.3}
```
In particular every former unit lattice-neighbor distance becomes
```math
\boxed{
1+\frac{\alpha}{L}>1.
}
\tag{105.4}
```
All other separations increase as well. Hence the entire patch is contact-free and
therefore triangle-free.

There are $`\Theta(L^2)`$ points, while the total nearest-neighbor clearance is
```math
\boxed{
\Theta(L^2)\frac{\alpha}{L}
=
\Theta(L).
}
\tag{105.5}
```

> **Regression 105.1 (distributed infinitesimal strain).**
> A $`D^2`$-scale triangle-free strict-rattler phase can retain exact zero-charge
> monomer scaffold combinatorics while paying only boundary-order total clearance.

The construction is not asserted to be globally diameter-optimal. Its purpose is to
kill the inference that triangle-freeness, strict-rattler status, near-triangular
bulk, or monomer phase purity automatically costs positive bulk defect.

Any closing theorem must use the global diameter boundary or an equivalent exact
optimality invariant.

---

# 106. Authoritative v1.5.0 Target A frontier

All audited Target A reductions now point to the same one-integer obstruction.

The original exact equivalence remains
```math
\boxed{
h(G)-j=d_{\rm sc}-\Delta_\Lambda.
}
\tag{106.1}
```
Thus Target A closes exactly when
```math
\boxed{d_{\rm sc}\ge\Delta_\Lambda}
\tag{106.2}
```
or equivalently
```math
\boxed{h(G)\ge j.}
\tag{106.3}
```

The preferred structural forms are now much sharper.

## 106.1 Nullity-zero residual form

The full fixed-basis tight core can be contracted, leaving a fully matchable residual
with
```math
\boxed{
g=\Delta_\Lambda-d_{\rm sc}.
}
\tag{106.4}
```
A survivor has $`g\ge1`$.

A sufficient closing theorem is therefore:

> **Nullity-zero global phase-rigidity theorem.**
> A nullity-zero residual obtained by the globally derived Target A scaffold cannot
> have $`g\ge1`$; global optimality forces $`g\le0`$ or a strict diameter decrease.

This is not a statement about arbitrary nullity-zero monomer--dimer complexes.

## 106.2 Phase-gammoid form

After contracting all dimers and either monomer orientation,
```math
\boxed{
d_{\rm sc}=m_- -\lambda_+=m_+-\lambda_-.
}
\tag{106.5}
```
The six anchor presentations give exact absolute-contour formulas. A sufficient
closing theorem is
```math
\boxed{
m_- -\lambda_+\ge\Delta_\Lambda.
}
\tag{106.6}
```

Planarity and the six height orders alone do not imply this.

## 106.3 Plateau-boundary form

After right-endpoint terminalization of the smaller optimum,
```math
\boxed{
d_{\rm sc}
=
d_{\rm int}+s_\partial-\lambda_\partial.
}
\tag{106.7}
```
Thus, if $`d_{\rm int}<\Delta_\Lambda`$, the exact boundary lemma is
```math
\boxed{
s_\partial-\lambda_\partial
\ge
\Delta_\Lambda-d_{\rm int}.
}
\tag{106.8}
```

## 106.4 Phase-pure boundary-minor form

For either phase,
```math
\boxed{
d_{\rm sc}
=
d_{\rm int}
+\theta_+
+d_{\partial,-}^{(+)}
}
\tag{106.9}
```
and symmetrically. The exact required inequality is
```math
\boxed{
\theta_+
+d_{\partial,-}^{(+)}
\ge
\Delta_\Lambda-d_{\rm int}.
}
\tag{106.10}
```

The quotient has only $`O(D)`$ ground elements and only one orientation of boundary
monomers as possibly nonloop residual elements.

## 106.5 Boundary-response form -- preferred endpoint

The Schur response is the cleanest exact endpoint:
```math
\boxed{
d_{\rm sc}
=
d_{\rm int}+|C^\partial|-\operatorname{rank}S.
}
\tag{106.11}
```
Therefore Target A is exactly:

> **Target A v1.5.0 (source-specific boundary-response theorem).**
> For the plateau-terminalized scaffold extracted from a genuine super-boundary
> triangle-free global minimizer,
> 

```math
> \boxed{
> \operatorname{rank}S
> \le
> d_{\rm int}+|C^\partial|-\Delta_\Lambda.
> }
> \tag{106.12}
> 
```

Equivalently,
```math
\boxed{
|O|-\operatorname{rank}S\ge j.
}
\tag{106.13}
```

## 106.6 Why the theorem must be source-specific

The independent smaller optimum and scaffold exist for arbitrary pairs of diameter
optima. In a surviving Target A configuration, global $`N`$-optimality itself gives
```math
d_{\rm sc}\le\Delta_\Lambda-1.
\tag{106.14}
```
Therefore no theorem depending only on the smaller optimum, plateau saturation,
Delaunay wells, phase contraction, boundary planarity, or Schur algebra can prove
(106.12).

The extra input must come from the original triangle-free source minimizer.

The source information now available is:

1. a super-boundary population of mutually independent strict rattlers;
2. an unchanged jammed contact-minimal backbone inside the hybrid representative;
3. exact facial-defect budget (103.3);
4. strict-rattler cage capacity (103.4);
5. latent-forest face confinement (103.17);
6. thermodynamic near-triangular cage structure in the regular bounded-face branch;
7. source lattice almost-independence (104.12);
8. the global KKT contact/diameter equilibrium stress and exact diameter boundary.

Items 1--7 still do not close the theorem. Regression 105.1 shows why purely local
bulk cost cannot.

## 106.7 The actual missing mechanism

The best current formulation is:

> **Boundary-to-bulk first-variation theorem.**
> Suppose a triangle-free global minimizer has the Target A source structure and a
> super-boundary strict-rattler population. The bulk may realize an
> $`O(1/D)`$-scale expansive strain with only $`O(D)`$ total clearance/area defect.
> Prove that the exact minimum-diameter boundary cannot support such a strain:
> either
>
> 1. there is a strict same-cardinality diameter-decreasing deformation; or
> 2. the source structure forces at least
>    $`\Delta_\Lambda`$ units of scaffold nullity, equivalently the Schur-response
>    rank loss (106.12).

This theorem is not proved.

A closing proof should now focus on coupling the source strain to the exact active
diameter/KKT boundary, or on converting source-specific structure into a vanishing
family of response minors. It should not return to local phase-charge counting.

---

# 107. Authoritative v1.5.0 Target B frontier

No post-v1.4.1 result in this continuation changes the pure Target B endpoint.

The required exact theorem remains
```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha,
}
\tag{107.1}
```
followed by exact topology-corrected transport.

The component classification remains:

1. $`s_C=0`$: atomic one-edge unit segment, strictly forward for every active bar;
2. $`s_C=1`$, tree: exactly two directions, at most nine trains, with residual
   active-bar-average obstruction $`\mathcal A_{1\rm t}`$;
3. $`s_C=1`$, cyclic: exactly two directions and, under the audited cyclic order
   hypotheses, the legitimate Ferrers/two-family class;
4. $`s_C=2`$: genuine two-dimensional turning component.

The next tree-specific theorem remains an exact charge of
```math
\operatorname{rank}\mathcal A_{1\rm t}
\tag{107.2}
```
to terminal coforest/cycle data or the existing $`I+r`$ budget.

No uncontrolled $`O(D)`$ loss is acceptable in the final topology transport.

---

# 108. v1.5.0 regressions, rejected shortcuts, and exact status

All earlier regressions remain binding. Add the following v1.5.0 tests.

1. **Fixed-basis overlap is signed-additive, not spatially additive.** Fundamental
   circuits relative to one maximum basis have exact signed deficiency additivity,
   but their supports may overlap almost completely.
2. **Arbitrary phase contraction remains invalid.** Only the exact fixed-basis and
   phase-selective contractions proved above may be used without further rank proof.
3. **Residual optimality is not inherited.** A residual after contraction/deletion is
   not automatically a global optimum for its new cardinality.
4. **Boundary terminals do not imply boundary routing.** Alternating paths may still
   traverse the quadratic bulk.
5. **Planar annular networks can have full linkage rank.** Planarity alone cannot
   prove the boundary deficit.
6. **Near-equilateral equality remains live.** Triangle-free configurations may
   converge to the $`\{1,1,1\}`$ well.
7. **Strained monomer patch.** A $`D^2`$-scale exact monomer scaffold phase can be
   made contact-free and triangle-free with only $`O(D)`$ total clearance.
8. **Source rattlers need not create bulk Hall nullity.** Their conditional source
   transversal nullity can be only $`O(D)`$.
9. **Long obtuse source runs are not automatically Schürmann loose edges.**
10. **Contact-minimal/maximal-contact normal forms are not interchangeable.** Use the
    hybrid theorem when transporting the unchanged jammed backbone into the flexible
    representative.

The following shortcuts are explicitly rejected unless separately proved:

- a fixed positive defect per triangle-free monomer cell;
- a fixed positive defect per strict rattler;
- asymptotic convergence to triangular lattice as a contradiction;
- use of phase-anchor DAGs as though the boundary-terminal matching had the same
  anchor orientation automatically;
- a width-one-annulus gammoid without a rank-preserving terminalization theorem;
- a claim that all response routing lies near $`\partial K`$;
- recursively applying optimum-only theorems to contracted residual configurations;
- treating the source and independent smaller optimum as coordinate-identified;
- replacing exact Schur rank loss by an $`O(D)`$ separator estimate; or
- invoking Schürmann without an actual polygon satisfying the precise loose-edge and
  obtuse-vertex hypotheses.

## 108.1 Exact status

**LEVEL I STATUS: STILL OPEN.**

Target A has been reduced to the source-specific boundary-response/first-variation
theorem (106.12). The quadratic scaffold bulk, dimer population, one complete
monomer phase, deep matching obstruction, and most circuit-overlap ambiguity can all
be removed exactly. The remaining rank object is boundary-order.

Target B remains (107.1) plus exact topology transport.

A Level I affirmative proof still requires closing **both** Target A and Target B.

## 108.2 Version history through v1.5.0

- **v1.0.0:** global KKT/stress, almost-rhombic and hybrid normal forms,
  translated-lattice and higher-order blocker machinery;
- **v1.1.0:** minimal-face harmonic transport, terminal direction network, exact
  plateau theorem;
- **v1.2.0:** rooted-forest exactification, affine triangle-factor exclusion,
  rattlerization, saturation, terminal Minkowski splitting;
- **v1.3.0:** compatible collar, clearance budget, strong Delaunay matching,
  two-well theorem, exact Hall scaffold;
- **v1.4.0:** exact monomer--dimer blocker complex and Target B component-rotation
  refinements;
- **v1.4.1:** dual Hall/lattice deficit, exact phase charge and peeling,
  transversal-matroid circuits, bounded `s_C=1` trees;
- **v1.5.0:** fixed-basis tight-core contraction, phase-selective exact contraction,
  six planar gammoid presentations, plateau interior terminalization,
  phase-pure $`O(D)`$ boundary minors, quantized Hall-core convexification,
  exact boundary Schur response, source facial/forest localization,
  source transversal almost-independence, and the distributed-strain regression.

`erdos_problem_99_1.5.0.md` was the sole canonical theorem-state file at the v1.5.0
stage. Sections 109 onward and the v1.5.1 audit policy supersede its corrected frontier.
---

# 109. v1.5.1 audit corrections, restored identities, and source-localization repair

This section is the authoritative audit patch to Sections 97--108.  It records the
results of a full post-build audit of v1.5.0.  Unless explicitly corrected below, the
mathematics of Sections 97--102 survives unchanged.  The corrections are concentrated
in the source-localization layer of Section 103, one overstrong phrase in Regression
105.1, and two exact supporting identities that v1.5.0 inadvertently omitted.

## 109.1 Audit classification of Sections 97--102

The following v1.5.0 results survive re-derivation without correction:

1. The fixed-basis tight-union theorem (97.3)--(97.14).
2. The full tight-core contraction and exact residual gap
   ```math
   g=\Delta_\Lambda-d_{\rm sc}.
   
   ```
3. The boundary-order estimates (97.28)--(97.32).
4. Phase-selective independence and exact nullity preservation (98.7)--(98.14).
5. The six phase-anchor layered DAG presentations and the directed Menger/contour
   formulas (98.17)--(98.21).
6. Right-endpoint plateau saturation, the exact interior matching
   ```math
   \nu(G_0)=|Z|,
   
   ```
   and the deep-nullity/boundary-linkage split (99.14)--(99.26).
7. The two-sided plateau endpoint normalization (99.27)--(99.33).
8. The phase-pure boundary-minor decomposition (100.13)--(100.15).
9. The exterior degree/interface theorem (100.16)--(100.23).
10. The quantized convexification-gap theorem and the circuit bounds
    ```math
    m_3\ge14,\qquad m_+\ge6,\qquad m_-\ge6.
    
    ```
11. The Schur response theorem (102.9)--(102.12) and the two-phase matroid
    connectivity interpretation (102.14)--(102.19).

The generic incidence matrix in Section 102 is understood over the rational-function
field generated by algebraically independent nonzero edge variables.  With that
convention, generic matrix rank equals transversal-matroid rank, and a Schur minor is
nonzero exactly when the corresponding square conflict submatrix has a perfect
matching.

## 109.2 Explicit outer-terminal population bound

Section 99 correctly states that the physical terminal populations are boundary-order,
but v1.5.0 omitted the explicit proof for the outer lattice set
```math
O=(\Lambda+v)\cap\bigl(\operatorname{int}(K+\mathbb B)\setminus K\bigr).
```
Restore it as follows.

Let
```math
r_\Lambda=\frac1{\sqrt3}.
```
The triangular-lattice Voronoi cells centered at the points of $`O`$ are disjoint,
have area $`a_0`$, lie in $`K+(1+r_\Lambda)\mathbb B`$, and are disjoint from
$`K\ominus r_\Lambda\mathbb B`$.  The elementary inner-tube inequality for a convex
body gives
```math
\operatorname{area}(K\ominus r\mathbb B)
\ge
\operatorname{area}(K)-rP;
```
if the right side is negative this is simply trivial.  Hence
```math
\begin{aligned}
a_0|O|
&\le
\operatorname{area}(K+(1+r_\Lambda)\mathbb B)
-
\operatorname{area}(K\ominus r_\Lambda\mathbb B)\\
&\le
(1+2r_\Lambda)P+\pi(1+r_\Lambda)^2.
\end{aligned}
```
Therefore
```math
\boxed{
|O|
\le
\frac{(1+2/\sqrt3)P+\pi(1+1/\sqrt3)^2}{a_0}
\le
7.816389\ldots\, d+9.025589\ldots
<12d+10.
}
\tag{109.1}
```
Thus the Schur response really is $`O(D)`$-by-$`O(D)`$, with an explicit row bound
rather than only a qualitative assertion.

## 109.3 Restored general biphasic Hall-core bounds

The stronger circuit theorem in Section 101 supersedes the old circuit constants, but
v1.5.0 inadvertently dropped a useful exact statement for arbitrary connected positive
Hall cores.

Let such a core have deficiency $`r>0`$, $`q`$ holes, boundary length $`b`$, and
monomer counts $`m_+,m_-`$.  Then
```math
m_++m_-=b+2r+2-2q,
```
while every boundary component has at least three elementary lattice edges, so
```math
b\ge3(q+1).
```
The orientation side count gives
```math
3(m_+-m_-)=b_+-b_-,
\qquad
|m_+-m_-|\le\frac b3.
```
Consequently
```math
\boxed{m_+\ge r+2,\qquad m_-\ge r+2}
\tag{109.2}
```
and
```math
\boxed{m_3=m_++m_-\ge2r+q+5.}
\tag{109.3}
```
These are exact integer bounds and require no circuit decomposition.

## 109.4 Restored two-sided finite-packing-defect identity

The continuation prompt in v1.5.0 retained two-sided plateau defect transfer as a
research route but the canonical state omitted the exact scalar identity that makes
that route meaningful.

Use the two-sided normalization of Section 99.4.  Thus
```math
N_-=\min\{q:D(q)=D\},
\qquad
m_+=\max\{q:D(q)=d\},
```
```math
\rho^\dagger=N_--m_+,
\qquad
t=\frac{D-d}{2},
```
and let $`K`$ be an $`m_+`$-point optimum of diameter $`d`$, with perimeter $`P`$ and
perimeter deficit
```math
\varepsilon^*=\pi d-P.
```
Recall
```math
E(n)=\frac{D(n)^2}{c}+\frac{\pi D(n)}2-(n-1).
```
Then subtraction of the two exact cardinality identities gives
```math
\boxed{
\rho^\dagger
=
\frac{D^2-d^2}{c}
+\pi t
+E(m_+)-E(N_-).
}
\tag{109.4}
```

Let
```math
\Omega=(K+t\mathbb B)\setminus(K+\mathbb B)
```
and define the translation-average residual after the safe collar by
```math
J_{\rm av}:=\rho^\dagger-\frac{\operatorname{area}(\Omega)}{a_0}.
```
The normalized area of the physical unit exterior band is
```math
B_{\rm av}:=\frac{P+\pi}{a_0}.
```
Steiner's formula gives
```math
\frac{\operatorname{area}(\Omega)}{a_0}
=
\frac{D^2-d^2}{c}
-
\frac{\pi(d+1)+\varepsilon^*(t-1)}{a_0}.
```
Combining with (109.4) yields the exact transfer identity
```math
\boxed{
J_{\rm av}-B_{\rm av}
=
\pi t
+\frac{\varepsilon^*t}{a_0}
+E(m_+)-E(N_-).
}
\tag{109.5}
```
Moreover, if
```math
p_N=N-N_-,\qquad p_m=m_+-m,
```
then
```math
\boxed{
E(m_+)-E(N_-)
=
E(m)-E(N)-p_m-p_N.
}
\tag{109.6}
```
The endpoint normalization therefore spends the full available plateau length
$`p_N+p_m`$ against the finite-packing defect transfer.  The sign of (109.5) remains
uncontrolled; this is an identity, not a Target A closure.

## 109.5 Correction to latent-forest confinement

Lemma 103.1 is valid, but the sentence following it was too strong.  A one-root tree
whose fixed root is a core vertex can have different branches entering different faces
incident to that root without any edge crossing a core edge.  The correct theorem is
branchwise.

> **Lemma 109.1 (branchwise core-face confinement).**
> Choose the forest rattlerization sufficiently small that every opened former forest
> edge has length less than $`\sqrt3`$.  No such edge crosses the relative interior of a
> fixed unit core edge.  Consequently every moving branch obtained after deleting its
> fixed core root is contained in one complementary face of the fixed core.  A one-root
> component whose root does not lie on the core is contained in one face.  A component
> rooted at a core vertex may meet several incident faces, but at most five.

The crossing estimate remains
```math
|pq|\ge\sqrt3
```
for an edge $`pq`$ crossing a unit core edge $`ab`$ while all four endpoint distances
to $`a,b`$ are at least one.  A rigorous short proof is: if $`x=pq\cap ab`$, then the
closed disk $`\overline B(x,\sqrt3/2)`$ is contained in the $`\sqrt3/2`$-stadium of
$`[a,b]`$, and that stadium is contained in
$`\overline B(a,1)\cup\overline B(b,1)`$.  Since $`p,q`$ lie outside both unit disks and
$`x\in[p,q]`$, the line through $`p,q`$ must traverse a chord of
$`\overline B(x,\sqrt3/2)`$ of length $`\sqrt3`$; hence $`|pq|\ge\sqrt3`$.

The post-root-skeleton forest has exactly
```math
r+b
```
one-root components, because the original $`c`$ components are cut along
$`r+b-c`$ skeleton paths.  Since
```math
b\le r-c,
\qquad
r\le\pi D,
```
```math
\boxed{
\#\{\text{one-root components}\}
=r+b
\le2r-c
\le2\pi D.
}
\tag{109.7}
```
Every component not rooted on the core contributes to one face; a core-rooted
component contributes to at most five face incidences.  Therefore the total number of
regular bounded-face component incidences is at most
```math
\boxed{10\pi D.}
\tag{109.8}
```
This supplies the previously implicit $`O(D)`$ justification for the $`r_F`$ term in
Section 103.5.

## 109.6 Corrected thermodynamic-cage theorem

Retain only the branch in which a super-boundary number of the **forest-rattlerized
vertices** lies in simple convex bounded faces of the fixed core.  For such a face
$`F`$, let

- $`k_F`$ be its number of retained forest rattlers;
- $`m_F`$ its unit-contact boundary length;
- $`L_F`$ the sum of their nearest-neighbor clearances after same-diameter saturation;
- $`E_F`$ the deep Delaunay excess of triangles contained in $`F`$, in a Delaunay
  triangulation containing the fixed unit core edges; and
- $`r_F`$ the number of one-root component--face incidences in $`F`$.

The fixed unit core edges are strong Gabriel edges, so they may be included
simultaneously in the Delaunay triangulation and the triangulation respects every
simple core-face boundary.  Equations (103.6), the global clearance/excess budgets,
and (109.8) give
```math
\sum_F(m_F+L_F+E_F+r_F)=O(D).
```
If
```math
\sum_F k_F=\omega(D),
```
a weighted-average argument gives a face with $`k_F\to\infty`$ and
```math
\boxed{
\frac{m_F+L_F+E_F+r_F}{k_F}\to0.
}
\tag{109.9}
```

To localize the nearest-neighbor argument correctly, choose
```math
\epsilon_F
=
\max\left\{
\sqrt{L_F/k_F},\ k_F^{-1/4}
\right\}
\longrightarrow0.
```
Only $`o(k_F)`$ rattlers have clearance greater than $`\epsilon_F`$.  The disjoint
radius-$`1/2`$ disks around rattlers within distance $`1+\epsilon_F`$ of
$`\partial F`$ lie in a radius $`3/2+\epsilon_F`$ tube around the polygonal boundary,
so their number is
```math
O(m_F)+O(1)=o(k_F).
```
Every remaining selected rattler has a nearest neighbor at distance
$`\le1+\epsilon_F`$ that still lies inside $`F`$.  The degree-six/maximal-matching
argument therefore gives
```math
\boxed{
|M_F|\ge\frac{k_F}{24}-o(k_F).
}
\tag{109.10}
```
All these matching edges are strong Gabriel edges and their two incident Delaunay
triangles lie in $`F`$.  Since $`E_F=o(k_F)`$, all but $`o(k_F)`$ of them have both
incident triangles converging to
```math
\{1,1,1\}
\qquad\text{or}\qquad
\{1,1,\sqrt3\}.
```
Finally, (109.9) and the fact that the $`k_F`$ selected vertices are forest rattlers
imply that one represented forest branch/tree has unbounded population.  Because every
latent edge has uniformly bounded length, finite Oler in a disk gives graph depth
$`\Omega(\sqrt s)`$ for a tree of $`s`$ moving vertices.

Thus the thermodynamic-cage normal form survives, but only with the corrected
branchwise confinement and component-incidence bookkeeping above.  Outer-face,
non-simple, and pinched/topological source branches remain separate.

## 109.7 Correction to Regression 105.1

The strained-monomer construction itself is valid: the finite patch is contact-free,
triangle-free, remains in the same monomer chambers, and has only boundary-order total
nearest-neighbor clearance.  The phrase "strict-rattler phase" in (105.1) was too
strong if the patch is considered by itself, because some patch points realize its own
diameter.

The safe canonical wording is:

> **Regression 109.2 (distributed infinitesimal monomer strain).**  A
> $`\Theta(L^2)`$-point triangle-free contact-free patch can retain the exact local
> same-orientation monomer scaffold combinatorics while paying only $`\Theta(L)`$ total
> nearest-neighbor clearance.  If desired, it can be placed strictly inside a larger
> fixed frame of diameter $`\Theta(L)`$, making the patch vertices non-diametral, but
> no global optimality is claimed.

Also, "zero-charge monomer phase" refers to the local interior incidence phase
$`(p,q)=(3,0)`$; a finite patch still has boundary charge of boundary order.

---

# 110. v1.5.1 exact status and audit verdict

**LEVEL I STATUS: STILL OPEN.**

The full audit finds **no fatal mathematical error in the principal v1.5 Target A
reductions**.  In particular, the fixed-basis contraction, phase-selective contraction,
six DAG/contour forms, plateau interior matching, phase-pure boundary minor, quantized
Hall-core theorem, and boundary Schur response all survive.

The v1.5.0 defects were:

1. an overstrong face-by-face statement for a core-rooted latent forest;
2. an omitted proof/bound for the $`O(D)`$ outer row population of the Schur response;
3. an implicit rather than proved $`O(D)`$ component-incidence budget in the
   thermodynamic-cage theorem;
4. a boundary-strip localization step that needed thickness $`1+\epsilon_F`$, not
   exactly one;
5. an overstrong use of the phrase "strict-rattler phase" for the standalone strained
   monomer regression; and
6. omission of the exact two-sided finite-packing-defect identity (109.5) and the
   general biphasic core bounds (109.2)--(109.3).

All six are repaired in Section 109 without changing the authoritative Target A
endpoint:
```math
\boxed{
\operatorname{rank}S
\le
d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{110.1}
```
Equivalently,
```math
\boxed{d_{\rm sc}\ge\Delta_\Lambda}
\qquad\Longleftrightarrow\qquad
\boxed{h(G)\ge j}.
\tag{110.2}
```

The best current research target remains the exact boundary-to-bulk first-variation /
source-to-response theorem.  The restored scalar identity (109.5) should be used when
pursuing the two-sided plateau-defect route.  Purely local monomer cost, asymptotic
triangular-lattice convergence, planar separator estimates, and unqualified
face-by-face forest confinement remain invalid shortcuts.

Target B remains unchanged:
```math
\operatorname{rank}\overline{\mathcal B}_\xi+I+r\le T-q-r_\alpha,
```
followed by exact topology-corrected transport.

`erdos_problem_99_1.5.1.md` is the sole canonical theorem-state file for subsequent
runs.


---
