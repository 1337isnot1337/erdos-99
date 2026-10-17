> Generated reading edition · [exact source](../../../docs/audits/target_c_oler_gluing_train_surplus_hostile_audit_2026-09-14.md) · source SHA-256 `d2a3fbc2bc22eadda2c1986ca434b2c3e8e2dc5e19c0b7961ba627188632171a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1A16FF45C6E6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — exact Oler gluing and train-surplus correction

**Date:** 2026-09-14
**Target:** `research/target_c_oler_gluing_train_surplus_identity_2026-09-14.md`
**Base:** `3ed76f59`
**Disposition:** PASS at proof-only scope
**Theorem-state authority:** unchanged

## 1. Audit question

The target note claims the exact finite identity

$$
\Sigma_{ch}+\Sigma_{ext}
=\Omega_K+2(T-q/2)+2a+L_{cap},
\qquad L_{cap}=P_F-P_{com}-r\ge0,
\tag{A.1}
$$

and derives the Type-II chamber floor

$$
\liminf {\Sigma_{ch}\over D}
\ge4\sqrt{\Delta_2}+0.00084-\frac\pi2.
\tag{A.2}
$$

This audit rederives every load-bearing identity from canonical Sections 68, 77, 85,
and the audited stopped-train ledger. It specifically checks occurrence multiplicity,
cap assignments, the sign of the punctured slack, and the use of Cauchy's perimeter
bound.

## 2. Exterior-cap gluing: PASS

Canonical Section 77.2 gives for the nondegenerate exterior caps

$$
\sum_i A_i=A_K-A_F,
\qquad
\sum_iP_i=P_K+P_F-2P_{com},
\qquad
\sum_i z_i=Z_{ext}.
$$

The cap Oler inequality is

$$
z_i+2\le A_i/a_0+P_i/2+1,
$$

so the target definition

$$
\sigma_i^{ext}=A_i/a_0+P_i/2-1-z_i
$$

is nonnegative with the correct constant. Summing and adding

$$
\Sigma_F=A_F/a_0+P_F/2+1-N_F
$$

uses the exact partition `n=N_F+Z_ext` and gives

$$
\Sigma_F+\Sigma_{ext}
=A_K/a_0+P_K/2+1-n+P_F-P_{com}-r.
$$

Thus

$$
\Sigma_F+\Sigma_{ext}=\Sigma_K+L_{cap}
$$

with no omitted cap term.

For every noncommon force-hull side, the corresponding source-hull arc differs from
the side, so it produces exactly one nondegenerate Section-77 cap. Conversely every
nondegenerate cap has one such closing side. Therefore

$$
P_F-P_{com}=\sum_{i=1}^r\ell_i,
$$

where `ell_i` is the closing-side length. Its endpoints are distinct source points and
hence `ell_i>=1`. Therefore

$$
L_{cap}=\sum_i(\ell_i-1)\ge0.
$$

No assumption that the cap boundary is a contact path is used.

## 3. Chamber/force-hull difference: PASS

Canonical Section 77 gives

$$
A_F=A_4+A_{ch},\qquad N_F=m+Z_{ch},
$$

$$
m=R_4+f+q-k+1,
\qquad A_4=a_0R_4+E_4.
$$

The exceptional chamber perimeter is `4f+Q`. The outer-pocket perimeter is exactly

$$
b+P_F-2q+2a.
$$

Therefore

$$
P_{ch}-P_F=4f+Q+b-2q+2a.
$$

Canonical Section 85 gives the occurrence-counted identity

$$
b+Q=2(q-k),
$$

so

$$
P_{ch}-P_F=4f-2k+2a.
$$

Substitution into the definitions gives

$$
\Sigma_{ch}-\Sigma_F
=q+4f-2k+2a-E_4/a_0.
$$

The all-stopped-train identity is

$$
T=q-k+2f,
$$

including singleton trains. Hence

$$
q+4f-2k=2T-q=2(T-q/2).
$$

This proves the target equation (G.15) exactly. No rhombic-train/all-train count is
confused here.

## 4. Punctured slack sign: PASS

Canonical Section 68.4 proves

$$
a_0n\le A_K+c_0P_K+a_0-E_4,
\qquad c_0=a_0/2.
$$

After division by `a_0`,

$$
A_K/a_0+P_K/2+1-n-E_4/a_0\ge0.
$$

This is exactly

$$
\Omega_K:=\Sigma_K-E_4/a_0\ge0.
$$

Therefore adding the two already-audited identities gives (A.1) with the claimed
signs.

## 5. Chamber-only coefficient: PASS

From the exact identity before exterior gluing,

$$
\Sigma_{ch}
=\Sigma_F+2(T-q/2)+2a-E_4/a_0.
$$

Oler on the unit-separated set `A cap F` gives `Sigma_F>=0`, and `a>=0`. Section 68
also gives

$$
E_4<c_0P_K=(a_0/2)P_K,
$$

so

$$
E_4/a_0<P_K/2\le\pi D/2
$$

by Cauchy's convex perimeter-diameter inequality. Hence

$$
\Sigma_{ch}>2(T-q/2)-\pi D/2.
$$

The audited-working AG42 floor

$$
(T-q/2)/D\ge2\sqrt{\Delta_2}+0.00042-o(1)
$$

then proves (A.2). Numerically the coefficient is

$$
2.239294900660933\ldots .
$$

## 6. Attempted counterexamples and non-implications

1. **No exterior caps.** Then `r=0`, `P_com=P_F`, `Sigma_ext=0`, and (A.1) reduces
   consistently to `Sigma_ch=Omega_K+2(T-q/2)+2a`.
2. **Unit closing chords.** They contribute zero to `L_cap`, as required.
3. **Long noncontact closing chords.** They contribute `ell_i-1>0`; the target does
   not falsely identify them with contact edges.
4. **Bridges and singleton trains.** They are retained because `T=q-k+2f` is the
   all-stopped-train ledger and `b,Q` are occurrence-counted.
5. **Many small Type-II exterior caps.** Canonical Section 84 proves only
   `max_i per(K_i)=o(D)`, not `sum_i per(K_i)=o(D)`. Thus it does not imply
   `Sigma_ext=o(D)`. The target note correctly avoids that inference.
6. **Global Oler slack.** Equation (A.1) proves that `Sigma_ch` cannot be compared to
   `Sigma_K` without the train/cap corrections. Any claimed cancellation omitting
   `2(T-q/2)` is false at the exact bookkeeping level.

## 7. Disposition

PASS at proof-only scope. The theorem is an exact bookkeeping result plus one use of
the audited-working AG42 asymptotic floor. It materially corrects the suggested
additive-gluing handoff but does not close C-II.

The most useful downstream target is now quantitative: control `Sigma_ext`, `L_cap`,
or the signed corrected slack

$$
\Sigma_{ch}+\Sigma_{ext}-2(T-q/2)-2a-L_{cap}=\Omega_K
$$

at boundary order, rather than attempting to cancel chamber perimeter alone.

---

**Recovery provenance:** copied from `research/c2-gluing-sol-20260914-r10` at exact tip `58950d925eaec5d281cddc0202a4ef3df4c1b0fd` during the 2026-10-04 Slot 2 branch audit. This recovered claim remains unreviewed and noncanonical.
