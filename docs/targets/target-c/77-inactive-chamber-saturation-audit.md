# Target C — force-hull population and inactive-chamber saturation audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module sharpens the live subquadratic-positive-core branch without importing the
historical annular Voronoi route.  It uses only finite convex-cap/Oler accounting and
canonical Sections 59, 67 and 68.

The main point is structural.  The old phrase “quadratic inactive cloud” can be
replaced by a single macroscopic convex chamber:

> if the positive contact core has `m=o(D^2)`, then one convex inactive chamber inside
> the force hull has area `Omega(D^2)`, contains `Omega(D^2)` contact-isolated source
> points, and has only `O(D)` Oler slack.

No contact-isolated source point is deleted or reclassified as KKT-positive.

---

# 77. Full-source population saturates the force hull and one inactive chamber becomes macroscopic

Use the canonical post-ZF representative and notation of Sections 59, 67 and 68.
Thus

- `A` is the full unit-separated source, `n=|A|`, `D=diam A`, and `K=conv A`;
- `G` is the connected nonisolated positive-contact core, with `m=|V(G)|`;
- `F=conv V(G)=conv B` is the full actual force hull;
- `B=Vert(F)` is the loaded actual-diameter endpoint set, `q=|B|`;
- `R_4` is the number of bounded quadrilateral contact faces;
- `f` is the number of bounded nonquadrilateral contact faces;
- `Q=sum_P(deg P-4)` over those exceptional bounded faces;
- `k=d_H+s_Z`;
- `E_4=sum_R(area(R)-a_0)` is the total strict-rhombus area excess;
- `a_0=sqrt(3)/2` and `c_0=a_0/2=sqrt(3)/4`.

Let

\[
A_F:=\operatorname{area}(F),\qquad
N_F:=|A\cap F|,\qquad
Z_{\rm ext}:=n-N_F.
\tag{77.1}
\]

Canonical Section 67 classifies every source point in `F` outside `V(G)` as
contact-isolated.  It also partitions those inactive points into

- `Z_def`, lying in bounded nonquadrilateral contact faces; and
- `Z_in`, lying in the old outer contact face but inside `F`.

Thus

\[
\boxed{N_F=m+Z_{def}+Z_{in}.}
\tag{77.2}
\]

Put

\[
Z_{ch}:=Z_{def}+Z_{in}=N_F-m.
\tag{77.3}
\]

We call the exceptional bounded faces and the convex outer pockets from Section 67.3
the **inactive chambers**.

---

## 77.1 Diameter endpoints are source-hull extreme vertices

The cap argument below needs the vertices of `F` to be actual extreme vertices of
`K`, not merely extreme in `F`.

### Lemma 77.1

Every endpoint of an actual diameter pair of `A` is an extreme point of `K`.

### Proof

Let `b,k in A` satisfy `|b-k|=D`.  If `b` were a nontrivial convex combination

\[
b=\sum_i\lambda_i a_i,\qquad
\lambda_i>0,\quad \sum_i\lambda_i=1,
\]

of at least two distinct source points, strict convexity of squared Euclidean norm
would give

\[
|b-k|^2
<\sum_i\lambda_i|a_i-k|^2
\le D^2,
\]

contradicting `|b-k|=D`.  Hence `b` is extreme.  The same argument applies to `k`.
`\square`

Therefore

\[
\boxed{B\subseteq\operatorname{Vert}(K).}
\tag{77.4}
\]

---

## 77.2 Exact exterior-cap population upper bound

List `B=Vert(F)` in cyclic source-hull order.  For each consecutive pair `u,v in B`,
compare the source-hull arc from `u` to `v` with the side `uv` of `F`.  If they differ,
the arc and chord bound a convex cap `K_i` lying outside `int F`.  Let

- `r` be the number of nondegenerate caps;
- `P_com` be the total length of sides of `F` that already lie on `partial K`;
- `A_i=area(K_i)` and `P_i=per(K_i)`; and
- `z_i` be the number of external source points assigned to `K_i`.

The cap interiors are pairwise disjoint and partition `K\setminus F` up to their
chord boundaries.  Hence

\[
\sum_i A_i=\operatorname{area}(K)-A_F,
\tag{77.5}
\]

and perimeter incidence gives

