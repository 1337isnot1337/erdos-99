<!-- theorem-state: {"artifact_id":"ART-FADEA00A4952","canonical":true,"claim_ids":["C-CANONICAL-FAN-FOREST-BLOCKER-MATCHING","C-CANONICAL-HALF-DEPTH-BLOCKER-PATH","C-CIRCUMCIRCLE-BLOCKER-CLOSURE","C-CIRCUMCIRCLE-UPPER-PAIR-SAFETY","C-FAN-CONTACT-HULL-FOREST","C-FAN-KKT-MULTIPLIER-BUDGET"],"claim_statuses":{"C-CANONICAL-FAN-FOREST-BLOCKER-MATCHING":"canonical","C-CANONICAL-HALF-DEPTH-BLOCKER-PATH":"canonical","C-CIRCUMCIRCLE-BLOCKER-CLOSURE":"canonical","C-CIRCUMCIRCLE-UPPER-PAIR-SAFETY":"canonical","C-FAN-CONTACT-HULL-FOREST":"canonical","C-FAN-KKT-MULTIPLIER-BUDGET":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent Audit.166: circumcircle blocker depth, fan forests, and stress budgets

**Date:** 2026-10-08
**Audit base:** `origin/main=fec25f568f6db7699a087f03fc6f44f53bb052ac`, state `2026-10-08.audit.161`.
**Frozen source:** `origin/research/level-i-closure-20261007` at `c981b6f818764765bcb99917a9d858599c425471`; the live branch subsequently advanced to `99064d1c942c5e3ed3ef9928091e70de9b788741`, with no changes to either audited artifact.
**Source report:** `docs/reports/target_c_half_depth_fan_forest_and_weight_budget_2026-10-08.md`, SHA-256 `78c1d8c3860e2a60f4e75c29103e0818790bc9358ef22f640c2da7f7e7d8f37f`.
**Source verifier:** `research/verify_target_c_half_depth_fan_forest_2026_10_08.py`, SHA-256 `694851bf3639b10f19351af9e4f32c2bdb4d199b101cb24baebb10beb934437c`.
**Verdict:** PASS — promote four exact claims below, with the displayed scopes.
**Level I:** OPEN. **C-II:** OPEN.

This is an audit of the frozen report, not its later branch tip. The route remains open: the results strengthen the depth of one source path and the count of first blockers, but give neither path disjointness nor a finite source competitor.

## 1. Canonical source and dependencies

For the source-motion statements, take the full finite unit-separated triangle-free global minimum-diameter configuration in Target C's contact-minimal, then actual-diameter-pair-minimal normalization. Retain every source label, including contact-isolated points. Write its actual diameter as `D`; all diameter pairs and contacts below are actual source pairs, not selected stress supports. The globality and tie-breaks are used only in the finite closure contradiction.

The quantitative specialization uses canonical full-source geometry `C-FS-GEOM`: the full-source circumradius obeys `R_circ < D/2 + eta`, where `eta=3^(1/4)*sqrt(D)`, and every actual diameter-pair midpoint is within `L=sqrt(D*eta+eta^2)` of the same full-source circumcenter. The fan hull-side and blocker-uniqueness inputs are the independently promoted `C-CENTERED-FAN-REFLECTIONS`. No conclusion uses positive-stress support in place of the full actual diameter graph.

## 2. Exact circumcircle upper-pair safety

Let a finite source of diameter `D` lie in `B(c,R)`, with `R>=D/2`, and fix an actual diameter pair `pa`. Set `u=(p-a)/D`, `s(x)=u dot (p-x)`, `P=u dot (p-c)`, and `E=sqrt(R^2-D^2/4)`. For `delta>0`, define

\[
A(E,\delta)=\begin{cases}
E^2/\delta+\delta/2,&E\le\delta/2,\\
E+\delta/4,&E\ge\delta/2,
\end{cases}\qquad H=P-A(E,\delta).
\]

**Promoted claim `C-CIRCUMCIRCLE-UPPER-PAIR-SAFETY`.** If `s(x)<H` and translating `x` to `x-delta*u` increases its distance to a fixed source point `y`, then the new distance is strictly below `D`.

Independent derivation: put `t=u dot (x-y)=s(y)-s(x)`. The squared-distance increase is `-2*delta*t+delta^2>0`, hence `t<delta/2`. For the old midpoint `m=(x+y)/2`,

\[
u\cdot(m-c)=P-s(x)-t/2>A(E,\delta)-t/2>0.
\]

The parallelogram identity and `x,y in B(c,R)` give `|x-y|^2/4+|m-c|^2<=R^2`. Substitution into the exact translated squared distance bounds it strictly by

\[
F(t)=4R^2-4(A-t/2)^2-2\delta t+\delta^2.
\]

For `E<=delta/2`, direct completion gives `F(t)=D^2-(t-2E^2/delta)^2<=D^2`. For `E>=delta/2`, `F(delta/2)=D^2` and `F'(t)=4E-delta-2t>=0` for `t<=delta/2`; since the actual `t` is strictly below `delta/2`, `F(t)<=D^2`. The strict midpoint-projection bound makes the actual new squared distance `<F(t)`, proving `<D^2` in both branches. No translated point is assumed to remain in the ball, and every old upper pair is covered.

The report's four-point example at `R=D/2` is a valid sharpness check for the finite threshold `D/2-delta/2` when that threshold is positive: an outward pair with `0<epsilon<delta/2` increases past `D`. It is nonglobal and is not a counterexample to the canonical source claim.

## 3. Full-source finite closure and the half-depth consequence

For the canonical source, define `x -> y` if moving `x` alone by `-delta*u` would change an old strict lower pair to distance `<=1`, or an old unit pair to distance `<1`. The report explicitly closes under every such arrow; it does not use a first-order velocity.

**Promoted claim `C-CIRCUMCIRCLE-BLOCKER-CLOSURE`.** If `H>0` and `0<delta<2D`, no arrow-closed set `R0` containing `p` can have `s(x)<H` for every `x in R0`. Hence the arrow closure from `p` reaches depth `H`. A first-crossing path has distinct vertices, edge lengths `1<=d_j<=1+delta`, depth increments `Delta s_j>delta/2`, and

\[
L_{path}\ge H/(1+\delta),\qquad
\sum_j(d_j-1)<\delta(H+1+\delta)-L_{path}\delta^2/2.
\]

Proof reconstruction: translate all labels in a proposed closed `R0` by `-delta*u`, fixing all other labels. Internal pairs are unchanged. Arrow-closure preserves every crossing lower constraint, with old strict pairs remaining strictly above one and old contacts remaining at least one. Thus the new contact graph is a subgraph of the old triangle-free contact graph. For crossing upper pairs, a nonincreasing distance stays at most its old value; an increasing distance is strictly below `D` by Section 2, so no old subdiameter pair becomes a diameter pair. Also `A(E,delta)>=E`, `P<=R`, and `R-E<=D/2`, so `H<=D/2`; the carrier `a` is outside `R0`. The old diameter pair `pa` therefore shortens strictly. If the new diameter is below `D`, global minimality is contradicted. At diameter `D`, either contact count falls, contradicting contact minimality, or it is unchanged and the actual diameter-pair count falls, contradicting the second tie-break. This uses a finite move of all points in `R0`, not separately feasible single-vertex moves.

For the canonical large-source corollary choose `delta=1/D`. By `C-FS-GEOM`, with `L=sqrt(D*eta+eta^2)`, the midpoint estimate gives `P>=D/2-E` and monotonicity of `A` gives

\[
H\ge \widehat H:=D/2-2L-1/(4D).
\]

The finite arithmetic is `L^2/D^2=eta/D+eta^2/D^2 < 4/(3*sqrt(D))+7/(4D) <= 4/300+7/40000 <1/64` for `D>=10000`; hence `L<D/8` and `Hhat>0`. Along any unbounded canonical source sequence, `Hhat/D -> 1/2`. Taking the first crossing of `Hhat` in the same closure proof yields `liminf(path length/D)>=1/2`; the displayed excess inequality yields `limsup sum(d_j-1)<=1/2`.

This path conclusion starts at **any supplied actual diameter endpoint** `p`, not just a fan leaf. In the degree-two fan specialization, the exact first reflection keeps the two old contacts, so its first arrow is a strict old noncontact and retains the Audit.152 first-edge depth bound. The new result strengthens the existing canonical `D/10` fan-path bound to `D/2-o(D)` for large sources. It still gives one path at a time and no cross-leaf separation or charging.

## 4. Fan forest and improved first-blocker matching

Let `F_fan` be the set of actual degree-one diameter vertices with exactly two unit contacts, both at distance `D` from their unique actual diameter partner; retain all source labels. For `D>=5`, each fan contact is a full-source hull side by the cap argument in `C-CENTERED-FAN-REFLECTIONS`. Thus these two contacts are exactly the two hull neighbors of the fan leaf. The induced contact graph on `F_fan` is a subgraph of the full-source hull cycle. That cycle has a nonfan vertex: any fan's carrier is incident to the three distinct diameter pairs to the leaf and its two contacts, so its actual diameter degree is at least three. Therefore the fan-induced graph is a disjoint union of paths, and it has an independent set of size at least `ceil(U/2)`, where `U=|F_fan|`.

For `D>=10000`, `C-FS-GEOM` gives every actual diameter midpoint within `T=L<D/8` of the full-source circumcenter. This satisfies both centered-fan thresholds: `T<=D/6-2` and `T<(D-2)/(2*sqrt(2))`. The canonical centered-fan theorem applies to the independent set of size `ceil(U/2)`: solo reflections require strict-pair blockers; its exact hull-normal argument makes the blockers distinct; the nearby-actual-diameter-endpoint separation excludes actual diameter endpoints as blockers. A selected fan leaf cannot itself be another selected leaf's blocker, since selected leaves are separated by at least `sqrt(2)` and each reflection moves only `1/D`. Every resulting pair is therefore loaded-to-diameter-inactive, vertex-disjoint, and has old distance in `(1,1+1/D]`.

**Promoted claim `C-CANONICAL-FAN-FOREST-BLOCKER-MATCHING`.** In the canonical full-source normalization with `D>=10000`, the fan set above has a contact-induced path forest and yields at least `ceil(U/2)` pairwise vertex-disjoint loaded-fan / diameter-inactive blocker pairs. This improves the prior `ceil(2U/5)` consequence without asserting `U` is large. “Loaded” here means an endpoint of an actual diameter pair; no selected-stress support is substituted.

The forest and independent-set proof is independent of finite sampling. The matching's uniqueness and endpoint-inactivity steps use only the already canonical `C-CENTERED-FAN-REFLECTIONS` under its stated midpoint hypotheses, which are verified above for `D>=10000`.

## 5. KKT multiplier budget

**Promoted claim `C-FAN-KKT-MULTIPLIER-BUDGET`.** For any normalized KKT stress of a source containing these fan leaves, use the convention `sum_H beta=1`. The virial identity gives `sum_C alpha=D^2`. At a fan leaf `p` with carrier `a`, the two contact vectors have equal radial projection `1/(2D)` along `(p-a)/D` and opposite tangent components. Local equilibrium therefore gives `alpha_(p p-)=alpha_(p p+)=D^2*beta_(p a)` (the identity also holds when these coefficients vanish).

For an independent fan set `S`, its incident contact edges are distinct; summing their nonnegative multipliers yields `2*sum_(p in S) beta_(p a)<=1`. In a fan path component with `r` leaves, adjacent leaves have the same carrier by uniqueness of their actual diameter partners, and the `r+1` distinct contact edges incident to the component each have weight `D^2*beta_r`. Across components these edge sets are disjoint, so `sum_components (r+1)*beta_r<=1`. Both inequalities are exact. They give no integer population bound without a separate lower bound on these stress multipliers.

## 6. Verifier, regressions, and remaining gap

I inspected and reran the frozen exact verifier. It passed 966 rational quadratic identity checks; 42 parameter cases containing 261,916 valid source cross-pairs (102,148 with increasing distance); nine exact sharp-threshold fixtures with 54 source-pair and 54 square-competitor checks; and six circular-arc fan fixtures with complete source pair graphs, hull/contact/diameter reconstruction, exact maximum-independent-set checks, and 150 local fan-balance checks. The script explicitly labels the fixtures nonglobal and says they do not verify universal analytic claims or full-source KKT existence. Its finite examples support the algebra and expose no edge-case failure; the universal claims above rely on the displayed proofs.

Hostile checks: all contact isolates remain in the finite translation and the hull cycle; actual diameter edges are kept distinct from positive stress support; closure is simultaneous; upper distances are controlled for all crossing pairs; the argument never upgrades a first-order move or a local fixture to global optimality; and no path-disjointness is inferred from the matching of first blockers.

**Exact unresolved implication:** convert the stronger one-path depth and conditional `ceil(U/2)` first-blocker matching into cross-leaf path separation, a shared finite competitor, or a canonical integer/payment inequality. The report provides none of these. C-II and Level I remain open.
