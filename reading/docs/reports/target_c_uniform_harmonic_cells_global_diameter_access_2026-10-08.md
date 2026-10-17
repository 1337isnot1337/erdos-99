> Generated reading edition · [exact source](../../../docs/reports/target_c_uniform_harmonic_cells_global_diameter_access_2026-10-08.md) · source SHA-256 `cc59000e5334e54036401db71f4546245faad1b1e6350eba493d02ca15f0025e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-742748719B3B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->

> **Destination status (2026-10-16).** This source report preserves the full derivation and its finite checker. Its earlier source-side “unreviewed” label is not the current destination claim status: Audit.173 is already present in the destination and the theorem-state records `C-UNIFORM-HARMONIC-CELL-AREA`, `C-TYPEII-LOCAL-COHERENT-GRID-ACCESS`, and `C-TYPEII-ACTUAL-DIAMETER-GRID-ACCESS` as canonical at the narrower scopes stated there. The edge count remains unweighted: no exceptional KKT-mass bound, compatible motion, refill or C-II closure follows. The [Target C theorem-state](../../../docs/state/theorem-state.yaml) remains authoritative; this import creates no theorem transition.

# Target C: uniform harmonic cells and global diameter-to-grid access

Date: 2026-10-08.
Run base: `d63e36654c903cb24add5da105d89db7801ae32b`.
Canonical base: `ca26397adb06a7335458d603d852eb465d61e28c`.
State: `2026-10-08.audit.143`.
Classification: proved candidate awaiting independent audit/promotion.
Registry: unreviewed; noncanonical. Level I and C-II remain open.

Rechecked after rebasing onto `350c8ed6cf38d9a051bffe1edae1d0d54df10672`,
state `2026-10-08.audit.145`. The new finite radial-lifting audit and
strict-turn path criterion do not alter any premise used below.

## 1. Source theorem and exact remaining bridge

Use an unbounded canonical contact-minimal, then diameter-pair-minimal
triangle-free global-source sequence, retaining all source labels. Let
`V` be the nonisolated positive-contact core, `B=Vert(F)` the actual
loaded diameter endpoints, and `I` any unloaded contact component.
Write `A_I` for its actual attachments and `P_I=conv(A_I)`.

The candidate conclusions are:

1. Every angle of `P_I` is strictly greater than `pi/6`.
2. There are fixed `c,alpha>0` such that, eventually and uniformly over
   every nonempty unloaded component,
   
   ```math
   \operatorname{diam}(P_I)\ge cD,\qquad |A_I|\ge cD/3,\qquad
   \operatorname{area}(P_I)\ge\alpha D^2.
   \tag{UC1}
   ```

   This holds in both C-II branches, without a Type-II premise.
3. The number of unloaded components is bounded independently of `D`.
   The statement allows no unloaded component; it does not force a
   quadratic core in the macroscopic inactive-container branch.
4. In Type II, every unloaded component has a uniformly quadratic
   coherent grain and complete grid. Every loaded endpoint can reach
   an actual attachment of one of these components along an actual
   loaded-loaded contact chain of uniformly `o(D)` length.
5. In Type II, for each fixed `lambda,eta>0` and `epsilon in (0,pi/6)`,
   there is a fixed `rho>0` such that eventually all but `eta D` edges
   of the complete actual diameter graph have the following property:
   both endpoints have actual contact routes of length `<lambda D`
   to nearby same-component epsilon-coherent complete grids, with
   both grid shores uniformly linear in `D`. The grids lie within
   `(rho+o(1))D` of their respective loaded endpoints.

The final count is of actual diameter edges, not merely unweighted
ports. It therefore also controls exceptional high-degree diameter
hubs. Routes and grids may overlap. No control of exceptional KKT
weight, compatible motion, or independent route payment is claimed.

The implication chain is

    actual diameter normals cluster at short source chords
      + unloaded degree and pinned rank
      -> every harmonic cell is uniformly macroscopic
      -> Type-II grains are available in every unloaded component
      -> loaded-only chains have submacroscopic length
      -> a single face-tail bank has small diameter-incidence multiplicity
      -> global actual-diameter endpoints are coupled to source grids.

This is a structural bridge to the finite replacement/motion route.
It does not refill a deleted diameter vertex cover or construct a
same-cardinality strict-D competitor. That closing implication and
the inactive-container branch remain open.

## 2. Canonical inputs

- [Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md), `C-ZRF`:
  mixed core rank `2|V|-3`, positive contact equilibrium, and unloaded
  degree at least three.
- [Section 58](../targets/target-c/58-full-source-geometry-audit.md),
  `C-FS-GEOM`: one full-source circumcenter `o`, with
  `eta_D=3^(1/4)sqrt(D)` and `r_D=sqrt(D eta_D+eta_D^2)`, such that
  
  ```math
  D/2-\eta_D<|b-o|<D/2+\eta_D,\qquad
  |(b+k)/2-o|<r_D
  \tag{UC2}
  ```

  for every actual diameter endpoint and pair. In particular both
  `eta_D/D` and `r_D/D` tend to zero. This does not say `F` tends to
  the disk in the inactive-container branch.
- [Sections 82](../targets/target-c/82-harmonic-cell-near-quadrangulation-audit.md)
  and [83](../targets/target-c/83-attachment-cell-disjoint-tiling-audit.md):
  harmonic trapping, extreme attachments, disjoint cell interiors,
  `t_I>=delta_I+3`, and loaded contact degree at most three.
- For the Type-II consequences only: [Section 80](../targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md),
  the cell tiling in Section 83, [Section 69](../targets/target-c/69-coherent-grain-interface-audit.md),
  and [Section 73](../targets/target-c/73-pseudosegment-grid-extraction-audit.md).
- [Section 123](../targets/target-c/123-augmented-cell-defect-budget-audit.md)
  and [Audit.134](../audits/target_c_fixed_port_route_bound_independent_audit_2026-10-08.md):
  convex augmented faces, total positive face defect
  `<=2(e_BB-k)`, and the local fixed-port contact route estimate.
- `C-LOADED-NEAR-UNIT-ADJACENCY`, as recorded in the
  [canonical loaded-near-unit audit](../audits/target_c_loaded_near_unit_cap_promotion_audit_2026-10-05.md):
  every loaded-loaded unit contact is a consecutive loaded-hull side
  for sufficiently large `D`.

No unreviewed claim is imported as a canonical premise. The elementary
geometry and counting bridges below are new candidate proofs. Source
isolates remain in the full source and never enter the core kernel.

## 3. An actual attachment forbids a cell angle at most 30 degrees

Fix `a in A_I` and an actual unit neighbor `x in I`. Translate `a` to
zero and rotate so `x=(1,0)`. All contact neighbors of `x` lie in `P_I`:
unloaded neighbors remain in `I`, and loaded neighbors belong to `A_I`.

Suppose the tangent cone of `P_I` at `a` has opening `gamma<=pi/6`.
For any other unit neighbor `y!=a` of `x`, write `y=t exp(i phi)`.
Source separation makes `t>0`. Since `|y-x|=1`,
```math
t=2\cos\phi,\qquad y-x=\exp(2i\phi).
\tag{UC3}
```
With a different initial rotation the last angle has the same doubled
variation. Every `phi` belongs to the cone's angle interval, so all
these other unit-contact rays from `x` lie in an arc of opening at
most `2gamma<=pi/3`.

But `deg_C(x)>=3` gives at least two such other neighbors. Their
distance is strictly greater than one: equality would make a unit
equilateral triangle with `x`. Two unit rays in an arc of opening at
most `pi/3` have endpoint distance at most one. Contradiction.
Thus every angle satisfies
```math
\gamma(a)>\pi/6.
\tag{UC4}
```
The strict 30-degree bound is sharp for geometric positive pinned
three-stars; those fixtures are not canonical global sources.

## 4. Diameter normals give a finite lower bound for cell diameter

For each `a in A_I` choose an actual diameter partner `k_a` and put
`n_a=(a-k_a)/D`, `m_a=(a+k_a)/2`. For every other source point `b`,
```math
n_a\cdot(b-a)\le-|b-a|^2/(2D)<0.
\tag{UC5}
```
These are strict supporting normals. If `d=diam(P_I)`, then
```math
|n_a-n_b|
\le 2d/D+4r_D/D=:\xi.
\tag{UC6}
```

Choose one normal `n_0` and let `t` be its quarter-turn. Pick `a`
minimizing `t dot a` on `A_I`. For `v=b-a!=0`, the strict supports
at `a,b` and their `xi`-closeness to `n_0` give
```math
|n_0\cdot v|<\xi|v|,\qquad t\cdot v\ge0.
```
If `xi<1` the latter inequality is strict. All outgoing chords from
`a` lie in a cone of opening at most `2asin(xi)`. If
`xi<=sin(pi/12)`, that opening is at most `pi/6`, contradicting (UC4).
Hence
```math
\boxed{d>(D/2)\sin(\pi/12)-2r_D.}
\tag{UC7}
```
If `xi>=1` this inequality is automatic. No near-disk force-hull
premise was used.

Every actual attachment lies one unit from `I`. Thus
`diam(I)>=d-2`, and its contact-graph diameter satisfies
`delta_I>=d-2`. The exact canonical pinned ledger gives
`t_I>=delta_I+3>=d+1`. Loaded degree at most three gives
```math
\boxed{|A_I|\ge(d+1)/3.}
\tag{UC8}
```
One may take any fixed `c<sin(pi/12)/2` in the first two assertions
of (UC1) for sufficiently large `D`.

## 5. A uniformly macroscopic area in both branches

Suppose, contrary to a uniform area lower bound, there is a sequence
of actual cells with `area(P_I)/D^2->0`. A compact convex polygon of
area `S` lies within `sqrt(2S)` of a line through a diametral pair:
the triangle-area bound gives height `<=2S/d`, while diameter bounds
it by `d`, and `min(d,2S/d)<=sqrt(2S)`.

Normalize by `D` about `o`. Passing to a subsequence, these lines
converge to a line; their offsets stay bounded because the cells lie
in the source hull. By (UC2), all normalized attachments approach the
radius-one-half circle, while their distances to that line tend to
zero. They therefore cluster around its at most two circle
intersections. A line missing the circle would leave no attachments.

For every fixed `zeta>0`, eventually the attachments lie in at most
two balls of radius `zeta D`. The vertices in either ball remain in
convex position and unit-separated. Their convex hull has diameter
at most `2zeta D` and perimeter at most `2pi zeta D`. With three or
more vertices, population is at most perimeter; adding two covers
smaller sets. Consequently
```math
|A_I|/D\le4\pi\zeta+4/D.
```
Letting zeta tend to zero gives `|A_I|=o(D)`, contradicting (UC7)--(UC8).

Thus some fixed `alpha>0` bounds every actual cell area below for all
sufficiently large `D`. Pairwise interior-disjointness and
`area(F)<=pi D^2/4` give
```math
\boxed{c_I\le\pi/(4\alpha).}
\tag{UC9}
```
This is a uniform component bound, not merely an approximation after
discarding small cells. It allows `c_I=0` and does not constrain the
number of contact-isolated source points.

## 6. Uniform Type-II grids at every actual attachment

In Type II the global cell deficit is `o(D^2)`. With every cell's area
`>=alpha D^2`, each contains unloaded-only actual rhombi of uniformly
quadratic total area. The fixed-epsilon coarse-grain deletion loses
only `O_epsilon(D)` faces globally and has total perimeter
`O_epsilon(D)`. Isoperimetry therefore supplies a coherent quadratic
grain in each cell, with uniform constants.

For any `a in A_I` and fixed `rho in (0,1)`, homothetically crop the
convex hull of that grain about `a` by ratio rho. This auxiliary
region has uniformly quadratic area, lies in
`int(P_I) intersect closed_ball(a,rho D)`, and has perimeter `O(D)`.
The global omitted area is `o(D^2)` uniformly over the moving crops.
Rhombi crossing a crop boundary lie in its width-two tube, so deleting
those bookkeeping faces costs `O(D)` area and perimeter. Isoperimetry
and Section 73 supply a complete coherent grid with uniform positive
linear shores. Cell disjointness puts its actual vertices in `I`.
No source face is physically moved.

## 7. Loaded-only contact chains are uniformly short in Type II

Put `A_* = union_I A_I`. Type-II tiling gives
`area(conv(A_*))>=sum_I area(P_I)=area(F)-o(D^2)`.
Both convex hulls therefore converge, after normalization, to the
same radius-one-half disk. The largest angular gap between consecutive
vertices of `A_*` tends to zero.

A loaded vertex outside `A_*` has only loaded contact neighbors.
Those contacts are consecutive loaded-hull sides, so there are at
most two. There cannot be just one for sufficiently large `D`.
Indeed, its single unit-contact force would be nearly tangent:
for a unit loaded pair `b,a`, chosen strict normals differ by at most
`2/D+4r_D/D`, and the strict support inequalities give
```math
0<n_b\cdot(b-a)\le2/D+4r_D/D.
```
On the other hand every diameter direction from `b` differs from
`n_b` by at most `4r_D/D`. Its positive weighted diameter-force
average, divided by `D sum beta`, has normal component at least
`1-4r_D/D` and norm at most one. It cannot be a positive multiple
of that nearly tangent unit vector. This contradicts equilibrium.

Thus each loaded-only vertex has its two consecutive unit neighbors.
Since Type II has unloaded rhombi, `A_*` is nonempty. Every maximal
loaded-only chain ends in `A_*`. It lies in one consecutive-attachment
angular gap tending to zero. Strict support-normal order puts all its
directed unit sides in a vanishing tangent-direction window. Projection
onto that window's central tangent bounds its length by its endpoint
chord divided by `cos(o(1))`. The endpoint chord is `o(D)` uniformly.
Write the resulting uniform contact-path bound as `ell_D=o(D)`.

For every `b in B` select an attachment `a_b` and a component `I_b`
with `a_b in A_{I_b}`, reached by such a path; take a zero-length path
when `b in A_*`. The selection is fixed before face charging.

## 8. Diameter directions control degree-weighted face multiplicity

### 8.1 A finite separation bound for actual diameter directions

Distinct diameter edges have projective angular separation at least
`a_D=asin(1/(2D))`. If they share an endpoint, unit separation of the
other endpoints gives `theta>=2asin(1/(2D))`.

For disjoint edges oriented with projective angle `theta<=pi/2`, let
their midpoints differ by `s`, and let their unit vectors be `u,v`.
The two crossed endpoint distances at most `D` imply
`|s|<=D sin(theta/2)`. The squared distances between the two same-side
endpoint pairs have average at most `2D^2 sin^2(theta/2)`. Both pairs
are unit-separated, so `theta>=2asin(1/(sqrt(2)D))>a_D`.
Thus any projective angular interval of length `w` contains at most
`2Dw+1` actual diameter directions.

### 8.2 A small convex face is near few diameter incidences

All bounded augmented faces of degree at least five have summed area
`o(D^2)` in Type II: no such face contains an unloaded-only strict
rhombus, whose internal contact edges are retained; cell deficits add
to `o(D^2)`. Their maximum normalized area tends to zero. Every face
lies within `epsilon_D D` of a line, with `epsilon_D->0`.

Loaded points within `rho D+ell_D` of a face are within
`(rho+epsilon_D+ell_D/D)D` of that line. By (UC2), their radial
directions lie in at most four circle arcs of total angular length
`<=12sqrt(rho)+o(1)`. This follows from the cosine interval of length
`4(rho+o(1))` and
`cos(theta)-cos(phi)>=2(phi-theta)^2/pi^2` on `[0,pi]`.

Every incident actual diameter direction differs from the endpoint's
radial direction by `O(r_D/D)=o(1)`. Enlarge the arcs by that amount,
project modulo pi, and use the direction-spacing bound. Counting
both endpoints conservatively yields, uniformly over faces,
```math
\sum_{\substack{b\in B\\
 \operatorname{dist}(b,f)\le\rho D+\ell_D}}\deg_H(b)
