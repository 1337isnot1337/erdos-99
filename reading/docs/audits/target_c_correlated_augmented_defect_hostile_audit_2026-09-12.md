> Generated reading edition · [exact source](../../../docs/audits/target_c_correlated_augmented_defect_hostile_audit_2026-09-12.md) · source SHA-256 `8c484b6082d0e593fa982f4bc29dbe51e7fb6d1c837d6b76674a9cf14705fe7a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-78BBD87E48B3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C correlated augmented-defect currencies

**Date:** 2026-09-12
**Reviewed:** proof-only post-123 cancellation on the Type-II full-core branch.
**Disposition:** **PASS after case-split sign repair at proof-only scope.** C-II remains open.

## 1. Exact implication chain

```text
loaded-hull localization + augmented-triangle charging + outer-tooth exactness
 -> finite identity (a-T)-Q^+ = 2k+2(m-T)+4c_I-4
 -> collapse of the augmented route-return lower bound
 -> at least one of attachment-diameter deficit, Q^+, k, or m-T is linear
 -> a future source-level contradiction if each currency is independently bounded.
```

The final contradiction is not present. This audit checks the finite cancellation and
the asymptotic case split only.

## 2. Recompute the finite identity

Use the named proof-only ledgers, with

```math
a=q-2+2c_I-d_{tile},\qquad e_{BB}=q-m,
```

and put `r_deep=m-T`.  Then

```math
A_*:=a-T
=e_{BB}+r_{deep}+2c_I-2-d_{tile}.
```

The augmented-triangle identity is

```math
Q_*:=\sum_rQ_r^+
=Q+u_B-r_{deep}-2(c_I-1)-d_{tile}.
```

The loaded-hull identity is `e_BB=Q+2k+u_B`, hence

```math
Q_*=e_{BB}-2k-r_{deep}-2c_I+2-d_{tile}.
```

Subtracting gives, with no limiting operation,

```math
A_*-Q_*=2k+2r_{deep}+4c_I-4.
```

Both `d_tile` and `e_BB` cancel exactly.  The nonnegative structural terms used later
are `k,r_deep,c_I,Q_*\ge0`; no independent sign is assigned to either `A_*` or
`Delta_ad`.

**Verdict:** PASS, conditional on the proof-only ledgers explicitly named by the
candidate. The algebra has no coefficient or sign error.

## 3. Recompute the collapsed return currency

The augmented-route lower bound is

```math
\liminf D^{-1}\left(\Delta_{ad}+\frac12A_*+3Q_*\right)
\ge \frac\pi4(2-\sqrt3).
```

Substituting `A_*=Q_*+2k+2r_deep+4c_I-4` gives

```math
\Delta_{ad}+\frac12A_*+3Q_*
=\Delta_{ad}+\frac72Q_*+k+r_{deep}+2c_I-2.
```

Because Section 75 supplies `c_I=O(D^{2/3})`, the finite `2c_I-2` term is `o(D)`.
Therefore the displayed first-order inequality with currencies

```math
\Delta_{ad},\quad \frac72Q_*,\quad k,\quad r_{deep}
```

is valid at the stated proof-only scope.

**Verdict:** PASS.  The passage to the limit discards only `o(D)` and preserves the
lower-bound direction.

## 4. Exhaustiveness of the case split

The earlier audit draft incorrectly called all four displayed currencies nonnegative.
Only `Q_*`, `k`, and `r_deep` are nonnegative a priori. The source route-compression
theorem does **not** prove `Delta_ad=sum_r(a_r-d_r)>=0`; it proves only correlated
compatibility inequalities involving that term.

This sign correction does not invalidate the claimed subsequence alternative. Let

```math
c_{ret}:={\pi\over4}(2-\sqrt3)>0.
```

If at least one of `Q_*/D`, `k/D`, or `r_deep/D` has positive limsup, then one of the
four named currencies is already linear along a subsequence. Otherwise those three
nonnegative normalized terms tend to zero along a common further subsequence, and the
collapsed return inequality itself forces

```math
\liminf {\Delta_{ad}\over D}\ge c_{ret}>0.
```

Thus the report's conclusion remains correct: after subsequence extraction, at least
one of `Delta_ad`, `Q_*`, `k`, or `r_deep` has positive linear scale. The proof is the
dichotomy above, not an assertion that `Delta_ad` is globally nonnegative.

For the quantitative form, if each of `Q_*/D`, `k/D`, and `r_deep/D` is at most
`eta` asymptotically, then

```math
\liminf\frac{\Delta_{ad}}D
\ge\frac\pi4(2-\sqrt3)-\frac72\eta-\eta-\eta
=\frac\pi4(2-\sqrt3)-\frac{11}2\eta,
```

with the `2c_I-2` term vanishing. This coefficient is correct and requires no
independent sign assumption on `Delta_ad`.

**Verdict:** PASS after correcting the sign rationale.

## 5. Binding limitations

- The cancellation inherits the proof-only status of loaded-contact localization,
  augmented-triangle charging, and outer-tooth exactness.
- It does not bound any of the four remaining currencies.
- It does not control the macroscopic inactive-container branch.
- It does not convert a linear `k` or `r_deep` term into an exact unit triangle or a
  source-preserving strict competitor.
- `Delta_ad` has no independent nonnegativity theorem here; downstream arguments must
  preserve the correlated lower bound rather than silently treating it as positive.
- Contact-isolated source points remain outside all core ledgers and are not deleted.

## Final classification

**Audited-working after sign-rationale repair.** The exact cancellation is sound and
materially sharpens the full-core research split, but it is not a canonical promotion
and does not close C-II.
