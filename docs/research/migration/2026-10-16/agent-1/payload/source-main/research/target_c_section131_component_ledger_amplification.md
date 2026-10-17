# Target C — Section 131 candidate: component-ledger amplification of the gap-diameter moment

**Date:** 2026-09-12
**Base:** canonical Section 75 plus proof-only Sections 125, 124/127, and repaired/audited Section 130
**Status:** proof-only research candidate; C-II remains open

Section 130 turns complement-gap area saturation into a global harmonic-cell diameter moment.  The canonical Section-75 component ledger contains a second, independent way to charge exactly the same diameter moment.  Keeping that charge before eliminating the loaded-side variable strengthens the endpoint scalar substantially.

The finite new inequality is

\[
\boxed{
q+m-k\ge \sum_r d_r-2,
}
\tag{131.1}
\]

where

- `q=|B|` is the loaded force-hull vertex count;
- `m` is the number of nonunit sides of the loaded force hull;
- `k=d_H+s_Z`;
- `d_r=diam(P_r)` is the Euclidean diameter of the harmonic attachment cell `P_r=conv(A_r)`.

It uses only the canonical component-diameter ledger and proof-only Section 125's Type-II identity `e_BB=q-m`.  No interface lower bound is used.

At the repaired Section-130 endpoint,

\[
\sum_r d_r\ge (S_*-o(1))D,
\qquad
S_*:=2.798596312209462\ldots .
\tag{131.2}
\]

Hence

\[
\boxed{
q+m-k\ge S_*D-o(D).
}
\tag{131.3}
\]

The Sections-124/127 payment, as already audited in Section 130, gives independently

\[
\boxed{
3q-2m-5k
\ge
(S_*+c_*)D-o(D),
}
\tag{131.4}
\]

with

\[
c_*={\pi\over4}(2-\sqrt3)
=0.210446803619233\ldots .
\tag{131.5}
\]

Twice (131.3) plus (131.4) eliminates `m` and yields

\[
\boxed{
5q-7k
\ge
(3S_*+c_*)D-o(D)
=8.60623574024762\ldots D-o(D).
}
\tag{131.6}
\]

Since `q=h+d_H` and `k=d_H+s_Z`, this is equivalently

\[
\boxed{
5h-2d_H-7s_Z
\ge
8.60623574024762\ldots D-o(D).
}
\tag{131.7}
\]

In particular every Section-130 endpoint countersequence must satisfy

\[
\boxed{
\liminf {h\over D}
\ge
{3S_*+c_*\over5}
=1.72124714804952\ldots .
}
\tag{131.8}
\]

This is not a C-II closure.  It is a new structural consequence of the complement-gap diameter moment: the endpoint cannot remain near the old universal diameter-edge floor `2 rho=1.47817...`; it is forced into a substantially denser diameter-thrackle regime.

---

## 131.1 Exact finite component-ledger inequality

Use the canonical Section-75 notation.  For every unloaded positive-contact component `I_r`, let

\[
\delta_r
\]

be its contact-graph diameter and let

\[
d_r=\operatorname{diam}(P_r),
\qquad
P_r=\operatorname{conv}(A_r).
\]

Canonical harmonic localization gives

\[
\boxed{d_r\le\delta_r+2.}
\tag{131.9}
\]

Summing over the `c_I` unloaded components,

\[
\boxed{
\sum_r d_r
\le
\sum_r\delta_r+2c_I.
}
\tag{131.10}
\]

Canonical Section 75 gives the exact all-phase component ledger

\[
\boxed{
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C,
}
\tag{131.11}
\]

where `R_I,s_B>=0`.  Therefore

\[
\sum_r\delta_r
\le
6+e_{BB}+2s_C-3k.
\tag{131.12}
\]

Insert (131.12) into (131.10):

\[
\sum_r d_r
\le
6+e_{BB}+2s_C-3k+2c_I.
\tag{131.13}
\]

Now use the two exact Type-II identities from proof-only Section 125:

\[
\boxed{e_{BB}=q-m,}
\tag{131.14}
\]

and

\[
\boxed{c_I+s_C=m+k-2.}
\tag{131.15}
\]

Equation (131.15) gives

\[
s_C=m+k-2-c_I.
\]

Substitute this and (131.14) into (131.13):

\[
\begin{aligned}
\sum_r d_r
&\le
6+(q-m)+2(m+k-2-c_I)-3k+2c_I\\
&=q+m-k+2.
\end{aligned}
\]

Thus

\[
\boxed{q+m-k\ge\sum_r d_r-2,}
\]

proving (131.1).

The cancellation of `c_I` is exact.  Section 75's asymptotic bound `c_I=O(D^{2/3})` is not needed for (131.1).

---

## 131.2 Insert the repaired Section-130 diameter moment

The binding Section-130 limit repair and hostile audit prove, at the Section-118 endpoint/common-cap branch,

