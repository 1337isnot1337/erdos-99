> Generated reading edition · [exact source](../../../docs/audits/target_c_unit_edge_lattice_interior_shell_exclusion_independent_audit_2026-10-10.md) · source SHA-256 `1fc0ef474e21ea1c4a356c63f9255cc8c669b31ffa4f74bfbd902ca4860fd293`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-641E7B0D30BC","canonical":true,"claim_ids":["C-UNIT-EDGE-HULL-SINGLE-LATTICE-INTERIOR-RADIAL-EXCESS"],"claim_statuses":{"C-UNIT-EDGE-HULL-SINGLE-LATTICE-INTERIOR-RADIAL-EXCESS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.244 — unit-edge hulls with a single lattice interior

Date: 2026-10-10. Canonical base: origin/main=9fa87641abc2abfe2a2046aa68653e7e5ff62177,
state 2026-10-10.audit.232.

Frozen candidate: origin/research/level-i-fused-review-20261009 at
6132201c1d3056ca68a222217094acb819f5b4d7. Source report:
docs/reports/target_c_full_source_lattice_conflict_deletion_reserve_2026-10-09.md,
SHA-256 a8e0334ad495eb5e4eefda1d1b4a1a5a1bf3a14e5851ef46e99cd4d2bfca70a2.
Only Sections 7.1–7.4 are audited here.

## Verdict

**PASS — promote the exact single-lattice interior exclusion.** Let $`A`$ be
a finite planar unit-separated global $`n`$-point diameter minimizer of
diameter $`D`$. Suppose its convex hull $`F`$ is a convex polygon with $`q`$
unit edges and every non-hull point of $`A`$ belongs to one translate and
rotation of a triangular lattice with spacing $`\lambda\ge1`$. There are
absolute constants $`c>0,D_0`$ such that, for $`D\ge D_0`$, every disk of
radius $`R`$ containing $`F`$ satisfies
```math
R^2-D^2/4\ge cD^{2/3}.
```
Thus a global minimizer in this source class cannot have circumradius
$`D/2+o(D^{-1/3})`$.

As a consequence, for odd $`q`$ tending to infinity, a regular unit-side
$`q`$-gon with all additional source points inside it and in one triangular
lattice of spacing at least one cannot be a global diameter minimizer. Its
exact excess $`R^2-D^2/4=1/(16\cos^2(\pi/(2q)))\le1/12`$ contradicts the
lower bound.

This is a scoped source-class exclusion. It does not establish that the
interior of a general global minimizer lies in one lattice, and it gives no
Target C or Level I closure.

## Independent proof

Write $`a_0=\sqrt3/2`$. The population reserve already canonical as
C-GLOBAL-POPULATION-EXCESS-TWO-THIRDS-RESERVE supplies an absolute
$`\kappa>0`$ such that
```math
g_A:=n-1-\frac{\pi D^2}{4a_0}\ge\kappa D^{2/3}
```
for $`D\ge2`$.

First, every non-hull source point $`x`$ lies at distance at least $`a_0`$
from $`\partial F`$. A closest point on the boundary is either a hull
vertex, where unit separation gives distance at least one, or lies in a
unit edge. In the latter case, with projection coordinate $`t\in[0,1]`$
and perpendicular distance $`h`$, separation from both edge endpoints gives
```math
h^2\ge\max\{1-t^2,\ 1-(1-t)^2\}\ge3/4.
```
Thus the non-hull points lie in the erosion $`F\ominus a_0B`$. If
$`F\subset\overline B(o,R)`$, this erosion is contained in
$`\overline B(o,R-a_0)`$.

Huxley's Theorem A in the author's Oberwolfach Report 14/2008,
pp. 703–704, gives the translated smooth-oval discrepancy estimate for
every fixed exponent $`\theta>131/208`$. The full proof in the 2003 article
was not inspected. A closed radius-$`r`$ disk is contained in the open
disk of radius $`r+r^{-2}`$, whose area differs by $`O(r^{-1})`$, so the
same estimate gives the needed closed-disk upper bound. See
[Huxley's Oberwolfach report](https://publications.mfo.de/bitstream/handle/mfo/3058/OWR_2008_14.pdf?isAllowed=y&sequence=1)
and [the 2003 article](https://doi.org/10.1112/S0024611503014485).
```math
\#((z+\Lambda)\cap\overline B(o,r))
=\frac{\pi r^2}{a_0}+O_\theta(1+r^\theta),
```
uniformly over translations for the fixed triangular lattice. For a
rotated lattice, rotate the disk and translation instead. For spacing
$`\lambda\ge1`$, scale coordinates by $`1/\lambda`$; the error is bounded
by $`O_\theta(1+r^\theta)`$ uniformly in $`\lambda`$, including the case
$`r/\lambda<1`$. Therefore the number of non-hull source points is at most
```math
\frac{\pi(R-a_0)^2}{a_0}+O_\theta(1+R^\theta).
```

The hull has $`q`$ vertices and perimeter $`q`$, since all its edges are
unit. A convex body contained in a radius-$`R`$ disk has perimeter at most
$`2\pi R`$. Hence
```math
n\le q+\frac{\pi(R-a_0)^2}{a_0}+O_\theta(1+R^\theta)
=\frac{\pi R^2}{a_0}+\pi a_0+O_\theta(1+R^\theta).
```
If $`R\ge D`$, then $`R^2-D^2/4\ge3D^2/4`$, which is stronger than
required for large $`D`$. Otherwise $`R<D`$, so the error is
$`O_\theta(D^\theta)`$. Subtracting $`\pi D^2/(4a_0)+1`$, and using
the global population reserve, gives
```math
\kappa D^{2/3}\le g_A
\le\frac{\pi}{a_0}(R^2-D^2/4)+O_\theta(D^\theta).
```
Since $`\theta<2/3`$, increasing $`D_0`$ absorbs the error into
$`\kappa D^{2/3}/2`$. One may take $`c=a_0\kappa/(2\pi)`$.

For an odd regular $`q`$-gon of unit side,
```math
R=\frac1{2\sin(\pi/q)},\qquad
D=\frac1{2\sin(\pi/(2q))},
```
and the stated excess identity follows directly. It remains bounded as
$`q\to\infty`$, whereas $`D^{2/3}\to\infty`$; therefore the regular-shell
family is excluded in the stated one-lattice source class.

## Hostile checks and limits

- The lower bound uses all source labels: the hull vertices contribute
  $`q`$, and every non-hull source point, including contact isolates, is
  counted in the lattice disk bound.
- The lattice condition is imposed only on the non-hull points. No
  crystallization or common lattice chart is inferred from global
  optimality.
- The circumradius estimate applies to any containing disk; it is not a
  claim that a minimum enclosing disk is attained at a specified center.
- This is an analytic theorem, not a finite enumeration. No verifier
  encodes the discrepancy estimate, erosion bound, or global-minimizer
  implication. The fused-review branch's finite checkers are not evidence
  for these steps.
- Section 4.2's triangle-free deformation and Section 8's proposed
  approximate stability bridge are outside this audit.

## Canonical disposition

Promote C-UNIT-EDGE-HULL-SINGLE-LATTICE-INTERIOR-RADIAL-EXCESS, dependent on
the canonical global population reserve. It excludes a narrow one-lattice
shell scenario but does not settle the full-source shell/interface payment
or change the active C-II frontier.
