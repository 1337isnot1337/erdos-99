<!-- theorem-state: {"artifact_id":"ART-F9B9171E4B7D","canonical":true,"claim_ids":["C-DENSE-PHASE-CORE","C-EXPLICIT-ORDERED-GRID","C-WRAP-FULL-GAP","C-WRAP-PERIMETER","C-WRAP-THREE-GAP"],"claim_statuses":{"C-DENSE-PHASE-CORE":"canonical","C-EXPLICIT-ORDERED-GRID":"canonical","C-WRAP-FULL-GAP":"canonical","C-WRAP-PERIMETER":"canonical","C-WRAP-THREE-GAP":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent hostile audit — Target C Sections 90–94

**Date:** 2026-09-12  
**Promotion target:** `2026-09-11.audit.36`  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit independently checks the proof-only Target C modules

- §90 `90-dense-inverse-phase-crossing-core-audit.md`;
- §91 `91-explicit-ordered-grid-audit.md`;
- §92 `92-wrapping-perimeter-diameter-audit.md`;
- §93 `93-full-gap-wrapping-diameter-audit.md`;
- §94 `94-three-forbidden-gap-wrapping-audit.md`.

The audit was performed against the live `audit.35` canonical stack. The purpose is to certify the exact finite/asymptotic claims, not merely to accept merged proof-only files because they are newer.

## Verdict

All five modules are valid in their stated scopes.

The dependency structure splits into two independent Type-II advances:

```text
C-HARMONIC-WRAPPING + C-HARMONIC-CARRIER-QUAD + C-PUNCTURED-PHASE
    -> §90 dense inverse-phase core
    -> §91 explicit ordered complete grid

C-FULLCORE-NEAR-DISK + C-HARMONIC-CARRIER-QUAD
+ C-HARMONIC-CELL-TILING + C-HARMONIC-WRAPPING
    -> §92 perimeter threshold 0.914487...
    -> §93 independent full-gap threshold 0.915964...
    -> §94 independent three-forbidden-gap threshold 0.919778...
```

Sections 93 and 94 do not logically depend on §92, and §94 does not depend on §93. Their scalar thresholds are progressively stronger conclusions from increasingly strong uses of the same canonical geometry. Sections 92 and 93 remain valid intermediate canonical results, but §94 is the live wrapping/carrier endpoint.

No module closes C-II.

---

## 1. Section 90 — dense inverse-diameter phase core

### Claim checked

Inside the canonical Section-88 macroscopic Type-II harmonic carrier, there are fixed phase-label train families supporting a simple bipartite crossing graph with

- `Theta(D^2)` actual strict-rhombus crossings;
- `O(D)` total train vertices;
- all reduced phases in one `O(1/D)` interval;
- linear minimum degree after pruning.

### Audit

Canonical §88 supplies `R_D >= r D^2` strict-rhombus crossings in one locally saturated carrier. Canonical §82 gives `T_D=O(D)` local train segments; §89 later improves the constant but is not needed. Canonical §68 gives both an `O(D)` phase-cut deletion and total angular defect `sum delta_R=O(D)`.

For fixed `K`, Markov gives at most `(C_phase/K)D^2` crossings with `delta>K/D`. Choosing `K` large relative to `r` leaves a fixed positive fraction of all carrier crossings `K`-good. One of the three unordered phase-label pairs therefore carries `Omega(D^2)` good crossings.

Random bins of width `4K/D` split any good edge with probability at most `1/4`, so one shift retains a fixed positive fraction of edges internally to bins. The small-shore estimate

`sum_{a_j<alpha D} e_j <= alpha D sum_j b_j`

and its symmetric counterpart are valid because the crossing graph is simple and the total number of train segments is `O(D)`. Hence finitely many bins with both shores linear carry a positive quadratic edge mass, so one such bin has `Omega(D^2)` edges.

The iterative deletion of vertices of degree `<kappa D` is also correct: if every vertex were deleted, the sum of deleted edges would be strictly smaller than the original edge count. A nonempty subgraph with minimum degree `Omega(D)` survives.

### Verdict

Certified.

Proposed canonical ID: `C-DENSE-PHASE-CORE`.

---

## 2. Section 91 — explicit ordered complete grid

This section received the most hostile scrutiny because an arbitrary dense bipartite graph does **not** contain a linear biclique.

### 2.1 Ordered cutwidth

For a forward graph on `N` ordered vertices with `E>=4N`, put `r=floor(E/(2N))`. At most `Nr<=E/2` edges have order span below `r`; the remaining edges contribute at least `rE/2` total cut crossings. Since there are fewer than `N` cuts, one cut has at least `E^2/(8N^2)` crossing edges. The tie-class correction loses at most a factor two and is valid because no retained edge has equal reduced phases.

Thus one genuine phase threshold has `Omega(D^2)` edges directed from the lower-phase shore to the upper-phase shore.

### 2.2 Reuse of Section 76 before completeness

This was the main dependency question.

Canonical §76's common-projection calculation uses only the pairwise angular inequalities

`L < beta_b-alpha_a < 2L`.

Completeness is not used until the later common-order lemma and diameter path. Section 91 establishes these inequalities for **every** retained cross-shore pair after its phase threshold because all phases lie in one `O(1/D)` bin. Therefore using the §76 cone argument to make every retained train strictly monotone in one common coordinate `X` is legitimate before the biclique is extracted.

### 2.3 Endpoint-balanced slabs

The endpoint partition can be chosen with `O(N/M_0)` endpoints per slab. In a slab with `p_j` endpoints, at most `p_j^2/4` assigned crossings can have both train segments ending in that slab. Summing gives the claimed `O(D^2/M_0)` bad-edge bound.

For every nonbad crossing, at least one train has neither endpoint in the crossing slab. Since that train is `X`-monotone and contains the crossing, its `X`-domain spans the entire slab. Pigeonholing over the two shores and finitely many slabs yields one slab with a pairwise-disjoint spanning family carrying `Omega(D^2)` crossings.

### 2.4 Interval neighborhoods

Order the spanning family vertically. If one `A` train crosses `b_i` and `b_k` with `b_i<b_j<b_k`, the common crossing sign forces the `b_i` crossing to occur before the `b_k` crossing. Between those coordinates the `A` graph changes from below `b_j` to above `b_j`, forcing a crossing with `b_j`. Thus every `A` neighborhood is an interval.

No disk topology or endpoint assumption is missing.

### 2.5 Dense consecutive-ones rectangle

If each shore has at most `CD` vertices and the graph has at least `epsilon D^2` edges, rows of degree below `epsilon D/(2C)` carry at most half the edges. Hence there are at least `epsilon D/(2C)` long interval rows. Partition the ordered shore into blocks of size about half the long-row threshold. Every long interval contains one full block, there are only `O(C^2/epsilon)` blocks, and pigeonholing gives a block contained in `Omega(D)` row neighborhoods. This yields a complete bipartite graph with both shores linear in `D`.

The displayed coefficient `epsilon^2/(18C^3)` is conservative but valid.

### Verdict

Certified, conditional only on §90 becoming canonical in the same promotion transaction.

Proposed canonical ID: `C-EXPLICIT-ORDERED-GRID`.

---

## 3. Section 92 — attachment-perimeter wrapping threshold

### 3.1 Finite perimeter capacity

Canonical §82 gives

`L+Q=4a-6-2s-2c`.

The induced component-plus-attachments graph is connected, every outer-walk edge is a unit contact, all attachment vertices are extreme in the attachment polygon `P`, and all induced vertices lie in `P`. Therefore the convex hull of the outer walk is exactly `P`, so projection variation/Cauchy width gives

`per(P)<=L<=4a-6`.

### 3.2 Three-anchor perimeter floor

For a wrapping support of diameter `lambda<1` on the radius-`1/2` circle, choose three anchors whose triangle contains the center. Their cyclic gaps `g_i` lie in `(0,theta]`, `theta=2 asin(lambda)`, and sum to `2pi`.

Putting `x_i=g_i/2`, the objective `sum sin x_i` is concave on the box-simplex. The minimum is attained at an extreme point. A zero coordinate is infeasible because the other two coordinates are each `<pi/2`; therefore two coordinates equal `theta/2` and the third is `pi-theta`. This gives

`per(conv S) >= 2 lambda (1+sqrt(1-lambda^2))`.

Combined with `per(P)<=4|A|-6` and the canonical §88 six-cluster attachment ceiling, every wrapping limit obeys

`6 asin(lambda)-2pi >= (lambda/2)(1+sqrt(1-lambda^2))`.

The scalar function is strictly increasing on `[sqrt(3)/2,1)`, giving the unique threshold

`mu_1=0.914487471642104...`.

Section 88's cap-family capacity theorem is stated for every fixed `mu<1`; its only use of the old `mu_0` was to know that shorter macroscopic limits are cap type. Replacing that classification threshold by `mu_1` is therefore valid.

### Verdict

Certified.

Proposed canonical ID: `C-WRAP-PERIMETER`.

---

## 4. Section 93 — full attachment-gap perimeter

### 4.1 Uniform lower spacing

If two consecutive attachment vertices have polar angular gap `g`, the intervening force-hull boundary arc has length at least their source-point distance, hence at least one. The canonical annular radial-arclength estimate bounds that arc above by `(R_D^2/r_D)g`. Therefore

`g >= ell_D:=r_D/R_D^2`, with `D ell_D -> 2`.

This is an individual finite-gap estimate and can be summed over `Theta(D)` gaps.

### 4.2 Upper spacing and gap optimization

A wrapping Hausdorff limit with `lambda<1` has no antipodal pair and largest support gap strictly below `pi`; Hausdorff convergence makes all finite cyclic gaps eventually `<pi`. The cell-diameter bound then gives a uniform upper gap `theta+o(1)`, `theta=2 asin(lambda)`.

For fixed lower/upper bounds, `sum sin(g_i/2)` is a concave objective on a box-simplex. Its minimum occurs with all but at most one gap at an endpoint. Passing to `a_D/D -> alpha` gives

`liminf per(P_D)/D >= p(alpha,lambda)`

with

`p=alpha+k lambda+sin(r/2)`

and the stated residual-angle definitions.

The function `F_lambda(alpha)=p(alpha,lambda)-4alpha` is continuous across floor-function transitions and has derivative `-3-cos(r/2)<0` on each smooth interval. Hence, under the §88 density ceiling `alpha<=U(lambda)`, the easiest capacity case is `alpha=U(lambda)`.

On the relevant interval the floor index is `k=2`; substitution yields

`2 lambda+sin(8 asin lambda) <= 18 asin lambda-6pi`.

The scalar left-minus-right function is strictly decreasing, giving

`mu_2=0.915964980334399...`.

### Verdict

Certified.

Proposed canonical ID: `C-WRAP-FULL-GAP`.

---

## 5. Section 94 — three forbidden wrapping gaps

### 5.1 Three genuine forbidden arcs

In each of the three anchor gaps from the canonical §88 six-cluster proof, the allowed endpoint intervals have total length

`g_i-(2pi-2theta)`.

Thus the middle support-free arc has exact angular length

`phi=2pi-2theta`.

These three forbidden arcs lie in different anchor gaps and are pairwise disjoint.

In the finite Type-II sequence, choose actual attachment vertices converging to the anchors. Compactness gives empty shrunken versions of the three forbidden arcs. Because an actual anchor attachment separates adjacent anchor gaps, the three forbidden arcs lie in three **distinct** finite cyclic attachment gaps.

### 5.2 Perimeter lower bound

The wrapping limit has largest cyclic gap strictly below `pi`, so all finite gaps are eventually below `pi`. Each of the three special gaps contributes at least `sin(phi/2)-o(1)` to normalized polygon perimeter. Every other gap contributes at least `sin(ell_D/2)`, and `(a_D-3)sin(ell_D/2)->alpha`.

Therefore

`liminf per(P_D)/D >= alpha+3 sin(phi/2)=alpha+3 sin(theta)`.

The finite capacity `per(P_D)<=4a_D-6` forces

`alpha>=sin(theta)`.

The canonical six-cluster packing bound gives

`alpha<=3theta-2pi`.

Hence every wrapping limit satisfies

`sin(theta)<=3theta-2pi`.

The scalar function `3theta-2pi-sin(theta)` has derivative `3-cos(theta)>0`, so it has one root on `[2pi/3,pi)`:

`theta_3=2.335032210844538...`,

`mu_3=sin(theta_3/2)=0.919778662688621...`.

Again the §88 cap-capacity theorem propagates the improved classification threshold to an actual macroscopic locally rhombus-saturated carrier.

### Verdict

Certified. This is the live scalar carrier threshold after promotion.

Proposed canonical ID: `C-WRAP-THREE-GAP`.

---

## 6. Remaining obstruction after promotion

The Type-II branch now contains, in one macroscopic harmonic carrier,

- diameter at least `(0.919778662688621...-o(1))D`;
- quadratic strict-rhombus area and local filling fraction `1-o(1)`;
- `O(D)` local trains with the exact §89 area/diameter budget;
- a dense inverse-diameter phase core (§90);
- an explicit linear-by-linear complete ordered near-triangular grid (§91).

Approaching the §94 scalar endpoint additionally forces simultaneous asymptotic saturation of

- six-cluster boundary packing;
- attachment-perimeter capacity;
- three macroscopic forbidden gaps;
- near-minimal spacing on essentially all remaining attachment gaps;
- and therefore `Q+2s+2c=o(D)` in the exact §82 local ledger.

The high-value next theorem is no longer another generic grid extraction. It should couple this boundary equality geometry to the interior near-rhombic train structure or to canonical §84's near-geodesic corridor mechanism and produce either

1. a contradiction to diameter minimality, or
2. a source-preserving strict sub-`D` deformation.

No such closing implication is claimed here.
