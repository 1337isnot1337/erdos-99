> Generated reading edition · [exact source](../../../../docs/targets/target-a/08-prescribed-phase-alignment.md) · source SHA-256 `de6abaaaac9207cb295129edc4b578e5afed484af2baa3038071575330eb1e07`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target A — prescribed-phase shadow and very-super-boundary alignment

This audited addendum records a source-to-scaffold coupling theorem valid in the
very-super-boundary subbranch. It strengthens the capacity-shadow route, but does not
prove the Target A Schur inequality.

**LEVEL I STATUS: STILL OPEN.**

## 154. Prescribed-phase Hall shadow

Let $`A\subset H=\operatorname{conv}A`$ be the genuine triangle-free source
minimizer, with $`|A|=N`$, $`\operatorname{diam}H=D`$, and
```math
M=\alpha_1(H)=N+\widehat p_H .
```
For a rotated and translated unit triangular lattice $`\Lambda'`$, put
```math
Y=\Lambda'\cap H,\qquad
a_0=\frac{\sqrt3}{2},\qquad r_\Lambda=\frac1{\sqrt3}.
```
Then the strict-conflict graph $`y\sim a\iff |y-a|<1`$ satisfies
```math
\boxed{\nu(Y,A)\ge |Y|-\widehat p_H,}\tag{154.1}
```
and
```math
\boxed{|Y|\ge
\frac{\operatorname{area}H-r_\Lambda\operatorname{per}H}{a_0}.}\tag{154.2}
```
Consequently, using Oler's finite packing inequality for $`M`$,
```math
\boxed{0\le M-|Y|\le \frac76\operatorname{per}H+1
\le\frac{7\pi}{6}D+1.}\tag{154.3}
```
Moreover, a maximum matching leaves at most $`\widehat p_H`$ lattice sites and at
most $`M-|Y|`$ source points unmatched.

### Proof

For every $`Q\subseteq Y`$, $`Q`$ is unit-separated and lies in $`H`$. The exact
fixed-source Hall inequality gives
```math
|Q|-|N_A(Q)|\le\widehat p_H.
```
The deficiency form of Hall's theorem is
```math
|Y|-\nu(Y,A)=\max_{Q\subseteq Y}(|Q|-|N_A(Q)|),
```
which proves (154.1).

Let $`H_{-r}=\{x\in H:\operatorname{dist}(x,\partial H)\ge r\}`$. Every
$`x\in H_{-r_\Lambda}`$ is within $`r_\Lambda`$ of a lattice point, and that
lattice point lies in $`H`$, hence in $`Y`$. Disjoint triangular-lattice Voronoi
cells of area $`a_0`$ therefore give
```math
\operatorname{area}(H_{-r_\Lambda})\le a_0|Y|.
```
For a convex body, inner parallel perimeters are nonincreasing, so coarea gives
```math
\operatorname{area}H-\operatorname{area}(H_{-r})
=\int_0^r\operatorname{per}(H_{-s})\,ds
\le r\operatorname{per}H.
```
Taking $`r=r_\Lambda`$ proves (154.2). Oler gives
```math
M\le\frac{\operatorname{area}H}{a_0}+\frac{\operatorname{per}H}{2}+1.
```
Subtracting (154.2), using $`r_\Lambda/a_0=2/3`$, and then
$`\operatorname{per}H\le\pi D`$ proves (154.3). A maximum matching leaves at most
$`|Y|-\nu(Y,A)\le\widehat p_H`$ lattice sites unmatched, and
```math
N-\nu(Y,A)\le N-|Y|+\widehat p_H=M-|Y|,
```
which proves the final assertion. $`\square`$

## 154.1 Co-phased bulk consequence

Assume the prescribed phase is generic: no source point lies on $`\Lambda'`$, and no
source-lattice distance is exactly one.
Let
```math
A_\partial=\{a\in A:\operatorname{dist}(a,\partial H)\le1\},\qquad
b=|A_\partial|.
```
Every source point in $`A\setminus A_\partial`$ has its complete infinite-lattice
strict neighborhood inside $`Y`$, hence exactly three or four lattice conflicts,
forming respectively an elementary triangle or a unit lozenge. If
```math
Z=\{y\in Y:N_A(y)\subseteq A_\partial\},
```
then
```math
\boxed{|Z|\le b+\widehat p_H.}\tag{154.4}
```
Indeed, apply the Hall inequality to $`Z`$, noting $`N_A(Z)\subseteq A_\partial`$.
The canonical boundary estimate gives $`b\le12D+9`$. This co-phased
monomer/dimer conclusion is structural only; it does not imply a Schur kernel.

## 155. Very-super-boundary hull alignment

