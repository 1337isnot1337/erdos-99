# Shard 2 verification summary

## Worklist and content

- Reconstructed backlog: **813** entries from frozen source/destination commits.
- Owned report paths: **163** (indexes 163–325), all same-path absent at the frozen destination baseline.
- Master-ledger audit: **163/163** source SHA-256 values match the frozen source blobs; **163/163** reviewable destination copies match those source blobs; all 163 source records remain `unreviewed`, noncanonical, and claim-free.
- Full destination-report scan: all **267** frozen-baseline report bodies read; zero exact normalized body matches and zero 4-token-shingle Jaccard scores at or above 0.20. Maximum score: 0.03560467.
- Every file is imported; there are no report exclusions.

## Relevant computation

- Existing q=13 S1 verifier for index 198: pass in a temporary Python 3.14.7 environment with SymPy 1.14.0 and mpmath 1.3.0; equilibrium residual `1.414e-15`, positive minimum stress, and positive inactive diameter slack. Finite local regression only.
- Four unique verifiers in indexes 211–238: pass, including 7,260 diameter-first exact states, 5,947 ball-hull thin-parabola pairs, 3,822 annular separation/diameter pairs, and local octagon-flip regressions. Ball-hull run used the same temporary SymPy environment.
- Two unique verifiers in indexes 239–266: exact EFAQ cap certificate over 1,000 rational bins and diameter-endpoint incidence/geometry audit pass.
- Three unique verifiers in indexes 267–283 and 286–297: harmonic rail checks, 164 exact gap-circulation packets with 8,492 cuts, and exclusive fan-port finite geometry checks pass.
- Two unique verifiers in indexes 284–285 and 298–325: face-following finite cap checks pass; exterior-cap population bounds pass with an exact temporary copy of the frozen shared helper. Existing destination five-arc threshold verifier also passes and was not changed.

All 11 imported verifier scripts were rerun. The two existing baseline verifiers were rerun. Python runtime was 3.14.7; this was not a registered Python 3.12 replay. Each batch’s detailed output and mathematical limits are in its `verification.md`.

## Repository checks

- Full final-PR diff and staged closeout metadata: `git diff --check` **PASS**. Batch 239–266 preserves two source reports with two terminal newline bytes; its unrestricted check flags only those source-authentic blank lines, while the check excluding those two files passes.
- `python3 tools/check_public.py`: **FAIL, 11 integrity errors**, with `mathematical_proof: false`. Counts were 94 certificates, 451 claims, 845 edges, 810 retained source files, and 23 tasks.

The 11 errors are:

1. The shared `verify_target_c_two_halfdisk_scalar_regression` helper imported by the exterior-cap verifier is missing; it is explicitly handed to the coordinator and is also referenced by outside-shard report index 28.
2. `target_c_complete_grid_collar_and_stress_shell_2026-10-02.md` links to `target_c_diameter_ball_hull_lattice_discrepancy_2026-10-02.md` (index 224, this shard’s open PR #48), `target_c_weak_pivot_axial_pressure_2026-10-02.md` (index 752, open shard 5 PR #56), `target_c_threshold_rail_deep_attachment_2026-10-02.md` (index 710, open shard 5 PR #55), and `target_c_weak_packet_correction_mass_2026-10-02.md` (index 751, open shard 5 PR #56). These are cross-PR links awaiting integration.
3. The face-following report at index 315 links to `target_c_oo_dual_tree_complete_rectangle_2026-10-01.md` (index 511, open shard 4 PR #36).
4. `target_c_connected_phase_core_collapse_2026-09-12.md` links to `target_c_phase_component_endpoint_closure_2026-09-12.md` (index 537, open shard 4 PR #39). Other current-main reports have unresolved references to `verify_aligned_swap_horn_obstructions.py`, `verify_convex_shared_witness_outer_occurrences.py`, and `verify_target_c_collinear_punctures_2026_10_02.py`; these are outside shard 2 and were not changed here.
5. The canonical generated `docs/state/artifact-index.jsonl` is stale for the new imports. The public checker suggests rebuilding it, but the user explicitly excludes that coordinator-owned file from this shard.

All named cross-shard report files are in other worker PRs or already merged; their exact indexes and PRs are in `dependency-handoff.md`. No theorem or publication status is claimed from this check.
