# Hostile audit — branch-aware matched atomic gap `g=0.0071`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_branch_aware_iterative_pruning_atomic_gap_0071_2026-09-15.md`
- `research/verify_target_c_branch_aware_atomic_gap_0071.py`
- `research/verify_target_c_branch_aware_atomic_gap_0071_pi_enclosure.py`

**Disposition:** **PASS at proof-only canonical full-core Type-II train-measure scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate raises the matched all-train and rhombic-only atomic gaps to

\[
\boxed{g=0.0071}
\]

using the stronger branch of the already-audited iterative-pruning pair theorem.  The
mathematical reduction survives audit.  One reproducibility defect was found in the
original verifier: it claimed to derive its `pi` interval from Machin's identity but
hard-coded that interval.  The companion exact Fraction verifier added in commit
`35156935` now proves that enclosure independently, so the full numerical certificate
is self-contained when the two scripts are run together.

---

## 1. Pair-theorem branch selection

The parent theorem gives

\[
\rho\ge
\min\left\{
{e^2\over10},
{2m^2\over29}
\right\},
\qquad
e=(a+b-K)_+,
\quad m=\min(a,b).
\]

Thus the `e^2/10` branch is valid whenever

\[
{e\over m}\le\sqrt{20/29}.
\]

The candidate uses exactly this condition.  The unconditional relaxation
`e<=sqrt(29/2)sqrt(rho)` and the strong-branch inequality
`e<=sqrt(10)sqrt(rho)` have the correct directions.

**Verdict:** PASS.

---

## 2. Dominant-orbit deficit domain

Under the contradiction hypothesis

\[
A\le\bar A=2\sqrt{\Delta_2}+0.0071,
\]

the generic exact-orbit square bound gives

\[
W\ge W_0={4\Delta_2\over\bar A}.
\]

Writing the dominant-orbit Mantel deficit as

\[
\delta=W^2/4-E,
\]

and bounding all residual-orbit crossings by `(A-W)^2/4` gives

\[
0\le\delta\le d_0=\sqrt{\Delta_2}\,g+g^2/4.
\]

No crossing mass is dropped with the wrong sign.  The center imbalance
`z=C-W/2` obeys `|z|<=sqrt(delta)` from `E<=C(W-C)`.

**Verdict:** PASS.

---

## 3. Strong-branch test for both center-leaf pairs

For a leaf of mass `L`, the relevant ratio is

\[
{(C+L-K)_+\over L}.
\]

In the candidate domain `C<K`, so where positive this ratio increases with `L`.
Because `L<=W-C`,

\[
{(C+L-K)_+\over L}
\le {W-K\over W-C}.
\]

Substituting `C=W/2+z`, the sufficient strong-branch condition becomes

\[
\left(1-{r\over2}\right)W+r z\le K,
\qquad r=\sqrt{20/29}.
\]

Using `W<=bar A` gives the stated conservative threshold

\[
z\le z_*={K-(1-r/2)\bar A\over r}.
\]

Thus using `sqrt(10)` below the certified `z_*` and reverting to `sqrt(29/2)` above it
is safe.

**Verdict:** PASS.

---

## 4. Weighted two-leaf correlation

Let `x,y` be center-leaf missing masses and `e(U,V)` the leaf-leaf crossing mass.  The
triangle-free center-neighborhood argument gives

\[
C e(U,V)\le Vx+Uy.
\]

With

\[
a=1-V/C,
\qquad b=1-U/C,
\]

this is exactly

\[
a x+b y\le h,
\qquad h=x+y-e(U,V).
\]

The weighted average step is also correct:

\[
{aU+bV\over a+b}\ge{U+V\over2}
\]

is equivalent to `4UV<=(U+V)^2`.  Cauchy then gives

\[
\max(F_U,F_V)
\ge {W+C\over2}
-\lambda\sqrt{h\,{C\over3C-W}}.
\]

Substituting `C=W/2+z` yields the candidate's factor

\[
{W+2z\over W+6z}.
\]

**Verdict:** PASS.

---

## 5. One-dimensional outward minimax

The interval reduction uses only monotonicity in directions that weaken the lower
bound.  For `z<0`,

\[
R(W,z)={W+2z\over W+6z}
\]

decreases with both `W` and `z`, so using the smallest allowed `W` and the left edge
of each `z` cell maximizes the square-root loss.  For `z>=0`, `R<=1` is safe.  The
quantity `d_0-z^2` is maximized at the point in the cell nearest zero.  The raw term
`3W/4+z/2` is minimized using `W=W_0` and the left cell endpoint.

The `10^-5` grid therefore supplies an outward lower bound, not a sampling heuristic.
The certified interval `[-0.083,0.083]` strictly covers `|z|<=sqrt(d_0)`.

**Verdict:** PASS.

---

## 6. Numerical certificate and repaired `pi` enclosure

The main Fraction verifier checks its square-root enclosures and obtains a contradiction
margin exceeding `3.66e-4` at `g=0.0071`.  Its only self-containment defect was the
hard-coded `pi` interval.

The independent companion verifier proves

\[
\pi=16\arctan(1/5)-4\arctan(1/239)
\]

with alternating rational series and encloses the true value in an interval of width
below `3.6e-86`.  That interval lies strictly inside the main verifier's hard-coded
`10^-60` interval, with lower and upper safety margins approximately

\[
5.92\times10^{-61},
\qquad4.08\times10^{-61}.
\]

Thus the constants used by the main verifier are now independently certified.

**Verdict:** PASS after companion enclosure patch.

---

## 7. Rhombic-only transfer

Sections 1--6 use only the simple triangle-free train-crossing graph, exact phase-orbit
crossing decomposition, and the physical iterative-pruning pair theorem.  Those inputs
are available on the non-singleton strict-rhombus train graph exactly as in the prior
hostile-audited matched-gap transfers.  Singleton trains and outer-hull response are
not used.

Hence the same argument proves

\[
\liminf {T_R\over D}\ge2\sqrt{\Delta_2}+0.0071,
\]

and therefore

\[
\liminf {\sigma_R\over D}\ge0.0142.
\]

**Verdict:** PASS.

---

## 8. Final disposition

The matched atomic gap

\[
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.0071
}
\]

and its rhombic-only counterpart are valid at the stated proof-only scope.  The result
does not close C-II by itself, but it may now be used as an audited input by downstream
low-`t` arguments.

**Final verdict:** PASS after the explicit `pi`-enclosure repair. C-II remains open.
