<!-- theorem-state: {"artifact_id":"ART-6A8C08C53DFE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — prescribed-phase Hall shadow and hull-alignment coupling

**Date:** 2026-08-30
**Repository state:** `research/bhs-scale-activation-regression-2026-08-30`, rebased through active v1.7.3 / Section 153
**Run type:** closing reduction / exact geometric transport
**Target:** A
**Active prompt:** `docs/prompts/erdos_problem_99_1.7.3_FINAL_CONTINUATION_PROMPT.md`
**External web search:** used only for the classical Bonnesen inequality, recorded below
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This report strengthens the capacity-shadow route in two ways.

First, the prescribed triangular-lattice phase does **not** require zero source-hull slack. The exact same-source Hall budget already gives an `O(D)`-defect matching from every prescribed lattice phase into the genuine source, while preserving the original source representative and its strict-rattler population.

Second, the apparent coordinate independence between the source hull and the independently chosen smaller optimum disappears in the very-super-boundary regime. A Bonnesen stability estimate puts both the source hull and the compatible scaffold container within `O(sqrt(D))` Hausdorff distance after a rigid placement. Once the Target A collar width is larger than that error, the whole one-unit scaffold interaction neighborhood `K_m + B` can be placed inside the actual source hull. The exact source Hall theorem then applies directly to both the smaller optimum and the inner scaffold lattice sites.

This does not yet imply the Schur nullity. It does produce a genuine global source-to-independent-scaffold coordinate coupling in the subbranch `rho >= C D^(3/2)`.

---

## 1. Starting endpoint

The exact Target A closure remains

\[
\boxed{\dim\ker S\ge \Delta_\Lambda-d_{\rm int}},
\]

equivalently

\[
\boxed{\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.}
\]

Use the canonical notation for the genuine source

\[
A\subset H=\operatorname{conv}A,
\qquad |A|=N,
\qquad \operatorname{diam}H=D,
\]

and its exact hull capacity

\[
M=\alpha_1(H)=N+\widehat p_H.
\]

Canonical Theorem 119.2 gives, for every finite unit-separated `Q subset H`,

\[
\boxed{|Q|-|N_A(Q)|\le\widehat p_H,}
\tag{1.1}
\]

with

\[
0\le\widehat p_H<\frac{\pi D}{2}.
\tag{1.2}
\]

For the independently chosen smaller optimum use

\[
|X_m|=m=N-\rho,
\qquad
K_m=\operatorname{conv}X_m,
\qquad
d=D(m),
\qquad
t=\frac{D-d}{2},
\]

and the compatible scaffold container

\[
L=K_m+t\mathbb B.
\tag{1.3}
\]

Canonical (63.8) gives

\[
\boxed{
t>
\frac{c}{4D}
\left(\rho-\frac{\pi D}{2}\right),
\qquad c=\frac{2\sqrt3}{\pi}.
}
\tag{1.4}
\]

---

## 2. Prescribed-phase Hall shadow with the exact source slack

Let

\[
\Lambda' = R\Lambda+v
\]

be **any** rotated and translated unit triangular lattice and put

\[
Y=\Lambda'\cap H.
\]

Let

\[
a_0=\frac{\sqrt3}{2},
\qquad
r_\Lambda=\frac1{\sqrt3}
\]

be the fundamental-cell area and covering radius of the unit triangular lattice.

> **Theorem A (prescribed-phase source Hall shadow).** For every prescribed triangular-lattice phase `Lambda'`:
>
> 1. the maximum matching in the strict conflict graph on `Y sqcup A`,
>    \[
>    y\sim a\iff |y-a|<1,
>    \]
>    has size
>    \[
>    \boxed{\nu(Y,A)\ge |Y|-\widehat p_H;}
>    \tag{2.1}
>    \]
> 2. every phase satisfies the deterministic lattice-count lower bound
>    \[
>    \boxed{|Y|\ge
>    \frac{\operatorname{area}H-r_\Lambda\operatorname{per}H}{a_0};}
>    \tag{2.2}
>    \]
> 3. writing `P_H=per(H)`,
>    \[
>    \boxed{
>    0\le M-|Y|\le\frac76P_H+1
>    \le\frac{7\pi}{6}D+1;
>    }
>    \tag{2.3}
>    \]
> 4. consequently there is a partial bijection between source points and lattice sites at distance `<1` leaving at most
>    \[
>    \boxed{\widehat p_H<\frac{\pi D}{2}}
>    \tag{2.4}
>    \]
>    lattice sites unmatched and at most
>    \[
>    \boxed{M-|Y|\le\frac76P_H+1}
>    \tag{2.5}
>    \]
>    source points unmatched.

### Proof

For every `Q subset Y`, the set `Q` is unit-separated and lies in `H`, so (1.1) applies:

\[
|Q|-|N_A(Q)|\le\widehat p_H.
\tag{2.6}
\]

The deficiency form of Hall's theorem therefore gives

\[
|Y|-\nu(Y,A)
=
\max_{Q\subseteq Y}\bigl(|Q|-|N_A(Q)|\bigr)
\le\widehat p_H,
\]

which is (2.1).

For (2.2), let

\[
H_{-r}=\{x\in H:\operatorname{dist}(x,\partial H)\ge r\}.
\]

Every point of the plane lies within `r_Lambda` of a lattice site. If `x in H_{-r_Lambda}` and `y` is a nearest lattice site, then `y in H`; hence `x` lies in the full Voronoi cell of some `y in Y`. The full triangular-lattice Voronoi cells have disjoint interiors and area `a_0`, so

\[
\operatorname{area}(H_{-r_\Lambda})\le a_0|Y|.
\tag{2.7}
\]

For a convex body the inner parallel perimeters are nonincreasing. The coarea formula gives

\[
\operatorname{area}H-\operatorname{area}(H_{-r})
=\int_0^r\operatorname{per}(H_{-s})\,ds
\le rP_H,
\tag{2.8}
\]

with the same inequality after the inner body becomes empty. Taking `r=r_Lambda` and combining (2.7)--(2.8) proves (2.2).

Now Oler's finite packing inequality applied to a capacity endpoint in `H` gives

\[
M\le\frac{\operatorname{area}H}{a_0}+\frac{P_H}{2}+1.
\tag{2.9}
\]

Subtract (2.2). Since

\[
\frac{r_\Lambda}{a_0}=\frac23,
\]

we obtain

\[
M-|Y|
\le\left(\frac12+\frac23\right)P_H+1
=\frac76P_H+1,
\]

and Cauchy's perimeter-diameter inequality gives `P_H <= pi D`. This proves (2.3).

Finally a maximum matching leaves `|Y|-nu <= p_hat_H` lattice sites unmatched. It leaves

\[
N-\nu
\le N-|Y|+\widehat p_H
=M-|Y|
\]

source points unmatched, proving (2.4)--(2.5). \(\square\)

### Exact significance

Canonical Theorem 126.1 matches the genuine source into an arbitrarily chosen full capacity endpoint. Theorem A is different: the triangular-lattice phase is chosen **in advance**. In particular it may be the phase used later by the Target A scaffold.

Unlike the previous zero-slack formulation, Theorem A preserves the original source, its cardinality, and its strict-rattler population. The price is exactly the canonical hull slack `p_hat_H`, already known to be boundary-order.

---

## 3. Generic co-phased monomer/dimer bulk with slack

Assume now that the prescribed lattice phase is generic for `A`: no source point lies on the lattice and no source-lattice distance is exactly one. Put

\[
A_\partial=
\{a\in A:\operatorname{dist}(a,\partial H)\le1\},
\qquad b=|A_\partial|.
\]

Canonical (72.12) gives

\[
\boxed{b\le\frac{12P_H}{\pi}+9\le12D+9.}
\tag{3.1}
\]

> **Corollary A.1 (generic source monomer/dimer bulk).** Every `a in A setminus A_partial` has its complete infinite-lattice strict neighborhood inside `Y`; that neighborhood has exactly three or four sites and forms respectively one elementary triangular-lattice triangle or one unit lozenge. The corresponding cell contains `a` in its interior, and distinct deep source cells have disjoint interiors.
>
> Furthermore, if
> \[
> Z=\{y\in Y:N_A(y)\subseteq A_\partial\}
> \]
> is the set of lattice sites having no deep source conflict, then
> \[
> \boxed{|Z|\le b+\widehat p_H.}
> \tag{3.2}
> \]

### Proof

For a deep source point, every lattice site at distance `<1` lies in `H`, so its neighborhood in `Y` equals its full neighborhood in the infinite triangular lattice. The exact 3/4-neighbor classification and disjoint-cell argument are canonical Theorems 79.1--79.2.

For `Z`, the exact source Hall inequality gives

\[
|Z|-|N_A(Z)|\le\widehat p_H.
\]

By definition `N_A(Z) subset A_partial`, so `|N_A(Z)| <= b`. This proves (3.2). \(\square\)

Thus **every prescribed generic phase** has a common source-side crystalline alphabet except for only `O(D)` source and lattice exceptions. This statement no longer depends on rebuilding to a zero-slack source.

### Corollary A.2 (source radial-cycle identity)

Let `m_3,m_4` be the numbers of deep source points with three and four lattice conflicts. Let `e_partial` be the total degree in the source-lattice strict conflict graph contributed by `A_partial`, let `gamma` be the number of graph components including isolated vertices, and put

\[
\delta=|Y|-N.
\]

The straight strict-conflict graph is planar by the canonical crossing argument. Its cyclomatic number, equivalently its number `mu` of bounded radial faces, is exactly

\[
\boxed{
\mu
=m_3+2m_4+e_\partial-2b-\delta+\gamma.
}
\tag{3.3}
\]

Since every generic source point has at most four full-lattice strict neighbors,

\[
0\le e_\partial\le4b.
\]

Together with (2.3), (1.2), and (3.1), this gives

\[
\boxed{
\mu=m_3+2m_4+\gamma+O(D).
}
\tag{3.4}
\]

Equation (3.3) is the source analogue of the scaffold branch-versus-cycle bookkeeping in Section 80. It is **not** itself a contradiction: the known monomer and dimer crystalline regressions can realize local branch charge by local cycle cancellation.

---

## 4. Bonnesen stability at the minimum-diameter scale

The next obstruction is coordinate placement. The source hull `H` and the independent scaffold container `L=K_m+tB` have the same diameter `D` but are not canonically aligned.

The required external input is the classical Bonnesen inequality. Daniel A. Klain, *An Error Estimate for the Isoperimetric Deficit*, Illinois Journal of Mathematics 49 (2005), 981--992, Section 4, equation (6), records the following classical theorem for compact convex planar sets:

> If `K` has perimeter `P`, area `A`, circumradius `R`, and inradius `r`, then
> \[
> \boxed{P^2-4\pi A\ge\pi^2(R-r)^2.}
> \tag{4.1}
> \]

The hypotheses match both convex bodies used below exactly.

Put

\[
\eta(D)=3^{1/4}\sqrt D.
\tag{4.2}
\]

> **Theorem B (minimum-diameter hull stability and alignment).** Both the genuine source hull `H` and the compatible scaffold container
> \[
> L=K_m+t\mathbb B
> \]
> admit circumcenters `c_H,c_L` such that, after translating the body to put its circumcenter at the origin,
> \[
> \boxed{
> B\left(0,\frac D2-2\eta(D)\right)
> \subseteq K
> \subseteq
> B\left(0,\frac D2+\eta(D)\right).
> }
> \tag{4.3}
> \]
> Consequently, after translating `L` so that `c_L=c_H`,
> \[
> \boxed{d_H(H,L)\le3\eta(D).}
> \tag{4.4}
> \]
> In particular
> \[
> \boxed{L\ominus3\eta(D)\mathbb B\subseteq H.}
> \tag{4.5}
> \]

### Proof for the source hull

Let `P=per(H)` and `A_H=area(H)`. Canonical (114.21) gives

\[
N-1-\frac{D^2}{c}>0.
\]

Oler therefore yields

\[
\begin{aligned}
A_H
&\ge a_0(N-1)-c_0P\\
&>a_0\frac{D^2}{c}-c_0\pi D\\
&=\frac{\pi D^2}{4}-c_0\pi D,
\end{aligned}
\tag{4.6}
\]

where `c_0=sqrt(3)/4`. Since `P<=pi D`,

\[
P^2-4\pi A_H
<4\pi^2c_0D
=\pi^2\sqrt3\,D.
\tag{4.7}
\]

Bonnesen (4.1) gives

\[
R-r<3^{1/4}\sqrt D=\eta(D).
\tag{4.8}
\]

Any containing disk has radius `R>=D/2`, while an inscribed disk has `r<=D/2`. Hence

\[
R\le\frac D2+\eta,
\qquad
r\ge\frac D2-\eta.
\tag{4.9}
\]

Let `c` and `a` be centers of a minimum circumscribed disk and a maximum inscribed disk. Since `B(a,r) subset B(c,R)`,

\[
|a-c|\le R-r<\eta.
\tag{4.10}
\]

Therefore

\[
B\left(c,r-|a-c|\right)
\subseteq H
\subseteq B(c,R),
\]

and the inner radius is larger than `D/2-2eta`. This proves (4.3) for `H`.

### Proof for the scaffold container

Canonical parallel-body identity (63.5) writes

\[
\operatorname{area}L
=\frac{\pi D^2}{4}-\delta_m-\varepsilon_mt,
\]

and canonical (63.6) gives

\[
\delta_m+\varepsilon_mt<c_0\pi D.
\tag{4.11}
\]

Also

\[
\operatorname{per}L
=P_m+2\pi t
\le\pi d+2\pi t
=\pi D.
\tag{4.12}
\]

Thus the identical estimate (4.7) holds for `L`. The same Bonnesen argument proves (4.3) for `L`.

After aligning circumcenters, both bodies contain the disk of radius `D/2-2eta` and lie in the disk of radius `D/2+eta`. Every point of either body is therefore within distance at most `3eta` of the common inner disk contained in the other body. This proves (4.4).

For convex compact sets, Hausdorff distance at most `h` is equivalent to

\[
|h_H(u)-h_L(u)|\le h
\qquad(|u|=1).
\]

If `x in L ominush B`, then

\[
x\cdot u+h\le h_L(u)
\]

for every unit `u`, so

\[
x\cdot u\le h_L(u)-h\le h_H(u).
\]

Hence `x in H`, proving (4.5). \(\square\)

---

## 5. Direct source-to-smaller-optimum coupling for `rho` above `D^(3/2)`

For a convex body `K` and `0<=h<=t`,

\[
(K+t\mathbb B)\ominus h\mathbb B
=K+(t-h)\mathbb B.
\tag{5.1}
\]

Apply this to `L=K_m+tB` and `h=3eta(D)`. If

\[
\boxed{t\ge1+3\eta(D),}
\tag{5.2}
\]

then Theorem B gives, after a rigid placement of the independently chosen smaller optimum,

\[
\boxed{K_m+\mathbb B\subseteq H.}
\tag{5.3}
\]

In particular both

\[
X_m\subset H
\]

and the entire inner scaffold lattice shore

\[
Y_{\rm in}
=\Lambda_v\cap\operatorname{int}(K_m+\mathbb B)
\subset H
\tag{5.4}
\]

live in the genuine source hull.

Combining (1.4) with (5.2), the explicit sufficient rattler threshold is

\[
\boxed{
\rho
\ge
\frac{\pi D}{2}
+\frac{4D}{c}
\left(1+3\,3^{1/4}\sqrt D\right).
}
\tag{5.5}
\]

> **Corollary B.1 (very-super-boundary coordinate coupling).** Under (5.5), the independently chosen smaller optimum and the inner scaffold may be rigidly placed inside the actual source hull so that the exact source Hall theorem applies directly. In particular,
> \[
> \boxed{
u(X_m,A)\ge m-\widehat p_H,}
> \tag{5.6}
> \]
> and
> \[
> \boxed{
u(Y_{\rm in},A)\ge |Y_{\rm in}|-\widehat p_H.}
> \tag{5.7}
> \]
> Thus all but `O(D)` points of the independent smaller optimum, and all but `O(D)` inner scaffold lattice sites, can be matched injectively to genuine source points at displacement `<1`.

### Proof

Once (5.3)--(5.4) hold, `X_m` and `Y_in` are unit-separated subsets of `H`. Apply (1.1) to every subset of either shore and use the deficiency form of Hall's theorem exactly as in Theorem A. \(\square\)

This is a genuine source-to-independent-scaffold transport statement. It uses:

1. global minimum-diameter optimality through the source and smaller-optimum area estimates;
2. the exact source hull Hall budget;
3. the compatible collar relation `D=d+2t`; and
4. a quantitative convex-body stability theorem.

It is therefore not contradicted by the non-global Section 152 regression or by the Section 153 zero-KKT-load theorem.

---

## 6. What this advances, and what it does not

### Advanced quantity

The canonical capacity-shadow route previously had a coordinate-identification gap: the genuine source and independently chosen smaller optimum/scaffold were only logically simultaneous.

Corollary B.1 removes that gap completely in the subbranch (5.5). There is now an actual bounded-displacement matching between the genuine source and all but `O(D)` points of `X_m`, and likewise between the source and all but `O(D)` inner scaffold lattice sites, in one common Euclidean placement.

The remaining Target A problem in this very-super-boundary regime is therefore **not** source/scaffold coordinate independence. It is the exact conversion of these two near-perfect source matchings into

\[
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}
\]

