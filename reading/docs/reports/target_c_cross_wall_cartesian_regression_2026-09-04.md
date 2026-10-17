> Generated reading edition · [exact source](../../../docs/reports/target_c_cross_wall_cartesian_regression_2026-09-04.md) · source SHA-256 `5d5b619ad44e8fc7c93d5d1ef884fec16a04a0f2b8588f64769208b282eca4ba`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-380B5A24DF16","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cross-wall Cartesian regression

**Date:** 2026-09-04  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Status:** regression; downstream claims retracted

## Error

The reports beginning with `target_c_cross_wall_cartesian_capacity_2026-09-04.md` treated long residual trains from the two different C90 boundary sides `L` and `U` as one Cartesian translation stack over a common interval of exact chain trains.

The graph-theoretic premise is true: two long residual rows share an exact chain train, so C77 triangle-freeness implies that they do not cross each other. The conclusion used afterward is not justified. The C91 Cartesian rectangle construction is a one-side wall construction. Trains whose terminals lie on `L` and trains whose terminals lie on `U` sit on opposite sides of the literal `z`--`a` chain. Pairwise noncrossing plus a common set of crossed chain trains does not by itself provide four source vertices

`p, p+U, p+V, p+U+V`

with one residual displacement `V` equal to the signed sum of both side families.

Equivalently, the two opposite-side walls may each translate a chain segment outward on their own side, but they cannot be concatenated into one train-coordinate rectangle without an additional realization lemma. No such lemma is present in C77, C80, C90, or C91.

Therefore the cross-wall profile inequality

`[f(t)+g(t)-1]_+^2+3t^2<=1`

and every numerical theorem derived from it are not established.

## Retracted branch reports

The following reports were deleted from the research branch because their main theorems depend on that unsupported cross-side Cartesian block:

- `target_c_cross_wall_cartesian_capacity_2026-09-04.md` (`T/D>2.926`);
- `target_c_full_row_cross_wall_capacity_2026-09-04.md` (`T/D>2.938`);
- `target_c_phase_orbit_bad_mass_capacity_2026-09-04.md` (`T/D>2.948`);
- `target_c_quintic_cross_wall_capacity_2026-09-04.md` (`T/D>2.95`);
- `target_c_side_local_phase_capacity_2026-09-04.md` (`T/D>2.9524`);
- `target_c_septic_cross_wall_capacity_2026-09-04.md` (`T/D>2.9527`).

Their Git history remains available, but none of those constants should be cited.

## What survives

Three ingredients used during that route survive independently:

1. **Same-side mixed wall.** After deleting rows of length at most `D/2`, any two residual trains on the same boundary side share a chain train, hence are noncrossing; their intervals are nested. C77 orientation gives a common transverse sign and magnitude greater than `sqrt(3)/2`. Thus one side wall of `lambda D` long rows has the valid profile
   
   `G(lambda)=integral_0^lambda sqrt(1-3t^2/4) dt`.

2. **Opposite-side noncrossing.** A non-chain train with both terminals on `L` cannot cross one with both terminals on `U`: their boundary endpoints do not alternate, so intersection parity is even, while C77 allows at most one crossing.

3. **Phase-orbit bookkeeping.** The limiting crossing relation still decomposes into three-point projective `60-degree` phase orbits. This can be combined with the two one-side wall capacities, but not with a fictitious cross-side rectangle.

The next quantitative theorem must optimize these valid one-side capacities separately.