Let $`X_m`$ be an independently chosen smaller optimum with
```math
|X_m|=m=N-\rho,\quad K_m=\operatorname{conv}X_m,\quad
d=\operatorname{diam}K_m,\quad t=\frac{D-d}{2},\quad L=K_m+t\mathbb B.
```
Assume $`D>16\sqrt3`$, as is harmless in the sufficiently large Target A regime,
and set $`\eta(D)=3^{1/4}\sqrt D`$. We use the classical Bonnesen inequality in
the form recorded by Daniel A. Klain, [*An Error Estimate for the Isoperimetric
Deficit*](https://faculty.uml.edu/dklain/Klain-Isoperimetric.pdf), Section 4,
equation (6): for every compact convex planar body of perimeter $`P`$, area $`A`$,
circumradius $`R`$, and inradius $`r`$,
```math
P^2-4\pi A\ge \pi^2(R-r)^2.
```
Both $`H`$ and $`L`$, after circumcenter
normalization, satisfy
```math
B\!\left(0,\frac D2-2\eta(D)\right)\subseteq K\subseteq
B\!\left(0,\frac D2+\eta(D)\right).\tag{155.1}
```
After aligning circumcenters,
```math
\boxed{d_H(H,L)\le3\eta(D),\qquad
L\ominus3\eta(D)\mathbb B\subseteq H.}\tag{155.2}
```
Thus, if $`t\ge1+3\eta(D)`$, one may place
```math
\boxed{K_m+\mathbb B\subseteq H.}\tag{155.3}
```
The canonical lower bound on $`t`$ implies this whenever
```math
\boxed{\rho\ge\frac{\pi D}{2}
+\frac{4D}{c}\left(1+3\,3^{1/4}\sqrt D\right),\qquad
c=\frac{2\sqrt3}{\pi}.}\tag{155.4}
```
In that regime the exact source Hall theorem applies in one common placement to
$`X_m`$ and to every inner scaffold lattice site
$`Y_{\rm in}=\Lambda'\cap\operatorname{int}(K_m+\mathbb B)`$:
```math
\boxed{\nu(X_m,A)\ge m-\widehat p_H,\qquad
\nu(Y_{\rm in},A)\ge|Y_{\rm in}|-\widehat p_H.}\tag{155.5}
```

### Proof

The canonical Oler-shell estimate gives, for the source hull,
```math
\operatorname{area}H>\frac{\pi D^2}{4}-\frac{\sqrt3\pi}{4}D,
\qquad \operatorname{per}H\le\pi D.
```
Hence $`P_H^2-4\pi\operatorname{area}H<\pi^2\sqrt3D`$. The classical Bonnesen
inequality $`P^2-4\pi A\ge\pi^2(R-r)^2`$ gives
$`R-r<3^{1/4}\sqrt D=\eta(D)`$, with $`R,r`$ the circumradius and inradius.
Since $`R\ge D/2`$, $`r\le D/2`$, and the incenter and circumcenter are within
$`R-r`$, the disk in (155.1) lies in $`H`$, while the outer disk contains $`H`$.

For $`L=K_m+t\mathbb B`$, the canonical parallel-body identities and strict Oler
defect give the same area lower bound and $`\operatorname{per}L\le\pi D`$, so
(155.1) holds for $`L`$ as well. Aligning circumcenters gives (155.2): every point
of either body is within $`3\eta(D)`$ of the common inner disk in the other body;
the support-function characterization of Hausdorff distance gives the erosion
inclusion. Since
```math
(K_m+t\mathbb B)\ominus h\mathbb B=K_m+(t-h)\mathbb B\qquad(0\le h\le t),
```
(155.3) follows when $`t\ge1+3\eta(D)`$. Combine this with the canonical strict
bound
```math
t>\frac{c}{4D}\left(\rho-\frac{\pi D}{2}\right)
```
to obtain (155.4). Applying the exact source Hall inequality to the two
unit-separated subsets of $`H`$ proves (155.5). $`\square`$

## Exact consequence for Target A

Sections 154–155 remove the source/scaffold coordinate-independence obstruction in
the explicit subbranch (155.4). They do **not** prove
```math
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}.
```
The two matchings in (155.5) need not use the same source vertices, need not leave
the strict rattlers unmatched, and do not by themselves produce a response-kernel
vector or a strict smaller-diameter competitor. The exact remaining lemma is:

> **Two-shadow compatibility lemma.** Under (155.4), exchange the source matchings
> for the smaller optimum and inner scaffold so their common source structure yields
> the Target A Schur bound or an $`N`$-point unit-separated configuration of diameter
> $`<D`$.

The result is compatible with the activation/monomer regressions because it uses
global source and smaller-optimum inequalities, not local activation rank or KKT
stress. The only external input is the classical Bonnesen inequality for compact
convex planar bodies; no infinite-plane Kuperberg conclusion is used.
