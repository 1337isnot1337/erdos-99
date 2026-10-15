# Target C — global isolate concentration or asymptotic full-core disk audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 77 gives two exact full-source packing decompositions:

1. source points inside the force hull but outside the positive core are assigned to
   convex inactive chambers; and
2. source points outside the force hull are assigned to convex exterior caps between
   the force hull and the full source hull.

Canonical Section 79 already shows that a quadratic inactive population **inside**
the force hull must concentrate into one macroscopic chamber. The same argument works
for the exterior caps, with an even smaller total-perimeter constant.

Combining both sides gives a global reduction:

> along every unbounded post-ZF C-II survivor sequence, either one actual convex
> container (an inactive chamber or an exterior cap) contains `Omega(D^2)`
> contact-isolated source points and has area `Omega(D^2)`, or the number of source
> points outside the nonisolated positive-contact core is `o(D^2)`. In the latter
> case the force hull has asymptotically maximal diameter-one area, the strict
> rhombi fill it in area, and the core/rhombus populations both approach the full
> triangular-lattice density `pi/(2sqrt(3)) D^2`.

This removes the remaining population-scale ambiguity. A hypothetical survivor can no
longer have a positive-density invisible population spread diffusely over both the
interior and exterior of the force hull while every individual inactive container
stays submacroscopic.

No source point is deleted. No zero-weight contact is promoted. The theorem does not
claim that an `o(D^2)` isolate set is empty.

---

# 80. Global inactive-container concentration

Let

\[
a_0={\sqrt3\over2},
\qquad
K=\operatorname{conv}A,
\qquad
F=\operatorname{conv}V(G),
\tag{80.1}
\]

where `G` is the connected nonisolated positive-contact core of the canonical post-ZF
representative. Write

\[
m:=|V(G)|,
\qquad
A_K:=\operatorname{area}K,
\qquad
A_F:=\operatorname{area}F.
\tag{80.2}
\]

Canonical Section 77 defines

- `Z_ch` = contact-isolated source points in the inactive chambers inside `F`;
- `Z_ext` = source points outside `F`, assigned to convex exterior caps; and
- `N_F=m+Z_ch` = full source population in `F`.

Thus the full source partitions exactly as

\[
\boxed{n=m+Z_{ch}+Z_{ext}.}
\tag{80.3}
\]

Canonical Section 77 proves

\[
\boxed{
a_0N_F=A_F+O(D),
\qquad
a_0Z_{ext}={\pi D^2\over4}-A_F+O(D).
}
\tag{80.4}
\]

It also proves for the internal inactive chambers

\[
\boxed{
a_0Z_{ch}=A_{ch}+O(D),
\qquad
P_{ch}\le13\pi D.
}
\tag{80.5}
\]

Here `A_ch` is their total area and `P_ch` their total perimeter.

## 80.1 Exterior cap area and population also agree to boundary order

Let the nondegenerate exterior caps of Section 77 be

\[
K_1,\ldots,K_r.
\]

Write

\[
A_i:=\operatorname{area}K_i,
\qquad
P_i:=\operatorname{per}K_i,
\qquad
z_i:=|A\cap(K_i\setminus F)|.
\tag{80.6}
\]

Their interiors are disjoint and they partition `K\setminus F` up to closing chords,
so

\[
A_{ext}:=\sum_iA_i=A_K-A_F.
\tag{80.7}
\]

Canonical Section 68 gives

\[
0\le \delta_K:={\pi D^2\over4}-A_K=O(D),
\tag{80.8}
\]

because `delta_K+E_4<c_0P_K` and `P_K<=pi D`. Therefore

\[
A_{ext}={\pi D^2\over4}-A_F+O(D).
\tag{80.9}
\]

Comparing with (80.4),

\[
\boxed{
a_0Z_{ext}=A_{ext}+O(D).}
\tag{80.10}
\]

The exact cap-perimeter incidence identity from Section 77 is

\[
\sum_iP_i=P_K+P_F-2P_{com}.
\tag{80.11}
\]

Hence

\[
\boxed{
P_{ext}:=\sum_iP_i\le P_K+P_F\le2\pi D.
}
\tag{80.12}
\]

Also `r<=q<=pi D`.

For each cap Section 77's Oler argument gives the nonnegative slack

\[
\sigma_i^{ext}
:={A_i\over a_0}+{P_i\over2}-1-z_i\ge0.
\tag{80.13}
\]

Summing and using (80.10)--(80.12),

\[
\sum_i\sigma_i^{ext}
={A_{ext}\over a_0}+{P_{ext}\over2}-r-Z_{ext}
=O(D).
\tag{80.14}
\]

