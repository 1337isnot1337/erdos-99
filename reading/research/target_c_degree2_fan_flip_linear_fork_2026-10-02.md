> Generated reading edition · [exact source](../../research/target_c_degree2_fan_flip_linear_fork_2026-10-02.md) · source SHA-256 `21e8e1452d3e3a9bb205de27a924b1648eb530f7ec311d3c5bb6dc8e35aa3347`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C: exact fan flips force a linear diameter-inactive population

**Date:** 2026-10-02  
**Base main:** b46222601c670ba1bfd8ca17842c0cb5b71a54f8  
**Status:** proof-only source-level reduction. Level I and C-II remain open.

## 1. Statement

Work in the current low-outer-walk, square-root actual-diameter-matching branch. Let
```math
\nu(H)\le K_\nu\sqrt D,\qquad x_B\le K_x\sqrt D
\tag{1}
```
for fixed constants $`K_\nu,K_x`$, and assume $`D`$ is sufficiently large.

The current global fan theorem gives exact same-carrier good fan runs with
```math
I\ge \lceil D\rceil-(4K_\nu+2K_x)\sqrt D
\tag{2}
```
internal fan vertices.

Every internal fan vertex has contact degree two or three. Let $`T`$ and $`U`$ be the
two populations, so $`I=T+U`$.

Then the source contains at least
```math
\boxed{{I\over12}}
\tag{3}
```
distinct diameter-inactive vertices. In particular,
```math
\boxed{
\#\{z:\deg_H(z)=0\}
\ge
(1/12-o(1))D.
}
\tag{4}
```

More precisely, one of two stronger alternatives holds.

### A. Degree-three fan leaves dominate

There are at least
```math
\boxed{{I\over10}}
\tag{5}
```
distinct diameter-inactive positive-contact vertices $`z`$. Each is joined by an
actual unit contact to a loaded diameter leaf and lies strictly inside the local
carrier/fan triangle.

### B. Degree-two fan leaves dominate

There are at least
```math
\boxed{{I\over2}}
\tag{6}
```
distinct previously strict source pairs $`py`$ satisfying
```math
\boxed{
1<|p-y|\le1+{1\over D},
}
\tag{7}
```
where $`p`$ is a loaded diameter leaf and
```math
\boxed{\deg_H(y)=0.}
\tag{8}
```

For $`D\ge9`$, these pairs contain a vertex-disjoint matching of size at least
```math
\boxed{{I\over22}.}
\tag{9}
```

The inactive endpoints $`y`$ themselves are at least
```math
\boxed{{I\over12}}
\tag{10}
```
distinct.

Thus the preceding square-root port/stress-flat fork collapses to a linear
diameter-inactive source population. In the degree-two-heavy case there is in
addition a linear vertex-disjoint inverse-$`D`$ almost-unit matching based at loaded
fan leaves.

No computation is used.

## 2. Exact reflection of one degree-two fan leaf

Let
```math
p_-,p,p_+
```
be three consecutive vertices of one good same-carrier fan, with common diameter
carrier $`a`$. Thus
```math
|p-a|=|p_--a|=|p_+-a|=D
\tag{11}
```
and
```math
|p-p_-|=|p-p_+|=1.
\tag{12}
```

Assume $`p`$ is an internal contact-degree-two fan vertex. Then its only positive
contacts are $`pp_-`$ and $`pp_+`$, and its full actual-diameter degree is one, with
unique diameter edge $`pa`$.

Put
```math
u={p-a\over D},
\qquad
\varepsilon={1\over2D},
\qquad
\tau=\sqrt{1-\varepsilon^2}.
\tag{13}
```

Choose a unit tangent $`t`$ so that
```math
p_-=a+(D-\varepsilon)u-\tau t,
\qquad
p_+=a+(D-\varepsilon)u+\tau t,
\tag{14}
```
while
```math
p=a+Du.
\tag{15}
```

The line through $`p_-,p_+`$ is
```math
a+(D-\varepsilon)u+\mathbb Rt.
```
Reflect $`p`$ across this line. The reflected point is
```math
\boxed{
p':=a+(D-2\varepsilon)u
=a+\left(D-{1\over D}\right)u.
}
\tag{16}
```

Hence
```math
\boxed{|p'-p|={1\over D}.}
\tag{17}
```

The two old contacts are preserved exactly:
```math
p'-p_-=-\varepsilon u+\tau t,
\qquad
p'-p_+=-\varepsilon u-\tau t,
```
so
```math
\boxed{
|p'-p_-|=|p'-p_+|=1.
}
\tag{18}
```

The unique old diameter at $`p`$ strictly shortens:
```math
\boxed{
|p'-a|=D-{1\over D}<D.
}
\tag{19}
```

