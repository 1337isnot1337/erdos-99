# Target C — audited §164 all-regime atomic Mantel gap by finite diagonal

**Date:** 2026-09-12
**Lifecycle:** audited-working proof-only route module; theorem-state authority unchanged.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module normalizes the finite-diagonal theorem recorded in
`research/target_c_atomic_mantel_gap_finite_diagonal_2026-09-12.md` and its hostile
audit. It depends on audited §142 and the robust near-complete-grid theorem §163.

A previously attempted compactness shortcut is **rejected**: total atomic mass is not
upper-semicontinuous under weak convergence, so endpoint nonattainment alone does not
produce a uniform gap. The valid proof freezes shrinking atom neighborhoods inside each
fixed near-extremal limit, selects one finite source realizing those statistics, and
then diagonalizes the finite source graphs themselves.

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
s_2:=\sqrt{\Delta_2}.
\]

---

## 164.1 Uniform atomic gap

There exists an absolute constant

\[
\boxed{\eta_{\rm grid}>0}
\tag{164.1}
\]

such that every audited-working Type-II train-measure subsequential limit in the §142
scope satisfies

\[
\boxed{x\sigma\ge 2s_2+\eta_{\rm grid},}
\tag{164.2}
\]

where

\[
x=\lim {T\over D}
\]

and `sigma` is the total atomic mass of the limiting projective train-direction
probability measure.

No numerical value of `eta_grid` is asserted.

### Proof by contradiction

Audited §142 already proves

\[
x\sigma\ge2s_2.
\tag{164.3}
\]

Assume there is no positive uniform gap. For every integer `j>=1`, choose a fixed
Type-II subsequential limit `(x_j,mu_j)` with total atomic mass `sigma_j` such that

\[
2s_2
\le A_j:=x_j\sigma_j
\le2s_2+{1\over j}.
\tag{164.4}
\]

Everything below is first done inside this fixed `j`-th limit. No weak limit of the
measures `mu_j` is taken.

---

## 164.2 Near equality concentrates the atomic crossing mass in one orbit

Write the atomic masses of `mu_j` in absolute `D` normalization and group them by the
projective relation

\[
\phi\sim\phi+{\pi\over3}\pmod\pi.
\]

Let `M_{j,r}` be the total atomic mass in orbit `r` and `E_{j,r}` the normalized
strict-rhombus crossing mass carried by that orbit.

Audited §142 gives the two key measure facts:

1. every normalized quadratic strict-rhombus crossing-measure limit is supported on the
   exact `+-pi/3` relation; and
2. the crossing measure is dominated by the product train-phase measure.

The product measure charges the exact relation only through atoms. Since the physical
train-crossing graph is simple and triangle-free, weighted Mantel gives

\[
E_{j,r}\le {M_{j,r}^2\over4}.
\tag{164.5}
\]

Type II has total normalized strict-rhombus crossing mass

\[
\sum_rE_{j,r}=\Delta_2=s_2^2,
\tag{164.6}
\]

while

\[
\sum_rM_{j,r}=A_j.
\tag{164.7}
\]

Therefore

\[
s_2^2
\le {1\over4}\sum_rM_{j,r}^2
\le {A_j^2\over4}
=s_2^2+O(1/j).
\tag{164.8}
\]

Hence

\[
A_j^2-\sum_rM_{j,r}^2=o_j(1).
\tag{164.9}
\]

This forces one dominant orbit even if infinitely many orbits have positive mass. If

\[
m_j:=\max_rM_{j,r},
\]

then

\[
\sum_rM_{j,r}^2\le m_jA_j,
\]

so

\[
m_j\ge {\sum_rM_{j,r}^2\over A_j}=A_j-o_j(1).
\]

Thus one orbit `r(j)` satisfies

\[
\boxed{M_j=2s_2-o_j(1),}
\tag{164.10}
\]

and all other orbit masses sum to `o_j(1)`. Their crossing capacity is also `o_j(1)`,
so the dominant orbit carries

\[
\boxed{E_j=s_2^2-o_j(1).}
\tag{164.11}
\]

No compactness step in `j` has occurred.

---

## 164.3 Freeze atom windows, then choose the finite source

The dominant orbit has at most three projective atom locations

\[
\phi_{j,0},
\qquad
\phi_{j,0}+{\pi\over3},
\qquad
\phi_{j,0}+{2\pi\over3}
\pmod\pi.
\]

Choose three disjoint projective arcs `U_{j,0},U_{j,1},U_{j,2}` with radii at most
`1/j`, with `mu_j`-null boundaries, and with total non-atomic mass captured beyond the
three atoms at most `1/j`. Shrink them further, if necessary, so their union carries
crossing mass at least `E_j-1/j`.

The product-boundary is crossing-measure null because the crossing measure is dominated
by `mu_j x mu_j`. Therefore, along one actual source sequence realizing the fixed
limit `(x_j,mu_j)`, empirical train counts and crossing counts in these fixed windows
converge.

Choose one sufficiently far source from that sequence, with diameter `D_j`, so that
`D_j->infinity` and simultaneously

\[
{N_j\over D_j}=2s_2-o_j(1),
\tag{164.12}
\]

\[
{R_j^{\rm orb}\over D_j^2}=s_2^2-o_j(1),
\tag{164.13}
\]

