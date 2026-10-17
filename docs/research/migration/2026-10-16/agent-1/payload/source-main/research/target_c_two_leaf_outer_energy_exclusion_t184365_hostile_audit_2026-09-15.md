# Hostile audit — two-leaf outer-energy exclusion through `t=1.84365`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_two_leaf_outer_energy_exclusion_t184365_2026-09-15.md`
- `research/verify_target_c_two_leaf_outer_energy_exclusion_t184365.py`
- hostile-audited two-leaf outer-energy stack through `t=1.84364`
- `g=.007707` residual-stability theorem
- hostile-audited cross-phase O--O endpoint-energy theorem

**Disposition:** **PASS at the stated proof-only full-core/no-macroscopic-container Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate raises the full-core Type-II exclusion endpoint from `1.84364` to
`1.84365`.  This is a tight continuation: the final contradiction margin is only about
`1.2e-5 D`, and the residual-slack localization margin is below `3e-7`.  The audit
therefore checks scope before numerical arithmetic.

## 1. Residual stability is genuinely in scope

The published `g=.007707` residual-stability lemma is only stated through
`U_net<=2.013`.  The candidate does not extrapolate it.  Instead it first uses the
independent all-`t<=1.844` phase theorem

\[
z_C,z_U,z_V>.616-o(1),
\]

so total retained dominant outer mass is above `1.848D`.  The audited dominant energy
bound then gives

\[
\delta\ge F(1.848)-o(1),
\qquad F(s)=s-6\sin(s/6).
\]

The exact certificate proves

\[
F(1.848)>.029.
\]

Therefore, at `t<=1.84365`,

\[
U_{net}
\le {9t\over2}-2\pi-2\delta
<1.955081<1.956<2.013.
\]

The residual-stability conclusion

\[
R=U_{net}-W\le1.05h
\]

is thus invoked only after its scope gate is satisfied.

**Verdict:** PASS.  No hidden extension of residual stability is used.

## 2. The residual cutoff `h<.000378` is exact and monotone

At the adverse point `t=1.84365`, `h=.000378`, `x=0`, the direct survivor condition
fails by

\[
F(A_H)-\delta_H>2.92\times10^{-7}.
\]

The parent derivative bounds remain

\[
Q_x<-2.7,
\qquad Q_h<-2.5,
\qquad Q_t>0.
\]

Hence larger `h` or `x` cannot restore survival, and smaller `t` is no harder than the
endpoint.  The small margin is exact, not a floating-point sign.

**Verdict:** PASS.

## 3. Dominant-orbit rounding is adverse

The cutoff gives the safe box

\[
W<1.912711,
\qquad E_{dom}>0.90689962.
\]

The verifier checks `C707+.000378<1.912711` and subtracts the entire generic residual
square `(1.05H)^2/4` from `Delta_2` before rounding the crossing lower bound.  Both
roundings weaken the information in the direction favorable to a putative survivor.

**Verdict:** PASS.

## 4. The retained-mass floor `z>2.21934` handles the active boundary correctly

Assume `z<=Z=2.21934`.  The capped retained quantity is increasing in `z`; the exact
certificate bounds that derivative below by `.96`.

On the branch `delta>=F(Z)`, motion in `x` reaches the active boundary
`delta=F(Z)`.  Unlike the earlier `1.8436` proof, at the largest residual cutoff
`h=H` this boundary still has positive

\[
x>3.56\times10^{-6}.
\]

Thus the adverse boundary is actually feasible inside the box.  Evaluating it at the
largest permitted `h` gives capped-retention excess below

\[
-2.71\times10^{-5}.
\]

The complementary `delta<F(Z)` branch is controlled by the already-audited negative
`Q_x,Q_h` derivatives.  No boundary is skipped.

**Verdict:** PASS.

## 5. Phasewise bathtub promotion to `.702D` is valid

The exact phase windows are disjoint and obey

\[
\delta\ge f(z_C)+f(z_U)+f(z_V)-o(1),
\qquad f(s)=s-2\sin(s/2).
\]

With total retained mass above `Z=2.21934`, strict convexity says that if one phase were
at most `A=.702`, the cheapest remaining split is equal.  The certificate proves

