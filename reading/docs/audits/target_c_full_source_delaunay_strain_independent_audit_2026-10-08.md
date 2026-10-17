> Generated reading edition · [exact source](../../../docs/audits/target_c_full_source_delaunay_strain_independent_audit_2026-10-08.md) · source SHA-256 `4682af190672d76d9a26dd107b1623e02c09895c9bca190988a0bd58ece2077f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-0BB12517F6BA","canonical":true,"claim_ids":["C-FULL-SOURCE-DELAUNAY-DEFECT-BUDGET","C-FULL-SOURCE-DELAUNAY-NEAR-NEIGHBOR-BUDGET","C-FULL-SOURCE-TWO-LOWER-BLOCKERS","C-HULL-COVERED-THIN-BOUNDARY-TRIANGLE-REGRESSION","C-LOWER-CLOSED-SET-SUPPORT-FRONT"],"claim_statuses":{"C-FULL-SOURCE-DELAUNAY-DEFECT-BUDGET":"canonical","C-FULL-SOURCE-DELAUNAY-NEAR-NEIGHBOR-BUDGET":"canonical","C-FULL-SOURCE-TWO-LOWER-BLOCKERS":"canonical","C-HULL-COVERED-THIN-BOUNDARY-TRIANGLE-REGRESSION":"regression","C-LOWER-CLOSED-SET-SUPPORT-FRONT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C Audit.164 — full-source Delaunay strain and lower-blocker fronts

**Audit base:** `origin/main=7ad247fd7a78e27766d26b205eb1ee6fc5937001`,
state `2026-10-08.audit.159`; C-I is closed, C-II and Level I remain open.

**Frozen research source:** `origin/research/level-i-closure-20261007` at
`c981b6f818764765bcb99917a9d858599c425471`.

**Audited source artifacts:**

- `docs/reports/target_c_full_source_delaunay_strain_and_branching_2026-10-08.md`,
  SHA-256 `5d3308597879966a95a03bc58ff8c3dea92827c5a9efe93ade5d1f3a0c25b1ae`;
- `research/verify_target_c_full_source_delaunay_budget_2026_10_08.py`,
  SHA-256 `1e27ae8f280cda1c99ab5ea6178518816c12c93f8dbdeb3bfc742ef316769642`.

The source branch is ahead of the frozen Voronoi snapshot; the report and
verifier above were audited at the immutable commit `c981b6f8`. The branch's
older theorem-state snapshot was not imported. The proof below uses the
already canonical Audit.163 hull-coverage result and independently reconstructs
the new full-source estimates.

## Claims and verdicts

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Full-source Delaunay defect and exceptional-label budget | PASS — promote | `C-FULL-SOURCE-DELAUNAY-DEFECT-BUDGET` |
| Near-six-neighbor population bound | PASS — promote | `C-FULL-SOURCE-DELAUNAY-NEAR-NEIGHBOR-BUDGET` |
| Two strict lower blockers for each small translation | PASS — promote | `C-FULL-SOURCE-TWO-LOWER-BLOCKERS` |
| Support front of a lower-closed set | PASS — promote | `C-LOWER-CLOSED-SET-SUPPORT-FRONT` |
| Hull-covered thin boundary triangle | REGRESSION VALID | `C-HULL-COVERED-THIN-BOUNDARY-TRIANGLE-REGRESSION` |
| Application to half-depth root closures or a source move | CONDITIONAL / NOT PROMOTED | Requires an unpromoted closure/payment theorem |

## Exact promoted statements

Let `A` be a finite noncollinear triangle-free global minimum-diameter source,
chosen contact-minimal, with `K=conv(A)`, `D=diam(A)`,
`g_A=|A|-1-pi*D^2/(2*sqrt(3))>0`,
`delta_K=pi*D^2/4-area(K)`, `a=sqrt(3)/4`,
`a0=sqrt(3)/2`, and `kappa=(2-sqrt(3))/4`. No
diameter-pair-minimality is needed for these statements. Take any straight-line
Delaunay triangulation of the complete source, with arbitrary legal
triangulation at cocircular degeneracies.

### `C-FULL-SOURCE-DELAUNAY-DEFECT-BUDGET`

Let `J` be labels whose Voronoi cells clipped to `K` meet `partial K`,
`m=|J|`, and `b` the number of all source labels on `partial K`, including
collinear side labels. Let `B` be the Delaunay faces with all three vertices
in `J`, `f_B=|B|`, and `A_B=sum_{T in B} area(T)`. For the remaining faces
`G`, define `sigma_T=area(T)-a` and `Sigma=sum_{T in G} sigma_T`. Then

```math
 m\le 8D+1,\qquad f_B\le 2m-b-2,
