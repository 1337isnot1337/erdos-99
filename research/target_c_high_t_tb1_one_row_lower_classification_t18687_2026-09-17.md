<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "89fc63e5a5b58b46a3ae2323f734a984645bf383", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_one_row_lower_classification_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e4a574035ca5a6d77ced2a408cf35d108c33ed2eae8f561cb90aa2e7b4044320"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — inverse-D near-unit blockers have one-row support, and LOWER witnesses cannot repeat

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the one-sign strong-TB1 finite-swap branch; no canonical promotion claimed  
**Scope:** the selected O--O path through `t=(q-k)/D<=1.8687`  
**Dependencies:** selected O--O proper centerline crosscuts; strict unit-rhombus geometry; source unit separation; common strong-TB1 row phase; exact double-witness collapse  
**Certificate:** `research/verify_target_c_high_t_tb1_one_row_lower_classification_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The four-row endpoint-incidence theorem can be sharpened much further. The extra observation is that the source points are unit-separated from every vertex of a crossed rhombus, not merely from its center.

Let `x,y` be source vertices with

\[
1<|x-y|\le {21\over20}.
\tag{OR.1}
\]

Then the exact selected-cut support of `xy` contains at most one selected O--O row:

\[
\boxed{
|\operatorname{reg}(x)-\operatorname{reg}(y)|\le1.
}
\tag{OR.2}
\]

Moreover, if one selected row separates `x` and `y`, then `x,y` are the two opposite vertices of the unique strict unit rhombus in which that row is crossed by the segment `xy`. Thus the pair itself is a rhombus diagonal.

For a LOWER exact-swap witness this applies for all sufficiently large `D`, because

\[
1<|x-y|\le1+q_i,
\qquad q_i=O(D^{-1}).
\tag{OR.3}
\]

The one-row classification has a second consequence. The exact double-witness theorem says that a LOWER pair reused at two distinct one-sign strong-TB1 interfaces is `O(D^{-1})`-parallel to the common row phase. But a diagonal of a strict unit rhombus is separated projectively from either side direction by an angle in

\[
\left({\pi\over6},{\pi\over3}\right).
\tag{OR.4}
\]

The unique separating row is a boundary row of both endpoint layers and therefore has the common strong-TB1 row phase to `O(D^{-1})`. Hence repeated LOWER witnesses are impossible for all sufficiently large `D`:

\[
\boxed{
N_{\rm repeated,LOWER}=0
\quad\text{eventually}.
}
\tag{OR.5}
\]

This removes the surviving cross-residue duplication mechanism on the LOWER side.

---

## 1. Center-distance identity for a unit rhombus

Write a strict unit rhombus as

\[
F=\operatorname{conv}\{0,u,v,u+v\},
\qquad |u|=|v|=1,
\]

and let

\[
c={u+v\over2}
\]

be its center. For every point `z`, the parallelogram identity gives

\[
\sum_{p\in V(F)}|p-z|^2
=4|c-z|^2+2.
\tag{OR.6}
\]

If `z` is a source vertex but is not a vertex of `F`, then it is at distance at least one from all four vertices of `F`. Therefore

\[
4|c-z|^2+2\ge4,
\]

so

\[
\boxed{|c-z|^2\ge{1\over2}.}
\tag{OR.7}
\]

---

## 2. A crossed rhombus cannot be incident to neither endpoint

Rigidly put

\[
x=(0,0),
\qquad y=(\ell,0),
\qquad \ell=1+\varepsilon,
\qquad 0<\varepsilon\le {1\over20}.
\tag{OR.8}
\]

Let a selected row separating `x,y` meet the segment `xy` in one of its strict unit rhombi `F`, and write the rhombus center as

\[
c=(t,h).
\]

The selected midpoint-centerline segment inside `F` has length one and is centered at `c`, so

\[
\operatorname{dist}(c,xy)\le {1\over2}.
\tag{OR.9}
\]

Assume first that neither `x` nor `y` is a vertex of `F`. By (OR.7),

\[
t^2+h^2\ge {1\over2},
\qquad
(\ell-t)^2+h^2\ge {1\over2}.
\tag{OR.10}
\]

The closest point of `xy` to `c` cannot be `x` or `y`, because (OR.9) would then contradict (OR.10). Hence

\[
0\le t\le\ell,
\qquad |h|\le {1\over2}.
\tag{OR.11}
\]

Equations (OR.10)--(OR.11) imply

\[
{1\over2}\le t\le {1\over2}+\varepsilon.
\tag{OR.12}
\]

Consequently

\[
|c-x|^2,\ |c-y|^2
\le {1\over2}+\varepsilon+\varepsilon^2.
\tag{OR.13}
\]

Put

\[
\delta:=4\varepsilon+4\varepsilon^2\le {21\over100}.
\tag{OR.14}
\]

For any rhombus vertex `p`, source unit separation and (OR.6), (OR.13) give

\[
1\le |p-x|^2\le1+\delta,
\qquad
1\le |p-y|^2\le1+\delta.
\tag{OR.15}
\]

Indeed, the sum of the four squared distances from `x` is at most `4+delta`, while the other three terms are each at least one; the same argument applies at `y`.

Write `p=(a,b)`. Subtract the two squared distances:

\[
|p-x|^2-|p-y|^2=2\ell a-\ell^2,
\]

and hence

\[
\left|a-\frac\ell2\right|
\le {\delta\over2\ell}.
\tag{OR.16}
\]

Since `ell<=21/20`, `ell>=1`, and `delta<=21/100`, every rhombus vertex satisfies

\[
|a|\le {21\over40}+{21\over200}
={63\over100}.
\tag{OR.17}
\]

Using (OR.15),

\[
|b|^2\ge1-\left({63\over100}\right)^2
>{9\over16},
\]

while

\[
|b|^2\le1+\delta\le {121\over100}.
\]

Thus every one of the four rhombus vertices belongs to one of the two strips

\[
{3\over4}<b\le {11\over10}
\qquad\text{or}\qquad
-{11\over10}\le b<-{3\over4}.
\tag{OR.18}
\]

Two vertices in the same strip differ horizontally by at most `delta/ell<=21/100` and vertically by at most `7/20`. Their squared distance is therefore at most

\[
\left({21\over100}\right)^2
+
\left({7\over20}\right)^2
={833\over5000}<1.
\tag{OR.19}
\]

Source unit separation allows at most one rhombus vertex in each strip. A strict rhombus has four distinct vertices. Contradiction.

Therefore

\[
\boxed{
\text{every crossed selected-row rhombus is incident to at least one of }x,y.
}
\tag{OR.20}
\]

---

## 3. A crossed rhombus cannot be incident to exactly one endpoint

Assume `F` is incident to `x` but not to `y`; the other case is symmetric. Write

\[
F=\operatorname{conv}\{x,x+u,x+v,x+u+v\},
\qquad |u|=|v|=1,
\tag{OR.21}
\]

where the selected row uses the pair of sides parallel to `u`. Its midpoint centerline in `F` is

\[
x+{u\over2}+s v,
\qquad 0\le s\le1.
\tag{OR.22}
\]

Let

\[
e={y-x\over\ell}
\]

be the ray direction. Since `xy` meets (OR.22), `e` is parallel to a positive combination of `u` and `v`.

If the intersection has `s=0`, then `e=u`; the source vertex `x+u` lies one unit from `x` on the same ray and

\[
|y-(x+u)|=\ell-1\le {1\over20}<1,
\]

contradicting source unit separation.

Hence `s>0`. The ray lies strictly inside the angular sector at `x`. Let `alpha,beta>0` be its angles from `u,v`, respectively. If `theta` is the rhombus interior angle at `x`, then strict unit-rhombus geometry gives

\[
{\pi\over3}<\theta=\alpha+\beta<{2\pi\over3}.
\tag{OR.23}
\]

Because `y` is not a rhombus vertex, source unit separation from the two adjacent vertices gives

\[
|\ell e-u|\ge1,
\qquad
|\ell e-v|\ge1.
\tag{OR.24}
\]

Thus

\[
\cos\alpha,\cos\beta\le {\ell\over2}.
\]

Put

\[
a_0:=\arccos{\ell\over2}.
\]

Then

\[
\alpha,\beta\ge a_0,
\qquad
\alpha,\beta<{2\pi\over3}-a_0.
\tag{OR.25}
\]

Therefore

\[
\begin{aligned}
e\cdot(u+v)
&=\cos\alpha+\cos\beta\\
&>2\cos\left({2\pi\over3}-a_0\right)\\
&=2\left[-{\ell\over4}
+{\sqrt3\over2}\sqrt{1-{\ell^2\over4}}\right].
\end{aligned}
\tag{OR.26}
\]

At `ell<=21/20`,

\[
\sqrt{1-{\ell^2\over4}}
\ge {\sqrt{1159}\over40}>{17\over20},
\qquad
{\sqrt3\over2}>{6\over7}.
\]

Hence the bracket in (OR.26) is larger than

\[
-{21\over80}+{6\over7}{17\over20}
={261\over560}>{13\over28},
\]

and so

\[
\boxed{e\cdot(u+v)>{13\over14}.}
\tag{OR.27}
\]

Also (OR.23), (OR.25) imply `theta>=2a_0`, whence

\[
|u+v|=2\cos{\theta\over2}
\le2\cos a_0=\ell.
\tag{OR.28}
\]

Now consider the opposite rhombus vertex `z=x+u+v`. Equations (OR.27)--(OR.28) give

\[
\begin{aligned}
|y-z|^2
&=\ell^2+|u+v|^2-2\ell\,e\cdot(u+v)\\
&<2\left({21\over20}\right)^2-{13\over7}\\
&={487\over1400}<1.
\end{aligned}
\tag{OR.29}
\]

But `z` and `y` are distinct source vertices. Contradiction.

Thus

\[
\boxed{
\text{every crossed selected-row rhombus is incident to both }x\text{ and }y.
}
\tag{OR.30}
\]

---

## 4. Both-endpoint incidence gives a unique rhombus and one selected row

Since `|x-y|>1`, the two endpoints cannot be adjacent vertices of a unit rhombus. By (OR.30), whenever a selected row separates them they are opposite vertices of its crossed rhombus.

For fixed opposite vertices `x,y`, the other two vertices of a unit rhombus are exactly the two intersections of the unit circles centered at `x` and `y`. Hence there is only one such unit rhombus.

Inside one strict rhombus there are exactly two train midpoint-centerline segments, and they cross at the rhombus center. The selected O--O rows are pairwise-disjoint proper centerline crosscuts. Therefore at most one selected row can use this unique rhombus. This proves (OR.2).

If `u,v` are the two unit side directions, the oriented interior angle lies in `(pi/3,2pi/3)`. Either diagonal bisects the angle between `u` and `v`, or the angle between `u` and `-v`. Consequently every rhombus diagonal has projective separation

\[
\boxed{
{\pi\over6}
<d_{\mathbb{RP}^1}([xy],[u])
<{\pi\over3}
}
\tag{OR.31}
\]

from either train side direction.

---

## 5. LOWER exact-swap blockers have exactly one-row support

A LOWER witness at a one-sign strong-TB1 layer is a previously strict pair whose exact swap reaches the unit boundary. The exact-swap window gives

\[
1<|x-y|\le1+q_i,
\qquad q_i=O(D^{-1}).
\]

Thus `|x-y|<=21/20` for all sufficiently large `D`, and (OR.2) applies.

The witness actually changes under the owner-layer translation, so its endpoints lie in different physical path layers. Its exact selected-cut support is therefore nonempty. Hence

\[
\boxed{
\text{every LOWER exact-swap blocker has selected-cut support depth exactly }1.
}
\tag{OR.32}
\]

Equivalently, its two endpoints lie in adjacent path regions and are opposite vertices of the unique strict unit rhombus on the separating selected row.

---

## 6. A LOWER witness cannot block two distinct strong-TB1 layers

Suppose a previously strict pair `xy` is a LOWER exact-swap witness at two distinct one-sign strong-TB1 layers `R_i,R_j`.

The exact double-witness theorem gives

\[
|x-y|=1+O(D^{-2})
\tag{OR.33}
\]

and

\[
d_{\mathbb{RP}^1}([xy],[u_*])=O(D^{-1}),
\tag{OR.34}
\]

where `[u_*]` is the common strong-TB1 row phase.

Because the physical layers are disjoint, one endpoint lies in `R_i` and the other in `R_j`. By (OR.32), their exact path support has depth one. Therefore

\[
|i-j|=1.
\tag{OR.35}
\]

Let `tau` be the unique selected row between the two adjacent endpoint layers. It is a boundary row of both strong-TB1 interfaces. The common-grid/cone-collapse theorem puts every such robust boundary row in one projective phase interval of width `O(D^{-1})`, so

\[
d_{\mathbb{RP}^1}([\tau],[u_*])=O(D^{-1}).
\tag{OR.36}
\]

Equations (OR.34), (OR.36) imply

\[
d_{\mathbb{RP}^1}([xy],[\tau])=O(D^{-1}).
\tag{OR.37}
\]

But Section 4 says `xy` is a diagonal of the strict unit rhombus in which `tau` is crossed. Equation (OR.31) gives

\[
d_{\mathbb{RP}^1}([xy],[\tau])>{\pi\over6}.
\tag{OR.38}
\]

Contradiction for all sufficiently large `D`. This proves (OR.5).

---

## 7. Finite-swap consequences

Parity thinning is now already enough for all LOWER geometry. Two retained parity coordinates differ by at least two path layers. A LOWER singleton blocker has support depth one, so its other endpoint cannot lie in a second retained coordinate. Any lower violation created by a two-coordinate state would come from an original pair of length `1+O(D^{-1})`; (OR.2) forbids such a pair from joining two parity-retained layers.

Hence on each parity class

\[
\boxed{
\text{every LOWER obstruction is a one-coordinate forbidden vertex.}
}
\tag{OR.39}
\]

The globally bounded genuine-UPPER binary family is the only finite exceptional family that still has to be deleted before the existing Horn truth-table argument.

More importantly for the current sharp all-residue theorem, (OR.5) means a LOWER blocker extracted in two different residue systems cannot be duplicated across those systems. The existing repeated-UPPER theorem already makes UPPER cross-system duplication only `O(1)`. Thus both metric classes are globally deduplicated up to bounded UPPER exceptions.

The resulting sharp Horn and one-row ladder constants are propagated in a separate note.

**Disposition:** sharpened inverse-`D` near-unit path bandwidth from four to one, classified every LOWER exact-swap blocker as the opposite diagonal of one strict unit rhombus, and used the fixed diagonal/row angle gap to exclude repeated LOWER witnesses. C-II and Level I remain open.
