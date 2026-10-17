> Generated reading edition · [exact source](../../../../docs/targets/target-c/66-forest-doubled-gap-audit.md) · source SHA-256 `f4728ff4227421bbb6a54a08979169823f6ea31029b500455e9e6d61dfca50e6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 3 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — forest doubled-gap and primitive-boundary audit

**Date:** 2026-09-11  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module independently audits the geometric core of
`docs/reports/target_c_forest_double_diameter_gap_2026-09-11.md` and removes an
unnecessary `s_Z=0` restriction from its outer-walk consequence.

The result is specific to the Woodall forest branch `d_H=q-h>0`. It uses no KKT weight
floor, no circuit equality, no hull-saturated normalization, and no removal of
contact-isolated source points.

The main new conclusions are

```math
\boxed{
\liminf {x_B\over D}
\ge 2\cos\left({1\over2}\lim {q\over D}\right)
}
```

along every convergent forest subsequence, and the universal forest primitive split

```math
\boxed{
\liminf {\max\{e_{BB},x_B\}\over D}\ge\kappa,
\qquad
\kappa=2\cos\kappa,
\qquad
\kappa=1.02986\ldots .
}
```

Thus the forest branch must carry more than one unit of either direct loaded-loaded
contact count or outer-walk excess per diameter scale.

---

# 66. Vertex-disjoint diameter chords pay double angular spacing

Put

```math
a_D:=\arcsin{1\over2D}.
```

## 66.1 Equal-diagonal metric lemma

Let `AB` and `CD` be two length-`D` segments in a planar set of diameter at most `D`,
with four distinct endpoints. Let `theta in (0,pi/2]` be the acute projective angle
between their supporting lines. Then

```math
\boxed{
\min\{|A-C|,|A-D|,|B-C|,|B-D|\}
\le2D\sin(\theta/4).
}
\tag{66.1}
```

### Proof

Scale `D` to one. Put the midpoint of `AB` at the origin and write the two half-edge
directions as unit vectors `u,v`. If `m` is the midpoint displacement, the four cross
vectors are

```math
m\pm{u-v\over2},
\qquad
m\pm{u+v\over2}.
```

Set

```math
w={u-v\over2},\quad z={u+v\over2},\quad
|w|=s=\sin(\theta/2),\quad |z|=c=\cos(\theta/2).
```

The vectors `w,z` are perpendicular. Write

```math
m=\alpha\widehat w+\beta\widehat z.
```

The two constraints `|m+z|,|m-z|<=1` imply

```math
\alpha^2+(|\beta|+c)^2\le1.
```

Thus `|alpha|<=s` and

```math
|\beta|\le\sqrt{1-\alpha^2}-c.
```

The smaller of `|m+w|,|m-w|` has squared length

```math
(s-|\alpha|)^2+\beta^2.
```

Write `|alpha|=sin(phi)` with `0<=phi<=theta/2`. Then

```math
\begin{aligned}
(s-\sin\phi)^2+(\cos\phi-c)^2
&=2-2\cos(\theta/2-\phi)\\
&\le 2-2\cos(\theta/2)\\
&=4\sin^2(\theta/4).
\end{aligned}
```

Restoring `D` proves (66.1). `square`

Because the source is unit-separated, every cross distance between four distinct
endpoints is at least one. Hence two vertex-disjoint actual diameter edges satisfy

```math
\boxed{\theta\ge4a_D}
\tag{66.2}
```

for all sufficiently large `D`. Two diameter edges that share an endpoint satisfy the
usual lower bound

```math
\boxed{\theta\ge2a_D}.
\tag{66.3}
```

## 66.2 At least `d_H` cyclic direction gaps are doubled

Order the `h` projective diameter directions cyclically. Let `N_sh` be the number of
consecutive direction pairs whose diameter edges share an endpoint.

Unless the diameter graph is a star, a vertex `v` of degree `d_v` can account for at
most `d_v-1` shared cyclic adjacencies: its incident edges occupy a proper subset of
the cyclic direction positions. Two simple edges share at most one endpoint, so no
shared adjacency is double-counted. Since every loaded diameter vertex has positive
degree,

```math
N_{sh}\le\sum_v(d_v-1)=2h-q.
\tag{66.4}
```

Therefore the number of consecutive pairs with disjoint endpoints is at least

```math
\boxed{
N_{dis}\ge h-(2h-q)=q-h=d_H.
}
\tag{66.5}
```

The star exception cannot occur in sufficiently large post-ZF survivors. If `H` is a
star, all leaf rays from its center lie in an angular arc of width at most `pi/3`,
because every two leaves are at distance at most `D`. Unit separation gives spacing at
least `2a_D`, hence

```math
h\le1+{\pi\over6a_D}
```

and `limsup h/D<=pi/3`. Canonical Section 59 gives
`liminf h/D>=2rho=1.47817...>pi/3`.

Thus (66.5) applies asymptotically throughout the forest branch.

---

# 67. Heterogeneous difference-body perimeter

For every sufficiently large forest survivor, let the cyclic projective direction gaps be `g_1,...,g_h`, with sum `pi`. Every gap is at least `2a_D`; at least `d_H` of them are at least `4a_D`.

The function `sin(g/2)` is concave on `[0,pi]`. Relax the constraints by designating
exactly `d_H` gap coordinates as doubled. Under fixed lower bounds and fixed total gap
sum, the minimum of the concave sum occurs at an extreme point: all but one gap are at
their lower bounds. There are two possible types of extreme point, depending on whether
the one free gap is a doubled coordinate or an ordinary coordinate.

If the free gap is doubled, then

```math
S_D:=(h-d_H)\sin a_D
 +(d_H-1)\sin(2a_D)
 +\cos((q-2)a_D).