```

```math
 \boxed{\Sigma+A_B+\delta_K+a_0g_A=a(b+f_B)},\qquad
 0\le\Sigma<a_0(m-1)\le4\sqrt3D.
```

There is an exceptional label set `E`, containing `J`, such that

```math
 |E|\le25m+(450+12/\kappa)\Sigma.
```

Every label outside `E` is an interior Delaunay vertex of valence six. Every
incident face is acute, has excess below `1/100`, and each of its sides and
angles obey

```math
 0\le |e|-1\le5\sigma_T,\qquad
 |\angle-\pi/3|\le50\sigma_T.
```

### `C-FULL-SOURCE-DELAUNAY-NEAR-NEIGHBOR-BUDGET`

For `0<epsilon<=1/10`, at most

```math
 25m+(450+12/\kappa)\Sigma+30\Sigma/\epsilon
```

source labels fail to have six distinct Delaunay neighbors at distances in
`[1,1+epsilon]`. Along any canonical source sequence with `D->infinity`,
`epsilon(D)->0`, and `D*epsilon(D)->infinity`, the exceptional population is
`o(D^2)`. This gives no common phase or lattice placement.

### `C-FULL-SOURCE-TWO-LOWER-BLOCKERS`

For `0<delta<=1/10`, use the preceding exceptional set with
`epsilon=delta/20`. Every label outside it has, for every unit direction `u`,
two distinct source neighbors whose relative vectors positively span `u` and
whose distances from the moved point after the individual translation
`x -> x-delta*u` are strictly less than one. They are strict lower blockers
for that single-label translation. No simultaneous move is asserted.

### `C-LOWER-CLOSED-SET-SUPPORT-FRONT`

Fix the same `delta,u`, and let `S` be any finite subset of the original
source closed under every strict lower blocker for `x -> x-delta*u`. If
`x in S` has a nonzero supporting normal `nu` for `conv(S)` and
`nu dot u<=0`, then `x` belongs to the stated exceptional set. Equivalently,
every support label outside the exceptions has all its support normals in
the open half-plane `nu dot u>0`. This gives no root multiplicity bound,
integer payment, or compatible motion.

### `C-HULL-COVERED-THIN-BOUNDARY-TRIANGLE-REGRESSION`

The exact three-point source `(0,0),(1,0),(2,1/10)` is unit-separated and
its hull is covered by closed unit disks about its labels, yet its only
Delaunay triangle has circumradius greater than one and area `1/20<sqrt(3)/4`.
It is nonglobal: the unit equilateral triple has the same cardinality and
strictly smaller diameter. Thus unit separation and hull coverage alone do
not give a nonnegative triangle excess for an all-boundary face. This is not
a regression to a global-minimizer theorem.

## Independent proof reconstruction

### Boundary labels and face accounting

Audit.163 proves that contact-minimality covers `K` by the closed unit disks
about the complete source. If a Voronoi cell clipped to `K` meets
`partial K`, the center of that cell is within one of the boundary point,
because the center is nearest there and some source label is within one.
The radius-`1/2` disks around these `m` centers have disjoint interiors.
They lie in the outer parallel body `K+B(0,1/2)` and outside
`int(K minus B(0,3/2))`. Steiner's formula and the decreasing perimeters of
inner parallel convex bodies bound this belt area by `2P(K)+pi/4`. Hence

```math
 m\le 8P(K)/\pi+1\le8D+1,
