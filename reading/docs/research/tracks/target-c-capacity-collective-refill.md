> Generated reading edition · [exact source](../../../../docs/research/tracks/target-c-capacity-collective-refill.md) · source SHA-256 `959cfeb1c2a6901d53943fccef83f98f4dfd876ce43ccf60b76601bc106dfcd9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C vacancy, wall capacity, and collective refill

**Lifecycle:** research-only. The eight reports below are unreviewed in the
destination artifact index; this track does not promote them or change the
theorem-state manifest. C-II and Level I remain open.

**Frozen source:** `e-99` branch
`research/sol/target-c-level1-gpt61-2026-10-04`, head
`9875cd6a77939bb6347353fc798ab8f9ab03ec3e`, tree
`198c83065add8175a921b4e9c55169e4690010a3`. Its merge base with frozen
source main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73` is
`0351e2c529e01750f7aceb87f8f6f0cb9c21dea7`. The [branch file ledger](../../../../docs/research/migration/2026-10-16/ledger/source-branch-files.jsonl)
records all 19 branch-delta paths, exact hashes, and their destination treatment.

## What the route establishes

### Vacancies and actual unit walls

- [One-vacancy collective strictification](../../reports/target_c_one_vacancy_collective_strictification_2026-10-05.md)
  moves every remaining interior label in two exact stages while fixing the
  wall and all labels. A source that starts with one vacancy has strict
  capacity `K-1`; this is a container-capacity result, not a global-minimizer
  example.
- [Vacancy-funded actual unit-wall activation](../../reports/target_c_vacancy_funded_unit_wall_activation_2026-10-05.md)
  uses contact minimality to force at least `K` enclosed labels behind the
  stated strict-oblique actual wall. Its triangular two-vacancy limit gives
  strict capacity `K-2` under the stated fixed-frame tolerance. The report
  does not extract such a complete wall or vacancy from every canonical
  source.
- [Two-boundary-pin refill](../../reports/target_c_boundary_vacancy_funded_collective_refill_2026-10-05.md)
  releases all `K` reference interior positions after deleting two adjacent
  wall labels in a sufficiently close triangular frame. Exact shielding
  handles every retained exterior point. The finite packets do not certify
  global optimality or a tolerance uniform in growing frame size.

### Oblique capacity thresholds

- [Two-side polynomial refill](../../reports/target_c_two_side_polynomial_collective_refill_2026-10-05.md)
  treats angles from 60 to 90 degrees. Opening the lower and left sides
  removes `J=m+n-1` labels and moves all `K=(m-1)(n-1)` interior labels
  simultaneously with squared gap `3/(250000*(m+n)^14)` and stated wall
  tolerance `gap/[4*(m+n+1)]`. Applying it requires an actual wall within
  tolerance and a population deficit of at least `J`.
- [One-pin oblique refill](../../reports/target_c_one_boundary_pin_oblique_refill_2026-10-05.md)
  removes only wall label `(1,0)` for `60°<phi<=90°`. With
  `delta=1-2*cos(phi)` and `L=m+n`, its explicit squared gap is
  `delta^4/(25000000000000*L^20)`. This removes the linear boundary charge
  for the stated frame, but the gap degenerates at the triangular endpoint
  and the source still needs an actual captured wall.
- [Triangular two-pin capacity](../../reports/target_c_triangular_two_pin_strict_capacity_2026-10-05.md)
  gives exact capacity `K` for triangular `3-by-n` frames and the triangular
  `4-by-4` square. It blocks a universal upgrade to `K+1`; it does not give
  an upper bound when both side lengths grow.

### Collective pentagon obstruction and multishear energy

- [Universal unit-pentagon capacity](../../reports/target_c_unit_pentagon_perimeter_capacity_2026-10-05.md)
  proves that a strictly convex unit pentagon with mutually unit-separated
  vertices has no additional unit-separated point in its closed container.
  After `d>=1` deletions, at most `d-1` interior replacements fit. For a
  vertex-disjoint bank of such walls, individual interiors cannot fund all
  deleted labels. Releasing wall constraints or using a larger collective
  region remains necessary.
- [Exact multishear traffic domination](../../reports/target_c_multishear_traffic_domination_2026-10-05.md)
  proves `W=diag(A)-B=R^T*Omega*R >= 0` for its stated canonical PSD stress
  and actual outer-train cuts, with kernel dimension
  `2-rank(span{unselected contact directions})`. This yields finite
  weighted mean-diameter-square loss and exact one-cut lower/upper feasibility
  quadratics. It does not produce a common maximum-diameter contraction or a
  global competitor.

## Required next bridge

The local results do not by themselves contradict global minimality. A valid
continuation must extract an actual wall or vacancy from every relevant
canonical source, pay the full population change, retain every source label,
check every lower pair and every actual or inactive diameter upper pair, and
produce either a strict same-cardinality sub-`D` competitor or an admissible
triangle-free endpoint at `D` with fewer contacts or actual diameter pairs.
The individual pentagon obstruction and triangular capacity regressions must
be used as countertests to any proposed refill implication. Mean traffic loss
cannot substitute for controlling the maximum diameter. No rate or chart
claim invalidated by the destination's inverse-phase correction is restored.

The machine-readable claims, dependencies, exact verifier commands, and
remaining obligations are in the [candidate registry](../../../../docs/targets/target-c/candidate-registry.json).
All eight scripts are available in `research/verify_target_c_*_2026_10_05.py`;
the six scripts that existed before this batch are byte-identical to the
frozen branch, and all eight passed on the integration tree. See the
[verification receipt](../../../../docs/research/migration/2026-10-16/receipts/source-branch-capacity-refill.json).

## Provenance treatment

Five report files and five verifier files were exact destination duplicates;
the three missing reports and three missing verifiers were imported byte for
byte. The source branch's generated artifact index was rebuilt from the
destination report headers. Its `research/README.md` and run synthesis were
not copied over curated destination navigation: their mathematical additions
are captured here and in the candidate registry, while their pre-existing
full proofs remain linked at their original report paths. One
conversation-specific closing line in the source synthesis was omitted.