Thus the replacement
```math
p\mapsto p'
\tag{20}
```
is an exact finite move of amplitude $`1/D`$ which preserves every old contact
incident with $`p`$, preserves every old contact not incident with $`p`$, and strictly
shortens the only old actual diameter incident with $`p`$.

## 3. The fan flip is globally nonexpansive

Fix any source point $`y\ne p`$, and write
```math
r:=p-y.
```
Since $`a`$ is a diameter partner of $`p`$,
```math
p-a=Du.
```
The global diameter bound applied to $`y,a`$ gives
```math
|y-a|^2
=
|Du-r|^2
\le D^2.
```
Therefore
```math
\boxed{
u\cdot r\ge {|r|^2\over2D}.
}
\tag{21}
```

Now
```math
p'-y=r-{u\over D},
```
so
```math
\begin{aligned}
|p'-y|^2
&=
|r|^2-{2\over D}u\cdot r+{1\over D^2}\\
&\le
|r|^2-{|r|^2\over D^2}+{1\over D^2}.
\end{aligned}
```
Thus
```math
\boxed{
|p'-y|^2
\le
|p-y|^2-
{|p-y|^2-1\over D^2}.
}
\tag{22}
```

Every source distance is at least one. Hence
```math
\boxed{|p'-y|\le|p-y|}
\tag{23}
```
for every $`y`$, and the inequality is strict whenever $`|p-y|>1`$.

For the two old contact neighbors $`p_\pm`$, exact equality is already known from
(18).

Therefore no previously strict pair can become a new diameter pair. Every previously
strict pair involving $`p`$ strictly shortens. The only possible obstruction to the
exact flip is the lower unit-separation constraint.

## 4. Canonical minimality forces an inverse-$`D`$ almost-unit blocker

Suppose that after the exact flip every previously strict noncontact $`py`$ still has
```math
|p'-y|>1.
\tag{24}
```

Then all source pairs remain unit-separated. The old contacts $`pp_-`$ and $`pp_+`$
are preserved exactly, all other old contacts are unchanged, and by (24) no new
contact is created. Hence the contact count is unchanged.

By Section 3, no source distance increases. The unique old diameter $`pa`$ strictly
shortens by (19), while every old diameter not incident with $`p`$ is unchanged.

If another old diameter remains, the moved source is another diameter-$`D`$ global
minimizer with the same contact count and strictly fewer actual diameter pairs. This
contradicts the canonical contact-minimal, then diameter-pair-minimal normalization.

If no old diameter remains, the moved source has diameter strictly below $`D`$,
contradicting global minimum diameter.

Therefore (24) is impossible. For every degree-two internal fan vertex $`p`$, there
is a previously strict noncontact $`py`$ such that
```math
|p'-y|\le1.
\tag{25}
```

By (17),
```math
|p-y|
\le
|p'-y|+|p'-p|
\le1+{1\over D}.
```
Since $`py`$ was previously a strict noncontact,
```math
\boxed{
1<|p-y|\le1+{1\over D}.
}
\tag{26}
```

Call such a point $`y`$ a **flip blocker** for $`p`$.

## 5. Every flip blocker is strictly inside the carrier/fan triangle

The flip blocker is not merely an almost-unit point. It is forced to be a
diameter-inactive interior source point.

Write
```math
y=a+Xu+Yt.
\tag{27}
```

The three relevant fan points are
```math
p=a+Du,
\qquad
p'=a+(D-2\varepsilon)u,
\qquad
p_\pm=a+(D-\varepsilon)u\pm\tau t.
\tag{28}
```

Because $`y`$ is an original source point,
```math
|y-p|>1,
\qquad
|y-p_\pm|\ge1,
\tag{29}
```
while the blocking property is
```math
|y-p'|\le1.
\tag{30}
```

Thus $`y`$ is no farther from $`p'`$ than from any of $`p,p_-,p_+`$.

### 5.1 Base half-plane

Comparing $`p'`$ with $`p`$, which lie on the same $`u`$-axis, gives
```math
|y-p'|<|y-p|
\quad\Longrightarrow\quad
\boxed{
X<D-\varepsilon.
}
\tag{31}
```

Also (30) gives
```math
X\ge D-2\varepsilon-1.
\tag{32}
```
For $`D\ge4`$, the right side is positive.

### 5.2 Side half-planes

From
```math
|y-p_\pm|^2\ge |y-p'|^2
```
one obtains exactly
```math
\varepsilon X+\tau Y\le1-2\varepsilon^2,
```
and
```math
\varepsilon X-\tau Y\le1-2\varepsilon^2.
```
Hence
```math
\boxed{
|Y|
\le
{1-2\varepsilon^2-\varepsilon X\over\tau}.
}
\tag{33}
```

