# Batch 267–283 and 286–297 verification

Frozen selection: source commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; destination missing-path comparison: `358af8253f85ab7b9cdbf976ce186ee8426718e4`. Worklist indexes 284–285 are intentionally held with index 315 in the next batch so their report links resolve together.

## Import integrity

- Source blob and imported worktree bytes compared for all 29 reports and 3 unique verifiers: **PASS 32/32**. SHA-256 values match the ledgers.
- Full-baseline comparison read all 267 destination report bodies per imported report; exact body matches and best shingle overlaps are in `dispositions.jsonl`.
- The relative-link review normalizes `..` before checking the frozen tree. The two frontier links from index 281 resolve to existing destination files; its missing reaction report and index 287’s four missing report links are recorded for coordinator handoff.
- `git diff --cached --check`: **PASS** after staging this batch.

## Imported evidence

- `python3 research/verify_harmonic_rail_endpoint_lift_2026_10_01.py`: **PASS** for exact square KKT/PSD and rail-width/moment checks; finite specified hypotheses only.
- `python3 research/verify_exact_phase_gap_circulation_2026_10_01.py`: **PASS**, 164 exact positive-circulation packets and 8,492 proper cuts, plus the rational diameter-star checks. Its scope excludes contact/train embedding and global optimality.
- `python3 research/verify_target_c_exclusive_fan_ports_2026_10_03.py`: **PASS** for the listed exact finite geometry and arithmetic checks, including five exact fan/pentagon sources. Packets are nonglobal and nonharmonic.

## Mathematical review boundary

The exact-phase, support-cap, and exterior-train results retain their inactive-blocker and global-closure limits. Shared ordered-gap-circulation and star-ray verifiers were not modified; see coordinator handoff. All reports remain unreviewed/noncanonical.
