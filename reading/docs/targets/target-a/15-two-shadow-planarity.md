> Generated reading edition · [exact source](../../../../docs/targets/target-a/15-two-shadow-planarity.md) · source SHA-256 `06e5080f576dd695f4196adc225525b9f314bf65685fd1f509ce3d15f77de8f8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — planar two-shadow transport

This audited addendum follows Sections 154--162. It supplies an exact geometric
compatibility theorem for the two source shadows in the Section-155 common placement.
The main new point is that strict-conflict matching edges between unit-separated planar
sets cannot cross. Consequently, crossings between the smaller-optimum source shadow
and the lattice source shadow are not abstract: they are actual edges of the canonical
smaller-optimum/scaffold conflict graph. A second parallel-body argument shows that,
after only an explicit boundary-order loss, the common-source paths end at actual inner
scaffold sites rather than arbitrary lattice sites in the source hull.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 163. Planar two-shadow transport and common-source V-paths

## 163.1 Strict-conflict matchings are noncrossing

> **Theorem 163.1 (short matching segments are disjoint).** Let `U,V` be finite
> unit-separated subsets of the plane, and let `M` be a matching between them such
> that
> 

$$

> |u-v|<1\qquad(uv\in M).
> \tag{163.1}
> 
$$


> Then the closed straight segments `[u,v]`, `uv in M`, are pairwise disjoint.

### Proof

Suppose distinct matched segments `[u_1,v_1]` and `[u_2,v_2]` meet at `z`. Since the
two shores are unit-separated,
$$
|u_1-u_2|\ge1,
\qquad
|v_1-v_2|\ge1.
$$
Hence
$$
\begin{aligned}
2
&\le |u_1-u_2|+|v_1-v_2|\\
&\le |u_1-z|+|z-u_2|+|v_1-z|+|z-v_2|\\
&=|u_1-v_1|+|u_2-v_2|<2,
\end{aligned}
$$
a contradiction. This also excludes collinear overlap. $\square$

No generic-position hypothesis is used.

## 163.2 Cross-shadow crossings are canonical scaffold conflicts

Now enter the common placement of Section 155. Let `Lambda'` be the actual generic
unit triangular-lattice phase used for the compatible collar/scaffold of Sections 71
and 79. Section 154 applies to this prescribed phase. Put
$$
Y=\Lambda'\cap H,
\qquad
Y_{\rm in}=\Lambda'\cap\operatorname{int}(K_m+\mathbb B).
\tag{163.2}
$$
The common-placement hypothesis gives
$$
X_m\subset K_m,
\qquad
K_m+\mathbb B\subset H.
\tag{163.3}
$$
Let `M_X` be any strict-conflict matching between `X_m` and the genuine source `A`,
and `M_Y` any strict-conflict matching between `Y` and `A`.

> **Theorem 163.2 (crossing-to-scaffold transport).** Each of `M_X` and `M_Y` is a
> noncrossing straight-line matching. Suppose
> 

$$

> xa\in M_X,
> \qquad
> yb\in M_Y,
> \qquad a\ne b,
> \tag{163.4}
> 
$$


> and `[x,a]` intersects `[y,b]`. Then
> 

$$

> \boxed{|x-y|<1.}
> \tag{163.5}
> 
$$


> Therefore `y in Y_in`, and `xy` is an edge of the canonical strict-conflict graph
> `G` between `X_m` and `Y_in`.

### Proof

The separate noncrossing assertions are Theorem 163.1 applied to `X_m,A` and to
`Y,A`. If (163.4) intersects and `|x-y|>=1`, then `{x,y}` and `{a,b}` are both
unit-separated two-point sets, while `x-a` and `y-b` are a strict-conflict matching
whose segments intersect. This contradicts Theorem 163.1. Thus (163.5) holds.

Since `x in K_m`, (163.5) gives
$$
y\in\operatorname{int}(K_m+\mathbb B).
$$
Together with `y in Lambda'`, this gives `y in Y_in`; (163.5) is exactly the edge
condition in `G`. $\square$

The crossing graph is therefore a literal subgraph of the canonical scaffold conflict
graph. In particular, by the exact cell classification of Section 79, every `M_X`
edge can cross at most four `M_Y` edges, and by the lattice-side degree bound every
`M_Y` edge can cross at most five `M_X` edges.

This theorem does not infer a Schur kernel from planarity. It transports a specific
source-shadow event into an actual canonical scaffold edge.

## 163.3 Boundary-order common-source overlap

