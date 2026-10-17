> Generated reading edition · [exact source](../../research/target_c_high_t_robust_angle_density_tradeoff_t18687_2026-09-17.md) · source SHA-256 `b48add5602ac798494d189e0b4a6d0784340a8cc9087cb55da505c7378ff6bc1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "31138cbe68273e04375fbc9433390cc08a6d5329", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_robust_angle_density_tradeoff_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "669b555c9a7cba4ab85a3ef55d9d77419b702d488450714190afdb81fccb1822"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — a parameterized fixed-angle / density tradeoff for the final high-`t` fork

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the linear one-sided high-`t` obstruction shore for `t=(q-k)/D<=1.8687`  
**Dependencies:** corrected exact-antipodal / non-antipodal TB1 density fork; common one-sided switch half-plane; exact-antipodal opposite-transverse blocker pair; shrinking common row-phase window; canonical C67 projective diameter-direction separation; source-wide diameter-star angle bound  
**Certificate:** `research/verify_target_c_high_t_robust_angle_density_tradeoff_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The fixed-angle antipodal-dipole theorem used the convenient scale

$$
\gamma={c_0\over32},
\qquad
c_0={113\over20{,}000{,}000},
$$

because the existing strong-TB1 theorem had already been stated at that scale.  The argument in fact gives a one-parameter family of robust forks.

Fix any constant

$$
\boxed{0<\rho<{c_0\over6}.}
\tag{RT.1}
$$

For all sufficiently large sources define:

- `S_D(rho)`: non-antipodal TB1 good interfaces whose chosen one-bar blocker is at least `rho` from both rays of its local dual cone;
- `E_D^{wide}(rho)`: exact-antipodal good interfaces whose selected opposite-transverse blocker pair has projective direction gap at least `rho`.

Then

$$
\boxed{
|E_D^{\rm wide}(\rho)|+|S_D(\rho)|
>(c_0-6\rho)D-o(D).
}
\tag{RT.2}
$$

Consequently

$$
\boxed{
\max\{|E_D^{\rm wide}(\rho)|,|S_D(\rho)|\}
>{c_0-6\rho\over2}D-o(D).
}
\tag{RT.3}
$$

The geometry on the two sides has the same prescribed absolute scale `rho`:

- every member of `S_D(rho)` has
  $$
  n_i\cdot w\ge D\sin\rho
  $$
  for every unit local contact-opening tangent `w`;
- every member of `E_D^{wide}(rho)` is, for sufficiently large `D`, a genuine pair of vertex-disjoint crossing actual diameter chords whose projective crossing angle is at least `rho`.

Thus the final positive-density obstruction can be requested at **any fixed angular margin below `c_0/6`**, with an explicit linear loss `6 rho D` in guaranteed population.  The earlier `rho=c_0/32` theorem is one corollary rather than a special scale built into the geometry.

---

## 1. Start from the unstrengthened linear fork

The corrected linear-shore theorem gives

$$
\boxed{
|E_D|+|U_D|>c_0D-o(D),
\qquad
c_0={113\over20{,}000{,}000},
}
\tag{RT.4}
$$

where `E_D` is the exact-antipodal good-interface set and `U_D` is the non-antipodal one-bar good-interface set.  Different interfaces on the selected hub side have disjoint switching supports, so chosen blocker bars at different interfaces are distinct.

All selected row projective directions lie in one interval of width

$$
\omega_D=o(1)
\tag{RT.5}
$$

about a projective phase `psi_D`.

---

## 2. Only `4 rho D+o(D)` TB1 bars can fail the `rho` interior margin

For each `i in U_D`, choose one TB1 switching diameter bar `h_i` with inward vector `n_i`.  Call it `rho`-boundary-near when

$$
d_{\mathbb{RP}^1}([n_i],\psi_D)<2\rho.
\tag{RT.6}
$$

The projective ball in (RT.6) has length `4 rho`.  Canonical C67 gives separation

$$
\delta_D=2\arcsin{1\over2D}\ge{1\over D}
\tag{RT.7}
$$

