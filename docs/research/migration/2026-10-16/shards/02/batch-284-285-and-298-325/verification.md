# Batch 284–285 and 298–325 verification

Frozen selection: source commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; destination missing-path comparison: `358af8253f85ab7b9cdbf976ce186ee8426718e4`.

## Import integrity

- Source blob and imported worktree bytes compared for all 30 reports and 2 unique verifiers: **PASS 32/32**. SHA-256 values match the per-file ledgers.
- The 267 frozen destination report bodies were scanned for every report. Indexes 284, 285, and 315 are in this same batch, preserving their local report chain.
- `git diff --check` will be recorded after staging; byte-preserving source reports are not normalized.

## Imported and existing evidence

- The exterior-cap verifier initially could not import `verify_target_c_two_halfdisk_scalar_regression`. This helper is a shared dependency used by an outside-shard report at backlog index 28, so it is not copied here. With an exact temporary copy of the helper from the frozen source commit on `PYTHONPATH`, `verify_exterior_cap_population.py`: **PASS**, all eight rational dimension/cardinality bounds.
- `python3 research/verify_target_c_face_following_cap_blockers_2026_10_01.py`: **PASS** (577 loaded-hull packets, 58 radical-enclosure packets, 2,040 binary colorings, 140,416 cyclic-host exemption packets, and 1,023 paired-gap trees). It explicitly makes no source-KKT, train-extraction, or global-optimality claim.
- Existing destination verifier `python3 research/target_c_five_arc_pin_threshold_check.py`: **PASS**; exact checks at 0.9604 and 0.961, plus the stated five-arc/three-arc margins. The script was not modified.
- Shared-helper SHA-256: `43bb8a6e3e90ca7b131d16cfff7a348bf54ddcd6c9de910d626430267274a0de`. The exact source commit and Git blob are recorded in `dependency-handoffs.jsonl` for the coordinator.

## Mathematical review boundary

The five-arc full-interval perimeter theorem remains conditional on actual occupancy of all five host components; the independent three-gap endpoint repair has a different and narrower conclusion. Extreme-stress circuit reports retain selected-support hypotheses and do not close the source-wide branch. The source report’s RSR strict-gap sentence is flagged against the exact equality-dependency audit; the RSR inequality-based threshold remains in scope. No claim is promoted.
