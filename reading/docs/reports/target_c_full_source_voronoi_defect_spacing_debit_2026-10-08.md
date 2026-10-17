> Generated reading edition · [exact source](../../../docs/reports/target_c_full_source_voronoi_defect_spacing_debit_2026-10-08.md) · source SHA-256 `50fe68821570c358a240cd75ba8c149dca59f6c45f4a3ad3556cd993f7c9c51e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "e1ec0eda3590643daf2a4fef4d8542ee7174abb5", "source_branch_refs": ["refs/heads/research/level-i-closure-20261007"], "source_commit": "871c56111c479d536b17a51d21fcd04fa86d8931", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_c_full_source_voronoi_defect_spacing_debit_2026-10-08.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "790afc3b6f832f27dd29d64cc6f1769d38235ba4f446a79f8d65a6388603c2f0"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Target C: full-source Voronoi defect and subset spacing debit

Date: 2026-10-08. Research base: `88c030143feaa7cead83d4d49a05cf8faa2a0e62`.
Run start: `d463ece47a8441a94074d0de19ef3bf75ee8894c`.
State: `2026-10-08.audit.156`, including the recorded Audit.160 entry.
Classification: **proved candidates awaiting independent audit**.
Registry status: unreviewed; canonical=false. C-II and Level I remain open.

The exact implication being attacked is

`a near-unit-free spectator population -> full-source spacing debit
-> g_A<=0 -> contradiction to canonical global optimality`.

A second implication is

`contact-minimal full source -> hull covering and full Voronoi surplus
-> only O(D/delta) delta-near-isolated labels`.

This is a source population restriction, not an extraction of a shallow
blocker closure. It uses all labels in both C-II population branches.

## 1. Inputs and definitions

Let `A` be a canonical triangle-free global minimizer chosen
contact-minimal and then actual-diameter-pair-minimal. Write

```math
n=|A|,\quad D=\operatorname{diam}A,\quad K=\operatorname{conv}A,\quad
P=\operatorname{per}K,\quad
a_0=\sqrt3/2,\quad \Delta=\pi/(2\sqrt3),
```
```math
g_A=n-1-\Delta D^2>0,\qquad
\delta_K=\pi D^2/4-\operatorname{area}K\ge0.
```

The strict population inequality is canonical
[FS.1 and GE.1](../targets/target-c/58-full-source-geometry-audit.md).
The finite scaled packing estimate is canonical
[Oler, Theory 03, Lemma 21.1](../theory/03-oler-shell.md).
The lower/upper endpoint uses the exact
[contact-loss normalization](../audits/target_c_one_spare_site_scope_refinement_independent_audit_2026-10-08.md);
its replacement remains triangle-free.

For `delta>0`, a **delta-near-isolated** label has
`|x-y|>1+delta` for every other original label.
Such a label is a contact isolate, but the converse need not hold.
No contact isolate is deleted or assigned a nonzero stress.

## 2. The unit disks cover the source hull

**Candidate lemma.**
Every `z in K` satisfies `min_x |z-x|<=1`.

If every original point were strictly farther than one from `z`,
remove a nonisolated contact vertex `v` and insert `z`.
All `n` labels remain represented, every new lower pair is strict,
and every new upper pair is at most `D` because `z in K`.
The new contact graph is the old induced graph plus an isolated
vertex, so it remains triangle-free and loses a contact.
Globality or contact minimality is contradicted.
Global minimality supplies a unit pair: if the minimum distance
were larger than one, a common scaling would strictly reduce D.
Secondary diameter-pair minimality is unnecessary.

In particular, every hull-clipped Voronoi cell of `x` lies in
the closed unit ball about `x`.

## 3. Checked literature input and a local extension

The original source checked is A. Mazel, I. Stuhl and Y. Suhov,
[Minimal Area of a Voronoi Cell in a Packing of Unit Circles,
arXiv:2211.03255v1](https://arxiv.org/pdf/2211.03255v1),
pages 1--4. Their occupied centers have separation at least two,
and their disks have radius one. A full Voronoi cell has area
at least `2sqrt(3)`, with equality only for the regular hexagon
whose six neighbor centers form a regular unit-contact ring.
Scaling coordinates by one half gives area at least `a_0`
for separation-one centers.

This concerns a **full cell**, not an arbitrary cell clipped by
a container. The proof below keeps every clipped boundary cell
in a separate exact area term.

### A polygon angular-density bound

The following extension of the source's polygon argument is a
new candidate. If a convex polygon contains the radius-`r` disk
about the origin and all its vertices have radius at least
`r_0>=r`, then its area is at least

```math
H(r,r_0)=
\frac{\pi r\sqrt{r_0^2-r^2}}{\arccos(r/r_0)}.
\tag{1}
```

The endpoint `r=r_0` is interpreted as the disk-area limit.

Here is a direct proof using the disjoint triangles from the
origin to successive polygon sides. Let one triangle have vertex
radii `a,b`, angle `phi in (0,pi)`, and side-line distance `h`
from the origin. The contained disk gives `h>=r`. The identity

```math
h^2=\frac{a^2b^2\sin^2\phi}{a^2+b^2-2ab\cos\phi}
\le ab\cos^2(\phi/2)
```

implies `ab>=r^2 sec^2(phi/2)`, while the vertex hypothesis gives
`ab>=r_0^2`. Thus this triangle has area at least

```math
\max\{\tfrac12r_0^2\sin\phi,\ r^2\tan(\phi/2)\}.
```

Put `theta_0=arccos(r/r_0)`. For `phi<=2theta_0`, the first
bound divided by `phi` is at least
`r sqrt(r_0^2-r^2)/(2theta_0)`, since `sin(phi)/phi` decreases
on `(0,pi)`. For `phi>=2theta_0`, the second gives the same
bound because `tan(phi/2)/phi` increases. Sum the triangle
angles, which total `2pi`, to obtain (1). The case `r=r_0`
follows by the disk-area bound or the continuous limit.

### Linear surplus for a near-isolated full cell

For any full bounded source Voronoi cell, every vertex has
radius at least `r_0=1/sqrt(3)`: it is an empty circumcenter
of at least three separation-one sites, and the sine law at
a smallest triangle angle gives this radius bound.

A delta-near-isolated center has a Voronoi cell containing the
radius `r=(1+delta)/2` disk. Then

```math
\boxed{|V_x|\ge a_0+\delta.}
\tag{2}
```

For `1/2<=r<=r_0`, apply (1). Put
`r=r_0 cos(theta)`, `0<=theta<=pi/6`. The right side is
`pi r_0^2 sin(2theta)/(2theta)`. Its derivative with respect
to `r` is

```math
\frac{\pi r_0}{2}
\frac{\sin(2\theta)-2\theta\cos(2\theta)}
     {\theta^2\sin\theta}\ge2.
