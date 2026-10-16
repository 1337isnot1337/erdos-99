<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f25ba4a7194c28483ebae5257513d6424a19a8c4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_wo145_lossless_global_propagation_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "bf0b08073e4d1a6bde6cdcde5f64c229a8278735287c604051b4288bb9131e42"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — WO145 lossless propagation through the C-II ledgers

**Date:** 2026-09-14  
**Target:** Target C-II canonical full-core Type-II branch  
**Claim class:** proof-only propagation of WO145  
**External input:** none  
**Computation:** exact-rational Section-171 endpoint certificate

## LEVEL I STATUS

`STILL OPEN`

The weighted-overlap theorem WO145 proves the proof-only atomic train gain

\[
 g:=\eta_{grid}=0.00145.
\]

This note propagates that gain through the audited Section-171 orbit/detour envelope and
then uses the exact lossless train identity before splitting singleton and rhombic
branches.  Keeping the Section-171 lower bound on `U=q-k` is substantially stronger
than falling back to the older difference-body lower bound on `q`.

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad s_2=\sqrt{\Delta_2},
\qquad
C_{146}={4\over9}(\pi+s_2).
\]

---

## 1. Section-171 endpoint with `g=0.00145`

Audited Section 171 reduces every Type-II subsequential limit

\[
t=\lim{q-k\over D},
\qquad
\delta=\lim{b-P_F\over D}\ge0
\]

to

\[
F_t(\delta)=
10t-5\pi-5\delta
+\left(81(\pi+\delta)^2\delta\right)^{1/3}
-{8\Delta_2\over9t/2-2\pi-2\delta}
\ge0.
\tag{W145.1}
\]

With train gain `g`, the feasible detour interval is

\[
0\le\delta\le
{{9\over2}(t-C_{146})-g\over2}.
\tag{W145.2}
\]

Take

\[
g=0.00145,
\qquad
\varepsilon_{145}=0.0015914,
\qquad
t_{145}=C_{146}+\varepsilon_{145}.
\tag{W145.3}
\]

The right endpoint is exactly

\[
\delta_{145}=0.00285565.
\tag{W145.4}
\]

The exact-rational certificate proves that `F_{t145}` is increasing throughout the
feasible detour interval, while

\[
F_{t_{145}}(\delta_{145})<0
\]

with outward-rounding margin exceeding `1.5e-5`.  Section 171 also gives strict
monotonicity in `t`.  Hence

\[
\boxed{
\liminf {q-k\over D}
\ge t_{145}
=1.821104937979444\ldots .
}
\tag{W145.5}
\]

The unchanged scalar equation has its first numerical zero at
`epsilon=0.00159145276455...`, so the displayed endpoint is deliberately below the
method root.

---

## 2. Lossless total train defect

Let `T` be the complete stopped-train count, `T_R` the non-singleton rhombic-train
count, and `S=T-T_R` the singleton count.  Put

\[
\rho_{rec}=2S,
\qquad
\sigma_R=2T_R-4\sqrt{R_4}.
\]

Exactly,

\[
\boxed{
\rho_{rec}+\sigma_R=2T-4\sqrt{R_4}.
}
\tag{W145.6}
\]

WO145 gives

\[
{T-q/2\over D}\ge2s_2+g-o(1),
\tag{W145.7}
\]

so

\[
2T\ge q+4s_2D+2gD-o(D).
\]

Since `q=(q-k)+k>=q-k`, equation (W145.5) applies.  Type-II rhombic saturation gives

\[
{\sqrt{R_4}\over D}\to s_2.
\]

Therefore

\[
\boxed{
\liminf {\rho_{rec}+\sigma_R\over D}
\ge L_{145}:=t_{145}+2g
=1.824004937979444\ldots .
}
\tag{W145.8}
\]

This is the correct lossless train split.  It is much stronger than the fallback
coefficient obtained by replacing `q-k` with a generic difference-body bound.

---

## 3. Singleton-versus-rhombic dichotomy

