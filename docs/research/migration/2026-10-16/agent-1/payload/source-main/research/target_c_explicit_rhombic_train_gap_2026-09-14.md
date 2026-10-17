# Erdős Problem #99 — explicit rhombic-train gap beyond the Mantel endpoint

**Date:** 2026-09-14
**Repository base:** `0c32f1aa`
**State version:** `2026-09-14.audit.51`
**Run type:** quantitative closing-proof reduction
**Target:** Target C-II, canonical full-core Type-II branch
**Claim class:** proof-only candidate; theorem-state authority unchanged
**External literature:** no new import; reuses the already-audited quantitative robust-grid argument in §§166/168
**Computation:** non-load-bearing arithmetic verification only

## LEVEL I STATUS

`STILL OPEN`

The preceding sublinear-train-slack exclusion proved only that the rhombic train
isoperimetric slack is `Omega(D)` with a non-explicit coefficient. This note makes that
gap explicit.

Let

\[
R_4=\#\{\text{strict-rhombus faces}\},
\qquad
B_4=\#\{\text{strict-rhombus boundary occurrences}\},
\]

and let

\[
T_R:=B_4/2
\]

be the number of non-singleton stopped trains of the strict-rhombus complex. Put

\[
\sigma_R:=B_4-4\sqrt{R_4}=2T_R-4\sqrt{R_4}\ge0.
\tag{RG.1}
\]

Then every canonical full-core Type-II survivor sequence satisfies

\[
\boxed{
\liminf_{D\to\infty}{T_R\over D}
\ge 2\sqrt{\Delta_2}+0.0004,
}
\tag{RG.2}
\]

and therefore

\[
\boxed{
\liminf_{D\to\infty}{\sigma_R\over D}\ge0.0008.
}
\tag{RG.3}
\]

Here

\[
\Delta_2={\pi\over2\sqrt3}.
\]

Equivalently, with rhombic-train Mantel deficit

\[
M_R:={T_R^2\over4}-R_4,
\]

\[
\boxed{
\liminf {M_R\over D^2}
\ge 0.0001\left(4\sqrt{\Delta_2}+0.0004\right)
=0.0003809651227455\ldots .
}
\tag{RG.4}
\]

This is a quantitative strengthening of `research/target_c_sublinear_train_slack_exclusion_2026-09-14.md`.

## 1. Two train counts and the exact singleton identity

The audited §142 stopped-train decomposition includes isolated positive-contact edges as
singleton trains. Denote its total number of trains by `T`. It has the exact endpoint
handshake

\[
b+4f+Q=2T.
\tag{RG.5}
\]

By contrast, `T_R=B_4/2` counts only trains that contain at least one strict rhombus.
If `S` is the number of singleton stopped trains, then exactly

\[
\boxed{T=T_R+S.}
\tag{RG.6}
\]

Consequently the recipient-capacity slack introduced in the post-endpoint split,

\[
\rho_{\rm rec}:=b+4f+Q-B_4,
\]

has the exact interpretation

\[
\boxed{\rho_{\rm rec}=2S.}
\tag{RG.7}
\]

There is therefore no contradiction between §142's equality (RG.5) and Section 85's
inequality `B_4<=b+4f+Q`: their difference is precisely the singleton train population.
Moreover the old train-boundary slack decomposes as

\[
\boxed{
\tau_D:=q-k+2f-2\sqrt{R_4}
=S+{\sigma_R\over2}.
}
\tag{RG.8}
\]

This exact bookkeeping will be useful below and in subsequent singleton-train attacks.

## 2. Rhombic trains satisfy the §142 crossing-measure hypotheses

Form the crossing graph `G_R` whose vertices are the `T_R` non-singleton rhombic trains
and whose edges are their strict-rhombus crossings. Canonical Theorem 10.6 gives:

1. `G_R` is simple;
2. `G_R` is triangle-free;
3. `e(G_R)=R_4` exactly.

The full-core asymptotics give

\[
{R_4\over D^2}\to\Delta_2.
\tag{RG.9}
\]

Mantel therefore gives `T_R>=2sqrt(R_4)=Theta(D)`, while Section 85 gives
`2T_R=B_4<=b+4f+Q=O(D)`. Hence

\[
T_R=\Theta(D).
\tag{RG.10}
\]

Let `nu_D` be the empirical projective direction probability measure on these `T_R`
rhombic trains. Pass to an arbitrary subsequence on which

\[
{T_R\over D}\to x_R,
\qquad
\nu_D\Rightarrow\nu.
\tag{RG.11}
\]

Let `s_R` be the total atomic mass of `nu`.

The canonical angular-defect bound applies to every strict rhombus, independent of
whether singleton contact-edge trains are retained in the vertex set. Thus, for each
fixed `epsilon>0`, only `o(D^2)=o(T_R^2)` crossings have projective angular separation
at least `pi/3+epsilon`. Every normalized crossing-measure limit is therefore supported
on

\[
\{(\phi,\psi):\psi-\phi\equiv\pm\pi/3\pmod\pi\}.
\tag{RG.12}
\]

Because `G_R` is simple, its normalized crossing measure is dominated by the product
measure `nu x nu`. The exact `+-pi/3` relation has product mass only at atoms. Group
those atoms into the three-point projective orbits

\[
\phi\mapsto\phi+\pi/3\pmod\pi.
\]

If `M_r` is the absolute atomic train mass of orbit `r` in `D` normalization and
`E_r` its limiting strict-rhombus crossing mass, weighted Mantel gives

\[
E_r\le {M_r^2\over4},
\qquad
\sum_r E_r=\Delta_2,
\qquad
\sum_r M_r=A_R:=x_Rs_R.
\tag{RG.13}
\]