\[
\sum_iP_i=\operatorname{per}(K)+\operatorname{per}(F)-2P_{com}.
\tag{77.6}
\]

The `z_i` external points together with the two chord endpoints form a unit-separated
set in the convex cap `K_i`.  Oler therefore gives

\[
z_i+2
\le {A_i\over a_0}+{P_i\over2}+1,
\]

so

\[
z_i\le {A_i\over a_0}+{P_i\over2}-1.
\tag{77.7}
\]

Summing (77.7), (77.5) and (77.6) yields the finite cap theorem

\[
\boxed{
Z_{ext}
\le {\operatorname{area}(K)-A_F\over a_0}
+{\operatorname{per}(K)+\operatorname{per}(F)\over2}
-P_{com}-r.
}
\tag{77.8}
\]

This is the old exterior-cap identity re-proved here at the exact current scope.  No
Voronoi-cell theorem is needed.

A source point lying on a closing chord is already in `F`, hence is not counted by
`Z_ext`; omitting such points from the cap Oler set only weakens the cap inequality and
causes no double count.

---

## 77.3 Boundary-order force-hull population saturation

The canonical strict translated-lattice comparison is

\[
\boxed{a_0(n-1)>{\pi D^2\over4}.}
\tag{77.9}
\]

Multiply (77.8) by `a_0` and subtract from (77.9).  Since
`N_F=n-Z_ext`,

\[
\begin{aligned}
a_0N_F
>{}&{\pi D^2\over4}+a_0-\operatorname{area}(K)+A_F\\
&-c_0\bigl(\operatorname{per}(K)+\operatorname{per}(F)\bigr)
+a_0(P_{com}+r).
\end{aligned}
\tag{77.10}
\]

The isodiametric and Cauchy perimeter-diameter inequalities give

\[
\operatorname{area}(K)\le{\pi D^2\over4},
\qquad
\operatorname{per}(K),\operatorname{per}(F)\le\pi D.
\tag{77.11}
\]

Dropping the nonnegative cap-credit term in (77.10),

\[
\boxed{
a_0N_F>A_F-a_0\pi D+a_0.
}
\tag{77.12}
\]

Oler applied directly to all source points in `F` gives the opposite estimate

\[
\boxed{
a_0N_F
\le A_F+c_0\operatorname{per}(F)+a_0
\le A_F+c_0\pi D+a_0.
}
\tag{77.13}
\]

Therefore

\[
\boxed{a_0N_F=A_F+O(D).}
\tag{77.14}
\]

The same two inequalities on the full source hull give

\[
{\pi D^2\over4}+a_0<a_0n
\le {\pi D^2\over4}+c_0\pi D+a_0,
\tag{77.15}
\]

hence

\[
\boxed{a_0n={\pi D^2\over4}+O(D).}
\tag{77.16}
\]

Subtracting (77.14) from (77.16),

\[
\boxed{
a_0Z_{ext}={\pi D^2\over4}-A_F+O(D).
}
\tag{77.17}
\]

Thus the population inside and outside the force hull both saturate their leading area
capacities to boundary order.  This is a statement about the full source, not only the
positive core.

Canonical Section 59 gives

\[
\liminf {A_F\over D^2}
\ge A_{SC}:={2\rho+\sin(2\rho)\over4},
\qquad \rho=\cos\rho.
\tag{77.18}
\]

Consequently

\[
\boxed{
\liminf {N_F\over D^2}
\ge {A_{SC}\over a_0}
={2A_{SC}\over\sqrt3}
=0.714148\ldots .
}
\tag{77.19}
\]

The decimal is only for scale; the theorem is the exact expression in (77.19).

---

## 77.4 The inactive chambers themselves saturate Oler capacity

Let

\[
A_4:=\sum_{R\text{ quadrilateral}}\operatorname{area}(R)
=a_0R_4+E_4.
\tag{77.20}
\]

Let `C_1,...,C_s` be all inactive chambers: the `f` exceptional bounded faces and the
`a` convex outer pockets of Section 67.3.  Write

\[
A_j:=\operatorname{area}(C_j),
\qquad
P_j:=\operatorname{per}(C_j),
\qquad
z_j:=\#\{\text{assigned contact-isolated source points in }C_j\}.
\tag{77.21}
\]

