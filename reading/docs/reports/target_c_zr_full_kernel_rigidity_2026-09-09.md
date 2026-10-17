> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_full_kernel_rigidity_2026-09-09.md) · source SHA-256 `53594cdeb49528be3f159c384a8980cd5ba47edc4a57948be2c8773f77379647`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2681D123CCE0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — full-kernel consequences of ZR: strict cuts, universal rigidity, and bridge matching

**Date:** 2026-09-09  
**Repository state:** `4bc7c9baddb38d12cbadde8394992c0e9f708104`  
**Run type:** closing-proof continuation and proof audit  
**Target:** Target C, Gate C-II  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`, with the run-specific C–Z instructions supplied separately  
**External web search:** used only for a current-status check; no theorem imported  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The audited report-level chain Z -> ZC -> ZR -> ZF does not yet prove the exact global face inequality needed for Level I. This continuation extracts new exact consequences of the maximal scalar-stress kernel in ZR. They eliminate every exact response-cut equality after ZR, prove universal rigidity and redundant infinitesimal rigidity of the mixed contact/diameter core, force the mixed active graph to be 3-vertex-connected, and sharpen every contact-bridge cut to a two-diameter-edge obstruction.

These are exact structural advances. They do not control the contact-isolated source population, do not give a spectral gap for the response defect, and do not prove the remaining face inequality.

## 1. Starting endpoint

The controlling canonical module is
[`../targets/target-c/56-ci-restored-frontier.md`](../targets/target-c/56-ci-restored-frontier.md): C-I is closed, and C-II is the remaining global gate. The campaign reports
[`campaign_zero_transfer_and_narrow_paths_2026-09-09.md`](campaign_zero_transfer_and_narrow_paths_2026-09-09.md) and
[`campaign_zero_transfer_defect_review_2026-09-09.md`](campaign_zero_transfer_defect_review_2026-09-09.md) audit the report-level consequences

```math
\ker\Omega=\operatorname{span}\{\mathbf 1,P_x,P_y\},
\qquad \operatorname{rank}\Omega=v-3,
\tag{1.1}
```

and

```math
e+h\ge 2v-2.
\tag{1.2}
```

Here `v` counts the nonisolated contact core only. Isolated source points are retained in the global source and are not included in (1.1).

The shortest scalar Level I endpoint remains

```math
\boxed{
 b+\sum_{F\text{ bounded}}(\deg F-4)>2h.
}
\tag{1.3}
```

By Euler, (1.3) is exactly equivalent to `e+h<2v-2`, contradicting (1.2).

The present implication chain is instead

```text
ZR exact affine kernel
  -> exact terminal Schur kernel
  -> every nontrivial response cut is strict
  -> C64 zero-excess terminals disappear

ZR + PSD stress + three diameter directions
  -> universal rigidity of the mixed core
  -> redundant infinitesimal rigidity + 3-vertex-connectivity
  -> every contact bridge is crossed by at least two diameter bars
  -> every nonsingleton bridge cut contains a two-edge diameter matching
