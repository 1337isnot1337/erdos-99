# Target C: exact primal audit of the depth-one all-root domination filter

The 3,874-cell generic-H6 endpoint survives every individual all-root interior-domination disjunction at the complete-angle affine level.

For each endpoint cell and each of the fourteen root-target pairs `(r,t)` with `t in {6,7}` and `r != t`, the verifier
`verify_target_c_support7_h6_all_root_domination_depth1_primal_2026_09_19.py`
found at least one of the two closed domination branches containing an exact rational point that satisfies the full 85-variable affine system, every original strict facet, and the added closed domination facet.

This gives 54,236 exact pair witnesses:

- endpoint cells checked: 3,874 / 3,874;
- root-target pairs certified: 54,236 / 54,236;
- unresolved cells: 0;
- exact-primal reconstruction failures: 0;
- branch LPs attempted: 55,112;
- numerical-live branches used for exact reconstruction: 54,236;
- coordinate reconstruction limit 1,000: 54,152 witnesses;
- coordinate reconstruction limit 10,000: 84 witnesses;
- largest coordinate denominator in any accepted witness: 2,220;
- smallest positive strict-facet slack among accepted witnesses: `1/1410`;
- accepted witnesses lying on at least one added closed domination equality: 2,828.

The eight deterministic partitions were the intervals
`[0,484)`, `[484,968)`, `[968,1452)`, `[1452,1937)`,
`[1937,2421)`, `[2421,2905)`, `[2905,3389)`, and `[3389,3874)`
in the frozen endpoint ledger. Every partition reported `unresolved_cells = 0`.

## Consequence

No single root-target domination disjunction can remove any of the 3,874 endpoint cells from the complete-angle affine relaxation. The earlier depth-one Farkas filter therefore cannot lower the current endpoint, even with exact primal feasibility replacing a merely numerical "live" branch.

This does **not** produce one point satisfying all fourteen disjunctions simultaneously. The witness may depend on `(r,t)`. Coupled branch-and-bound remains open and is the next relevant test. It also does not establish a Euclidean realization of any endpoint cell; metric integrability and the remaining nonlinear geometry are not imposed here.

The first coupled layer worth testing is the six same-root pairs for roots `r=0,...,5`: require one target-6 branch and one target-7 branch simultaneously. A cell is excluded at that layer only if all four branch combinations admit exact rational Farkas contradictions. The companion depth-two verifier implements precisely this conservative test.

## Audit source

The aggregate above was reconstructed from all eight successful artifacts of GitHub Actions run `35485395305` at commit `049daea17931e18e681bed3e4c28c86cd962ab21`. The run's separate summary job failed to start, but every scan partition completed successfully and uploaded its JSON ledger. The aggregate was recomputed directly from those eight ledgers; no mathematical claim depends on the failed summary job.