They tile exactly the part of `F` not occupied by bounded quadrilateral faces, so

\[
\boxed{A_{ch}:=\sum_jA_j=A_F-A_4.}
\tag{77.22}
\]

Their assigned inactive population is

\[
\boxed{Z_{ch}:=\sum_jz_j=N_F-m.}
\tag{77.23}
\]

Section 67's exact face identity is

\[
\boxed{m=R_4+f+q-k+1.}
\tag{77.24}
\]

Subtract (77.20) from `a_0` times (77.24):

\[
\boxed{
a_0m-A_4=a_0(f+q-k+1)-E_4.
}
\tag{77.25}
\]

Every term on the right is boundary order.  Indeed

- `q<=per(F)<=pi D`;
- `b+Q=2(h-s_Z)` implies `s_Z<=h<=q` and `Q<=2h<=2pi D`;
- `d_H<=q`, hence `k=d_H+s_Z<=2q<=2pi D`;
- `f<=Q<=2pi D`; and
- canonical Section 68 gives `E_4=O(D)`.

Thus

\[
\boxed{a_0m-A_4=O(D).}
\tag{77.26}
\]

Now subtract (77.26) from the force-hull population saturation (77.14):

\[
\begin{aligned}
a_0Z_{ch}-A_{ch}
&=(a_0N_F-A_F)-(a_0m-A_4)\\
&=O(D).
\end{aligned}
\]

Hence

\[
\boxed{a_0Z_{ch}=A_{ch}+O(D).}
\tag{77.27}
\]

So the inactive part of the source saturates the inactive-chamber area to boundary
order even when the positive core is not subquadratic.

---

## 77.5 Total inactive-chamber perimeter and total Oler slack are boundary order

For the exceptional bounded faces, all boundary edges are unit contacts, so

\[
\sum_{j\in exc}P_j=4f+Q\le5Q\le10\pi D.
\tag{77.28}
\]

For the outer pockets, Section 67 gives

\[
\sum_{j\in out}P_j=b+2L_{add}-\operatorname{per}(F),
\tag{77.29}
\]

and

\[
\operatorname{per}(F)=q-a+L_{add}.
\tag{77.30}
\]

Therefore

\[
\sum_{j\in out}P_j
=b+\operatorname{per}(F)-2q+2a
\le b+\operatorname{per}(F)
\le3\pi D,
\tag{77.31}
\]

because `a<=q`, `b<=2h<=2pi D`, and `per(F)<=pi D`.  Hence

\[
\boxed{P_{ch}:=\sum_jP_j\le13\pi D.}
\tag{77.32}
\]

The number of chambers is also boundary order:

\[
s=f+a\le Q+q\le3\pi D.
\tag{77.33}
\]

For each chamber define the isolate-only Oler slack

\[
\sigma_j:={A_j\over a_0}+{P_j\over2}+1-z_j\ge0.
\tag{77.34}
\]

Summing and using (77.27), (77.32), and (77.33),

\[
\begin{aligned}
\Sigma_{ch}:=\sum_j\sigma_j
&={A_{ch}\over a_0}+{P_{ch}\over2}+s-Z_{ch}\\
&=O(D).
\end{aligned}
\]

Thus

\[
\boxed{0\le\Sigma_{ch}=O(D).}
\tag{77.35}
\]

This is stronger than a total population estimate: the sum of all individual convex
chamber capacity deficits is only boundary order.

---

## 77.6 Subquadratic positive core forces one macroscopic inactive chamber

Assume now the live subquadratic-core branch

\[
\boxed{m=o(D^2).}
\tag{77.36}
\]

Since every strict unit rhombus has area at most one and `R_4<=m`,

\[
A_4\le R_4\le m=o(D^2).
\tag{77.37}
\]

Using (77.18), (77.22), and (77.37),

\[
\boxed{
\liminf {A_{ch}\over D^2}\ge A_{SC}>0.
}
\tag{77.38}
\]

Likewise (77.19), (77.23), and `m=o(D^2)` give

\[
\boxed{
\liminf {Z_{ch}\over D^2}\ge {A_{SC}\over a_0}>0.
}
\tag{77.39}
\]

Now let

\[
A_{max}:=\max_jA_j.
\]

