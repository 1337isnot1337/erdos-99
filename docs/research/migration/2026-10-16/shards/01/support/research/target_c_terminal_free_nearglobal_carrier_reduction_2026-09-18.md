# Target C — terminal FREE low-`t` branch forces a diameter-one wrapping carrier

**Date:** 2026-09-18  
**Status:** proof-only Type-II/terminal-FREE research candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note combines the hostile-audited strict aggregate attachment-cell moment gap, the hostile-audited all-regime wrapping/two-half-disk dichotomy, and the complement-gap filling mechanism behind Section 130.

The new point is that the complement-gap filling argument does not need a common cell-diameter cap once an actual positive-area center-wrapping cell has already been selected. Removing that cap gives the structural threshold

\[
\boxed{t_{\rm NG}:=2+c_0=2.042089360723846\ldots},
\qquad
c_0:={\pi\over20}(2-\sqrt3).
\tag{NG.1}
\]

For any Type-II subsequence on which

\[
t_D:={q-k\over D}\longrightarrow t<t_{\rm NG},
\tag{NG.2}
\]

there is, after a further subsequence, an actual positive-area harmonic-cell sequence `P_{w,D}` whose normalized limit `K` contains the disk center in its interior and has

\[
\boxed{\operatorname{diam}(K)=1.}
\tag{NG.3}
\]

Thus every sub-`2.042089...` Type-II survivor is forced into the previously isolated near-global center-wrapping carrier branch.

The diameter-one branch also has quantitative stability. Let `{g_j}` be the complement gaps of the circle support of `K`, and put

\[
C(K):=\sum_j\sin(g_j/2).
\tag{NG.4}
\]

Then

\[
\boxed{C(K)\le t-1-c_0<1.}
\tag{NG.5}
\]

Writing

\[
\mathcal A(x):={1\over4}\left(\arcsin x-x\sqrt{1-x^2}\right),
\qquad 0\le x\le1,
\tag{NG.6}
\]

the carrier area satisfies

\[
\boxed{\operatorname{area}(K)\ge {\pi\over4}-\mathcal A(t-1-c_0).}
\tag{NG.7}
\]

Since the selected cell is locally rhombus-saturated, the same coefficient is a lower bound for its strict-rhombus area after normalization. The canonical local train budget then gives

\[
\boxed{\liminf {T_{w,D}\over D}\ge 2\left[{\pi\over4}-\mathcal A(t-1-c_0)\right],}
\tag{NG.8}
\]

and its attachment count satisfies

\[
\boxed{\liminf {a_{w,D}\over D}\ge {1\over3}\left[{\pi\over4}-\mathcal A(t-1-c_0)\right].}
\tag{NG.9}
\]

## 1. Uncapped complement-gap diameter moment

Work in the canonical Type-II full-core near-disk normalization. Suppose an actual positive-area harmonic-cell sequence `P_{w,D}` has normalized Hausdorff limit

\[
K=\operatorname{conv}(S)\subset B_{1/2},
\qquad 0\in\operatorname{int}K,
\tag{1.1}
\]

where `S` is its compact attachment support on the radius-`1/2` circle. Let `{g_j}` be the open complement gaps of `S` on that circle.

Because the center lies in the interior of `K`, every complement gap has length strictly below `pi`. The complement `B_{1/2}\setminus K` is the disjoint union, up to boundaries, of the circular segments over these gaps.

Canonical Type-II harmonic-cell tiling gives pairwise interior-disjoint cell limits, full disk-area saturation, and the square-root small-cell-tail bound. A positive-area residual convex cell cannot meet the interiors of two distinct gap segments: the segment between such two interior points would cross `int(K)`, contradicting interior disjointness. Hence every residual positive-area limit is contained in one gap segment.

Fix one positive gap `g`. After retaining a fixed positive-area cutoff and then sending the cutoff to zero, global area saturation forces the residual cells assigned to that gap to fill its complete circular-segment area

\[
G(g)={g-\sin g\over8}.
\tag{1.2}
\]

Their minimal support arcs are laminar by the canonical cap-support lemma. If the inclusion-maximal arc lengths are `theta_i`, then

\[
\sum_i\theta_i\le g
\tag{1.3}
\]

and their total available area is at most

\[
\sum_iG(\theta_i)\le G\left(\sum_i\theta_i\right)\le G(g).
\tag{1.4}
\]