\[
f(.702)+2f((2.21934-.702)/2)-R_T/2
>1.14\times10^{-6}.
\]

Therefore every exact phase retains more than `.702D`.

**Verdict:** PASS.

## 6. The leaf train-mass localization `U,V<.5304` stays inside the strong-pair scope

Assume `U>=U_0=.5304`, with `C>=U>=V` and `W<=1.912711`.

For `C<=.851911`, generic center capacity is increasing and already lies more than
`.003` below the required crossing mass.  For `C>=1.0443`, it is decreasing and lies
more than `1e-5` below the required mass.

On the remaining interval, the worst physical center/leaf excess ratio is

\[
<.791855<\sqrt{20/29},
\]

so the strong `1/10` pair theorem is used only on its certified branch.  The correlated
capacity reduction to the adverse values `W=W_0`, `U=U_0` is the same monotonic
reduction hostile-audited in the parent theorem.

For the resulting one-variable capacity `G(C)`, the symbolic second-derivative identity
gives `G''<-2`.  At `c_0=.931414`, the tangent bound yields a capacity deficit

\[
E_{dom}-\max G>2.25\times10^{-6}.
\]

Hence `U,V<.5304-o(1)`.

**Verdict:** PASS.

## 7. The bad-center O--O weight is one total budget

From `z_U,z_V>.702` and leaf masses below `.5304`, each leaf has retained O--O pair
weight

\[
P_U,P_V>.1716-o(1).
\]

The center/leaf missing-pair correlation bounds the **total** bad retained pair weight
across both leaves.  The candidate's quadratic certificate has discriminant

\[
<-2.5\times10^{-4},
\]

and gives

\[
B_U+B_V<.0367-o(1).
\]

Therefore each individual bad weight is also below `.0367`, so both leaves retain

\[
G_U,G_V>.1349-o(1).
\]

Subtracting the whole total bad budget from each leaf is deliberately wasteful but
valid; the proof does not create two separate `.0367` budgets.

Every good U/V pair shares a center neighbor because both degrees are strictly greater
than half of the same finite center family.  Triangle-freeness therefore makes the
entire good cross-product noncrossing.

**Verdict:** PASS.

## 8. The endpoint-energy and final detour ledger are disjoint

The two exact leaf phases differ projectively by `pi/3`.  The hostile-audited endpoint
theorem gives for every noncrossing good pair

\[
e_\tau+e_\sigma\ge2-\sqrt3-o(1).
\]

Weighted product summation gives

\[
E_U+E_V>(2-\sqrt3)(.1349)-o(1)
>.03613971-o(1).
\]

The center one-well payment uses selected occurrences in the disjoint center phase
window, so it can be added without double-counting:

\[
f(.702)>.0143259828.
\]

Thus

\[
\delta>.0504656928-o(1),
\]

whereas the complete envelope gives

\[
\delta<.0504535396+o(1).
\]

The exact final contradiction margin is

\[
1.2153\times10^{-5}.
\]

**Verdict:** PASS.

## 9. Independent exact recheck

Re-evaluating the certificate with exact rational arithmetic reproduces the load-bearing
margins:

```text
residual-scope U upper      1.9550800182...
h localization margin      2.9221071e-7
phase-imbalance margin      1.1414853e-6
strong ratio upper          0.79185418...
leaf-capacity margin        2.2566814e-6
bad-weight discriminant    -2.54086716e-4
final energy margin         1.2153328e-5
```

All asserted signs agree with the committed verifier.

**Verdict:** PASS.

## 10. Scope and frontier

The theorem excludes only the stated full-core/no-macroscopic-container Type-II branch.
It does not by itself close C-II globally or Level I.  Numerically, the present rounded
two-leaf propagation is close to exhaustion.  Further progress should use a stronger
structural constraint, especially the newly audited arbitrary outer-train multishear or
an improved coupled bad-center allocation, rather than rely on un-audited decimal
continuation.

**Final verdict:** **PASS** for the claimed proof-only floor

\[
\boxed{\liminf (q-k)/D\ge1.84365}
\]

at the stated full-core Type-II scope.