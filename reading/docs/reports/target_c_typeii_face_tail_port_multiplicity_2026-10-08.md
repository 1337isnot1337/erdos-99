> Generated reading edition · [exact source](../../../docs/reports/target_c_typeii_face_tail_port_multiplicity_2026-10-08.md) · source SHA-256 `1b5b6d6345c976c6662b6612a704779b28dee702e604ef1b597d88b1cf6ef335`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-6E974B927D40","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->

> **Destination status (2026-10-16).** This source report preserves the full derivation and finite checker. Audit.173's supplement is already present in the destination; `C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY` and `C-TYPEII-ATTACHMENT-COHERENT-PROPER-CAP` are canonical in the [theorem-state manifest](../../../docs/state/theorem-state.yaml). The report's many-grid consequence is subsumed by the existing canonical grid/access claims and is not a separate theorem. The proved cap is selected after the attachment; no prescribed chord, route independence, stress-mass bound, payment or finite move follows. This import creates no theorem transition.

# Target C: Type-II face tails have small loaded-port multiplicity

Date: 2026-10-08.
Run base: `99368bc1c086f1ccd76011ed1fa5b503684563bf`.
Canonical base: `419ab570f137bb5243155086285d10354b6c9616`.
State: `2026-10-08.audit.142`.
Classification: proved candidate awaiting independent audit/promotion.
Registry: unreviewed; noncanonical. Level I and C-II remain open.

Rechecked after rebasing the preceding local work onto
`ca26397adb06a7335458d603d852eb465d61e28c`, state
`2026-10-08.audit.143`. The added partial-wall interior-chord/isolate
regression changes no input used here; no wall shielding is assumed.

## 1. Exact source statement and remaining implication

Take an unbounded canonical contact-minimal, then diameter-pair-minimal,
triangle-free global-source sequence in the Type-II branch. Retain every
source point. Write `B=Vert(F)` for actual loaded endpoints. For an
unloaded component `I` let `A_I` be its actual attachments,
`P_I=conv(A_I)`, and `J_I^+` its augmented harmonic graph.
The contact distance `dist_I(a,z)` permits the specified loaded initial
vertex `a` and otherwise only vertices of `I`.

The candidate proves:

1. For every fixed `lambda>0` and `eta>0` there is a fixed `rho>0`
   such that eventually fewer than `eta D` attachment incidences
   `(a,I)` fail
   
   ```math
   \operatorname{dist}_I(a,z)<\lambda D
   \quad\text{for every }z\in I\cap\overline B(a,\rho D).
   \tag{PM1}
   ```

   The count is over all harmonic components.
2. In the macroscopic cell supplied by Section 78, for every fixed
   `lambda>0` at least `cD` actual attachments have same-component
   epsilon-coherent complete grids within `rho D`, with both shores
   linear in `D`; every grid vertex is reachable from its specified
   attachment by an actual contact path of length `<lambda D`.
   Constants depend on the cell, fixed epsilon, and lambda.
3. Every attachment of this cell admits a proper actual-loaded-chord
   cap containing quadratic same-component coherent mass, with that
   attachment at uniformly positive linear height. The cap is chosen
   after the attachment.

The implication chain is

    Type-II convex faces have vanishing normalized area
      -> each face lies near one line
      -> each face is near a small loaded-hull population
      -> the one global face-tail bank has small port multiplicity
      -> many specified ports have short access to actual grids.

This eliminates a universal many-port obstruction allowed by the global
tail bound alone. It does not give short access at a port specified
independently of the counting argument. It gives no disjointness of the
short paths, simultaneous motion, or phase/population payment. Turning
these packages into a full-source strict-diameter replacement remains
open. The macroscopic inactive-container branch is separate.

## 2. Canonical inputs

- [Section 80](../targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md),
  `C-FULLCORE-NEAR-DISK`: after translation `D^(-1)F` converges to the
  radius-one-half disk; unloaded strict rhombi fill `F` up to `o(D^2)`.
- [Section 83](../targets/target-c/83-attachment-cell-disjoint-tiling-audit.md),
  `C-HARMONIC-CELL-TILING`: cells have disjoint interiors, harmonic
  trapping holds, and their summed unloaded-rhombic deficit is `o(D^2)`.
