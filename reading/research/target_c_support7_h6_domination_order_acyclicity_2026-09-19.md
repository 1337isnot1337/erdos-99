> Generated reading edition · [exact source](../../research/target_c_support7_h6_domination_order_acyclicity_2026-09-19.md) · source SHA-256 `21e95dac8500d19896e28f25b74a0281d02a7897ba096ffc393af005025d4f65`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6f7406eed6e34bf5d1934ba0a014c538dff1fcfb", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h6_domination_order_acyclicity_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "50352fcc2f86fe9ecf0c23e6451afd2b4364918098ad162ff10696dcd36693e5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C support-seven H6: domination branches are order-acyclic by themselves

Date: 2026-09-19

Status: exact structural statement inside the generic-H6 metric-order layer. The theorem-state authority is unchanged. C-II remains open.

## Result

The fourteen all-root interior-domination disjunctions do not, by themselves, create a contradiction in the common `L(K8)` segment-order system. In fact every one of their `2^14 = 16384` branch products has the same explicit scalar length realization at the order level.

For an unordered reciprocal segment `e`, let

```math
\delta(e)=|e\cap\{6,7\}|,
```

so a hull-hull segment has level `0`, a hull-interior segment has level `1`, and the interior-interior segment `67` has level `2`.

A domination branch for root `r`, interior target `t`, and one chosen bracketing hull endpoint `h` is

```math
|y_t-y_r|<|y_h-y_r|.
```

If `r` is a hull vertex, the target segment `rt` is hull-interior while `rh` is hull-hull, hence

```math
\delta(rt)=1,\qquad \delta(rh)=0.
```

If `r` is the other interior vertex, the target segment is `67` while `rh` is hull-interior, hence

```math
\delta(rt)=2,\qquad \delta(rh)=1.
```

Thus every selected strict comparison decreases `delta` by exactly one when oriented from the shorter target segment toward the longer chosen endpoint. A directed cycle made only of domination-branch comparisons is therefore impossible.

There is an explicit common order realization for every possible branch atom, not just an acyclicity argument. Assign

```text
interior-interior segment : 1
hull-interior segment     : 2
hull-hull segment         : 3
```

Every possible domination branch is then either `1 < 2` or `2 < 3`. Consequently the same assignment satisfies every possible choice of one branch from each of the fourteen disjunctions.

## Consequence for the closure search

The domination theorem is still useful when intersected with the 85-variable complete-angle affine system, because the affine angle equations can force additional segment comparisons or make a branch polyhedron empty. What this result rules out is a weaker strategy: branch on the fourteen domination clauses and expect the selected branch edges alone to produce a directed cycle in `L(K8)`.

Any `L(K8)` cycle contradiction at this layer must use at least one comparison not supplied solely by the chosen domination branches, for example a comparison forced independently by the complete-angle affine cell. Likewise, any exclusion obtained by the full domination branch-and-bound must come from interaction with the affine equations and strict facets, not from an intrinsic inconsistency among the fourteen distance-order clauses.

This justifies the full exact affine branch-and-bound verifier `verify_target_c_support7_h6_all_root_domination_full_bnb_2026_09_19.py`: its LP/Farkas layer is essential. A pure combinatorial enumeration of the `2^14` domination choices cannot remove a cell.

## Verification

`research/verify_target_c_support7_h6_domination_order_acyclicity_2026_09_19.py` checks every possible atomic root/target/hull-endpoint comparison, verifies the only level transitions are `2 -> 1` and `1 -> 0`, and checks the universal three-level scalar assignment. The proof itself is the level argument above; no floating-point arithmetic is involved.
