<!-- theorem-state: {"artifact_id":"ART-AC886134DD35","canonical":true,"claim_ids":["C-TYPEII-ATTACHMENT-COHERENT-PROPER-CAP","C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY"],"claim_statuses":{"C-TYPEII-ATTACHMENT-COHERENT-PROPER-CAP":"canonical","C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.173 supplement — face-tail port multiplicity and prescribed-port caps

Date: 2026-10-08
Canonical base: `a98757336129ce59a1166a5802f4d88d7fdf0cd4`
State before this promotion: `2026-10-08.audit.168`
Frozen source: `origin/research/level-i-closure-20261007` at
`12f6833725f281ce39a6d04ebcb45630b3a6768f`.
Candidate report introduced at `6d27eabfd6ec267a955ade033264296425f843cf`.

The frozen report hash is
`e55a7f7fe9a440a7801d8c0d0cb4221a4d76993805c5609c912567832f8ca164`.
The exact finite-checker hash is
`ea86eb99c1b6fa83fedf31d42cb87d03ad02ba9d85b0706f917eebdf40ff6604`.

## Verdicts

| Candidate claim | Verdict | Disposition |
|---|---|---|
| Most attachment incidences have short local routes to all nearby vertices | PASS — promote | `C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY` |
| At least linearly many ports in one macroscopic cell access local coherent grids | PASS — already follows | Subsumed by the promoted incidence theorem and `C-TYPEII-LOCAL-COHERENT-GRID-ACCESS`; no duplicate ID |
| Every attachment has a proper loaded-endpoint chord cap containing quadratic coherent mass at positive linear height | PASS WITH SCOPE NARROWED to every cell using Audit.173's uniform cell-area theorem | `C-TYPEII-ATTACHMENT-COHERENT-PROPER-CAP` |
| Exact finite verifier proves the universal asymptotic claims | FAIL — it does not | Fixture and arithmetic evidence only; no theorem premise |

Neither promoted result yields a stress-mass bound, disjoint route family, compatible motion, strict diameter improvement, C-II closure, or Level I closure. All contact-isolated source points remain retained.

## 1. Scope and dependencies

Use an unbounded canonical post-ZF C-II Type-II sequence of triangle-free global minimizers in the contact-minimal, then actual-diameter-pair-minimal normal form, with `D -> infinity`, `C=C_*`, and `H=H_*`. Let `B` be the actual loaded diameter endpoints. For each unloaded positive-contact component `I`, let `A_I` be its actual loaded attachment vertices, `P_I=conv(A_I)`, and `J_I^+` its canonical augmented harmonic graph. Contact distances use actual contact edges in `I`, allowing the specified starting attachment and no other loaded internal vertex. Isolates stay in the full source and are not assigned coordinates in these graphs.

The incidence result uses `C-FULLCORE-NEAR-DISK`, `C-HARMONIC-CELL-TILING`, `C-AUGMENTED-CELL-DEFECT-BUDGET`, `C-BOUNDED-FACE-PORT-ROUTE-BUDGET`, and its local route estimate from `C-FIXED-PORT-CONTACT-ROUTE-BOUND`. The cap result additionally uses `C-UNIFORM-HARMONIC-CELL-AREA` and `C-COHERENT-GRAINS`. All these inputs are canonical at the audit base.

## 2. Independent reconstruction of the incidence estimate

For a compact convex face `Q` of area `S`, choose a diametral pair `x,y`, with distance `L`. Every `z in Q` has triangle `xyz` contained in `Q`, so its distance to line `xy` is at most `2S/L`; it is also at most `L`. Therefore the face lies in a strip of half-width at most `min(L,2S/L) <= sqrt(2S)`. This applies to long thin faces as well as round faces.

Let `E_D` be all bounded augmented faces of degree at least six in all cells. An unloaded-only strict rhombus remains a face of its augmented graph because all four of its unloaded contact edges are retained; no face of `E_D` can contain such a rhombus interior. The augmented faces partition their cell, and cell interiors are disjoint. Thus

`sum_{f in E_D} area(f) <= sum_I (area(P_I)-A_{4,I}) = o(D^2)`,

where `A_{4,I}` is the area of the retained unloaded-only strict rhombi in cell `I`. In particular the maximum area of a face in `E_D` is `o(D^2)`, uniformly. Type-II near-disk convergence puts every `b in B` at radius `(1/2+o(1))D` from the common center.

Here is the needed strip count with its dependence made explicit. Suppose a convex-position unit-separated set `B` has all radii in `[(1/2-delta)D,(1/2+delta)D]`. For the angular restriction, first project points radially to the circle of radius `D/2`; this changes each point by at most `delta D`, so points originally in a strip of half-width `wD` project into the cosine preimage interval of width at most `4(w+delta)`. The inequality `cos(theta)-cos(phi) >= 2(phi-theta)^2/pi^2` on `0<=theta<=phi<=pi` bounds the total angular preimage by `2sqrt(2)pi sqrt(w+delta) < 12 sqrt(w+delta)`. Split it into at most four arcs of length at most pi. For the perimeter estimate, instead project each selected original point to the outer circle of radius `(1/2+delta)D`; this second projection moves it by at most `2delta D`. On each arc, the convex hull of the original selected points lies in the `2delta D` parallel body of the projected outer-circle arc hull. That arc hull has perimeter at most `(1+2delta)D` times the arc angle, and the parallel-body perimeter adds `4pi delta D`. Every selected original point is extreme and consecutive selected points remain unit-separated, so their count is at most this hull perimeter; the two-point cases are covered by adding two. Summing the four arcs gives

`# {b in B : dist(b,line) <= wD} <= 12(1+2delta)sqrt(w+delta)D + 64delta D + 8`.

Each face in `E_D` has strip half-width `o(D)`. Consequently, for every fixed `rho>0`, uniformly over all faces in `E_D`, the number of loaded endpoints within `rho D` is at most `(12 sqrt(rho)+o(1))D`. This estimate uses endpoint radii, not an unsupported assumption that the face itself is a circle arc.

For fixed `M>=5`, set

`T_M = sum_{I,f in J_I^+, deg(f)>M} (deg(f)-4)`

and

`Phi_(a,I)(M,rho) = sum_{f in J_I^+, deg(f)>M, dist(a,f)<=rho D} (deg(f)-4)`.

Swapping finite nonnegative sums counts each face once per nearby attachment of its own cell, all of which are in `B`. A port shared by multiple cells creates multiple incidences, but does not duplicate the face in the single global tail. Hence

`sum_(a,I) Phi_(a,I)(M,rho) <= (12 sqrt(rho)+o(1)) D T_M`.

The canonical augmented-cell budget and loaded contact-degree cap give

`T_M <= 2(e_BB-k) <= 2e_BB <= 3q <= 3pi D`,

where `q` is the number of loaded-hull sides. Thus

`limsup D^(-2) sum_(a,I) Phi_(a,I)(M,rho) <= 36pi sqrt(rho)`.

The local fixed-port route estimate from Audit.134, with `M=5`, gives

`dist_I(a,z) <= K_5 |a-z| + B_5 + 5 Phi_(a,I)(5,rho)`

whenever `|a-z|<=rho D`; every high-degree face crossed by the segment is included in `Phi`. Given fixed `lambda,eta>0`, choose fixed `rho>0` so `K_5 rho<lambda/4` and `(360pi/lambda)sqrt(rho)<eta`. Markov's inequality shows fewer than `eta D` attachment incidences have `Phi >= lambda D/10` (after decreasing `rho` to absorb the asymptotic error). For every other incidence, eventually `B_5<lambda D/4`, so the displayed route bound is strictly less than `lambda D` for every `z in I intersect closed_ball(a,rho D)`. This proves the promoted statement. The order of choices is `lambda,eta`, then fixed `rho`, then sufficiently large `D`; it is not a uniform finite-D claim.

## 3. Grid consequence is subsumed

By `C-UNIFORM-HARMONIC-CELL-AREA`, every nonempty cell has at least `alpha D^2` area for one fixed `alpha>0`. The preceding count therefore leaves linearly many good ports in any selected cell. At each port, `C-TYPEII-LOCAL-COHERENT-GRID-ACCESS` can be applied with a smaller fixed crop radius so every grid vertex is within the chosen local-route radius. Thus the candidate's many-accessible-grids statement follows from the two promoted results. It does not warrant a third theorem ID.

This implication only counts ports. It gives no disjointness or independence among their routes or grids; all ports may share paths and grid vertices.

## 4. Every attachment has a proper coherent cap

Fix a cell `P_I`, an attachment `a in A_I`, and fixed `epsilon in (0,pi/6)`. Audit.173 gives `area(P_I)>=alpha D^2`, uniformly for every nonempty cell. Choose `b in A_I` farthest from `a`, and write `L=|a-b|`. Since `P_I` lies in the radius-`L` disk about `a`, `L>=sqrt(area(P_I)/pi)`. The tangential width of `P_I` along line `ab` is at most `D`; hence its total signed-height range over that line is at least `area(P_I)/D`. Choose `c in A_I` with absolute height at least half that range. Then

`area(conv{a,b,c}) >= area(P_I)^(3/2)/(4 sqrt(pi) D) >= tau D^2`,

where `tau=alpha^(3/2)/(4sqrt(pi))>0`.

Relative to line `bc`, the altitude of `a` is at least `2tau D`; since the triangle diameter is at most `D`, `|b-c|>=2tau D`. Every side of the near-disk loaded hull has length `o(D)`: its support line is at distance `(1/2-o(1))D` from the center while its endpoints have radii `(1/2+o(1))D`. Thus `b,c` are nonconsecutive loaded-hull vertices for large `D`. Their chord cuts a proper cap containing `a` on its designated side; both endpoints are actual loaded attachments, not prescribed abstract pins.

The triangle is contained in `P_I`. Its perimeter is at most `3D`. The Type-II coherent-grain theorem omits only `o(D^2)` area globally, and the rhombi meeting the triangle boundary contribute only `O(D)` area. Therefore a quadratic amount of epsilon-coherent rhombic mass remains inside the triangle. The global physical interface perimeter is `O_epsilon(D)`. Isoperimetry then gives one physical coherent component of area at least `beta D^2` and perimeter `O_epsilon(D)`, for a fixed `beta>0`; cell disjointness places it in the same component `I`. The triangle is inside the selected cap. Its height above chord `bc` is at most the height of `a`, and its tangential span is at most `D`, so this coherent mass has height at least `beta D` above `bc`. Constants are uniform over cells and attachments. The cap/chord is selected after `a`; no prescribed-chord conclusion follows.

This proves `C-TYPEII-ATTACHMENT-COHERENT-PROPER-CAP` in the narrowed per-cell scope. A complete grid can be extracted from the coherent component only with the separate pseudo-grid theorem and is not part of this claim.

## 5. Verifier boundary and limits

I inspected and reran the exact checker copied from the frozen branch. It uses `fractions.Fraction`, exact convexity/orientation, exact circle coordinates, and integer-rounded upper square roots. It passed three fixtures with 64, 128, and 256 antipodal circle endpoints; 42,784 full-source pair checks; 96 convex-body flatness vertex checks; 15,680 port/body/radius tests; 21 weighted identities; 84 threshold checks; 480 strip cases; and 448 prescribed-port triangle checks. These fixtures are contact-isolated and nonglobal. The auxiliary polygons are not certified augmented source faces; no Type-II sequence, harmonic cell, stress, coherent grain, global minimizer, or motion is certified by the script. The asymptotic theorems follow from the analytic arguments and canonical dependencies above, not from this finite verifier.

## Frontier effect

Audit.173's supplement supplies (i) a many-port local-access result using the one global face-tail budget, and (ii) a proper cap with coherent mass for every attachment in every Type-II cell. Neither result turns one tail into independent route currency, bounds exceptional KKT mass, or constructs a compatible source move. The exact C-II obligation—source-realized finite move or discrete replacement yielding strict contact loss at diameter `D` or a strict sub-`D` competitor—remains unchanged; C-II and Level I stay open.