Write
$$
p=\widehat p_H,
\qquad
M=\alpha_1(H)=N+p,
\qquad
E=M-|Y|.
\tag{163.6}
$$
Sections 119 and 154 give
$$
0\le p<\frac{\pi D}{2},
\qquad
0\le E\le\frac76\operatorname{per}H+1
\le\frac{7\pi}{6}D+1.
\tag{163.7}
$$
Choose the source matchings so that
$$
|M_Y|\ge |Y|-p,
\qquad
|M_X|\ge m-p.
\tag{163.8}
$$
The second inequality is available in the Section-155 common placement.

> **Theorem 163.3 (common-source V-path theorem).** There are subsets
> `X' subset X_m`, `Y' subset Y`, a bijection `pi:X'->Y'`, and pairwise distinct
> mediators `a_x in A` such that
> 

$$

> |x-a_x|<1,
> \qquad
> |\pi(x)-a_x|<1,
> \qquad
> |x-\pi(x)|<2
> \tag{163.9}
> 
$$


> for every `x in X'`, while
> 

$$

> \boxed{|X'|\ge m-p-E.}
> \tag{163.10}
> 
$$


> Consequently
> 

$$

> \boxed{|X_m\setminus X'|\le p+E
> <\frac{5\pi}{3}D+1.}
> \tag{163.11}
> 
$$



### Proof

The matching `M_Y` leaves at most
$$
N-|M_Y|
\le N-|Y|+p
=M-|Y|
=E
\tag{163.12}
$$
source vertices unmatched. Hence at most `E` source endpoints used by `M_X` are not
also used by `M_Y`. The two source images therefore intersect in at least
$$
|M_X|-E\ge m-p-E
$$
vertices. For each common source endpoint `a`, take its unique partners `x` and `y`
in the two matchings. Matching injectivity makes the resulting `x`, `y`, and `a`
all distinct. The last inequality in (163.9) follows from the triangle inequality.
Equation (163.11) follows from (163.7). $\square$

Every mediator produced here actually lies in the open body `K_m+B`, because it is
strictly within one of its matched `x in X_m subset K_m`. The lattice partner need
not yet lie in `Y_in`; the next lemma shows that only boundary-order many partners can
fail this.

## 163.4 Inner-scaffold purification

Let
$$
P_m=\operatorname{per}K_m,
\qquad
d=\operatorname{diam}K_m<D.
\tag{163.13}
$$
The canonical perimeter bound gives `P_m<=pi d`.

> **Lemma 163.4 (width-one lattice-collar bound).** The number of lattice sites
> 

$$

> \mathcal C_2
> =\Lambda'\cap\left((K_m+2\mathbb B)
> \setminus\operatorname{int}(K_m+\mathbb B)\right)
> \tag{163.14}
> 
$$


> satisfies
> 

$$

> \boxed{
> |\mathcal C_2|
> \le\frac{8P_m}{\pi}+24
> \le8d+24
> <8D+24.
> }
> \tag{163.15}
> 
$$



### Proof

The open radius-`1/2` disks centered at the sites of `mathcal C_2` are pairwise
disjoint because the triangular lattice is unit-separated. If `y in mathcal C_2`,
then
$$
1\le\operatorname{dist}(y,K_m)\le2.
$$
Therefore every point of the open radius-`1/2` disk about `y` has distance from
`K_m` strictly between `1/2` and `5/2`. All these disks lie in the parallel-body
annulus
$$
(K_m+\tfrac52\mathbb B)
\setminus\operatorname{int}(K_m+\tfrac12\mathbb B).
$$
Steiner's formula gives this annulus area
$$
\left(\frac52-\frac12\right)P_m
+\pi\left(\frac{25}{4}-\frac14\right)
=2P_m+6\pi.
$$
Comparing areas gives
$$
|\mathcal C_2|\frac\pi4\le2P_m+6\pi,
$$
which is (163.15). $\square$

> **Corollary 163.5 (canonical inner V-path family).** The family in Theorem 163.3
> can be restricted to subsets `X'' subset X_m`, `Y'' subset Y_in` with a bijection
> and distinct source mediators satisfying (163.9), while
> 

$$

> \boxed{
> |X_m\setminus X''|
> \le p+E+\frac{8P_m}{\pi}+24
> <\left(\frac{5\pi}{3}+8\right)D+25.
> }
> \tag{163.16}
> 
$$



### Proof

For a V-path `x-a-y` from Theorem 163.3, (163.9) and `x in K_m` give
`y in K_m+2B`. If `y notin Y_in`, then `y in mathcal C_2`. Distinct paths have
distinct lattice endpoints, so Lemma 163.4 bounds the number discarded. $\square$

Thus, modulo an explicit boundary-order exceptional set, the two source shadows are
coupled inside the actual three-partite geometry
$$
X_m\;--\;A\;--\;Y_{\rm in}
$$
of the canonical scaffold.