between distinct actual diameter directions.  Therefore the number of boundary-near chosen bars is at most

$$
1+{4\rho\over\delta_D}
\le1+4\rho D.
\tag{RT.8}
$$

Because `omega_D=o(1)`, eventually every local boundary projective ray is within `rho` of `psi_D`.  Hence a chosen TB1 direction not counted by (RT.8) is at projective distance at least `rho` from each local cone ray.  Using its positive-cone orientation exactly as in the strong-TB1 theorem gives the ordinary interior margins

$$
\rho\le t_i\le\theta_i-\rho
\tag{RT.9}
$$

and therefore

$$
\boxed{
 n_i\cdot w\ge D\sin\rho
\quad\text{for every unit }w\text{ in the local opening cone}.}
\tag{RT.10}
$$

Let `S_D(rho)` be this strong subfamily.  Equations (RT.4) and (RT.8) imply

$$
\boxed{
|E_D|+|S_D(\rho)|
>(c_0-4\rho)D-o(D).
}
\tag{RT.11}
$$

---

## 3. Only `2 rho D+o(D)` exact-antipodal pairs can have gap below `rho`

For `i in E_D`, choose the two opposite-transverse consistently inward blockers `d_i^+,d_i^-` and put

$$
\eta_i=d_{\mathbb{RP}^1}([d_i^+],[d_i^-]).
\tag{RT.12}
$$

The common one-sided switch theorem supplies one linear functional `phi` with

$$
\phi(n_h)>0
\tag{RT.13}
$$

for every switching bar on the shore.  Hence every consistently inward switching direction lies in one common open semicircle.  At an exact-antipodal interface the nonzero axial reaction is a positive combination of those switching vectors, so after choosing the sign of the row direction according to that axial reaction, the row direction lies in the same open semicircle.

The opposite-transverse signs place that oriented row direction strictly between the two blocker directions inside the semicircle.  If their projective gap satisfies

$$
\eta_i<\rho,
\tag{RT.14}
$$

then exactly the same open-semicircle dichotomy as in the fixed-angle theorem gives one of two alternatives:

1. both blocker projective directions lie within `rho` of the row projective direction; or
2. both lie within `rho` of the single projective boundary line `kappa_D=ker phi` of the common semicircle.

The first population lies in the `rho`-neighborhood of the shrinking row window, of length at most

$$
\omega_D+2\rho.
\tag{RT.15}
$$

The second lies in one projective ball of length `2 rho`.  Thus all blockers from `rho`-narrow exact-antipodal interfaces lie in a union of at most two projective arcs of total length

$$
\ell_D\le\omega_D+4\rho.
\tag{RT.16}
$$

If there are `N_D(rho)` such interfaces, switching-support disjointness makes their `2N_D(rho)` blocker edges distinct.  C67 therefore gives

$$
2N_D(\rho)
\le2+{\omega_D+4\rho\over\delta_D}
\le2+D\omega_D+4\rho D,
$$

so

$$
\boxed{
N_D(\rho)\le2\rho D+o(D).
}
\tag{RT.17}
$$

Let

$$
E_D^{\rm wide}(\rho):=\{i\in E_D:\eta_i\ge\rho\}.
\tag{RT.18}
$$

Subtracting (RT.17) from (RT.11) proves (RT.2).

---

## 4. Wide exact-antipodal pairs are genuine crossing pairs

The full-source circumradius theorem gives the shared-endpoint diameter-star angle bound

$$
\Theta_D
=(4\,3^{1/8}+o(1))D^{-1/4}
\longrightarrow0.
\tag{RT.19}
$$

For fixed `rho>0`, eventually `Theta_D<rho`.  Hence the two blockers at every interface in `E_D^{wide}(rho)` cannot share an endpoint.  They are vertex-disjoint actual diameter edges, so the convex geometric-thrackle property makes them cross.  Their crossing angle is their projective direction gap and is therefore at least `rho`.

Thus

$$
\boxed{
 i\in E_D^{\rm wide}(\rho)
 \Longrightarrow
 \text{a crossing two-chord dipole of angle at least }\rho.}
