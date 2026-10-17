> Generated reading edition · [exact source](../../../docs/audits/target_c_population_excess_sharp_coefficient_independent_audit_2026-10-10.md) · source SHA-256 `e795de8e2d3f65592921cf39a2c4462da9e4269e7beb24a2c8d014c745836a41`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-618AB04808AD","canonical":true,"claim_ids":["C-GLOBAL-POPULATION-EXCESS-ASYMPTOTIC-COEFFICIENT"],"claim_statuses":{"C-GLOBAL-POPULATION-EXCESS-ASYMPTOTIC-COEFFICIENT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.243 — explicit asymptotic coefficient for the population reserve

Date: 2026-10-10. Canonical base: origin/main=1c12b5dcbbc5cc9b0cc9ffd697d77f9bfffe01d8,
state 2026-10-10.audit.231.

Frozen candidate: origin/research/level-i-fused-review-20261009 at
6132201c1d3056ca68a222217094acb819f5b4d7. Source report:
docs/reports/target_c_full_source_lattice_conflict_deletion_reserve_2026-10-09.md,
SHA-256 a8e0334ad495eb5e4eefda1d1b4a1a5a1bf3a14e5851ef46e99cd4d2bfca70a2.

## Verdict

**PASS — promote only the explicit asymptotic population coefficient.** For
every fixed $`\theta`$ with $`131/208<\theta<2/3`$, there are constants
$`C_\theta,D_\theta`$ such that every planar unit-separated global
$`n`$-point diameter minimizer with diameter $`D\ge D_\theta`$ satisfies

```math
g_A:=n-1-\frac{\pi D^2}{2\sqrt3}
\ \ge\ \kappa_0 D^{2/3}-C_\theta D^\theta,
\qquad
\kappa_0=\frac{3\pi}{5a_0}\left(\frac{3a_0}{16}\right)^{2/3},
\quad a_0=\frac{\sqrt3}{2}.
```

In particular, along every sequence of such minimizers with $`D\to\infty`$,
$`\liminf g_A/D^{2/3}\ge\kappa_0`$ (approximately $`0.647826`$).
This sharpens the coefficient in canonical
C-GLOBAL-POPULATION-EXCESS-TWO-THIRDS-RESERVE asymptotically. The older
explicit finite-range square-root reserve remains separately useful; no
uniform finite-$`D`$ dominance between the two bounds is claimed.

The result does not use a structural hypothesis on a minimizer and does not
give a source move, a unit-triangle conclusion, C-II closure, or Level I.
Only the Section 9 sharp-coefficient claim is audited here. The candidate's
triangle-free deformation, one-lattice shell exclusion, and their separate
literature applications remain outside this promotion.

## Literature input

