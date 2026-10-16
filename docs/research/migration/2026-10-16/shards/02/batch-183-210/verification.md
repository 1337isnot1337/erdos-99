# Batch 183–210 verification

Frozen selection: source commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; destination missing-path comparison: `358af8253f85ab7b9cdbf976ce186ee8426718e4`.

## Import integrity

- Frozen source blob identity and SHA-256 checked for all 28 reports: **PASS 28/28**. Twenty-one destination reports are byte-identical; seven reports (indexes 184, 187, 188, 191, 193, 198, 210) contain only 18 exact `b\x0crac` → `b\\frac` repairs of source form-feed corruption in LaTeX. The shard reconciliation ledger records original source hashes, repaired destination hashes, and the transformation per report.
- Frozen destination same-path absence is recorded per report. The full-baseline scan read all 267 destination report bodies and found no exact normalized body match; the highest 4-token-shingle Jaccard in this batch was 0.0273884.
- `git diff --cached --check`: final PASS after all report and receipt edits were staged.

## Relevant evidence

- Initial command `python3 research/target_c_s1_q13_shell_regression.py` stopped at `ModuleNotFoundError: No module named 'sympy'`.
- Created an isolated temporary environment outside the repository with system site packages and installed `sympy==1.14.0` plus `mpmath==1.3.0`; reran `/tmp/erdos-e99-verification-venv/bin/python research/target_c_s1_q13_shell_regression.py`: **PASS**, exit 0.
- The regression reports q=13/m=11, 13 contacts, 12 diameter pairs, positive minimum stress coefficient `0.052831185547`, minimum inactive contact slack `0.771341203065`, minimum inactive diameter slack `0.072420120481`, equilibrium residual `1.435e-15`, and the expected spectrum with three numerical zero modes. This is a finite local regression, not a global-optimality proof.
- Runtime was Python 3.14.7. This is not a registered Python 3.12 replay.

## Repository integrity check

`python3 tools/check_public.py`: **BLOCKED** by its single reported integrity error, `artifact-index.jsonl is stale; run tools/build_artifact_index.py --write --write-headers` (94 certificates, 451 claims, 845 edges, 810 retained source files, 23 tasks). The central generated index and report headers are coordinator-owned and were not changed.

## Mathematical review boundary

All 28 source artifacts remain `unreviewed`, `canonical: false`, and non-promoted. The batch includes the source's own correction notes and the force-bulk warning at indexes 190/209/210. No independent theorem proof audit was performed by this migration.
