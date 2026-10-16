# Target C migration shard 2

## Frozen worklist and disposition

The worklist is reconstructed from source commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`: read `docs/state/artifact-index.jsonl`, keep `target == "target-c"` entries absent from the recursive destination tree at `358af8253f85ab7b9cdbf976ce186ee8426718e4`, then sort paths lexicographically. The complete backlog contains **813** paths. This shard owns zero-based indexes 163–325 inclusive (**163 reports**), from `docs/reports/target_c_cyclic_isostatic_body_bar_reduction_2026-09-09.md` through `docs/reports/target_c_fixed_star_common_witness_pairs_2026-10-01.md`.

All 163 same-path entries were absent from the frozen destination. All 163 source artifact-index entries say `unreviewed`, `canonical: false`, and have no claim IDs or manifest dependencies. Every owned report was imported byte-for-byte at its original path. **No report was excluded.** Related reports and intermediate proofs remain separate even when later work improves a bound or corrects only one implication.

## Full-content comparison

The disposition ledger records the SHA-256 and Git blob for every source file, the imported report SHA and byte count, report-declared dependencies, source lifecycle, result/scope and remaining-obligation excerpts, link targets, and verification boundary. It also records the closest full-body match in all **267** Markdown reports present at the frozen destination baseline.

The comparison removes the generated theorem-state comment, normalizes Unicode/case/whitespace for exact-body comparison, and compares sets of four-token shingles. Results: **0** normalized exact-body matches, **0** scores at or above 0.20, and a maximum Jaccard score of **0.03560467** (owned index 324 against `docs/reports/target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md`). The scan is a duplicate-screening aid, not a mathematical redundancy test. Per-file distinctions and successor scope are recorded in the ledger and highlights.

## Batch PRs

| Worklist indexes | Reports | PR | State |
|---|---:|---|---|
| 163–182 | 20 | [#37](https://github.com/1337isnot1337/erdos-99/pull/37) | Merged by the coordinator |
| 183–210 | 28 | [#45](https://github.com/1337isnot1337/erdos-99/pull/45) | Open |
| 211–238 | 28 | [#48](https://github.com/1337isnot1337/erdos-99/pull/48) | Open |
| 239–266 | 28 | [#51](https://github.com/1337isnot1337/erdos-99/pull/51) | Open |
| 267–283 and 286–297 | 29 | [#52](https://github.com/1337isnot1337/erdos-99/pull/52) | Open |
| 284–285 and 298–325 | 30 | [#61](https://github.com/1337isnot1337/erdos-99/pull/61) | Open |

PR #37 was already merged by the project coordinator. The remaining five PRs are reviewable and unmerged, as requested. PR #61 contains this consolidated ledger and shard closeout metadata.

## Ledgers and notes

- [`dispositions-163-325.jsonl`](dispositions-163-325.jsonl): complete per-file ledger for all 163 paths, including links to the owning PR and the source/destination content checks.
- [`mathematical-highlights.md`](mathematical-highlights.md): scoped summary of cyclic-body reductions, KKT/stress arguments, diameter response, endpoint constructions, corrections, and remaining obstructions.
- [`dependency-handoff.md`](dependency-handoff.md): cross-shard report links, shared verifier handoffs, and existing verifier files left unchanged.
- Each batch directory has its own `dispositions.jsonl`, receipt, and verification record; batches with unique code imports also have `supporting-code.jsonl`.

## Verification boundary and status

The imported verifiers were run where available; exact commands and finite counts are in the batch verification files. These checks cover exact arithmetic, stated finite configurations, or local regressions. They do not independently audit the full report proofs or establish the global-minimizer implication needed for Target C-II. No report lifecycle, theorem state, route, central artifact index, candidate registry, or release manifest was changed. The current destination theorem state remains **Level I open; C-I closed; C-II open**. The final public scanner result and its 11 cross-shard/coordinator integrity errors are itemized in [`verification-summary.md`](verification-summary.md).
