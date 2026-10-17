# Target C-II — line-section rigidity and the canonical terminal companion of every LOWER blocker

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the current one-row LOWER branch; no canonical promotion claimed  
**Scope:** selected O--O path coordinates in the one-sign strong-TB1 branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** selected O--O proper midpoint-centerline crosscuts; strict unit-rhombus face geometry; source unit separation; exact contact-swap algebra; train crossing-angle theorem; one-row all-residue Horn propagation  
**Certificate:** `research/verify_target_c_high_t_tb1_lower_terminal_companion_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current one-row theorem says that every inverse-`D` near-unit LOWER blocker is the diagonal of one strict rhombus on its unique selected support row. This note adds two facts.

First, a direct line-section argument proves the same normal form on the larger fixed window

\[
1<|x-y|\le L_*:=\frac{3\sqrt3}{4}=1.29903810567\ldots,
\]

rather than only `|x-y|<=21/20`.

Second, exact contact-swap algebra gives every LOWER blocker a canonical companion train. The singleton LOWER inequality forces that train to cross the blocker row but not the opposite boundary row of the owner layer. Its blocker-rhombus angular defect is at most the owner layer's TB1 non-antipodality.

On the current GLOBAL LOWER winner this yields more than

\[
\left(\frac{s_0}{32}-o(1)\right)D
=\left(7.724609375\times10^{-8}-o(1)\right)D,
\qquad
s_0=\frac{791}{320{,}000{,}000},
\]

distinct same-side terminal companion trains.

---

## 1. A crossed strict rhombus spends more than `sqrt(3)/4` of blocker length

Write a strict unit rhombus as

\[
F=\operatorname{conv}\{0,u,v,u+v\},
\qquad |u|=|v|=1,
\qquad \frac\pi3<\theta<\frac{2\pi}{3}.
\]

Suppose the selected row uses the pair of sides parallel to `u`. Its midpoint centerline is

\[
M_F=\left\{\frac u2+t v:0\le t\le1\right\}.
\tag{TC.1}
\]

Let a line with unit direction `d` meet `M_F` at `z=u/2+t v`, and write

\[
d=A u+B v.
\]

Cramer's rule gives

\[
A=\frac{\det(d,v)}{\det(u,v)},
\qquad
B=\frac{\det(u,d)}{\det(u,v)}.
\]

Since `sin(theta)>sqrt(3)/2`,

\[
\boxed{|A|,|B|<\frac2{\sqrt3}.}
\tag{TC.2}
\]

In `(u,v)` coordinates, `z+lambda d` is

\[
\left(\frac12+\lambda A,\ t+\lambda B\right).
\]

Unless the line is tangent to a side of `F` at an endpoint of `M_F`, one of the two directions from `z` stays in `int(F)` for length greater than

\[
\min\left\{\frac1{2|A|},\frac1{2|B|}\right\}
>\frac{\sqrt3}{4},
\tag{TC.3}
\]

with a zero denominator interpreted as infinity. At `t=0` or `1`, choose the sign that enters the rhombus; the available `v`-coordinate room is then even larger.

The only exceptional case is `t in {0,1}` and `B=0`, when the blocker line is exactly the line of the unit contact edge whose midpoint is `z`. This cannot happen for a strict source pair of length below two. Normalize that edge to endpoints `-1/2,1/2`. Every other source point on the line is at least unit distance from both endpoints, hence lies at coordinate at most `-3/2` or at least `3/2`. A source pair containing the midpoint is therefore either that unit edge or has length at least two.

Thus every crossed selected-row rhombus of a strict pair with `1<|x-y|<2` contributes an open interior line section `J_F` satisfying

\[
\boxed{|J_F|>\frac{\sqrt3}{4}.}
\tag{TC.4}
\]

---

## 2. Those line sections lie inside the blocker segment

A midpoint-centerline intersection is not a source vertex. It lies strictly between the blocker endpoints.

Also, no source vertex other than a vertex of `F` can lie in `F`. Indeed, for

\[
p=\alpha u+\beta v,
\qquad 0\le\alpha,\beta\le1,
\]

choose the nearest values `alpha_0,beta_0 in {0,1}`. Then

\[
|p-(\alpha_0u+\beta_0v)|
\le|\alpha-\alpha_0|+|\beta-\beta_0|\le1,
\]

and equality in the last bound would require the two nonparallel side directions to be positively collinear. Hence a nonvertex point of `F` is strictly less than one from a face vertex.

Therefore an open section `J_F` cannot pass through either blocker endpoint. Since its closure contains the internal midpoint-centerline intersection,

\[
\boxed{J_F\subset(x,y).}
\tag{TC.5}
\]

Distinct selected rows use distinct bounded contact faces with disjoint interiors, so their `J_F` are pairwise disjoint. If `N` selected rows separate `x,y`,

\[
\boxed{N\frac{\sqrt3}{4}<|x-y|.}
\tag{TC.6}
\]

Hence `N<=2` whenever `|x-y|<=3sqrt(3)/4`.

---

## 3. A nonvertex source point stays `sqrt(3)/2` from a unit-rhombus face

Let `z` be a source vertex which is not a vertex of `F`. It lies outside `F`. Let `p` be a closest point of `F`.

If `p` is a rhombus vertex, unit separation gives `dist(z,F)>=1`. Otherwise `p` is in the relative interior of a unit side. Let `t in (0,1)` be the projection coordinate on that side and `h=dist(z,F)`. Unit separation from the side endpoints gives

\[
h^2+t^2\ge1,
\qquad
h^2+(1-t)^2\ge1.
\]

Therefore

\[
h^2\ge\max\{1-t^2,1-(1-t)^2\}\ge\frac34,
\]

so

\[
\boxed{\operatorname{dist}(z,F)\ge\frac{\sqrt3}{2}.}
\tag{TC.7}
\]

---

## 4. One row is a missing diagonal; two rows are impossible

Assume exactly one selected row is crossed, with face `F`. By (TC.4), the blocker length outside `int(F)` is less than

\[
\frac{3\sqrt3}{4}-\frac{\sqrt3}{4}=\frac{\sqrt3}{2}.
\]

Each endpoint is therefore within `sqrt(3)/2` of `F`. By (TC.7), both are vertices of `F`. Since their distance is greater than one, they are opposite vertices. Thus

\[
\boxed{xy\text{ is a diagonal of the unique crossed strict unit rhombus.}}
\tag{TC.8}
\]

Now suppose two rows are crossed, with faces `F_1,F_2` in order. Their interior sections have total length greater than `sqrt(3)/2`, so the total residual length is less than `sqrt(3)/4`. In particular the first endpoint `x` is a vertex of `F_1`.

The selected midpoint centerline of `F_1` is at distance

\[
\frac{\sin\theta}{2}>\frac{\sqrt3}{4}
\]

from every rhombus vertex. Let `z_1` be its intersection with `xy`. If `y` were not a vertex of `F_1`, then (TC.7) would give `|y-z_1|>=sqrt(3)/2`, while `|x-z_1|>sqrt(3)/4`. This would force `|x-y|>3sqrt(3)/4`, contradiction.

So `x,y` are opposite vertices of `F_1`. The open diagonal `(x,y)` lies in `int(F_1)`. But the nonempty open section `J_{F_2}` lies in both `(x,y)` and `int(F_2)`, contradicting disjoint face interiors.

Therefore:

> **Line-section one-row theorem.** If source vertices satisfy
> \[
> 1<|x-y|\le\frac{3\sqrt3}{4},
> \]
> then their selected O--O support contains at most one row. If one row is present, `x,y` are the opposite vertices of its unique crossed strict unit rhombus.

This strictly contains the old fixed window because

\[
\left(\frac{21}{20}\right)^2=\frac{441}{400}<\frac{27}{16}
=\left(\frac{3\sqrt3}{4}\right)^2.
\tag{TC.9}
\]

---

## 5. Exact LOWER algebra bounds the blocker-face angular defect

Consider a one-sign strong-TB1 owner layer `R_i`. Orient its two unit boundary-contact directions from the fixed sides into the moving layer:

\[
|a|=|b|=1,
\qquad
\angle(a,b)=\pi-\varepsilon,
\qquad
\varepsilon>0.
\tag{TC.10}
\]

The exact swap is

\[
v=-(a+b).
\tag{TC.11}
\]

Let a LOWER blocker be supported on the boundary row with transverse direction `[a]`. At that boundary every contact edge of the blocker rhombus points from the fixed side to the moving side with vector `a`. Choose a unit vector `c` along the other pair of rhombus sides so that the blocker vector from its fixed endpoint to its moving endpoint is

\[
r=a+c.
\tag{TC.12}
\]

This covers both diagonals after replacing `c` by `-c` when necessary. Strict rhombus geometry gives

\[
\gamma:=\angle(a,c)\in\left(\frac\pi3,\frac{2\pi}{3}\right).
\tag{TC.13}
\]

After the exact swap,

\[
r'=r+v=c-b.
\tag{TC.14}
\]

Because this pair is a LOWER witness, `|c-b|<=1`. For unit vectors,

\[
\eta:=\angle(c,b)\le\frac\pi3.
\tag{TC.15}
\]

The angular triangle inequality gives

\[
\pi-\varepsilon
=\angle(a,b)
\le\angle(a,c)+\angle(c,b)
\le\gamma+\frac\pi3.
\]

Hence

\[
\boxed{0<\delta_F:=\frac{2\pi}{3}-\gamma\le\varepsilon.}
\tag{TC.16}
\]

For large `D`, `epsilon=O(D^-1)<pi/6`, so `gamma>pi/2`. Then `pi-gamma` is the acute angle of the blocker rhombus and `delta_F=(pi-gamma)-pi/3` is exactly its usual acute angular defect. Thus the blocker face itself is automatically inverse-`D` near-equilateral, with defect bounded by the owner layer's TB1 non-antipodality.

---

## 6. Every LOWER blocker has a canonical terminal companion train

Let `sigma_e` be the train with transverse direction `[c]`. It crosses the blocker support row `[a]` in the blocker rhombus.

The opposite boundary row of `R_i` has transverse direction `[b]`. If `sigma_e` crossed that row in a strict rhombus, the train crossing theorem would require

\[
d_{\mathbb{RP}^1}([c],[b])>\frac\pi3.
\]

But (TC.15) gives an ordinary angle at most `pi/3`, hence projective acute angle at most `pi/3`. Contradiction. Therefore

\[
\boxed{\sigma_e\text{ crosses the support row but not the opposite boundary row of }R_i.}
\tag{TC.17}
\]

Writing the adjacent row crossing families as `Gamma^-` and `Gamma^+`, the appropriate orientation gives

\[
\boxed{\sigma_e\in\Gamma^-\setminus\Gamma^+.}
\tag{TC.18}
\]

Thus every LOWER blocker supplies a canonical member of the adjacent symmetric difference. Since the terminal-topology cost satisfies

\[
|\Gamma^-\triangle\Gamma^+|\le L_i,
\]

every LOWER owner interface has

\[
\boxed{L_i\ge1.}
\tag{TC.19}
\]

The selected rows are pairwise-disjoint proper crosscuts. A connected train which crosses rows `tau_j` and `tau_k`, `j<k`, must cross every intermediate selected row; it cannot recross a selected row because two trains cross at most once. Hence one train's selected-row crossing set is an integer interval.

By (TC.17), the support row is one endpoint of the crossing interval of `sigma_e` on the owner side. In the retained GLOBAL LOWER family, owner coordinates are injective. At a fixed interval endpoint, the owner-side orientation determines a single adjacent owner layer, so at most one retained blocker can use that train there. An unsplit train has two interval endpoints; after fixing owner-side orientation, the canonical-companion map is injective.

---

## 7. Quantitative terminal-rail population

The fully deduplicated Horn theorem gives, on the LOWER winner,

\[
N_L>\left(\delta_{\rm one}-o(1)\right)D,
\qquad
\delta_{\rm one}=\frac{s_0}{16}
=\frac{791}{5{,}120{,}000{,}000}.
\tag{TC.20}
\]

Split blockers by which side of the support row contains the owner layer. One orientation retains at least half. On this oriented family the companion map is injective. Therefore the source contains more than

\[
\boxed{
\left(\frac{s_0}{32}-o(1)\right)D
=\left(7.724609375\times10^{-8}-o(1)\right)D
}
\tag{TC.21}
\]

distinct same-side canonical terminal companion trains.

The current fixed-spine theorem also supplies a pairwise-distinct-support-row family of density

\[
\frac{1{,}272{,}719}{156{,}697{,}600{,}000{,}000}
=8.12213460832\ldots\times10^{-9}.
\tag{TC.22}
\]

Every member is threaded by one fixed complete train `b_*`. Split this family by owner-side orientation. The larger half has injective canonical companions, so it contains more than

\[
\boxed{
\frac{1{,}272{,}719}{313{,}395{,}200{,}000{,}000}D-o(D)
=\left(4.06106730416\ldots\times10^{-9}-o(1)\right)D
}
\tag{TC.23}
\]

distinct same-side terminal companion trains attached to `b_*`-threaded blocker rows.

Thus the remaining LOWER seam has the normal form

```text
one fixed complete spine b_*
    crosses linearly many distinct blocker rows;

on every retained blocker row:
    the blocker is one strict-rhombus diagonal;
    its blocker-face defect is <= owner TB1 non-antipodality = O(D^-1);
    a distinct companion train sigma_e crosses that row;
    sigma_e does not cross the opposite boundary row;
    all sigma_e terminate in selected-row order on the same owner side.
```

This is a fixed-spine / terminal-rail configuration. The next closure target is to exploit its planar order or to charge the forced same-side terminal endpoints to a sharper boundary/exceptional-face currency than the generic `O(D)` terminal-variation estimate.

**Disposition:** extended one-row rigidity to `3sqrt(3)/4`; proved `delta_F<=epsilon_i`; proved every LOWER blocker has a canonical train in the adjacent crossing-family symmetric difference; and extracted a linear fixed-spine family of distinct same-side terminal companions. C-II and Level I remain open.
