<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cf77d6e61f0fabe413242ecd15533e5e41d1223a", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/open_cell_staircase_finite_preservation_2026-10-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ec81b7e426ad59ead886875f9caf4afae0b2838617e36cbcecea9907802c3105"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Open-cell signed chains: finite certificate preservation

**Date:** 2026-10-15. **Base:** `d999528cfaafd811a4a19bcfacd00f217c2fc375`.
**State:** `2026-10-10.audit.234`. **Lifecycle:** unreviewed finite evidence;
the abstract finite census below is exact, with no canonical promotion.
Level I, A, B and C-II remain open.

## Source and exact finite statement

Source `audit/target-c-open-cell-finite-mechanics-20261005` at
`dad8485f18aaff02ea9b40ada95bca06b98682fc` contains a proposed historical
`audit.58` promotion. That transaction is not imported. Its analytic phase-flux,
sign-nesting/release and strong-SCC arguments already occur in the preserved
[phase-flux note](../../research/target_c_open_cell_phase_flux_2026-10-03.md),
[sign-nesting note](../../research/target_c_open_cell_sign_nesting_and_isolated_release_2026-10-04.md)
and [staircase note](../../research/target_c_open_cell_strong_scc_bidirected_staircase_2026-10-04.md).
These are unreviewed candidates, not canonical finite mechanics.

The unique source checker is now preserved at
`research/verify_target_c_open_cell_strong_staircase_2026_10_05.py`.
It exhausts this **abstract finite universe**: for each `1<=m<=5`, choose two
chains of nonempty integer intervals `[a,b]`, `0<=a<b<=m`, both starting
with `[0,m]` and then strictly nested. Add a positive directed edge `a->b`
for each interval in the first chain and a negative edge `b->a` for each
interval in the second. If the resulting graph is strongly connected, both
chains are identical and have lengths `m,m-1,...,1`.

| m | Chains per sign | Complete pairs | Strong pairs |
| --- | ---: | ---: | ---: |
| 1 | 1 | 1 | 1 |
| 2 | 3 | 9 | 2 |
| 3 | 10 | 100 | 4 |
| 4 | 34 | 1,156 | 8 |
| 5 | 116 | 13,456 | 16 |
| 6 | 396 | 156,816 | 32 |

The source checker covers the first five rows: 14,722 chain pairs and 31
strong pairs. A separate iterative-chain/bitset-transitive-closure implementation,
`research/verify_target_c_open_cell_chain_census_independent_2026_10_15.py`,
reconstructs those counts and adds the sixth row: 171,538 complete cases and
63 strong cases in total. It also accepts the common maximal staircase and
rejects it after removing the opposite full-support edge. No symmetry reduction,
random sampling, floating-point arithmetic or geometric realization is used.

## Reproduction and scope

```sh
python3 -I -B research/verify_target_c_open_cell_strong_staircase_2026_10_05.py
python3 -I -B research/verify_target_c_open_cell_chain_census_independent_2026_10_15.py
```

The source checker uses recursive interval-chain enumeration and two graph
traversals. Its added `-O` refusal prevents disabled assertions from producing
unchecked success. The independent checker uses explicit exceptions, iterative
enumeration and bitset transitive closure. Both use standard-library exact
integer operations. No theorem certificate is newly registered.

The finite statement is proved by complete enumeration of its stated domain.
The analytic all-`m` staircase claim remains unreviewed; extrapolation from six
rows is not a proof. Neither checker establishes that any canonical source has
a common-witness open cell, nested sign supports, or a strongly connected gap
graph. Neither supplies a full-source motion, diameter decrease or population
bound. Claims about physical diameter endpoints additionally need the actual
source realization and the exact hypotheses of `C-WOODALL`.

The former branch's proposed canonical labels and audit verdict do not resolve
those obligations. Its useful geometric candidates remain conveniently available
at the three predecessor paths above, without duplicating the 425-line proposed
promotion report or its overlapping audit.

## Bounded independent review and attribution

A finite reviewer can independently generate all nested chains through `m=6`,
check the directed endpoint convention and reproduce every count above. An
analytic reviewer should separately prove the all-size no-two-endpoint-trim and
first-divergence implications in the staircase note, with an explicit directed
cut at each step. A geometric reviewer must establish the common witness,
guard cone, sign nesting and source-layer hypotheses for a specified canonical
source; the finite census supplies none of them.

Original source authors remain recorded in the frozen source commit. OpenAI
Codex compared the predecessor notes, restored the checker, implemented the
separate finite census and ran both. This is AI-assisted preservation and exact
finite verification, not independent human peer review or a theorem promotion.