\tag{3}
```

Indeed the numerator is `integral_0^(2theta) t sin(t) dt`.
Concavity of sine on `[0,pi/3]` gives
`sin(t)>=(3sqrt(3)/(2pi))t`, while `sin(theta)<=theta`.
Integration proves (3). At `r=1/2`, (1) is `a_0`;
integration therefore gives `a_0+2(r-1/2)=a_0+delta`.

For `r>=r_0`, use the contained disk. Its area agrees with
the continuous limit in (1) at `r_0`, and its derivative
with respect to `delta` is `pi r>=pi/sqrt(3)>1`.
The same lower bound continues for every larger `delta`.

## 4. An exact full-source Voronoi ledger

Let `J` be the labels whose clipped Voronoi cells touch
`partial K`, and put `m=|J|`.
Every label outside `J` has its full bounded cell inside `int K`.
Write

```math
\sigma_x=|V_x|-a_0\ge0\quad(x\notin J),\qquad
A_\partial=\sum_{x\in J}|V_x\cap K|.
```

The cells partition `K` up to zero-area boundaries, so

```math
\boxed{
\sum_{x\notin J}\sigma_x+A_\partial+\delta_K
=a_0(m-1)-a_0g_A.
}
\tag{4}
```

This counts all original labels. A triangle-free source has
`sigma_x>0` on every full cell: equality in the checked local
Voronoi theorem supplies six unit neighbors and unit triangles.
Strictness alone supplies no uniform surplus per cell.

### Boundary label count

Hull covering shows that each `x in J` is within one of
`partial K`. Its radius-`1/2` disk is contained in

`(K+B(0,1/2)) \ int(K eroded by B(0,3/2))`.

Those disks have disjoint interiors. The outer parallel-area
formula and the inner-boundary-layer estimate give belt area
at most `2P+pi/4`. The latter estimate follows by integrating
the decreasing perimeters of convex inner parallel sets.
Thus

```math
m\le(8/\pi)P+1\le8D+1.
\tag{5}
```

### Near-isolation count

Let `z_int` count delta-near-isolated labels outside `J`.
Equations (2)--(4) imply

```math
\delta z_{\rm int}+A_\partial+\delta_K
\le a_0(m-1)-a_0g_A<a_0(m-1).
```

There are at most `m` remaining near-isolated boundary labels.
Consequently

```math
\boxed{
|Z_\delta|<
\left(\frac{4\sqrt3}{\delta}+8\right)D+1.
}
\tag{6}
```

For any `delta(D)->0` with `D delta(D)->infinity`,
`|Z_delta|=o(D^2)`. This controls an empty near-unit neighborhood,
not the total contact-isolated population. A dense contact-isolated
chamber may have many near-unit neighbors and obey (6).

## 5. A spacing debit that uses the canonical population excess

Partition any unit-separated diameter-`D` source into `X` and
`Y`. Suppose the mutual distances in `Y` are at least
`lambda=1+c/D`, with `c>0`.
Scale `Y` and the full source hull by `1/lambda` and apply Oler:

```math
|Y|-1\le\Delta D^2/\lambda^2+\pi D/(2\lambda).
```

Therefore the full-source quantity satisfies

```math
\boxed{
g_A\le |X|-\Delta D^2(1-\lambda^{-2})
+\frac{\pi D}{2\lambda}.
}
\tag{7}
```

If `|X|<=bD+o(D)` for fixed `b,c`, then

```math
g_A\le(b+\pi/2-2c\Delta)D+o(D).
\tag{8}
```

A canonical source must therefore satisfy
`b>=2c Delta-pi/2` whenever such a partition is supplied.
This is only a necessary condition; passing it does not certify
global optimality.

### Exact exclusion of the previous augmentation mechanism

The [forced-congestion family](target_c_sharp_cap_closure_and_unbounded_path_congestion_2026-10-08.md)
has `D>=576` and fewer than `D/5` old labels. Its proposed
leading-density augmentation uses a triangular lattice of
spacing `1+2/D`. Even if that augmentation could use the
entire diameter-`D` hull, (7) gives

```math
g_A<-\frac95D.
\tag{9}
```

To check the constant, use
`D^2(D+1)/(D+2)^2>=D-3` and
`Delta>471/520`, `pi/2<11/7`.
For `D>=576`,

```math
4\Delta-\pi/2-1/5-\frac{12\Delta}{D}-9/5
\ge(191/48)(471/520)-11/7-2
=\frac{5727}{174720}>0.
```

The numerical bounds follow from
`pi>157/50`, `pi<22/7` and `sqrt(3)<26/15`;
the checker certifies the pi bounds by rational alternating
arctangent sums. The family has
`8q+7+ceil(D/7)<D/5` because `D>=576q^2` and
`8q+8<=16q^2<2D/35`.

Thus the earlier augmentation is a leading-density regression
with a definite linear population deficit, not an example
satisfying the canonical `g_A>0` condition. The original report
already classifies it as nonglobal. This calculation strengthens
that scope boundary; it does not reject congestion in a different
globally optimal source.

## 6. Verification and remaining obligation

The [exact checker](../../../research/verify_target_c_voronoi_spacing_debit_2026_10_08.py)
reconstructs all hull-clipped Voronoi cells for six finite
unit-separated grids in Q(sqrt(3)). It checks every original
pair, every same-cardinality square-competitor pair, hull
covering by cell vertices, boundary labels, full-cell areas
and vertex radii, the exact cell-area partition and surplus
identity, and the local linear near-isolation surplus.
The grids are explicitly nonglobal.

A separate seven-site regular hexagon with center checks the
equality cell and its six unit triangles; global optimality is
not certified. Rational arithmetic certifies the population
debit constants and the all-q base-count bounds. Universal
claims are proved analytically, not by these finite samples.

The final checker run passed: 9,432 complete grid-source pairs
and 9,432 complete square-competitor pairs; 310 clipped cells,
including 166 full cells and 144 boundary cells; 1,704 covering
vertex checks; and 155 near-isolated labels. The equality fixture
adds 21 pairs, six cell vertices and six unit triangles. Rational
pi bounds and 1,000 all-q arithmetic samples passed. Python
compilation and all five local proof links passed. None of these
finite checks certifies global optimality or the universal
polygon inequality by enumeration.

Equations (4), (6) and (7) constrain the **whole source**.
They do not extract a shallow arrow-closed set, control a
high-degree near-unit merger, provide a compatible wall move,
or restore deleted labels. High near-unit degree can make a
closure grow deeper. No C-II or Level I closure is claimed.
