> Generated reading edition · [exact source](../../research/target_c_outer_walk_near_simplicity_2026-09-15.md) · source SHA-256 `7163d20854729774ec1b662ed4908a71d1173c29d7dc92bdd7fd615381364c94`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "22bc2b0fed35eb0313f5b8f54d966cb6b9f58a98", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_outer_walk_near_simplicity_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7834a81f731b04463d25245b10c1138a931f16314773a2414ac358df88bdebe9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — low-detour outer walk is almost simple

**Date:** 2026-09-15  
**Repository base:** `494b8b7cd3a2fe4120e673f09a46072e74b9a917`  
**Status:** proved proof-only consequence of global straight events plus bridge suppression; theorem-state authority unchanged  
**Scope:** fully force-visible, no-container/full-core Type-II low-`t` branch  
**LEVEL I STATUS:** `STILL OPEN`

The global straight-event theorem forces more than `1.28D` locally near-straight
internal occurrences on the distinguished outer routes. A priori one physical
articulation vertex could be visited twice and absorb two of those occurrences. The
angular geometry of two straight outer-face sectors sharply restricts that
multiplicity: any physical vertex supporting two straight occurrences has contact
degree exactly three and is therefore incident to a bridge. Full-core near-disk
isoperimetry makes the bridge population tiny.

Consequently almost every straight occurrence occurs at a different physical unloaded
vertex. At the current endpoint there are at least

$$
\boxed{1.2776514506993147\ldots D-o(D)}
$$

distinct unloaded straight outer vertices, and the entire outer-face walk contains at
least

$$
\boxed{3.0985400886787594\ldots D-o(D)}
$$

distinct physical vertices. Equivalently, fewer than about `1.461%` of outer-walk
occurrences can be lost to repetition or to the nonstraight residue at the current
worst low-`t` point.

## 1. Straight-event notation

Fix

$$
0<\beta\le\pi/6,
\qquad
c_\beta:=1-\cos\beta.
$$

Let `S_beta` be the number of `beta`-straight internal occurrences on all Section-63
distinguished outer routes. The global directional-energy theorem gives

$$
\boxed{
S_\beta
\ge x_B-{2d_{out}\over c_\beta},
\qquad
x_B=b-q.
}
\tag{NS.1}
$$

The hostile-audited loaded-route exclusion says every internal route vertex is
unloaded, so C26 gives contact degree between three and five.

Let `V_beta` be the number of distinct physical vertices supporting at least one
`beta`-straight occurrence, and let `R_beta` be the number of physical vertices
supporting exactly two such occurrences.

The outer-sector argument already proves that one physical vertex supports at most two
straight occurrences. Therefore

$$
\boxed{V_\beta=S_\beta-R_\beta.}
\tag{NS.2}
$$

## 2. A double-straight vertex has degree exactly three

Take a physical vertex `x` supporting two distinct `beta`-straight outer-face
occurrences. Each occurrence occupies one angular outer-face sector whose measure is
strictly greater than

$$
\pi-2\beta\ge {2\pi\over3}.
\tag{NS.3}
$$

The two occurrences correspond to two distinct disjoint cyclic sectors at `x`.

Suppose `deg_C(x)>=4`. Contact-neighbor directions at a triangle-free unit-contact
vertex have pairwise cyclic separation strictly greater than `pi/3`. Hence, besides
the two straight outer sectors, the cyclic rotation at `x` contains at least two more
angular gaps, each strictly greater than `pi/3`. The total angular measure would then
be strictly larger than

$$
2\cdot{2\pi\over3}+2\cdot{\pi\over3}=2\pi,
$$

impossible. Since `x` is unloaded and internal, C26 already gives `deg_C(x)>=3`.
Therefore

$$
\boxed{\deg_C(x)=3.}
\tag{NS.4}
$$

This uses strict triangle-freeness at equality: a `pi/3` gap would make the two
corresponding contact neighbors unit distance apart and create a unit equilateral
triangle with `x`.

## 3. A double-straight vertex is incident to a bridge

A physical vertex with two distinct occurrences on one face-boundary walk is an
articulation vertex. Thus every vertex counted by `R_beta` is an articulation.

A degree-three articulation in a connected loopless graph is incident to a bridge. To
see this, decompose the graph into blocks at `x`. Since `x` lies in at least two
blocks, if every incident block were nontrivial then each would use at least two edges
incident with `x`, requiring degree at least four. Therefore one incident block is a
single bridge edge.

Let `B_br` be the number of physical contact bridges. Charging a double-straight
vertex to one incident bridge gives the safe incidence bound

$$
\boxed{R_\beta\le2B_{br},}
\tag{NS.5}
$$

because one bridge has only two endpoints.

Canonical bridge localization puts every positive contact bridge on the unbounded
face, so `B_br=B_o`, the outer-bridge count used by bridge-subtracted isoperimetry.