or into a strict sub-`D` replacement.

### Why this does not already close the branch

The two matchings in (5.6)--(5.7) need not be compatible with each other. They do not identify the same source point with both an `X_m` point and a lattice site, and they do not force the original strict rattlers to be the unmatched source vertices. Section 152 warns that coherent local monomer incidence can coexist with zero nullity; Section 153 warns that the activation forest carries zero KKT multiplier in the canonical activation normalization.

Moreover, Bonnesen stability is only `O(sqrt(D))` in Hausdorff distance from the present `O(D)` isoperimetric deficit. Eroding the outer scaffold by that amount loses a potentially `O(D^(3/2))` boundary population. That is too large for the exact `O(D)` one-integer Target A endpoint. Hence this argument does not reduce the full super-boundary regime `rho/D -> infinity` to one container; it only reaches the stronger scale (5.5).

This `sqrt(D)` versus boundary-order mismatch is now an exact quantitative obstruction rather than an informal shape-alignment issue.

---

## 7. Regression audit

| Regression / warning | Result | Exact reason |
| --- | --- | --- |
| Section 152 activation/monomer family | passed | Theorem A uses genuine source hull capacity; Theorem B uses global-minimizer area bounds. |
| Section 153 universal zero-KKT activation theorem | passed | No positive KKT multiplier is used anywhere. |
| two-leaf locked cage | passed | The theorem does not perturb locked transition triangles. |
| full-rank planar response examples | passed | Planarity is used only for the source radial-cycle identity, not to infer Schur nullity. |
| independent source/scaffold coordinates | partially eliminated | Eliminated under the explicit scale (5.5), still open below that scale. |
| local monomer/dimer crystalline cancellation | passed | Corollary A.2 explicitly permits large cycle cancellation and claims no local nullity. |
| fixed-hull Hall-capacity ceiling | passed | Every matching defect is bounded by, not made larger than, `p_hat_H`. |