\tag{67.1}
```

If `h-d_H>=1` and the free gap is ordinary, then

```math
S_N:=(h-d_H-1)\sin a_D
 +d_H\sin(2a_D)
 +\cos((q-1)a_D).
\tag{67.2}
```

Therefore the exact finite lower bound is

```math
\boxed{
\sum_{i=1}^h\sin(g_i/2)
\ge
\begin{cases}
S_D,&h-d_H=0,\\
\min\{S_D,S_N\},&h-d_H\ge1.
\end{cases}
}
\tag{67.3}
```

No ordering between `S_D` and `S_N` is needed. In particular, we do **not** assume the
unsupported finite inequality `2a_D q<=pi`; the ordinary convex perimeter bound alone
does not imply it.

Let

```math
P_H=D\operatorname{conv}\{\pm u_e:e\in E(H)\}.
```

Every diameter vector belongs to `F-F`, so `P_H subset F-F`. Cauchy perimeter
monotonicity and `per(F-F)=2per(F)` give

```math
\operatorname{per}(F)
\ge2D\sum_i\sin(g_i/2).
```

Using `sin a_D=1/(2D)` and `2D sin(2a_D)=2 cos a_D`, the two exact candidate perimeter
bounds are

```math
P_D:=h-d_H+2(d_H-1)\cos a_D
 +2D\cos((q-2)a_D),
\tag{67.4}
```

and, when `h-d_H>=1`,

```math
P_N:=h-d_H-1+2d_H\cos a_D
 +2D\cos((q-1)a_D).
\tag{67.5}
```

Thus

```math
\boxed{
\operatorname{per}(F)
\ge
\begin{cases}
P_D,&h-d_H=0,\\
\min\{P_D,P_N\},&h-d_H\ge1.
\end{cases}
}
\tag{67.6}
```

This exact finite statement has no `s_Z=0` assumption.

---

# 68. The outer-walk consequence is all-`s_Z`

The outer contact-face walk has length

```math
b=q+x_B
```

and convex hull `F`, so

```math
\operatorname{per}(F)\le q+x_B.
\tag{68.1}
```

In the forest branch `d_H=q-h`. Subtract `q` from the two candidate bounds in
(67.4)--(67.5). They give respectively

```math
X_D:=2D\cos((q-2)a_D)
 -2-2(d_H-1)(1-\cos a_D),
\tag{68.2}
```

and, when `h-d_H>=1`,

```math
X_N:=2D\cos((q-1)a_D)
 -1-2d_H(1-\cos a_D).
