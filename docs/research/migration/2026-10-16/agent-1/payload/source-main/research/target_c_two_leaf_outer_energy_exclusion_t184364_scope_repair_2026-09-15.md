# Target C-II — scope repair for the `t<=1.84364` leaf-cap step

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_two_leaf_outer_energy_exclusion_t184364_2026-09-15.md`  
**Disposition:** **PASS AFTER REPAIR** at the stated proof-only full-core Type-II scope  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The `1.84364` theorem's Section 3.2 displays the strong-pair ratio at the rounded point
`C=1.055, U=0.528`.  That value is not the literal maximum over the contradiction box:
for fixed `C<K`, the ratio

\[
r(C,U)={C+U-K\over U}
=1+{C-K\over U}
\]

increases with `U`.  The theorem therefore needs the inherited lower bound on the
smallest leaf, rather than only the test value `U=0.528`.

The repair is short and strengthens the certificate.

---

## 1. Inherited smallest-leaf lower bound

The already-audited phase-resolved outer-occurrence theorem is valid throughout
`t<1.844` and gives

\[
z_V>0.616-o(1).
\]

Every complete train has at most two outer terminal occurrences of retained weight at
most one, so

\[
z_V\le2V+o(1).
\]

Hence every source sequence in the present `t<=1.84364` contradiction box satisfies

\[
\boxed{V>0.308-o(1).}
\tag{SR64.1}

The exact certificate uses the finite rounded value

\[
V_{min}=0.308.
\]

---

## 2. True worst center/larger-leaf ratio

On the main center interval,

\[
C<1.055<K={2\over\sqrt3}.
\]

For the center/larger-leaf pair, positive excess has ratio

\[
r_U={C+U-K\over U}.
\]

Since `C-K<0`,

\[
{\partial r_U\over\partial U}
=-{C-K\over U^2}>0.
\]

At fixed `C`, (SR64.1) and `C+U+V<=W_0=1.91267` give

\[
U\le W_0-C-0.308.
\]

Therefore

\[
r_U
\le
{W_0-0.308-K\over W_0-C-0.308}.
\tag{SR64.2}

The numerator is constant and positive, while the denominator decreases with `C`.
Thus the right side is maximized at the upper center endpoint `C=1.055`.  Put

\[
U_{max}=1.91267-1.055-0.308=0.54967.
\]

The corrected exact certificate checks

\[
\boxed{
{1.91267-0.308-K\over0.54967}
<\sqrt{20/29}.
}
\tag{SR64.3}

Numerically the left side is about `0.8186`, while the strong-branch threshold is about
`0.83045`.

For the smaller leaf,

\[
r_V=1+{C-K\over V}.
\]

Because `C-K<0` and `V<=U`, one has

\[
r_V\le r_U.
\]

Hence both center/leaf pairs lie in the physical `1/10` strong branch throughout the
whole main interval.

This replaces the weaker displayed ratio check in the theorem's Section 3.2.  All
subsequent capacity formulas are unchanged.

---

## 3. Common-center denominator guard

The common-center bad-weight estimate later replaces `U` by the adverse upper bound
`U_0=0.528`, producing denominator `C-U_0`.  The corrected certificate now checks
explicitly that generic center capacity excludes `C<=U_0`:

\[
0.528(1.91267-0.528)<0.90689964<E_{dom}.
\]

Thus

\[
\boxed{C>0.528}
\]

throughout the common-center step, so the denominator remains strictly positive and
replacing `U` by `U_0` is in the adverse direction.

---

## 4. No numerical conclusion changes

The repaired ratio still lies strictly below the strong-branch threshold, so the
`1/10` missing-pair payments used in the one-variable capacity `G(C)` remain valid.
The exact `1.84364` certificate continues to prove:

```text
h < 0.00033
W < 1.91267
E_dom > 0.90689964
U,V < 0.528
z > 2.2194
z_C,z_U,z_V > 0.704
good O-O pair weight in each leaf > 0.139
final outer-energy contradiction margin > 0.001255
```

**Final disposition:** the `t<=1.84364` theorem is valid after replacing its displayed
strong-ratio shortcut by (SR64.1)--(SR64.3) and using the explicit common-center
denominator guard.  C-II and Level I remain open.
