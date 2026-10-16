# Global planar endpoint routes: colour lifts and finite palettes

**Frozen source:** main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; open draft PR
#958 head `0a72556e786024c9313c7d6287e26c20c1e9b9b8` (tree
`7b37e2fc5af3bb2e0471a690195a21f9d9fd0d2c`), merge base
`d6f953100d62a84de72e991642041fdd026e82ba` (tree
`3d6ac96556b891d7b17ea7c13ae9364e0c5082f0`).

**Status:** level-I research only. Every analytic claim remains unreviewed and
outside the theorem-state manifest. The finite examples are nonglobal
regressions or controls. Nothing in this track closes Level I or C-II.

The full arguments are in the [colour-lift report](../../reports/global_colouring_lift_and_planar_rank_barrier_2026-10-12.md)
and the [palette-endpoint report](../../reports/global_palette_endpoints_and_full_source_exhaustion_2026-10-12.md).
The source AI audit is retained as [provenance](../../audits/pr958_autonomous_proof_audit_2026-10-15.md),
not as the destination's independent exact-head promotion review. Source hashes,
transformations, dependencies, and per-file dispositions are in the
[PR #958 migration ledger](../migration/2026-10-16/ledger/source-pr-files.jsonl).

## Relation to the queued PR #960 rank barrier

The uniform squared-distance interpolation and rank-\(n-1\) obstruction are
the same claim as the first section of source PR #960's
global_planarity_and_radius_barriers_2026-10-12.md, after setting
\(t=1-\lambda\). Do not count them as independent results. PR #960 adds a
rank-two-truncation analysis and separate enclosing-radius / finite
replacement results. By contrast, the contact-colour lift, its affine
flattening criterion, the all-pair endpoint quadratics, and the finite
palette regressions in this track add distinct material.

## Route map

| Result | Exact scope | Missing implication |
| --- | --- | --- |
| Uniform distance interpolation | For any finite unit-separated set with diameter `D>1`, `d'²=1+λ(d²-1)` preserves every unit contact and strictly reduces diameter for `0<λ<1`. The centered Gram matrix is `λG+(1-λ)J/2`; its rank is `n-1`. | For `n>=4`, the resulting metric has no planar realization. A metric improvement is not a planar competitor. |
| Proper-contact-colour lift | The contact graph of a triangle-free penny graph is 2-degenerate, so it has a proper colouring with at most three colours, including isolates. The lifted source gives a full-label, contact-preserving strict diameter decrease in `R^4`. | The new point set is generally not planar. The square control has lift rank three. No planar competitor follows for a general source. |
| Affine-colour flattening criterion | The lift remains planar exactly when the centered colour vectors lie in the centered source plane. With two nonempty colours this means two parallel colour lines; with three colours and `n>=4` it is impossible. | No affine colouring of a general triangle-free global minimizer is constructed. This condition characterizes flattening of this lift, not arbitrary planar rearrangements. |
| Full-pair endpoint inequalities | For prescribed planar targets `v_i` and common `t`, exact lower and strict upper constraints reduce to the two report's quadratics for every pair. A feasible endpoint can cross an infeasible intermediate configuration. | No target configuration is supplied for every sufficiently large triangle-free global minimizer. No path or local-flex premise repairs this quantifier. |
| Palette independent transversal | For finite palettes, selecting one position per label while satisfying every `1<=d<D` constraint is exactly an independent transversal in the complete lower/upper conflict graph. Sufficient SAT gives a valid endpoint; permissive UNSAT excludes every choice in that one palette. | No universal palette or transversal theorem is proved for global minimizers. |

## The finite palette controls

For the regular unit 43-gon, set

`R=1/(2 sin(π/43))`, `D=1/(2 sin(π/86))`, and `α=17/20`. The three translation
vectors are `(1,0)`, `(-1/2,√3/2)`, and `(-1/2,-√3/2)`. An exact search found a
43-label planar endpoint in 13 nodes and checked all 903 pairs, with squared
minimum distance `>1.01` and endpoint squared diameter `<185` while the old
source has `D²>187.4262`. This is a strict competitor for that finite source,
which is already nonglobal; it is not evidence of a global minimizer.

The source audit then adds 132 strictly interior isolates to this rim. For the
same three translations and `α`, the permissive full-source system has 2,039
constrained label pairs and is unsatisfiable after four exhaustive branches,
covering all `3^175` assignments for that exact palette. An independent
175-label unit-separated packet checks all 15,225 pairs and has `D²<183.2352`.
Thus the filled source is also strictly nonglobal, and improvement of a loaded
rim does not imply a compatible choice for the complete source.

These are method-level controls. The full-source palette failure is specific to
one parameter and one palette; it does not exclude other palettes or arbitrary
planar endpoints. The finite exhaustive search is not a universal contradiction.

## External fixture rights and reproducibility

The 132- and 175-label coordinate tables come from the external Packomania URLs
and have expected SHA-256 values in the destination's
[provenance record](../../../research/fixtures/global_palette_translation_2026_10_12/provenance.json).
The migration retains those URLs, hashes, and the first-party verifier, but not
the coordinate tables. The source audit says redistribution clearance was
unresolved; the Packomania [homepage](https://www.packomania.com/) and
[submission-format page](https://www.packomania.com/hints.html) inspected for
this migration did not provide an explicit redistribution grant. The two
source files therefore have explicit rights-blocked rows in the migration
ledger.

Run the palette verifier with --core-only to reproduce the 43-gon endpoint without external tables. If authorized to use the external data, place files named
`cci132.txt` and `cci175.txt` in a directory and run:

```sh
python3 research/verify_global_palette_transversal_2026_10_12.py \
  --fixture-dir <local-authorized-data-directory>
```

The checker compares both files to the retained hashes before parsing. The
colour-lift verifier needs no external fixtures:

```sh
python3 research/verify_global_colouring_lift_rank_2026_10_12.py
```

The source verifier audit reports 4,096 Boolean-system controls, four original
geometric controls, and a proof replay that does not invoke search. Destination
reproduction of the 175-label geometric system still requires the external
tables; the current local receipt records that limit rather than claiming the
data-dependent replay.

## Continue from the exact gap

The remaining Level-I route is either:

1. construct an actual planar strict-diameter endpoint for every sufficiently
   large triangle-free global minimizer, retaining every label and every lower
   and upper pair; or
2. produce an unbounded family of triangle-free configurations with an
   independently proved global-minimality property.

The colour lift settles neither planar realization nor source extraction. The
finite palette method validates particular endpoint choices, while its
full-source regression blocks a fixed three-translation shortcut. Any
continuation must use an endpoint or global contradiction, not dimension-free
metric relaxation or a nonglobal finite screen. Related source PR #960 rank and
planarity barriers are a separate route and must be reconciled by mathematical
scope if that batch is integrated; neither result is silently substituted for
the claims here.