## 4. Full-core near-disk bridge suppression

On a convergent full-core Type-II subsequence write

$$
\delta:=\lim {d_{out}\over D}.
$$

The bridge-subtracted isoperimetric theorem, combined with full-core near-disk area
saturation and `per(F)/D->pi`, gives

$$
\boxed{
\limsup {2B_o\over D}\le\delta.
}
\tag{NS.6}
$$

Equations (NS.2), (NS.5), and (NS.6) therefore imply

$$
\liminf {V_\beta\over D}
\ge
\liminf {S_\beta\over D}-\delta.
\tag{NS.7}
$$

Using

$$
{x_B\over D}=\pi+\delta-t-\kappa+o(1),
\qquad
\kappa={k\over D},
$$

and (NS.1), this becomes

$$
\boxed{
\liminf {V_\beta\over D}
\ge
\pi-t-\kappa-{2\delta\over1-\cos\beta}.
}
\tag{NS.8}
$$

## 5. Current low-`t` distinct-vertex floor

Take `beta=pi/6`, so

$$
c_*:=1-{\sqrt3\over2}.
$$

The low-`t` network squeeze is

$$
2\delta+{\kappa\over2}\le R(t).
$$

To minimize the right side of (NS.8), maximize

$$
\kappa+{2\delta\over c_*}.
$$

As in the global contact theorem, the detour endpoint is more expensive per unit
network budget, so the worst point is

$$
\delta={R(t)\over2},
\qquad
\kappa=0.
$$

Therefore

$$
\boxed{
\liminf {V_{\pi/6}\over D}
\ge
\pi-t-{R(t)\over1-\sqrt3/2}.
}
\tag{NS.9}
$$

At the current proof-only endpoint

$$
t_{42}=1.8208886379794447041\ldots,
\qquad
R(t_{42})=0.00576795,
$$

this gives

$$
\boxed{
{V_{\pi/6}\over D}
\ge1.2776514506993147228\ldots-o(1).
}
\tag{NS.10}
$$

These are distinct physical **unloaded** vertices on the outer face, each supporting a
locally near-straight distinguished-route occurrence.

## 6. The whole outer-face walk is nearly simple

Let `V_out` be the number of distinct physical vertices incident with the unbounded
face. All `q` loaded force-hull vertices are distinct outer-face vertices, and the
vertices counted by `V_beta` are unloaded, so the two sets are disjoint. Hence

$$
V_{out}\ge q+V_\beta.
\tag{NS.11}
$$

Using (NS.8) and `q/D=t+kappa`,

$$
\boxed{
\liminf {V_{out}\over D}
\ge
\pi-{2\delta\over1-\cos\beta}.
}
\tag{NS.12}
$$

At `beta=pi/6` and `delta<=R(t)/2`,

$$
\boxed{
\liminf {V_{out}\over D}
\ge
\pi-{R(t)\over1-\sqrt3/2}.
}
\tag{NS.13}
$$

At `t=t_42`,

$$
\boxed{
{V_{out}\over D}
\ge3.0985400886787594269\ldots-o(1).
}
\tag{NS.14}
$$

Meanwhile

$$
{b\over D}=\pi+\delta+o(1)
\le3.1444766285897932385\ldots+o(1)
$$

at the same worst detour endpoint. Thus

$$
\boxed{
{b-V_{out}\over D}
\le0.0459365399110338116\ldots+o(1).
}
\tag{NS.15}
$$

and consequently

$$
\boxed{
{V_{out}\over b}
\ge0.9853913559117038\ldots-o(1).
}
\tag{NS.16}
$$

So at least `98.539%` of outer-walk occurrence mass survives as distinct physical
outer vertices at the worst current low-`t` point.

## 7. Frontier effect

The low-`t` endpoint is now simultaneously:

1. metrically near-geodesic (`d_out/D<=0.002884`);
2. locally near-straight on at least `1.2805D` internal route occurrences;
3. supported on at least `1.27765D` distinct unloaded outer vertices; and
4. almost simple as a global outer walk, with repetition/nonstraight loss below
   `0.04594D`.

This is stronger than a pure contact-edge count. It says the large transverse-contact
population from `3bedbb12` is carried by a boundary that is already close, at linear
scale, to a simple unit-edge polygon surrounding the full-core near-disk region.

C-II remains open. A useful next step is to combine this near-simple boundary with the
full-core area saturation: a nearly simple unit-edge boundary of near-isodiametric
area should strongly constrain the geometry of the `1.27765D` unloaded indenting
vertices and the trains launched through them. The current repository does not yet
contain that finite stability statement.

## 8. Reproducibility

Run

```bash
python3 research/verify_target_c_outer_walk_near_simplicity.py
```

for the displayed endpoint constants.
