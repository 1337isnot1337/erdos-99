> Generated reading edition · [exact source](../../research/target_c_support7_h7b_full_angle_verifier_repair_2026-09-19.md) · source SHA-256 `cb7eb7e3e6a874deb450867ef0016f9dff823c8bd91d5651fa1b9a91e8f4b8ee`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "06a8ab6fe172ce9843eb65e9baa3327c41f69fd7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h7b_full_angle_verifier_repair_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "94aa1670882ec1a7c674edc76a7c814cd775f0b507a0c7fedf4d2663c50298ba"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — repair and independent recertification of the generic H7b full-angle reduction

**Date:** 2026-09-19  
**Scope:** generic interior-ground `H7b` full-angle affine reduction  
**Historical claim:** `184 -> 27`, with all 27 survivors of missing-graph type `C7`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

## 1. A real executable defect was present

The committed verifier

`verify_target_c_support7_h7b_full_angle_reduction_2026_09_19.py`

contains one dispatch error in `build_system`. It first constructs a dictionary of the five-edge signed force cycles,

```python
cyc={i:force_cycle(i,m,ks,sd) for i in N}
```

but then calls

```python
raw_force_angle(cyc,i,a,b,sd,po)
```

instead of

```python
raw_force_angle(cyc[i],i,a,b,sd,po)
```

`raw_force_angle` passes its first argument to `force_arc`, which calls `.index(...)`. A dictionary has no `.index`, so the historical file is not executable as committed. The preceding audit therefore overstated the validation status when it described that exact file as having passed.

The new shim

`verify_target_c_support7_h7b_full_angle_reduction_repaired_2026_09_19.py`

asserts that this exact defect occurs once, replaces only that occurrence in memory, and executes the otherwise unchanged historical verifier. It deliberately does not duplicate the large certificate table.

## 2. The mathematical census was independently rebuilt

The implementation defect does not change the intended affine system. To make sure the result was not being rescued by assumption, the intended system was independently reconstructed with the corrected per-vertex force-cycle dispatch.

The reconstruction reproduces, from first principles:

- 57 admissible interior-ground radial slot vectors;
- 4332 labelled compatible order/sign states;
- 184 orbits modulo heptagon dihedral symmetry and global sign reversal;
- the split `120 C7 + 64 (C3 + C4)`;
- the 84 variables (`35` force-turn, `42` full hull raw-gap, `7` ground radial-gap);
- 92 affine equalities;
- 112 strict affine inequalities.

A strict-margin LP on the intended system leaves exactly the same 27 positive-margin cells:

```text
115, 118, 129, 130,
134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148,
169, 170, 171, 172, 173, 174, 175, 176
```

and all 27 are `C7` cells.

## 3. Exact rational certificates were regenerated and checked

The 157 excluded cells were not accepted from the broken verifier. Candidate Farkas multipliers were regenerated from the corrected system and reconstructed over `fractions.Fraction`. Every resulting certificate was then checked by exact coefficient cancellation against the rebuilt affine rows.

The exact recertification reproduces:

```text
PASS: exact full-angle H7b reduction
generic H7b order/sign orbits: 184
excluded by exact rational Farkas certificates: 157
  C7 excluded: 93; C3+C4 excluded: 64
  boundary certificates: 38
surviving necessary affine cases: 27 all C7
most negative certificate rhs: -5/42
```

Thus the `184 -> 27 C7` mathematical reduction survives independent exact recertification. What failed was the executable routing in the originally committed verifier, not the affine exclusion itself.

## 4. Equality-space dimension of every survivor

For each of the 27 survivors, the 92-row equality matrix has exact rational rank

```math
57
```

inside the 84-variable full-angle space. The augmented matrix has the same rank in every case. Hence each surviving affine equality cell has dimension

```math
84-57=27.
```

This is only an equality-space dimension statement. It does not imply that the subsequent nonlinear equations are independent or that the cell is empty.

## 5. Correct status

The generic `H7b` endpoint remains exactly 27 necessary affine `C7` cells. The old verifier should not be cited as an executable pass without the repair shim above. The next proof layer is nonlinear metric/force compatibility, not another affine recensus.

No theorem-state file is changed. C-II remains open.
