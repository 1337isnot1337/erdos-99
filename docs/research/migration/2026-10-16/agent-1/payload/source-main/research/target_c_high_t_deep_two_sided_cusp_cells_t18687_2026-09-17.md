# Target C-II — deep exact-phase force cells can be made quantitatively two-sided

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the no-fixed-margin-TB1 side of the high-`t` branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** deep bilateral exact-phase force-cell theorem; exact-antipodal exact force-pair theorem; elementary antipodal dipole support localization; C67 diameter-direction separation; shrinking common row-phase window  
**Certificate:** `research/verify_target_c_high_t_deep_two_sided_cusp_cells_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The deep-force-cell theorem gives positive linear density of robust bilateral exact-force diamonds arbitrarily far from every non-antipodal or high-complexity separator. Its fixed-angle condition controls the angle **between** the two force bars, but by itself it does not force both bars to stay a fixed distance from the reaction axis. One bar could, in principle, lie almost on the axis while the other carries essentially all of the transverse opening.

Global direction packing removes that regression at positive density.

Put

\[
c={113\over5{,}000{,}000},
\qquad
\delta_0={c\over64}={113\over320{,}000{,}000},
\tag{TS.1}
\]

and retain the robust force-pair angle

\[
\rho_0={c\over48}={113\over240{,}000{,}000}.
\tag{TS.2}
\]

For every fixed exact-phase depth `r`, the deep-force theorem supplies more than

\[
{c\over16}D-o(D)
\tag{TS.3}
\]

robust bilateral force centers. At all but at most

\[
2\delta_0D+o(D)={c\over32}D+o(D)
\tag{TS.4}
\]

of those centers, **both** selected force bars have projective distance at least `delta_0` from the common reaction/row axis. Consequently more than

\[
\boxed{
{c\over32}D-o(D)
={113\over160{,}000{,}000}D-o(D)
}
\tag{TS.5}
\]

deep centers simultaneously have:

- exact phase throughout the radius-`r` neighborhood;
- bounded local switching complexity there;
- bilateral birth on the two ordered host arcs;
- a fixed-angle central exact-force diamond at the center;
- both center force bars at projective distance at least `delta_0` from the reaction axis.

This last condition makes the elementary antipodal dipole cusp quantitatively two-sided. If `d^(i)` is the elementary dipole coordinate at such a center and `s!=0`, then its two selected force bars `h_i^- ,h_i^+` satisfy

\[
\boxed{
|\ell_{h_i^\pm}(s d^{(i)})|
\ge 2D|s|\sin\delta_0,
}
\tag{TS.6}
\]

with opposite signs. Hence **for either sign of the local shear parameter**, one actual diameter bar lengthens with squared-length derivative at least

\[
\boxed{2D|s|\sin\delta_0.}
\tag{TS.7}
\]

The positive force compression is also uniformly conditioned relative to the reaction magnitude. If

\[
G_i=D(\lambda_i^-d_i^-+\lambda_i^+d_i^+),
\tag{TS.8}
\]

then

\[
\boxed{
\lambda_i^\pm
\ge {|G_i|\over D}\sin\delta_0.
}
\tag{TS.9}
\]

Together with the deep-cell upper bound

\[
\lambda_i^\pm
\le {T_rC\over D\sin\rho_0},
\tag{TS.10}
\]

this shows that the two selected force rays cannot become geometrically irrelevant by collapsing onto the axial direction, even though their absolute KKT scale may tend to zero.

---

## 1. Near-axis selected force bars have only `2 delta D + o(D)` interface capacity

Fix any positive constant `delta`. At every exact-antipodal force center orient the reaction axis as

\[
e_i={G_i\over|G_i|}=\pm u_i.
\tag{TS.11}
\]

All projective row lines `[u_i]=[e_i]` on the selected high-`t` shore lie in one common interval `W_D` of width

\[
\omega_D=o(1).
\tag{TS.12}
\]

Call a selected force center **axis-near** if at least one of its two selected force bars has projective distance less than `delta` from `[e_i]`.

Choose one such near-axis bar from each axis-near center. Switching supports at distinct interfaces are disjoint, so the chosen actual diameter bars are distinct. Their projective directions all lie in the `delta`-neighborhood of `W_D`, an interval of length at most

\[
\omega_D+2\delta.
\tag{TS.13}
\]

Canonical C67 separates distinct actual diameter directions by at least `1/D`. Therefore the number `A_D(delta)` of axis-near selected centers satisfies

\[
\boxed{
A_D(\delta)
\le(\omega_D+2\delta)D+O(1)
=2\delta D+o(D).
}
\tag{TS.14}
\]

This estimate uses one selected bar per bad center, so it does not require the two force bars at a center to have comparable KKT coefficients.

---

## 2. Apply the capacity bound inside the deep robust family

On the no-fixed-margin-TB1 branch, for every fixed `r` the deep-force-cell theorem gives a center family `Q_D(r)` satisfying

\[
|Q_D(r)|>{c\over16}D-o(D).
\tag{TS.15}
\]

Set

\[
\delta_0={c\over64}.
\]

By (TS.14), at most

\[
2\delta_0D+o(D)
={c\over32}D+o(D)
\tag{TS.16}
\]

members of `Q_D(r)` have either selected force bar within `delta_0` of the local reaction axis. Delete them. The retained family `Q_D^{two}(r)` has

\[
\begin{aligned}
|Q_D^{two}(r)|
&>{c\over16}D-{c\over32}D-o(D)\\
&={c\over32}D-o(D),
\end{aligned}
\tag{TS.17}
\]

which proves (TS.5).

Every retained force pair still has projective pair gap at least `rho_0`, is bilateral, is centrally localized, and lies at the center of the same clean radius-`r` exact-phase neighborhood. The deletion only imposes the extra two-sided axial margin.

---

## 3. Quantitative two-sided dipole cusp

Fix a retained center `i`. Let `v=e_i` be the ordinary reaction-axis orientation. For its two selected force bars choose consistent unit diameter directions `d_i^- ,d_i^+` on opposite transverse sides of `v`.

The elementary exact-antipodal dipole coordinate `d^(i)` has relative velocity `+Jv` or `-Jv` on every switching diameter row at interface `i`, with a common sign convention. Multiplying by `s` gives relative velocity of magnitude `|s|` in the transverse direction.

For an actual diameter bar `h` of vector `Dd_h`, the first derivative of squared length is

\[
\ell_h(s d^{(i)})
=2D s\, d_h\cdot Jv
\tag{TS.18}
\]

up to the common interface orientation sign, which does not affect the absolute value.

For both selected force bars,

\[
d_\pi([d_i^\pm],[v])\ge\delta_0.
\tag{TS.19}
\]

Since `|d\cdot Jv|` is the sine of the projective angle between the two lines,

\[
|d_i^\pm\cdot Jv|
\ge\sin\delta_0.
\tag{TS.20}
\]

Equation (TS.18) gives (TS.6). The selected force bars lie on opposite transverse sides of `v`, so their derivatives have opposite signs. Reversing `s` swaps which bar lengthens. Therefore the positive derivative in either shear direction has magnitude at least the bound in (TS.7).

This is stronger than the qualitative antipodal sign cusp: the local one-dimensional dipole coordinate is uniformly linearly jammed at a fixed geometric rate independent of `D` after division by `D`.

---

## 4. The exact force representation is two-sided conditioned

Write the lifted angular deviations of the two selected force rays from `v` as `p_i,q_i>0`, with `p_i+q_i<pi`. The exact-force theorem gives

\[
\lambda_i^-={|G_i|\over D}{\sin q_i\over\sin(p_i+q_i)},
\qquad
\lambda_i^+={|G_i|\over D}{\sin p_i\over\sin(p_i+q_i)}.
\tag{TS.21}
\]

The two-sided axial margin says the projective distance of each ray from `[v]` is at least `delta_0`, hence

\[
\sin p_i,\sin q_i\ge\sin\delta_0.
\tag{TS.22}
\]

Since `0<sin(p_i+q_i)<=1`, (TS.21) gives

\[
\lambda_i^-,\lambda_i^+
\ge {|G_i|\over D}\sin\delta_0,
\]

which is (TS.9).

The pair gap remains at least `rho_0`, so the deep-force theorem supplies the complementary upper bound (TS.10). No absolute lower bound follows because `|G_i|/D` may vanish.

---

## 5. Growing-depth diagonal form

The density in (TS.17) is independent of the fixed radius `r`. Apply the same diagonal extraction as in the deep-force theorem. There are `D_k->infinity` and `r_k->infinity`, with `r_k=o(D_k)`, such that at least

\[
{c\over32}D_k-o(D_k)
\tag{TS.23}
\]

centers have exact-phase depth `r_k`, bilateral fixed-angle central force diamonds, and the fixed two-sided axial margin `delta_0`.

At those centers the normalized switching stress and normalized reaction still tend to zero across the growing neighborhoods, while the elementary local dipole remains uniformly jammed at the geometric rate

\[
2\sin\delta_0>0.
\tag{TS.24}
\]

Thus vanishing KKT scale and strong geometric first-order jamming coexist on a positive linear family of arbitrarily deep exact-phase cells.

---

## 6. Frontier effect

The surviving exact-antipodal branch is now more rigid than a growing phase plateau with occasional wide diamonds. At positive linear density one can choose centers that are simultaneously:

```text
arbitrarily deep inside exact phase,
locally bounded-complexity,
bilaterally born,
macroscopically central,
exact force-carrying,
fixed-angle between the two force bars,
and fixed-angle away from the reaction axis on BOTH sides.
```

At every such center the canonical elementary dipole has a uniform two-sided linear cusp: changing the sign of the shear merely swaps which selected diameter bar lengthens, and the positive squared-length derivative is always at least `2D|s| sin(delta_0)`.

This rules out another degeneration in which deep exact-phase cells survive only because one force ray becomes asymptotically axial. A closing argument must now accommodate a positive-density family of genuinely transverse, quantitatively jammed local cells inside arbitrarily long exact-phase neighborhoods.

No C-II or Level-I closure is claimed.

**Disposition:** extracted positive linear density `c/32` of deep exact-phase robust force cells whose two selected diameter bars each retain a fixed transverse margin from the common reaction axis, yielding a uniform two-sided elementary-dipole cusp and a conditioned two-ray exact-force representation. C-II and Level I remain open.
