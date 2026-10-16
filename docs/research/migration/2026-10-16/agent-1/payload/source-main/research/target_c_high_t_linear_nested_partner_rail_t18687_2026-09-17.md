# Target C-II — linear-density nested partner rail before endpoint thinning

**Date:** 2026-09-17  
**Status:** proof-only structural strengthening; no canonical promotion claimed  
**Scope:** no-fixed-margin-TB1 exact-antipodal high-`t` shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** parameterized deep grid-force density; bilateral birth loading; one-sided common-hub support; convex diameter-thrackle property; nested partner-support rail orientation argument; source-wide diameter-degree bound; global one-sided reaction budget  
**Certificate:** `research/verify_target_c_high_t_linear_nested_partner_rail_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current partner-rainbow argument was stated after thinning the force cells until all four source endpoints of different force diamonds were disjoint. That thinning costs a factor `Theta(D^(3/4))`, leaving only `Omega(D^(1/4))` cells.

For endpoint **order**, that thinning is unnecessary.

Every selected force bar crosses the common hub cut. Its birth endpoint lies on the pre-hub shore and its other endpoint lies on the hubward shore. Birth endpoints at distinct interface tags are already distinct because they lie in occurrence-disjoint layer subarcs. Partner endpoints may repeat, but this only creates ties. Two bars with distinct partner endpoints are vertex-disjoint diameter edges and therefore cross; bars with the same partner endpoint meet there. Hence the partner map is weakly order-preserving from the birth shore to the hubward shore.

That is enough to transport the bilateral birth word and recover the same unimodal partner-region sequence at the **full linear parent density**.

---

## Theorem LNR — linear nested partner rail

Fix the parameterized deep family on one pre-hub shore,

\[
Q_D=Q_D(r;\rho,\eta,\delta),
\qquad
|Q_D|>\lambda D-o(D),
\tag{LNR.1}
\]

where

\[
\lambda=c_0-6\rho-\eta-2\delta>0,
\qquad
c_0={113\over20{,}000{,}000}.
\tag{LNR.2}
\]

Write its interface tags as

\[
i_1<i_2<\cdots<i_N<k,
\qquad N=|Q_D|,
\tag{LNR.3}
\]

with common hub region `R_k`.

At cell `i_s`, label the two selected exact-force diameter bars by birth side,

\[
e_s^+,e_s^-,
\tag{LNR.4}
\]

with birth endpoints

\[
x_s^+\in C_{i_s}^+,
\qquad
x_s^-\in C_{i_s}^-.
\tag{LNR.5}
\]

Let the other endpoints lie in regions

\[
y_s^\pm\in R_{b_s^\pm},
\qquad b_s^\pm\ge k,
\tag{LNR.6}
\]

so

\[
I_s^\pm=\{i_s+1,\ldots,b_s^\pm\}.
\tag{LNR.7}
\]

Then there is a fixed birth side

\[
\sigma\in\{+,-\}
\tag{LNR.8}
\]

such that **all `N` cells** satisfy

\[
\boxed{
b_1^\sigma\ge b_2^\sigma\ge\cdots\ge b_N^\sigma,}
\tag{LNR.9}
\]

and therefore

\[
\boxed{
I_1^\sigma\supsetneq I_2^\sigma\supsetneq\cdots\supsetneq I_N^\sigma.
}
\tag{LNR.10}
\]

Thus the exact-antipodal branch contains a nested support rail of **linear size**

\[
\boxed{
N>\lambda D-o(D),
}
\tag{LNR.11}
\]

with one selected actual diameter bar from every parameterized deep force cell.

The rail's birth endpoints are all distinct. Partner endpoints are allowed to repeat; if they do, the corresponding rail bars form a diameter star at that partner vertex. Distinct-partner rail bars cross geometrically.

---

## 1. Common hub cut gives a two-shore bipartite diameter graph

Every selected bar is born at `i_s<k` and its support interval contains the common hub cut `tau_k`. Therefore `tau_k` separates its two source endpoints:

- the birth endpoint `x_s^\pm` lies on the pre-hub boundary shore `P`;
- the partner endpoint `y_s^\pm` lies on the complementary hubward shore `Q`.

The `2N` birth endpoints are pairwise distinct. On each host side, distinct interface tags use occurrence-disjoint subarcs `C_i^\pm`; the two host sides are disjoint from each other.

The `2N` selected force bars are also distinct actual diameter edges. Their hubward endpoints need not be distinct.

---

## 2. Diameter-thrackle order survives partner collisions

Orient both boundary shores by the ambient cyclic orientation. Consider two selected bars

\[
e=pq,
\qquad e'=p'q',
\tag{LNR.12}
\]

with distinct birth endpoints `p,p' in P`, encountered in that order on `P`.