```

This removes exact-equality and star-only subbranches but does not itself imply (1.3).

## 2. Strongest genuinely new audited theorem

Work with a triangle-free global minimizer in the lexicographic C-II normal form: first minimize the number of contacts, then the number of diameter pairs. Assume `D>=9`. Let

- `V` be the nonisolated contact core, `|V|=v`;
- `C` be its complete unit-contact set;
- `H` be the active diameter-pair set in the diameter-minimal representative;
- `B=B_+` be the loaded terminal set, `|B|=q`;
- `I=V\B`;
- `alpha_e>0` for every `e in C` and `beta_h>0` for every `h in H` be a relative-interior normalized KKT stress.

Thus

```math
\sum_{e\in C}\alpha_e=D^2,
\qquad
\sum_{h\in H}\beta_h=1.
\tag{2.1}
```

Write

```math
\Omega=L_C(\alpha)-L_H(\beta).
\tag{2.2}
```

Use the audited ZC/ZR conclusion

```math
\Omega\succeq0,
\qquad
\ker\Omega=\operatorname{span}\{\mathbf1,P_x,P_y\}.
\tag{2.3}
```

Let `Lambda` be the Dirichlet response of the positive contact network on `B`, and put

```math
M=\Lambda-L_H(\beta).
\tag{2.4}
```

Finally let

```math
J=(V,C\cup H)
\tag{2.5}
```

be the mixed active bar graph.

### Theorem ZK — maximal-kernel rigidity package

Under the preceding hypotheses:

1. **Exact terminal kernel.**  
   
   ```math
   \ker M
   =\operatorname{span}\{\mathbf1_B,P_x|_B,P_y|_B\},
   \qquad
   \operatorname{rank}M=q-3.
   \tag{ZK1}
   ```


2. **Every proper terminal cut is strictly response-dominated.** For every nonempty proper `S subset B`, if `c_bk=-Lambda_bk`, then
   
   ```math
   \boxed{
   \sum_{b\in S,\ k\notin S}c_{bk}
   >
   \sum_{\substack{bk\in H\\b\in S,\ k\notin S}}\beta_{bk}.
   }
   \tag{ZK2}
   ```

   In particular, every loaded terminal has strict local response excess:
   
   ```math
   d_b:=\sum_{k\ne b}c_{bk}
   >
   s_b:=\sum_{k\ne b}\beta_{bk}
   \qquad(b\in B).
   \tag{ZK3}
   ```

   Thus the zero-excess set in C64 is empty after ZR.

3. **Universal rigidity of the mixed core.** Any realization `y_i` of `J` in any Euclidean space `R^d` satisfying
   
   ```math
   |y_i-y_j|=1\quad(ij\in C),
   \qquad
   |y_i-y_j|=D\quad(ij\in H)
   \tag{ZK4}
   ```

   is congruent to the original planar core.

4. **Redundant infinitesimal rigidity.** Deleting any one bar of `C union H` leaves an infinitesimally rigid planar framework on the same `v` vertices.

5. **Three-vertex-connectivity.** The mixed graph `J` is 3-vertex-connected.

6. **Bridge matching.** Let `e=uv` be a contact bridge and let `X,Y` be the two components of `C-e`, with `u in X`, `v in Y`. Then at least two active diameter edges cross `X|Y`. If `|X|,|Y|>=2`, two such diameter edges can be chosen vertex-disjoint.

### Proof of ZK1

Order the stress matrix by `B,I`. The contact interior Dirichlet block `L_II` is positive definite because the positive contact core is connected and `B` is nonempty. The standard Schur congruence used in C64 gives

```math
\Omega
\sim
\begin{pmatrix}
M&0\\
0&L_{II}
\end{pmatrix}.
\tag{2.6}
```

Therefore

```math
\operatorname{nullity}M
=
\operatorname{nullity}\Omega
=3.
\tag{2.7}
```

Affine equilibrium gives

```math
M\mathbf1_B=0,
\qquad
M(P_x|_B)=0,
\qquad
M(P_y|_B)=0.
\tag{2.8}
```

The force hull is two-dimensional, so these three terminal vectors are independent. Equation (2.7) leaves no further kernel. This proves (ZK1).

### Proof of ZK2 and ZK3

C34 gives `q>=6` for `D>=9`. Every terminal in `B` is an extreme vertex of the convex core hull. Hence no three distinct terminals are collinear.

Fix a nonempty proper `S subset B`. If the indicator `1_S` belonged to the affine kernel in (ZK1), an affine scalar function on the plane would take one constant value on `S` and the other constant value on `B\S`. Since `q>=6`, one of these two sets contains at least three terminals. Those three terminals are noncollinear, so an affine function constant on them is constant on the entire plane. This contradicts the two distinct indicator values. Therefore

```math
\mathbf1_S\notin\ker M.
\tag{2.9}
```

Because `M` is PSD, zero quadratic energy is equivalent to membership in its kernel. Hence

```math
\mathbf1_S^{\mathsf T}M\mathbf1_S>0.
\tag{2.10}
```

The Laplacian energy identity expands this as

```math
\mathbf1_S^{\mathsf T}M\mathbf1_S
=
\sum_{b\in S,k\notin S}
(c_{bk}-\beta_{bk}),
\tag{2.11}
```

which is (ZK2). Taking `S={b}` proves (ZK3).

A slightly stronger form will sometimes be useful: if `S subset B` and `|B\S|>=3`, then the principal matrix `M_SS` is positive definite. Indeed, a nonzero vector supported on `S` with zero `M`-energy would extend to an affine kernel vector vanishing at at least three noncollinear terminals, hence would vanish identically.

### Proof of universal rigidity

Let `y_i in R^d` satisfy (ZK4), and write `y^(r)` for its `r`-th coordinate vector on `V`. By (2.1),

```math
\begin{aligned}
\sum_{r=1}^d (y^{(r)})^{\mathsf T}\Omega y^{(r)}
&=
\sum_{ij\in C}\alpha_{ij}|y_i-y_j|^2
-
\sum_{ij\in H}\beta_{ij}|y_i-y_j|^2\\
&=
\sum_{ij\in C}\alpha_{ij}
-D^2\sum_{ij\in H}\beta_{ij}\\
&=D^2-D^2=0.
\end{aligned}
\tag{2.12}
```

Every summand on the left is nonnegative because `Omega>=0`. Therefore each coordinate vector belongs to the kernel in (2.3). There are a vector `a in R^d` and a linear map `A:R^2->R^d` such that

```math
y_i=a+Ap_i
\qquad(i\in V).
\tag{2.13}
```

There are at least three active diameter edges. Indeed `q>=6` and every terminal is incident to an active diameter edge. Their projective directions are distinct. Two disjoint diameter chords cross by the diameter-thrackle property and hence cannot be parallel. Two diameter chords sharing an endpoint cannot lie on the same projective line: the same ray would repeat the other endpoint, while opposite rays would put the two other endpoints at distance `2D>D`.

For every diameter vector `r=p_i-p_j`, equation (ZK4) and (2.13) give

```math
r^{\mathsf T}(A^{\mathsf T}A-I_2)r=0.
\tag{2.14}
```

A nonzero homogeneous quadratic form in two variables has at most two projective zero directions. Equation (2.14) holds on at least three distinct projective directions, so

```math
A^{\mathsf T}A=I_2.
\tag{2.15}
```

Thus `A` is an isometric embedding of the original plane. Equation (2.13) preserves every pairwise distance, not merely the bar lengths. The realization `y` is congruent to the original core. This proves universal rigidity.

### Proof of redundant infinitesimal rigidity

Let `R_J` be the planar bar-rigidity matrix of `J`. ZF gives

```math
\operatorname{rank}R_J=2v-3.
\tag{2.16}
```

The KKT equilibrium is a nonzero left-kernel relation among its rows: use coefficient `alpha_e` on each contact row and `-beta_h` on each diameter row. Relative interior gives

```math
\alpha_e>0,
\qquad
\beta_h>0,
\tag{2.17}
```

on every active row. Hence every coefficient in this row dependence is nonzero. For any chosen row `r_g`, solve the dependence for that row:

```math
r_g
=-\frac1{\omega_g}
\sum_{f\ne g}\omega_f r_f.
\tag{2.18}
```

So deleting `r_g` does not change the row span or its rank `2v-3`. This holds for every active contact or diameter bar. The mixed framework is redundantly infinitesimally rigid.

### Proof of 3-vertex-connectivity

Since `q>=6`, the graph has more than three vertices.

First suppose `J` has a cut vertex `z`. Let `S` be one component of `J-z`. Give every vertex of `S` the infinitesimal velocity

```math
u_i=R_{\pi/2}(p_i-p_z),
\tag{2.19}
```

and give every other vertex velocity zero. Every bar internal to `S` undergoes an infinitesimal rigid rotation, and every bar from `S` to `z` has zero first derivative because its velocity is perpendicular to the bar. There are no other bars leaving `S`. This is a nonzero infinitesimal flex. It is not a global Euclidean infinitesimal motion because it fixes `z` and any vertex in another component. This contradicts (2.16). Hence `J` has no cut vertex.

Now suppose `{a,b}` is a two-vertex separator. Let `L` be the line through `p_a,p_b`, and let `S` be any component of `J-{a,b}`. The vertices of `S` cannot all lie on `L`. If they did, translate every vertex of `S` by the same nonzero vector perpendicular to `L` and keep all other velocities zero. Internal bars have zero relative velocity, and every bar from `S` to `a` or `b` lies on `L` and therefore has zero first derivative. This again gives a non-Euclidean infinitesimal flex, contradicting (2.16).

Thus every component of `J-{a,b}` contains a point off `L`. Choose two components `S_1,S_2`. Embed the original realization in `R^3`. Rotate all vertices of `S_1` through an angle, say `pi/2`, about the axis `L`, while fixing `a,b` and every vertex outside `S_1`. Every bar length is preserved: the only bars leaving `S_1` end at `a` or `b`, both on the rotation axis. Hence this is a bar-equivalent realization.

It is not congruent to the original. The component `S_2` contains a point `x` off `L` and remains fixed. Any Euclidean isometry taking the original labeled realization to the new one would fix the three noncollinear points `p_a,p_b,p_x`; therefore it fixes their original plane pointwise. But `S_1` contains a point off `L`, and the chosen rotation sends that point out of the original plane. This contradicts universal rigidity. Hence no two-vertex separator exists, proving that `J` is 3-vertex-connected.

### Proof of the bridge-matching conclusion

Let `e=uv` be a bridge of the contact graph `C`, with components `X,Y` of `C-e` and `u in X`, `v in Y`. Every mixed edge crossing `X|Y` is either the contact bridge `uv` or an active diameter edge.

If `X={u}` is a singleton, then `u` has contact degree one. A 3-connected graph has minimum degree at least three, so `u` is incident to at least two diameter edges, both crossing `X|Y`. The same argument applies if `Y` is a singleton.

Assume now `|X|,|Y|>=2`. Suppose the crossing diameter graph contains no two vertex-disjoint edges. Because it is bipartite across `X|Y`, all of its edges have a common endpoint `z`: choose one crossing edge; if there were both an edge using only its `X` endpoint and another using only its `Y` endpoint, those two would be vertex-disjoint.

If there are no crossing diameter edges at all, deleting `u` and `v` disconnects the nonempty sets `X\{u}` and `Y\{v}`, contradicting 3-connectivity.

Otherwise let `z` be the common endpoint. If `z in X`, delete `z` and `v`; if `z in Y`, delete `z` and `u`. The contact bridge is removed, every crossing diameter edge is removed through `z`, and both sides retain at least one vertex. The remaining mixed graph is disconnected, again contradicting 3-connectivity. Therefore the crossing diameter graph has a matching of size at least two.

This proves every part of Theorem ZK. QED.

### Scope

The theorem concerns the **nonisolated core of the actual lexicographically normalized global source**. It does not rigidify contact-isolated source points. It uses exact bar lengths and exact PSD/nullity conclusions, not a limiting spectral gap.

Universal rigidity here is stronger than what the Level I problem directly asks: the comparison realization need not itself be a feasible packing or a global minimizer. The conclusion follows because the same signed PSD stress has zero energy on every realization preserving the active contact and diameter bar lengths.

### Dependencies

The proof uses:

- [`../targets/target-c/56-ci-restored-frontier.md`](../targets/target-c/56-ci-restored-frontier.md): promoted PSD, finite integration, and the lexicographic `C=C_*`, `H=H_*` normal form;
- [`campaign_zero_transfer_and_narrow_paths_2026-09-09.md`](campaign_zero_transfer_and_narrow_paths_2026-09-09.md): Theorem Z, ZC, ZR, and ZF;
- [`campaign_zero_transfer_defect_review_2026-09-09.md`](campaign_zero_transfer_defect_review_2026-09-09.md): adversarial review accepting Z/ZC/ZR/ZF under their stated dependencies;
- [`target_c_psd_response_cut_domination_2026-08-31.md`](target_c_psd_response_cut_domination_2026-08-31.md): the Schur congruence and C64 cut-energy notation;
- the canonical diameter-thrackle property and C34 terminal lower bound already used in ZC/ZF.

No external rigidity theorem is imported. In particular, the universal-rigidity and 3-connectivity conclusions are proved directly, so no generic-position hypothesis is being smuggled in.

### Why it is new

The repository search at the run base contains no statement of universal rigidity, redundant rigidity, or 3-vertex-connectivity for the lexicographic mixed active graph. C64 proves only non-strict cut domination and then shows that at least `2q/5` terminals have strict singleton excess. ZR supplies the missing exact kernel information. ZK upgrades C64 to strict domination on **every** proper terminal cut and to strict local excess at **every** loaded terminal.

The bridge stack previously warned that a bridge cut need not be a diameter star and retained crossing matchings as a regression. ZK now proves the complementary exact statement: a single crossing diameter edge is impossible on every bridge, and a star-supported crossing set is impossible whenever both contact sides are nonsingleton. The surviving bridge obstruction is necessarily a genuine matching/caterpillar geometry.

## 3. Exact target implication

ZK changes two live C-II subfrontiers exactly.

### 3.1 Response equality is eliminated after ZR

C64 defines

```math
Z=\{b:d_b=s_b\},
\qquad T=B\setminus Z,
```

and proves only

```math
|T|\ge\frac25|B|.
```

Under ZR, ZK gives

```math
\boxed{Z=\varnothing,\qquad T=B.}
\tag{3.1}
```

More strongly, every proper terminal cut has positive defect energy. Exact equality cannot survive on a large cut even if all singleton rows are individually very small.

This does **not** give a numerical lower bound on `tr M`, on any `d_b-s_b`, or on the smallest positive eigenvalue of `M`.

### 3.2 The bridge-dominant branch loses its star-only cases

For every contact bridge:

```math
\boxed{|H(X,Y)|\ge2.}
\tag{3.2}
```

If both contact sides are nonsingletons,

```math
\boxed{\nu(H(X,Y))\ge2.}
\tag{3.3}
```

Thus the macroscopic bridge-cut problem can no longer be reduced to or modeled by one diameter reaction or a single diameter star on a nontrivial side. The residual exact geometry contains two vertex-disjoint crossing diameter chords, and therefore the canonical common-cut order constraints apply to a genuine matching.

The exact face endpoint (1.3) is unchanged. ZK supplies structure with which to attack it or the bridge/response dichotomy; it is not itself the missing scalar inequality.

## 4. Exact remaining lemma

For Level I, the shortest scalar theorem remains (1.3).

Within the bridge-dominant subbranch, ZK sharpens the next theorem to the following form.

> **BM2 — macroscopic matching-cut exclusion.** For every fixed `c>0`, there is `D_c` such that no lexicographically normalized triangle-free C-II global minimizer of diameter `D>=D_c` has a contact bridge `e` satisfying
> ```math
> \alpha_e\ge cD,
> \qquad
> w_e:=\sum_{h\text{ crossing }e}\beta_h\ge c,
> ```
> where, as forced by ZK, the crossing diameter graph contains two vertex-disjoint diameter edges whenever both contact sides are nonsingletons.

C27 would then exclude bridge-dominant stress. The remaining work is genuinely metric: use the two crossing diameter chords, exact bridge resultant, circular order, C18/C41 response structure, and global packing to contradict a macroscopic bridge cut. A purely topological argument is insufficient.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Z, ZC | correct report-level inputs | The consolidated September 9 review accepts the full-terminal additive-resistance proof and the source-preserving separator contradiction. |
| ZR | correct report-level input | SVD plus Schur elimination gives the exact three-dimensional affine kernel on the nonisolated core. |
| ZF | correct report-level input | Promoted finite integration plus lexicographic minimality and ZR give mixed infinitesimal rigidity and `e+h>=2v-2`. |
| ZK1-ZK3 | proved | Direct Schur-nullity and affine-kernel argument. |
| Universal rigidity | proved | Exact PSD energy forces every bar-equivalent realization into the affine kernel; three diameter directions force an isometry. |
| Redundant infinitesimal rigidity | proved | The relative-interior KKT dependence has nonzero coefficient on every active row. |
| 3-vertex-connectivity | proved | One-cuts give infinitesimal rotations; two-cuts give a higher-dimensional hinge after collinear components are excluded by infinitesimal rigidity. |
| Bridge matching | proved | 3-connectivity excludes one-edge crossing support and one-vertex covers on nonsingleton bridge cuts. |
| Uniform strict response gap | not proved | Exact kernel gives strict positivity but no spectral lower bound. |
| Global face inequality | still open | ZK does not control exceptional-face currency or the invisible source population. |

## 6. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Two-edge crossing square | yes | The Z/ZR chain used here requires the large C-II regime; the two-edge square is exactly the small-support obstruction to Z. |
| Regular odd shells | yes | They omit the global-optimality hypothesis for large size. They can remain rigid and still violate the global-free face inequality; ZK does not claim otherwise. |
| Unit heptagon plus isolated center | yes | ZK is explicitly a theorem about the nonisolated core and makes no claim that isolates are diametral or rigid. |
| Near-star circular-planar networks | yes | ZK permits every cut defect to be positive while tending to zero. No conductance floor or spectral gap is claimed. |
| Crossing diameter matchings | yes | They are not excluded. They are exactly the residual bridge geometry after the star-only cases are removed. |
| Degree-five near-opposite-ray patches | yes | These local examples lack the global lexicographic KKT/ZR hypotheses. ZK makes no degree-four claim. |
| Disk-clipped oblique grids | yes | They lack exact global optimality and the full ZR normal form. |
| Pure strict-rhombic disk | yes | The separate ZB contradiction already excludes the large pure class under the same report-level dependencies; ZK is compatible with that result. |

## 7. Failed routes and no-go results

### Strict cut positivity -> quantitative trace gap

This implication is not available. A PSD matrix can have the exact affine kernel while its positive eigenvalues tend to zero. ZK removes exact equality but does not repair the near-star quantitative regression. Any use of ZK in the response branch must add unit-contact geometry, KKT force transport, or a global packing estimate.

### Three-connectivity -> no contact bridges

False as a graph-theoretic implication. A bridge of the contact graph can be repaired in the mixed graph by diameter bars. ZK proves only the exact repair cost: at least two crossing diameter bars, with a two-edge matching on nonsingleton sides.

### Universal rigidity of the core -> control of isolated source points

Invalid. Isolated source coordinates are absent from the rank-`v-3` core stress matrix. The theorem supplies no bound on `n-v` and does not revive the rejected force-bulk/FB4 localization argument.

### Redundant rigidity -> closing row count

Redundant rigidity is compatible with the extremal row count `e+h=2v-2`; a single full-support self-stress can make every row redundant. It therefore does not strengthen ZF to the desired opposite inequality by matroid theory alone.

## 8. Literature imported

No external theorem is used in ZK. The September 9 Gorbounov–Kazakov update remains relevant only to the upstream circular-planar Kalmanson dependency. It does not prove ZR, ZK, or the Level I result.

A current-status web check found no new public settlement of Erdős Problem #99 matching the global-minimizer quantifiers. No search result is used as a proof dependency.

## 9. Computation and reproducibility

No computation is required. Every new statement is finite and exact.

The relevant earlier exact computational audits remain those recorded in the September 9 campaign review for the Z interval signs, Z small-support regressions, and C53 orientation normalization. ZK introduces no new finite enumeration claim.

## 10. Canonical promotion recommendation

**Hold as report.**

The proof of ZK is complete relative to ZR/ZF, but ZR and ZF themselves remain report-level results rather than explicitly promoted Target C theorems. Promoting ZK ahead of its dependencies would invert the repository authority hierarchy.

If Z/ZC/ZR/ZF are promoted after a separate synthesis audit, then update:

1. `docs/targets/target-c/README.md` — add the exact affine terminal kernel, all-cut strictness, universal/redundant rigidity, 3-connectivity, and bridge-matching consequences;
2. `docs/targets/target-c/02-fully-visible-bridge-frontier.md` — replace star/single-edge bridge-cut cases by the ZK matching constraint;
3. the C64 response frontier or a short audited addendum — strengthen `|T|>=2|B|/5` to `T=B` under ZR;
4. `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md` — point the next bridge run at BM2 and retain the quantitative near-star warning.

Do not modify the canonical route map merely because this report is committed.

## 11. Next run

The highest-value next theorem is BM2. The most concrete route is to combine:

1. the ZK-mandated pair of vertex-disjoint crossing diameter chords on a nonsingleton bridge cut;
2. the exact bridge equilibrium/resultant relation and reciprocal diagonal;
3. C41/C64 response-cut domination, now strict on the same terminal shore;
4. the diameter-thrackle cyclic order and the global unit-packing/Oler shell bounds.

The alternative high-value route is quantitative response: use the fact that **every** loaded terminal and every proper terminal cut is strict, together with the `q=Omega(D)` scale and C43 short-pair geometry, to prove a source-specific lower bound on aggregate defect. A topology-only lower bound remains ruled out by the near-star regression.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem (ZK), conditional only on the audited ZR/ZF report-level chain:
- ker(Lambda-L_H)=span{1,Px,Py} on B, rank q-3;
- every nontrivial terminal cut has strict response excess;
- in particular every loaded terminal has d_b>s_b, so C64's zero-excess set is empty;
- the mixed contact/diameter core is universally rigid in every Euclidean dimension;
- every active bar is redundantly infinitesimally rigid;
- the mixed active graph is 3-vertex-connected;
- every contact bridge is crossed by at least two diameter edges;
- if both bridge sides are nonsingletons, two crossing diameter edges are vertex-disjoint.

Exact Level I endpoint remains:
  b + sum_F(deg F - 4) > 2h.

Exact bridge endpoint after ZK:
  BM2 = exclude a contact bridge with alpha_e >= cD and crossing beta mass >= c,
  now knowing a nonsingleton cut contains a genuine two-edge diameter matching.

Binding regressions:
- no spectral gap follows from exact kernel;
- crossing matchings remain possible;
- isolates remain outside the core stress;
- regular shells show rigidity alone cannot prove the global face inequality.

Promotion status:
Hold as report until Z/ZC/ZR/ZF are explicitly promoted.

Authoritative inputs:
- docs/targets/target-c/56-ci-restored-frontier.md
- docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md
- docs/reports/campaign_zero_transfer_defect_review_2026-09-09.md
- docs/reports/target_c_psd_response_cut_domination_2026-08-31.md
```
