<!-- theorem-state: {"artifact_id":"ART-A1E11F79CF6E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: one actual vacancy releases a complete oblique chart

**Worker:** 07. **Base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`, state `2026-10-10.audit.234`. **Date:** 2026-10-10.

**Classification:** proved candidate awaiting independent audit; conditional stress-transversal corollary. This report changes no canonical claim, route, or status. Level I remains open.

## 1. Exact chain and dependencies

```text
actual complete oblique rectangular chart + one interior deletion
 -> canonical Audit 195 strictifies every retained interior label
 -> actual-source normal inequalities release every noncorner wall label
 -> actual-source corner inequalities release all four corners
 -> every retained chart label is lower- and upper-strict against the full source
 -> if this chart hits every normalized source stress, strict diameter descent
    with exactly one literal deletion.
```

The new bridge is the third and fourth stages, with full-source lower and upper checks. It compresses an entire chart-sized virtual transversal to one literal vacancy. It does not restore that vacancy or extract a complete chart from an arbitrary canonical survivor.

Canonical dependencies are `C-OBLIQUE-ONE-VACANCY-STRICTIFICATION` (Audit 195), `C-NONCONTACT-WALL-WEAK-SHIELD` (Audit 169), `C-NONCONTACT-WALL-STRICT-SHIELD` (Audit 88), and, for the stress corollary, `C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE` (Audit 87). The source-normal Lemma N is a candidate dependency proved completely in `target_c_one_vacancy_side_pin_restoration_slot07_2026-10-10.md`, Section 3. The new corner lemma is proved below. No unreviewed dependency is presented as canonical.

## 2. Full-source statement

Let `m,n>=2` be integers. Let `u,v` be unit vectors making an angle `phi` strictly between `pi/3` and `2pi/3`. Put

```text
T={i u+j v : 0<=i<=m, 0<=j<=n},
K=conv(T),
I={i u+j v : 0<i<m, 0<j<n}.
```

Let `A` be any finite actual unit-separated planar source containing every displayed site of `T`. Choose any interior source label `p=a u+b v`, with `0<a<m`, `0<b<n`, and delete exactly `p`. Every label of `R=A\T`, including every original contact isolate, is retained at its old coordinate.

**Theorem G (proved candidate).** There is a four-stage piecewise-linear finite motion of `A\{p}` such that:

1. Every lower pair stays at least one and diameter stays at most `D=diam(A)` throughout.
2. Every retained chart label ends strictly inside `K`.
3. Every endpoint pair involving a retained chart label is strictly greater than one and strictly less than `D`.
4. Every source label outside the chart remains fixed; the endpoint has exactly `|A|-1` labels.

This is a source-level finite endpoint, not an abstract stress or constraint assignment. It requires neither global optimality nor triangle-freeness of the full source.

### No undisplayed labels inside the chart

The only unit lattice steps are `+/-u,+/-v`: for integer `r,s` both nonzero,

```text
|r u+s v|^2 > r^2+s^2-|rs| >= 1.
```

For each unit parallelogram, split along its shorter diagonal. Both triangles have squared side lengths at most two. If `x=sum_i lambda_i z_i` is a point of either triangle, its barycentric variance identity gives

```text
sum_i lambda_i |x-z_i|^2
 = sum_{i<j} lambda_i lambda_j |z_i-z_j|^2
 <= 2 sum_{i<j} lambda_i lambda_j <= 2/3 < 1.
```

At least one displayed triangle vertex is therefore strictly less than one from `x`. This covers all of `K`, including its boundary. A distinct additional source label in `K` is impossible.

The boundary of `K`, subdivided at every grid site, has only unit sides. For later use, the weak wall shield gives every weakly boundary-clear interior point distance at least one from every source label in `R`. The unit-side version actually gives at least `sqrt(3)` for nonvertex exterior labels; the elementary weighted exit identity is `|x-y|^2>=4-|e|^2` when segment `xy` exits at side `e` and both endpoints are unit-clear from its two vertices. Only the weak inequality is needed. The strict wall shield gives strict separation once the chart interior packet is strict.

## 3. First two stages: canonical vacancy strictification in the actual source

Apply Audit 195 with the complete old boundary fixed and vacancy `(a,b)`. Its two explicitly constructed finite stages remain inside `K`, are unit-separated, and end with every retained interior label strict against every other chart label. The first stage moves the punctured row and column; the second moves the remaining four blocks. Its proof is valid for the full angle interval, including obtuse angles.

At every point of both stages, the wall is at its old coordinates and the packet is weakly wall-clear. The weak wall shield checks all lower pairs against `R`; after strictification the strict wall shield checks them strictly. Every position lies in the original source hull. Hence all upper constraints, including previously inactive pairs, stay at most `D`. Call the retained strict interior packet `Q`.

## 4. Third stage: simultaneous release of the noncorner wall

For each noncorner boundary site `z`, let `n_z` be its unit outward normal to its side. These are `+Ju,-Ju,+Jv,-Jv` as appropriate, where `J` is counterclockwise quarter-turn. Assign mutually distinct positive depths `d_z` in `[1,2]`. Move all these boundary sites simultaneously by

```text
z -> z-t d_z n_z,  0<=t<=tau.
```

For each such `z`, choose its original unit interior neighbor `p_z` across the side and a unit side direction `a_z` for which the old sites `p_z-a_z` and `z+a_z` lie in the chart. They exist even when `m=n=2`: for a top site `(i,n)` use `a_z=u`, for a bottom site `(i,0)` use `a_z=u`, and for either vertical side use `a_z=v`. Since only noncorner wall sites are being considered, the requisite indices remain in the grid. Put `b_z=z-p_z`. The angle between `a_z,b_z` lies strictly between `pi/3` and `2pi/3`.

Source-normal Lemma N shows that every original unit neighbor `y!=p_z` of `z` satisfies `(y-z) dot n_z>=0`. In particular every original exterior unit contact and every contact to a fixed corner opens strictly:

```text
|y-(z-t d_z n_z)|^2=1+2t d_z (y-z) dot n_z+t^2 d_z^2>1.
```

The exceptional `p_z` is either the deleted vacancy or an interior label already strict at its new packet coordinate. The packet's positive finite clearance pays for that pair. Thus the argument is also valid when `p_z` has been deleted.

Original unit pairs between two moving noncorner wall sites are precisely adjacent labels on the same side. Their common normal is perpendicular to their unit separation, and their new squared distance is `1+t^2(d_z-d_{z'})^2>1`. Wall sites on distinct sides are never unit neighbors except through a corner, which is still fixed.

Every other relevant old lower pair has positive slack. Choose `tau>0` smaller than all the finitely many margins needed to preserve the packet-wall pairs and original nonunit pairs, and small enough that every moving wall site is strictly inside `K` for `t>0`. Such containment follows directly in axial coordinates: a noncorner site begins with positive distance along its side from both corners, and its chosen velocity has a strictly inward transverse component. The opposite sides have positive distance. At the endpoint every pair involving a retained interior label or a noncorner boundary label is strict against the entire source, including the four fixed corners.

No wall shield is applied to the now moved boundary. Exterior unit contacts are checked by Lemma N and exterior nonunit contacts by their actual finite margins.

## 5. Fourth stage: actual-source corner release

**Lemma C (proved candidate).** Suppose an actual unit-separated source contains `z,z+a,z+b`, where `a,b` are unit vectors with angle `theta in (pi/3,2pi/3)`. If `y` is any other original unit neighbor of `z`, write `w=y-z`. Then

```text
w dot (a+b) <= 2cos(theta/2)cos(pi/3+theta/2) < 0.
```

**Proof.** Take `a` at angle zero and `b` at angle `theta`. Source separation from the two distinct adjacent labels gives `w dot a<=1/2`, `w dot b<=1/2`. For unit `w`, its argument must therefore lie in `[theta+pi/3,5pi/3]`. The direction of `a+b` is `theta/2`, so its angle relative to `w` lies in `[pi/3+theta/2,5pi/3-theta/2]`. On this interval cosine has maximum `cos(pi/3+theta/2)<0`. Multiply by `|a+b|=2cos(theta/2)`. This proof excludes precisely the two adjacent labels, for which the corresponding separation inequality cannot be imposed. Every other original source label is covered.

At each corner of `K`, let `a,b` be the two unit steps along its incident sides pointing into the chart. Their angle is `phi` or `pi-phi`, both in the permitted interval. Move that corner in direction `a+b` with a sufficiently small positive amplitude. The new squared distance to any original fixed exterior unit neighbor is

```text
1-2t w dot(a+b)+t^2|a+b|^2>1.
```

The only exceptional original unit neighbors are the two adjacent wall sites, whose strict clearance was established in stage three. All current pairs to `Q` and to noncorner wall labels are already strict. All original corner-corner distances are at least two because `m,n>=2`; all remaining corner-involving nonunit pairs have positive original margins. Therefore one sufficiently small simultaneous corner amplitude preserves every lower pair throughout and makes every corner-involving lower pair strict. In axial coordinates each corner moves a positive amount toward each opposite side; it is strictly inside `K` for every positive sufficiently small amplitude.

This proves full-source strict lower feasibility. It also covers arbitrary exterior unit neighbors of the corners and every original contact isolate.

## 6. All upper constraints and stress consequence

All positions throughout lie in `K` or are fixed original source positions, so they lie in `conv(A)` and every upper pair is at most `D`. At the final endpoint every retained chart point lies in `int(K)`, hence in `int(conv(A))`. For any fixed `y in conv(A)`, the function `x -> |x-y|` is strictly below `D` on `int(conv(A))`: otherwise a small extension of the ray from `y` through `x`, still in the hull, would have distance greater than `D`, contradicting the hull's diameter `D`. This checks both old diameter pairs and newly possible upper pairs, including pairs of moving labels. Theorem G follows.

**Corollary S (conditional).** Suppose every normalized contact/diameter stress on the original full source has at least one positive row incident to `T`. Then the endpoint has no normalized stress. Indeed every endpoint active pair has both labels in fixed `R`; extending its weights by zero gives a normalized original stress supported outside `T`, contrary to the hypothesis. If the endpoint diameter is `D`, Audit 87 supplies a strict direction and a finite further step checking every inactive lower and upper pair; if its diameter is already below `D`, this is unnecessary. Either way there is a unit-separated `|A|-1`-point configuration of diameter strictly less than `D`.

The hypothesis concerns every normalized stress, not a single selected stress. It is not proved by this report. No same-cardinality contradiction follows without an actual restoration of one additional label.

## 7. General release lemma and exact remaining gap

The side and corner steps instantiate a useful general mechanism. Suppose a feasible placement already has a set `F` whose every incident lower and upper pair is strict, and all labels in `R` are at their original coordinates. For `p in R`, suppose a nonzero vector `w` obeys

```text
(p-q) dot w >= 0 for every fixed original unit neighbor q in R,
p+t w lies in the old source hull for every sufficiently small t>=0,
p+t w is in its interior for t>0.
```

Then a sufficiently small move of `p` releases it: each remaining old unit pair has new squared distance `1+2t(p-q) dot w+t^2|w|^2>1`; all current strict and old nonunit pairs are protected by finite margins; hull containment protects every upper pair and interior containment makes those involving `p` strict. This is a finite inductive release lemma. Its planar constraint is exact: the remaining unit-neighbor directions must fit in a closed semicircle, and the available direction must also point into the hull. A combinatorial deletion order alone does not supply this geometric property.

**Next exact restoration obligation.** For every canonical survivor to which Corollary S applies, construct one point `x` and, if needed, a further simultaneous displacement of the `|A|-1` endpoint labels, such that all `|A|` labels are pairwise unit-separated and their maximum pair distance is strictly below the original `D`. The present proof does not provide that point, a wall capacity payment, or universal chart/transversal extraction. Near-triangular fixed-wall capacity regressions remain binding; the corners here actually move, so those fixed-wall hypotheses cannot simply be reused or silently discarded.

## 8. Exact finite verification

The companion executable `research/verify_target_c_one_vacancy_full_chart_release_slot07_2026_10_10.py` records its exact counts and stage amplitudes in `research/target_c_one_vacancy_full_chart_release_slot07_certificate_2026_10_10.json`. It passed 72 fixtures: eight acute/right/obtuse angles, three chart dimensions/vacancy choices, and three exterior modes. Counts are 20,168 original source pairs, 74,464 whole-segment pairs, 18,616 endpoint pairs, 17,232 strict chart-involving lower/upper pairs, 1,456 side-normal unit-neighbor checks, 96 corner unit-neighbor checks, and 48 retained isolates. All 24 bare-chart endpoints have strictly smaller diameter with one fewer label.

It uses rational and `Q(sqrt(15))` arithmetic and checks each entire linear segment by the exact minimum of its squared-distance quadratic on `[0,1]`. Upper feasibility on each segment is checked at both endpoints because squared distance is convex. It checks strict axial containment for the claimed released labels, source-normal inequalities against every actual original unit neighbor, retained exterior contacts and isolates, and strict endpoint upper pairs. These finite sources are not canonical global minimizers. Finite verification does not prove the universal extraction, stress-transversal hypothesis, or restoration obligation; the analytic proof above carries the all-source motion claim.

## 9. Uniform exterior clearance and nearby-chart discrete replacement

The fixed-wall pinning regression in `target_c_near_coherent_one_vacancy_pinning_regression_slot07_2026-10-10.md` prevents a direct continuous fixed-wall stability argument. A different statement survives: the complete moved-wall endpoint can be chosen with clearance from **every hypothetical exterior point**, uniformly over actual sources. This yields a discrete full-source endpoint for a sufficiently close labeled chart, even if that chart is pinned with its wall fixed.

### 9.1 A uniform coherent endpoint

Fix the finite reference chart `T`, its parallelogram `K`, and its vacancy. Put

```text
E={y in R^2 : |y-t|>=1 for every t in T}.
```

The triangle-cover argument shows `E` is disjoint from `K`. We claim the four-stage construction can choose a retained chart endpoint `X`, depending only on this reference chart and its vacancy, such that

```text
|X|=|T|-1,
X subset int(K),
all internal distances in X are strictly greater than one,
inf_{x in X, y in E}|x-y| >= 1+mu for some mu>0.
```

The first two stages involve only a fixed finite chart, so choose their amplitudes without referring to any actual exterior labels. The unchanged interior packet is strict against every old wall vertex. The unit-side strict wall shield separates it from every `y in E` by at least `sqrt(3)`.

For a noncorner old wall site `z`, let `z'=z-h n_z` be its inward endpoint, `h>0`. Choose h small enough that `z'` is unit-clear from every other original wall vertex. This is possible: its distances to adjacent same-side vertices have squared value `1+h^2`, and all other wall-vertex distances start strictly above one. If `y in E` is outside the supporting half-plane of z's side, then

```text
|z'-y|^2 >= |z-y|^2+h^2 >= 1+h^2.
```

If y is inside that half-plane but outside K, segment `z'y` exits through another side. The endpoints of that unit wall edge are different from z and are weakly clear from both z' and y. The weighted exit identity gives `|z'-y|>=sqrt(3)`. Thus each moved side pin has uniform exterior clearance at least `min(sqrt(1+h^2),sqrt(3))>1`. This covers all nonunit exterior pairs as well as the unit pairs. The selected depths and finite internal packet margins suffice to choose the whole side stage independently of an actual source.

At a corner z with inward unit steps a,b and angle theta, take

```text
1<r_0<min(2sin(theta/2),2cos(theta/2)),
kappa=-2cos(theta/2)cos(theta/2+acos(r_0/2))>0.
```

Both upper bounds on `r_0` exceed one because `theta in (pi/3,2pi/3)`. If `y in E` has `r=|y-z| in [1,r_0]`, unit clearance from z+a and z+b gives, for `e=(y-z)/r`,

```text
e dot a<=r/2, e dot b<=r/2.
```

The forbidden angular intervals about a and b overlap since `acos(r/2)>theta/2`. Their complement is the interval with arguments from `theta+acos(r/2)` to `2pi-acos(r/2)`. Relative to the bisector a+b, its minimum angular distance is at least `theta/2+acos(r_0/2)>pi/2`. Therefore `(y-z) dot(a+b)<=-kappa`. An inward corner step `z'=z+t(a+b)` satisfies

```text
|z'-y|^2>=1+2kappa t.
```

For `r>=r_0`, choosing `t|a+b|<(r_0-1)/2` instead gives `|z'-y|>(r_0+1)/2>1`. Hence each corner has a uniform positive exterior gap. Select its amplitude small enough for these two bounds and the already strict finite internal margins. The construction stays feasible for every possible finite subset of E along each stage; no exterior nonunit-gap minimum is required. Taking the minimum of the finitely many packet, side-pin, and corner gaps supplies mu. This proves the claim.

### 9.2 Precise tolerance and full-source replacement theorem

Let `X,mu` be the reference endpoint above. Define the positive hull margin

```text
r=min_{x in X} dist(x,boundary K)>0,
B=union_{x in X} closed_ball(x,1+mu/2),
delta=min_{y in B}(1-min_{t in T}|y-t|)>0,
eta_*=min(r/2,delta/2,1/4)>0.
```

The strict positivity of delta is justified, not assumed. B is compact. If any `y in B` were unit-clear from every reference site, it would belong to E and be at least `1+mu` from every point of X, contrary to the defining ball of radius `1+mu/2`. Thus its minimum reference-guard distance is strictly below one. The continuous deficiency function has a positive minimum on compact B.

**Theorem G_eta (proved candidate).** Suppose an actual finite unit-separated source A contains distinct labeled sites `T'={t': t in T}`, with a specified bijection satisfying `max_t |t'-t|<eta_*`. Delete only the site corresponding to the reference vacancy. Replace the other chart labels by X, and keep every original label in `R=A\T'` fixed. This is a unit-separated `|A|-1`-point endpoint. Every pair involving a replaced label is strictly greater than one and strictly below `D=diam(A)`.

**Proof of all lower constraints.** For any original exterior label y, actual source separation gives `|y-t'|>=1`, hence `|y-t|>1-eta_*` for every reference guard. If y were within `1+mu/2` of a point of X, it would lie in B and have `min_T |y-t|<=1-delta`. Since `eta_*<=delta/2`, this is impossible. Thus every replaced-label/exterior pair is strictly greater than `1+mu/2`. Internal X pairs are strict by construction; all fixed R pairs remain their old feasible pairs. Every original isolate in R stays at its actual coordinate. Matched chart labels, including any chart contact isolates, are all retained and relocated except for the one explicitly counted deletion.

**Proof of all upper constraints.** For every unit direction e, the matched coordinate bound gives `h_conv(T')(e)>=h_K(e)-eta_*`. Each x in X obeys `h_K(e)-e dot x>=r`. Therefore `h_conv(T')(e)-e dot x>=r-eta_*>0` in every direction, so X lies strictly inside the actual chart hull, hence inside `int(conv(A))`. The interior-hull argument of Section 6 checks every actual and potentially newly active upper pair strictly. Fixed R pairs remain at most D.

The replacement is discrete; no continuous feasible path from a perturbed old chart is asserted. The tolerance depends only on the finite reference chart and its chosen vacancy, and applies uniformly to arbitrary exterior source labels and cardinalities. It is not a uniform tolerance as `m,n` grow or phi approaches an excluded angle. A canonical near-phase grid does not satisfy this coordinate tolerance merely because its phase interval is `O(1/D)`.

If the actual labeled set T' hits every normalized stress, the same zero-extension argument as Corollary S gives reduced-source strict diameter descent. The remaining population deficit is exactly one. The all-parameter tolerance and uniform-exterior proofs are analytic; the finite verifier in Section 8 checks selected exact coherent full-source paths and does not certify a numerical value of eta_* or canonical extraction.

## 10. Compatible banks and compression of a distributed transversal

**Theorem B (proved candidate).** Suppose the actual source contains `b` pairwise label-disjoint charts `T'_1,...,T'_b`, each satisfying Theorem G_eta for its own finite reference geometry, prescribed vacancy, and tolerance. There is one jointly feasible full-source discrete replacement which deletes exactly one label per chart, replaces every other chart label by its prescribed strict packet, fixes every original label outside the charts, and never increases diameter. At the final endpoint every pair involving any replaced label is lower-strict and strictly below the original D.

This is simultaneous compatibility, not an inference from unrelated individual exchange tests. Replace the first chart by its packet. Theorem G_eta checks that packet against **every old label** of every remaining chart. Thus the new source is unit-separated and still contains each remaining matched chart at its prescribed original coordinates. Apply Theorem G_eta to that actual new source and the next chart. Its unchanged exterior now includes all previously inserted packet labels, so the theorem checks every cross-packet lower pair directly. Induction proves joint feasibility and exact population loss b. Every packet lies in the interior of its own actual old chart hull, hence inside the original source hull; this proves all final upper pairs involving replaced labels strictly below the original D. The construction works in every chart order because the same invariant is preserved at every step. No assumption of unchanged walls or one-at-a-time abstract exchange compatibility is used.

For exactly coherent actual charts, one may instead use the universal four-stage endpoint, with its finite continuous source motion, at each step. Previously inserted packets are genuine current exterior labels, so the all-source argument checks them. Concatenating the stages supplies a finite path of diameter at most the original D, with one deletion per chart.

If the union of the actual chart labels hits every normalized original source stress, all active endpoint pairs lie among the unchanged outside labels. Zero-extension and Audit 87 give strict diameter descent after exactly b literal deletions, irrespective of how many virtual-transversal labels lie in those charts. Label-disjointness is an explicit hypothesis: charts sharing a wall label require a new coupled construction, and no conclusion for them is asserted. The next missing implication is an actual same-cardinality restoration of all b vacancies, or an independently certified post-descent packet paying that exact population deficit. Neither source-bank extraction nor such payment follows here.

## 11. A strict packet can still cover its entire old chart

**Theorem V (proved candidate regression).** The reference endpoint above can additionally be chosen so that its open unit disks cover all of K. In particular, no single extra label can be inserted anywhere in K while that endpoint is fixed, despite every retained chart label having strict contact clearance. This rules out a specific unproved refill inference, not every further rearrangement or exterior insertion.

Here is a complete proof. The original full chart covers K with nearest-site radius at most `q_0=sqrt(2/3)<1` by Section 2. After removing the interior site p, the old retained sites still have nearest-site distance strictly below one at every `x!=p`, with equality one only at p. Indeed if a nearest full-chart site is not p, its distance is at most q_0. Otherwise put `r=|x-p|<=q_0`. The four neighbors `p+/-u,p+/-v` give

```text
min_{a in {+/-u,+/-v}} |x-p-a|^2
 =1+r^2-2r max(|e dot u|,|e dot v|)
 <=1+r^2-2r a_0 <1 for r>0,
a_0=min(sin(phi/2),cos(phi/2))>1/2, e=(x-p)/r.
```

The last strict inequality uses `r<=q_0<1<2a_0`. The angular lower bound a_0 follows by dividing the circle at the four directions `+/-u,+/-v`; the largest gap is `max(phi,pi-phi)`, and a direction midway in that gap minimizes the maximum absolute projection.

In the four-stage construction, each of these four neighbors ends with a nonzero displacement d toward the vacancy satisfying `a dot d=-s|d|`, where a is its old vector from p. Interior neighbors move in the first punctured row/column stage and are untouched later; a boundary neighbor is a noncorner wall site and moves inward in stage three. Stage two does not move a vacancy neighbor and stage four moves only corners, none of which is a unit neighbor of the interior vacancy. Thus for `|x-p|<=r_0=s/4` and `|d|<s/2`,

```text
|x-p-a-d|^2-|x-p-a|^2
 =2(a-(x-p)) dot d+|d|^2
 <=-2s|d|+2r_0|d|+|d|^2<0.
```

Each new vacancy neighbor is therefore strictly closer than its old position throughout that ball. The four old neighbors already cover the ball strictly except at p; the new ones cover it strictly everywhere, including p.

On the compact set `K\open_ball(p,r_0)`, the old punctured chart has nearest-site maximum `q_1<1`. Choose all four stage amplitudes still smaller, if necessary, so that every retained site's total displacement is less than `(1-q_1)/2` and the vacancy-neighbor displacements are less than `s/2`. All earlier finite feasibility and uniform exterior-clearance arguments permit arbitrarily small positive amplitudes. The moved sites cover this remaining compact set with nearest-site distance at most `(1+q_1)/2<1`. Combining the two regions proves open-unit-disk coverage of K. Compactness then supplies a positive coverage gap

```text
nu=1-max_{x in K} min_{z in X}|x-z|>0.
```

The same disks cover the whole `nu/2` neighborhood of K. For the nearby-chart replacement, reduce the allowed tolerance to `min(eta_*,nu/2)` if this extra property is wanted. Its actual chart hull lies within that neighborhood by the matched-coordinate convex-combination bound. Thus a single additional point cannot be inserted into the actual old chart hull while X stays fixed. A full restoration must change the packet further or use space outside that hull and check every full-source lower and upper constraint. This is an analytic packet-specific capacity obstruction; the finite path verifier does not certify nu or this whole-region coverage.
