# Target C-II — low-detour endpoint forces a large loaded-unit-side set

**Date:** 2026-09-13  
**Status:** proof-only Type-II endpoint composition; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

On the audited Section-118 common-cap profile, the strict aggregate gap gives a
two-way endpoint split. The low-detour side of the split has a large population of
direct loaded-loaded unit contacts. No lower bound on the nonunit-side count `m` is
claimed.

Let

\[
T_0:=S_{118}+\alpha,
\qquad
\alpha:=\frac{\pi}{20}(2-\sqrt3),
\]

so that

\[
T_0=2.840685672933308\ldots .
\tag{1}
\]

The strict-gap and Section-118 moment bounds give

\[
\frac{q-k}{D}\ge T_0-o(1).
\tag{2}
\]

Put

\[
K_0:=\pi-T_0=0.300906980656484\ldots .
\tag{3}
\]

The audited Section-172 identity gives the branch-safe detour bound

\[
\liminf\frac{b-\operatorname{per}(F)}D
\ge\left(\frac{m+k}{D}-K_0\right)_+-o(1).
\tag{4}
\]

## Low-detour branch

Assume along a subsequence that

\[
\frac{m+k}{D}<K_0-o(1).
\tag{5}
\]

In Type II the audited loaded-hull theorem gives `e_{BB}=q-m`. Since
`q\ge(q-k)+k`, (2) and (5) imply

\[
\begin{aligned}
\frac{e_{BB}}D
 &=\frac{q-m}{D}\\
 &\ge T_0+\frac{k}{D}-\frac{K_0D-kD}{D}-o(1)\\
 &=T_0-K_0+2\frac{k}{D}-o(1).
\end{aligned}
\]

Therefore

\[
\boxed{
\liminf\frac{e_{BB}}D\ge E_0,
\qquad
E_0:=T_0-K_0=2T_0-\pi
 =2.539778692276824\ldots .}
\tag{6}
\]

Using the exact Type-II identity

\[
e_{BB}=Q+2k+u_B,
\]

the same branch also forces

\[
\boxed{\liminf\frac{Q+u_B}{D}\ge E_0.}
\tag{7}
\]

Thus if the old outer-walk detour is sublinear, at least `2.5397D-o(D)` loaded
force-hull sides are direct unit contacts, and the same amount of the exact ledger
currency `Q+u_B` remains to be carried by exceptional-face degree or outer-walk
surplus.

The branch also has `k/D<K_0+o(1)`, hence `d_H/D` and `s_Z/D` are each at most
`0.300907+o(1)`. This is a bounded-defect statement, not a vanishing-defect claim.

## Scope and non-implications

- The result is scoped to the Section-118 common-cap endpoint profile.
- No lower bound on `m` is inferred; the identity `G_D=m+2+X_D` does not support
  that inference from lower bounds on `G_D` and `X_D`.
- The split does not determine whether `Q` or `u_B` carries (7), and it does not
  force an exact unit equilateral triangle or a strict source-preserving diameter
  decrease.
- Contact-isolated source points remain retained, and no full-source affine-kernel
  claim is used.

**Classification:** proved candidate awaiting hostile audit; proof-only endpoint
composition. C-II remains open.