```

using Cauchy's perimeter formula. Every hull-boundary label belongs to `J`,
so `b<=m` and `conv(J)=K`.

The full triangulation has `2|A|-b-2` faces. Its all-`J` faces remain faces
in a triangulation of `J` inside `K`, giving `f_B<=2m-b-2`. A mixed
Delaunay edge has one endpoint outside `J`; its incident circumcenter lies
in that endpoint's full bounded Voronoi cell, which Audit.163 places inside
the unit disk about its center. The mixed edge therefore has length at most
two. A radius-`1/2` disk packing around one `J` endpoint shows it has at
most 24 neighbors within distance two. Each mixed face has two mixed edges,
and each mixed edge has two mixed incident faces, so the numbers of mixed
faces and mixed edges agree. Thus at most `24m` faces are mixed and
`W=J union N_Del(J)` has size at most `25m`.

### Exact area ledger

For a face `T` with a vertex outside `J`, its circumcenter lies in that
vertex's full bounded Voronoi cell, so its circumradius is at most one. All
three sides are at least one. The smallest triangle angle is at most
`pi/3`, hence `R>=1/sqrt(3)`. At fixed `R`, concavity of `log(sin(theta))`
minimizes the area when the angles are `ell,ell,pi-2ell`, where
`ell=asin(1/(2R))`; this gives

```math
 area(T)\ge\frac{\sqrt{4R^2-1}}{4R^2}\ge a
 \quad(1/\sqrt3\le R\le1).
```

The last function has its only interior critical point at a maximum and
equals `a` at both endpoints. Thus every `sigma_T` on `G` is nonnegative.
The face-area sum is

```math
 area(K)=a(2|A|-b-2-f_B)+\Sigma+A_B.
