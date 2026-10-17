# Target C-II — modern high-t bootstrap raises the Section-85 chamber surplus to `0.656552D`

**Date:** 2026-09-15
**Status:** proof-only source-level strengthening; theorem-state authority unchanged
**Scope:** canonical full-core/no-macroscopic-container Type-II branch after the hostile-audited exclusion of `t=(q-k)/D<=1.844`
**Dependencies:** scope-safe matched all-train gap `g=0.007707`; hostile-audited `t<=1.844` exclusion; canonical Sections 63, 67, 77, 80, and 85
**Certificate:** `research/verify_target_c_modern_high_t_interface_bootstrap_0656552.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current modern high-`t` chamber theorem derives the smaller Section-85 currency

\[
H_D:=(b-P_F)+(Q+2f)
\]

directly from the train slack `tau_D`, obtaining `H_D/D>=1.353825-o(1)` and chamber surplus `0.586223D-o(D)`.

There is a stronger composition from the same audited inputs. The larger exact interface currency

\[
J_D:=(b-P_F)+(Q+4f)
\]

satisfies

\[
\boxed{J_D=2T-P_F.}
\tag{MJ.1}

The modern all-train theorem controls `T-q/2`, while the hostile-audited low-`t` exclusion controls `q-k` and hence `q`. Feeding both into (MJ.1) first, then applying the canonical Section-85 inequality

\[
H_D\ge {3\over5}J_D,
\]

raises every first-order chamber constant.

The safe asymptotic package is

\[
\boxed{\liminf {J_D\over D}\ge2.527072,}
\tag{MJ.2}

\[
\boxed{\liminf {H_D\over D}\ge1.516243,}
\tag{MJ.3}

\[
\boxed{\liminf {A_{ch}-a_0Z_{ch}\over D}\ge0.656552,\qquad a_0={\sqrt3\over2},}
\tag{MJ.4}

\[
\boxed{\liminf {f\over D}\ge0.170767,}
\tag{MJ.5}

\[
\boxed{\liminf {m-R_4\over D}\ge2.328917,}
\tag{MJ.6}

\[
\boxed{\liminf {\Sigma_{ch}\over D}\ge2.192424,}
\tag{MJ.7}

and

\[
\boxed{\liminf {\Delta_2D^2-R_4\over D}\ge0.758121,\qquad \Delta_2={\pi\over2\sqrt3}.}
\tag{MJ.8}

The theorem does not close C-II. It strengthens the quantitative obligation carried by every remaining full-core Type-II survivor and makes the internal-boundary cancellation problem in the chamber Oler ledger more severe.

## 1. Modern all-train and high-t inputs

The scope-safe matched all-train theorem gives

\[
\boxed{\liminf {T-q/2\over D}\ge C_g:=2\sqrt{\Delta_2}+g,\qquad g=0.007707.}
\tag{MJ.9}

The hostile-audited phase-resolved remainder theorem excludes sufficiently large full-core survivors with

\[
t={q-k\over D}\le1.844.
\]

Hence every surviving sequence obeys

\[
\boxed{\liminf {q-k\over D}\ge1.844.}
\tag{MJ.10}

Since `k>=0`, this implies

\[
\boxed{\liminf {q\over D}\ge1.844.}
\tag{MJ.11}

Canonical Type-II near-disk geometry gives

\[
{P_F\over D}\to\pi.
\tag{MJ.12}

## 2. Bootstrap the larger exact interface currency first

Canonical train/outer-face bookkeeping gives the finite identity

\[
\boxed{J_D=(b-P_F)+(Q+4f)=2T-P_F.}
\tag{MJ.13}

Also

\[
2T=q+2\left(T-{q\over2}\right).
\]

Using (MJ.9), (MJ.11), and (MJ.12),

\[
\begin{aligned}
\liminf {J_D\over D}
&\ge1.844+2C_g-\pi\\
&=1.844+4\sqrt{\Delta_2}+0.015414-\pi\\
&=2.5270725738\ldots .
\end{aligned}
\tag{MJ.14}

The exact companion certificate proves (MJ.2).

## 3. Convert `J_D` into the Section-85 currency

Put `d=b-P_F>=0`. Then

\[
J_D=d+Q+4f,
\qquad
H_D=d+Q+2f.
\]

Every bounded nonquadrilateral face has degree at least five, so `Q>=f`. Therefore

\[
5H_D-3J_D=2(d+Q-f)\ge0,
\]

and

\[
\boxed{H_D\ge{3\over5}J_D.}
\tag{MJ.15}

Combining (MJ.14) and (MJ.15) gives

\[
\liminf {H_D\over D}\ge1.5162435443\ldots,
\]

proving (MJ.3). For comparison, the direct train-slack route on current main gives only `1.353825-o(1)`.

## 4. Chamber Oler surplus rises to `0.656552D`

Canonical Section 85 proves

\[
A_{ch}-a_0Z_{ch}\ge c_0H_D,
\qquad c_0={\sqrt3\over4},
\qquad a_0={\sqrt3\over2}.
\tag{MJ.16}

Therefore

\[
\begin{aligned}
\liminf {A_{ch}-a_0Z_{ch}\over D}
&\ge {\sqrt3\over4}{3\over5}
\left(1.844+4\sqrt{\Delta_2}+0.015414-\pi\right)\\
&=0.6565527138\ldots .
\end{aligned}
\tag{MJ.17}

The exact verifier proves the safe rounded coefficient `0.656552`, improving the current merged modern value `0.586223` by more than `0.0703D`.

## 5. Modern exceptional-face density

The exact stopped-train identity gives

\[
T-{q\over2}={q\over2}+2f-k.
\tag{MJ.18}

Every force-hull side joins distinct unit-separated source points, so `q<=P_F`; also `k>=0`. Hence

\[
T-{q\over2}\le {P_F\over2}+2f.
\]

Using (MJ.9) and `P_F/D->pi`,

\[
\boxed{\liminf {f\over D}\ge\sqrt{\Delta_2}-{\pi\over4}+{g\over2}=0.1707681434\ldots .}
\tag{MJ.19}

This proves the safe value (MJ.5).

## 6. Positive-core excess and chamber Oler-slack sum

Canonical Sections 63 and 67 give

\[
\boxed{m-R_4={P_F+H_D\over2}+1.}
\tag{MJ.20}

Thus

\[
\liminf {m-R_4\over D}
\ge {\pi\over2}+{3J_*\over10}
=2.3289180989\ldots,
\tag{MJ.21}

where

\[
J_*:=1.844+4\sqrt{\Delta_2}+0.015414-\pi.
\]

Let `P_ch` be total inactive-chamber perimeter and `s_ch` the chamber count. Canonical Section 77 gives

\[
P_{ch}\ge J_D,
\qquad s_{ch}\ge f.
\]

The chamber Oler-slack identity is

\[
\Sigma_{ch}
={A_{ch}-a_0Z_{ch}\over a_0}+{P_{ch}\over2}+s_{ch}.
\tag{MJ.22}

Since `c_0/a_0=1/2`,

\[
\begin{aligned}
\liminf {\Sigma_{ch}\over D}
&\ge {3J_*\over10}+{J_*\over2}
+\left(\sqrt{\Delta_2}-{\pi\over4}+{g\over2}\right)\\
&={4J_*\over5}+\sqrt{\Delta_2}-{\pi\over4}+{g\over2}\\
&=2.1924262025\ldots .
\end{aligned}
\tag{MJ.23}

The verifier proves (MJ.7).

## 7. Linear absolute rhombus-count deficit

The full-source Oler upper bound is

\[
n\le\Delta_2D^2+{\pi\over2}D+1.
\tag{MJ.24}

Since `m<=n`, equation (MJ.21) gives

\[
\boxed{\liminf {\Delta_2D^2-R_4\over D}\ge {3\over10}J_*=0.7581217721\ldots .}
\tag{MJ.25}

Multiplying by `a_0` gives

\[
\liminf {\pi D^2/4-a_0R_4\over D}\ge0.6565527138\ldots,
\tag{MJ.26}

matching the chamber-surplus coefficient. This reflects the common Section-85 currency; it is not an independent contradiction.

## 8. Frontier effect

Every remaining full-core/no-container Type-II survivor now simultaneously obeys

```text
J_D / D >= 2.527072 - o(1),
H_D / D >= 1.516243 - o(1),
f / D >= 0.170767 - o(1),
(m-R4) / D >= 2.328917 - o(1),
(A_ch-a0 Z_ch) / D >= 0.656552 - o(1),
P_ch / D >= 2.527072 - o(1),
Sigma_ch / D >= 2.192424 - o(1),
(Delta2 D^2-R4) / D >= 0.758121 - o(1).
```

The main remaining scalar obstruction is still internal-boundary cancellation. The single full-source Oler slack does not directly dominate `Sigma_ch`, because chamber partitioning creates `P_ch/2`. But the required local slack is now larger than the current merged modern package by a fixed linear amount.

The geometric alternative is also sharper: at least `0.170767D-o(D)` actual bounded exceptional faces must coexist with the near-disk rhombic phase system. Any theorem forcing a positive phase-conditioned width or diameter-load cost per such face would close the thin-chamber escape.

This theorem does not address the separate macroscopic-container/exterior-cap branch. No exact equilateral triangle or strict same-cardinality competitor is produced.

**Disposition:** proved proof-only modern high-`t` bootstrap of the larger Section-85 interface currency. C-II and Level I remain open.