The planar isoperimetric inequality gives

\[
\sqrt{A_j}\le {P_j\over2\sqrt\pi}.
\]

Hence, by (77.32),

\[
\sum_j\sqrt{A_j}
\le{P_{ch}\over2\sqrt\pi}
\le {13\sqrt\pi\over2}D.
\tag{77.40}
\]

But

\[
A_{ch}=\sum_jA_j
\le \sqrt{A_{max}}\sum_j\sqrt{A_j}.
\]

Combining with (77.38)--(77.40),

\[
\boxed{
\liminf {A_{max}\over D^2}
\ge
\left({2A_{SC}\over13\sqrt\pi}\right)^2
={4A_{SC}^2\over169\pi}>0.
}
\tag{77.41}
\]

Choose a chamber `C_*` attaining `A_max`, and let `z_*` and `sigma_*` be its assigned
isolated population and Oler slack.  Since every `sigma_j>=0`, (77.35) gives
`sigma_*=O(D)`.  Also `P_*=O(D)` by (77.32).  Therefore

\[
z_*
={A_{max}\over a_0}+{P_*\over2}+1-\sigma_*
={A_{max}\over a_0}+O(D).
\tag{77.42}
\]

Together with (77.41),

\[
\boxed{
\liminf {z_*\over D^2}
\ge {1\over a_0}{4A_{SC}^2\over169\pi}>0.
}
\tag{77.43}
\]

Thus one convex inactive chamber has simultaneously

\[
\boxed{
\operatorname{area}(C_*)=\Omega(D^2),
\quad
z_*=\Omega(D^2),
\quad
\sigma_*=O(D),
\quad
\operatorname{per}(C_*)=O(D).
}
\tag{77.44}
\]

By isodiametry, it also has `diam(C_*)=Omega(D)`.

Every point counted by `z_*` is an actual source point and is contact-isolated in the
full-support canonical contact graph.  The chamber is either one convex exceptional
bounded contact face or one convex outer pocket.  This is not an averaged or virtual
container.

---

## 77.7 What this changes and what remains open

Section 77 turns the subquadratic-core branch into the concrete endpoint

```text
m=o(D^2)
  -> force-hull source population is quadratic
  -> inactive chambers collectively have area Theta(D^2),
     total perimeter O(D), and total Oler slack O(D)
  -> one actual convex inactive chamber C_* has
       area Omega(D^2),
       Omega(D^2) contact-isolated source points,
       perimeter O(D),
       Oler slack O(D).
```

This is strictly stronger than saying only that a quadratic inactive population may
exist somewhere in `F`.

It still does **not** settle C-II.  A near-triangular unit-separated packing in a
macroscopic convex chamber can have only boundary-order Oler slack while avoiding exact
unit contacts by `o(1)` perturbations.  The next missing theorem must use global
minimal-diameter coupling to the chamber boundary, not density alone.  Plausible exact
endpoints are:

1. a protected chamber replacement that preserves all cross-boundary distances while
   creating a strict sub-`D` source;
2. a second-order stability theorem showing that a contact-isolated chamber with
   `Omega(D^2)` points must spend more than `O(D)` packing slack; or
3. a coupling between the chamber's boundary core and its near-capacity population
   that forces a forbidden unit triangle.

No such final implication is claimed here.

---

## 77.8 Dependency audit

The proof uses only:

- canonical Section 59 (`C-FS-STABILITY`) for the force-hull area floor and standard
  `q<=per(F)<=pi D` consequences;
- canonical Section 67 (`C-RHOMBUS-POP`) for the exact face identity, convex chamber
  decomposition, full-source classification in `F`, and outer-pocket perimeter
  identities;
- canonical Section 68 (`C-PUNCTURED-PHASE`) for `E_4=O(D)`;
- the canonical strict translated-lattice comparison and finite Oler inequality; and
- standard convex isodiametric, isoperimetric, and Cauchy perimeter-diameter
  inequalities.

The historical annular Voronoi theorem AV, the rejected Reuleaux-cap route, any KKT
coefficient lower bound, and Sections 70--76 are not proof dependencies.

**Disposition:** canonical as `C-INACTIVE-CHAMBER`; see `docs/state/theorem-state.yaml` for lifecycle authority. Level I and C-II remain open.