\tag{68.3}
```

Hence exactly

```math
\boxed{
 x_B\ge
\begin{cases}
X_D,&h-d_H=0,\\
\min\{X_D,X_N\},&h-d_H\ge1.
\end{cases}
}
\tag{68.4}
```

Now `d_H<=q<=pi D`, `1-cos a_D=O(D^{-2})`, and `a_D=1/(2D)+O(D^{-3})`.
Therefore along every unbounded forest subsequence with

```math
{q\over D}\to x,
```

both `X_D/D` and `X_N/D` tend to `2cos(x/2)`. Consequently

```math
\boxed{
\liminf {x_B\over D}\ge2\cos(x/2).
}
\tag{68.5}
```

Thus the old forest doubled-gap asymptotic survives without any finite ordering of the
two extreme-point types and remains valid for arbitrary mixed surplus `s_Z>=0`.

---

# 69. Forest primitive split above one

Canonical Section 63 gives

```math
\boxed{e_{BB}+x_B\ge q.}
\tag{69.1}
```

Put

```math
M:=\max\{e_{BB},x_B\}.
```

Along a convergent forest subsequence `q/D->x`, equations (68.5) and (69.1) give

```math
\liminf {M\over D}
\ge
\max\left\{{x\over2},\,2\cos(x/2)\right\}.
\tag{69.2}
```

Canonical Section 59 gives `q>=h` and
`liminf h/D>=2rho`, so every subsequential `x` lies in `[2rho,pi]`.
The first function in (69.2) increases strictly and the second decreases strictly.
Their maximum is minimized at their unique intersection

```math
{x\over2}=2\cos(x/2).
```

Write `x=2kappa`. Then the crossing equation is

```math
\boxed{\kappa=2\cos\kappa.}
\tag{69.3}
```

The function `t-2cos t` is strictly increasing on `(0,pi/2)` and changes sign, so the
root is unique. It lies above one and numerically is

```math
\kappa=1.02986\ldots .
```

Hence every unbounded Woodall-forest survivor sequence satisfies

```math
\boxed{
\liminf {\max\{e_{BB},x_B\}\over D}\ge\kappa>1.0298.
}
\tag{69.4}
```

This strictly strengthens both Section 63's `rho` bound and Section 65's all-branch
`4rho/3` bound in the forest branch.

Resolving `x_B=m+u_B` as in Section 63 gives the forest trichotomy

```math
\boxed{
\text{either }e_{BB}\ge(\kappa-o(1))D,
\quad m\ge(\kappa/2-o(1))D,
\quad\text{or }u_B\ge(\kappa/2-o(1))D.
}
\tag{69.5}
```

---

## Equality/stability information

If a forest sequence approaches the constant `kappa` in (69.4), then necessarily

```math
{q\over D}\to2\kappa,
\qquad
{x_B\over D}\to\kappa,
\qquad
{e_{BB}\over D}\to\kappa.
```

Moreover the two candidate perimeter bounds (67.4)--(67.6) and `per(F)<=q+x_B` become asymptotically sharp, so

```math
{\operatorname{per}(F)\over D}\to3\kappa.
```

Section 63's exact identity

```math
e_{BB}+x_B=q+u_B+c_B
```

then forces

```math
{u_B+c_B\over D}\to0.
```

Thus a near-extremal forest has no linear budget for deep outer-walk repetition or
extra loaded-loaded contact chords. Almost all of its primitive boundary complexity is
stored in one-extra-edge replacements of nonunit loaded hull sides.

This endpoint description is not yet a contradiction. It gives a concrete next
stability target: combine the resulting shallow-detour shell with C26 loaded/unloaded
contact-degree constraints and the canonical common-block/negative-transfer structure.

## Scope and regressions

- **Woodall cyclic branch:** outside the doubled-gap theorem; Section 65 still applies.
- **Forest with `s_Z>0`:** fully included. The proof never invokes the circuit identity.
- **Star diameter graph:** excluded asymptotically before the perimeter theorem.
- **Matching components:** allowed, but the aggregate forest still obeys (69.4).
- **Contact-isolated source points:** untouched.
- **KKT coefficient floors:** not used.
- **Rejected Reuleaux-cap detour:** not used.

The theorem does not close the forest branch. It upgrades the remaining forest
obstruction to a directly geometric primitive-boundary alternative with constant
strictly above one.
