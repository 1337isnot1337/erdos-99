> Generated reading edition · [exact source](../../research/target_c_outer_route_direction_concentration_2026-09-14.md) · source SHA-256 `c62bc9905331054d2ca7a13a87db95c9ee9f6d27caf2f7b086d3c9858823bbf6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c9f42d2dcd212c4c0349d9216cb621d843679ffc", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_outer_route_direction_concentration_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8e03930569cc9bf4975e4951c8bf251101c4c66cabb96a5627498836c2ece66c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — outer-route direction concentration and a physical low-`t` boundary dichotomy

**Date:** 2026-09-14  
**Repository base:** `d6d1281dfc1d249a3a0dd6ef7291f3abee97fa23`  
**Status:** proved proof-only source-level reduction; theorem-state authority unchanged  
**Scope:** finite outer-route geometry plus the current Type-II low-`t` tooth/long-side split  
**LEVEL I STATUS:** `STILL OPEN`

The outer-tooth/long-side theorem leaves two formally different branches. The tooth
branch is now physical: shallow-tooth apex injectivity forces a linear family of
strongly inward unit contacts. This note gives the long-side branch an equally
physical interpretation.

The key observation is exact and finite. Metric outer detour is the total directional
energy of the distinguished unit-contact routes relative to their loaded-hull chords.
Thus small outer detour forces almost every outer-route edge occurrence to point close
to its corresponding loaded-hull side. A linear amount of side length above two then
produces a linear family of distinct near-tangent physical contact edges.

## 1. Exact directional-energy identity

For consecutive loaded force-hull vertices `b_i,b_{i+1}`, write

$$
s_i:=|b_i-b_{i+1}|,
\qquad
u_i:={b_{i+1}-b_i\over s_i},
$$

and orient the distinguished outer-face contact route `W_i` from `b_i` to
`b_{i+1}`. If its unit edge-occurrence vectors are

$$
v_{i,1},\ldots,v_{i,\ell_i},
\qquad |v_{i,j}|=1,
$$

then

$$
\sum_{j=1}^{\ell_i}v_{i,j}=s_i u_i.
$$

Taking the scalar product with `u_i` gives

$$
\ell_i-s_i
=\sum_{j=1}^{\ell_i}(1-v_{i,j}\cdot u_i).
\tag{DC.1}
$$

Let `theta_{i,j} in[-pi,pi]` be the oriented angle from `u_i` to `v_{i,j}`. Then

$$
\boxed{
\ell_i-s_i
=\sum_{j=1}^{\ell_i}(1-\cos\theta_{i,j}).
}
\tag{DC.2}
$$

Summing over the distinguished outer-route partition gives the exact finite identity

$$
\boxed{
d_{out}:=b-\operatorname{per}(F)
=\sum_i\sum_{j=1}^{\ell_i}(1-\cos\theta_{i,j}).
}
\tag{DC.3}
$$

No simplicity of the route is required. Bridge excursions and repeated articulation
occurrences are already included with outer-walk multiplicity.

## 2. Angular tail bound

Fix `beta in(0,pi)`. Let `A_beta` be the number of outer-route edge occurrences for
which

$$
|\theta_{i,j}|\ge\beta.
$$

Every such occurrence contributes at least `1-cos(beta)` to (DC.3). Hence

$$
\boxed{
A_\beta\le {d_{out}\over1-\cos\beta}.
}
\tag{DC.4}
$$

This is a deterministic Markov bound for physical contact-edge directions. It uses no
stress coefficient and no face-area estimate.

## 3. Long-side mass forces distinct near-tangent contacts

Let

$$
J:=\{i:s_i>2\},
\qquad
L_{>2}:=\sum_{i\in J}(s_i-2).
$$

The number of outer-route edge occurrences belonging to these long-side intervals is

$$
M_J:=\sum_{i\in J}\ell_i.
$$

Since `ell_i>=s_i`,

$$
M_J\ge\sum_{i\in J}s_i
=2|J|+L_{>2}
\ge L_{>2}.
\tag{DC.5}
$$

Delete every occurrence counted by `A_beta`. At least

$$
L_{>2}-{d_{out}\over1-\cos\beta}
$$

occurrences remain on long-side routes with oriented angle strictly less than `beta`
from the corresponding loaded-hull side.

An undirected edge has at most two occurrences in one face-boundary walk: one for each
side of the embedded edge. Therefore, if `E_tan(beta)` denotes the number of distinct
physical contact edges represented by these remaining occurrences,

$$
\boxed{
E_{tan}(\beta)
\ge {1\over2}
\left(
L_{>2}-{d_{out}\over1-\cos\beta}
\right)_+.
}
\tag{DC.6}
$$

This is again finite. It converts the metric long-side currency directly into
physical unit contacts rather than another scalar ledger variable.

## 4. Current low-`t` long-side corollary

At the present proof-only floor `t=t_42`, the low-`t` squeeze gives

$$
{d_{out}\over D}\le0.002883975+o(1),
$$

and the outer-tooth/long-side dichotomy gives the long-side alternative

$$
{L_{>2}\over D}\ge
0.4363893718701161781\ldots-o(1).
\tag{DC.7}
$$

Choose

$$
\beta={\pi\over6}.
$$

Then `1-cos(beta)=1-sqrt(3)/2`, and (DC.4) permits at most

$$
\boxed{
{A_{\pi/6}\over D}
\le0.02152628245551690578\ldots+o(1)
}
\tag{DC.8}
$$

bad outer-route occurrences. Therefore (DC.6) gives

$$
\boxed{
{E_{tan}(\pi/6)\over D}
\ge0.2074315447072996361\ldots-o(1).
}
\tag{DC.9}
$$

So the long-side branch contains at least `0.2074D-o(D)` distinct outer-face unit
contacts whose oriented directions lie within 30 degrees of the corresponding long
loaded-hull side.

## 5. Unified physical boundary dichotomy at the current floor

The exact tooth/long-side burden gives

$$
\max\{N_2,L_{>2}\}
\ge0.4363893718701161781\ldots D-o(D).
$$

If the tooth alternative holds, shallow-tooth apex injectivity with `eta=1/15` gives

$$
{E_{pen}\over D}
\ge0.1965648734350580890\ldots-o(1),
$$

where every selected penetration contact has inward normal component greater than

$$
{29\sqrt3-\sqrt{59}\over60}
=0.7091387945271472222\ldots .
$$

If the long-side alternative holds, (DC.9) gives

$$
{E_{tan}(\pi/6)\over D}
\ge0.2074315447072996361\ldots-o(1).
$$

Hence every current-floor low-`t` survivor satisfies the following purely physical
contact-edge alternative:

$$
\boxed{
\begin{array}{ll}
\text{either}&\ge0.1965648734D-o(D)\text{ distinct strongly inward contacts},\\[2mm]
\text{or}&\ge0.2074315447D-o(D)\text{ distinct near-tangent outer contacts}.
\end{array}
}
\tag{DC.10}
$$

In particular, regardless of branch, at least

$$
\boxed{0.1965648734350580890\ldots D-o(D)}
$$

distinct unit contacts belong to one of two explicit robust geometric families.

## 6. Frontier effect

This removes the interpretation of the long-side branch as merely a rounded scalar
endpoint. Both sides of the low-`t` split now force linear populations of actual
contact edges with quantitative directions.

The remaining gap is therefore sharper. A closure theorem may now target a common
weight-free statement for these two contact families, for example:

1. a phase-boundary incidence theorem saying that either a strongly inward contact or
   a near-tangent long-side contact consumes a controlled amount of coherent-rhombic
   train capacity;
2. a Woodall-thrackle angular theorem coupling the near-tangent outer family to the
   almost-extremal loaded diameter graph; or
3. a simultaneous boundary deformation in which either family supplies a linear set
   of independently usable first-order constraints.

A scalar optimization over `N_2` versus `L_{>2}` is no longer the useful next step.

## 7. Reproducibility

Run

```bash
python3 research/verify_target_c_outer_route_direction_concentration.py
```

for the Decimal certificate of the displayed constants.