Thus the exterior-cap Oler slack is boundary order just as the internal-chamber slack
is.

## 80.2 Quadratic external population forces one macroscopic exterior cap

Put

\[
A_{ext,max}:=\max_iA_i.
\]

Isoperimetry gives

\[
\sum_i\sqrt{A_i}
\le {P_{ext}\over2\sqrt\pi}
\le\sqrt\pi D.
\tag{80.15}
\]

Therefore

\[
A_{ext}
=\sum_iA_i
\le\sqrt{A_{ext,max}}\sum_i\sqrt{A_i}
\le\sqrt{A_{ext,max}}\sqrt\pi D,
\]

so

\[
\boxed{
A_{ext,max}\ge {A_{ext}^2\over\pi D^2}.
}
\tag{80.16}
\]

Suppose along a subsequence

\[
Z_{ext}\ge\zeta D^2
\tag{80.17}
\]

for some fixed `zeta>0`. Equation (80.10) gives

\[
A_{ext}\ge a_0\zeta D^2-O(D).
\]

Hence (80.16) yields

\[
\boxed{
\liminf {A_{ext,max}\over D^2}
\ge {a_0^2\zeta^2\over\pi}>0.
}
\tag{80.18}
\]

Choose a cap `K_*` attaining `A_ext,max`. Its individual slack is `O(D)` by
(80.14), and its perimeter is `O(D)` by (80.12). Therefore

\[
z_*
={A_{ext,max}\over a_0}+{P_*\over2}-1-\sigma_*^{ext}
={A_{ext,max}\over a_0}+O(D),
\tag{80.19}
\]

so

\[
\boxed{z_*=\Omega(D^2).}
\tag{80.20}
\]

Thus a quadratic external source population cannot be diffuse: it forces one actual
macroscopic convex exterior cap containing a quadratic number of source points.
Those points lie outside the positive contact core and are contact-isolated in the
canonical representative.

## 80.3 No macroscopic exterior cap implies `Z_ext=o(D^2)`

Conversely, if

\[
A_{ext,max}=o(D^2),
\tag{80.21}
\]

then (80.15) gives

\[
A_{ext}
\le\sqrt{A_{ext,max}}\sqrt\pi D
=o(D^2).
\tag{80.22}
\]

Equation (80.10) gives

\[
\boxed{Z_{ext}=o(D^2).}
\tag{80.23}
\]

Equivalently, absence of one macroscopic exterior cap forces the full source hull and
force hull to agree in area to leading order:

\[
A_K-A_F=o(D^2).
\tag{80.24}
\]

## 80.4 Combine with the internal chamber dichotomy

Canonical Section 79 proves the corresponding internal statement:

- if `Z_ch=Omega(D^2)` on a subsequence, one actual inactive chamber has quadratic
  area and quadratic isolated population; and
- if every internal inactive chamber has area `o(D^2)`, then

\[
Z_{ch}=o(D^2),
\qquad
A_{ch}=o(D^2),
\qquad
A_4=A_F-o(D^2).
\tag{80.25}
\]

Therefore, if **neither** an internal inactive chamber nor an exterior cap is
macroscopic, (80.23) and (80.25) give

\[
\boxed{
n-m=Z_{ch}+Z_{ext}=o(D^2).}
\tag{80.26}
\]

The entire source is asymptotically force-visible in population, although an
`o(D^2)` isolate set may remain.

## 80.5 The no-container branch is asymptotically full-core and near-disk

Canonical Section 77 gives the full-source density identity

\[
\boxed{
a_0n={\pi D^2\over4}+O(D).}
\tag{80.27}
\]

Hence

\[
{n\over D^2}\longrightarrow
\Delta_2:={\pi\over4a_0}={\pi\over2\sqrt3}.
\tag{80.28}
\]

Using (80.26),

\[
\boxed{
{m\over D^2}\longrightarrow\Delta_2.
}
\tag{80.29}
\]

Equation (80.4) and `Z_ext=o(D^2)` give

\[
\boxed{
{A_F\over D^2}\longrightarrow{\pi\over4}.
}
\tag{80.30}
\]

Canonical Section 79 gives `A_4=A_F-o(D^2)`, so

\[
\boxed{
{A_4\over D^2}\longrightarrow{\pi\over4}.
}
\tag{80.31}
\]

Canonical Section 68 writes

\[
A_4=a_0R_4+E_4,
\qquad E_4=O(D),
\tag{80.32}
\]

therefore

\[
\boxed{
{R_4\over D^2}\longrightarrow\Delta_2.
}
\tag{80.33}
\]

This is the genuine asymptotic full-core density, not merely `m=Omega(D^2)`.

