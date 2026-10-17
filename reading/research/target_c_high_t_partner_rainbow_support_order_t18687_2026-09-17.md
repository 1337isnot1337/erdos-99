> Generated reading edition · [exact source](../../research/target_c_high_t_partner_rainbow_support_order_t18687_2026-09-17.md) · source SHA-256 `1c0f9aa5fedc6803a9697efd971acb1328f353399af9bacbb7235a20b7eea3a9`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "428a74fab0c67b9f64c80bafa86caa6aa023a499", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_partner_rainbow_support_order_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "23839a1b44fba801bb8b2d35a45dba2bdfd1b98047179df862a5b51e3908fd34"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the deep exact-force braid has a monotone partner-support lane

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the no-fixed-margin-TB1 exact-antipodal side through `t=(q-k)/D<=1.8687`  
**Dependencies:** phase-free O--O path coordinates and common diameter-routing hub; one-sided interval support; bilateral birth loading; parameterized deep grid-force density; disjoint deep exact-force braid; global one-sided reaction budget; convex geometric-thrackle property of actual diameter edges  
**Certificate:** `research/verify_target_c_high_t_partner_rainbow_support_order_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current deep-braid theorem gives an `Omega(D^(1/4))` family of exact-force dipoles whose four source endpoints are pairwise disjoint, whose diameter bars are all pairwise crossing, and whose two birth endpoints occur on the two ordered host arcs at the same tagged layer. It also records that every selected bar persists hubward from its birth layer, but it does not order the *other* endpoints of those bars.

The complete-crossing condition supplies that missing order.

Fix a pre-hub selected family of centers

```math
i_1<i_2<\cdots<i_M<k,
\tag{PR.1}
```

where `R_k` is the common diameter-routing hub region. At center `i_s`, relabel the two selected force bars by **birth side** rather than transverse sign:

```math
e_s^+,e_s^-.
\tag{PR.2}
```

Thus the birth endpoint of `e_s^+` lies in `C_{i_s}^+`, and the birth endpoint of `e_s^-` lies in `C_{i_s}^-`. Write the partner endpoint regions as

```math
y_s^\pm\in R_{b_s^\pm}.
\tag{PR.3}
```

One-sided hub routing gives

```math
\boxed{b_s^\pm\ge k}
\tag{PR.4}
```

and the exact support intervals are

```math
I_s^\pm=\{i_s+1,\ldots,b_s^\pm\}.
\tag{PR.5}
```

### Theorem PR — partner-rainbow support order

For every disjoint deep braid as above, after possibly exchanging the names of the two host arcs and reversing the global boundary orientation, the following hold.

1. Around the **pre-hub shore** of the common cut `tau_k`, the `2M` birth endpoints occur in the two-block order
   
   ```math
   x_M^+,x_{M-1}^+,\ldots,x_1^+,
   x_1^-,x_2^-,\ldots,x_M^-.
   \tag{PR.6}
   ```

2. Around the complementary **hubward shore**, the partner endpoints occur in the **same edge-label order**
   
   ```math
   y_M^+,y_{M-1}^+,\ldots,y_1^+,
   y_1^-,y_2^-,\ldots,y_M^-.
   \tag{PR.7}
   ```

   Here both shores are read in the same global cyclic orientation. If the two shore intervals are instead given compatible crosscut orientations, this is the usual order reversal from the ordered-thrackle theorem.
3. The corresponding region-index sequence
   
   ```math
   b_M^+,\ldots,b_1^+,b_1^-,\ldots,b_M^-
   \tag{PR.8}
   ```

   is weakly unimodal: it is a subsequence of a sequence that increases from the hub toward the far end region, may plateau in the far end region, and then decreases back toward the hub.
4. Consequently **at least one complete birth-side lane is monotone without any further thinning**:
   
   ```math
   \boxed{
   (b_1^+,\ldots,b_M^+)\text{ is monotone}
   \quad\text{or}\quad
   (b_1^-,\ldots,b_M^-)\text{ is monotone}.}
   \tag{PR.9}
   ```


For the monotone lane there is an exact interval dichotomy.

- If its `b_s` are nonincreasing with `s`, then
  
  ```math
  I_1\supseteq I_2\supseteq\cdots\supseteq I_M;
  \tag{PR.10}
  ```

  the complete lane is a nested support rainbow.
- If its `b_s` are nondecreasing with `s`, then both support endpoints advance monotonically:
  
  ```math
  i_1<i_2<\cdots<i_M,
  \qquad
  b_1\le b_2\le\cdots\le b_M;
  \tag{PR.11}
  ```

  the complete lane is a proper hub-crossing staircase. All intervals still contain the common hub cut.

Thus the previous statement

```text
synchronized bilateral births
+ arbitrary hubward partner endpoints
```

is impossible for a complete crossing braid. One entire side of the braid has globally ordered support ends.

---

## 1. Every selected bar crosses the same hub cut

The exact path coordinates are

```math
R_0\xleftrightarrow{\tau_1}R_1\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m.
\tag{PR.12}
```

On the pre-hub side, a switching bar born at `R_i` has interval start `a=i`. The common-hub theorem gives `a<=k<=b`, so for every selected bar born at `i_s<k`,

```math
I_s^\pm=\{i_s+1,\ldots,b_s^\pm\},
\qquad b_s^\pm\ge k.
\tag{PR.13}
```

Hence `tau_k` belongs to every selected support interval. Its proper crosscut splits the convex-hull boundary into two complementary cyclic intervals:

- `P`, containing every birth endpoint `x_s^\pm`;
- `Q`, containing every partner endpoint `y_s^\pm`.

The path-region support convention assigns each selected endpoint to its corresponding shore. The deep-braid extraction additionally makes all `4M` selected source endpoints pairwise distinct.

---

## 2. Bilateral birth order is a two-block word

The crosscuts `tau_1,...,tau_m` all join the same two separated host arcs. Between consecutive cuts, the internal layer `R_i` meets the hull in the two ordered subarcs `C_i^+` and `C_i^-`.

Travel once along the pre-hub boundary interval `P` in the ambient cyclic orientation. On one host arc the layer indices are encountered toward the far end, while after the pre-hub terminal boundary piece the opposite host arc is encountered in the reverse physical direction. Therefore the selected bilateral birth endpoints occur, up to the harmless global choices stated in the theorem, as

```math
x_M^+,\ldots,x_1^+,x_1^-,\ldots,x_M^-.
\tag{PR.14}
```

This is exactly the synchronized bilateral order already present in the birth-loading theorem, now written in the cyclic order of the single shore `P`.

---

## 3. A complete crossing matching transports the word exactly

Forget the pairing of the two bars at each force cell for a moment. The braid has `2M` diameter bars with pairwise disjoint endpoints, and every two bars cross geometrically.

For two complementary boundary intervals `P,Q`, let `p_1,p_2` be two endpoints in that order on `P` in the ambient cyclic orientation, and let their partners be `q_1,q_2` on `Q`. The two chords cross if and only if `q_1,q_2` occur in that same ambient cyclic order on `Q`. Otherwise their endpoints are nested rather than alternating.

Applying this pairwise to all `2M` bars shows that the partner map of a complete crossing matching is an order isomorphism between the two shore intervals in the ambient cyclic orientation. Equivalently it is an order anti-isomorphism if each shore is independently oriented from one endpoint of the crosscut toward the other.

Therefore the label word (PR.14) is transported unchanged to `Q`, proving (PR.7).

This step uses the **complete** crossing braid, not merely the fact that the two bars inside each force cell cross.

---

## 4. Region labels on the hubward shore have one peak

Now traverse the complementary hull interval `Q` in the same ambient cyclic orientation. The path topology is rigid. Starting at one endpoint of `tau_k`, the boundary passes successively through the hubward regions

```math
R_k,R_{k+1},\ldots,R_m,
\tag{PR.15}
```

on one host side, then through the far terminal boundary piece belonging to `R_m`, and then through

```math
R_m,R_{m-1},\ldots,R_k
\tag{PR.16}
```

on the other host side. A region may contribute many consecutive hull vertices, so the exact region-label word is a weakly nondecreasing sequence followed by a weakly nonincreasing sequence, with an arbitrary plateau at its maximum.

The selected partner endpoints form an ordered subsequence of this hull word. Hence

```math
b_M^+,\ldots,b_1^+,b_1^-,\ldots,b_M^-
\tag{PR.17}
```

is weakly unimodal.

The point is topological: no metric estimate, multiplier lower bound, or phase approximation is used here.

---

## 5. One full lane avoids the turning point

A weakly unimodal sequence split into two contiguous blocks has at least one monotone block. Indeed:

- if the first decrease occurs in the first block, the second block is nonincreasing;
- if it occurs in the second block, the first block is nondecreasing;
- if the maximum plateau meets the block boundary, the first block is nondecreasing and the second is nonincreasing.

Apply this to the two length-`M` blocks in (PR.17). The first block is indexed by `s=M,...,1`, so reversing that block does not destroy monotonicity. This proves (PR.9).

For the chosen lane, (PR.10)--(PR.11) are immediate from

```math
I_s=\{i_s+1,\ldots,b_s\}
```

and `i_1<...<i_M<k<=b_s`.

Thus no subfamily loss is needed to obtain an ordered support lane.

---

## 6. Coherent transverse-sign sublane and current quantitative scale

Return to the exact-force labels. At every force cell the two selected bars lie on opposite transverse sides of the coherently oriented high-`t` row axis. The monotone birth-side lane from Theorem PR chooses exactly one of those two bars at each cell. By the two-color pigeonhole principle, at least half of the lane bars have the same transverse sign.

Therefore there is a sublane of size at least

```math
\boxed{\left\lceil {M\over2}\right\rceil}
\tag{PR.18}
```

which simultaneously has:

- pairwise vertex-disjoint actual diameter bars;
- pairwise geometric crossing;
- pairwise disjoint deep exact-phase neighborhoods inherited from the parent cells;
- monotone birth indices and monotone support-end indices;
- one common transverse sign;
- the common inverse-`D` train grid inherited from the parameterized deep-cell theorem;
- the fixed local derivative margin
  
  ```math
  |\ell_h(s d^{(i)})|\ge2D|s|\sin\delta.
  \tag{PR.19}
  ```


Use the current parameterized family with

```math
\lambda=c_0-6\rho-\eta-2\delta>0,
\qquad
c_0={113\over20{,}000{,}000}.
\tag{PR.20}
```

On the growing-depth diagonal, the current conflict-graph extraction gives

```math
M>
\left({\lambda\over16\,3^{1/8}}-o(1)\right)D^{1/4}.
\tag{PR.21}
```

Hence the coherent monotone support lane satisfies

```math
\boxed{
|L_D|>
\left({\lambda\over32\,3^{1/8}}-o(1)\right)D^{1/4}.
}
\tag{PR.22}
```

For the convenient ninety-percent parameter choice

```math
\rho=\delta={c_0\over100},
\qquad
\eta={c_0\over50},
\qquad
\lambda={9c_0\over10},
\tag{PR.23}
```

this leading coefficient is

```math
\boxed{
{0.9c_0\over32\,3^{1/8}}
\approx1.38516280797\times10^{-7}.
}
\tag{PR.24}
```

As `rho,eta,delta` tend to zero through fixed admissible choices, the present density input allows the coefficient to approach

```math
\boxed{
{c_0\over32\,3^{1/8}}
\approx1.53906978663\times10^{-7}.
}
\tag{PR.25}
```

This is the current optimized scale, rather than the smaller coefficient from the first fixed-constant deep-braid extraction.

---

## 7. The monotone lane can simultaneously be globally stress-dilute

The new one-sided reaction budget can be imposed *before* the conflict-graph extraction. Fix a quantile parameter `0<sigma<1`. From the parameterized center family of density `lambda`, delete centers with

```math
B_i>{1\over\sigma\lambda D}.
\tag{PR.26}
```

The global budget deletes fewer than `sigma lambda D` centers, leaving

```math
>(1-\sigma)\lambda D-o(D)
\tag{PR.27}
```

deep grid-locked cells with

```math
\boxed{
B_i\le {1\over\sigma\lambda D},
\qquad
0<|G_i|\le {1\over\sigma\lambda}.
}
\tag{PR.28}
```

Apply the same window/endpoint conflict graph and then Theorem PR. On a diagonal with `r_D->infinity` and `r_D=o(D^(3/4))`, one obtains a coherent-sign monotone support lane with

```math
\boxed{
|L_D^{budget}|>
\left({(1-\sigma)\lambda\over32\,3^{1/8}}-o(1)\right)D^{1/4}.
}
\tag{PR.29}
```

Every retained cell still satisfies (PR.28). Moreover its exact two-ray compressed force coefficients obey the parent budget bound

```math
0<\lambda_i^\pm
\le {1\over\sigma\lambda D\sin\rho}.
\tag{PR.30}
```

Thus the ordered lane can be chosen so that its per-cell switching stress and compressed exact-force coefficients are `O(D^-1)` with constants independent of the growing exact-phase depth.

For the ninety-percent parameters (PR.23) and `sigma=1/2`,

```math
|L_D^{budget}|>
\left({0.45c_0\over32\,3^{1/8}}-o(1)\right)D^{1/4}
\approx(6.92581403985\times10^{-8}-o(1))D^{1/4},
\tag{PR.31}
```

while

```math
B_i\le {2\over\lambda D},
\qquad
|G_i|\le {2\over\lambda}
=393313.6676\ldots.
\tag{PR.32}
```

This rules out a further escape in which the newly ordered lane exists only by concentrating a growing amount of KKT stress on its cells.

---

## 8. Scope audit and frontier effect

The theorem does **not** assert that partner endpoints lie on a prescribed physical host arc. Several endpoints may lie in the same hubward region, including the far end region. What is proved exactly is the order of their path-region indices and hence the order of their laminar support ends.

It also does not contradict a regular-shell model by itself. Such a model can realize large complete crossing diameter matchings with monotone endpoint pairing.

What has changed is that the deep force braid is no longer free to choose independent support lengths cell by cell. After one fixed global choice of birth side, a whole `Omega(D^(1/4))` lane is forced into one of only two exact interval geometries:

```text
nested rainbow:
    earlier birth -> weakly later death;
    I_1 superset I_2 superset ... superset I_M

or

proper staircase:
    earlier birth -> weakly earlier death;
    both interval endpoints advance toward the far side.
```

After a factor-two thinning, the lane has one transverse force sign and the same quantitative local cusp margin. After an optional fixed reaction-quantile thinning, it simultaneously has depth-independent `O(D^-1)` switching stress. This couples the source cyclic order, the train-path support order, the common near-triangular grid, and the exact-force dipole tags at the full `D^(1/4)` scale.

The remaining closing step is now narrower: rule out one of these two monotone support-lane normal forms inside the common inverse-`D` near-triangular train grid, or show that either normal form forces an exact unit triangle or a finite/nonlocal strict diameter descent. Arbitrary partner-end scrambling and stress concentration are no longer escapes.

No C-II or Level-I closure is claimed.

**Disposition:** proved that every complete crossing deep exact-force braid has a full-size monotone partner-support lane; at the current optimized parameterized density, a coherent transverse-sign lane has size approaching `(c0/(32*3^(1/8)))D^(1/4)`, and a fixed positive fraction can simultaneously carry depth-independent `O(D^-1)` switching stress. The lane is exactly either nested or proper-staircase in its laminar support intervals. C-II and Level I remain open.