\le(48\sqrt\rho+o(1))D.
\tag{UC10}
```
High-degree hubs are included in this incidence count.

A finite version, used by the checker, is also available. If all endpoint
radii lie in `[D/2-eta,D/2+eta]` and all diameter midpoints lie within
`r<D/4` of the same center, the diameter incidence count within a
width-`wD` line strip is at most

`48D sqrt(w+eta/D)+256r+16`.

Radial directions occupy at most four arcs of total length
`<=12sqrt(w+eta/D)`. Normalizing
`b-o=(D/2)n+(m-o)` changes unit direction by at most `4r/D`,
and hence angle by at most `8r/D`. Enlarging the four arcs adds at
most `64r/D` to their total length. Projective splitting uses at most
eight intervals. Direction separation, then doubling to count endpoints,
gives the stated bound. For a body of area `S` and a radius-`rho D`
neighborhood, take `w=rho+sqrt(2S)/D`.

### 8.3 The one global face bank gives few exceptional diameter edges

Fix `M=5`. Let `T_M` be the global degree tail, and put
```math
\Psi_b=
\sum_{\substack{f\text{ in }J_{I_b}^+,\,d(f)>M\\
                \operatorname{dist}(a_b,f)\le\rho D}}(d(f)-4).
```
Every charged face is within `rho D+ell_D` of `b`. Swap sums and use
(UC10) and `T_M<=2(e_BB-k)<=3pi D`:
```math
\sum_{b\in B}\deg_H(b)\Psi_b
\le(144\pi\sqrt\rho+o(1))D^2.
\tag{UC11}
```

The canonical local route bound gives, for every
`z in I_b intersect closed_ball(a_b,rho D)`,
```math
\operatorname{dist}_C(b,z)
\le\ell_D+K_M\rho D+B_M+5\Psi_b.
\tag{UC12}
```
Choose fixed rho with `K_M rho<lambda/4`. Eventually
`ell_D+B_M<lambda D/4`. Endpoints with `Psi_b<lambda D/20` have
contact routes of length `<lambda D` to every vertex of their grids.

The number of actual diameter edges with an exceptional endpoint is
at most the total diameter degree of exceptional endpoints, and hence
```math
\limsup_D D^{-1}\#\{\text{exceptional actual diameter edges}\}
\le(2880\pi/\lambda)\sqrt\rho.
\tag{UC13}
```
A sufficiently small fixed rho makes this less than eta. This proves
the global diameter-to-grid conclusion. It is a count, not a bound
on the exceptional positive KKT diameter weight.

## 9. Verification and remaining limits

The exact checker
[verify_target_c_uniform_cells_diameter_access_2026_10_08.py](../../../research/verify_target_c_uniform_cells_diameter_access_2026_10_08.py)
checks sharp rational unit-star cone geometry, actual diameter-direction
separation, high-degree diameter fans, weighted face incidence,
and thin/small-arc attachment diagnostics.

Fixtures are explicitly nonglobal. Stars test positive pinned
equilibrium at an unloaded vertex; circle/fan sources test actual
diameter geometry but have no source stress. Auxiliary bodies and
attachment subsets are not asserted to be actual canonical cells.
No numerical search certifies the asymptotic theorem.

PASS: 21 positive pinned stars and 126 star source pairs; 45,643
circle/fan source pairs; 13,384 actual diameter-direction pair checks;
11,792 port/body/radius tests; 24 degree-weighted identities; three
single-port high-degree fan witnesses; and six impossible-cell diagnostics.

The analytic proof retains every source isolate and uses actual
loaded endpoints throughout. The inactive-container case may have
no unloaded component or have macroscopic cells containing sparse
core graphs and many isolates. Type-II paths can share vertices,
loaded prefixes, and face banks. No exact contact-isometric endpoint,
refill packet, triangle-free exchange, or strict-D competitor is
constructed. The full Level I conclusion remains unproved.
