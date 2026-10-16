# Target C-II — a narrow TT pair makes the far terminal piece almost diametrical

**Date:** 2026-09-17  
**Status:** proof-only high-`t` geometric/structural strengthening; no canonical promotion claimed  
**Scope:** the no-positive-density-TB1 near-full paired exact-force shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** terminal-or-fixed-aperture corridor theorem; full-parent non-TT aperture theorem; ordered bilateral narrow-pair theorem; exact diameter support-normality; full-source diameter-midpoint localization; dense-force-grid/coercive-corridor arguments  
**Certificate:** `research/verify_target_c_high_t_near_diameter_terminal_or_uniform_corridor_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current paired obstruction has a small remaining asymmetry. Every non-TT center already has the full parent projective aperture

\[
\nu-o(1),
\qquad
\nu:={113\over10{,}000{,}000}=1.13\times10^{-5},
\]

but a TT-prefix pair can in principle have a smaller projective gap. The previous terminal branch used only the fixed host-cap separation and therefore concluded merely

\[
\operatorname{diam}(T_m\cap S)\ge(0.4538\ldots-o(1))D.
\]

A narrow TT pair is much more rigid than that. Its two force directions cannot realize the small ordinary lift, because both rays stay a fixed angle from the reaction axis. Hence the pair is nearly **antiparallel in ordinary angle**. Both hubward endpoints lie in the same far terminal piece `T_m`; the two terminal outward normals are the exact antipodes of those nearly antiparallel birth normals. Midpoint localization then makes the terminal endpoints themselves nearly diametrically opposite.

This gives an exhaustive sharpening:

\[
\boxed{
\begin{array}{c}
\operatorname{diam}(T_m\cap S)
\ge(\cos(\nu/2)-o(1))D\\[1mm]
\text{and }\operatorname{normalspan}(T_m)\ge\pi-\nu-o(1),
\end{array}
}
\]

or else **every** center in the near-full paired population, TT included, has projective force-pair aperture at least `nu-o(1)`. In the latter case the vanishing-mass block extraction no longer needs a positive-density non-TT suffix: it applies directly to the whole near-full shore. Thus there is a growing consecutive physical corridor on which every separator has fixed aperture, vanishing total KKT and compressed-force mass, the uniform coercivity floor, and the same near-full dense train grid.

Numerically,

\[
\boxed{
\cos(\nu/2)
=0.9999999999840388\ldots,
}
\]

so the terminal alternative is within about `1.5962e-11 D` of the full diameter at leading order. Its central angular span is at least

\[
\boxed{
\pi-\nu-o(1)
=179.99935255769\ldots^\circ-o(1).
}
\]

The asymptotic `o(D)` midpoint error is still present, so the decimal should not be read as a useful finite-`D` numerical estimate. The point is structural: projective collapse in TT can survive only by making the far terminal boundary piece asymptotically almost diametrical.

---

## 1. Setup and notation

Use the near-full paired population on one strict side of the common hub,

\[
i_1<i_2<\cdots<i_N<k,
\qquad
N>(\nu-o(1))D,
\tag{ND.1}
\]

where

\[
\nu={c\over2},
\qquad
c={113\over5{,}000{,}000}.
\tag{ND.2}
\]

At center `s`, write the bilateral exact force pair as

\[
h_s^A=x_s^Ay_s^A,
\qquad
h_s^B=x_s^By_s^B,
\tag{ND.3}
\]

with the diameter directions oriented from hubward partner to birth endpoint,

\[
d_s^A={x_s^A-y_s^A\over D},
\qquad
d_s^B={x_s^B-y_s^B\over D}.
\tag{ND.4}
\]

Let

\[
\eta_s
:=d_{\mathbb{RP}^1}([d_s^A],[d_s^B])
\in[0,\pi/2]
\tag{ND.5}
\]

be the projective pair gap.

The paired destination order has a TT prefix. At a TT center,

\[
y_s^A,y_s^B\in T_m.
\tag{ND.6}
\]

The ordered bilateral theorem supplies one common ordinary switching semicircle. If the two lifted force angles at a center have ordinary separation `Delta_s in (0,pi)`, then

\[
\eta_s=\min\{\Delta_s,\pi-\Delta_s\}.
\tag{ND.7}
\]

The sharpened host margin gives

\[
\Delta_s\ge2(\gamma_H-\varepsilon_D),
\qquad
\varepsilon_D\to0,
\tag{ND.8}
\]

where

\[
c_H=0.453819885927\ldots,
\qquad
\gamma_H:=\arcsin c_H=0.471047423019\ldots .
\tag{ND.9}
\]

Finally every actual diameter midpoint lies in the common central ball

\[
|m_h-o|\le L_D,
\qquad
L_D=O(D^{3/4})=o(D).
\tag{ND.10}
\]

---

## 2. Any TT pair narrower than `nu` is ordinary-near-antipodal

Assume one TT center `s` satisfies

\[
\eta_s<\nu.
\tag{ND.11}
\]

Since `nu=1.13e-5` while `gamma_H=0.471...`, equation (ND.8) rules out the small ordinary realization

\[
\Delta_s=\eta_s
\]

for all sufficiently large `D`. Therefore (ND.7) must use the other lift:

\[
\boxed{
\Delta_s=\pi-\eta_s>\pi-\nu.
}
\tag{ND.12}
\]

This is the key point. A projectively narrow TT force pair is not two almost-parallel ordinary diameter directions. It is two almost-antiparallel directions in the common switching semicircle.

At an actual diameter endpoint the chord direction is an exact support normal. Thus the outward normals selected at the two terminal endpoints are

\[
-d_s^A,
\qquad
-d_s^B,
\tag{ND.13}
\]

and have the same ordinary separation `Delta_s`. Both occur on `T_m`, so immediately

\[
\boxed{
\operatorname{normalspan}(T_m)
\ge\Delta_s
>\pi-\nu.
}
\tag{ND.14}
\]

No near-disk approximation is used in (ND.14).

---

## 3. The two TT terminal endpoints are almost a diameter apart

Let `m_s^A,m_s^B` be the two diameter midpoints. From (ND.4),

\[
y_s^\sigma
=m_s^\sigma-{D\over2}d_s^\sigma,
\qquad \sigma\in\{A,B\}.
\tag{ND.15}
\]

Hence

\[
\begin{aligned}
|y_s^A-y_s^B|
&\ge {D\over2}|d_s^A-d_s^B|-|m_s^A-m_s^B|\\
&\ge D\sin{\Delta_s\over2}-2L_D.
\end{aligned}
\tag{ND.16}
\]

Using (ND.12),

\[
\sin{\Delta_s\over2}
=\sin{\pi-\eta_s\over2}
=\cos{\eta_s\over2}
>\cos{\nu\over2}.
\tag{ND.17}
\]

Therefore

\[
\boxed{
|y_s^A-y_s^B|
>D\cos{\nu\over2}-2L_D,
}
\tag{ND.18}
\]

and because both endpoints lie on `T_m`,

\[
\boxed{
{\operatorname{diam}(T_m\cap S)\over D}
\ge\cos{\nu\over2}-o(1).
}
\tag{ND.19}
\]

Numerically,

\[
\boxed{
\cos{\nu\over2}
=0.9999999999840388\ldots .
}
\tag{ND.20}
\]

The deficit from one is

\[
1-\cos(\nu/2)
=1.59612\ldots\times10^{-11}.
\tag{ND.21}
\]

This is far stronger than the previous one-TT host-rung floor `c_H D` whenever the pair is projectively narrower than the parent aperture.

---

## 4. Central angular span is almost `pi`

The same midpoint localization gives a directional statement. From (ND.15) and (ND.10), the radial direction from `o` to `y_s^sigma` differs from `-d_s^sigma` by `o(1)` uniformly over actual diameter edges. Hence the smaller central angle between the two terminal rays satisfies

\[
\angle_o(y_s^A,y_s^B)
\ge\Delta_s-o(1).
\tag{ND.22}
\]

Combining with (ND.12),

\[
\boxed{
\operatorname{angdiam}_o(T_m\cap S)
\ge\pi-\nu-o(1).
}
\tag{ND.23}
\]

Numerically,

\[
\boxed{
\pi-\nu
=3.141581353589793\ldots
=179.999352557691\ldots^\circ.
}
\tag{ND.24}
\]

Thus the narrow-TT escape consumes essentially a semicircle of support-normal rotation and places two terminal source vertices essentially opposite about the common Type-II center.

---

## 5. Otherwise the whole paired population has the parent aperture

Assume now that no TT center satisfies (ND.11). Then every TT center obeys

\[
\eta_s\ge\nu.
\tag{ND.25}
\]

Every non-TT center independently satisfies the full-parent aperture theorem

\[
\eta_s\ge N\delta_D-o(1)
\ge\nu-o(1),
\qquad
\delta_D=2\arcsin{1\over2D}\ge {1\over D}.
\tag{ND.26}
\]

Therefore the **entire** near-full paired population satisfies

\[
\boxed{
\eta_s\ge\nu-o(1)
\qquad(1\le s\le N).
}
\tag{ND.27}
\]

This removes the positive-non-TT-density hypothesis from the fixed-aperture corridor construction. Destination type no longer matters.

---

## 6. A fixed-aperture vanishing-mass corridor now exists without a destination hypothesis

Use the physical-hole statement from the terminal-or-fixed-aperture corridor theorem. The paired population is obtained from its one-sided physical interface shore by deleting only

\[
H_D=o(D)
\tag{ND.28}
\]

center indices, while

\[
|P_D|>(\nu-o(1))D.
\tag{ND.29}
\]

Let `T_D=o(D)` be the common neighborhood-complexity scale from the same diagonal. Choose integers `m_D` so slowly that

\[
\boxed{
m_D\to\infty,
\qquad
{m_D(H_D+1)\over D}\to0,
\qquad
{m_DT_D\over D}\to0.
}
\tag{ND.30}
\]

The holes split the physical shore into at most `H_D+1` paired runs. Packing disjoint consecutive `m_D`-blocks into those runs gives `K_D` blocks with

\[
K_Dm_D
\ge|P_D|-(H_D+1)(m_D-1).
\tag{ND.31}
\]

Thus

\[
\boxed{
K_D\ge(\nu-o(1)){D\over m_D}\to\infty.
}
\tag{ND.32}
\]

On one side of the common hub the switching sets of distinct interfaces are edge-disjoint, so

\[
\sum_iB_i\le1.
\tag{ND.33}
\]

Choose among the `K_D` blocks one block `J_D` minimizing total switching mass. Then

\[
\boxed{
\mathcal B_D:=\sum_{i\in J_D}B_i
\le {1\over K_D}
=O\!\left({m_D\over D}\right)
\to0.
}
\tag{ND.34}
\]

By (ND.27), for all large `D` every separator of `J_D` has projective pair gap at least the fixed safe value

\[
\rho_*={\nu\over2}.
\tag{ND.35}
\]

The existing two-ray sine-law estimate then gives

\[
\boxed{
\sum_{i\in J_D}(\lambda_i^-+\lambda_i^+)
\le {2\mathcal B_D\over\sin(\nu/2)}
\to0.
}
\tag{ND.36}
\]

Likewise

\[
{1\over D}\sum_{i\in J_D}|G_i|
\le\mathcal B_D\to0.
\tag{ND.37}
\]

So fixed aperture and vanishing original/compressed force mass coexist on one unbounded consecutive physical corridor whether its separators are TT, mixed, OO, or cross a destination transition.

---

## 7. The full coercive dense-grid normal form survives unchanged

Every separator of `J_D` is exact-antipodal. Therefore the `m_D+1` rows have one common phase and the full cancellation kernel is

\[
\mathcal K_D
=\left\{c\in\mathbb R^{m_D+1}:\sum_jc_j=0\right\}.
\tag{ND.38}
\]

The direct-sum argument gives the same dimension-free bounds

\[
\boxed{
\max_h(L_D(c)_h)_+,
\max_h(-L_D(c)_h)_+
\ge(c_H-o(1))D\|c\|_\infty,
}
\tag{ND.39}
\]

and

\[
\boxed{
\left\|D^{-1}L_D(c)\right\|_2
\ge(\sqrt2\,c_H-o(1))\|c\|_2.
}
\tag{ND.40}
\]

The complexity condition in (ND.30) also lets the dense-grid argument run verbatim. There is one common transverse family `P_D` with

\[
\boxed{|P_D|>(0.6536-o(1))D}
\tag{ND.41}
\]

such that every row-column rhombus has angle

\[
\boxed{
{\pi\over3}<\theta={\pi\over3}+o(1)
}
\tag{ND.42}
\]

uniformly over the entire growing rectangle. The same initial and final column blocks satisfy

\[
\boxed{
|P_D^-|,|P_D^+|
>(0.0647027254265\ldots-o(1))D
}
\tag{ND.43}
\]

and bracket the row-normal circumcenter levels `-0.01D` and `+0.01D` simultaneously on every row.

Finally (ND.27) lets the central-diamond theorem be applied uniformly on all separators:

\[
\boxed{
B\!\left(o,
\left({1\over2}\sin{\nu\over2}-o(1)\right)D
\right)
\subset Q_i
\qquad(i\in J_D),
}
\tag{ND.44}
\]

with radius coefficient

\[
{1\over2}\sin{\nu\over2}
=2.82499999998\ldots\times10^{-6}.
\tag{ND.45}
\]

Thus branch (ND.25) produces the same fixed-aperture, massless, uniformly coercive, dense-grid corridor previously available only from a positive-density non-TT suffix.

---

## 8. Sharpened exhaustive frontier

The no-positive-density-TB1 near-full paired shore now satisfies the following exhaustive alternative.

### A. Near-diametrical terminal piece

Some TT force pair has `eta_s<nu`. Then

\[
\boxed{
\operatorname{normalspan}(T_m)>\pi-\nu,
}
\]

\[
\boxed{
\operatorname{angdiam}_o(T_m\cap S)
\ge\pi-\nu-o(1),
}
\]

and

\[
\boxed{
\operatorname{diam}(T_m\cap S)
\ge(0.9999999999840388\ldots-o(1))D.
}
\]

### B. Uniform fixed-aperture massless corridor

No TT pair has gap below `nu`. Then every paired center has gap at least `nu-o(1)`, and there is a consecutive corridor `J_D`, `|J_D|->infinity`, on which simultaneously

```text
every separator carries a bilateral exact positive two-diameter force pair;
every pair has projective aperture >= 1.13e-5-o(1);
every force diamond contains the same radius-(2.825e-6-o(1))D central disk;
total switching KKT mass over the corridor -> 0;
total compressed two-ray coefficient mass over the corridor -> 0;
normalized resultant variation over the corridor -> 0;
the full cancellation kernel has singular-value floor 0.641798...-o(1);
all rows cross the same (0.6536-o(1))D near-60-degree columns;
common +/-0.01D circumcenter flanks each have density 0.0647027-o(1).
```

This supersedes the previous terminal-dominant versus return-positive split as the sharpest current no-TB1 normal form. A terminal-heavy population is no longer by itself an escape from the fixed-aperture corridor: it escapes only if one TT pair is projectively narrow, and that single pair forces `T_m` to become asymptotically almost a diameter of the entire source.

C-II remains open. The two remaining geometric seams are now correspondingly sharp:

1. prove that the far terminal boundary piece cannot have normalized diameter tending to at least `cos(nu/2)=0.999999999984...` while carrying support-normal span at least `pi-nu`; or
2. in the uniform-corridor branch, localize the actual fixed-aperture diameter crossings relative to the common near-equilateral train-grid centers strongly enough to contradict the source diameter or construct a strict source-preserving diameter decrease.

**Disposition:** converted a projectively narrow TT force pair into an almost-diametrical far terminal piece, and used the contrapositive to remove the positive-non-TT-density hypothesis from the fixed-aperture vanishing-mass dense-force corridor. C-II and Level I remain open.