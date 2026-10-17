> Generated reading edition · [exact source](../../../docs/reports/target_c_sharp_annular_simplicial_packing_2026-09-11.md) · source SHA-256 `a585af66bd3eeb2731cd8fa755a792b9e85f8b44035f27bfea67e3e542991c65`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-0BFDD8A9F379","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - sharp annular simplicial packing and loaded-terminal credit

**Date:** 2026-09-11  
**Repository base:** branch after GR/GA/LT  
**Run type:** literature-assisted exact packing theorem / post-ZF source-capacity sharpening  
**Target:** Target C C-II after ZF  
**Depends on:** GR general rhombus-excess inequality; C65 identification `B_+=Vert(F)`  
**External theorem:** Graham-Witsenhausen-Zassenhaus, *On tightest packings in the Minkowski plane*, Pacific J. Math. 41 (1972), Theorem 4

## LEVEL I STATUS

`STILL OPEN`.

The promoted AV annular theorem has the sharp bulk coefficient `2/sqrt(3)` but pays
both boundary perimeters with coefficient `2/sqrt(3)` before multiplication by
`a0=sqrt(3)/2`.  The best simplicial packing inequality of
Graham-Witsenhausen-Zassenhaus gives the exact Oler boundary coefficient instead.

For a Euclidean finite plane simplicial packing `S`, their Theorem 4 specializes to

```math
\boxed{
|V(S)|
\le {2\over\sqrt3}\operatorname{area}|S|
+{1\over2}\operatorname{per}|S|
+\chi(S).
}
\tag{SA.1}
```

Equivalently, with

```math
a_0={\sqrt3\over2},\qquad c_0={\sqrt3\over4},
```

```math
\boxed{
a_0|V(S)|
\le \operatorname{area}|S|+c_0\operatorname{per}|S|+a_0\chi(S).}
\tag{SA.2}
```

Applying this to the annular region between the full source hull `K` and force hull
`F`, with all external source points and all loaded force-hull vertices included as
vertices, gives

```math
\boxed{
a_0(Z_{ext}+q)
\le A_K-A_F+c_0(P_K+P_F)+a_0.}
\tag{SA.3}
```

The additive `a0` is a safe finite allowance for the case in which `F` meets
`partial K`; if `F subset int K`, the region is a genuine annulus and its Euler
characteristic is zero, so the `a0` term disappears.

Combining SA.3 with the new GR theorem yields

```math
\boxed{
E+\delta_K+a_0q
< c_0(P_K+2P_F)+a_0.
}
\tag{SA.4}
```

This strictly strengthens the earlier LT loaded-terminal annular ledger.

---

## 1. External theorem and Euclidean constants

Graham, Witsenhausen and Zassenhaus define a finite plane simplicial complex `S` to
provide a finite packing if every two distinct vertices whose joining segment belongs
to the support are at Minkowski distance at least one.  Their Theorem 4 states the
best invariant-measure packing inequality

```math
\alpha_0(S)
\le {\mathcal A(S)\over2\Delta_*}
+{\mathcal P(S)\over2}
+\chi(S),
\tag{1.1}
```

where `Delta_*` is the minimum area of a unit equilateral triangle in the norm.

For the Euclidean norm,

```math
\Delta_*={\sqrt3\over4},
```

so (1.1) is exactly SA.1.  The source configuration is globally unit-separated,
therefore **any** straight triangulation using source points as vertices satisfies the
paper's packing hypothesis: every simplicial edge joins two source points and hence
has length at least one.

Reference:

R. L. Graham, H. S. Witsenhausen, H. J. Zassenhaus, *On tightest packings in the
Minkowski plane*, Pacific Journal of Mathematics 41 (1972), 699-715, Theorem 4,
pp. 710-714.

---

## 2. Triangulate the source annulus

Let

```math
K=\operatorname{conv}A,
\qquad
F=\operatorname{conv}V(C),
\qquad F\subseteq K.
```

Let

```math
X=(A\setminus F)\cup B_+,
\qquad |X|=Z_{ext}+q.
\tag{2.1}
```

Every point of `X` belongs to

```math
U:=K\setminus\operatorname{int}F.
```

Add, if needed, the extreme vertices of `K` and `F` to the vertex list used for a
straight triangulation of `U`.  The vertices of `F` are exactly `B_+`; the extreme
vertices of `K` already belong to `A`, and any such vertex outside `F` is already in
`A\setminus F`.  Degenerate collinear boundary points need not be triangulation
vertices.  Insert every remaining point of `X` into the triangulation by the standard
stellar subdivision of the containing triangle or boundary edge.  Thus there is a
finite plane simplicial complex `S_U` with

```math
|S_U|=U
```

and vertex set containing `X`; using only `X` plus the necessary extreme boundary
vertices does not introduce any non-source vertex.

All simplicial edges join source points, so the complex is a finite packing in the
sense of Theorem 4.

