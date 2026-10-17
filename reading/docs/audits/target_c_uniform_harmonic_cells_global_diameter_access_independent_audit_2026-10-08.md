> Generated reading edition · [exact source](../../../docs/audits/target_c_uniform_harmonic_cells_global_diameter_access_independent_audit_2026-10-08.md) · source SHA-256 `60af5da043ca638e6f9740442e18d3d345b2d344cec91dc13cbb933f9ba02936`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F91C599D73F7","canonical":true,"claim_ids":["C-TYPEII-ACTUAL-DIAMETER-GRID-ACCESS","C-TYPEII-LOCAL-COHERENT-GRID-ACCESS","C-UNIFORM-HARMONIC-CELL-AREA"],"claim_statuses":{"C-TYPEII-ACTUAL-DIAMETER-GRID-ACCESS":"canonical","C-TYPEII-LOCAL-COHERENT-GRID-ACCESS":"canonical","C-UNIFORM-HARMONIC-CELL-AREA":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.173 — uniform harmonic-cell geometry and diameter access

Date: 2026-10-08
Canonical base: `a98757336129ce59a1166a5802f4d88d7fdf0cd4`
State: `2026-10-08.audit.168`
Frozen source: `origin/research/level-i-closure-20261007` at
`12f6833725f281ce39a6d04ebcb45630b3a6768f`
Candidate report introduced at `a7b27218c7657dd2de63a82c53e54e5d24bf195a`.

The source report hash is
`d9386f9dc3f4114d4cc34fd3b0c0ecbeb313084ad753abcf2905ee999a4d53d2`.
Its exact finite checker hash is
`a5ae09187c54af4092109549d43f275941573c8ffde40b1aa2a5356c764da3e0`;
the imported helper hash is
`ea86eb99c1b6fa83fedf31d42cb87d03ad02ba9d85b0706f917eebdf40ff6604`.

## Audit verdict

| Claim | Verdict | Canonical disposition |
|---|---|---|
| Uniform cell angle, diameter, attachment-count, area, and component-count bounds in both C-II branches | PASS — promote | `C-UNIFORM-HARMONIC-CELL-AREA` |
| A quadratic coherent grain and complete grid in every Type-II cell, locally accessible near every attachment | PASS WITH REPAIRED PROOF — promote | `C-TYPEII-LOCAL-COHERENT-GRID-ACCESS` |
| All but `eta D` actual diameter edges have both endpoints routed to local grids in Type II | PASS — promote | `C-TYPEII-ACTUAL-DIAMETER-GRID-ACCESS` |
| Candidate's crop of a selected grain's convex hull is itself rhombically occupied near every attachment | FAIL AS WRITTEN — not promoted | Replaced by the cell-crop argument below |
| Candidate's finite auxiliary circle/fan incidence formula as a universal finite theorem | NOT AUDITED / not promoted | Checker fixtures do not establish it |

The claims above are structural only. They prove no bound on exceptional positive KKT diameter weight, no path disjointness or shared route payment, no compatible motion or refill, no strict sub-`D` competitor, and no C-II or Level I closure. The Type-I inactive-container branch receives only the cell-area and bounded-component conclusion.

## Exact setting and dependencies

Take an unbounded canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global-minimizer sequence in Target C C-II normal form, with `D -> infinity`. Let `V` be its nonisolated positive-contact core, `B` the full set of actual loaded diameter endpoints, and `I_r` any connected component of the unloaded positive-contact graph. Let `A_r subset B` be its distinct actual loaded attachments and `P_r=conv(A_r)`. All contact-isolated source points remain in the full source and outside the core graph.

The proof uses only canonical claims: `C-ZRF`, `C-FS-GEOM`, `C-ATTACH-CURRENCY`, `C-FULLCORE-NEAR-DISK` in Type II, `C-COHERENT-GRAINS`, `C-PSEUDO-GRID`, `C-HARMONIC-CARRIER-QUAD`, `C-HARMONIC-CELL-TILING`, `C-AUGMENTED-CELL-DEFECT-BUDGET`, `C-LOADED-NEAR-UNIT-ADJACENCY`, `C-FIXED-PORT-CONTACT-ROUTE-BOUND`, and `C-BOUNDED-FACE-PORT-ROUTE-BUDGET`. No unreviewed premise is used.

The implication chain is

```text
strict source-diameter supports + unloaded degree >= 3
  -> every attachment cell has linear diameter and a linear attachment set
  -> annular attachment geometry rules out a thin cell
  -> every cell has quadratic area; there are O(1) cells
  -> Type-II rhombi fill every cell up to o(D^2)
  -> cell crops near every attachment contain a quadratic coherent grain and grid
  -> loaded-only contact chains have length o(D)
  -> diameter-direction spacing controls face-tail incidence
  -> all but eta D actual diameter edges have accessible endpoint grids.
```