---

## 8. Literature imported

### Daniel A. Klain, “An Error Estimate for the Isoperimetric Deficit”

- Journal: *Illinois Journal of Mathematics* 49 (2005), 981--992.
- Exact point used: Section 4, equation (6), classical Bonnesen inequality.
- Hypotheses: compact convex planar set; perimeter `P`, area `A`, circumradius `R`, inradius `r`.
- Conclusion: `P^2-4 pi A >= pi^2(R-r)^2`.
- Applicability: exact. Both `H` and `L` are compact convex planar bodies.
- Role: converts the canonical `O(D)` isoperimetric area deficit into an `O(sqrt(D))` annular-thickness/Hausdorff bound.

No other external theorem is imported.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

Theorem A is an elementary but useful strengthening of the existing capacity-shadow theorem. Theorem B imports one standard convex-geometry inequality and then uses only canonical estimates. Corollary B.1 changes the frontier for the `rho >= C D^(3/2)` subbranch, but it still does not prove the required Schur rank loss.

If audited, the natural canonical placement is a post-Section-153 Target A addendum, with the active prompt updated to say that capacity-shadow coordinate independence is already removed above the explicit `D^(3/2)` rattler scale.

---

## 10. Exact next lemma

The next theorem should exploit the fact that, under (5.5), **both** `X_m` and `Y_in` have matchings into the same genuine source with only `O(D)` defects.