If `q=q'`, there is a partner tie and no order inversion.

If `q\ne q'`, then the two diameter bars are vertex-disjoint. Actual diameter edges of a convex source form a geometric thrackle, so `e,e'` cross. For chords joining complementary boundary intervals `P,Q`, crossing is equivalent to the partner endpoints occurring in the same ambient cyclic order on `Q`. Hence

\[
p<p'\quad\Longrightarrow\quad q\le q'
\tag{LNR.13}
\]

in the weak boundary order on `Q`, where equality means a shared partner vertex.

Therefore the edge-partner map from the ordered birth incidences on `P` to `Q` is weakly order-preserving. Within a tied partner vertex, order the incident edge labels as they occur on `P`; all tied region labels are equal, so this convention changes no path-region statement.

---

## 3. The full linear partner word is still unimodal

The bilateral birth word on `P` is, after the harmless global orientation choices,

\[
x_N^+,x_{N-1}^+,\ldots,x_1^+,
\;x_1^-,x_2^-,\ldots,x_N^-.
\tag{LNR.14}
\]

By weak order preservation, the partner incidences on `Q` occur in the same label order, allowing ties:

\[
y_N^+,y_{N-1}^+,\ldots,y_1^+,
\;y_1^-,y_2^-,\ldots,y_N^-.
\tag{LNR.15}
\]

Along `Q`, path-region labels increase weakly from `R_k` toward the far terminal region and then decrease weakly back toward `R_k`. Consequently

\[
\boxed{
(b_N^+,\ldots,b_1^+,\;b_1^-,\ldots,b_N^-)
\text{ is weakly unimodal}.}
\tag{LNR.16}
\]

The two-block orientation argument now applies without any endpoint-disjoint thinning. For a unimodal word `A|B`, either the first block `A` is nondecreasing or the second block `B` is nonincreasing. Here the first block is the `+` lane written in reverse interface order. Therefore either

\[
b_1^+\ge\cdots\ge b_N^+
\tag{LNR.17}
\]

or

\[
b_1^-\ge\cdots\ge b_N^-.
\tag{LNR.18}
\]

This proves (LNR.9), and the strict nesting (LNR.10) follows from `i_1<...<i_N<k<=b_s`.

---

## 4. A coherent-sign nested rail is still linear

The nested birth-side lane contains one of the two opposite-transverse force bars from each cell. Color its bars by transverse sign relative to the coherently oriented high-`t` row axis. One color occurs on at least half the cells.

Thus there is a coherent-sign nested subrail with

\[
\boxed{
|L_D|>{\lambda\over2}D-o(D).
}
\tag{LNR.19}
\]

Every retained bar is born at a parameterized deep force cell and therefore inherits:

- the common inverse-`D` near-triangular train grid;
- a fixed transverse derivative margin at least `2D|s|sin(delta)` in the elementary dipole coordinate;
- an exact-phase radius-`r` neighborhood at its birth interface.

No source-degree estimate is used for the linear statement.

---

## 5. Low-stress linear nested rail

Impose the global KKT quantile before the order argument. For fixed `0<sigma<1`, remove cells with

\[
B_i>{1\over\sigma\lambda D}.
\tag{LNR.20}
\]

The one-sided reaction budget removes fewer than `sigma lambda D` cells. The survivor has

\[
N_{budget}>(1-\sigma)\lambda D-o(D)
\tag{LNR.21}
\]

and every surviving cell satisfies

\[
\boxed{
B_i\le {1\over\sigma\lambda D},
\qquad
0<|G_i|\le {1\over\sigma\lambda}.
}
\tag{LNR.22}
\]

Repeat Sections 1--3 on this survivor. One entire birth-side lane is nested, so there is a low-stress nested rail of the same linear size (LNR.21). A coherent-sign subrail has size

\[
\boxed{
>{(1-\sigma)\lambda\over2}D-o(D).
}
\tag{LNR.23}
\]

The exact two-ray compressed coefficients still obey