## 1. Both-branch cell theorem — PASS

For `a in A_r`, choose an actual diameter partner `k_a`, set
`n_a=(a-k_a)/D`, and `m_a=(a+k_a)/2`. The diameter constraint gives, for every
other source point `x`,

```math
n_a\cdot(x-a)\le -|x-a|^2/(2D)<0.
```

Thus each attachment is a strict source-hull support point. Every `a in A_r` is a
vertex of `P_r` by Section 62. If `x in I_r` is a unit neighbor of `a`, every other
unit neighbor of `x` lies in `I_r union A_r`, hence in `P_r`. When the tangent cone
of `P_r` at `a` has angle `gamma <= pi/6`, the unit-circle identity in coordinates
`a=(0,0), x=(1,0)` sends each other contact ray from `x` to a ray whose angle is
`2 phi`, where `phi` is the direction from `a`. Its angular span is at most
`2 gamma <= pi/3`. The unloaded vertex `x` has at least three positive contacts by
`C-ZRF`, so two of those other contact rays exist. Their tips are unit-separated and
cannot be at distance exactly one because the source has no unit equilateral
triangle; their distance is therefore strictly greater than one. Two unit rays
separated by at most `pi/3` have tips at distance at most one, a contradiction.
Every cell angle is strictly greater than `pi/6`.

Let `d_r=diam(P_r)`. From the common-center midpoint localization in `C-FS-GEOM`,

```math
|n_a-n_b|\le 2d_r/D+4r_D/D,
\qquad r_D=\sqrt{D\eta_D+\eta_D^2}=o(D).
```
Choose one normal `n_0`, its quarter-turn `t`, and an attachment `a` minimizing
`t dot a`. For every `b in A_r` the strict support inequalities at `a,b` put
`b-a` in a half-plane and in the strip
`|n_0 dot (b-a)| < (2d_r/D+4r_D/D)|b-a|`.
All outgoing attachment chords therefore lie in a cone of opening at most
`2 asin(2d_r/D+4r_D/D)`. The angle bound just proved implies

```math
d_r>(D/2)\sin(\pi/12)-2r_D.
```

Every attachment lies one unit from `I_r`, so `diam(I_r)>=d_r-2`. Its contact-graph
diameter `delta_r` is at least this Euclidean diameter. The exact pinned ledger
` t_r-delta_r-3=s_r+r_r >= 0 ` from Section 62 and the loaded contact-degree cap
three give

```math
t_r\ge d_r+1,\qquad |A_r|\ge t_r/3\ge(d_r+1)/3.
```
In particular, for every fixed `c<sin(pi/12)/2`, eventually
`d_r>=cD` and `|A_r|>=cD/3`, uniformly over all nonempty components.

It remains to rule out `area(P_r)=o(D^2)` uniformly. Suppose a sequence of cells has
that property. A convex body of area `S` and diameter `d` lies in a strip of
half-width at most `min(d,2S/d)<=sqrt(2S)` around the line through a diametral pair:
the body contains a triangle of base `d` and height equal to either one-sided
excursion from that line. After normalization by `D` and translation to the
`C-FS-GEOM` center, a subsequence of those lines converges. Every attachment is
within `o(D)` of that line and within `o(D)` of the radius-`D/2` circle. A limiting
line has at most two intersections with that circle, so for every fixed `zeta>0`,
eventually all attachments lie in two radius-`zeta D` disks. Attachments are in
convex position and unit-separated. In each disk their convex-hull perimeter is at
most `2 pi zeta D`; because consecutive hull vertices are unit-separated, its
population is at most its perimeter (with two extra points covering the degenerate
cases). Hence `|A_r|/D <= 4 pi zeta + 4/D`, contradicting the uniform linear lower
bound as `zeta -> 0`.

There is therefore a fixed `alpha>0` such that every nonempty cell has area at least
`alpha D^2` eventually. Section 83 gives pairwise interior-disjointness and
`sum_r area(P_r)<=area(F)<=pi D^2/4`, so the number of unloaded components is at
most `pi/(4 alpha)`. This is an asymptotic both-branch statement; it does not bound
contact-isolated source points and allows no unloaded component.

## 2. Type-II grid access at every attachment — repaired proof, PASS

In Type II, `C-HARMONIC-CELL-TILING` gives nonnegative local deficits

```math
\Delta_r=area(P_r)-A_{4,r},\qquad \sum_r\Delta_r=o(D^2),
```
where `A_{4,r}` is the area of unloaded-only actual strict rhombi assigned to `I_r`.
The number and total area of rhombi incident to loaded endpoints are `O(D)` by the
loaded degree-three bound, so discard them. `C-COHERENT-GRAINS` supplies, for each
fixed `epsilon in (0,pi/6)`, a global phase cut deleting only `O_epsilon(D)` further
rhombi, with total physical-grain interface perimeter `O_epsilon(D)`.