```

Substitution of `delta_K` and `g_A` gives the claimed exact identity.
Since `delta_K>=0`, `A_B>=0`, and the canonical strict lattice comparison
gives `g_A>0`,
`Sigma<a(b+f_B)<=a_0(m-1)<=4sqrt(3)D`. The thin-triangle regression above
confirms why `A_B` must remain explicit.

### Obtuse-face charges and exceptional labels

Let `H_0` count right or obtuse faces with no vertex in `J`. Their longest
edges are internal. Across such an edge the Delaunay neighbor is in `G`;
both circumradii are at most one. If the first face's largest angle is
`alpha`, local Delaunay legality gives the neighboring opposite angle
`beta<=pi-alpha`; side separation gives all relevant angles at least
`pi/6`, and `alpha<=2pi/3`. The sine rule and concavity of `log(sin)` give

```math
 area(T)\ge\tfrac12\sin\alpha,\qquad
 area(T')\ge a(1-\cos\alpha),
```

so `sigma_T+sigma_T'>=1/2 sin(alpha)-a(1+cos(alpha))>=kappa`.
Each face excess is used at most four times (once as the selected face
and at most once across each of its three edges), hence
`H_0<=4Sigma/kappa`.

Mark `W`, all vertices of a face in `G` with excess at least `1/100`, and
all vertices of the `H_0` faces. There are at most `100Sigma` large-excess
faces and at most `4Sigma/kappa` selected obtuse faces. For an unmarked
interior vertex of valence `q!=6`, the incident angles sum to `2pi`; the
local small-excess estimate below forces incident excess greater than
`1/50`. Summing over vertices counts each face at most three times, so
there are fewer than `150Sigma` such vertices. The total exceptional count
is at most
`25m+(300+12/kappa+150)Sigma`, as claimed.

For completeness, the small-excess estimates are local and do not import
the fixed-unit-wall conclusion outside its scope. In an acute triangle
with sides at least one, let `L` be the longest side. On the feasible
squared-side region, Heron's formula gives area at least
`L*sqrt(4-L^2)/4` for `1<=L<=sqrt(2)`, and at least `1/2` for
`sqrt(2)<=L`. Since `L*sqrt(4-L^2)/4` at `L=11/10` exceeds
`a+1/100`, an acute face of excess below `1/100` has `L<11/10`.
The derivative of this lower bound exceeds `1/5` on `[1,11/10]`, giving
`L-1<=5sigma_T`. On the cube of side lengths `[1,11/10]^3`, direct
cosine-law differentiation gives `sin(angle)>4/5` and each side derivative
of a cosine has magnitude below two. The mean-value theorem yields
`|angle-pi/3|<= (5/2) sum_e(|e|-1)<=50sigma_T`.

### Near-neighbor count and blockers

Summing the preceding local estimates over all small-excess faces gives
total edge strain at most `15Sigma` and total angle strain at most
`150Sigma`. Marking both endpoints of every such face edge longer than
`1+epsilon` costs at most `30Sigma/epsilon` additional labels. Every
remaining label has exactly six Delaunay neighbors, all within
`1+epsilon`. There cannot be seven source neighbors in that radius: the
cosine law gives angular separation at least `2asin(1/(2(1+epsilon)))`,
which is greater than `2pi/7` for `epsilon<=1/10`. This proves the
population bound and its `o(D^2)` consequence.

For `epsilon=delta/20`, consecutive near-neighbor rays have gaps at least
`pi/3-2epsilon` and at most `pi/3+10epsilon`. For any unit direction `u`,
take the two rays bracketing `u`; if `u` is itself a ray, use its immediate
neighbors. Each selected vector `r` satisfies
`u dot r>=1/2-delta/2`. If the label moves to `x-delta*u`, then

```math
 |r-\delta u|^2\le(1+\delta/20)^2
 -2\delta(1/2-\delta/2)+\delta^2
 =1-\tfrac9{10}\delta+\tfrac{801}{400}\delta^2<1
```

for `0<delta<=1/10`. The blockers strictly bracket `u` and so positively
span it. If `S` is lower-closed, these blockers lie in `S`. At a support
label `x` with normal `nu`, `nu dot (x-y_i)>=0` for both blockers. Their
positive combination is `u`, so `nu dot u>=0`; equality would force a
nonzero `nu` to annihilate two independent vectors. Therefore
`nu dot u>0`, proving the support-front claim.

## Verifier boundary and hostile checks

The exact source verifier was inspected and rerun at `c981b6f8`. It checks
six rational/quadratic-field oblique grids, all source and square-competitor
pairs, clipped Voronoi cells, empty circumcircles, Delaunay face and mixed
edge counts, the exact area ledger, six-neighbor fixtures, blocker pairs,
finite lower-closed fronts, and the thin-boundary-triangle regression. It
passed 9,432 source-pair checks, 9,432 competitor-pair checks, 29,392
empty-circumcircle comparisons, 310 clipped cells, 228 mixed edges and
faces, 770 blocker-direction checks, 56,592 complete lower-arrow checks,
and 366 support checks. These are finite fixtures; the universal results
above are analytic. No verifier fixture is asserted globally optimal.

The following limits are binding:

- Boundary triangles are not assigned nonnegative excess; they remain in
  `A_B`.
- `Sigma=O(D)` permits diffuse metric strain. No global lattice phase,
  exact vacancy, or defect localization follows.
- A lower-closed front can be shared by many root closures; the estimate
  gives no root multiplicity or integer payment.
- Individual blockers do not form a simultaneous finite move. No
  source-preserving competitor is supplied.
- The combination with the separate half-depth closure candidate remains
  conditional because that closure/payment input is not canonical.

**Verdict: PASS — promote the four exact lemmas and record the scoped
boundary-triangle regression.** The canonical C-II finite-move/payment
obligation and Level I status are unchanged.
