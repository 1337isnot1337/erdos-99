<!-- theorem-state: {"artifact_id":"ART-D68C93BF1E67","canonical":true,"claim_ids":["C-SIX-SIDED-WALL-CENTRAL-VACANCY-CLASSIFICATION"],"claim_statuses":{"C-SIX-SIDED-WALL-CENTRAL-VACANCY-CLASSIFICATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.234 — central-vacancy sorting classification

**Date:** 2026-10-10
**Canonical base:** `origin/main=81b9928d2c0976a3b6a3f3843d5222fb42ea99de`, state `2026-10-09.audit.227`
**Frozen source:** `origin/research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`
**Source report:** `docs/reports/target_c_sorted_rate_packet_classification_2026-10-06.md`, SHA-256 `964e7d9dacd942e8dd5114217f271e79454a9222069fb8e125e882f281271fe4`
**Finite verifier:** `research/verify_target_c_sorted_rate_packets_2026_10_06.py`, SHA-256 `67f73a8f48757aef8a1c7aca4e4ba7c9a3803f44eea8220dfc78912e4178b061`

## Verdict

**PASS — promote only the fixed-`M` central-vacancy chart classification.** The report proves that every sufficiently small feasible placement converging to the central-vacancy triangular chart is exactly one of the finite sorting packets with its center omitted. Each packet contains `6(M-2)` interior unit triangles when `M>=3`.

This is an auxiliary local-chart theorem. It does not classify arbitrary `N-1` point placements, provide a uniform onset in `M`, or extract this chart from a canonical source. The complete-chart classification and the highest-population source conclusion in the same report are already covered more broadly by canonical fixed-profile sorting/source-exclusion claims; they are not promoted again here.

## Exact statement audited

Fix `M>=3`, put

```text
N = 3M^2 - 3M + 1
Lambda = {M-1, M-3, ..., -M+1}
```

and use the specified arithmetic six-sided curved unit wall `W_(M,theta)`, with all `6M` wall vertices included and `M` unit edges on each side. For each `theta>0`, consider any pairwise unit-separated placement consisting of those wall vertices and exactly `N-1` additional points in the closed wall. Assume a sequence `theta_k -> 0` of such placements converges, after rigid wall alignment and relabeling, to the radius-`M-1` triangular-lattice interior chart with its central site removed.

Then, for all sufficiently large `k`, the additional points are exactly a sorting packet associated with some permutation of `Lambda`, with its central site deleted. Thus the placement contains at least `6(M-2)` actual unit equilateral triangles. The onset may depend on `M`; no arbitrary one-deficit chart is covered.

## Independent reconstruction

### First-order rates

Use triangular coordinates `p=iu+jv`, with unit generators `u,v` at angle `pi/3`. On each radial axis, the ring and radial-chain rows force the first velocity to have the form

```text
d_(r e_k) = alpha_r J e_k,
t_r = alpha_(r+1) - alpha_r,  0 <= r < M,
sum_r t_r = 0.
```

Here `alpha_0:=0` is only a rate convention for the omitted center, while `alpha_M=0` follows from the zero first-order corner velocity. The missing center contributes no moving coordinate. In one sector, write the remaining first-order coordinates as `s_(r,j)`. The two non-axis unit-neighbor rows give

```text
s_(r,j) >= s_(r-1,j),
s_(r,j) >= s_(r-1,j-1) - t_(r-1),
s_(M,j) = j(M-j).
```

Following either predecessor at every layer shows that for every `j`-element subset `I` of `{0,...,M-1}`,

```text
-sum_(r in I) t_r <= j(M-j).
```

Together with `sum t_r=0`, these are the subset-sum inequalities of the permutahedron with vertices the permutations of `Lambda`. This follows by sorting an arbitrary linear functional's coefficients and applying Abel summation to its successive largest-coefficient subsets. Consequently

```text
sum_r t_r^2 <= sum_(a in Lambda) a^2 = M(M^2-1)/3.
```

The center-deleted chart has the same selected stress energy as the radius-one ring plus the six radial chains:

```text
E = 6 alpha_1^2 + 6 sum_(r=1)^(M-1) t_r^2
  = 6 sum_(r=0)^(M-1) t_r^2.
```

The selected positive stress is equilibrated at the moving vertices. Its first-order terms cancel in the summed unit lower constraints. The six prescribed corner changes are `L(theta)-M=-C theta^2+O(theta^4)`, with `C=M(M^2-1)/6`; dividing the second-order stress inequality by `theta^2` gives `E>=12C=2M(M^2-1)`. This matches the permutahedron upper bound. Strict convexity then forces `t` to be a permutation of `Lambda`.

For such a permutation, the predecessor inequalities and the outer subset bounds force every sector coordinate to equal the **negative** sum of the `j` smallest rates in the corresponding prefix. Thus each possible limiting first velocity is one of finitely many sorting velocities; no continuous family remains.

### Finite packets and local isolation

For a rate order `tau`, let `z_h=exp(i tau_h theta)`. In a sector, the sorting packet sites are

```text
p_(r,j) = (sum_(h<r) z_h) u + (sum_(h in S_(r,j)) z_h)(v-u),
```

where `S_(r,j)` selects the `j` smallest rates among the first `r`. Rotate the sector six times and omit the center. Same-layer edges and two predecessor edges have length one. The remaining limiting unit rows open for positive `theta`; every other pair starts with strict lower-distance slack. All nonboundary sites remain strictly inside the wall for sufficiently small `theta`. At each insertion layer `r=2,...,M-1`, the two selected sites and their predecessor have edge vectors `z_h u`, `z_h v`, and `z_h(v-u)`, so they form an exact unit equilateral triangle in each sector.

For completeness, the local uniqueness step is as follows. Let `P` be the bounded first-order feasible polytope in the moving coordinates. Its affine equalities are the ring and radial rows; each other limiting unit row is weak, and every weak row is strict in at least one sorting velocity. This follows by ordering the two rates that determine that diagonal row on opposite sides of its predecessor; all rates are distinct. Averaging the finite set of sorting velocities therefore gives strict slack in every weak row. At a fixed sorting velocity `d_*`, the gradient of the corresponding ring/radial quadratic energy uniquely maximizes its linear functional on `P`: equality in `t_* dot t <= |t_*|^2` forces `t=t_*`, and the sector recurrences then fix every coordinate. Hence that gradient lies in the relative interior of the normal cone at `d_*`.

Take the positive radius-one stress and add sufficiently small positive multiples of the other nested stresses `S_r`, `r>=2`. Their supports, together with `S_1`, cover exactly the ring and radial rows, so the resulting coefficients are positive on every strong row. The derivative of this stress matrix is one half of the energy gradient. Relative-interior normal-cone membership supplies a first correction whose coefficients are strictly positive on every weak row active at the selected packet; coefficients on strong rows may have either sign. If `R_theta` is the matrix of the packet's actual moving-involving unit contacts, full column rank of `R_0` follows because a kernel direction would leave all active rows unchanged, while inactive rows have positive slack; both signs would then give feasible first-order points through the unique maximizer. A bounded right inverse of `R_theta^T` corrects the stress residual, which is `O(theta^2)`, to an exact equilibrium stress. Strong-row weights stay bounded below by a positive constant and active weak-row weights are at least `c theta` for fixed `M` and packet.

For a feasible displacement `delta` from that packet, each old unit-contact row satisfies

```text
R_theta delta >= -C_1 |delta|^2
```

coordinatewise. Positive equilibrium and the minimum weight `c theta` bound every row above by `C_2 |delta|^2/theta`. Full column rank therefore gives `|delta| <= C_3 |delta|^2/theta`; the packet is the only feasible placement within a radius `c_1 theta`.

Finally, the canonical `C-ONE-VACANCY-FLAT-PINNING-RATE` theorem applies to this center vacancy: the fixed-`M` wall boundary moves by `O(theta)`, and the assumed placement converges to the punctured chart. Thus its displacement is `O(theta)` and normalized displacements have bounded subsequences. Every subsequential first velocity is one of the sorting velocities above. The placement then differs from the matching exact sorting packet by `o(theta)`, so the finite local-isolation radius makes them identical. Since there are finitely many rate permutations for fixed `M`, a compactness contradiction gives a common onset for all placements in the stated sequence class at that `M`.

## Hostile scope and regression checks

- The canonical `C-SORTED-RATE-NESTED-ENERGY-EQUALITY-REGRESSION` is respected: equality in the energy bound is realized by packets, so no strict energy gap is asserted. The audited conclusion comes from identifying every equality velocity with a finite packet and proving local isolation.
- The canonical `C-SIX-SIDED-WALL-PROFILE-SORTING-CLASSIFICATION` covers the complete `N`-point chart and supersedes that part of the source report. `C-SIX-SIDED-WALL-FIXED-CLASS-EXCLUSION` also covers its global-source application in its stated profile/window. Neither theorem is silently used for the `N-1` central-vacancy chart.
- The claim assumes convergence to the punctured central chart. It says nothing about arbitrary `N-1` clouds, outside source labels, contact-isolate movement, canonical wall extraction, global optimality, or Level I.
- The exact verifier was inspected and rerun at the frozen source tip. Its `Fraction` and `Q(sqrt(3))` arithmetic checks 14 packet cases (`M=3,4,5,6`), 37,773 pair distances, 2,412 first-order rows, 1,016 subset sums, packet triangles, ring energies, and sampled pinned ranks. It corroborates those finite examples only; the all-fixed-`M` proof is the analytic argument above. The verifier does not test arbitrary placements or prove the stress continuation.

## Canonical disposition

Promote `C-SIX-SIDED-WALL-CENTRAL-VACANCY-CLASSIFICATION` with dependency `C-ONE-VACANCY-FLAT-PINNING-RATE`. No route-map or continuation-prompt change is warranted: the theorem assumes the special chart and supplies no actual-source extraction or finite source move. Target C C-II and Level I remain open.