- [Audit.134](../audits/target_c_fixed_port_route_bound_independent_audit_2026-10-08.md),
  `C-FIXED-PORT-CONTACT-ROUTE-BOUND` and
  `C-BOUNDED-FACE-PORT-ROUTE-BUDGET`: bounded augmented faces are convex
  with simple boundaries, and the fixed-port contact bound holds with
  the stated local face charges.
- [Section 123](../targets/target-c/123-augmented-cell-defect-budget-audit.md),
  `C-AUGMENTED-CELL-DEFECT-BUDGET`:
  `sum_I Q_I^+ <= 2(e_BB-k)`.
- [Sections 69](../targets/target-c/69-coherent-grain-interface-audit.md),
  [73](../targets/target-c/73-pseudosegment-grid-extraction-audit.md), and
  [78](../targets/target-c/78-harmonic-cell-grid-localization-audit.md):
  coarse coherent grains omit `o(D^2)` area and have total perimeter
  `O_epsilon(D)`; quadratic coherent complexes of perimeter `O(D)`
  contain complete grids; one quadratic grain occurs in one component.
- [Audit.133](../audits/target_c_rhombus_bulk_separator_independent_audit_2026-10-08.md):
  quadratic actual rhombus mass has linearly many simultaneous returns
  to distinct actual attachments.

These are used only at their canonical scopes. Conditional Audits.136--137
are not premises. No contact isolate receives a core coordinate.

## 3. Convex face flatness and strip population

Let `Q` be a compact convex polygon of area `S>0`. Choose diametral
vertices `x,y` with `L=|x-y|`. Every triangle `xyz`, `z in Q`, lies in
`Q`, giving `dist(z,ell_xy)<=2S/L`. Also that distance is at most `L`.
Therefore
```math
Q\subset\{z:\operatorname{dist}(z,\ell_{xy})\le\sqrt{2S}\}.
\tag{PM2}
```
This uses `min(L,2S/L)<=sqrt(2S)`, and allows long thin faces.

Suppose the unit-separated convex-position vertices `B` satisfy
```math
\overline B(0,(1/2-\delta)D)\subset F
\subset\overline B(0,(1/2+\delta)D),\qquad 0\le\delta<1/4.
\tag{PM3}
```
Every vertex has radius in that interval. For any line `ell` and `w>=0`,
```math
\#\{b\in B:\operatorname{dist}(b,\ell)\le wD\}
\le12(1+2\delta)\sqrt{w+\delta}\,D+64\delta D+8.
\tag{PM4}
```

The bound in fact requires only the vertex-radius interval and convex
position. The hull inclusions are a sufficient canonical way to obtain
that interval; the exact circle fixtures below use the weaker hypothesis.

Here is a finite proof. Write the strip as `|u dot x-tD|<=wD`. Radial
projection to the radius-one-half circle changes the normal coordinate
by at most `delta D`. The angular directions have cosine in an interval
of length at most `4(w+delta)`, clipped to `[-1,1]`. For
`0<=theta<=phi<=pi`,
```math
\cos\theta-\cos\phi
=2\sin((\theta+\phi)/2)\sin((\phi-\theta)/2)
\ge2\sin^2((\phi-\theta)/2)
\ge2(\phi-\theta)^2/\pi^2.
```
The full angular preimage has length at most
`2sqrt(2)pi sqrt(w+delta)<12sqrt(w+delta)`. Split it into at most four
closed arcs of length at most `pi`.

For an arc of length `Delta`, project its selected points radially to
the outer circle, changing them by at most `2delta D`. Their convex
hull lies in the radius-`2delta D` parallel body of the outer arc hull.
That arc hull has perimeter at most `(1+2delta)D Delta`. Perimeter
monotonicity and the parallel-body formula give the bound
`(1+2delta)D Delta+4pi delta D` for the selected convex hull.
Every selected vertex remains extreme. With at least three vertices,
unit separation bounds population by perimeter; adding two covers
smaller sets. Sum over the four arcs and use `16pi<=64` to get (PM4).
Arc endpoint overlap only overcounts.

Let `E_D` be all bounded augmented faces of degree at least five in
all cells. Every unloaded-only actual rhombus remains a face of its
augmented graph, since all its internal contact edges are retained.
No face of `E_D` contains such a rhombus interior. Cell disjointness
and Section 83 imply
```math
\sum_{f\in E_D}\operatorname{area}(f)
\le\sum_I\{\operatorname{area}(P_I)-A_{4,I}\}=o(D^2).
\tag{PM5}
```
Omitting loaded-loaded edges cannot merge across an unloaded-only
rhombus edge. Polygon-side faces are included; their added sides need
not have length one.

