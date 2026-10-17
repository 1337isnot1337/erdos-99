<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f7d1a3e35e8a51d3c25e0b3a9a036543978389a7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_small_leaf_center_fan_7404_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "fb50268deac373f2df19df57be38342a2264a4adf1b82b9a5d0bd08248a2b0cb"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — `>0.7404D` smallest-leaf center fan

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_small_leaf_center_fan_7404_t1844_2026-09-15.md`
- `research/verify_target_c_small_leaf_center_fan_7404_t1844_2026-09-15.py`
- parent `target_c_small_leaf_center_fan_073_t1844_2026-09-15.md`

**Disposition:** **PASS at proof-only `t<=1.844` full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit is deliberately narrow. The new note changes only the terminal scalar
threshold in an already-audited optimization. It must not revive the older invalid
fan-density-floor normalization that was retracted on September 12.

---

## 1. No new upstream inequality is introduced

The candidate reuses exactly the parent safe constants

\[
W_0=1.915963,
\quad E_0=0.9068958,
\quad C>0.8538,
\quad z_V>0.616,
\]

and the already-proved reduction

\[
R(C,V)=C-{CH(C)\over(2C+V-W_0)(0.616-V)},
\qquad H(C)=C(W_0-C)-E_0.
\]

The feasible domain and the concavity reduction in `V` are unchanged. Hence the only
new obligation is to prove `R(C,V)>0.7404` at the two endpoint families.

**Verdict:** PASS.

---

## 2. Low-leaf endpoint is comfortably positive

At `V=0.308`, clearing the positive denominator gives the cubic `N_lo,L` with
`L=0.7404`. The exact verifier proves strict convexity, brackets the unique critical
point in

\[
(0.88341,0.88342),
\]

and gives the rigorous lower bound

\[
N_{lo,L}>0.00233998.
\]

Both feasible interval endpoints are positive as well.

**Verdict:** PASS.

---

## 3. Balanced-leaf endpoint is the actual bottleneck and remains positive

At `V=(W_0-C)/2`, the exact verifier similarly proves strict convexity, brackets the
unique critical point in

\[
(0.90484,0.90485),
\]

and gives

\[
N_{hi,L}>4.47\times10^{-6}.
\]

The margin is much smaller than at the low-leaf endpoint but is exact. The certificate
uses only `Fraction` arithmetic; no floating-point root or sign is used in the proof.

Numerical minimization places the limiting rounded degree near `0.74050149`, so the
claimed `0.7404` lies on the correct side of the observed frontier. That numerical
value is diagnostic only.

**Verdict:** PASS.

---

## 4. The weighted-average inference is legitimate and limited

The theorem concludes

\[
{\sum_\tau w_\tau d_\tau\over\sum_\tau w_\tau}>0.7404-o(1)
\]

for positive retained pair weights `w_tau`. Therefore some positive-weight train must
have `d_tau>0.7404-o(1)`.

It does **not** infer that `0.7404D` distinct leaf trains exist, nor that every retained
leaf train has this degree. This distinction is exactly what the September 12 fan-floor
retraction requires.

**Verdict:** PASS.

---

## 5. Scope and downstream use

The result is valid only in the same `t<=1.844` phase-resolved full-core branch as its
parent. It can be inserted into the later weighted-good-leaf argument because that
argument uses a weighted average degree plus the pointwise upper degree bound
`d_tau<=1.063+o(1)`; it does not require an invalid unweighted fan floor.

No C-II closure or theorem-state promotion follows from the degree sharpening alone.

**Final disposition:** **PASS.**
