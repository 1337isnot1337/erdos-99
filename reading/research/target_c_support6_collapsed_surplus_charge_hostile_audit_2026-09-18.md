> Generated reading edition · [exact source](../../research/target_c_support6_collapsed_surplus_charge_hostile_audit_2026-09-18.md) · source SHA-256 `8c491ad5f194ce40909f7a263d0ef509daf143a0e945c17324d3385c25dce359`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "55786585e5ead514005a973403a5d54fb96de8f1", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_surplus_charge_hostile_audit_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e7f2d58be28ebe37e6234e4932bd1fcb1e8926d6126d519be837efe69bd2b6c9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — collapsed support-six surplus charge

**Audit date:** 2026-09-18  
**Disposition:** PASS for the stated degree-pure residual scope; no C-II promotion

## What is proved

The exact one-unit charge for a bounded-face component with one projective outer
anchor direction is already the audited host-anchor theorem (HA.1). The main note
specializes that theorem to a degree-pure collapsed support-six component and then
combines it with the newer support-five/noncollapsed-support-six exclusions. The
verifier independently checks the specialization symbolically: internal train columns
cancel in the sum of the six first-coordinate rows, and anchor columns have zero
first-coordinate derivative.

For disjoint degree-pure blocks, the row supports are disjoint, so the dependencies
are independent. The audited closure-rank theorem then gives `c <= sigma_C <= s_Z`.
Splitting the existing one-anchor component count into noncollapsed size at least seven
and collapsed size six gives the new displayed implicit and explicit corank bounds.

## Scope checks

1. The argument is about the linearized train-angle closure matrix, not a claim that
   the local collapsed pentagon family embeds globally.
2. “Degree-pure” is essential: an internal train leaving the six-face block would
   contribute to the proposed row sum unless the corresponding endpoint rows are
   included.  The support-six one-anchor reduction supplies the isolated relation
   graph `K_6` minus a matching in this scope.
3. Projective parallelism is enough.  The signs of the six anchors do not matter,
   since rotating a vector parallel to `e_1` has zero `e_1` component.
4. The result supplies only one dependency.  A second dependency would require an
   additional relation among the six outside angular rates and is not assumed.
5. The inequality `c <= sigma_C` counts independent row dependencies; it does not
   identify `c` with the number of globally realizable collapsed blocks outside the
   degree-pure residual decomposition.
6. The terminal decimal is an explicit consequence of the existing audited `f/D`
   bound and `E_U=o(D)` floor; it is not a new global density theorem.

## False stronger claims rejected

- The local contraction certificate is not upgraded to a global source realization.
- The charge is not used to claim `s_Z=0`, nor to eliminate all collapsed blocks.
- The coefficient `n_1/7` is not asserted unconditionally; the exact unconditional
  replacement is the implicit/`42/41` bound in the note.
- Contact-isolated source points and the full-source diameter system are untouched.

**Audit conclusion:** the row-dependency and corank bookkeeping are exact within the
degree-pure one-anchor scope.  The remaining C-II obstruction is global routing or
diameter/KKT compatibility of collapsed blocks.