The triangle
```math
\Delta:=
\operatorname{conv}\{a,p_-,p_+\}
```
has coordinate description
```math
\Delta
=
\left\{
a+xu+yt:
0\le x\le D-\varepsilon,\quad
|y|\le{\tau x\over D-\varepsilon}
\right\}.
\tag{34}
```

It remains to compare the right side of (33) with the side of this triangle.

Put
```math
G(X):=
(1-2\varepsilon^2-\varepsilon X)(D-\varepsilon)
-\tau^2X.
\tag{35}
```
The coefficient of $`X`$ is negative, so $`G`$ is strictly decreasing.

At the lower bound
```math
X_0:=D-2\varepsilon-1,
```
using $`D=1/(2\varepsilon)`$,
```math
\boxed{
G(X_0)
=
-{8\varepsilon^4+8\varepsilon^3-8\varepsilon^2-6\varepsilon+1
 \over4\varepsilon}.
}
\tag{36}
```

For $`D\ge4`$, one has $`\varepsilon\le1/8`$, and
```math
8\varepsilon^4+8\varepsilon^3-8\varepsilon^2-6\varepsilon+1
\ge
1-8\varepsilon^2-6\varepsilon
\ge {1\over8}>0.
\tag{37}
```
Therefore
```math
G(X_0)<0.
```
Since $`X\ge X_0`$ and $`G`$ decreases,
```math
G(X)<0.
```
Combining with (33),
```math
\boxed{
|Y|<
{\tau X\over D-\varepsilon}.
}
\tag{38}
```

Equations (31), (32), and (38) give
```math
\boxed{
y\in
\operatorname{int}
\operatorname{conv}\{a,p_-,p_+\}.
}
\tag{39}
```

Every actual diameter endpoint is an extreme point of the source convex hull.
Therefore
```math
\boxed{
\deg_H(y)=0.
}
\tag{40}
```

So every degree-two fan leaf produces an inverse-$`D`$ almost-unit pair from a loaded
diameter leaf to a diameter-inactive source point.

## 6. The near-unit graph has maximum degree six

Let $`G_{\rm near}`$ be the graph on the full source whose edges are all pairs
satisfying
```math
1<|x-y|\le R_D:=1+{1\over D}.
\tag{41}
```

### Lemma 6.1

For $`D\ge9`$,
```math
\boxed{\Delta(G_{\rm near})\le6.}
\tag{42}
```

### Proof

Fix a vertex $`y`$ and two distinct near neighbors $`x_1,x_2`$. Put
```math
r_i=|x_i-y|\in(1,R_D].
```
Let $`\theta\in[0,\pi]`$ be the smaller angle between the two rays from $`y`$.

Source separation gives
```math
|x_1-x_2|\ge1.
```
The cosine law therefore gives
```math
\cos\theta
\le
F(r_1,r_2)
:=
{r_1^2+r_2^2-1\over2r_1r_2}.
\tag{43}
```

For fixed $`s`$,
```math
{\partial F(r,s)\over\partial r}
=
{r^2-s^2+1\over2r^2s},
```
so the maximum over $`1\le r\le R_D`$ is attained at an endpoint. Repeating in the
other variable shows that the maximum on $`[1,R_D]^2`$ occurs among
```math
(1,1),\quad(1,R_D),\quad(R_D,R_D).
```
Their values are
```math
{1\over2},\qquad
{R_D\over2},\qquad
1-{1\over2R_D^2}.
```
For $`1<R_D<(1+\sqrt5)/2`$, the last is the largest. Thus
```math
\cos\theta
\le
1-{1\over2R_D^2},
```
or
```math
\boxed{
\theta\ge2\arcsin{1\over2R_D}.
}
\tag{44}
```

If $`D\ge9`$, then
```math
{1\over2R_D}
\ge {9\over20}
>{\pi\over7}
>\sin{\pi\over7}.
```
Hence
```math
\theta>{2\pi\over7}.
\tag{45}
```

Seven rays around one point would have some cyclic angular gap at most $`2\pi/7`$,
contradicting (45). Therefore every vertex has at most six near neighbors. QED.

## 7. Degree-two leaves give distinct inactive blockers and a linear matching

Choose one flip blocker $`y(p)`$ for every contact-degree-two internal fan leaf $`p`$.

By (40), every $`y(p)`$ is diameter-inactive, whereas every $`p`$ is loaded. Hence
two different loaded leaves $`p\ne q`$ give two different unordered blocker pairs:
```math
\{p,y(p)\}\ne\{q,y(q)\}.
```
Therefore the degree-two population gives exactly $`U`$ chosen distinct near-unit
edges.