## 163.5 Diameter-cover mass beyond the boundary allowance is rattler-mediated

Use the source decomposition from the source-backbone theorem,
$$
A=P\sqcup R,
\qquad
|P|=m,
\qquad
|R|=\rho,
\tag{163.17}
$$
and let
$$
\tau=\tau_D(A)
\tag{163.18}
$$
be the vertex-cover number of the diameter graph on `P`. The Section-155 regime has
`t=(D-d)/2>1`, so Theorem 157.1 of the source-backbone module applies with strict
conflict radius one.

> **Theorem 163.6 (rattler-mediated common shadows).** The matchings in
> Theorem 163.3 can be chosen so that there are at least
> 

$$

> \boxed{q\ge\max\{0,\tau-p-E\}}
> \tag{163.19}
> 
$$


> pairwise vertex-disjoint triples
> 

$$

> x_i-r_i-y_i,
> \qquad
> x_i\in X_m,
> \quad r_i\in R,
> \quad y_i\in Y,
> \tag{163.20}
> 
$$


> satisfying
> 

$$

> |x_i-r_i|<1,
> \qquad
> |r_i-y_i|<1,
> \qquad
> |x_i-y_i|<2.
> \tag{163.21}
> 
$$


> In particular,
> 

$$

> q>\tau-\frac{5\pi}{3}D-1.
> \tag{163.22}
> 
$$


> After requiring `y_i in Y_in`, at least
> 

$$

> \boxed{
> q_{\rm in}
> \ge\max\left\{0,
> \tau-p-E-\frac{8P_m}{\pi}-24
> \right\}
> }
> \tag{163.23}
> 
$$


> such triples remain, and hence
> 

$$

> q_{\rm in}>
> \tau-\left(\frac{5\pi}{3}+8\right)D-25.
> \tag{163.24}
> 
$$



### Proof

Choose `M_X` as in (163.8). Its edges ending in `P` form a matching in the
radius-one graph `J_1` of the source-backbone theorem. The diameter-cover obstruction
bounds the number of such edges by `m-tau`. Therefore at least
$$
|M_X|-(m-\tau)\ge\tau-p
\tag{163.25}
$$
edges of `M_X` end in genuine strict rattlers.

By (163.12), `M_Y` misses at most `E` source vertices. Hence all but at most `E` of
the rattler endpoints counted in (163.25) are also endpoints of `M_Y`. Taking their
unique partners gives (163.19)--(163.22). At most `|mathcal C_2|` of their distinct
lattice partners lie outside `Y_in`; Lemma 163.4 gives (163.23)--(163.24). $\square$

The lower bounds may be zero. The regular-shell and diameter-star possibilities remain
binding, so no super-boundary lower bound for `tau` is asserted. The exact content is
that any diameter-cover obstruction exceeding the explicit boundary allowance is now
realized by source rattlers simultaneously visible to both the smaller optimum and the
actual scaffold lattice in one embedding.

## 163.6 Exact consequence and remaining bridge

Sections 154--155 previously produced two separate near-perfect source matchings. The
new information is that those shadows have an exact planar coupling:

1. each shadow is a noncrossing straight-line matching;
2. every proper crossing between the shadows is an actual canonical scaffold conflict;
3. all but fewer than `(5 pi/3)D+1` smaller-optimum points belong to distinct
   common-source V-paths to the source-hull lattice;
4. after an explicit additional width-one collar loss, all but
   `(<(5 pi/3+8)D+25)` smaller-optimum points belong to such V-paths ending in the
   actual inner scaffold `Y_in`;
5. diameter-cover mass beyond the corresponding boundary allowance is forced through
   strict-rattler V-paths.

This survives the coherent strained-monomer regression. That regression shows that a
bounded-displacement matching, even a perfect one, does not by itself force Hall or
Schur nullity. No such inference is made here. Sections 152--153 and 156--159 are also
respected: no activation rank, KKT load, or local cage-to-response implication is used.

The exact Target A endpoint remains
$$
\boxed{\dim\ker S\ge\Delta_\Lambda-d_{\rm int}}
\tag{163.26}
$$
or an `N`-point unit-separated configuration of diameter strictly below `D`.

A sufficient next theorem is a **planar V-path transport lemma**: use the canonical
inner V-path family, the crossing-to-scaffold rule, and genuine source/global-optimality
data to force (163.26), or the exact collar Hall threshold `h(G)>=j`, or directly a
strict sub-`D` competitor. The remaining difficulty is no longer the absence of a
common embedding of the two shadows; it is extracting the required rank/capacity
saving from this planar common-source transport.