\[
\liminf {1\over D}\sum_r d_r
\ge S_*,
\tag{131.16}
\]

where

\[
S_*
=\mu_*+M(\theta_*)
=2.798596312209462\ldots .
\tag{131.17}
\]

Here

\[
\mu_*=0.9762439137425688\ldots
\]

is the wrapping carrier diameter coefficient and

\[
M(\theta_*)=1.822352398466893\ldots
\]

is the complement-gap chord moment.  No exact full-gap limiting cell is assumed; the repaired theorem uses approximate cap saturation and then a finite-gap/diagonal limit.

Combining (131.1) with (131.16) gives (131.3):

\[
q+m-k\ge S_*D-o(D).
\]

---

## 131.3 Eliminate the loaded-side variable against the return payment

The corrected Sections-124/127/130 chain gives

\[
3(h-s_Z)-2s_C
\ge
(S_*+c_*)D-o(D),
\tag{131.18}
\]

with `c_*` from (131.5).

Use

\[
h-s_Z=q-k
\]

and, from (131.15) plus canonical `c_I=o(D)`,

\[
s_C=m+k+o(D).
\tag{131.19}
\]

Then (131.18) becomes

\[
\boxed{
3q-2m-5k
\ge
(S_*+c_*)D-o(D),
}
\tag{131.20}
\]

which is (131.4).

Multiply (131.3) by two and add (131.20):

\[
\begin{aligned}
2q+2m-2k
&\ge 2S_*D-o(D),\\
3q-2m-5k
&\ge (S_*+c_*)D-o(D).
\end{aligned}
\]

The `m` terms cancel, giving

\[
5q-7k
\ge
(3S_*+c_*)D-o(D).
\]

Numerically,

\[
3S_*+c_*
=8.60623574024762\ldots .
\tag{131.21}
\]

Finally

\[
q=h+d_H,
\qquad
k=d_H+s_Z,
\]

so

\[
5q-7k
=5h-2d_H-7s_Z.
\]

This proves (131.7).  Since `d_H,s_Z>=0`, (131.8) follows.

---

## 131.4 Why this is stronger than the Section-130 elimination

Section 130 used the loaded contact-degree cap to obtain

\[
q+2m\ge S_*D-o(D)
\]

and combined it with (131.20), giving

\[
4q-5k\ge(2S_*+c_*)D-o(D).
\]

The new component-ledger inequality is

\[
q+m-k\ge S_*D-o(D).
\]

It charges every unit of harmonic-cell Euclidean diameter through the actual component graph-diameter budget before the pinned/contact variables are eliminated.  The exact cancellation of `c_I` makes that charge substantially sharper at the endpoint.

The improvement is therefore structural rather than a recalculation of the Section-118 carrier decimal.

---

## 131.5 Hostile scope checks

1. **No withdrawn Type-II interface floor.**  The proof does not use the rejected `0.6676585...` nonmatching/interface claim or the rejected unconditional `q-k>=1.9046256...D` claim.  It is compatible with the corrected `1.637562...` loaded-hull report but does not depend on it.
2. **No source deletion.**  Contact-isolated source points remain in the full source.  The component variables refer only to the canonical nonisolated positive-contact core, exactly as in Section 75.
3. **No full-source ZR/ZF extension.**  No affine-kernel statement is applied to isolated coordinates.
4. **Finite inequality first.**  Equation (131.1) is finite.  The only asymptotic step is insertion of the repaired Section-130 endpoint moment and `c_I=o(D)` when rewriting `s_C` in (131.19).
5. **Section-125 dependency.**  The identities `e_BB=q-m` and `c_I+s_C=m+k-2` are proof-only Type-II inputs.  Therefore Section 131 is proof-only and cannot be promoted independently of Section 125.
6. **Section-130 dependency.**  The endpoint constant uses the repaired, hostile-audited version of Section 130, not its rejected exact-equality shortcut.
7. **No closure claim.**  The resulting high diameter-edge density remains algebraically feasible.  A closing theorem must couple this dense diameter thrackle to the loaded side sequence, harmonic-cell interfaces, or global minimality.

---

## 131.6 New live endpoint

The Section-118 endpoint/common-cap countersequence, if it exists, must simultaneously satisfy

\[
{h\over D}\ge1.7212471480\ldots-o(1),
\]

\[
q+m-k\ge2.7985963122\ldots D-o(D),
\]

and

\[
3q-2m-5k\ge3.0090431158\ldots D-o(D).
\]

Thus the next high-value attack is no longer the old minimum-density diameter-thrackle regime.  It is the interaction of a **dense diameter thrackle** with the Type-II near-circular loaded boundary and the gap-spanning harmonic cells forced by Section 130.

**Theorem state:** unchanged.  This is proof-only pending independent hostile audit and lifecycle review.