\tag{RT.20}
$$

No quantitative KKT multiplier floor is used.

---

## 5. Useful calibrated choices of `rho`

The parameterized theorem lets a later closing argument choose density versus angular robustness according to the currency it can charge.

### Density-heavy choice: `rho=c_0/32`

This recovers the previous fixed theorem:

$$
 c_0-6\rho={13c_0\over16},
\qquad
{c_0-6\rho\over2}={13c_0\over32}.
\tag{RT.21}
$$

Numerically,

$$
\rho=1.765625\times10^{-7},
\qquad
{c_0-6\rho\over2}=2.2953125\times10^{-6}.
$$

### Linear angle-density product choice: `rho=c_0/12`

If a future contradiction charges one power of the angular margin, the crude guaranteed product

$$
\rho\,{c_0-6\rho\over2}
\tag{RT.22}
$$

is maximized at

$$
\boxed{\rho={c_0\over12}.}
\tag{RT.23}
$$

At that scale

$$
 c_0-6\rho={c_0\over2},
\qquad
{c_0-6\rho\over2}={c_0\over4},
\tag{RT.24}
$$

so one robust mechanism has more than

$$
1.4125\times10^{-6}D-o(D)
$$

interfaces, each with angular margin

$$
4.708333333\times10^{-7}.
$$

### Quadratic angle-density product choice: `rho=c_0/9`

If a future argument charges an angular-square currency, the crude product

$$
\rho^2\,{c_0-6\rho\over2}
\tag{RT.25}
$$

is maximized at

$$
\boxed{\rho={c_0\over9}.}
\tag{RT.26}
$$

Then

$$
 c_0-6\rho={c_0\over3},
\qquad
{c_0-6\rho\over2}={c_0\over6},
\tag{RT.27}
$$

so one robust mechanism has more than

$$
9.416666667\times10^{-7}D-o(D)
$$

interfaces with angular margin

$$
6.277777778\times10^{-7}.
$$

These optimizations are only calibrations of the proved linear tradeoff; they do not assert that either product is itself a canonical global currency.

---

## 6. Wide-antipodal bundle extraction at arbitrary `rho`

The source-wide diameter-degree estimate is

$$
\Delta(H)\le(4\,3^{1/8}+o(1))D^{3/4}.
\tag{RT.28}
$$

If the `E_D^{wide}(rho)` side is the winning side of (RT.3), then it has more than

$$
{c_0-6\rho\over2}D-o(D)
$$

interfaces.  Treat each crossing pair as one four-endpoint bundle.  The usual conflict-graph greedy extraction gives at least

$$
\boxed{
\left(
{c_0-6\rho\over32\,3^{1/8}}-o(1)
\right)D^{1/4}
}
\tag{RT.29}
$$

bundles with mutually disjoint endpoint sets.  All selected diameter edges are then pairwise crossing, while every tagged pair retains crossing angle at least `rho`.

Thus the angular margin can be carried through the existing growing matching/braid extraction at every fixed scale allowed by (RT.1).

---

## 7. Frontier effect

The remaining high-`t` obstruction is not tied to one arbitrarily chosen small constant.  It satisfies a continuum of quantitative robust alternatives:

```text
for every fixed 0 < rho < c0/6,

  fixed-angle exact-antipodal crossing dipoles
  OR
  fixed-interior-margin one-bar blockers

occupy together > (c0 - 6 rho) D - o(D) interfaces,

and one side occupies > (c0 - 6 rho)D/2 - o(D).
```

This is useful because any future global order, endpoint, or angular-energy inequality can choose `rho` after its own quantitative scale is known.  The next closing target remains to charge one of these robust populations against the ordered common train-cut caterpillar and the near-triangular transverse rectangle.

No C-II or Level-I closure is claimed.

**Disposition:** generalized the fixed robust high-`t` fork to an explicit angle-density tradeoff valid at every fixed `rho<c_0/6`, with calibrated linear- and quadratic-angular scales and matching extraction. C-II and Level I remain open.