Moreover `F` has Euclidean diameter exactly `D`: at least one positive actual diameter
edge has both endpoints in the loaded vertex set `B subset F`. Thus the normalized
convex bodies `D^{-1}F` have diameter one and area tending to the isodiametric maximum
`pi/4`.

By Blaschke selection and uniqueness of equality in the planar isodiametric inequality,
every Hausdorff-convergent subsequence of suitable translates tends to the radius-1/2
Euclidean disk. Consequently

\[
\boxed{
{1\over D}\inf_o d_H\!\left(F,B(o,D/2)\right)\longrightarrow0.
}
\tag{80.34}
\]

So the no-macroscopic-container branch is an **asymptotic full-core near-disk
rhombic branch**:

\[
\boxed{
 n-m=o(D^2),
\quad
 A_F={\pi D^2\over4}-o(D^2),
\quad
 A_4={\pi D^2\over4}-o(D^2),
\quad
 m,R_4=(\Delta_2+o(1))D^2.
}
\tag{80.35}
\]

## 80.6 Coherent grains cover the near-disk force hull

Fix `epsilon in (0,pi/6)`. Canonical Section 69 deletes only `O_epsilon(D)` rhombi to
form `epsilon`-coherent physical grains, so in the no-container branch their union has
area

\[
{\pi D^2\over4}-o(D^2).
\tag{80.36}
\]

The total grain perimeter is `O_epsilon(D)`. As in Section 79, for every fixed
`eta>0`, grains with fewer than `eta D^2` rhombi carry only

\[
O_\epsilon(\sqrt\eta\,D^2)
\tag{80.37}
\]

rhombi in total. Thus, after fixing `epsilon` and then taking `eta` small, finitely
many macroscopic `epsilon`-coherent grains cover all but an arbitrarily small area
fraction of a body converging to the disk.

Canonical Section 78 further localizes one such quadratic coherent subgrain inside one
macroscopic harmonic attachment cell and localizes the complete-grid diameter bound to
that cell.

## 80.7 Final global alternatives after Sections 77--80

Every unbounded post-ZF C-II survivor sequence has a subsequence in one of the
following two **types**.

### Type I — one macroscopic inactive convex container

At least one of the following exists:

1. an internal inactive chamber `C_* subset F`; or
2. an exterior cap `K_* subset K\setminus int(F)`.

In either case the container has

\[
\boxed{
area=\Omega(D^2),
\qquad
z=\Omega(D^2),
\qquad
perimeter=O(D),
\qquad
Oler\ slack=O(D),
}
\tag{80.38}
\]

and its `z` points are actual contact-isolated source points in the canonical
representative.

### Type II — asymptotic full-core near-disk rhombic saturation

Equation (80.35) holds. For each fixed phase width, finitely many macroscopic coherent
rhombic grains cover asymptotically all of the force hull area, and the force hull
itself converges after scaling to the diameter-one disk.

There is no third population-scale regime.

## 80.8 What remains open

This is a structural reduction, not a Level-I closure.

- **Type I:** density alone cannot exclude a contact-isolated near-triangular packing.
  A closing theorem must couple the macroscopic container to global diameter
  minimality, its core boundary, or a source-preserving strict competitor.
- **Type II:** the positive core is asymptotically full and the rhombi occupy a
  near-disk body, but the fixed-width coherent grains can form a finite-perimeter
  polycrystal. A closing theorem must extract the missing boundary-order shell
  surplus from the grain interfaces/phase defects, or aggregate the local Section-76
  diameter inequalities strongly enough to beat the strict lattice comparison.

Old reports that assume **exactly** `m=n` or exactly no contact isolates are not made
canonical by (80.26); only asymptotic full visibility is proved.

## 80.9 Dependency audit

- **Canonical Section 77 / `C-INACTIVE-CHAMBER`:** full-source population identities,
  exterior cap decomposition, cap Oler inequalities, internal chamber identities.
- **Canonical Section 79 / `C-INACTIVE-DICHOTOMY`:** internal concentration/rhombic-
  saturation dichotomy.
- **Canonical Section 68 / `C-PUNCTURED-PHASE`:** `delta_K=O(D)`, `E_4=O(D)`, and
  phase-cut deletion.
- **Canonical Section 69 / `C-COHERENT-GRAINS`:** coherent physical grains and total
  perimeter/square-root budget.
- **Canonical Section 78 / `C-HARMONIC-GRID-LOCAL`:** used only in the Type-II handoff.
- **Isodiametric compactness:** standard planar convex geometry; used only for the
  near-disk conclusion (80.34).
- **Contact isolates:** retained and explicitly counted throughout Type I.

**Status:** canonical as `C-FULLCORE-NEAR-DISK`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
