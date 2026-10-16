# Target C-II - THIN braid directions must disperse on the inverse-D scale

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the THIN phase-cone uniqueness normal form; no canonical promotion claimed  
**Scope:** THIN side of the 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** THIN superdiameter window; vertex-disjoint growing braid; phase-cone uniqueness theorem  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_directional_dispersion_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The phase-cone uniqueness theorem leaves a `Theta(log D)` vertex-disjoint THIN braid in one open `pi/3` projective sector, with one common row/guard uniqueness mode and one common four-bit guard-incidence word. A remaining possibility was that this entire braid could still collapse into one `O(D^-1)` direction tube. That does not happen.

The reason is metric and independent of the train geometry. A vertex-disjoint family of `D-A/D` near-diameters in a projective direction tube of half-width `L/D` has only `O_A(L)` members. The linear, rather than quadratic, dependence on `L` comes from using a near-support cap: all left endpoints lie in a strip of depth `O((A+L^2)/D)`, and the diameter constraint against the most forward right endpoint confines their transverse coordinates to an interval of length `O(sqrt(A+L^2))`. Unit separation then gives one-dimensional packing.

For the THIN value `A=1/4`, this implies:

> **Directional-dispersion theorem.** Let `F_D` be any vertex-disjoint THIN family with
> \[
> D-{1\over4D}<|e|<D.
> \]
> If `K_D=|F_D|->infinity`, `K_D=o(sqrt D)`, and `omega_D` is the projective angular diameter of its directions inside one arc of length `<pi/2`, then
> \[
> \boxed{
> \omega_D\ge
> \left(1-o(1)\right){K_D\over D}.
> }
> \tag{DD.1}
> \]
>
> More locally, for every fixed `L>0`, any projective tube of radius `L/D` contains at most
> \[
> \boxed{
> 1+\sqrt{2+4L^2}+o(1)
> }
> \tag{DD.2}
> \]
> members of a vertex-disjoint THIN family.

Applying this after the phase-cone and four-bit purification gives a sub-braid of size
\[
K_D\ge\left({1\over96\log5}-o(1)\right)\log D
\tag{DD.3}
\]
through the same `D^(1/2-o(1))` common rows and four macroscopic guards. Hence
\[
\boxed{
\omega_D\ge
\left({1\over96\log5}-o(1)\right){\log D\over D}
}
\tag{DD.4}
\]
with
\[
{1\over96\log5}
=0.00647223890166\ldots .
\tag{DD.5}
\]

Even more usefully, for every fixed inverse-`D` clearance scale `L`, a further `Theta(log D)` sub-braid can be selected whose chord directions are pairwise more than `L/D` apart, while preserving pairwise proper crossing, the same uniqueness mode, the same four-bit guard word, the same four fixed macroscopic guards, and the same polynomial common row stack.

Thus the THIN uniqueness branch is not a one-phase degeneration. It contains logarithmically many genuinely distinct inverse-`D` direction classes.

---

## 1. A finite cap-packing bound for near-diameters

Let `S` be a unit-separated planar set with diameter at most `D`. Fix `A>0`. Let `E` be a vertex-disjoint family of unordered pairs `xy` satisfying
\[
D-{A\over D}\le |x-y|\le D.
\tag{DD.6}
\]
Assume all projective directions lie in one arc of width `2L/D`, where `L=L_D` may depend on `D`. Orient each pair so that
\[
r_e=y_e-x_e=\ell_e d_e,
\qquad
\angle(d_e,u)\le {L\over D}
\tag{DD.7}
\]
for one unit vector `u`.

Write
\[
m:=\min_{p\in S}u\cdot p,
\qquad
M:=\max_{p\in S}u\cdot p,
\qquad
W:=M-m\le D.
\tag{DD.8}
\]
Put
\[
P_D:=\left(D-{A\over D}\right)\cos{L\over D},
\qquad
\varepsilon_D:=D-P_D.
\tag{DD.9}
\]
Every oriented edge has longitudinal projection at least `P_D`, hence
\[
W\ge P_D=D-\varepsilon_D.
\tag{DD.10}
\]
Moreover
\[
u\cdot x_e\le M-P_D\le m+\varepsilon_D,
\tag{DD.11}
\]
and symmetrically
\[
u\cdot y_e\ge M-\varepsilon_D.
\tag{DD.12}
\]
Thus every left endpoint lies in the lower support cap of `u`-depth `\varepsilon_D`, while every right endpoint lies in the opposite cap of the same depth.

