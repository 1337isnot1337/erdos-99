<!-- theorem-state: {"artifact_id":"ART-9AC44B910DDA","canonical":true,"claim_ids":["C-CANONICAL-NEAR-ISOLATE-POPULATION-BOUND","C-CONTACT-MINIMAL-HULL-COVERAGE","C-CONVEX-POLYGON-ANGULAR-AREA-BOUND","C-FULL-SOURCE-SPACING-DEBIT","C-UNIT-VORONOI-CELL-AREA-SURPLUS"],"claim_statuses":{"C-CANONICAL-NEAR-ISOLATE-POPULATION-BOUND":"canonical","C-CONTACT-MINIMAL-HULL-COVERAGE":"canonical","C-CONVEX-POLYGON-ANGULAR-AREA-BOUND":"canonical","C-FULL-SOURCE-SPACING-DEBIT":"canonical","C-UNIT-VORONOI-CELL-AREA-SURPLUS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.163 — full-source Voronoi population bounds

**Audit base:** `origin/main=e0343614eac964a57273b564d0b1bd673f821f3e`,
state `2026-10-08.audit.158`; C-I is closed, C-II and Level I remain open.

**Frozen research source:** `origin/research/level-i-closure-20261007` at
`871c56111c479d536b17a51d21fcd04fa86d8931`.

**Source artifacts:**

- `docs/reports/target_c_full_source_voronoi_defect_spacing_debit_2026-10-08.md`,
  SHA-256 `790afc3b6f832f27dd29d64cc6f1769d38235ba4f446a79f8d65a6388603c2f0`;
- `research/verify_target_c_voronoi_spacing_debit_2026_10_08.py`,
  SHA-256 `82d8e392ce31b5fc6ed7b52b8ac236fbd0635b0075d09dae434386c3edf11709`;
- imported exact-field helper
  `research/verify_target_c_three_direction_corner_barrier_2026_10_06.py`,
  whose `Q(a+b*sqrt(3))` operations and sign test were inspected.

The research branch was not edited. The verifier was run from a detached
worktree at the frozen source commit. This audit separates the universal
claims from finite certificates and from the source's nonglobal fixtures.

## Claims and verdicts

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Contact-minimal hull coverage | PASS — promote | `C-CONTACT-MINIMAL-HULL-COVERAGE` |
| Convex-polygon angular area bound | PASS — promote | `C-CONVEX-POLYGON-ANGULAR-AREA-BOUND` |
| Unit Voronoi cell area and near-isolation surplus | PASS — promote | `C-UNIT-VORONOI-CELL-AREA-SURPLUS` |
| Full-source near-isolated population bound | PASS — promote | `C-CANONICAL-NEAR-ISOLATE-POPULATION-BOUND` |
| Oler spacing debit | PASS — promote | `C-FULL-SOURCE-SPACING-DEBIT` |
| Nonglobal congestion/augmentation fixtures | REGRESSION ONLY | No global-minimizer or Level I counterexample |

## Exact promoted statements

### `C-CONTACT-MINIMAL-HULL-COVERAGE`

Let `A` be a finite triangle-free global minimum-diameter source with
`|A|>=2`, chosen contact-minimal, and let `K=conv(A)`. Every `z in K` is
within distance one of at least one label of `A`. This result does not use
diameter-pair minimality.

### `C-CONVEX-POLYGON-ANGULAR-AREA-BOUND`

Let a convex polygon contain the closed disk of radius `r>0` centered at the
origin, and suppose every polygon vertex has distance at least `r0>=r` from
the origin. If `r<r0`, then

\[
\operatorname{area}(P)\ge
\frac{\pi r\sqrt{r_0^2-r^2}}{\arccos(r/r_0)}.
\]

At `r=r0`, the right side is interpreted by continuity as `pi*r0^2`, which
also follows directly from disk containment.

### `C-UNIT-VORONOI-CELL-AREA-SURPLUS`

For any full bounded Voronoi cell of a planar set whose distinct centers are
at least one apart, the cell area is at least `a0=sqrt(3)/2`. Equality is
possible only for the regular hexagonal cell with its six unit-spaced
neighbor centers. If the center is `delta`-near-isolated, meaning its
distance from every other center is strictly greater than `1+delta` for
`delta>0`, then

\[
|V_x|\ge a_0+\delta.
\]

The equality characterization and the non-strict base area bound are the
scaled theorem of Mazel, Stuhl, and Suhov. Their original unit-disk centers
are separated by at least two and have minimum Voronoi-cell area `2*sqrt(3)`;
scaling coordinates by one half gives the normalization above. The original
source and proof were checked in [arXiv:2211.03255v1](https://arxiv.org/pdf/2211.03255v1),
Theorem on pp. 3–4. The linear `a0+delta` surplus is the independently
reconstructed polygon argument below.

### `C-CANONICAL-NEAR-ISOLATE-POPULATION-BOUND`

Let `A` be a finite noncollinear triangle-free global minimum-diameter
source, chosen contact-minimal, with the complete source retained. Write
`D=diam(A)` and let `Z_delta` be the set of labels at distance strictly
greater than `1+delta` from every other original label. For every `delta>0`,

\[
|Z_\delta|<\left(\frac{4\sqrt{3}}{\delta}+8\right)D+1.
\]

Consequently, along any such sequence with `delta=delta(D)->0` and
`D*delta(D)->infinity`, `|Z_delta|=o(D^2)`. This bounds only the
near-unit-free labels; it does not bound all contact-isolated labels.

### `C-FULL-SOURCE-SPACING-DEBIT`

Let `A=X disjoint-union Y` be any finite unit-separated source of diameter
`D>0`. Let `c>0`, `lambda=1+c/D`, and suppose every two distinct labels of
`Y` are at least `lambda` apart. With
`Delta=pi/(2*sqrt(3))` and `g_A=|A|-1-Delta*D^2`,

\[
g_A\le |X|-\Delta D^2(1-\lambda^{-2})+\frac{\pi D}{2\lambda}.
\]

If such partitions are supplied along canonical global-minimizer sources
with `|X|<=bD+o(D)` for fixed `b,c`, the strict canonical inequality
`g_A>0` requires `b>=2*c*Delta-pi/2`. This is a necessary condition only.

## Independent proof reconstruction

### Hull coverage

If some `z in K` were strictly farther than one from every label, globality
first guarantees an old unit pair: otherwise scaling the whole source down
until its closest pair is at one would reduce its diameter. Delete an endpoint
`v` of an old unit pair and insert `z`. Distances among retained labels are
unchanged; every new lower-distance constraint is strict; and every new
distance is at most `D`, since both endpoints lie in `K` and a convex hull has
the same diameter as its generating finite set. The inserted point has no
unit contact, so the new contact graph is the old induced graph plus an
isolated vertex and remains triangle-free. If the new diameter is below `D`
global minimality fails; if it equals `D`, contact minimality fails. This
contradiction proves the claim. It retains every label other than `v`,
including contact isolates.

### Polygon area inequality

Join the origin to consecutive polygon vertices. Their radii are `a,b`, and
the intervening angle `phi` lies in `(0,pi)`. The altitude `h` to the side is
at least `r`. The exact altitude identity and `a^2+b^2>=2ab` give

\[
h^2=\frac{a^2b^2\sin^2\phi}{a^2+b^2-2ab\cos\phi}
\le ab\cos^2(\phi/2).
\]

Thus `ab>=r^2 sec^2(phi/2)` and, independently, `ab>=r0^2`. The triangle
area is therefore at least
\[
\max\{\tfrac12r_0^2\sin\phi,\ r^2\tan(\phi/2)\}.
\]
Put `theta0=arccos(r/r0)`. On `0<phi<=2*theta0`, the first expression
divided by `phi` is bounded below by
`r*sqrt(r0^2-r^2)/(2*theta0)`, since `sin(phi)/phi` decreases. On
`2*theta0<=phi<pi`, the second divided by `phi` has the same lower bound,
since `tan(phi/2)/phi` increases. Summing over the consecutive angles, whose
sum is `2*pi`, yields the displayed formula. The limit at `r=r0` is
`pi*r0^2`.

### Voronoi surplus

The imported theorem gives the base `a0` cell area and its equality case. A
full bounded Voronoi cell vertex is a circumcenter of at least three
unit-separated sites. In that triangle, the smallest angle is at most
`pi/3`; its opposite side is at least one. The sine rule therefore puts every
cell vertex at radius at least `r0=1/sqrt(3)` from its center. A
`delta`-near-isolated center has a Voronoi cell containing the disk of radius
`r=(1+delta)/2`.

For `1/2<=r<r0`, apply the polygon bound `H(r,r0)`. With
`r=r0*cos(theta)`, `0<theta<=pi/6`,

\[
H=\pi r_0^2\frac{\sin(2\theta)}{2\theta},\qquad
\frac{dH}{dr}=\frac{\pi r_0}{2}
\frac{\sin(2\theta)-2\theta\cos(2\theta)}
{\theta^2\sin\theta}\ge2.
\]

The numerator is `integral_0^(2 theta) t*sin(t) dt`. Concavity gives
`sin(t)>=3*sqrt(3)*t/(2*pi)` on `[0,pi/3]`, and `sin(theta)<=theta`,
which proves the derivative bound. Since `H(1/2,r0)=a0` and
`delta=2r-1`, integration gives `H>=a0+delta`. For `r>=r0`, disk
containment gives area at least `pi*r^2`; at `r0` this exceeds the required
linear value, and its derivative with respect to `delta` is `pi*r>1`, so
the same bound continues. In a triangle-free source, equality in the imported
base theorem is also impossible because the regular hexagonal neighbor ring
creates unit equilateral triangles.

### Full-source count and spacing debit

Let `J` be the source labels whose Voronoi cells clipped to `K` touch
`\partial K`, and `m=|J|`. The remaining `n-m` cells are full bounded cells.
Put `sigma_x=|V_x|-a0` on those full cells and
`A_partial=sum_{x in J}|V_x intersect K|`. Their areas partition `K` up to
zero-area boundaries. With `delta_K=pi*D^2/4-area(K)` and
`g_A=n-1-Delta*D^2`, exact cancellation gives

\[
\sum_{x\notin J}\sigma_x+A_{\partial}+\delta_K
=a_0(m-1)-a_0g_A.
\]

All terms on the left are nonnegative. By hull coverage, each label in `J`
lies within one of `\partial K`; its radius-`1/2` disk is in the outer
parallel body `K+B(0,1/2)` and outside the interior of the erosion
`K minus B(0,3/2)`. These disks have disjoint interiors. Steiner's formula
gives outer area `area(K)+P/2+pi/4`; integrating the decreasing perimeters
of convex inner parallel bodies bounds the lost inner layer by `3P/2`.
Thus the containing belt has area at most `2P+pi/4`, and disk counting
gives `m<=8P/pi+1<=8D+1` by Cauchy's perimeter formula.

For every delta-near-isolated label outside `J`, the Voronoi surplus gives
`sigma_x>=delta`; all other `sigma_x>=0` by the imported theorem. Hence
`delta*z_int+A_partial+delta_K<a0(m-1)`, where `z_int` counts such interior
labels. At most `m` such labels are in `J`. Substituting `m<=8D+1` proves
the strict stated bound.

For the spacing debit, scale `Y` and its convex hull by `1/lambda`. It is a
unit-separated set in a convex body with area at most `pi*D^2/(4*lambda^2)`
and perimeter at most `pi*D/lambda`. Canonical Oler gives
`|Y|-1<=Delta*D^2/lambda^2+pi*D/(2*lambda)`. Substituting
`|A|=|X|+|Y|` proves the exact inequality. Expansion of
`D^2*(1-lambda^-2)` gives `2*c*D+O(1)` and hence the necessary leading-order
condition. The imported inequality is Lemma 21.1 of the canonical shared
module `docs/theory/03-oler-shell.md`.

## Verifier boundary and hostile checks

The exact verifier was inspected and rerun at `871c5611`. It reconstructs
clipped Voronoi cells for six rational/quadratic-field grids, checks all
source and same-cardinality competitor pairs, cell coverage, areas, the
exact area ledger, the local near-isolation surplus on those fixtures, and a
seven-site hexagonal equality fixture. It also certifies the rational pi
bounds and 1,000 finite arithmetic samples for the augmentation calculation.
All passed: 9,432 source-pair checks, 9,432 competitor-pair checks, 310
clipped cells, 1,704 cell-vertex coverage checks, and six unit triangles in
the equality fixture. The universal arguments above are analytic; grid
sampling does not prove them or any global-optimality claim.

The following scope checks were binding:

- `delta`-near-isolated labels are a strict subset of contact isolates; the
  theorem does not bound all isolates or dense contact-isolated chambers.
- Boundary cells are kept in `A_partial`; the full-cell area theorem is never
  applied to a clipped boundary cell.
- The population count uses `g_A>0` from canonical full-source geometry and
  retains all original source labels.
- The spacing debit needs separation only within `Y`; no claim is made that
  enlarging a `Y` subset yields a feasible source or a global minimizer.
- The named congestion and lattice fixtures are nonglobal regressions. They
  are not Level I counterexamples, and their broader closure applications
  remain unproved.

**Verdict: PASS — promote all five listed claims with the exact scopes above.**
The near-isolated count supplies a source-population restriction but no
shallow blocker closure, controlled merger, wall move, or refill. No
authoritative Target C endpoint changes; C-II and Level I remain open.
