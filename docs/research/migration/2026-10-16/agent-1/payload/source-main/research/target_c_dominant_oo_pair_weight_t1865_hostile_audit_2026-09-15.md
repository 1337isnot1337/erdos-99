# Hostile audit — dominant retained O--O pair weight through `t<=1.865`

**Date:** 2026-09-15
**Reviewed:**
- `research/target_c_dominant_oo_pair_weight_t1865_2026-09-15.md`
- `research/verify_target_c_dominant_double_outer_trains_g0076_t1865.py`

**Disposition:** **PASS at the stated proof-only full-core scope.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate extends the existing `g=0.0076` retained-mass bootstrap from `1.860` to
`1.865`.  This is close enough to the numerical zero of the retained-pair margin that
the audit must check scope rather than merely rerun decimal arithmetic.

The extension is valid.  The parent proof explicitly states that its bootstrap map
uses only the symbolic retained-mass inequalities and the monotonicity signs of
`m_2,r`; no `t<=1.860`-specific scalar-floor estimate enters.  At the new endpoint the
radical domain and complement denominator remain safely valid, every rounded bootstrap
step has positive exact margin, and the final conversion uses the independently proved
retained **pair-weight** inequality rather than the weaker double-outer train-count
currency.

---

## 1. No stale `delta<0.05` or other narrow scalar-floor input is imported

The parent theorem records its inputs as

\[
z+p\ge \pi-U-(t+\kappa)/2+m_2(U)-o(1),
\]

\[
p\le {\delta-F(z)+r(U)^2\over2(1-\delta)}+o(1),
\]

\[
\delta\ge F(z)-o(1),
\qquad
U\ge C_{76}-o(1).
\]

It explicitly states that the old feasible-triangle `delta<0.05` estimate is not used.
The bootstrap endpoint enters only through

\[
U_{max}=9T/2-2\pi,
\qquad
\delta_{max}=(U_{max}-C_{76})/2.
\]

At `T=1.865`, the exact certificate proves

\[
\delta_{max}<0.099<1.
\]

Therefore the complement denominator remains uniformly positive.  No old `0.0873`
bound from `T=1.860` is reused.

**Verdict:** PASS.

---

## 2. The `m_2` radical and derivative signs remain in scope

The parent monotonicity argument assumes

\[
U\ge C_{76}>2\sqrt{\Delta_2}.
\]

This is unchanged.  On that branch,

\[
m_2'(U)<0,
\qquad
r'(U)>0.
\]

The exact verifier additionally evaluates

\[
8\Delta_2-U^2
\]

outward at every bootstrap step and asserts its lower enclosure is positive before
calling the square root.  Thus the formula for `m_2(U)` remains real on every adverse
endpoint used by the proof.

The retained-mass envelope derivatives consequently retain the same signs:

\[
S_t<0,
\qquad
S_\delta>0,
\qquad
S_\kappa>0.
\]

So setting `t=T`, `kappa=0`, and `delta=F(z_j)` is still the adverse lower-bound
choice.  There is no derivative sign change between `1.860` and `1.865`.

**Verdict:** PASS.

---

## 3. Every rounded bootstrap implication is exact and outward

The verifier uses rational Machin enclosures for `pi`, integer-square-root enclosures,
and alternating-series enclosures for `sin`.  It proves

```text
0       -> 1.9111    margin > 8.79e-5
1.9111  -> 2.0144    margin > 5.46e-5
2.0144  -> 2.0311    margin > 6.29e-5
2.0311  -> 2.0339    margin > 1.04e-4
2.0339  -> 2.0344    margin > 8.51e-5
2.0344  -> 2.0345    margin > 7.09e-5.
```

The rounded values are all downward relative to the certified next-step lower bound.
The final retained-edge energy is bounded outward as

\[
F(2.0345)>0.03876343775,
\]

which gives

\[
U<2.031787818+o(1).
\]

These margins are much larger than the final `0.0027` retained-pair rounding gap.

**Verdict:** PASS.

---

## 4. The final currency is retained pair weight, not just train count

The older double-outer theorem used

\[
zD\le M_D+H_D
\]

to infer a count of trains with two selected terminal occurrences.  That is not by
itself enough for the weighted phase-zero deletion argument.

The candidate correctly invokes the later retained pair-weight identity.  For one
train with terminal retained weights `a_tau,b_tau`, put

\[
w_\tau=\min(a_\tau,b_\tau).
\]

Then finitely

\[
a_\tau+b_\tau\le1+w_\tau.
\]

Summation gives

\[
z\le M_{dom}+P_{OO}^{dom}+o(1),
\]

while the exposed-hull train-mass chain gives

\[
M_{dom}\le U+o(1).
\]

Hence

\[
P_{OO}^{dom}\ge z-U-o(1).
\]

Using the exact rounded bounds gives

\[
P_{OO}^{dom}/D>0.002712\ldots-o(1)>0.0027-o(1).
\]

This is the correct weighted currency.  Dividing among at most three dominant
projective phase classes yields one phase with pair weight `>0.0009D-o(D)`.

**Verdict:** PASS.

---

## 5. The theorem does not overclaim a path

The result stops at retained pair weight.  It does not infer low terminal energy,
fixed positive endpoint-arc separation, or a complement-dual path.  This matters
because the current main low-energy path reaches only `1.8623`.

A separate phase-zero marker theorem can potentially convert the new pair weight into
a path without a low-energy truncation, but that route has its own asymptotic deletion
and topology proof and must remain a separate dependency.

**Verdict:** PASS.

---

## 6. Endpoint sharpness

A floating-point fixed-point exploration, used only for route selection, places the
zero of the same retained-pair lower envelope near

\[
1.865196.
\]

The candidate makes no theorem claim there.  `1.865` leaves a positive exact pair
margin while `1.866` is already negative in the continuous relaxation.  Stopping at
the safely rounded endpoint is appropriate.

**Final disposition:** **PASS.**  The dominant retained O--O pair-weight theorem is
valid through `t<=1.865` at the stated full-core scope.  C-II and Level I remain open.