Fix any `rho in (0,1)`, any cell `P_r`, and any attachment `a in A_r`. Use the
**cell** crop

```math
Q=(1-rho)a+rho P_r.
```
It lies in `P_r` by convexity, satisfies `Q subset closed_ball(a,rho D)` because
`diam(P_r)<=D`, has area `rho^2 area(P_r)>=rho^2 alpha D^2`, and has perimeter
`rho per(P_r)<=rho pi D` by the convex perimeter-diameter inequality. It lies inside the cell; its intersection with the cell boundary is contained in the
two scaled incident sides and has area zero.

The rhombi meeting `partial Q` lie in its width-two boundary tube, whose area is
`O(per(Q)+1)=O_rho(D)` by the planar Steiner formula. Each rhombus has area at least
`a_0=sqrt(3)/2`, so only `O_rho(D)` faces meet that boundary. The cell deficit
`Delta_r=o(D^2)` is uniform over cells because it is nonnegative and bounded by the
sum. Consequently, after removing boundary-crossing faces, loaded-incident faces,
and the `O_epsilon(D)` phase-cut deletions, a positive fraction of `area(Q)` remains
as `epsilon`-coherent rhombi wholly contained in `Q`; for fixed `epsilon,rho`, their
number is at least `c_{epsilon,rho}D^2` eventually.

The total perimeter of all remaining physical components within `Q` is
`O_{epsilon,rho}(D)`: use the canonical global grain-interface bound, and add the
perimeters of the `O_rho(D)+O_epsilon(D)` removed unit rhombi. If those components
contain `R_j` rhombi, their areas are at least `a_0R_j`; planar isoperimetry yields
`P_j>=2 sqrt(pi a_0 R_j)`. Thus `sum_j sqrt(R_j)=O_{epsilon,rho}(D)`. Since
`sum_j R_j>=c_{epsilon,rho}D^2`,

```math
\max_j R_j\ge
\left(\frac{\sum_jR_j}{\sum_j\sqrt{R_j}}\right)^2
\ge c'_{epsilon,rho}D^2.
```

Choose such a single retained physical grain. `C-PSEUDO-GRID` applies with its
rhombus mass and perimeter bounds, giving a complete epsilon-coherent train grid
with both shores at least `c''_{epsilon,rho}D`. All its rhombi and grid centerlines
lie in `Q`, and its actual source vertices lie in `I_r`. Since `a` and `rho` were
arbitrary, this holds uniformly for every attachment in every cell. The constants
depend on the fixed `epsilon,rho`, not on the cell or the source index.

This argument repairs a genuine gap in the candidate wording: a crop of the convex
hull of one selected grain need not itself contain quadratic rhombic area near an
arbitrary attachment. The cell crop is filled because the **sum of all cell
rhombic deficits** is `o(D^2)`; the bounded global interface makes the filled local
crop yield one large coherent component.

## 3. Type-II loaded chains and the global actual-diameter edge count — PASS

Let `A_* = union_r A_r`. The cell tiling and local deficit statements imply
`area(conv(A_*))>=sum_r area(P_r)=area(F)-o(D^2)`. In Type II, `F/D` converges up
to translation to the radius-`1/2` disk. The same is true of `conv(A_*)`, so the
maximum angular gap between consecutive members of `A_*` tends to zero uniformly.

A loaded endpoint outside `A_*` has only loaded unit-contact neighbors. By
`C-LOADED-NEAR-UNIT-ADJACENCY`, those contacts are consecutive loaded-hull sides,
so it has at most two. It has at least one by its positive-contact membership. It
cannot have exactly one: for a selected diameter partner at `b`, the strict support
inequalities make the unit contact vector have normal component `O(1/D+r_D/D)`;
meanwhile the positive diameter-force average has component `1-o(1)` along that
normal by the midpoint localization. Equilibrium cannot balance a nearly tangent
single contact. Thus every nonattachment loaded endpoint has both adjacent loaded
hull contacts. Its contact-only run is bounded by consecutive vertices of `A_*`.

On such a short hull arc, all selected diameter normals are `o(1)`-close to one
radial direction. The two strict support inequalities at each unit hull side force
its unit direction into an `o(1)`-wide tangent window. Projection onto the center of
that window bounds the run length by its endpoint chord divided by `cos(o(1))`.
The endpoint chord is `o(D)` because the attachment angular gap is `o(1)`. Hence
there is a uniform `ell_D=o(D)` contact-path bound from every `b in B` to a chosen
attachment `a_b` in some `A_{r(b)}`.