From (W145.8), after subsequence extraction at least one of

\[
\rho_{rec}\ge\left({L_{145}\over2}-o(1)\right)D,
\qquad
\sigma_R\ge\left({L_{145}\over2}-o(1)\right)D
\]

holds.  Since `rho_rec=2S`, either

\[
\boxed{
S\ge0.456001234494861\ldots D-o(D),
}
\tag{W145.9}
\]

or

\[
\boxed{
\sigma_R\ge0.912002468989722\ldots D-o(D).
}
\tag{W145.10}
\]

On the rhombic branch, the exact rationalization

\[
M_R={\sigma_R\over8}
\left(4\sqrt{R_4}+{\sigma_R\over2}\right)
\]

gives

\[
\boxed{
\liminf {M_R\over D^2}
\ge0.486240097020440\ldots .
}
\tag{W145.11}
\]

Thus the surviving full-core geometry must carry either a linear population of nearly
half a diameter's worth of singleton trains or almost one full `D` of rhombic
isoperimetric slack, the latter corresponding to a macroscopic quadratic loss of
rhombic crossing capacity.

---

## 4. Post-endpoint scalar floor

The exact post-endpoint identity is

\[
\begin{aligned}
\mu_DD
={}&{2P_F+2\sqrt{R_4}\over5}
+m_B+{2\over5}(Q-f)+{2\over5}(b-P_F)\\
&+{1\over10}\rho_{rec}
+{1\over10}\sigma_R
-2c_I-4.
\end{aligned}
\tag{W145.12}
\]

The displayed defect currencies are nonnegative, while

\[
P_F/D\to\pi,
\qquad
R_4/D^2\to\Delta_2,
\qquad
c_I/D\to0.
\]

Using the **total** train-defect floor (W145.8), rather than only one rhombic term,
therefore gives

\[
\boxed{
\liminf\mu_D
\ge
{2\pi+2s_2\over5}+{L_{145}\over10}
=1.819962677979444\ldots .
}
\tag{W145.13}
\]

No universal upper bound currently known for `mu_D` contradicts this value, so it is a
stronger scalar reduction rather than C-II closure.

---

## 5. Bridge-subtracted and detour-free forms

Split singleton trains as

\[
S=S_o+S_E,
\]

where `S_o` has no bounded-exceptional terminal incidence and `S_E` has at least one.
The audited bridge payment gives

\[
2S_o\le b-P_F+o(D).
\]

Subtracting only that paid population from (W145.8) yields

\[
\boxed{
\sigma_R+2S_E+(b-P_F)
\ge(L_{145}-o(1))D.
}
\tag{W145.14}
\]

The exact detour-free elimination is algebraic in the train gain and gives

\[
\boxed{
{\sigma_R+2S_E\over D}
\ge
c_{DF,145}
+{5\over2}{k\over D}
+{Q-f\over D}
-o(1),
}
\tag{W145.15}
\]

where

\[
\boxed{
c_{DF,145}
=s_2-\frac\pi4+\frac52g
=0.170539643466509\ldots .}
\tag{W145.16}
\]

Even after discarding the positive `k` and `Q-f` terms, every detour-free survivor has
at least one of

\[
\boxed{
\sigma_R\ge0.0852698217332545\ldots D-o(D)
}
\tag{W145.17}
\]

or

\[
\boxed{
S_E\ge0.0426349108666273\ldots D-o(D).
}
\tag{W145.18}
\]

For any fixed two sufficiently narrow projective windows, the exceptional-singleton
incidence theorem correspondingly becomes

\[
\boxed{
\sigma_R+11(Q-f)+20T_{off}
\ge c_{DF,145}D+{5\over2}k-o(D).
}
\tag{W145.19}
\]

---

## 6. Exceptional-face and chamber-interface floors

The exact all-train ledger and `P_F/D->pi` give

\[
T-{q\over2}\le {P_F\over2}+2f.
\]

Therefore WO145 forces

