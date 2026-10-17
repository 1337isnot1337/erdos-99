> Generated reading edition · [exact source](../../research/target_c_support6_collapsed_coarse_mod2_regression_hostile_audit_2026-09-19.md) · source SHA-256 `5e73ff8d70866401411cda4eb7e447dba18753e75263067ae1dd29fdfe968b37`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "df1587e19ab6b8ae00d75775405523dca3dd2917", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_coarse_mod2_regression_hostile_audit_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b1c7e5925a2f9ce9d601968565b92573ced9e893f6576ba09ea854b1ec5181cd"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — coarse collapsed support-six mod-2 regression

**Date:** 2026-09-19  
**Audited note:** `research/target_c_support6_collapsed_coarse_mod2_regression_2026-09-19.md`  
**Certificate:** `research/verify_target_c_support6_collapsed_coarse_mod2_2026_09_19.cpp`  
**Disposition:** PASS as an exact negative regression; theorem-state authority unchanged; C-II remains open.

## 1. The direction of the implication is correct

The verifier deliberately over-relaxes each coarse rotation cell. A train-pair crossing variable is forced to zero only when neither strict crossing window

```math
1<x_e-x_f<2,
\qquad
1<x_f-x_e<2
```

intersects the base rational angle cell. If either window intersects, the crossing bit remains completely free.

This can admit binary crossing assignments that no single angle vector realizes simultaneously. Therefore:

- inconsistency of the relaxed MI.1 system would exclude the whole rotation cell;
- consistency of the relaxed system does **not** prove any realization.

The source note states only the second, negative conclusion: the coarse parity shortcut cannot close support six.

## 2. The crossing-window test is exact

The base 388 cells are strict integer-difference systems after the scaling `x=3 alpha/pi`. Adding either crossing orientation adds exactly two further strict integer-difference inequalities. The imported rotation-cell verifier uses its exact transformed-cycle Bellman--Ford test; no floating-point threshold comparison is introduced.

Pairs on or near the walls `|x_e-x_f|=1,2` do not cause a soundness problem. The question asked is only whether the open crossing window intersects the open base cell. If it does, the variable is left free. Boundary-only contact does not create a strict-rhombus crossing and therefore never needs to be forced to one.

## 3. The MI.1 equation set is complete at the claimed scope

The verifier enumerates every simple cycle of `K_6\setminus M`, then every unordered edge-disjoint cycle pair. Only those pairs are used, matching the scope of the audited MI.1 theorem.

The right-hand side is computed from the actual four-edge rotation at each common exceptional face. For an edge-disjoint cycle pair, a common face contributes exactly when the two endpoints of one cycle separate the two endpoints of the other in that cyclic order.

On the left, every train-pair crossing bit is retained, including pairs whose trains share an exceptional endpoint. This matches the hostile audit of MI.1 and avoids the invalid good-drawing simplification.

## 4. The binary elimination is exact

There are 66 unordered pairs of twelve relation trains. The verifier forms one augmented bit row per cycle-pair equation and performs Gaussian elimination with `std::bitset<67>` using XOR only. Thus the reported ranks and consistency decisions are exact over `F_2`.

The locally reproduced output was

```text
all-cross matching: cells=180, coarse-parity-inconsistent=0, allowed-vars=30..34, rank=16..16, affine-dim=14..18
all-cross matching: affine-dim histogram 14:24 15:12 16:24 17:96 18:24
mixed matching: cells=208, coarse-parity-inconsistent=0, allowed-vars=30..35, rank=16..16, affine-dim=14..19
mixed matching: affine-dim histogram 14:8 15:24 16:56 17:64 18:32 19:24
PASS: coarse MI.1 parity is consistent on all 388 rotation cells; crossing-wall subdivision is necessary.
```

The certificate was compiled with `g++ -O3 -std=c++17 -Wall -Wextra -pedantic` and completed without assertion failure.

## 5. What the constant rank does not prove

Rank 16 appears for every one of the 388 relaxed systems. The note correctly records this only as an exact finite observation. It does not infer a universal homology theorem or use the value 16 downstream.

## 6. Relation to the two certified global exclusions

There is no conflict with either certified collapsed root-box exclusion. Those proofs know which side of specific crossing thresholds their tiny parameter boxes occupy. The present relaxation forgets that information by freeing a crossing variable whenever its crossing window occurs anywhere in the much larger rotation cell. A parity contradiction can therefore disappear under the relaxation.

This confirms rather than weakens the value of the MI.1 theorem: threshold information is load-bearing.

## 7. Remaining obligation

A complete finite attack should refine the 42 symmetry representatives along crossing-threshold walls before applying MI.1. The number of raw sign patterns should not be assumed to be `3^66`; most pairwise threshold states are ruled out by the shared difference constraints. Exact cell enumeration should use the same difference-constraint machinery and symmetry quotient, with MI.1 inconsistency applied during search to prune cells early.

**Audit disposition:** PASS. Every one of the 388 coarse rational rotation cells admits a solution to the intentionally relaxed MI.1 crossing system. This is a rigorous regression against discarding the crossing-threshold subdivision, not evidence of a globally realizable collapsed block.
