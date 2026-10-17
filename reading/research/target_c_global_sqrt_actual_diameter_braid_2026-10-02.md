> Generated reading edition · [exact source](../../research/target_c_global_sqrt_actual_diameter_braid_2026-10-02.md) · source SHA-256 `8b981cf9551710928797f20c90264cc812b70f046e1cda5c0ac3692e5f63b2e2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9252f21d030f2354f41c7fd8c6cdfe8f4ad2189e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_global_sqrt_actual_diameter_braid_2026-10-02.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "db51c76da4e6b777388e57bfbb787a6548a5f42ddb8a4b734cf4aaa30f5479fd"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: global square-root actual-diameter braid

Date: 2026-10-02

Status: proof-only candidate on current remote main \`3bad7c12bf5133665be466d0396362108fadef2c\`. Level I and C-II remain open.

## 1. Inputs

This note combines two results already present on current main.

First, \`docs/reports/target_c_global_diameter_star_cubic_budget_2026-10-02.md\` proves the following unreviewed incidence theorem. For the full actual diameter graph $`H`$, define
```math
a_D=2\arcsin\frac1{2D},\qquad
\mathcal B_D=\frac{12\pi\sqrt3}{D a_D^3}.
```
If a set $`S`$ of $`N`$ actual diameter vertices receives $`J`$ endpoint incidences from a specified family of actual diameter edges, then
```math
(J-N)_+^3<\mathcal B_D N^2. \tag{1}
```
It also gives
```math
\mathcal B_D/D^2\to12\pi\sqrt3. \tag{2}
```

Second, \`docs/reports/target_c_full_source_midpoint_energy_2026-10-02.md\` proves, also as an unreviewed candidate, that one point $`s`$ satisfies
```math
\left|\frac{p+q}{2}-s\right|<\frac32D^{2/3} \tag{3}
```
for every actual source diameter $`pq`$.

Canonical ZF supplies
```math
h:=|E(H)|\ge\lceil D\rceil. \tag{4}
```

The deduction below inherits the unreviewed status of (1)-(3). No KKT multiplier floor is assumed.

## 2. Global square-root matching

### Theorem 2.1

Along every unbounded canonical post-ZF C-II sequence,
```math
\boxed{
\nu(H)\ge
\left(\frac{1}{2\sqrt{12\pi\sqrt3}}-o(1)\right)\sqrt D.
} \tag{5}
```

### Proof

Take a maximal matching $`M`$ in $`H`$. Let $`S`$ be its endpoint set and put
```math
\nu=|M|,\qquad N=|S|=2\nu.
```
Maximality makes $`S`$ a vertex cover: if an edge had both endpoints outside $`S`$, it could be added to $`M`$.

Use all actual diameter edges as the edge family in (1), and let
```math
J=\sum_{v\in S}d_H(v)
```
be their endpoint incidence count on $`S`$. Since $`S`$ is a vertex cover, every edge contributes at least one incidence, so
```math
J\ge h\ge D. \tag{6}
```

If $`N/D`$ does not tend to zero on a subsequence, then $`N/\sqrt D\to\infty`$ there and (5) is automatic. Otherwise pass to a subsequence with $`N/D\to0`$. For large $`D`$, $`N<D\le J`$, and (1), (6) imply
```math
(D-N)^3\le(J-N)^3<\mathcal B_DN^2. \tag{7}
```
Divide by $`D^3`$:
```math
\left(1-\frac ND\right)^3
<
\frac{\mathcal B_D}{D^2}\frac{N^2}{D}. \tag{8}
```
Using (2) and $`N/D\to0`$,
```math
\liminf\frac{N}{\sqrt D}\ge\frac1{\sqrt{12\pi\sqrt3}}. \tag{9}
```
Since $`N=2\nu`$, (5) follows. QED.

There is also a direct finite form. If $`N\le D/2`$, then (7) gives
```math
\nu(H)=N/2>\frac{\sqrt D}{2\sqrt{96\pi\sqrt3}}. \tag{10}
```
If $`N>D/2`$, then $`\nu(H)>D/4`$.

This improves the old global post-ZF matching scale $`\Omega(D^{1/4})`$, and also the $`\Omega(D^{1/3})`$ bound obtained by discarding the cubic moment down to a maximum-degree estimate. The gain comes from applying the full incidence theorem to the vertex cover produced by a maximal matching.

## 3. Exact crossing braid order

Distinct edges of $`M`$ have disjoint endpoints. The actual planar diameter graph is a convex geometric thrackle, so every two edges of $`M`$ cross properly.

The crossing family has an exact cyclic order.

### Lemma 3.1

Let $`k\ge2`$ pairwise properly crossing straight chords have $`2k`$ distinct endpoints in strictly convex position. Label the endpoints cyclically as
```math
x_0,x_1,\ldots,x_{2k-1}.
```
After a cyclic relabeling,
```math
\boxed{M=\{x_ix_{i+k}:0\le i<k\}.} \tag{11}
```

### Proof

Fix one chord $`xy`$. Every other chord crosses $`xy`$, so it has one endpoint in each of the two open boundary arcs cut off by $`x,y`$. Hence each arc contains at least $`k-1`$ selected endpoints. There are exactly $`2k-2`$ selected endpoints other than $`x,y`$, so each arc contains exactly $`k-1`$. Therefore the endpoints of every matching chord are separated by exactly $`k-1`$ selected endpoints on either side. This is exactly the offset-$`k`$ pairing (11). QED.

Actual diameter endpoints are strict source-hull vertices, so Lemma 3.1 applies. Thus every sufficiently large canonical post-ZF survivor contains an exact two-shore actual-diameter braid of size
```math
k\ge\left(\frac{1}{2\sqrt{12\pi\sqrt3}}-o(1)\right)\sqrt D. \tag{12}
```
No threshold staircase, train extraction, or exact-phase hypothesis is needed.

For any two braid edges, the disjoint-diameter gap theorem on current main gives projective direction separation at least
```math
4\arcsin\frac1{2D}. \tag{13}
```

## 4. Common midpoint core

Apply (3) to every braid edge $`x_ix_{i+k}`$. All braid midpoints lie in
```math
\boxed{B\!\left(s,\frac32D^{2/3}\right).} \tag{14}
```
Equivalently,
```math
\boxed{|x_{i+k}-(2s-x_i)|<3D^{2/3}.} \tag{15}
```
After scaling by $`D`$, the two cyclic shores are paired by central reflection about $`s/D`$ with error $`O(D^{-1/3})`$, while the number of paired endpoints is $`\Omega(\sqrt D)`$.

Thus current main yields a global ordered, separated, near-centrally-reflected actual-diameter braid, rather than only an unstructured growing matching.

## 5. Remaining obstruction

This is support geometry, not stress control. Relative-interior KKT positivity gives no uniform lower bound on the total diameter multiplier carried by this braid. Regular odd-shell regressions already show why a large near-centered crossing matching alone is not a contradiction.

A closing use of (11)-(15) must couple the braid endpoints to the actual loaded/contact graph and the aggregate outer-walk currency, or construct a source-preserving finite motion that shortens all relevant active diameters, or force an exact unit triangle from the ordered two-shore geometry.

No computation or verifier is used in this note.