where `N_j` is the number of complete trains in the three windows and
`R_j^{orb}` is the number of actual strict-rhombus crossings among them.

The induced finite crossing graph `G_j` is simple and triangle-free, and

\[
\boxed{
e(G_j)={N_j^2\over4}-o(D_j^2).}
\tag{164.14}
\]

This is the decisive repair: the diagonal object is a sequence of finite source graphs,
not a weak limit of the measures `mu_j`.

---

## 164.4 Finite near-Mantel stability creates a forbidden robust grid

Apply the finite near-Mantel stability lemma from §153 to `G_j`. It gives a partition

\[
V(G_j)=X_j\sqcup Y_j
\]

with

\[
|X_j|=s_2D_j+o(D_j),
\qquad
|Y_j|=s_2D_j+o(D_j),
\tag{164.15}
\]

and only `o(D_j^2)` missing cross-shore pairs.

For large `j`, each selected atom window has projective diameter below `pi/3`. Two
trains from the same window therefore cannot cross in a strict triangle-free unit
rhombus. If one linearly populated window had linear populations on both Mantel shores,
all corresponding same-window cross-shore pairs would be absent, contradicting the
`o(D_j^2)` missing-pair count. Hence every linearly populated window lies, up to
`o(D_j)` trains, on one shore.

There are at most three windows and both shores have asymptotic size `s_2D_j`.
Therefore one shore consists, up to `o(D_j)`, of a single window family of size

\[
\boxed{s_2D_j+o(D_j),}
\tag{164.16}
\]

and the other shore contains a window family of size at least

\[
\boxed{{s_2\over2}D_j+o(D_j).}
\tag{164.17}
\]

The two selected windows are distinct members of the same `pi/3` orbit, their angular
widths tend to zero, and they have only `o(D_j^2)` missing physical crossings. Thus
§163 applies with

\[
a=s_2,
\qquad
b\ge {s_2\over2}.
\]

It would force

\[
{3\over2}s_2\le {2\over\sqrt3},
\]

but

\[
{3\over2}s_2=1.428469210295936\ldots
>
{2\over\sqrt3}=1.1547005383792517\ldots .
\]

Contradiction. This proves the existence of the absolute `eta_grid>0` in (164.1).

---

## 164.5 Propagation through the train and defect ledgers

Audited §142 gives

\[
{q\over T}=y\le2(1-\sigma).
\]

Therefore every Type-II subsequential limit satisfies

\[
\lim {T-q/2\over D}
=x\left(1-{y\over2}\right)
\ge x\sigma
\ge2s_2+\eta_{\rm grid}.
\]

Hence

\[
\boxed{
\liminf {T-q/2\over D}
\ge2s_2+\eta_{\rm grid}.
}
\tag{164.18}
\]

Using the exact ledger

\[
T-q=2f-k
\]

and `q/D<=pi+o(1)`,

\[
\boxed{
\liminf {2f-k\over D}
\ge2s_2-{\pi\over2}+\eta_{\rm grid}.
}
\tag{164.19}
\]

Repeat the audited §146 elimination. Along a normalized subsequence write

\[
{h\over D}\to y_h,
\qquad
{d_H\over D}\to d,
\qquad
{s_Z\over D}\to s.
\]

From (164.18),

\[
{f\over D}
\ge
s_2+{\eta_{\rm grid}\over2}
-{y_h\over4}+{d\over4}+{s\over2}-o(1).
\tag{164.20}
\]

The exact outer ledger and Type-II force-hull perimeter limit give

\[
\limsup {Q\over D}+2s\le2y_h-\pi.
\tag{164.21}
\]

Since `Q>=f`,

\[
{9y_h\over4}
\ge
\pi+s_2+{\eta_{\rm grid}\over2}
+{d\over4}+{5s\over2}.
\]

Thus

\[
\boxed{
\liminf {1\over D}
\left(
 h-{d_H\over9}-{10s_Z\over9}
\right)
\ge
{4\over9}(\pi+s_2)+{2\over9}\eta_{\rm grid}.
}
\tag{164.22}
\]

This strictly improves the audited §146 weighted floor in every Type-II regime.

---

## Binding regression and scope

- The rejected argument “endpoint nonattainment + weak compactness implies a uniform
  atomic gap” remains false. Atomic mass is not upper-semicontinuous.
- The valid proof freezes continuity windows inside each fixed near-extremal limit before
  selecting a finite source; there is no second weak limit of atomic mass.
- §142 supplies the exact-relation support, product domination, and total crossing mass;
  no diffuse crossing mass is discarded.
- The near-Mantel step is finite and the three-window pigeonhole uses only
  `o(D_j^2)` missing cross pairs.
- The robust contradiction has a macroscopic margin about `0.27377`, so all diagonal
  `o(D_j)` and `o(D_j^2)` errors are harmless.
- `eta_grid` is existential only; no explicit value is certified.
- No outer-detour hypothesis is used.
- Contact-isolated source points remain outside the train/rigidity kernel and are not
  deleted.
- This strengthens the all-regime Type-II frontier but does not close Type II or the
  Type-I inactive-container branch by itself.

**Disposition:** §164 PASS at audited-working proof-only scope. C-II and Level I remain
open.