A precise target is:

> **Two-shadow compatibility lemma.** In the setting of Corollary B.1, prove that the two source matchings can be chosen or exchanged so that their overlap produces either
> \[
> \dim\ker S\ge\Delta_\Lambda-d_{\rm int}
> \]
> or an `N`-point unit-separated configuration of diameter `<D`.

Any proof must use more than local monomer incidence and more than KKT stress weights. Natural remaining data are the transversal-matroid exchange structure of the two source conflict graphs, the critical cone of the genuine source, and the exact boundary-order defect sets.

A second, independent route is to improve the `O(sqrt(D))` hull-alignment error. To affect the exact `O(D)` Target A deficit, one would need an `O(1)`-scale or otherwise boundary-order population loss, and the present scalar area/perimeter estimates do not provide that.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New Theorem A:
For the genuine source A in H with exact hull slack p_hat_H, every prescribed
triangular-lattice phase Y=Lambda_v intersect H satisfies

    nu(Y,A) >= |Y|-p_hat_H,
    M-|Y| <= (7/6) per(H)+1,

where M=alpha_1(H). Thus every prescribed phase has an O(D)-defect bounded-displacement
shadow in the original source; zero slack is not needed. For a generic phase, all but
O(D) source points have exact triangular-lattice monomer/dimer cells, and all but
O(D) lattice sites see a deep source cell.

New Theorem B:
Using Oler + the canonical strict lattice defect and the classical Bonnesen inequality,
both the genuine source hull H and compatible scaffold container L=K_m+tB have,
after circumcenter normalization,

    B(0,D/2-2*3^(1/4)*sqrt(D)) subset K
      subset B(0,D/2+3^(1/4)*sqrt(D)).

Hence H and L can be rigidly aligned with Hausdorff distance <=3*3^(1/4)*sqrt(D).

If

    rho >= pi D/2 + (4D/c)(1+3*3^(1/4)*sqrt(D)),

then t>=1+3*3^(1/4)*sqrt(D), so K_m+B can be placed inside H. Consequently

    nu(X_m,A) >= m-p_hat_H,
    nu(Y_in,A) >= |Y_in|-p_hat_H.

This removes the source/scaffold coordinate-independence obstruction in the
rho = Omega(D^(3/2)) subbranch. It does not yet force Schur nullity because the two
near-perfect source matchings need not be mutually compatible.

Exact next lemma:
Use the two O(D)-defect matchings into the same genuine source to force the Schur
kernel bound or a strict sub-D competitor.
```