\[
0<\lambda_i^\pm
\le {1\over\sigma\lambda D\sin\rho}.
\tag{LNR.24}
\]

The constants are independent of exact-phase depth. Hence the same linear nested rail persists on the parameterized diagonal `r_D->infinity`.

---

## 6. Recovering a genuinely endpoint-disjoint crossing rail is four times cheaper

The linear nested rail has distinct birth endpoints; only partner endpoints can collide. The source-wide diameter-degree theorem gives

\[
\Delta(H)
\le(4\,3^{1/8}+o(1))D^{3/4}.
\tag{LNR.25}
\]

Greedily choose at most one rail bar per partner vertex. Since one partner vertex is incident to at most `Delta(H)` rail bars, (LNR.11) yields an endpoint-disjoint nested subrail of size

\[
\boxed{
M_D^{disj}
>
\left({\lambda\over4\,3^{1/8}}-o(1)\right)D^{1/4}.
}
\tag{LNR.26}
\]

All bars in this subrail have disjoint endpoints and therefore cross pairwise.

If one first imposes a common transverse sign, the corresponding endpoint-disjoint nested crossing rail has

\[
\boxed{
|L_D^{disj}|
>
\left({\lambda\over8\,3^{1/8}}-o(1)\right)D^{1/4}.
}
\tag{LNR.27}
\]

These constants are four times the corresponding two-bar-bundle extraction constants because the nested order argument no longer needs to keep both force bars or all four endpoints of every cell.

For pairwise disjoint radius-`r_D` birth neighborhoods, add the usual `O(r_D)` interval-overlap conflict. On any diagonal with `r_D=o(D^(3/4))`, this does not change the leading coefficients in (LNR.26)--(LNR.27).

---

## 7. Explicit current constants

For the ninety-percent parameter choice

\[
\rho=\delta={c_0\over100},
\qquad
\eta={c_0\over50},
\qquad
\lambda={9c_0\over10}
=5.085\times10^{-6},
\tag{LNR.28}
\]

the full nested rail has more than

\[
(5.085\times10^{-6})D-o(D)
\tag{LNR.29}
\]

bars, and its coherent-sign subrail has more than

\[
(2.5425\times10^{-6})D-o(D).
\tag{LNR.30}
\]

The endpoint-disjoint nested crossing coefficients are

\[
\boxed{
{\lambda\over4\,3^{1/8}}
\approx1.10813024638\times10^{-6},
}
\tag{LNR.31}
\]

and, after imposing one common transverse sign,

\[
\boxed{
{\lambda\over8\,3^{1/8}}
\approx5.54065123188\times10^{-7}.
}
\tag{LNR.32}
\]

With the half-quantile stress pruning `sigma=1/2`, the nested rail remains linear with density

\[
2.5425\times10^{-6},
\tag{LNR.33}
\]

and

\[
B_i\le {393313.668\over D},
\qquad
0<|G_i|\le393313.668.
\tag{LNR.34}
\]

A coherent-sign endpoint-disjoint subrail of this stress-pruned family still has coefficient

\[
\boxed{
2.77032561594\times10^{-7}
}
\tag{LNR.35}
\]

in front of `D^(1/4)`.

---

## 8. Scope audit and frontier effect

This theorem does **not** claim that all rail bars cross pairwise before partner collisions are removed. Two rail bars may share a hubward diameter endpoint and then meet at that vertex. The exact statement before thinning is a nested **geometric-thrackle rail** with distinct births and a weakly ordered partner map.

Nor does the theorem prescribe a physical host side for every partner endpoint. The hubward shore may turn through the far terminal region, and partner-region labels are controlled through unimodality rather than a false four-block host-side split.

What is now forced is substantially larger than the previous `D^(1/4)` ordered braid:

```text
Theta(D) deep exact-force birth cells
+ one full birth-side lane with strictly nested support intervals
+ one coherent-transverse-sign nested sublane of linear size
+ optional B_i=O(1/D) stress control on a linear-size nested lane
+ one common inverse-D train grid
+ growing exact-phase birth neighborhoods
+ a factor-four improved endpoint-disjoint nested crossing extraction.
```

The next closure step should use this linear nested rail directly rather than immediately paying the source-degree thinning cost.

**Disposition:** lifted the partner-order/nesting mechanism from the endpoint-disjoint `Omega(D^(1/4))` braid to the full positive-linear deep-force population by allowing partner collisions as weak-order ties. C-II and Level I remain open.