If `F subset int K`, then `U` is a closed annulus and

```math
\chi(U)=0.
```

If `F` meets `partial K`, the removal of `int F` opens the hole to the exterior.  The
resulting compact convex-annular support is connected and has no more than one hole,
so

```math
\boxed{\chi(U)\le1.}
\tag{2.2}
```

The geometric boundary of `U` is contained in `partial K union partial F`; shared
boundary pieces cancel rather than add.  Hence

```math
\boxed{\operatorname{per}(U)\le P_K+P_F.}
\tag{2.3}
```

Also

```math
\operatorname{area}U=A_K-A_F.
\tag{2.4}
```

Apply SA.2 and use (2.2)-(2.4):

```math
a_0(Z_{ext}+q)
\le A_K-A_F+c_0(P_K+P_F)+a_0,
```

which proves SA.3.

### Scope note on the touching case

If `F=K`, then `Z_ext=0` and the annular region has zero area.  SA.3 follows directly
from the ordinary convex Oler inequality on `F` or by an inward parallel-body limit;
no two-dimensional triangulation of a zero-width annulus is required.  If the bodies
share only boundary arcs or points, an arbitrarily small inward offset of `F`, followed
by a limit, gives the same safe `chi<=1` bound.

---

## 3. Combine with GR

GR proves for every post-ZF survivor

```math
\boxed{E+\delta_F<a_0Z_{ext}+c_0P_F,}
\tag{3.1}
```

where

```math
\delta_F={\pi D^2\over4}-A_F,
\qquad
\delta_K={\pi D^2\over4}-A_K.
```

SA.3 gives

```math
\begin{aligned}
a_0Z_{ext}
&\le A_K-A_F+c_0(P_K+P_F)+a_0-a_0q\\
&=\delta_F-\delta_K+c_0(P_K+P_F)+a_0-a_0q.
\end{aligned}
\tag{3.2}
```

Insert (3.2) into (3.1):

```math
E+\delta_F
<\delta_F-\delta_K+c_0(P_K+2P_F)+a_0-a_0q.
```

Cancel `delta_F` and rearrange:

### Theorem SA - sharp annular loaded-terminal ledger

```math
\boxed{
E+\delta_K+a_0q
< c_0(P_K+2P_F)+a_0.
}
\tag{SA.4}
```

If `F subset int K`, the final `+a0` can be removed.

Because `P_K,P_F<=pi D`, SA.4 gives the finite coarse estimate

```math
E+\delta_K+a_0q
<3c_0\pi D+a_0.
\tag{3.3}
```

The exact form SA.4 is the useful statement; the three-perimeter relaxation throws
away most of the new information.

---

## 4. Comparison with AV/LT

LT, using the promoted AV theorem, gives

```math
E+\delta_K+a_0q
<P_K+(1+c_0)P_F+\pi.
```

SA replaces the coefficients `(1,1+c0)` by `(c0,2c0)` and the additive `pi` by at
most `a0`.  Numerically

```math
c_0=0.4330127\ldots,
\qquad
2c_0=0.8660254\ldots.
```

Thus the annular boundary loss drops substantially while retaining the same sharp
bulk cancellation.

The theorem does not by itself close C-II because the force-hull perimeter `P_F` can
still be linear in `D` with a coefficient large enough to absorb `a0 q`.

---

## 5. Tightness and why no discrete slack gap is imported

The same 1972 paper proves that equality in its packing inequality is equivalent to a
unit-equilateral triangulation of the support.  This does **not** imply a uniform
positive slack for a triangle-free source: near-equilateral shears can have arbitrarily
small positive slack.  SA uses only the exact inequality, not an invalid discrete
stability gap.

---

## 6. Exact next use

SA.4 should be combined with the post-ZF exact force-boundary identities rather than
with `P_F<=pi D` alone.  In particular

```math
P_F\le b,
\qquad
b+Q=2(q-d_H-s_Z),
```

and DB/NB couple `q,h,Q,s_Z`.  The remaining scalar optimization is therefore over
actual post-ZF currencies, not an independent annular population term.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

External exact input (Graham-Witsenhausen-Zassenhaus 1972, Thm 4):
for a Euclidean finite plane simplicial packing,
    N <= (2/sqrt3) area + perimeter/2 + chi.

Triangulate U=K\int(F) using the external source points plus B_+.  All triangulation
vertices are source points, so every simplicial edge has length >=1.  Since chi(U)<=1
and per(U)<=P_K+P_F,
    a0(Z_ext+q)<=A_K-A_F+c0(P_K+P_F)+a0.

GR says
    E+delta_F<a0 Z_ext+c0 P_F.
Substitution cancels delta_F and gives
    E+delta_K+a0 q<c0(P_K+2P_F)+a0.
This strictly improves LT and is valid for arbitrary d_H,s_Z, external rattlers,
exceptional faces, and diameter topology.
```
