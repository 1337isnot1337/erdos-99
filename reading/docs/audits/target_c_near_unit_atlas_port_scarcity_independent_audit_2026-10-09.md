> Generated reading edition · [exact source](../../../docs/audits/target_c_near_unit_atlas_port_scarcity_independent_audit_2026-10-09.md) · source SHA-256 `d977d03d3506e850ce81e259567342a318641b7de40517593741a657693f61a6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2ABFCD11BEF1","canonical":true,"claim_ids":["C-NEAR-UNIT-ATLAS-PORT-SCARCITY","C-THREE-PORT-REPEATED-ANCHOR-DIRECTION-BOUND"],"claim_statuses":{"C-NEAR-UNIT-ATLAS-PORT-SCARCITY":"canonical","C-THREE-PORT-REPEATED-ANCHOR-DIRECTION-BOUND":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.211 — repeated-anchor and near-unit port scarcity

Date: 2026-10-09. Audit base: `origin/main=eebbd5dfbd70b7264c0a7a83e776b8ded71dd69a`, state `2026-10-09.audit.204`.

## Frozen candidate and verdict

- Source branch: `origin/research/level-i-fused-review-20261009`.
- Frozen source commit: `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate artifacts: the repeated-anchor variant in Section 13.4 and Section 13.6 of `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.
- Verdicts: **PASS WITH EXPLICIT HYPOTHESIS — promote** `C-THREE-PORT-REPEATED-ANCHOR-DIRECTION-BOUND`; **PASS WITH NARROWED SCOPE — promote** `C-NEAR-UNIT-ATLAS-PORT-SCARCITY` under the explicit finite-atlas/local-approximation hypothesis.

## Repeated-anchor finite direction theorem

Let `a_0,a_1,a_2` be arbitrary planar anchors, which may coincide, and let integers `0<r<s`. For a unit direction `t`, put

$$
 p_0=z,\qquad p_r=z+rt,\qquad p_s=z+st.
$$

Assume

$$
 |p_0-a_0|=|p_r-a_1|=|p_s-a_2|=1,
 \qquad |p_r-a_0|\ge1.
$$

Then at most ten distinct directions `t` are feasible. Several translations at one direction are allowed. The extra cross-pair lower bound is essential to the stated proof scope and is not inferred from the three unit contacts.

### Independent proof

Translate `a_0` to zero and write `A=a_1-a_0`, `B=a_2-a_0`, `C=sA-rB`. The two equations after subtracting `|z|^2=1` are

$$
 z\cdot(rt-A)=-\tfrac12|rt-A|^2,
 \qquad z\cdot(st-B)=-\tfrac12|st-B|^2.
$$

Their determinant is `d(t)=det(t,C)+det(A,B)`. If it vanishes identically, `C=0`, so `A/r=B/s=c`; comparing the equations forces `t=c`, giving at most one direction. Otherwise there are at most two singular directions. On every other direction, Cramer's rule makes `z(t)` rational with an affine denominator and quadratic numerators. The equation `|z(t)|^2=1` has degree at most four on the unit circle; unless it is an identity, it has at most eight regular roots. It remains to rule out the identity case.

When `d` is nonidentically zero, `C` is nonzero. A linear combination of the equations makes `z(t)\cdot C` affine in `t`. Rotate so `C` is horizontal; then `z_x=L(t)=c_0+c_1t_x+c_2t_y`. If `L` is constant, `|z|=1` makes `z` constant on the real circle. The second unit-distance identity forces `A=z` and `r=1`; the third forces `B=z` and `s=1`, contrary to `r<s`.

If `L` is nonconstant, rationality of `z_y` makes `1-L^2=z_y^2` a rational square on the complexified unit circle. The two disjoint level sets `L=1` and `L=-1` must each meet the circle with even multiplicity. Both lines are therefore tangent, giving `c_0=0` and `c_1^2+c_2^2=1`. Hence `z(t)=Ot` for a fixed orthogonal matrix `O`. A reflection is impossible because `(O+rI)^T(O+rI)=(1+r^2)I+2rO` is not scalar. Thus `O` is a rotation. The third contact identity has matrix `O+sI`, invertible since `s>=2`; its first harmonic forces `B=0`. Then `p_0=Ot` and `p_s=(O+sI)t` both lie on the unit circle centered at `a_0=0`. Their strict intermediate point `p_r=(1-r/s)p_0+(r/s)p_s` lies inside the open disk, contradicting `|p_r-a_0|>=1`. The identity branch is excluded, leaving at most eight regular plus two singular directions.

No anchor distinctness is used. No numerical root count is substituted for the exact degree-four bound.

## Near-unit finite-atlas port scarcity

Consider a canonical post-ZF C-II sequence in either branch, with `D->infinity`, `q` loaded-hull vertices and loaded-hull perimeter `P_F`. Let `a_D` count loaded vertices with a chosen actual unloaded unit neighbor assigned to one of a fixed finite number `J` of unit-rhombic lattice charts; chart bases may vary with `D` but their basis angles stay in `[pi/3,2pi/3]`.

Assume that on every bounded physical loaded-hull window, for each chart the actual chosen neighbors in that chart are within `epsilon_{D,M}->0` of one common translate of its reference lattice, uniformly over windows, for every fixed window size `M`. No common translation between different windows is required. Then

$$
 P_F-q=o(D)\quad\Longrightarrow\quad a_D=o(D).
$$

Consequently, along any sequence with `a_D>=gamma D` for a fixed `gamma>0`, the loaded-hull excess ratio `(P_F-q)/D` has positive liminf. This supplies no numerical positive constant.

### Independent reconstruction

Write the loaded-hull side lengths as `ell_i>=1`, so

$$
 E_D=P_F-q=\sum_i(ell_i-1)=o(D).
$$

Choose `delta_D=sqrt(E_D/D)+D^(-1/10)`. Then `delta_D->0` and `E_D/delta_D=o(D)`. At most `E_D/delta_D=o(D)` sides have length greater than `1+delta_D`. For each fixed block size `M`, discard blocks touching any such side; this removes `o(D)` loaded vertices. Every remaining side has length in `[1,1+delta_D]`. For large `D` it is below a fixed threshold `t<sqrt(2)`, so `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE` makes it an actual full-source hull side.

Audit.206's midpoint and support-derivative bounds radialize these sides by `O(D^(-1/3))`. A fixed physical window has bounded diameter, hence its loaded chain converges, after normalization, to a straight unit chain. The local atlas assumption supplies one translated reference lattice for the chosen neighbors assigned to each chart in that window.

Fix `M`. A remaining block with more than `2J` chosen ports contains three assigned to one chart, at loaded indices `i,i+r,i+s` with `0<r<s<M`. After passing to a subsequence, the chart basis and the finite lattice-offset pattern converge. The limiting anchors may repeat. The first anchor is an actual unloaded source point, while the middle loaded site is distinct from it, so the source separation inequality `|p_r-a_0|>=1` passes to the limit. The repeated-anchor theorem applies and leaves at most ten limiting tangent directions per chart/pattern. For fixed `M` there are only finitely many charts and lattice-offset patterns; compactness therefore puts all rich-block tangents within `tau_{D,M}->0` of a fixed finite set.

All loaded endpoints in rich blocks, except the `o(D)` endpoints touching discarded sides, have both adjacent loaded-hull sides in the same shrinking tangent window. At a block boundary, a near-unit side in the neighboring block has its outward normal radialized at the same loaded endpoint, so it shares the rich block's tangent window; endpoints adjacent to discarded sides were already charged. The full-source diameter normal at such an endpoint lies in the corresponding normal cone. Audit.203's actual-diameter-normal window estimate bounds the number of endpoints in each shrinking window by `o_M(D)`. There are finitely many limiting directions, so all rich blocks contribute `o_M(D)` ports. Each nonrich block has at most `2J` ports, and the number of blocks is at most `ceil(q/M)+1`. Thus

$$
 a_D\le 2J(\lceil q/M\rceil+1)+o_M(D)
$$

for every fixed `M`. The loaded hull's perimeter is at most `pi D`, so `q<=pi D`. Divide by `D`, first let `D->infinity` at fixed `M`, then let `M->infinity` to get `a_D=o(D)`. The order of limits is essential.

If `a_D>=gamma D` but `(P_F-q)/D` had liminf zero, a subsequence would satisfy `P_F-q=o(D)` and contradict the theorem. Hence a positive liminf follows, with no explicit rate.

## Hostile scope, dependencies, and verifier boundary

- The repeated-anchor theorem uses exactly the extra lower bound from the first unloaded anchor to the middle loaded site. It does not promote an unrestricted repeated-anchor claim.
- The atlas approximation is required on every bounded physical loaded window, uniformly for each fixed window size. The chart set is fixed finite, but chart orientations and translations may vary with `D` and from window to window.
- The near-unit theorem uses `C-FS-GEOM`, `C-FS-DIAMETER-MIDPOINT-D2-3`, `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE`, `C-LOADED-HULL`, and `C-LOADED-WALK-DIRECTIONAL-STRAIN` only for its audited full-source normal-window count, plus the repeated-anchor finite theorem above.
- Contact-isolated points remain in the full-source hull, support, and separation arguments. No chart is extracted from canonical sources, and no motion, capacity, or strict-diameter competitor is constructed.
- No finite verifier certifies the rational identity or compactness arguments. The degree-four root count and actual-normal window theorem are used only in their audited scopes.

**Frontier effect:** none. The finite-atlas premise and near-unit saturation are not established for canonical sources; C-II and Level I remain open.