Set `epsilon_D=sqrt(2 max_{f in E_D}area(f))/D`, zero for an empty family.
Then `epsilon_D->0`. Convexity and Type-II Hausdorff convergence give
`delta_D->0` satisfying (PM3). By (PM2)--(PM4), uniformly for every face,
```math
\#\{b\in B:\operatorname{dist}(b,f)\le\rho D\}\le L_D(\rho),
\tag{PM6}
```
where
```math
L_D(\rho)=12(1+2\delta_D)\sqrt{\rho+\epsilon_D+\delta_D}\,D
+64\delta_D D+8.
```
For each fixed `rho>0`,
`limsup_D L_D(rho)/D<=12sqrt(rho)`. No convergence rate is asserted.

## 4. One global tail, with controlled multiplicity

For fixed `M>=5` define
```math
T_M=\sum_{I,f:\ d(f)>M}(d(f)-4),\qquad
\Phi_{a,I}(M,\rho)=
\sum_{\substack{f\text{ in }J_I^+,\,d(f)>M\\
                 \operatorname{dist}(a,f)\le\rho D}}(d(f)-4).
```
Swap the finite nonnegative sums:
```math
\sum_{(a,I):\,a\in A_I}\Phi_{a,I}(M,\rho)\le L_D(\rho)T_M.
\tag{PM7}
```
Each face counts only attachments of its own cell, a subset of `B`.
A port shared by several cells gives several incidences, but each face
enters the global bank once. This is a multiplicity bound, not a
collection of independently available route banks.

Loaded contact degree is at most three, `k>=0`, and `q<=pi D`, so
```math
T_M\le2(e_{BB}-k)\le2e_{BB}\le3q\le3\pi D.
\tag{PM8}
```
Thus, for fixed rho,
```math
\limsup_{D\to\infty}D^{-2}\sum_{(a,I)}\Phi_{a,I}(M,\rho)
\le36\pi\sqrt\rho.
\tag{PM9}
```
A linear global tail remains permitted.

## 5. Short access outside a small exceptional incidence set

Audit.134's proof directly gives the local refinement
```math
\operatorname{dist}_I(a,z)
\le K_M|a-z|+B_M+5\Phi_{a,I}(M,\rho)
\quad\text{if }|a-z|\le\rho D.
\tag{PM10}
```
Every high-degree face met by `[a,z]` is within `rho D` of `a`.
The low-degree tube count is unchanged. Closed faces and distances
retain the degenerate limiting charges used in the canonical proof.

Fix `M=5` and choose `K_M rho<lambda/4`. Eventually
`B_M<lambda D/4`. Every incidence with
`Phi_{a,I}(M,rho)<lambda D/10` satisfies (PM1) for every indicated
target. Equations (PM7)--(PM9) yield
```math
\limsup_{D\to\infty}
\frac{\#\{(a,I):\Phi_{a,I}(5,\rho)\ge\lambda D/10\}}D
\le(360\pi/\lambda)\sqrt\rho.
\tag{PM11}
```
Taking also `360pi sqrt(rho)/lambda<eta/2` proves statement 1.
Equivalently, for each fixed lambda,
```math
\lim_{\rho\downarrow0}\limsup_{D\to\infty}
D^{-1}\#\{(a,I):\exists z\in I,\ |a-z|\le\rho D,\
                    \operatorname{dist}_I(a,z)\ge\lambda D\}=0.
\tag{PM12}
```
This iterated-limit count does not bound a worst specified port or
imply a vanishing global degree tail.

## 6. Many accessible grids in one macroscopic cell

Fix Section 78's actual grain `G_0` in `I`, of area `>=alpha D^2` and
perimeter `O(D)`, with cell `P=conv(A)`. The harmonic maximum principle
gives `I subset int(P)`: a supporting functional maximal at an unloaded
vertex would propagate its value by positive equilibrium to every
attachment, contradicting their noncollinearity.

The grain has at least `alpha D^2` rhombi, since each has area at most
one. Audit.133 gives `|A|>=c_A D` eventually, for fixed `c_A>0`.

For each fixed `rho in (0,1)` and every `a in A` use the auxiliary region
`K_a=a+rho(conv(G_0)-a)`. No source face is moved. This convex region is
in `int(P) intersect closed_ball(a,rho D)`, has area
`>=alpha rho^2 D^2`, and perimeter `<=pi rho D`. The global coarse-grain
omitted area is `o(D^2)`, uniformly over these moving regions.