\[
\boxed{
\liminf {f\over D}
\ge s_2-\frac\pi4+{g\over2}
=0.167639643466509\ldots .
}
\tag{W145.20}
\]

Since every bounded exceptional face has degree at least five,

\[
\boxed{
\liminf {4f+Q\over D}
\ge0.838198217332545\ldots .
}
\tag{W145.21}
\]

Define

\[
J=(b-P_F)+(Q+4f)=2T-P_F.
\]

Using `q>=q-k`, WO145, (W145.5), and `P_F/D->pi`,

\[
\boxed{
\liminf {J\over D}
\ge j_{145}:=t_{145}+4s_2+2g-\pi
=2.491663511845481\ldots .
}
\tag{W145.22}
\]

The exact chamber decomposition

\[
\Sigma_{ch}=J+a+L_{add}+R_F
\]

then gives

\[
\boxed{
\liminf {\Sigma_{ch}\over D}
\ge2.491663511845481\ldots .
}
\tag{W145.23}
\]

As in the corrected chamber audit, this large raw slack contains mandatory boundary
credit and cannot be compared directly with the full-source Oler slack.

---

## 7. Exact `H` bootstrap and linear rhombus deficit

The exact identity

\[
H={J\over2}+(q-k)-{P_F\over2}
\]

gives

\[
\boxed{
\liminf {H\over D}
\ge h_{145}:={j_{145}\over2}+t_{145}-{\pi\over2}
=1.496140367107289\ldots .
}
\tag{W145.24}
\]

Canonical Section 85 therefore yields

\[
\boxed{
\liminf {A_{ch}-a_0Z_{ch}\over D}
\ge {\sqrt3\over4}h_{145}
=0.647847782771144\ldots,
}
\tag{W145.25}
\]

and the full-source count comparison gives

\[
\boxed{
\liminf {\Delta_2D^2-R_4\over D}
\ge {h_{145}\over2}
=0.748070183553644\ldots .
}
\tag{W145.26}
\]

The positive-core population identity

\[
m-R_4={P_F+H\over2}+1
\]

gives

\[
\boxed{
\liminf {m-R_4\over D}
\ge {\pi+h_{145}\over2}
=2.318866510348541\ldots .
}
\tag{W145.27}
\]

---

## 8. Corrected residual budget

The exact corrected cap remains

\[
R_F+\Sigma_{ext}
<{P_K\over2}+P_F-q-{\delta_K+E_4\over a_0}.
\]

Using `q>=q-k`, `P_K,P_F<=pi D`, and (W145.5),

\[
\boxed{
\limsup {R_F+\Sigma_{ext}\over D}
\le {3\pi\over2}-t_{145}
=2.891284042405245\ldots .
}
\tag{W145.28}
\]

The first-order gap between mandatory interface complexity and genuine residual
allowance continues to move in the favorable direction, but it is not yet a
contradiction.

---

## 9. Current full-core frontier

At proof-only scope every full-core Type-II survivor now obeys all of the following:

```text
(q-k)/D >= 1.8211049379... - o(1),
(rho_rec+sigma_R)/D >= 1.8240049379... - o(1),
mu_D >= 1.8199626779... - o(1),
f/D >= 0.1676396434... - o(1),
J/D >= 2.4916635118... - o(1),
H/D >= 1.4961403671... - o(1),
(Delta_2 D^2-R_4)/D >= 0.7480701835... - o(1).
```

And, after a subsequence split, either

```text
S >= 0.4560012344 D - o(D)
```

or

```text
sigma_R >= 0.9120024689 D - o(D),
M_R >= 0.4862400970 D^2 - o(D^2).
```

These are much stronger geometric populations than the pre-WO145 package.  The
remaining closing theorem must use the actual geometry of singleton trains,
exceptional-face incidences, or the large quadratic rhombic crossing deficit; further
scalar retuning alone is not a plausible route to C-II closure.

The Section-171 sign certificate is
`research/verify_target_c_wo145_global_propagation.py`.

**Disposition:** proof-only WO145 propagation.  C-II and Level I remain open.
