# Batch 211–238 verification

Frozen selection: source commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; destination missing-path comparison: `358af8253f85ab7b9cdbf976ce186ee8426718e4`.

## Import integrity

- Source blob and imported worktree bytes compared for all 28 reports and 4 unique verifier files: **PASS 32/32**. SHA-256 values match the per-file ledgers.
- All 267 destination report bodies at the frozen baseline were scanned for each report; no exact normalized body match was found. Per-report best matches and 4-token overlap scores are in `dispositions.jsonl`.
- `git diff --cached --check`: **PASS** after staging the batch.

## Imported evidence

- `python3 research/verify_target_c_deep_isolate_octagon_flip_2026_10_02.py`: **PASS**. Seven exact 13-point sources and three exact `Q(sqrt(3))` degree-five stars; the script explicitly gives no global-optimality certificate.
- The ball-hull verifier first stopped because system Python lacked SymPy. With temporary Python 3.14.7 environment `/tmp/e99-target-c-shard02-venv` and `sympy==1.14.0`, `research/verify_target_c_ball_hull_lattice_2026_10_02.py`: **PASS** (360 rational sources, 720 support margins, 5,947 thin-parabola pairs, exact symbolic/identity checks). The script explicitly gives no Fourier, global-optimality, positive-stress, train, or atlas-concentration certificate.
- `python3 research/verify_diameter_first_joint_depth_2026_10_02.py`: **PASS** (7,260 exact depth/interpolation states; 12 sharpness packets; 125 protected axial states).
- `python3 research/verify_target_c_annular_atlas_2026_09_26.py`: **PASS** (3,822 exact separation/diameter pairs, 378 exact sources, plus the stated finite normal-sector and atlas regressions). It explicitly gives no global-optimum or Level-I certificate.

The temporary SymPy environment is outside the repository. Python 3.14.7 is not a registered Python 3.12 replay.

## Mathematical review boundary

All reports and scripts remain research evidence; no theorem or lifecycle status is promoted. The D6 affine-window comparison and approximate-stability scripts are shared with other work and were not modified; see the shard-level coordinator handoff.