Among the oriented right endpoints, choose `y_*` maximizing `u\cdot y`. For every edge `e`,
\[
u\cdot(y_*-x_e)
\ge u\cdot(y_e-x_e)
\ge P_D
=D-\varepsilon_D.
\tag{DD.13}
\]
Let `v=Ju`. Since every source distance is at most `D`,
\[
|v\cdot(y_*-x_e)|^2
\le D^2-P_D^2
=2D\varepsilon_D-\varepsilon_D^2.
\tag{DD.14}
\]
Therefore all left endpoints have `v`-coordinates in one interval of length at most
\[
2\sqrt{2D\varepsilon_D-\varepsilon_D^2}.
\tag{DD.15}
\]

On the other hand, (DD.11) and `u\cdot x_e>=m` place all left `u`-coordinates in an interval of length at most `\varepsilon_D`. If `\varepsilon_D<1`, unit separation implies that distinct left endpoints have transverse-coordinate separation at least
\[
\sqrt{1-\varepsilon_D^2}.
\tag{DD.16}
\]
The edges are vertex-disjoint, so all left endpoints are distinct. One-dimensional packing in (DD.15) proves the exact finite bound
\[
\boxed{
|E|
\le
1+{2\sqrt{2D\varepsilon_D-\varepsilon_D^2}\over\sqrt{1-\varepsilon_D^2}}
}
\tag{DD.17}
\]
whenever `\varepsilon_D<1`.

This is the key improvement over the earlier bounded-capacity proof, which only needed a fixed-radius disk and therefore did not record the linear dependence on the angular tube scale.

---

## 2. Fixed inverse-D tubes have bounded linear capacity

Suppose now that `L` is fixed while `D->infinity`. Taylor expansion of (DD.9) gives
\[
D\varepsilon_D
=A+{L^2\over2}+o(1),
\qquad
\varepsilon_D=o(1).
\tag{DD.18}
\]
Substituting into (DD.17),
\[
\boxed{
|E|
\le
1+2\sqrt{2A+L^2}+o(1).
}
\tag{DD.19}
\]
For THIN edges, `A=1/4`, so
\[
\boxed{
|E|
\le
1+\sqrt{2+4L^2}+o(1).
}
\tag{DD.20}
\]
This proves (DD.2).

A convenient eventual integer bound is
\[
C_L:=2+\left\lceil\sqrt{2+4L^2}\right\rceil.
\tag{DD.21}
\]
For all sufficiently large `D`, every radius-`L/D` projective direction tube contains fewer than `C_L` THIN matching edges.

Greedy selection now gives:

> **Corollary DD.1.** From any `K`-edge vertex-disjoint THIN family one can choose at least
> \[
> \boxed{\left\lceil {K\over C_L}\right\rceil}
> \tag{DD.22}
> \]
> edges whose projective directions are pairwise more than `L/D` apart.

Indeed, select one edge and delete all edges within projective distance `L/D` of it. By (DD.21), each greedy step deletes fewer than `C_L` edges.

---

## 3. Growing families force angular diameter K/D

Let `K_D=|E_D|->infinity` with `K_D=o(sqrt D)`, and let `omega_D` be the angular diameter of the family inside one projective arc of length `<pi/2`.

We prove
\[
\liminf_{D\to\infty}{D\omega_D\over K_D}\ge 1.
\tag{DD.23}
\]
Suppose not. Then for some fixed `delta>0` and an infinite subsequence,
\[
D\omega_D\le
(1-\delta)K_D.
\tag{DD.24}
\]
Put
\[
L_D={D\omega_D\over2}.
\tag{DD.25}
\]
Along this subsequence, `L_D=O(K_D)=o(sqrt D)`. Hence the expansion of (DD.9) is uniform:
\[
D\varepsilon_D
=A+{L_D^2\over2}+o(1+L_D^2),
\qquad
\varepsilon_D=o(1).
\tag{DD.26}
\]
Equation (DD.17) gives
\[
K_D
\le
1+2\sqrt{2A+L_D^2+o(1+L_D^2)}
=(2+o(1))L_D,
\tag{DD.27}
\]
because `L_D->infinity` whenever `K_D->infinity` and (DD.27) is to hold. Therefore
\[
K_D\le(1+o(1))D\omega_D.
\tag{DD.28}
\]
Combining with (DD.24) yields
\[
K_D
\le
(1-\delta+o(1))K_D,
\]
a contradiction. Thus
\[
\boxed{
\omega_D\ge
\left(1-o(1)\right){K_D\over D}.
}
\tag{DD.29}
\]
This proves (DD.1).