The needed disk estimate is the fixed-circle specialization of Martin N.
Huxley's Theorem A in *Configurations of Lattice Points*, Oberwolfach Report
14/2008, printed pages 703–704. The report states that under $`C^3`$
smoothness,
```math
N(r,P)=A r^2+O(r^{131/208+\varepsilon}),
```
for every $`\varepsilon>0`$, where $`P`$ is the translation parameter. The
original 2003 article's full proof was not inspected; the Oberwolfach report
is Huxley's own reliable transcription of the result. The circle is $`C^\infty`$,
and this audit uses only the estimate for disks centered at the origin in the
fixed unit triangular lattice, not a uniform translated-domain consequence.
[Huxley, Oberwolfach Report 14/2008](https://publications.mfo.de/bitstream/handle/mfo/3058/OWR_2008_14.pdf?isAllowed=y&sequence=1);
[Huxley, *Exponential Sums and Lattice Points III*](https://doi.org/10.1112/S0024611503014485).

Thus, for any fixed $`\theta\in(131/208,2/3)`$, the centered disk count obeys
```math
N(r):=\#\{\lambda\in\Lambda:|\lambda|\le r\}
=\frac{\pi r^2}{a_0}+O_\theta(r^\theta).
```
The constant may depend on the chosen $`\theta`$, which is fixed throughout
the argument.

## Independent reconstruction

Put $`A_1=\pi/a_0`$. Fix a positive $`c`$, let
```math
\delta=cD^{-1/3},\qquad S=D/2+\delta,
```
and let $`L_S(s)`$ be the area of intersection of two radius-$`S`$ disks whose
centers are distance $`s`$ apart. For $`d=2S-s\in[0,2\delta]`$, direct
integration of the two circular caps gives
```math
L_S(2S-d)=4\int_0^{d/2}\sqrt{2St-t^2}\,dt
=\frac43\sqrt S\,d^{3/2}\left(1+O(d/S)\right),
```
uniformly on this interval. In particular $`L_S(D)=O_c(1)`$, and
$`L_S(2S)=0`$.

Every triangular-lattice difference vector of length at least $`D`$ arising
from two sites in the open radius-$`S`$ disk lies in
```math
\{w\in\Lambda:D\le |w|<2S\}.
```
Use the centered disk counting function above and Stieltjes integration by
parts with the nonincreasing weight $`L_S`$. Taking the left limit $`N(D^-)`$
at the lower endpoint includes every vector with $`|w|=D`$. The discrepancy
term is bounded by
```math
O_\theta(D^\theta)\operatorname{Var}_{[D,2S]}(L_S)
=O_{c,\theta}(D^\theta),
```
because the interval has radii comparable to $`D`$, the total variation is
$`L_S(D)=O_c(1)`$, and the upper endpoint weight is zero. Therefore
```math
\sum_{\substack{w\in\Lambda\\D\le|w|<2S}}L_S(|w|)
=\frac1{a_0}\int_D^{2S}2\pi sL_S(s)\,ds+O_{c,\theta}(D^\theta).
```
Substituting the cap expansion, with $`d=2S-s`$, yields
```math
\int_D^{2S}L_S(s)\,ds
=\frac{32}{15}\sqrt D\,\delta^{5/2}(1+o(1)),
```
and hence
```math
\sum_{\substack{w\in\Lambda\\D\le|w|<2S}}L_S(|w|)
=\frac{64\pi}{15a_0}c^{5/2}D^{2/3}
+O_{c,\theta}(D^\theta).
```
The error from replacing $`s`$ by $`D`$ and $`S`$ by $`D/2`$ is smaller than
the displayed discrepancy error.

Translate $`\Lambda`$ uniformly over a fundamental parallelogram. Let $`N(z)`$
count its sites in the open radius-$`S`$ disk and let $`E(z)`$ count unordered
pairs in that disk at distance at least $`D`$. The first expectation is exactly
```math
\mathbb E N=\frac{\pi S^2}{a_0}
=\frac{\pi D^2}{4a_0}
+\frac{\pi}{a_0}cD^{2/3}+O(D^{-2/3}).
```
For each fixed difference vector $`w`$, the translation average of ordered
pairs separated by $`w`$ is $`L_S(|w|)/a_0`$; summing over $`w`$ and dividing
by two counts each unordered pair once. Thus
```math
\mathbb E E
=\frac{1}{2a_0}
\sum_{\substack{w\in\Lambda\\D\le|w|<2S}}L_S(|w|)
=\frac{32\pi}{15a_0^2}c^{5/2}D^{2/3}
+O_{c,\theta}(D^\theta).
```
The exact-distance ties are included in $`E`$, as required for a strict
diameter improvement after deletion.

The mean of the integer-valued quantity $`N-E`$ is therefore at least
```math
\frac{\pi D^2}{4a_0}
+\left(\frac{\pi}{a_0}c-\frac{32\pi}{15a_0^2}c^{5/2}\right)D^{2/3}
-C_{c,\theta}D^\theta.
```
The coefficient is maximized at
```math
c_*=\left(\frac{3a_0}{16}\right)^{2/3}<1,\qquad
\kappa_0=\frac{3\pi}{5a_0}c_*.
```
Some translate has $`N-E`$ at least its mean. In the finite conflict graph,
delete one chosen endpoint of each edge. At most $`E`$ vertices are deleted,
so at least $`N-E`$ remain; all remaining pair distances are strictly below
$`D`$, and unit lattice separation is preserved. Consequently the triangular
lattice supplies a finite strict-sub-$`D`$ competitor with at least
```math
\frac{\pi D^2}{4a_0}+\kappa_0D^{2/3}-C_\theta D^\theta
```
sites.

If this competitor had at least $`n`$ sites, any $`n`$-point subset would
contradict global minimality. Its integer population is therefore at most
$`n-1`$. Comparing gives the promoted inequality with no rounding loss.
No original minimizer label is moved or deleted.

As an algebraic corollary, define
```math
T=\sqrt{\frac{4a_0(n-1)}{\pi}}.
```
The same inequality implies for the minimum diameter
```math
D(n)\le T-\frac65\left(\frac{3a_0}{16}\right)^{2/3}T^{-1/3}
+o(T^{-1/3}).
```
If $`T-D(n)`$ is already larger than a fixed multiple of $`T^{-1/3}`$, the
bound is immediate; otherwise $`D(n)/T\to1`$ and the population inequality
gives the displayed coefficient.

## Hostile checks and exact limits

- The weighted annulus estimate is for the fixed centered lattice count; it
  does not assume a uniform discrepancy constant over a changing family of
  translated or rotated ovals.
- Lattice vectors with length exactly $`D`$ are included at the lower
  Stieltjes endpoint. Omitting them would not ensure a strict-sub-$`D`$
  competitor.
- The deletion is performed only in the independent lattice comparison. The
  proof preserves the all-minimizer quantifier and imposes no triangle-free,
  contact-minimality, KKT, stress, or source-extraction hypothesis.
- The source branch's finite verify_target_c_two_port_triangular_limits_2026_10_09.py
  checker concerns a different two-port claim; it is not evidence for this
  analytic lattice estimate. No finite verifier is registered or claimed here.
- This audit makes no disposition of the source report's Sections 4.2, 7, or
  7.1–7.4. In particular, the separate one-lattice shell exclusion is not
  inferred from the population reserve.

## Canonical disposition

Promote C-GLOBAL-POPULATION-EXCESS-ASYMPTOTIC-COEFFICIENT with no internal
theorem dependency. It sharpens the coefficient in the existing global
population reserve but does not change the C-II payment obligation: a
source-wide shell/interface upper bound with a sub-$`D^{2/3}`$ error is still
missing. C-II and Level I remain open.
