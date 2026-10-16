# Batch 239–266 verification

Frozen selection: source commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; destination missing-path comparison: `358af8253f85ab7b9cdbf976ce186ee8426718e4`.

## Import integrity

- Source blob and imported worktree bytes compared for all 28 reports and 2 unique verifiers: **PASS 30/30**. SHA-256 values match the per-file ledgers.
- The full 267-report destination baseline corpus was scanned for each imported report; exact body duplicates and high-overlap candidates are recorded per report.
- `git diff --cached --check` on the whole batch exits 2 for two source files that already end with two newline bytes: `target_c_endpoint_outer_walk_geodesic_collapse_mu4_2026-09-12.md` and `target_c_endpoint_train_end_balance_2026-09-12.md`. Their source and imported bytes match exactly, so the original whitespace is preserved. Excluding those two source files, `git diff --cached --check`: **PASS** (exit 0).

## Imported evidence

- `python3 research/target_c_efaq_uniform_cap.py`: **CERTIFIED**, 1,000 rational bins; exact maximum upper numerator `3009480763847760179` over denominator `10^18`, below `3.01` by exact rational margin `519236152239821/10^18`.
- `python3 research/diameter_endpoint_gap_audit.py`: **PASS**, 1,950 exact ordered K4 incidence checks plus the listed finite crossing, two-arc, shell, and gap-simplex checks. Its output expressly does not certify global optimality or solve Erdős #99.

## Mathematical review boundary

All source claims remain unreviewed/noncanonical. ENS remains a valid independent proof with its exact rational EFAQ cap, while its scalar floor is numerically improved by the explicitly named BVP/BAS chain and the later generic AAS floor; RCC is a separate conditional small-response result. The batch also retains the exact endpoint repair and the corrected perimeter-squeeze scope. None of these imports or finite verifiers is treated as a Target C closure.
