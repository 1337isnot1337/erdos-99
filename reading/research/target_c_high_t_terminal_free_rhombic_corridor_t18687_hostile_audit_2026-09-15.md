> Generated reading edition · [exact source](../../research/target_c_high_t_terminal_free_rhombic_corridor_t18687_hostile_audit_2026-09-15.md) · source SHA-256 `fad11b41d6084454b9d42bf471b9e09ccb3aadf88b9c4ebd2506efb2ec86dc48`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "1b0b793cccaec9c04735f76bb099c51a0bcd5413", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_terminal_free_rhombic_corridor_t18687_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "be1821804672eb1f80f722e4c40a7993bb02c0761392428cea8a69bfad7a17c7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — high-`t` terminal-free rhombic corridor through `t<=1.8687`

**Date:** 2026-09-15  
**Artifact audited:** `target_c_high_t_terminal_free_rhombic_corridor_t18687_2026-09-15.md`  
**Verdict:** PASS as a proof-only structural theorem; no C-II or Level-I promotion.

## 1. Dependency check

The argument uses only already-audited interfaces:

1. the finite-defect/KKT strip through `t<=1.8687`, including `L<=70954` terminal face-side occurrences and the common-neighborhood symmetric-difference bound;
2. the selected-train terminal-energy/rhombus-incidence inequality and the `t<=1.8687` bounds `e_tau<=0.5857-delta`, `delta<0.107+o(1)`;
3. simplicity and triangle-freeness of the complete-train crossing graph, giving distinct crossing neighbors and common order for the through-going family;
4. the stopped-train decomposition fact that every side occurrence of a bounded nonquadrilateral face is a train terminal occurrence;
5. the phase-collapsed joint cusp for the optional near-triangular subcorridor.

No new response inequality, stress lower bound, or unproved lattice approximation is introduced.

## 2. Common-family count

For each selected boundary train,

$$
r_tau/D\ge1-delta-e_tau/2-o(1)
\ge0.70715-delta/2-o(1)
>0.6536-o(1).
$$

Simplicity of train crossings converts rhombi to distinct crossing neighbors. The finite-strip theorem gives

$$
|Gamma(tau_0) triangle Gamma(tau_1)|<=70954.
$$

Therefore

$$
|Gamma(tau_0) cap Gamma(tau_1)|>0.6536D-o(D).
$$

The subtraction of the fixed constant `70954` is correctly absorbed into `o(D)`.

## 3. Pigeonhole check

Order the common transverse trains between the two boundary crosscuts. A terminal occurrence cannot lie in the interior of a common column segment because that segment is a through-going stopped-train midpoint path consisting only of strict-rhombus steps between its two boundary crossings.

At most `L` internal gaps are contaminated, because every contaminated open slab contains at least one terminal occurrence and one occurrence belongs to only one open slab. Removing contaminated gaps divides the column sequence into at most `L+1` consecutive blocks.

Hence the largest clean block has at least `M/(L+1)` columns. The exact certificate verifies

$$
0.6536/70955>9.2e-6
$$

and

$$
0.0783/1109000>7e-8.
$$

The theorem uses strict asymptotic inequalities, so the fixed endpoint/gap conventions do not affect the stated `cD-o(D)` bounds.

## 4. Pure-rhombic claim scope

The dangerous overclaim would be “the corridor contains no other source points” or “the corridor is a literal two-family lattice.” Neither is asserted.

The proved statement is only:

> every bounded **contact face** meeting the open retained corridor is a strict rhombus.

If a bounded nonquadrilateral contact face met an open terminal-free slab, at least one of its boundary side occurrences would be a stopped-train terminal occurrence in that slab, contradiction. Common transverse midpoint arcs cannot pass through such a face because a stopped train terminates when it reaches a non-rhombic face.

Contact-isolated source points may remain in interiors of rhombic contact faces. Extra complete trains may also cross the corridor through strict rhombi. These possibilities do not contradict the theorem and are explicitly retained in its scope note.

## 5. Phase-controlled subcorridor

The second conclusion is obtained only by taking a subfamily of the already-audited joint-cusp family `B_0`. Therefore common order and the crossing-angle estimate

$$
0<theta-pi/3<1.416e7/D+o(D^{-1})
$$

are inherited without modification. The contaminated-gap deletion does not alter any crossing angle or row choice.

## 6. Non-conclusions

This result does not prove:

- that the terminal-free corridor is empty of contact-isolates;
- that the only trains in the corridor are the two selected rows and retained columns;
- that the one/two switching diameter bars are absent;
- that a multishear decreases every active diameter;
- that Type II, C-II, or Level I is closed.

The theorem is useful because it relocates all bounded non-rhombic contact-face defects away from a linear ordered transverse block while preserving the existing finite KKT cusp at the row interface.

**Audit verdict:** PASS, proof-only. The constants and topology are consistent with the cited audited interfaces, and the statement avoids the source-empty/literal-lattice overclaim.