We independently check the incidence count used to spend the one global face tail.
Distinct actual diameter directions have projective angular separation at least
`asin(1/(2D))`: for edges sharing an endpoint this follows from unit separation of
the other endpoints; for disjoint edges, average the two crossed endpoint squared
distances to bound the midpoint displacement, then average the two parallel-side
squared distances and use unit separation. In particular, any projective angular
interval of width `w` contains at most `2Dw+1` actual directions.

Every bounded augmented face of degree at least six is convex, has diameter at most
`D`, and contains no unloaded-only strict rhombus face: its internal contact edges
would subdivide it. Its area is bounded by the non-rhombic deficit, whose global sum
is `o(D^2)` in Type II. If `S_D=o(D^2)` is the maximum such face area, the face lies
within `sqrt(2S_D)=o(D)` of a line through a diametral pair. Loaded endpoints within
`rho D+ell_D` of that face therefore have radial directions in at most four arcs
of total angular width `12 sqrt(rho)+o(1)`: their radii are `D/2+o(D)` by
`C-FS-GEOM`, and the line-strip condition restricts the cosine of the radial angle
to an interval of length `4rho+o(1)`. Each incident diameter direction is itself
`o(1)`-close to the radial direction at that endpoint, again by midpoint
localization. Enlarging the arcs by `o(1)`, applying the direction-spacing bound,
and counting both endpoints gives, uniformly over such faces,

```math
\sum_{b\in B:\ dist(b,f)\le rho D+ell_D}deg_H(b)
\le (48\sqrt{rho}+o(1))D.
```

Take `M=5`, and for each selected `b` define

```math
\Psi_b=\sum_{\substack{f\in J^+_{r(b)},\ d(f)>5\\
              dist(a_b,f)\le rho D}}(d(f)-4).
```
Every charged face is within `rho D+ell_D` of `b`. Swapping the endpoint and face sums and using the preceding bound together with the one global tail gives

```math
\sum_{b\in B}deg_H(b)\Psi_b
\le(48\sqrt{rho}+o(1))D T_5
\le(144 pi\sqrt{rho}+o(1))D^2,
```
where `T_5<=2(e_{BB}-k)<=3 pi D` by Sections 62, 123, and the loaded
contact-degree cap.

Set `C=4/sqrt(3)+30 pi`, `C_0=90 pi+30`,
`K_5=C+200(5.5)/pi`, and `B_5=C_0+100(5.5)^2`. For every grid vertex `z` in
`Q_{r(b)}` the Audit.134 fixed-port estimate gives

```math
contact\_dist_C(b,z)
\le ell_D+K_5 rho D+B_5+5\Psi_b.
```
Choose fixed `rho` so that `K_5rho<lambda/4` and
`(2880 pi/lambda)sqrt(rho)<eta`. For large `D`, both `ell_D+B_5<lambda D/4`
and the incidence-sum error is small. Every endpoint with
`Psi_b<lambda D/20` then reaches every vertex of its chosen grid by an actual
contact path of length `<lambda D`.

The total diameter degree of endpoints failing this threshold is at most
`(2880 pi/lambda)sqrt(rho)D+o(D)`. Each actual diameter edge with a failing endpoint
is counted by that endpoint's degree, so after slightly decreasing `rho`, at most
`eta D` actual diameter edges are exceptional. All other edges have both endpoints
routed to their own same-component Type-II grids. Each grid lies within
`(rho+o(1))D` of its endpoint because it lies within `rho D` of `a_b` and the
loaded prefix has length `ell_D=o(D)`.

Routes and grids may overlap. No weighted stress-mass bound follows from this
unweighted edge count.

## 4. Verifier boundary, regressions, and frontier effect

I inspected and reran the frozen exact verifier. It passed 21 rational positive
pinned-star fixtures and 126 star-pair checks; 45,643 circle/fan source-pair checks;
13,384 actual diameter-direction pair checks; 11,792 body/port/radius checks; 24
weighted-count identities; three high-degree single-port witnesses; and six
impossible-cell diagnostics. All finite arithmetic uses `Fraction`; square roots are
rounded upward by integer arithmetic. The checker explicitly marks its sources and
bodies as nonglobal or auxiliary. It tests finite ingredients only; it does not
certify uniform asymptotics, actual Type-II cells, grid extraction, globality, or the
analytic implication chain.

No binding regression applies: all endpoints are actual diameter endpoints, loaded
contact chains are not inferred from incident diameter sequences, the cell grids are
source contact-face objects rather than scaffold points, the route theorem is fixed
port in the actual component, and contact isolates are never deleted. The actual
face-tail budget is spent once after weighting by actual diameter degree.

The promotion adds an approximate Type-II endpoint-access theorem. It does not close
the current stress-transversal use: the exceptional `eta D` edges may carry all
positive KKT diameter weight, and no source theorem bounds that exceptional weight.
The exact C-II finite-move/cardinality-restoration and inactive-container obligations
remain. C-II and Level I stay open. The current prompt's exact global endpoint is
unchanged.
