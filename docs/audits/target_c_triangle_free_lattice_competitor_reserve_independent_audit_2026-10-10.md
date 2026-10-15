<!-- theorem-state: {"artifact_id":"ART-9C5C9CB6A19C","canonical":true,"claim_ids":["C-TRIANGLE-FREE-PACKING-DENSITY-CAP-REGRESSION","C-TRIANGULAR-LATTICE-STRICT-D-COMPETITOR-RESERVE"],"claim_statuses":{"C-TRIANGLE-FREE-PACKING-DENSITY-CAP-REGRESSION":"regression","C-TRIANGULAR-LATTICE-STRICT-D-COMPETITOR-RESERVE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C Audit.245 — triangle-free lattice competitor reserve

Date: 2026-10-10. Canonical base: origin/main=5d93ac0eec111ee56e07548f55085fd553b9e4f5,
state 2026-10-10.audit.233.

Frozen candidate: origin/research/level-i-fused-review-20261009 at
6132201c1d3056ca68a222217094acb819f5b4d7. Source report:
docs/reports/target_c_full_source_lattice_conflict_deletion_reserve_2026-10-09.md,
SHA-256 a8e0334ad495eb5e4eefda1d1b4a1a5a1bf3a14e5851ef46e99cd4d2bfca70a2.
Only Section 4.2 is audited here.

## Verdict

**PASS — promote the strict-diameter lattice competitor and its triangle-free
deformation.** There is an absolute constant \(\kappa>0\) such that for
every real \(D\ge2\) there is a finite unit-separated triangle-free set
\(X_D\subset\mathbb R^2\) satisfying
\[
\operatorname{diam}(X_D)<D,\qquad
|X_D|\ge\frac{\pi D^2}{2\sqrt3}+\kappa D^{2/3}.
\]
Thus a uniform upper bound of the form
\(\pi D^2/(2\sqrt3)+o(D^{2/3})\) cannot hold for all finite
triangle-free unit-separated sets of diameter below \(D\).

This is a packing-class regression only. The constructed set is not claimed
to be a global minimizer or a source-level deformation of any minimizer.

## Independent reconstruction

First construct the strict-diameter competitor. For the unit triangular
lattice \(\Lambda\) with covolume \(a_0=\sqrt3/2\), the disk discrepancy
bound, uniform over translations, is
\[
\#((z+\Lambda)\cap B_r)=\frac{\pi r^2}{a_0}+O(r^{2/3}).
\]
For \(0<c\le1\), set \(\delta=cD^{-1/3}\) and \(S=D/2+\delta\). The number
of possible difference vectors with lengths in \([D,D+2\delta)\) is at
most \(K_0D^{2/3}\), by subtracting an open inner disk count from a closed
outer disk count. For each such vector, the intersection area of the
radius-\(S\) disks controlling its translation-averaged pair count is at
most \((8\sqrt2/3)c^{3/2}\). Hence the expected number \(E\) of unordered
pairs at distance at least \(D\), under a uniform lattice translate, is at
most \(K_1c^{3/2}D^{2/3}\), where \(K_0,K_1\) are absolute.

The expected number \(N\) of lattice sites in the open radius-\(S\) disk is
exactly \(\pi S^2/a_0\), so
\[
\mathbb E(N-E)\ge
\frac{\pi D^2}{4a_0}
+\left(\frac{\pi}{a_0}c-K_1c^{3/2}\right)D^{2/3}.
\]
Choose a sufficiently small fixed \(c>0\) so the parenthesized
coefficient is a positive absolute \(\kappa\). Some translate has integer
\(N-E\) at least this mean. Delete one chosen endpoint of every pair at
distance at least \(D\). At most \(E\) sites are deleted; the remaining
finite set \(Y_D\) is unit-separated, has diameter strictly below \(D\),
and has cardinality at least
\[
\frac{\pi D^2}{4a_0}+\kappa D^{2/3}
=\frac{\pi D^2}{2\sqrt3}+\kappa D^{2/3}.
\]
This is the lattice conflict-deletion construction independently audited
for the population reserve in Audit.199. Here it is used only to supply the
finite set that will be deformed.

Represent the points of \(Y_D\) by their distinct lattice indices
\((i,j)\in\mathbb Z^2\), and deform the basis vectors from angle \(\pi/3\)
to angle \(\pi/3+\varepsilon\), keeping each basis vector unit. For any
pair of indices with difference \((m,n)\), squared distance changes
continuously from \(m^2+n^2+mn\) to
\[
m^2+n^2+2mn\cos(\pi/3+\varepsilon).
\]
Among nonzero integer differences, the original unit vectors are exactly
\((\pm1,0),(0,\pm1),(1,-1),(-1,1)\). The first four remain unit; the last
two become strictly longer than one. Every other difference in the finite
set had length strictly above one at \(\varepsilon=0\), so a sufficiently
small positive \(\varepsilon\) keeps all of those lengths above one. The
original set also has a strict diameter margin below \(D\); by continuity,
choose \(\varepsilon\) still smaller so the deformed diameter remains below
\(D\). Cardinality is unchanged.

After deformation, every unit contact changes one index coordinate by
\(\pm1\) and leaves the other unchanged. Coloring each point by the parity
of \(i+j\) makes every unit contact cross the two color classes. The contact
graph is bipartite and therefore has no triangle. This proves the asserted
triangle-free competitor for each \(D\), with no uniform lower bound on
\(\varepsilon\) required.

## Hostile checks and limits

- The conflict deletion counts distance-\(D\) ties as conflicts, which
  ensures the remaining diameter is strictly below \(D\).
- The perturbation is selected separately for each finite set; no
  source-uniform or asymptotically uniform deformation size is asserted.
- Bipartiteness follows from the actual index differences of all remaining
  unit contacts; no contact outside the two basis directions is assumed
  absent without the finite positive-gap continuity check.
- The result refutes an unqualified triangle-free packing density cap at
  error \(o(D^{2/3})\). It gives no counterexample to global optimality and
  no conclusion about triangle-free global minimizers.
- No finite verifier proves the discrepancy estimate or continuum
  perturbation argument. No source-branch finite checker is used as proof.

## Canonical disposition

Promote C-TRIANGULAR-LATTICE-STRICT-D-COMPETITOR-RESERVE and record
C-TRIANGLE-FREE-PACKING-DENSITY-CAP-REGRESSION, with the latter depending
on the former. The all-minimizer population reserve from Audit.199 also
depends on the now-registered strict-diameter competitor. This blocks the
use of a triangle-free-only density ceiling with sub-\(D^{2/3}\) error as
the missing C-II payment. The active full-source shell/interface obligation
and Level I remain open.
