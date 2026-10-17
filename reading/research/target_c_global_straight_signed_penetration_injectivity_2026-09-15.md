> Generated reading edition · [exact source](../../research/target_c_global_straight_signed_penetration_injectivity_2026-09-15.md) · source SHA-256 `5de32ad24ee628bf0c945ef633d3a825804d1f0fc19d3dd23192a6db21eafc3f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "90929278feaf9d8afb3ee4c018c8825ea2edd579", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_global_straight_signed_penetration_injectivity_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4fa8268089d577e03f32fec59640d55d80cbb9373492341e0134212f033efedc"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — signed outer penetration removes the final factor two

**Date:** 2026-09-15  
**Repository base:** branch after `81dc88499e74c8d43b070948b08eea71cd2e303e`  
**Status:** proof-only Type-II strengthening; theorem-state authority unchanged  
**Scope:** no-container/full-core Type-II low-`t` branch  
**LEVEL I STATUS:** `STILL OPEN`

The bridge-free global straight-event theorem still divides selected incidences by two because, abstractly, one physical contact could be selected from both endpoints. In the actual Type-II near-disk geometry that cannot happen.

The missing ingredient is orientation. A straight internal occurrence lies on the occurrence-counted outer-face walk. Its extra contact is not merely transverse to the loaded-hull chord: it points to the **core side** of the outer walk, hence has a signed inward component greater than `1/2` relative to that loaded-hull side. If one physical edge were selected at both endpoints, its two associated loaded-hull inward normals would have to differ by more than `60` degrees.

Near-disk geometry then puts the midpoints of those two loaded-hull sides at distance at least `D/2-o(D)`. But the selected edge has length one, so the two distinguished outer routes would have to travel a combined extra length `D-o(D)`. This contradicts the current low-`t` bound

$$
d_{out}\le0.002883975D+o(D).
$$

Therefore the local occurrence selections are globally edge-injective. The current endpoint consequently forces

$$
\boxed{1.2805354256993147\ldots D-o(D)}
$$

distinct signed inward penetration contacts, twice the bridge-free count.

---

## 1. Orientation convention

Orient the occurrence-counted boundary walk of the unbounded contact face once and for all. Choose its orientation so that the unbounded face lies locally on the left of every directed edge occurrence. Then the loaded force-hull vertices encountered on their distinguished occurrences appear in clockwise cyclic order.

For consecutive distinguished loaded vertices `b_i,b_{i+1}`, write

$$
u_i={b_{i+1}-b_i\over s_i},
\qquad
s_i=|b_i-b_{i+1}|,
$$

and let `n_i` be the unit normal to the loaded-hull side pointing into the convex force hull. With the chosen clockwise orientation, `n_i` is the right normal to `u_i`.

Let

$$
W_i:b_i\leadsto b_{i+1}
$$

be the corresponding distinguished outer route, oriented as part of the outer-face walk.

At every occurrence on `W_i`, the outer-face sector is on the left side of the oriented route and the contact core is on the complementary side. Thus, at a near-straight occurrence, the core side is the side of the chord direction containing `n_i`.

This statement is occurrence-level and remains valid at articulation vertices: different occurrences correspond to different outer-face sectors, each with the unbounded face on the designated side of its directed boundary pair.

---

## 2. Straight extra contacts have a signed inward component

Fix

$$
0<\beta\le\pi/6.
$$

Consider a `beta`-straight internal occurrence at a physical vertex `x` on `W_i`. Let `v_-` be the oriented incoming route-edge vector and `v_+` the oriented outgoing vector. Then

$$
\angle(v_-,u_i)<\beta,
\qquad
\angle(v_+,u_i)<\beta.
\tag{SI.1}
$$

The two contact rays at `x` along the route are `-v_-` and `v_+`. The outer-face sector between them lies on the exterior/left side. Every extra contact edge lies in the complementary core/right sector.

Triangle-freeness makes every extra contact ray have angular distance strictly greater than `pi/3` from both route rays. The core-side angular interval is therefore contained in the cone around `n_i` bounded by the two extremal rays obtained after removing `pi/3` neighborhoods of the route rays. Consequently every extra contact `xw` satisfies the **signed** estimate

$$
\boxed{
(w-x)\cdot n_i
>\sin(\pi/3-\beta).
}
\tag{SI.2}

For

\[
\beta=\pi/6,
$$

this gives

$$
\boxed{(w-x)\cdot n_i>1/2.}
\tag{SI.3}

This strengthens the absolute-transverse estimate in the current global theorem by fixing the sign from the outer-face orientation.

---

## 3. Double selection forces far-separated hull normals

Use the current local system-of-distinct-representatives theorem at every physical vertex: one distinct extra contact incidence is selected for each straight occurrence at that vertex.

Suppose one physical edge `xy` were selected at both endpoints. Let the occurrence at `x` belong to route `W_i` and the occurrence at `y` belong to route `W_j`. Put

\[
e=y-x,
\qquad |e|=1.
$$

Equation (SI.3) at `x` gives

$$
e\cdot n_i>1/2.
\tag{SI.4}
$$

At `y` the selected directed contact is `x-y=-e`, so

$$
(-e)\cdot n_j>1/2,
$$

or

$$
e\cdot n_j<-1/2.
\tag{SI.5}
$$

If `i=j`, (SI.4)--(SI.5) are already contradictory. Hence `i!=j`.

For two unit normals to satisfy (SI.4)--(SI.5), their angular separation must be strictly greater than `pi/3`. Indeed `n_i` lies within angle `<pi/3` of `e`, while `n_j` lies within angle `<pi/3` of `-e`; the two open caps are separated by angle `pi/3`.

Thus

$$
\boxed{\angle(n_i,n_j)>\pi/3.}
\tag{SI.6}

---

## 4. Near-disk geometry separates the two loaded-hull sides by `D/2-o(D)`

Let `M_i,M_j` be the Euclidean midpoints of the loaded-hull sides

\[
b_i b_{i+1},
\qquad
b_j b_{j+1}.
$$

Canonical Type-II near-disk geometry gives centers `o_D` and errors `epsilon_D=o(D)` with

$$
B(o_D,D/2-\epsilon_D)
\subset F_D
\subset B(o_D,D/2+\epsilon_D).
\tag{SI.7}
$$

For a hull side, its inward/outward support normal is `o(1)`-aligned with the radial direction at every point of that side. In particular

$$
|M_r-o_D|=D/2+o(D)
$$

and the angle between `M_r-o_D` and the corresponding side normal is `o(1)`, uniformly in the side index `r`.

Equation (SI.6) therefore gives

$$
\angle(M_i-o_D,M_j-o_D)
>\pi/3-o(1).
$$

The chord formula yields

$$
\boxed{|M_i-M_j|\ge D/2-o(D).}
\tag{SI.8}

No quantitative Hausdorff rate is required.

---

## 5. A unit edge between the two routes would cost `D-o(D)` detour

Let

\[
\ell_i=|W_i|,
\qquad
\ell_j=|W_j|
$$

be the occurrence-counted route lengths, and define their individual detours

$$
d_i:=\ell_i-s_i,
\qquad
d_j:=\ell_j-s_j.
\tag{SI.9}

Both are nonnegative, and

\[
\sum_r d_r=d_{out}.
\tag{SI.10}

At the occurrence of `x` on `W_i`, one of the two route endpoints is reached along at most `ell_i/2` unit edges. Since the side midpoint lies `s_i/2` from either loaded endpoint,

\[
|x-M_i|
\le {\ell_i+s_i\over2}
=s_i+{d_i\over2}.
\tag{SI.11}

Similarly,

\[
|y-M_j|
\le s_j+{d_j\over2}.
\tag{SI.12}

Since `|x-y|=1`,

\[
|M_i-M_j|
\le s_i+s_j+1+{d_i+d_j\over2}.
\tag{SI.13}

Canonical Type-II interface collapse proves the largest loaded force-hull side is uniformly sublinear:

\[
\max_r s_r=o(D).
\tag{SI.14}

Insert (SI.8) and (SI.14) into (SI.13):

\[
{D\over2}-o(D)
\le o(D)+1+{d_i+d_j\over2}.
$$

Therefore

$$
\boxed{d_i+d_j\ge D-o(D).}
\tag{SI.15}

By (SI.10), any doubly selected edge would force

\[
\boxed{d_{out}\ge D-o(D).}
\tag{SI.16}

---

## 6. Low-`t` detour excludes every double selection

At the current low-`t` endpoint, the network squeeze gives

\[
{d_{out}\over D}\le0.002883975+o(1).
\tag{SI.17}

Equations (SI.16)--(SI.17) are incompatible for all sufficiently large `D`.

### Theorem SI.1 — global occurrence-to-edge injectivity

For all sufficiently large low-`t` Type-II survivors, after making the current local occurrence-injective selections, no physical contact edge is selected at both endpoints.

Since the local selection is already injective among multiple occurrences at one endpoint, the global map from straight occurrences to selected physical contacts is injective:

\[
\boxed{E_\perp(\beta)\ge S_\beta.}
\tag{SI.18}

For `beta=pi/6`, every selected edge also satisfies the signed inward estimate (SI.3).

---

## 7. Finite/asymptotic count after injectivity

The current global directional-energy theorem gives

\[
S_\beta
\ge x_B-{2d_{out}\over1-\cos\beta}.
\tag{SI.19}

Together with (SI.18),

\[
\boxed{
E_\perp(\beta)
\ge x_B-{2d_{out}\over1-\cos\beta}
}
\tag{SI.20}

for all sufficiently large members of the low-`t` Type-II sequence.

Normalize as before:

\[
{x_B\over D}
=\pi+\delta-t-\kappa+o(1).
$$

At `beta=pi/6`, put

$$
A={2\over1-\sqrt3/2}-1
=7+4\sqrt3.
$$

Then

$$
\boxed{
\liminf {E_\perp\over D}
\ge
\pi-t-\kappa-A\delta.
}
\tag{SI.21}

Under the low-`t` joint constraint

\[
2\delta+\kappa/2\le R(t),
$$

the same endpoint optimization gives

$$
\delta=R(t)/2,
\qquad \kappa=0,
$$

and therefore

$$
\boxed{
\liminf {E_\perp\over D}
\ge
\pi-t-
\left({7\over2}+2\sqrt3\right)R(t).
}
\tag{SI.22}

---

## 8. Current endpoint

At

\[
t=t_{42}=1.8208886379794447\ldots,
\qquad
R(t)=0.00576795,
$$

(SI.22) gives

\[
\boxed{
{E_\perp\over D}
\ge
1.28053542569931472276048\ldots-o(1).
}
\tag{SI.23}

Thus the current low-`t` survivor must contain more than `1.2805D` **distinct** unit contacts, each attached to a straight internal outer occurrence and pointing at least one half-unit inward relative to that occurrence's loaded-hull side normal.

This is exactly twice the bridge-free absolute-transverse floor, because the only remaining factor two has been eliminated geometrically rather than by another incidence estimate.

---

## 9. What remains

The selected contacts are now globally distinct, but they need not be vertex-disjoint and need not lie on distinct stopped trains. A one-cell-thick rhombic strip can still place many such inward contacts on one train family.

The next live theorem is therefore a true train-occupancy statement. The selected edges must be partitioned by their stopped trains and by whether the adjacent outer-face shoulders are strict rhombi or exceptional faces. A valid closure route must show that either

1. more than `1.2805D` signed penetrations consume too many distinct train/interface resources, or
2. their concentration into long rhombic strips creates a macroscopic coherent corridor incompatible with the near-extremal diameter thrackle or with global minimality.

No such final occupancy theorem is claimed here. C-II remains open.