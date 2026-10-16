# Target C-II — the no-TT return branch is fixed-wide at full near-shore density

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural/metric strengthening; no canonical promotion claimed  
**Scope:** the no-positive-density-TB1 near-full exact-force shore through `t=(q-k)/D<=1.8687`, in the no-TT branch  
**Dependencies:** terminal-or-wide-return dichotomy; ordered bilateral narrow-pair capacity; coupled host transverse margin; full-source diameter-midpoint localization  
**Certificate:** `research/verify_target_c_high_t_full_density_wide_return_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The terminal-or-wide-return theorem gives, when no terminal-terminal force cell occurs, one force lane which returns to the opposite physical host at every center. Its same-host return arc yields a projective-gap lower bound which is strongest near the beginning of the ordered population and weakens toward the end.

Independently, the ordered bilateral theorem makes the projective gap of a near-antipodal force pair grow at least `2 delta_D` per retained center. That lower bound is weakest near the beginning and strengthens toward the end.

The two ramps are complementary. Combining them removes the half-population loss from the previous return theorem:

\[
\boxed{
\text{if TT is absent, every center in the near-full population satisfies}
\quad
\eta_s\ge\rho_F-o(1),
}
\]

where

\[
\boxed{
\rho_F:={c_Hc\over1+c_H}
=7.05474558522\ldots\times10^{-6}\ \text{radians}.
}
\]

Thus the full population

\[
\boxed{
N>\left({c\over2}-o(1)\right)D
=(1.13\times10^{-5}-o(1))D
}
\]

is a fixed-aperture exact-force family. This doubles the guaranteed fixed-wide cardinality from the return theorem's `c/4` prefix while also improving its aperture from `5.12816e-6` to `7.05475e-6` radians.

Together with the terminal branch, the paired obstruction now has the sharper dichotomy

\[
\boxed{
\operatorname{diam}(T_m\cap S)\ge(c_H-o(1))D
\quad\text{or}\quad
(c/2-o(1))D\text{ exact-force cells are uniformly fixed-wide.}
}
\]

---

## 1. No-TT return geometry

Use the same notation as the terminal-or-wide-return theorem. The retained centers are

\[
i_1<i_2<\cdots<i_N<k,
\qquad
N>\left({c\over2}-o(1)\right)D,
\qquad
c={113\over5{,}000{,}000}.
\tag{FW.1}
\]

If TT is absent, after interchanging the physical hosts if necessary, the `B`-born force lane satisfies

\[
y_s^B\in Q^A
\qquad(1\le s\le N).
\tag{FW.2}
\]

The mate birth `x_s^A` and this partner `y_s^B` lie on the same physical host `A`, and the boundary arc from `x_s^A` to `y_s^B` contains all later mate births. The host-arc projection lemma therefore gives

\[
|x_s^A-y_s^B|
\ge(c_H-o(1))(N-s).
\tag{FW.3}
\]

Let

\[
\eta_s=d_{\mathbb{RP}^1}([d_s^A],[d_s^B])
\tag{FW.4}
\]

be the force-pair projective gap. Put

\[
\gamma_H:=\arcsin c_H.
\tag{FW.5}
\]

For any center with `eta_s<gamma_H/2`, the ordinary force pair must be in the near-antipodal realization, and midpoint localization gives

\[
|x_s^A-y_s^B|
\le2L_D+D\sin{\eta_s\over2},
\qquad L_D=o(D).
\tag{FW.6}
\]

Combining (FW.3)--(FW.6),

\[
\boxed{
\sin{\eta_s\over2}
\ge c_H{N-s\over D}-o(1).
}
\tag{FW.7}
\]

Using `arcsin z>=z` for `z>=0`, this implies the simpler linear ramp

\[
\boxed{
\eta_s
\ge2c_H{N-s\over D}-o(1)
}
\tag{FW.8}
\]

whenever `eta_s<gamma_H/2`. If `eta_s>=gamma_H/2`, every final bound below is automatic because the constants there are much smaller than `gamma_H/2`.

---

## 2. Bilateral birth order supplies the complementary ramp

The ordered bilateral theorem applies to these same exact-force centers. Let

\[
\delta_D=2\arcsin{1\over2D}.
\tag{FW.9}
\]

For any center satisfying `eta_s<gamma_H/2`, the `gamma_H/2`-narrow centers form an initial segment and their gaps increase by at least `2 delta_D` per retained interface. Hence

\[
\boxed{
\eta_s\ge2(s-1)\delta_D.
}
\tag{FW.10}
\]

Since

\[
\delta_D\ge{1\over D},
\tag{FW.11}
\]

we get

\[
\boxed{
\eta_s\ge2{s-1\over D}.
}
\tag{FW.12}
\]

Again, if `eta_s>=gamma_H/2`, the final fixed-width conclusion is automatic.

---

## 3. The two ramps have a uniform positive minimum

Put

\[
x_s:={s-1\over D},
\qquad
n_D:={N\over D}.
\tag{FW.13}
\]

Equations (FW.8) and (FW.12) give, for every center after absorbing the trivial large-gap case,

\[
\eta_s
\ge
2\max\{x_s,\ c_H(n_D-x_s)-O(D^{-1})\}-o(1).
\tag{FW.14}
\]

For any real `x` and `n>0`,

\[
\max\{x,c_H(n-x)\}
\ge {c_Hn\over1+c_H}.
\tag{FW.15}
\]

Indeed, the two affine functions meet at

\[
x={c_Hn\over1+c_H},
\]

where their common value is exactly the right side of (FW.15), and their maximum is no smaller elsewhere.

Using

\[
n_D\ge{c\over2}-o(1),
\tag{FW.16}
\]

we obtain uniformly for every retained center

\[
\boxed{
\eta_s
\ge {c_Hc\over1+c_H}-o(1).
}
\tag{FW.17}
\]

Define

\[
\boxed{
\rho_F:={c_Hc\over1+c_H}.
}
\tag{FW.18}
\]

With

\[
c_H=0.453819885927\ldots,
\qquad
c=2.26\times10^{-5},
\]

this gives

\[
\boxed{
\rho_F
=7.05474558522\ldots\times10^{-6}\ \text{rad}
=0.000404207147572\ldots^\circ.
}
\tag{FW.19}
\]

Since `rho_F<<gamma_H/2`, the large-gap cases excluded while deriving the ramps really are automatic.

---

## 4. Full-density central-diamond consequence

The fixed-angle central-diamond theorem may now be applied at every center of the no-TT population with any fixed aperture

\[
0<\rho<\rho_F.
\]

In particular, after choosing one fixed `rho` arbitrarily close to `rho_F`, every center has the two force chords separated by a fixed projective angle, while all the existing exact-force metadata remains:

- one birth on each physical host;
- one fixed force lane returning to the opposite host through the whole population;
- strict nested support order in both lanes;
- complete cross-sign crossing weave on every growing exact-phase block;
- exact positive two-ray force identity;
- fixed individual host transverse derivative margin `c_H-o(1)`;
- growing exact-phase depth and common near-equilateral train grid;
- vanishing normalized local switching/KKT complexity on the diagonal.

The elementary endpoint-separation scale supplied by the central-diamond estimate is

\[
D\sin{\rho_F\over2}-2L_D.
\tag{FW.20}
\]

Numerically,

\[
\boxed{
\sin(\rho_F/2)=3.52737279261\ldots\times10^{-6}.
}
\tag{FW.21}
\]

Thus, asymptotically, every no-TT force cell has a fixed positive linear central-diamond aperture, not merely a positive-density subfamily of cells.

---

## 5. Combined paired obstruction

The terminal-or-wide-return theorem and (FW.17) give the following no-TB1 alternative along the near-full diagonal.

### Terminal branch

A TT center exists. Then

\[
\boxed{
{\operatorname{diam}(T_m\cap S)\over D}
\ge c_H-o(1)
=0.453819885927\ldots-o(1),
}
\tag{FW.22}
\]

and its central angular diameter is at least `2 gamma_H-o(1)`; the ordered bilateral theorem further widens this span by `2 delta_D` for each additional TT center in the TT prefix.

### Full-density return branch

No TT center exists. Then

\[
\boxed{
N>\left({c\over2}-o(1)\right)D
=(1.13\times10^{-5}-o(1))D
}
\tag{FW.23}
\]

exact-force cells all satisfy

\[
\boxed{
\eta_s\ge\rho_F-o(1)
=7.05474558522\ldots\times10^{-6}-o(1),
}
\tag{FW.24}
\]

and one force lane goes to the opposite physical host at every center.

This removes the remaining projective-degeneration escape from the whole no-TT near-full population. The live split is now geometric: either the far terminal piece occupies a `0.4538D` chord, or a full near-shore-density nested bilateral weave has a fixed central diamond at every cell.

C-II remains open. The next closing theorem must either derive a terminal-piece upper span below `c_H D` from the stopped-train/terminal ledger, or show that the full-density fixed-wide return weave is incompatible with the common train grid / host order.

**Disposition:** combined the opposite-host return ramp with the ordered two-lane C67 ramp to force a fixed projective aperture at every center of the no-TT near-full population, with no density loss. C-II and Level I remain open.