In particular

\[
A_R\ge2\sqrt{\Delta_2}.
\tag{RG.14}
\]

These are exactly the inputs used before the exposed-hull propagation step in audited
§§166/168.

## 3. The explicit §168 robust-grid gap transfers verbatim

The proof of audited §168.1--§168.4 uses only the data in (RG.13):

- the exact total crossing mass `Delta_2`;
- the product-measure orbit capacities `E_r<=M_r^2/4`;
- finite triangle-free Mantel stability inside a dominant orbit;
- the fact that two trains from one shrinking atom window cannot cross;
- actual strict-rhombus pseudosegment geometry; and
- the robust opposite-corner source-diameter contradiction.

The exposed-hull inequality `q/T<=2(1-s)` is used only later in §168.5 to propagate the
atomic gain into the full stopped-train boundary ledger. It is not used to prove the
atomic gain itself.

Therefore the entire quantitative contradiction of §168.1--§168.4 applies to `G_R`.
With the same conservative constant,

\[
\boxed{
A_R=x_Rs_R\ge2\sqrt{\Delta_2}+0.0004.
}
\tag{RG.15}
\]

Since `s_R<=1`,

\[
x_R\ge A_R\ge2\sqrt{\Delta_2}+0.0004.
\tag{RG.16}
\]

The starting subsequence in (RG.11) was arbitrary. This proves (RG.2).

## 4. Explicit train-isoperimetric and Mantel gaps

From (RG.1), (RG.2), and (RG.9),

\[
\begin{aligned}
\liminf {\sigma_R\over D}
&=\liminf\left(2{T_R\over D}-4{\sqrt{R_4}\over D}\right)\\
&\ge2\left(2\sqrt{\Delta_2}+0.0004\right)-4\sqrt{\Delta_2}\\
&=0.0008.
\end{aligned}
\]

This proves (RG.3).

The exact rationalization identity is

\[
\sigma_R={8M_R\over T_R+2\sqrt{R_4}},
\qquad
M_R={\sigma_R(T_R+2\sqrt{R_4})\over8}.
\tag{RG.17}
\]

All factors are nonnegative, so (RG.2)--(RG.3) and (RG.9) give

\[
\liminf {M_R\over D^2}
\ge {0.0008\over8}
\left(4\sqrt{\Delta_2}+0.0004\right),
\]

which is (RG.4).

Thus every sufficiently large full-core survivor is not merely separated from the
rhombic Mantel endpoint: it loses at least about `0.000380965 D^2` possible rhombic
train crossings.

## 5. Explicit improvement of the post-endpoint scalar floor

The exact proof-only post-endpoint identity is

\[
\begin{aligned}
\mu_DD
={}&{2P_F+2\sqrt{R_4}\over5}
+m_B+{2\over5}(Q-f)+{2\over5}(b-P_F)\\
&+{1\over10}\rho_{\rm rec}
+{1\over10}\sigma_R
-2c_I-4.
\end{aligned}
\tag{RG.18}
\]

All five defect currencies are nonnegative, while

\[
{P_F\over D}\to\pi,
\qquad
{R_4\over D^2}\to\Delta_2,
\qquad
{c_I\over D}\to0.
\]

Hence (RG.3) gives the explicit strengthening

\[
\boxed{
\liminf\mu_D
\ge\mu_{\rm TC}+0.00008,
}
\tag{RG.19}
\]

where

\[
\mu_{\rm TC}={2\pi+2\sqrt{\Delta_2}\over5}.
\]

This does not close the full-core branch, but it replaces the previous non-explicit
post-endpoint separation by a concrete numerical gap.

## 6. Explicit improvement of the chamber/train budget

Canonical Section 85 gives

\[
A_{ch}-a_0Z_{ch}
\ge {3c_0\over5}(B_4-P_F),
\qquad
a_0={\sqrt3\over2},\quad c_0={\sqrt3\over4}.
\tag{RG.20}
\]

Using

\[
B_4=4\sqrt{R_4}+\sigma_R
\]

and (RG.3),

\[
\boxed{
\liminf{A_{ch}-a_0Z_{ch}\over D}
\ge\beta_{tr}+{3c_0\over5}(0.0008),
}
\tag{RG.21}
\]

with

\[
\beta_{tr}:={3\sqrt3\over20}
\left(4\sqrt{\Delta_2}-\pi\right).
\]

The explicit added chamber surplus is

\[
{3c_0\over5}(0.0008)
=0.0002078460969082\ldots .
\tag{RG.22}
\]

Using the exact chamber Oler identity

\[
A_{ch}-a_0Z_{ch}
=a_0\Sigma_{ch}-c_0P_{ch}-a_0s,
\]

this contributes an additional

\[
\boxed{0.00024D-o(D)}
\tag{RG.23}
\]

to the lower bound for total chamber Oler slack `Sigma_ch` beyond the old train-floor
baseline.

## 7. Scope and next target

This note does not close C-II. It does, however, remove three ambiguities:

1. the recipient vacancy is exactly twice the singleton-train population;
2. the rhombic train graph has an explicit linear isoperimetric gap and explicit
   quadratic Mantel deficit; and
3. the post-endpoint scalar and chamber-surplus gaps are now explicit.

The next useful attack is to exploit the two exact sources of train excess separately:

\[
T-2\sqrt{R_4}
=S+{\sigma_R\over2}.
\]

The audited all-stopped-train atomic theorem controls the left side strongly, while
(RG.3) controls the second term. A large residual singleton population means a linear
family of positive-contact edges that lie in no strict rhombus; a large `sigma_R`
means a quadratic loss in rhombic crossing capacity. Those two mechanisms should be
charged against different geometric ledgers rather than merged back into one scalar.