For positive arguments with sum below `pi`, `G` is strictly superadditive. Equality of the actual residual area with `G(g)` therefore forces one maximal support arc of length exactly `g`. Its two endpoint attachments have chord length `sin(g/2)` in the normalized disk. Thus one residual cell assigned to this gap has normalized diameter at least `sin(g/2)`.

Distinct gaps force distinct residual cells. Summing first over any finite gap set and then using monotone convergence gives the uncapped moment bound

\[
\boxed{\liminf_{D\to\infty}{1\over D}\sum_{r\ne w}d_{r,D}\ge C(K):=\sum_j\sin(g_j/2).}
\tag{1.5}
\]

This is the geometric core of Section 130, but the common-cap hypothesis used by that endpoint package is unnecessary for (1.5): after `K` is selected, convex interior-disjointness localizes every other positive-area cell to a complement segment of `K` directly. No upper bound on the diameters of those residual cells is used.

## 2. A fixed wrapping diameter below one costs more than `2D`

Assume now

\[
\lambda:=\operatorname{diam}(K)<1,
\qquad
\theta:=2\arcsin\lambda<\pi.
\tag{2.1}
\]

Canonical Section 101 applies to this same wrapping support and its same complement-gap scalar `C(K)`, giving

\[
C(K)\ge\sin(\theta/2)+2\sin\theta=\lambda+2\sin\theta.
\tag{2.2}
\]

The carrier itself contributes `lambda D+o(D)` to the cell-diameter sum. Hence (1.5) and (2.2) give

\[
\boxed{\liminf {1\over D}\sum_r d_{r,D}\ge H(\lambda):=2\lambda+2\sin\theta=2\lambda+4\lambda\sqrt{1-\lambda^2}.}
\tag{2.3}
\]

Every center-wrapping circle support has `lambda>=sqrt(3)/2`. Write

\[
y:=\sqrt{1-\lambda^2}\in(0,1/2].
\]

Then `H(lambda)>2` is equivalent to `lambda(1+2y)>1`. After squaring, the excess is

\[
(1-y^2)(1+2y)^2-1=y(4+3y-4y^2-4y^3)>0
\tag{2.4}
\]

for `0<y<=1/2`. Therefore

\[
\boxed{H(\lambda)>2\quad\text{for every fixed center-wrapping }\lambda<1.}
\tag{2.5}
\]

This strict statement is deliberately not extended by continuity to `lambda=1`. A diameter-one wrapping support may become dense on the whole circle and have vanishing complement-gap currency. That endpoint is exactly the branch isolated below.

## 3. Spend the strict aggregate moment gap

Let

\[
S_D:=\sum_r d_{r,D}.
\]

The hostile-audited strict aggregate moment theorem gives

\[
\liminf {t_DD-S_D\over D}\ge c_0.
\tag{3.1}
\]

Hence, along any subsequence with `t_D->t`,

\[
\boxed{\limsup {S_D\over D}\le t-c_0.}
\tag{3.2}
\]

Now apply the hostile-audited all-regime Type-II cell dichotomy.

In the two-half-disk alternative there are two distinct actual defining cell sequences with `d_{1,D}/D->1` and `d_{2,D}/D->1`. Therefore `liminf S_D/D>=2`, and (3.2) forces

\[
\boxed{t\ge2+c_0=t_{\rm NG}.}
\tag{3.3}
\]

In the center-wrapping alternative with fixed diameter `lambda<1`, (2.3)--(2.5) give `liminf S_D/D>2`, so again `t>2+c_0`.

Consequently, if `t<t_NG`, both cases are impossible. The only remaining case in the exhaustive all-regime dichotomy is a positive-area center-wrapping limit of diameter exactly one. This proves (NG.3).

## 4. Stability inside the diameter-one branch

Let `K` be the diameter-one center-wrapping limit forced when `t<t_NG`. The uncapped gap moment (1.5) remains valid because center-wrapping still makes every individual gap strictly shorter than `pi`. The carrier itself contributes one unit to `S_D/D`, so

\[
\liminf S_D/D\ge1+C(K).
\tag{4.1}
\]

Combining with (3.2) gives (NG.5).

The disk area missing from `K` is exactly the sum of its complement circular-segment areas:

\[
{\pi\over4}-\operatorname{area}(K)=\sum_j{g_j-\sin g_j\over8}.
\tag{4.2}
\]

Set `x_j:=sin(g_j/2)`. Then