Remove rhombi meeting `partial K_a`. Their diameter is below two and
their disjoint areas are at least `sqrt(3)/2`, so the width-two boundary
tube contains only `O(D)` such faces, uniformly in `a`. Lost area and
added perimeter are `O(D)`. Surviving coherent components have quadratic
total area and summed perimeter `O_epsilon(D)`. Isoperimetry,
`sum sqrt(area_j)<=sum perimeter_j/(2sqrt(pi))`, gives one quadratic
component with constants uniform over `a`. Section 73 extracts its
complete grid, with two fixed positive linear shore constants.

Its actual edges put it in one unloaded component `I'`. Harmonic
trapping puts each positive-area rhombus in `P_{I'}`, while it lies
in `int(P)`. Cell disjointness forces `I'=I`.
Use statement 1 with `eta<c_A/2` and its fixed rho. At least `c_A D/2`
ports have short contact access to every vertex of their grids. This
proves statement 2. Different grids and paths may overlap, and shore
constants need not stay positive uniformly as lambda tends to zero.

## 7. Select a proper cap for any prescribed attachment

Put `S=area(P)>=alpha D^2`, and fix any `a in A`. Choose `b in A` farthest
from `a`, with `L=|a-b|`. Since `P subset closed_ball(a,L)`,
`L>=sqrt(S/pi)`. Relative to line `ab`, the total signed-height range
is at least `S/D`, since the tangential span of `P` is at most `D`.
Choose `c in A` of absolute height at least `S/(2D)`. Then
```math
\operatorname{area}(\Delta)\ge\frac{S^{3/2}}{4\sqrt\pi D}
\ge\tau D^2,\quad
\Delta=\operatorname{conv}\{a,b,c\},\quad
\tau=\alpha^{3/2}/(4\sqrt\pi)>0.
\tag{PM13}
```
Orient line `bc` so the height `eta(a)` is positive. As both altitude
and base length are at most `D`,
`eta(a)>=2tau D` and `|b-c|>=2tau D`.

Every side of the near-disk loaded hull has length `o(D)`: its supporting
line is at distance at least `(1/2-delta_D)D` from the center, and its
endpoints have radius at most `(1/2+delta_D)D`. Its length is at most
`2sqrt(2delta_D)D`. Therefore `b,c` are nonconsecutive on `F` eventually,
uniformly in `a`. Their chord gives a proper cap
`C=F intersect {eta>=0}`, whose designated hull arc contains `a`.

The triangle has perimeter at most `3D`. Type-II coherent coverage,
discarding only auxiliary faces crossing `partial Delta`, and the same
isoperimetric argument supply a quadratic coherent component
`G subset int(Delta)` with perimeter `O_epsilon(D)`. Its vertices belong
to `I` by cell disjointness. All constants are uniform in `a`.
Since its height is at most `eta(a)` and tangential span at most `D`,
`eta(a)>=area(G)/D`. This proves statement 3.

This supplies a near-port cap package for a prescribed attachment and
a subsequently selected cap. It does not validate a prescribed chord
or cap. The attachment need not maximize height over all of `A`.

## 8. Verification and limits

The exact checker
[verify_target_c_face_tail_port_multiplicity_2026_10_08.py](../../../research/verify_target_c_face_tail_port_multiplicity_2026_10_08.py)
checks rational circle port sets, convex-body flatness, point-to-body
incidences, weighted double counting, the strip bound, and prescribed-
vertex triangle extraction.

Its rational circle points are unit-separated and antipodally paired,
so all are actual diameter endpoints of those finite fixtures. They
are contact-isolated and explicitly nonglobal. The auxiliary convex
polygons are geometric test bodies, not certified augmented source
faces. The checker does not certify canonical stress, Type-II limits,
global optimality, coherent-grain extraction, or a source move.

The checker passed 42,784 full-source pair checks, 96 flatness vertex
checks, 15,680 port/body/radius tests, 21 weighted identities, 84
threshold counts, 480 strip cases and 448 prescribed-port triangles.

The universal candidate implications rest on the analytic proof.
Small face area bounds geometric multiplicity; it does not imply a
vanishing global degree tail. No grid is moved, and no source label
is removed. No independent path-cost payment or compatible motion
is proved. The full-source finite-move/payment obligation remains.
