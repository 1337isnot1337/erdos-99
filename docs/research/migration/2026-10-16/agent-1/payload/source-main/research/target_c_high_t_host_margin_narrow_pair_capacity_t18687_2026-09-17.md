# Target C-II — host margin halves the narrow exact-force-pair capacity

**Date:** 2026-09-17  
**Status:** proof-only high-`t` quantitative strengthening; no canonical promotion claimed  
**Scope:** exact-antipodal force pairs on one selected one-sided high-`t` shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** common one-sided switching half-plane; exact-antipodal exact-force pair; coupled host transverse margin; C67 projective diameter-direction separation; host-cap force-pair separation  
**Certificate:** `research/verify_target_c_high_t_host_margin_narrow_pair_capacity_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous narrow-pair packing theorem allowed two ways for a projectively narrow opposite-transverse force pair to fit inside the common oriented switching semicircle:

1. both directions can lie near the row/reaction axis;
2. the two oriented rays can be almost antiparallel, so projectively both lie near the common boundary line of the switching semicircle.

This produced two projective packing arcs and the loss

\[
2\rho D+o(D)
\]

for force pairs of projective gap below `rho`.

The coupled host theorem removes the first mechanism pointwise. Every switching diameter stays at least

\[
\gamma_H-o(1),
\qquad
\gamma_H=\arcsin(0.453819885927\ldots)
=0.4710474230\ldots
\]

from its own row axis. Therefore, for every fixed `rho<gamma_H`, a `rho`-narrow exact force pair must be of the second type: its two projective diameter directions lie in the **single** radius-`rho` neighborhood of the common semicircle boundary line.

C67 then gives the sharpened capacity

\[
\boxed{
N_D^{\rm narrow}(\rho)\le \rho D+o(D),
}
\]

halving the old `2rho D` loss. The proof also gives a finite form for a variable aperture once the finite-source host-margin error is included explicitly.

---

## Theorem NC — one-arc narrow-pair packing

Let `E_D` be any family of exact-antipodal interfaces on one fixed one-sided shore. At each `i in E_D`, choose the exact positive force pair

\[
d_i^-,d_i^+.
\]

Let

\[
\eta_i=d_{\mathbb{RP}^1}([d_i^-],[d_i^+]).
\tag{NC.1}
\]

Let `ell_D` be the projective boundary line of the common open semicircle containing every consistently oriented switching direction on this shore. Let

\[
\delta_D:=2\arcsin{1\over2D}
\tag{NC.2}
\]

be the canonical C67 separation between distinct actual diameter directions.

Write the finite-source host-margin estimate as

\[
d_{\mathbb{RP}^1}([d],[u_i])\ge \gamma_H-\varepsilon_D,
\qquad \varepsilon_D\to0,
\tag{NC.3}
\]

uniformly for switching diameters on the selected shore. Suppose `rho_D>0` satisfies eventually

\[
\rho_D<\gamma_H-\varepsilon_D.
\tag{NC.4}
\]

Then every interface with `eta_i<rho_D` contributes two distinct actual diameter directions lying in the single projective arc

\[
B_{\mathbb{RP}^1}(\ell_D,\rho_D),
\tag{NC.5}
\]

whose length is `2rho_D`. Hence, if

\[
N_D(\rho_D)
:=\#\{i\in E_D:\eta_i<\rho_D\},
\]

then

\[
\boxed{
2N_D(\rho_D)-1
\le {2\rho_D\over\delta_D},
}
\tag{NC.6}
\]

and therefore

\[
\boxed{
N_D(\rho_D)
\le {\rho_D\over\delta_D}+{1\over2}.
}
\tag{NC.7}
\]

For every fixed `0<rho<gamma_H`, since `D delta_D ->1`,

\[
\boxed{
N_D(\rho)\le\rho D+o(D).
}
\tag{NC.8}
\]

No shrinking row-phase-window packing term remains.

---

## 1. Elementary semicircle dichotomy

Lift the common switching semicircle to an ordinary angular interval

\[
(\beta,\beta+\pi).
\]

At one exact interface choose the lift so that

\[
\beta<\theta^-<\alpha<\theta^+<\beta+\pi,
\tag{NC.9}
\]

where `alpha` is the oriented reaction axis and `theta^\pm` are the two force-ray angles. Opposite transverse signs and positive force generation give exactly this bracketing order.

Put

\[
s:=\theta^+-\theta^-\in(0,\pi).
\]

The projective pair gap is

\[
\eta=\min\{s,\pi-s\}.
\tag{NC.10}
\]

If `eta<rho`, there are only two cases.

### Case A: `s<rho`

Since `alpha` lies between the two rays,

\[
|\theta^- -\alpha|<\rho,
\qquad
|\theta^+ -\alpha|<\rho.
\tag{NC.11}
\]

Both projective force directions are `rho`-close to the row/reaction axis.

### Case B: `pi-s<rho`

Because both rays lie inside the same semicircle,

\[
(\theta^- -\beta)
+((\beta+\pi)-\theta^+)
=\pi-s<\rho.
\tag{NC.12}
\]

Both nonnegative summands are below `rho`. Thus the lower ray lies within `rho` of the lower semicircle boundary and the upper ray within `rho` of the opposite boundary ray. Those two boundary rays are the same point of `RP^1`, namely `ell_D`. Hence both projective directions lie in (NC.5).

This is the exact two-arc dichotomy used implicitly in the older `2rho D` capacity bound.

---

## 2. The host margin deletes the row-axis case

The coupled host theorem gives (NC.3), and at an exact-antipodal interface the reaction axis is projectively `[u_i]`.

If `rho=rho_D` satisfies (NC.4), then (NC.11) contradicts (NC.3). Thus Case A is impossible. Every `rho_D`-narrow exact force pair is necessarily the almost-antiparallel Case B, and all of its projective directions lie in the one common arc (NC.5).

This step does not need the global shrinking row-phase window. It uses the pointwise host margin against each pair's own exact row axis.

---

## 3. C67 packs all narrow force rays into that one arc

The two bars at one exact force interface are distinct. Switching supports at different one-sided interfaces are edge-disjoint. Thus the `N_D(rho_D)` narrow interfaces contribute exactly `2N_D(rho_D)` distinct actual diameter edges.

C67 separates every two distinct projective actual diameter directions by at least `delta_D`. A projective arc of length `2rho_D` can therefore contain at most

\[
1+{2\rho_D\over\delta_D}
\]

such directions. This is (NC.6)--(NC.7).

The host-cap theorem separately shows that every exact force pair is internally vertex-disjoint and crossing even when `eta_i` is very small. That fact is not needed for the packing count, but it removes the old possibility that the near-boundary concentration could be realized by local diameter stars.

---

## 4. Sharpened robust exact-force/TB1 fork

Use the host-sharpened parent fork

\[
|E_D|+|U_D|>c_0D-o(D),
\qquad
c_0={113\over20{,}000{,}000}=5.65\times10^{-6},
\tag{NC.13}
\]

where host geometry already makes every non-antipodal TB1 interface uniformly strong without an angular-density deletion.

For any fixed

\[
0<\rho<c_0
\]

(the much weaker condition `rho<gamma_H` is automatic), remove the narrow exact force pairs. By (NC.8) this costs at most `rho D+o(D)`. Therefore

\[
\boxed{
|S_D^{host}|+|E_D^{force}(\rho)|
>(c_0-\rho)D-o(D).
}
\tag{NC.14}
\]

Consequently one mechanism has population

\[
\boxed{
>{c_0-\rho\over2}D-o(D).
}
\tag{NC.15}
\]

The previous host-sharpened bound was `(c_0-2rho)D-o(D)`.

If a later contradiction pays one power of the pair gap, the guaranteed product

\[
\rho{c_0-\rho\over2}
\]

is maximized at

\[
\boxed{\rho={c_0\over2},}
\tag{NC.16}
\]

where one mechanism still has density

\[
\boxed{{c_0\over4}=1.4125\times10^{-6}.}
\tag{NC.17}
\]

This doubles the old optimized one-power product.

If a later contradiction pays `rho^2`, the optimum is

\[
\boxed{\rho={2c_0\over3},}
\tag{NC.18}
\]

where one mechanism has density

\[
\boxed{{c_0\over6}=9.416666\ldots\times10^{-7}.}
\tag{NC.19}
\]

The optimized `rho^2` product is four times the old `c_0-2rho` value.

---

## 5. Near-full-shore deep blocks lose only `m rho D`

The full-shore deep-force theorem starts from the one-sided shore density

\[
{c\over2}D-o(D),
\qquad c={113\over5{,}000{,}000},
\tag{NC.20}
\]

and, for a radius-`r` block with `m=2r+1` internal interfaces, separately pays center-complexity and neighborhood-separator losses `eta_0 D` and `eta_r D`.

Its old fixed-gap deletion used the bound `2rho D+o(D)` for narrow interfaces and therefore paid `2m rho D`. Replacing that step by (NC.8) gives the sharpened retained density

\[
\boxed{
\Lambda_r^{sharp}
:={c\over2}-\eta_0-\eta_r-m\rho.
}
\tag{NC.21}
\]

whenever the displayed coefficient is positive.

Every retained internal interface keeps the full previous conclusions:

- exact common phase through the block;
- bounded local complexity;
- a `rho`-wide exact positive force pair;
- individual transverse margin `c_H-o(1)`;
- pointwise bilateral birth and internal crossing by Theorem HC;
- the common inverse-`D` train grid;
- strict monotonicity of the exact resultants through the block.

Only the narrow-pair counting constant changes.

At the parameter schedule used for the existing growing diagonal, one may therefore double `rho_n` while keeping the old density loss. With

\[
\varepsilon_n={c\over10n},
\qquad m_n=2n+1,
\]

the old choice was `rho_n=epsilon_n/(8m_n)`. The sharpened capacity allows

\[
\boxed{
\rho_n={\varepsilon_n\over4m_n}
}
\tag{NC.22}

for the same `epsilon_n/4` neighborhood-wide narrow-pair loss. Thus the resolved force-diamond aperture may be doubled at no density cost.

---

## 6. Adjacent double-force cells also retain more wide pairs

In the current double-antipodal theorem let

\[
p_0={2599\over960{,}000{,}000},
\qquad
\rho_*={p_0\over8}.
\tag{NC.23}
\]

If the adjacent exact-antipodal side occurs, then

\[
|P_D|>p_0D-o(D).
\]

The old capacity bound allowed `p_0D/4+o(D)` narrow constituent interfaces; since one interface can spoil two adjacent cells, it retained only `p_0D/2-o(D)` cells with both pairs wide.

Theorem NC instead gives at most

\[
\rho_*D+o(D)={p_0\over8}D+o(D)
\]

narrow interfaces. At most `p_0D/4+o(D)` adjacent cells are spoiled. Hence

\[
\boxed{
>{3p_0\over4}D-o(D)
}
\tag{NC.24}

adjacent double-force cells have both exact force pairs of projective gap at least `rho_*`. Numerically the coefficient is

\[
\boxed{2.03046875\times10^{-6}.}
\tag{NC.25}

This improves the previous retained coefficient `p_0/2=1.353645833...e-6` by a factor `3/2` at the same fixed pair gap.

---

## 7. Frontier effect

Projectively narrow exact force pairs now have only one possible global geometry:

```text
not near the row axis (host margin forbids it),
therefore almost antiparallel in the common oriented semicircle,
therefore both projective lines lie near the one common semicircle boundary line.
```

This halves every current density loss that came solely from narrow exact-force-pair packing. It also isolates the residual narrow-pair escape in one common projective direction rather than a union of row-axis and boundary-line neighborhoods.

C-II remains open. The narrow branch is now a globally localized near-boundary line family; the wide branch has larger guaranteed density. A next useful attack is to combine the near-boundary localization with the host-cap zipper and the ordered train grid, instead of treating small pair aperture as an unstructured local degeneration.

**Disposition:** proved the one-arc narrow-pair capacity `rho D+o(D)`, improved the robust fork to `c_0-rho`, halved the fixed-gap loss in near-full-shore deep blocks, and increased the retained wide double-force-cell density to `3p_0/4`. C-II and Level I remain open.