For `A=1/4`, retaining the lower-order constant in (DD.27) gives the useful finite-scale guide
\[
D\omega_D
\gtrsim
\sqrt{(K_D-1)^2-2},
\tag{DD.30}
\]
which has the same asymptotic coefficient `1`.

---

## 4. Apply to the THIN phase-cone uniqueness braid

Use the macroscopic four-guard theorem at
\[
c={1\over2\log5}.
\tag{DD.31}
\]
The phase-cone uniqueness theorem deletes only `O(1)` boundary-near chords, keeps one of three direction sectors, and then keeps one of sixteen four-bit guard words. It therefore gives a vertex-disjoint pairwise-crossing THIN family `F_D^uniq` with
\[
\boxed{
K_D:=|F_D^{uniq}|
\ge
\left({1\over96\log5}-o(1)\right)\log D.
}
\tag{DD.32}
\]
All its directions lie in one open sector of width `pi/3`, so its projective angular diameter is unambiguous and `<pi/2`.

Every edge satisfies the THIN shell estimate
\[
D-|e|<{1\over4D}.
\tag{DD.33}
\]
Since `K_D=Theta(log D)=o(sqrt D)`, (DD.29) applies and gives
\[
\omega_D
\ge
\left(
{1\over96\log5}-o(1)
\right){\log D\over D},
\tag{DD.34}
\]
which is (DD.4).

Now fix any constant `L>0`. Apply Corollary DD.1 to `F_D^uniq`. There is a subset
\[
F_D^{sep}(L)\subset F_D^{uniq}
\]
with
\[
\boxed{
|F_D^{sep}(L)|
\ge
\left(
{1\over96\log5\,C_L}-o(1)
\right)\log D
}
\tag{DD.35}
\]
and
\[
\boxed{
d_{\mathbb{RP}^1}([e],[f])>{L\over D}
\quad(e\ne f\in F_D^{sep}(L)).}
\tag{DD.36}
\]
Taking a subset preserves all prior structure:

- every two selected THIN chords still cross properly;
- the row/guard uniqueness alternative is unchanged;
- the common four-bit incidence word against the same four guards is unchanged;
- the same `D^(1/2-o(1))` common inverse-`D` phase row family is retained;
- the four fixed guards retain their macroscopic flank separations.

Hence one may take `L` larger than any fixed phase-error constant appearing in a later row/guard argument without losing the logarithmic braid order.

---

## 5. Frontier effect

The latest THIN normal form had removed intersection multiplicity but still allowed a hidden near-parallel degeneration of the entire logarithmic braid. That degeneration is now excluded.

At the half-exponent scale the surviving system contains

```text
Theta(log D) pairwise-crossing THIN hull chords;
one common ROW-UNIQUE or GUARD-UNIQUE mode;
one common four-bit incidence word against four macroscopic train guards;
D^(1/2-o(1)) common near-equilateral selected rows;
and braid angular diameter at least
    (0.00647223890166... - o(1)) log(D)/D.
```

More strongly, for every fixed `L`, a `Theta(log D)` sub-braid has pairwise direction separation `>L/D`. Thus a future closure argument may demand inverse-`D` angular clearance larger than all row/guard phase errors and still keep logarithmically many pairwise-crossing chords.

This does not by itself contradict the THIN branch. The remaining geometric task is to combine this robust directional dispersion with either the unique row intersections or the unique guard intersections. In particular, any order argument may now assume simultaneously that the participating braid chords have genuinely distinct slopes at the same scale on which the train phases are controlled.

**Disposition:** excluded inverse-`D` single-phase collapse of the THIN uniqueness braid and produced a logarithmic robustly direction-separated sub-braid. C-II and Level I remain open.
