# Hostile audit — extended multi-rhombic empty-pentagon range

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_multirhombic_empty_pentagons_extended_range_2026-09-15.md`  
**Disposition:** **PASS at its stated Branch-R scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate propagates the already-audited multi-rhombic pentagon counting inequalities beyond the former `t<=1.8623` endpoint, using the separately audited fact that the matched all-train gap and modern train-slack split are uniform throughout the full-core Type-II train-measure branch.

## 1. Scope propagation is legitimate

The hostile audit of the extended pentagon sea verifies that

\[
P_5/D\ge C_{707}+\pi-{5t\over2}-o(1)
\]

holds at every fixed full-core endpoint for which the right side is used.  The modern Branch-R split is likewise global in the full-core train-measure branch and gives

\[
I_5/D\ge5\left(C_{707}+\pi-{5t\over2}\right)-\tau_0-o(1).
\]

No O--O path, residual-localization, or `t<=1.8623` hypothesis enters either inequality.

**Verdict:** PASS.

## 2. The `X_2` and `X_3` affine formulas are correct

The finite incidence inequalities are

\[
X_2\ge{I_5-Q\over4},
\qquad
X_3\ge{I_5-2Q\over3},
\]

with

\[
Q/D\le2t-\pi+o(1).
\]

Write

\[
p_5(t)=C_{707}+\pi-{5t\over2},
\qquad
i_5(t)=5p_5(t)-\tau_0.
\]

Then

\[
\begin{aligned}
{i_5(t)-(2t-\pi)\over4}
&={5C_{707}+6\pi-\tau_0-(29/2)t\over4},
\end{aligned}
\]

and

\[
\begin{aligned}
{i_5(t)-2(2t-\pi)\over3}
&={5C_{707}+7\pi-\tau_0-(33/2)t\over3}.
\end{aligned}
\]

A separate symbolic Pyroam regression represented each affine expression by its coefficient vector in `(C707,pi,t,tau0)` and reproduced exactly

```text
X2: (5/4, 3/2, -29/8, -1/4)
X3: (5/3, 7/3, -11/2, -1/3).
```

The first draft of that independent checker accidentally encoded `Q=2t+pi`; it failed, the sign bug was identified immediately, and the corrected independent regression passed.  No repository theorem or certificate used the erroneous checker.

**Verdict:** PASS.

## 3. Positivity thresholds use the correct denominators

Setting the two affine lower envelopes equal to zero gives

\[
t_2^*={5C_{707}+6\pi-\tau_0\over29/2},
\]

\[
t_3^*={5C_{707}+7\pi-\tau_0\over33/2}.
\]

The exact companion certificate uses outward enclosures for `pi` and `sqrt(Delta_2)` and proves safe lower enclosures

\[
t_2^*>1.9078,
\qquad
t_3^*>1.8670.
\]

Thus the candidate's qualitative ranges

```text
X2 = Omega(D) for every fixed t < 1.90789...
X3 = Omega(D) for every fixed t < 1.86703...
```

are correctly stated as scalar-envelope thresholds, with displayed decimal values only descriptive and the rational lower enclosures load-bearing.

**Verdict:** PASS.

## 4. Representative endpoint rows are conservative

The exact verifier gives, among others,

```text
T=1.865: X2/D > 0.1554..., X3/D > 0.01117...
T=1.880: X2/D > 0.10110...
T=1.900: X2/D > 0.02860...
T=1.905: X2/D > 0.01048...
T=1.907: X2/D > 0.00323....
```

The theorem rounds these downward (`0.1518`, `0.0111`, `0.1011`, `0.0286`, `0.0104`, `0.0032`).  The first `X2` row is noticeably coarser than necessary but remains valid.

**Verdict:** PASS.

## 5. Empty-face and double-corner conclusions still apply

All faces counted by `X2` and `X3` are pentagons, and the merged isolate-host theorem is independent of `t`: every bounded pentagonal contact face has empty source interior.

Every `X3` pentagon has at least three rhombus-adjacent sides.  Since the independence number of the side-adjacency cycle `C_5` is two, two of those marked sides are consecutive.  Hence each `X3` face contains at least one double-rhombic pentagon corner.

This remains a face-corner count, not a count of distinct contact vertices.

**Verdict:** PASS.

## 6. No hidden extension of the path theorem

The candidate keeps the wider pentagon ranges logically separate from the current valid O--O path endpoint `t<=1.860`.  In particular, it does not infer a hub, one-sided switching, or path-region saturation above that endpoint.

The wider result is solely a consequence of the uniform all-train/face ledger.

**Final verdict:** **PASS.** The extended multi-rhombic ranges and the two positivity thresholds are valid at the stated Branch-R scope. C-II remains open.