\[
{g_j-\sin g_j\over8}=\mathcal A(x_j),
\qquad
\sum_jx_j=C(K)\le c:=t-1-c_0<1.
\tag{4.3}
\]

A direct derivative calculation gives

\[
\mathcal A'(x)={x^2\over2\sqrt{1-x^2}},
\tag{4.4}
\]

which is increasing on `[0,1)`. Since `A(0)=0`, increasing derivative implies

\[
\mathcal A(x)+\mathcal A(y)\le\mathcal A(x+y),
\qquad x,y\ge0,\quad x+y<1.
\tag{4.5}
\]

Iterating over finite gap sets and then using monotone convergence,

\[
\sum_j\mathcal A(x_j)\le\mathcal A\left(\sum_jx_j\right)\le\mathcal A(c).
\tag{4.6}
\]

Equations (4.2)--(4.6) prove the area stability (NG.7).

Canonical Type-II local-rhombic deficit is a sum of nonnegative cell deficits and is `o(D^2)` globally. Therefore the selected carrier itself has strict-rhombus area

\[
{A_{4,w,D}\over D^2}\ge\operatorname{area}(K)-o(1).
\tag{4.7}
\]

Canonical Section 89 gives

\[
2A_{4,w,D}\le T_{w,D}d_{w,D},
\qquad
A_{4,w,D}<3a_{w,D}d_{w,D}.
\tag{4.8}
\]

Since `d_{w,D}/D->1`, (NG.8)--(NG.9) follow.

## 5. Terminal FREE specialization

The current terminal FREE t-gap certificate gives

\[
t_D\ge t_0-o(1),
\qquad
t_0=1.959852849540479\ldots .
\tag{5.1}
\]

Therefore every terminal FREE countersequence has the strengthened split

\[
\boxed{\begin{array}{ll}
\textbf{high-}t:& \liminf t_D\ge2.042089360723846\ldots,\\[1mm]
\textbf{near-global carrier}:&
1.959852849540479\ldots\le\liminf t_D<2.042089360723846\ldots,\\
&\text{and a positive-area center-wrapping harmonic cell has }d_w/D\to1.
\end{array}}
\tag{5.2}
\]

The width of this low band is

\[
0.082236511183367\ldots .
\tag{5.3}
\]

If a subsequence approaches the current lower endpoint `t_0`, (NG.5) gives

\[
C(K)\le t_0-1-c_0=0.917763488816633\ldots .
\tag{5.4}
\]

Substitution into (NG.7)--(NG.9) gives

\[
\boxed{\operatorname{area}(K)\ge0.585912522543338\ldots,}
\tag{5.5}
\]

\[
\boxed{\liminf {T_{w,D}\over D}\ge1.171825045086677\ldots,\qquad
\liminf {a_{w,D}\over D}\ge0.195304174181112\ldots.}
\tag{5.6}
\]

Thus the current low endpoint can no longer be represented by a diffuse family of ordinary macroscopic cells or by the two-half-disk equality profile. It must put at least `0.5859D^2` limiting area and strict-rhombus area into one near-global center-wrapping harmonic carrier, with at least `1.1718D` local train segments.

## 6. Scope and remaining obstruction

- The new uncapped statement is (1.5). It uses no common diameter cap, but it requires that a positive-area center-wrapping carrier has already been selected.
- The strict moment gap, the all-regime dichotomy, and the current terminal FREE `0.00659` t-gap are proof-only/audited-working inputs. This note therefore remains proof-only and does not mutate theorem state.
- At diameter exactly one, canonical Section 101's fixed-`lambda<1` complement-chord lower bound cannot simply be passed to the endpoint. A dense circle support can have arbitrarily small complement-gap currency. The argument stops there.
- No contact-isolated source point is discarded. All cells are actual attachment-cell convex hulls from the full source-level Type-II tiling.
- No source-preserving deformation is constructed.

The remaining low-`t` obstruction is now specific: a single positive-area, diameter-one, center-wrapping, locally rhombus-saturated harmonic carrier with gap currency bounded by (NG.5). Near the current `t_0` endpoint it carries at least `0.5859D^2` strict-rhombus area and `1.1718D` local train segments. A closing theorem can target this one carrier directly. The complementary branch already pays `t>=2.042089...` and should be fed into the high-`t` source-level currency/deformation machinery.

**Disposition:** proof-only low-`t` near-global-carrier reduction and quantitative area/train stability; C-II remains open.
