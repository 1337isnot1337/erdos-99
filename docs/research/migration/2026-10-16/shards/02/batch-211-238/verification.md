# Batch 211–238 verification

Frozen selection: source commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; destination missing-path comparison: `358af8253f85ab7b9cdbf976ce186ee8426718e4`.

## Import integrity

- Source blob and imported worktree bytes compared for all 28 reports and 4 unique verifier files: **PASS 32/32**. SHA-256 values match the per-file ledgers.
- All 267 destination report bodies at the frozen baseline were scanned for each report; no exact normalized body match was found. Per-report best matches and 4-token overlap scores are in `dispositions.jsonl`.
- `git diff --cached --check`: **PASS** after staging the batch.

## Cross-shard link and independent replay

- Shard-1 index 83, `docs/reports/target_c_complete_grid_collar_and_stress_shell_2026-10-02.md`, contains a relative link to the ball-hull report imported by this batch. The source report blob/SHA-256 is `17878daf0aab59b72fbfcdbc0c010de99e5cb2b1` / `12d7a99aad408105f0e7f855b560b10d5a383dbcd55dada35f199107aa3566ee`; the target was absent at current main `dfac17ac` and is present byte-identically on this PR head. Merging the batch into current main resolves the link.
- Independently reran `/tmp/erdos-e99-verification-venv/bin/python research/verify_target_c_ball_hull_lattice_2026_10_02.py` under Python 3.14.7, SymPy 1.14.0, and mpmath 1.3.0: **PASS** with 360 rational source pairs, 720 exact support margins, 48 midpoint bounds, 48 rounded representatives, 5,947 thin-parabola pairs, 24 complete difference-alphabet checks, 72 three-port polynomials (12 identities and 60 exact triangular centers), 20 rational leaf-location bounds, 12 rational one-port pairs, and 18 algebraic two-port sources with 108 exact pair identities. The verifier explicitly does not certify the analytic Fourier/Poisson argument, positive stress, global optimality, train, or atlas concentration.

## Imported evidence

- `python3 research/verify_target_c_deep_isolate_octagon_flip_2026_10_02.py`: **PASS**. Seven exact 13-point sources and three exact `Q(sqrt(3))` degree-five stars; the script explicitly gives no global-optimality certificate.
- The ball-hull verifier first stopped because system Python lacked SymPy. With temporary Python 3.14.7 environment `/tmp/e99-target-c-shard02-venv` and `sympy==1.14.0`, `research/verify_target_c_ball_hull_lattice_2026_10_02.py`: **PASS** (360 rational sources, 720 support margins, 5,947 thin-parabola pairs, exact symbolic/identity checks). The script explicitly gives no Fourier, global-optimality, positive-stress, train, or atlas-concentration certificate.
- `python3 research/verify_diameter_first_joint_depth_2026_10_02.py`: **PASS** (7,260 exact depth/interpolation states; 12 sharpness packets; 125 protected axial states).
- `python3 research/verify_target_c_annular_atlas_2026_09_26.py`: **PASS** (3,822 exact separation/diameter pairs, 378 exact sources, plus the stated finite normal-sector and atlas regressions). It explicitly gives no global-optimum or Level-I certificate.

The temporary SymPy environment is outside the repository. Python 3.14.7 is not a registered Python 3.12 replay.

## Mathematical review boundary

All reports and scripts remain research evidence; no theorem or lifecycle status is promoted. The D6 affine-window comparison and approximate-stability scripts are shared with other work and were not modified; see the shard-level coordinator handoff.
