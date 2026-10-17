> Generated reading edition · [exact source](../../../docs/audits/target_c_one_deficit_delaunay_defect_budget_independent_audit_2026-10-08.md) · source SHA-256 `bc2c99c5a327b7c539735c8192108ad5e5b2d89ab3f61f51341f0d6d113643b2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-686233C5C892","canonical":true,"claim_ids":["C-UNIT-WALL-DELAUNAY-DEFECT-BUDGET","C-UNIT-WALL-ONE-DEFICIT-DICHOTOMY"],"claim_statuses":{"C-UNIT-WALL-DELAUNAY-DEFECT-BUDGET":"canonical","C-UNIT-WALL-ONE-DEFICIT-DICHOTOMY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.161 — unit-wall Delaunay defect budget

**Date:** 2026-10-08  
**Audit base:** `origin/main=88c030143feaa7cead83d4d49a05cf8faa2a0e62`, state `2026-10-08.audit.156`  
**Frozen source:** `research/sol/target-c-overnight-closure-20261007` at `c6a75bd708e553c4feb3a540e0b17f3b65e22a82` (66 commits ahead of main; 126 main-only)  
**Source artifact:** `docs/reports/target_c_one_deficit_delaunay_completion_and_defect_budget_2026-10-07.md`, Git blob `19bd2ab09b0719ec42406ab7b2787ad201dd16bd`, SHA-256 `65a25b92317133b2ad6d5b7249f5c5380466ba3be3d5e4f7d8207f42a802169b`; introduced at `8ebb9b81` and unchanged at the frozen tip.  
**Audited unit:** the general boundary-order completion/defect estimate and its one-deficit corollary only. The report's possible source-level use is not audited as a theorem.

## Exact claims

Let (F) be a convex polygon with (b) cyclic unit edges and vertices, and let (X) consist of those wall vertices and (z) strict-interior points, with all distinct points of (X) pairwise at distance at least one. Put

$$
a=\frac{\sqrt3}{4},\qquad a_0=2a=\frac{\sqrt3}{2},\qquad
\sigma_0=\operatorname{area}(F)-a(2z+b-2).
$$

Oler's finite inequality gives $\sigma_0\ge0$. Complete (X) to a maximal unit-separated set inside (F), adding (k) auxiliary interior points, and then extend it to a saturated unit-separated packing in the plane without adding points in (F). Let

$$
\sigma=\sigma_0-a_0k.
$$

The promoted statements are:

1. **General defect budget (`C-UNIT-WALL-DELAUNAY-DEFECT-BUDGET`).** The completion has $k\le\sigma_0/a_0$. A Delaunay triangulation restricted to $F$ has $2(z+k)+b-2$ triangular faces, each with nonnegative area excess $\sigma_T=\operatorname{area}(T)-a$, with $\sum_T\sigma_T=\sigma$. If $H$ is the number of right or obtuse faces, then
   $$
   H\le \frac{4\sigma}{\delta},\qquad \delta=\frac{2-\sqrt3}{4}.
   $$
   The union of all faces with $\sigma_T\ge1/100$ and all right/obtuse faces, together with interior vertices of non-six valence not already incident to those faces, has at most
   $$
   \left(450+\frac{12}{\delta}\right)\sigma
   $$
   vertices. Every other triangle is acute, has all sides in $[1,11/10)$, and satisfies $\max_e(|e|-1)\le5\sigma_T$ and $|\angle-\pi/3|\le50\sigma_T$; every interior vertex outside the exceptional set has valence six.
2. **One-deficit alternative (`C-UNIT-WALL-ONE-DEFICIT-DICHOTOMY`).** If $0\le\sigma_0\le a_0+1/1000$, a maximal completion adds zero or one point. If it adds one, the completed cloud has residual slack at most $1/1000$ and the canonical low-slack unit-wall chart theorem applies. If it adds none, the old cloud is saturated inside $F$, and one can choose its auxiliary-plane Delaunay triangulation with at most 51 right/obtuse faces, at most 137 defective faces, and at most 541 exceptional vertices as defined above.

These are fixed-container packing and triangulation statements. Auxiliary additions are not source labels or a same-cardinality competitor. The result gives neither an exact lattice vacancy in the old cloud nor a source-preserving move.

## Independent reconstruction

Oler applied to the $z+b$ labels gives $\sigma_0\ge0$. After $k$ added interior points, it gives $\sigma=\sigma_0-a_0k\ge0$, hence $k\le\lfloor\sigma_0/a_0\rfloor$. A point in the relative interior of a unit wall edge is within distance less than one of an endpoint, so no added point can lie there. Since the packing inside the compact polygon has a finite Oler bound, adding feasible points until none remain terminates.

Extend that maximal-in-(F\) packing by greedy insertion from a countable dense set in the plane. No accepted point lies inside $F$, because the original completion was maximal there. The final packing has covering radius at most one: if some $y$ had distance $d>1$ from it, choose an enumerated point within $(d-1)/3$ of $y$. If rejected, an earlier accepted point within one of that candidate would be strictly closer than $d$ to $y$; if accepted, it would itself be closer than $d$. Both contradict the definition of $d$. Local finiteness follows from unit separation.

Every Delaunay circumradius is therefore at most one. Each unit wall edge is a strict Gabriel edge: for its midpoint $m$, the parallelogram identity and separation from its two endpoints give $|x-m|\ge\sqrt3/2>1/2$ for any other packing point $x$. Thus the wall cycle bounds a triangulated disk whose vertices are exactly the completed points in $F$. Euler's formula gives $2(z+k)+b-2$ faces.

For any face, all side lengths are at least one and its circumradius $R\le1$. By the sine rule each angle is at least $\ell=\arcsin(1/(2R))$, so $R\ge1/\sqrt3$. At fixed $R$, concavity of $\log\sin$ shows the area is minimized when two angles are $\ell$, giving
$$
\operatorname{area}(T)\ge\frac{\sqrt{4R^2-1}}{4R^2}\ge\frac{\sqrt3}{4}=a
\quad (1/\sqrt3\le R\le1).
$$
Summing face areas yields the exact nonnegative excess identity $\sum_T\sigma_T=\sigma$.

For a face with largest angle $\alpha\ge\pi/2$, its opposite side satisfies $L^2\ge2(1-\cos\alpha)>1$, so this side is internal. If $\beta$ is the opposite angle in the Delaunay neighbor, local Delaunay legality gives $\beta\le\pi-\alpha\le\pi/2$. The neighbor's other angles are at least $\pi/6$; concavity of $\log\sin$ and the sine rule give
$$
\operatorname{area}(T')\ge\frac{L^2}{4}\left(\frac{\sqrt3}{2}+\frac12\cot\beta\right)
\ge a(1-\cos\alpha).
$$
The original face has area at least $\tfrac12\sin\alpha$, because its two sides at $\alpha$ are at least one. Therefore
$$
\sigma_T+\sigma_{T'}\ge \frac12\sin\alpha-a(1+\cos\alpha)
\ge \frac{2-\sqrt3}{4}=\delta,
$$
where the middle expression is increasing on $[\pi/2,2\pi/3]$. Summing over all $H$ such faces charges each face excess at most four times (once as the selected face and at most once from each of its three edges), proving $H\delta\le4\sigma$.

There are at most $100\sigma$ faces with excess at least $1/100$. Mark those and all right/obtuse faces as defective. Their vertex union has size at most $3(100+4/\delta)\sigma$. For an interior vertex outside that union with valence $q\ne6$, the incident angle sum is $2\pi$, and the local estimate below implies
$$
50\sum_{T\ni v}\sigma_T\ge |2\pi-q\pi/3|\ge\pi/3,
$$
so its incident excess is strictly greater than $1/50$. Summing over such vertices counts each face at most three times, giving fewer than $150\sigma$ additional exceptional vertices. The total is at most $(450+12/\delta)\sigma$.

For completeness, the local estimates claimed here follow at the report's larger $1/100$ threshold, not just under the canonical chart's global $1/1000$ hypothesis. If an acute triangle's longest side $L\ge\sqrt2$, Heron's formula on the feasible squared-side polygon gives area at least $1/2$, contradicting $a+\sigma_T<a+1/100<1/2$. Otherwise its altitude over the longest side is at least $\sqrt{1-L^2/4}$, hence its area is at least $f(L)=L\sqrt{4-L^2}/4$. Since $f(11/10)>a+1/100$, $L<11/10$; and $f'(L)>1/5$ on $[1,11/10]$, so $L-1\le5\sigma_T$. On the cube of side lengths $[1,11/10]^3$, the sine of every angle exceeds $4/5$, and each side partial derivative of its cosine has absolute value below two. The mean-value estimate gives $|\angle-\pi/3|\le(5/2)\sum_{e\subset T}(|e|-1)\le50\sigma_T$.

For the one-deficit numbers, $\sigma\le\sqrt3/2+1/1000$. Exact inequalities give $4\sigma<52\delta$, $100\sigma<87$, and $150\sigma<131$. Thus there are at most 51 right/obtuse faces and 86 large-excess faces, hence at most 137 defective faces and 411 vertices incident to them. The non-six-valence count is at most 130, for a total of 541. If one point is added, $\sigma=\sigma_0-a_0\in[0,1/1000]$, exactly the scope of canonical `C-UNIT-WALL-LOW-SLACK-TRIANGULAR-CHART`.

## Hostile checks and regression boundary

- The proof uses the full set of wall labels and all interior labels; it does not discard boundary isolates or replace the wall by a scaffold.
- Boundary sides are actual unit edges, and the Delaunay triangulation is taken from an auxiliary saturated plane packing. This does not identify any auxiliary point with a source point.
- A low defect count is not a bound on total metric strain: excess can be spread over many nondefective faces. No global orientation, exact vacancy, or defect-localized metric budget follows.
- The exact diffuse-strain regression in `target_c_one_deficit_diffuse_strain_independent_audit_2026-10-08.md` is compatible with this theorem. Its rational/algebraic verifier was reproduced at the frozen source: all 120, 300, 2,016, and 7,260 pair checks for `M=3,4,7,10` passed. This kills the upgrade from one Oler-unit slack to exact vacancy localization or global optimality; it does not refute the defect counts.
- There is no dedicated computational verifier for these analytic bounds. Reproduced `research/verify_target_c_one_deficit_diffuse_strain_2026_10_07.py` from the frozen source (SHA-256 `ec04da709f68efd21630f045b8a020a223a55feb2af5c836fef3b5a6518ba324`); it verifies only its finite pair ledgers and strict sub-diameter comparison, not the Delaunay theorem.
- The report's bounded inactive-face `O(D)` application still assumes perimeter and area/population slack bounds. Even under those assumptions it supplies an auxiliary completion and `O(D)` defect set, not a source-preserving packet or a C-II contradiction.

## Dependencies and verdict

`C-UNIT-WALL-DELAUNAY-DEFECT-BUDGET` is proved directly from finite Oler, saturation, Delaunay geometry, and Euler's formula. `C-UNIT-WALL-ONE-DEFICIT-DICHOTOMY` additionally depends on canonical `C-UNIT-WALL-LOW-SLACK-TRIANGULAR-CHART` in the one-addition branch.

**PASS — promote both exact claims.** Keep the bounded-face transfer conditional and preserve the diffuse-strain regression as a binding limit. The theorem makes no change to the canonical C-II source-move/payment obligation; C-II and Level I remain open.