Lemma 6.1 has two consequences.

First, one diameter-inactive blocker vertex can serve at most six loaded leaves, so
the number $`Y`$ of distinct inactive blocker vertices satisfies
```math
\boxed{
Y\ge {U\over6}.
}
\tag{46}
```

Second, in a graph of maximum degree six, one greedy matching step deletes at most
```math
6+6-1=11
```
edges. Therefore the chosen blocker graph contains a matching of size at least
```math
\boxed{
\nu_{\rm near}\ge {U\over11}.
}
\tag{47}
```

Every selected matching edge is a previously strict pair of length in
$`(1,1+1/D]`$, with one loaded fan-leaf endpoint and one diameter-inactive endpoint.

## 8. Degree-three leaves give actual inactive contact ports

For each contact-degree-three internal fan vertex, let $`z`$ be its third contact
neighbor.

The current third-neighbor inactivity theorem proves
```math
\deg_H(z)=0
\tag{48}
```
and
```math
z\in
\operatorname{int}
\operatorname{conv}\{a,p_-,p_+\}.
\tag{49}
```

The global unit-contact degree cap gives
```math
\deg_C(z)\le5.
\tag{50}
```

Hence one source vertex $`z`$ can be the third neighbor of at most five of the $`T`$
fan vertices. Therefore the number $`Z`$ of distinct diameter-inactive third
neighbors satisfies
```math
\boxed{
Z\ge {T\over5}.
}
\tag{51}
```

The current inward-spoke theorem also gives
```math
|z-a|\le D-\delta_D,
\qquad
\delta_D\to{\sqrt3\over2}.
\tag{52}
```

## 9. Unconditional linear inactive population

Since
```math
I=T+U,
```
either
```math
T\ge {I\over2}
```
or
```math
U\ge {I\over2}.
```

In the first case,
```math
Z\ge {T\over5}\ge {I\over10}.
\tag{53}
```

In the second case,
```math
Y\ge {U\over6}\ge {I\over12},
\tag{54}
```
and the near-unit matching satisfies
```math
\nu_{\rm near}\ge {U\over11}\ge {I\over22}.
\tag{55}
```

Thus in all cases
```math
\boxed{
\#\{z:\deg_H(z)=0\}\ge {I\over12}.
}
\tag{56}
```

Using (2),
```math
\boxed{
\#\{z:\deg_H(z)=0\}
\ge
{1\over12}
\left(
\lceil D\rceil-(4K_\nu+2K_x)\sqrt D
\right).
}
\tag{57}
```

In particular,
```math
\boxed{
\#\{z:\deg_H(z)=0\}
\ge
(1/12-o(1))D.
}
\tag{58}
```

Moreover, if the degree-two population is the larger half, the source contains a
vertex-disjoint matching of previously strict almost-unit pairs of size
```math
\boxed{
{1\over22}
\left(
\lceil D\rceil-(4K_\nu+2K_x)\sqrt D
\right)
=
(1/22-o(1))D.
}
\tag{59}
```

## 10. Frontier effect and remaining bottleneck

The previous fan analysis left a square-root port/stress-flat fork. The exact
degree-two reflection and blocker-triangle theorem remove that fork.

The current low-$`x_B`$, square-root-matching branch now **unconditionally** contains
a linear population of diameter-inactive source vertices:
```math
(1/12-o(1))D.
```

There are two geometric realizations.

1. **Actual-contact ports:** a linear subpopulation is joined by unit contacts to
   loaded fan leaves and lies at fixed positive carrier depth.
2. **Almost-contact ports:** a linear subpopulation lies strictly inside the same
   local fan triangles and is within $`1/D`$ of loaded fan leaves. In the
   degree-two-heavy case, these almost-unit pairs contain a linear vertex-disjoint
   matching.

This still does not close C-II. The remaining target is now sharply stated:

> Convert the forced linear diameter-inactive population into canonical
> attachment/container currency, or use the protected loaded-to-inactive near-unit
> matching to create a source-preserving contact/diameter improvement.

For actual-contact ports, the canonical harmonic attachment theorem applies directly:
each port belongs to an unpinned positive-contact component whose attachment set
contains its loaded fan leaf.

For almost-contact ports, the inactive endpoint need not be nonisolated in the
positive-contact graph, so a separate pair-closing or attachment-activation theorem
is still required.

No macroscopic inactive chamber, strict smaller-diameter source, C-II closure, or
Level I closure is claimed.

**Disposition:** exact proof-only source-level strengthening. No numerical search,
verifier execution, CI output, or unexecuted certificate code is used.
