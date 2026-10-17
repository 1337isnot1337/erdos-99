> Generated reading edition · [exact source](../../research/target_c_flat_pentagon_hidden_derivative_rank_independent_audit_2026-09-14.md) · source SHA-256 `d27e78d04af8761035523bb893e2e7a44b146a4bcbf8916c81502b7196cf338a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "4dea53aa8acb98b2cb51f261d7fc93598f3f3239", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_flat_pentagon_hidden_derivative_rank_independent_audit_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a50b7e1929041fa2edbe445cb26b84dce25a78be61782bbe81c8e1d1b34eab92"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Independent audit - flat-pentagon hidden-derivative rank

**Date:** 2026-09-14
**Object audited:** `target_c_flat_pentagon_hidden_derivative_rank_2026-09-14.md`
**Disposition:** PASS for the structural rank theorem; numerical insertion superseded by the refined payment note

## LEVEL I STATUS

`STILL OPEN`

The load-bearing claim is

```math
\operatorname{rank}(H_P|_{\ker C_{face}})
\ge {7p\over3}-2f+\sigma_C.
```

I checked the following points independently.

1. **Local block.**  At the flat trapezoid the two closure rows and the two hidden
   radial rows have a `4 x 4` minor equal to `(sqrt(3)/2)^3`, hence rank four.  All
   four rows kill the all-ones angular-rate vector, so their common kernel on the five
   incident train variables is exactly the rotation line.  Continuity preserves this
   rank on one fixed sufficiently flat neighborhood.

2. **Five distinct train variables per pentagon.**  Bounded-face train-loop exclusion
   prevents a complete train from returning to the same pentagon.  Thus the five
   boundary occurrences are five train variables.

3. **Internal incidence simplicity.**  Bounded-face endpoint simplicity forbids two
   distinct trains from joining the same pair of selected pentagons.  The selected
   face-to-face endpoint graph is therefore simple.

4. **Component count.**  A component of `s` selected pentagons with `e` internal
   trains uses exactly `n=5s-e` train variables.  Setting closure and both hidden rows
   to zero makes all five rates equal on each face, and connectivity propagates one
   common rate through the component.  Hence the combined local row rank is `n-1`.
   Simplicity and degree at most five give

   ```math
   e\le\min\{\binom{s}{2},\lfloor5s/2\rfloor\},
   
   ```

   and direct checking for `s<=5`, followed by the degree bound for `s>=6`, gives
   `n-1>=7s/3`.  Equality can occur in the abstract bound at `s=6`; a pure
   `3:1:1` phase coloring does not exclude that case, so the theorem correctly does
   not claim a larger local coefficient.

5. **Global rank subtraction.**  Different selected components have disjoint train
   variable supports.  Since the selected closure rows are a subset of `C_face`,

   ```math
   \operatorname{rank}\binom{C_{face}}{H_P}
   \ge {7p\over3}.
   
   ```

   The exact linear identity

   ```math
   \operatorname{rank}(H_P|_{\ker C_{face}})
   =\operatorname{rank}\binom{C_{face}}{H_P}-\operatorname{rank}C_{face}
   
   ```

   and `rank C_face=2f-sigma_C` prove the claimed bound.

The theorem is therefore a valid proof-only activation-rank reduction.  It says the
hard pentagon sea is not first-order redundant with contact closure; the remaining
obstruction is the active-diameter locking map.  It does not supply a common sign for
hidden-chord shortening and does not by itself close C-II.
