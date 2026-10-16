<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c9cf5da181ff9f6df281857c0bbf8df293ae715f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_typeii_boundary_defect_tradeoff_hostile_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c99c133d0d296f1ee805713f67e1f7d4972897cb45af6aff1102c8e3c0916f17"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Type-II low-q-k boundary-defect tradeoff

**Date:** 2026-09-12  
**Reviewed:** target_c_typeii_boundary_defect_tradeoff_2026-09-12.md  
**Disposition:** **PASS.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Exact ledger check

In Type II, the proof-only Section-125 identities are

\[
e_{BB}=q-m,
\qquad c_I+s_C=m+k-2,
\]

and Section 63 gives

\[
x_B=q-Q-2k,
\qquad u_B=x_B-m.
\]

Since q-k=tD,

\[
m=tD-Q-k-u_B.
\]

Therefore

\[
s_C=tD-Q-u_B-c_I-2,
\]

and the exact identity is

\[
3(h-s_Z)-2s_C=tD+2Q+2u_B+2c_I+4.
\]

This is correct. Section 125 also gives

\[
e_{BB}=Q+2k+u_B,
\]

so Q+u_B=e_{BB}-2k is correct.

**Verdict:** PASS.

## 2. Cellwise payment check

Section 132 gives

\[
3(h-s_Z)-2s_C\ge2\sum_r\sqrt{R_{4,r}}+6.
\]

In Type II, the unloaded-only rhombus count is at least
\Delta_2D^2-o(D^2) and belongs to the induced harmonic cells, while loaded-touching
rhombi contribute only O(D). Thus

\[
\sum_r\sqrt{R_{4,r}}
\ge(\sqrt{\Delta_2}-o(1))D.
\]

Combining with the exact identity gives

\[
t+2(Q+u_B)/D+o(1)\ge2\sqrt{\Delta_2}-o(1).
\]

**Verdict:** PASS at the stated proof-only scope.

## 3. Explicit numerical window

The source uses the certified value 2\sqrt{\Delta_2}=1.9046256137... for the
1.85 example, so the margin is

\[
\frac12(2\sqrt{\Delta_2}-1.85)=0.0273128068\ldots .
\]

The Section-162 low-window substitution similarly gives a margin greater than 0.0421.

**Verdict:** PASS.

## 4. Scope and limitation

The positive-part tradeoff is a convergent-subsequence statement. No global liminf
claim is made without passing to a subsequence on which t converges. The theorem uses
proof-only Sections 125 and 132 and does not promote either one.

No comparison is asserted between global (b-per(F))+(Q+4f) and local Q+u_B, and no
source point is removed. The result does not close C-II.

**Final classification:** audited-working proof-only Type-II tradeoff. Theorem-state
authority remains unchanged; C-II remains open.
