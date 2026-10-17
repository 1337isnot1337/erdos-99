> Generated reading edition · [exact source](../../../../docs/research/tracks/target-c-cyclic-reinhardt-corpus-2026-10-16.md) · source SHA-256 `67ad0e3d8809295e8bd64f47423541147d2dd3ffbda77871a5a2fdf55c47005e`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source excerpt note: 4 deliberately truncated formula quotation(s) are displayed as literal text, with no reconstructed equation.

> Source formatting note: 10 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C cyclic and Reinhardt research corpus (frozen 2026-10-16)

## Status and route boundary

This is a navigation page for 28 source-main reports imported from frozen source commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`, indexes 183–210 of shard 2. Every full report remains at its original `docs/reports/` path. Twenty-one are byte-identical; seven preserve a recorded repair of literal form-feed-plus-`rac` bytes to `\frac`. Exact per-file source and destination Git hashes, result excerpts, lifecycle, and transformations are in the [central migration ledger](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) and [batch dispositions](../../../../docs/research/migration/2026-10-16/shards/02/batch-183-210/dispositions.jsonl).

**All reports remain unreviewed and noncanonical.** Their strongest conclusions assume a cyclic primitive survivor or a specified `d_H` phase. The common global bridge is still missing: derive the applicable cyclic phase and its hypotheses from every sufficiently large global minimizer, then complete a same-cardinality strict-diameter comparison or a valid finite endpoint contradiction. The q=13 S1 result is a finite nonglobal shell regression that rules out a shell-only KKT/PSD contradiction. Nothing here closes Target C-II or Level I.

The canonical theorem-state manifest remains authoritative. This route does not restore the withdrawn global inverse-phase chart or the unsupported `q=O(D^(4/5))` rate.

## Research tracks

### Arithmetic endpoint restrictions

#### 183. [Erdős Problem #99 — cyclic P1: exclude `q-2 = 3*2^k`](../../reports/target_c_cyclic_p1_three_times_power_two_exclusion_2026-09-10.md)

**Reported result and scope:** ### Theorem P3 Let 

```math
 m:=q-2=3r, \qquad r=2^k, \qquad k\ge1. 
```

 Then the cyclic P1 endpoint is impossible. Equivalently, 

```math
 \boxed{q-2=3\cdot2^k\quad\Longrightarrow\quad\text{no P1 survivor}.} 
```

 The proof does **not** require irreducibility of the Chebyshev trace polynomial. Indeed `G_m` has the elementary factor `T-1` throughout this family. Instead, two 2-adic Newton polygons separate the remaining cofactor into a large `T=1` cluster and a smaller `T=0` cluster. The P1 Littlewood reduction modulo two cannot accommodate the reciprocal lift of the smaller cluster. ---

**Next obligation recorded in the source:** No explicit remaining/next section was identified by the migration parser. Independent proof audit and the global Level-I implication remain outstanding; source lifecycle is unreviewed.

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 183).

#### 186. [Erdős Problem #99 — prime-power odd part forces periodic Reinhardt symmetry](../../reports/target_c_cyclic_prime_power_periodicity_2026-09-09.md)

**Reported result and scope:** ### Theorem PPW — block antiperiodicity Let 

```math
 \boxed{q=2^a p^b} \tag{PP.2} 
```

 with `a>=0`, `b>=1`, and `p` an odd prime. Put 

```math
 m:=q/p=2^a p^{b-1}. 
```

 Then every Littlewood closure (PP.1) has the exact form 

```math
 \boxed{ (\epsilon_0,\ldots,\epsilon_{q-1}) = (A,-A,A,-A,\ldots,A), } \tag{PP.3} 
```

 where 

```math
 A=(a_0,\ldots,a_{m-1})\in\{\pm1\}^m 
```

 is arbitrary and there are exactly `p` consecutive blocks. Equivalently, 

```math
 \boxed{ \epsilon_{j+m}=-\epsilon_j \qquad(0\le j<q-m). } \tag{PP.4} 
```

 Thus every such exact Reinhardt polygon is periodic rather than sporadic. Geometrically the shell has exact `p`-fold rotational symmetry. In particular its uniqu…

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. RS: P(zeta)=sum_{j<q} epsilon_j zeta^j=0, epsilon_j=+-1, zeta primitive 2q-th root. If q=2^a p^b with p odd prime, put m=q/p and eta=zeta^m (primitive 2p-th root). Field degrees give [Q(zeta):Q(eta)]=m, so 1,zeta,...,zeta^(m-1) are a Q(eta)-basis. Group P by residues mod m: P(zeta)=sum_r zeta^r B_r(eta). Every B_r has p coefficients +-1 and must vanish at eta. Since de…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 186).

### Exact d_H=0 Reinhardt and stress program

#### 184. [Erdős Problem #99 — the full `d_H=0` KKT family reduces to one stress variable per Reuleaux path](../../reports/target_c_cyclic_path_stress_recurrence_2026-09-09.md)

**Reported result and scope:** ### Theorem PS — exact path-stress reduction 1. Every contact on the `i`th LC path has coefficient exactly `sigma_i`. 2. Every pendant diameter edge lying between `t_i` and `t_{i+1}` has coefficient 

```math
 \boxed{\beta_h=\frac{\sigma_i}{D^2}.} \tag{PS.3} 
```

 3. If 

```math
 d_i:=\sigma_{i-1}-\sigma_i, \tag{PS.4} 
```

 then the coefficient `beta_i` of the cycle diameter edge at `t_i` is 

```math
 \boxed{ \beta_i =(1-\cos\theta)(\sigma_{i-1}+\sigma_i) -\frac{\sin\theta}{\sin\phi_i} \left( \cos\phi_i\,d_i+d_{i+1} \right). } \tag{PS.5} 
```

 4. The alternating jump sequence 

```math
 y_i:=(-1)^i d_i 
```

 satisfies the exact variable-step harmonic recurrence 

```text
 \boxed{ y_{i+2} = \…
```

**Next obligation recorded in the source:** ## 13. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Cycle diameter directions occur at positions t_i with ell_i=t_{i+1}-t_i and phi_i=ell_i*pi/q. These are exactly the LC Reuleaux composition parts. KL contact variable a_t is constant across every pendant direction position, so all ell_i shell contacts on one LC path have one common stress sigma_i>0. Every ell_i-1 pendant diameter edge in that star has beta=sigma_i/D^2.…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 184).

#### 187. [Erdős Problem #99 — Reinhardt completion traps all rattlers and forces a growing diameter core](../../reports/target_c_cyclic_reinhardt_completion_core_growth_2026-09-09.md)

**Reported result and scope:** ### Theorem RC — exact diameter completion Let `V(F)` be the force-hull vertex set. Then 

```math
 \boxed{ \bigcap_{p\in V(F)}\overline B(p,D)=R.} \tag{RC.1} 
```

 Consequently the entire source satisfies 

```math
 \boxed{A\subseteq R.} \tag{RC.2} 
```

 Every C65 rattler lies in the strict interior of `R`. If `nu` is the odd cycle length of the full diameter graph, equivalently the number of defining vertices/arcs of the Reinhardt Reuleaux polygon, then 

```math
 \boxed{ \nu^2> \frac{\pi^3D^2}{12\sqrt3(\pi D+2)}.} \tag{RC.3} 
```

 In particular 

```math
 \boxed{ \liminf\frac{\nu}{\sqrt D} \ge \frac{\pi}{\sqrt{12\sqrt3}} =0.6890947417\ldots .} \tag{RC.4} 
```

 Thus the exact cyclic…

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. RE makes F an exact Reinhardt q-gon. Let R be its width-D Reuleaux completion and S subset V(F) the defining Reuleaux vertices. Since R = intersection_{c in S} B(c,D), and R has diameter D while V(F) subset R, intersection_{p in V(F)} B(p,D) = R. Every source point is within D of every p in V(F), hence A subset R. C65 rattlers are not diameter endpoints, so they lie in…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 187).

#### 188. [Erdős Problem #99 — exact area gap between the Reinhardt completion and force hull](../../reports/target_c_cyclic_reinhardt_exact_cap_area_2026-09-09.md)

**Reported result and scope:** ### Theorem CA — exact completion-minus-hull area Let `R` be the width-`D` Reuleaux completion of the exact cyclic `d_H=0` force hull `F`. Then 

```math
 \boxed{ \operatorname{area}(R)-\operatorname{area}(F) = \frac{qD^2}{2} \left( \frac\pi q-\sin\frac\pi q \right).} \tag{CA.1} 
```

 Using 

```math
 D=\frac1{2\sin(\pi/(2q))}, 
```

 this can also be written 

```math
 \boxed{ \operatorname{area}(R)-\operatorname{area}(F) = \frac{\pi}{8\sin^2 x} \left(1-\frac{\sin x\cos x}{x}\right), \qquad x:=\frac\pi{2q}.} \tag{CA.2} 
```

 In particular, 

```math
 \boxed{ \operatorname{area}(R)-\operatorname{area}(F) = \frac\pi{12} + \frac{\pi^3}{360q^2} + \frac{\pi^5}{10080q^4} +O(q^{-6}).} \tag…
```

**Next obligation recorded in the source:** ## 9. Compact handoff ```text LEVEL I STATUS: STILL OPEN. In exact cyclic d_H=0, each of the q force-hull unit sides is a chord of a radius-D Reuleaux-completion arc with central angle delta=pi/q. The q circular caps are disjoint and exactly fill R\F. Hence area(R)-area(F) = q D^2/2 (pi/q - sin(pi/q)). With x=pi/(2q), D=1/(2sin x): = pi/[8 sin^2 x] * [1-sin x cos x/x] = pi/12 + pi^3/(360q^2)+pi^5/(10080q^4)+O(q^-6). Thus compl…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 188).

#### 189. [Erdős Problem #99 — cyclic unicyclic phase collapses to exact Reinhardt equality](../../reports/target_c_cyclic_reinhardt_exact_collapse_2026-09-09.md)

**Reported result and scope:** ### Theorem RE — exact cyclic Reinhardt collapse Let a sufficiently large cyclic primitive survivor satisfy 

```math
 d_H=0. 
```

 Then 

```math
 \boxed{ D=\frac1{2\sin(\pi/(2q))}, \qquad \delta_D:=2\arcsin\frac1{2D}=\frac\pi q.} \tag{RE.1} 
```

 Every projective diameter-direction gap is exactly `pi/q`. Moreover the DA diameter-direction polygon equals the complete difference body: 

```math
 \boxed{ P_H=F-F,} \tag{RE.2} 
```

 and this common body is the regular `2q`-gon with circumradius `D`. Consequently the force hull attains Reinhardt's sharp perimeter-diameter bound exactly: 

```math
 \boxed{ \operatorname{per}(F)=q =2q\sin\frac\pi{2q}\,D.} \tag{RE.3} 
```

 Thus the `d_H=0` cy…

**Next obligation recorded in the source:** ## 12. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Cyclic d_H=0 gives h=q and q projective diameter gaps g_i>=delta_D with sum g_i=pi, delta_D=2asin(1/(2D)); hence delta_D<=pi/q. DA lower: area(P_H) >= Psi_q(delta_D), Psi_q(delta)=((q-1)sin delta+sin((q-1)delta))/(4 sin^2(delta/2)). Psi_q is strictly decreasing on (0,pi/q]. Proof: split it as (q-1)/2 cot(delta/2) + sin((q-1)delta)/(4 sin^2(delta/2)). The first term dec…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 189).

#### 190. [Erdős Problem #99 — exact cyclic Reinhardt phase has no external force-hull population](../../reports/target_c_cyclic_reinhardt_force_bulk_closure_2026-09-09.md)

**Reported result and scope:** ### Theorem FB — force-bulk closure in the exact `d_H=0` cyclic phase Every source point lies in the force hull: 

```math
 \boxed{A\subseteq F.} \tag{FB.1} 
```

 Since `V(F) subseteq A`, this gives 

```math
 \boxed{F=\operatorname{conv}A.} \tag{FB.2} 
```

 Thus the `d_H=0` cyclic phase has **no external force-hull population at all**. All 

```math
 n-q=\Theta(D^2) 
```

 C65 rattlers are strictly inside the same polygonal force hull whose boundary is the positive unit contact cycle. This closes the force-bulk localization problem completely for this exact cyclic subphase, although it does not yet create positive KKT contacts on the rattlers. ---

**Next obligation recorded in the source:** ## 10. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Each unit Reinhardt side cuts one radius-D circular cap from the Reuleaux completion. Its maximum depth is the sagitta sigma_D=D-sqrt(D^2-1/4) =1/(8D)+1/(128D^3)+O(D^-5). Every point of R\F has dist(x,partial R)<=sigma_D. RD gives every C65 rattler dist(z,partial R)>r_D with r_D=sqrt3/2+1/(8D)+O(D^-3). Thus r_D>sigma_D and no rattler lies in R\F. Since RC gives A subse…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 190).

#### 191. [Erdős Problem #99 — cyclic endpoint: Reinhardt/polygonal-isoperimetric scale matching](../../reports/target_c_cyclic_reinhardt_polygonal_match_2026-09-09.md)

**Reported result and scope:** ### Theorem RP.1 — discrete upper deficit 

```math
 \boxed{ t_D \le \frac\pi{24D}+O(D^{-2}).} \tag{RP.4} This improves the DP bound `pi/(12D)` by a factor two. ---
```

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. DP gave t_D=pi D-q=O(1/D). Polygonal isoperimetry on F-F (<=2q sides, perimeter 2q): area(F-F) <= q/[2 tan(pi/(2q))] = q^2/pi-pi/12+O(q^-2). DA lower: area(F-F) >= pi D^2-pi/6+O(D^-1). Hence t_D <= pi/(24D)+O(D^-2). Reinhardt: per(F)=q <= 2q sin(pi/(2q)) D, so D >=1/[2sin(pi/(2q))] and t_D >= pi/(24D)+O(D^-3). Therefore pi D-q=pi/(24D)+O(D^-2) for all d_H=0,1,2. Projec…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 191).

#### 192. [Erdős Problem #99 — exact Reinhardt shell forces a uniform rattler boundary depth](../../reports/target_c_cyclic_reinhardt_rattler_depth_2026-09-09.md)

**Reported result and scope:** ### Theorem RD — exact rattler depth Put 

```math
 \delta_D:=\frac\pi q =2\arcsin\frac1{2D} 
```

 and define 

```math
 \boxed{ s_D^2 :=4D^2\sin^2\frac{\delta_D}{4} =\frac1{2\left(1+\sqrt{1-1/(4D^2)}\right)}.} \tag{RD.1} 
```

 Let `r_D` be the positive root of 

```math
 t^2+s_D^2\left(1-\frac tD\right)=1. 
```

 Equivalently, 

```math
 \boxed{ r_D = \frac12\left[ \frac{s_D^2}{D} + \sqrt{\frac{s_D^4}{D^2}+4(1-s_D^2)} \right].} \tag{RD.2} 
```

 Then every C65 contact-isolated source point `z` satisfies 

```math
 \boxed{ \operatorname{dist}(z,\partial R)>r_D.} \tag{RD.3} 
```

 Moreover 

```math
 \boxed{ r_D = \frac{\sqrt3}{2} + \frac1{8D} + \frac1{128D^3} +O(D^{-5}).} \tag{RD.4} 
```

 Thus all rattlers lie…

**Next obligation recorded in the source:** ## 10. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Exact RE shell: delta_D=pi/q=2asin(1/(2D)). Every consecutive shell pair on partial R is a unit chord on one radius-D arc. Let z be a C65 rattler and t=dist(z,partial R). If the nearest boundary point is inside a shell subarc, one endpoint p has central offset phi<=delta_D/2. With z on the inward radial normal, |z-p|^2 <= t^2+s_D^2(1-t/D), where s_D^2=4D^2 sin^2(delta_…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 192).

#### 193. [Erdős Problem #99 — cyclic Reinhardt ladder defect is bounded explicitly by `d_H`](../../reports/target_c_cyclic_reinhardt_second_order_defect_2026-09-09.md)

**Reported result and scope:** ### Theorem R2 — phase-dependent second-order ladder defect Every unbounded cyclic survivor sequence satisfies 

```math
 \boxed{ \limsup_{D\to\infty} \frac{s}{\delta^2} \le \frac{d(d+1)(d+2)}{12}.} \tag{R2.1} 
```

 Since only `d=0,1,2` occur, 

```math
 \boxed{ \begin{array}{c|c} d_H & \displaystyle\limsup D^2\bigl(q_R(D)-q\bigr)\\ \hline 0 & 0,\\[2mm] 1 & \le\frac12,\\[2mm] 2 & \le2. \end{array}} \tag{R2.2} 
```

 The `d_H=0` phase is already strengthened by RE to exact equality `s=0` for every sufficiently large survivor. The new content is the explicit constants in the two tree phases. Equivalently, if 

```math
 D_R(q):=\frac1{2\sin(\pi/(2q))}, 
```

 then 

```text
 \boxed{ \lim…
```

**Next obligation recorded in the source:** ## 10. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Let delta=2asin(1/(2D)), q_R=pi/delta, s=q_R-q>=0, d=d_H. RP gives s=O(delta^2). DA lower with h=q-d becomes exactly L=D^2[(pi/delta-s-d-1)sin(delta)+sin((s+d+1)delta)]. Expanding: L=pi/delta^2-pi/12-A_d delta+O(delta^2), A_d=d(d+1)(d+2)/6. Polygonal-isoperimetric upper: U=q/[2tan(pi/(2q))] =pi/delta^2-pi/12-2s/delta+O(delta^2). Since L<=U, 0<=A_d delta-2s/delta+O(delt…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 193).

#### 194. [Erdős Problem #99 — cyclic equality gives a Reinhardt sign equation](../../reports/target_c_cyclic_reinhardt_sign_obstruction_2026-09-09.md)

**Reported result and scope:** ### Lemma RS.1 — no parallel-side collision The `2q` vectors in (1.3) have pairwise distinct oriented directions, and they are exactly the `2q` side vectors of the regular polygon `F-F`. `\square` ---

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. CE gives in cyclic d_H=0: F-F = regular 2q-gon R_{2q} with circumradius D and side length one. F itself is a strict convex unit q-gon. Minkowski edge merging for F+(-F) has 2q unit input edges and the output R_{2q} has exactly 2q unit edges. Hence no codirected merge occurs. After rotation, if zeta=exp(pi i/q), the q side vectors of F choose exactly one member of each…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 194).

#### 195. [Erdős Problem #99 — exact Reinhardt shell has a canonical uniform KKT stress](../../reports/target_c_cyclic_reinhardt_uniform_stress_2026-09-09.md)

**Reported result and scope:** ### Theorem US — uniform full-support stress For every exact `d_H=0` cyclic survivor, the coefficients 

```math
 \boxed{ \beta_h=\frac1q \quad(h\in H), \qquad \alpha_e=\frac{D^2}{q} \quad(e\in C_q)} \tag{US.1} 
```

 satisfy KKT equilibrium at every loaded vertex. In particular they define a strictly positive normalized full-support stress. Equivalently, if `L_C` is the unweighted Laplacian of the boundary contact cycle and `L_H` the unweighted Laplacian of the full diameter graph, then the corresponding scalar stress matrix is 

```math
 \boxed{ \Omega_{\rm unif} =\frac1q\left(D^2L_C-L_H\right).} \tag{US.2} 
```

 By CY/CG this stress is PSD and maximal-rank: 

```math
 \…
```

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. RE d_H=0 geometry: delta=pi/q, D=1/(2sin(delta/2)), theta_b=deg_H(b) delta, every local diameter fan fills the normal cone with boundary gaps delta/2 and internal gaps delta. At a vertex of diameter degree d: sum of its d unit diameter directions = [sin(d delta/2)/sin(delta/2)] n_b. Equal contact coefficient A gives resultant 2A sin(d delta/2) n_b. Equal diameter coeff…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 195).

#### 196. [Erdős Problem #99 — additive Reuleaux energy controls the full Reinhardt leaf composition](../../reports/target_c_cyclic_reuleaux_aggregate_composition_energy_2026-09-09.md)

**Reported result and scope:** <!-- theorem-state: {"artifact_id":"ART-AB02ECDD6D66","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} --> # Erdős Problem #99 — additive Reuleaux energy controls the full Reinhardt leaf composition **Date:** 2026-09-09 **Run type:** exact constant-width variational inequality / composition stability **Target:** Target C cyclic `d_H=0` Reinhardt endpoint **Depends on:** LC Reuleaux leaf composition in this PR; PR #118 exact Reinhardt completion and WG finite-packing area bound **External literature:** none for the new variational inequality **Computation:…

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. For width-D Reuleaux completion R write h=D/2+p, f=(h+h'')-D/2 and L=-d^2/dtheta^2-1. Then delta_R=pi D^2/4-area(R)=1/2 <f,L^{-1}f>. On one radius-D arc interval I of length phi, f=D/2; on I+pi, f=-D/2. Solve the optimal local Dirichlet test -g''-g=1, g(0)=g(phi)=0, so g=cos x+tan(phi/2)sin x-1, C(phi)=int g=2tan(phi/2)-phi. Pair it antiperiodically. Then <f,g>=D C(phi…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 196).

#### 197. [Erdős Problem #99 — cyclic circuit Oler cancellation exposes only O(D) rhombus defect](../../reports/target_c_cyclic_rhombus_excess_transport_2026-09-10.md)

**Reported result and scope:** <!-- theorem-state: {"artifact_id":"ART-F47E8F741FC5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} --> # Erdős Problem #99 — cyclic circuit Oler cancellation exposes only O(D) rhombus defect **Date:** 2026-09-10 **Repository base:** `1adc420e9227476135d6891b61f1a75193aa90ab` plus the cyclic Reuleaux reports in this branch **Run type:** exact source-population bookkeeping / Target C-to-B bridge **Target:** post-ZF `s_Z=0`, Woodall cyclic branch `d_H=0` ## LEVEL I STATUS `STILL OPEN`. Let `R_4` be the number of bounded quadrilateral contact faces. C51 m…

**Next obligation recorded in the source:** ## Compact handoff ```text LEVEL I STATUS: STILL OPEN. In s_Z=d_H=0: b+Q=2q, m=R_4+f+q+1. Write A_4=a0 R_4+E. Exceptional-face Oler gives A_exc >= a0(Z_def+f)+c0 Q. OP.1 gives a0 Z_in <= H+c0(P_F-b). After exact cancellation using b+Q=2q and a0=2c0: a0 N_F <= area(F)+c0 P_F+a0-E. C17/CRC partition R\F into q convex Reuleaux caps. Oler on each cap, including its two loaded endpoints, gives a0 Z_ext <= area(R)-area(F)+c0(P_F+pi…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 197).

#### 198. [Erdős Problem #99 — a strict `q=13` S1 shell survives closure, positive KKT, and maximal-rank PSD stress](../../reports/target_c_cyclic_s1_q13_shell_regression_2026-09-10.md)

**Reported result and scope:** <!-- theorem-state: {"artifact_id":"ART-7A2B3FF788EF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} --> LEVEL I STATUS: STILL OPEN # Erdős Problem #99 — a strict `q=13` S1 shell survives closure, positive KKT, and maximal-rank PSD stress **Date:** 2026-09-10 **Run type:** exact algebraic shell construction plus high-precision mechanical regression check **Target:** primitive cyclic `d_H=1,s_Z=1`, S1 **Depends on:** D1/SC on PR #118; RSQ on this branch **Computation:** yes; all numerical claims below are regression/certificate data, not promoted as a so…

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Strict S1 shell regression at q=13, m=11: Q=-Z^10+Z^9-Z^8-Z^7+Z^6+Z^5+Z^4-Z^3-Z^2+Z-1, Q=Q*. RSQ amplitude reduces to P13(t)=0 with P13=t^10-2t^9-8t^8+18t^7+17t^6-52t^5+t^4+51t^3-22t^2-13t+11. Physical root: t=1.9419941305433685..., delta=0.2414300075120225..., D=4.1520639086997635..., strictly between P1 and Reinhardt boundaries. Reconstruction has exactly: 13 consecu…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 198).

#### 199. [Erdős Problem #99 — second-order rigidity of the cyclic atomic endpoint](../../reports/target_c_cyclic_second_order_pocket_rigidity_2026-09-11.md)

**Reported result and scope:** ### Theorem SPR Under (SP.1), for the subfamily $`\mathcal T_D=\{P:k_P=3\}`$, write $`\delta_P\in[0,\pi]`$ for the non-collinearity angle of the two unit contact edges of $`\Gamma_P`$: the internal path angle is $`\pi-\delta_P`$. Then 

```math
 \boxed{\sum_{P\in\mathcal T_D}\delta_P^2=o(D).} \tag{SP.7} 
```

 Moreover, fix any $`\delta_0<\pi/3`$. If the internal vertex has contact degree exactly three, if $`\alpha_{P,1},\alpha_{P,2}`$ are the positive KKT coefficients of the two path edges, and $`\gamma_P`$ is the coefficient of the unique third contact edge, then for every triangular pocket with $`\delta_P\le\delta_0`$, 

```text
 \boxed{ \gamma_P \le c(\delta…
```

**Next obligation recorded in the source:** No explicit remaining/next section was identified by the migration parser. Independent proof audit and the global Level-I implication remain outstanding; source lifecycle is unreviewed.

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 199).

#### 200. [Erdős Problem #99 — cyclic endpoint: every selected stress is generic and maximal-rank](../../reports/target_c_cyclic_selected_genericity_2026-09-09.md)

**Reported result and scope:** ### Theorem CG.1 — support-stable generic transfer For every normalized KKT stress of a sufficiently large cyclic survivor, 

```math
 \boxed{\text{C56-G holds and C56-Z is impossible}.} \tag{CG.2} In C56 notation the minimum off-diagonal transfer is strictly negative and the edge-defect kernel is exactly 
```



```math
 \operatorname{span}\{\mathbf1,t\}. \tag{1.2} ---
```

**Next obligation recorded in the source:** ## 10. Compact handoff ```text LEVEL I STATUS: STILL OPEN. CY gives for every normalized stress in the cyclic endpoint: C_s=C_q, B_s=B_+, so H_s is a diameter edge cover of all q terminals. For q>=6, H_s has at least 3 edges. Therefore Theorem Z applies to every selected stress. C56-Z would make the cycle resistance metric additive and SEPq would force a loaded contact degree >=q-1, contradicting deg_C=2. Hence every stress is…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 200).

#### 201. [Erdős Problem #99 — cyclic force hull is a locally diameter-minimal equilateral polygon](../../reports/target_c_cyclic_shell_local_optimality_2026-09-09.md)

**Reported result and scope:** ### Theorem SL — shell local diameter minimality Let 

```math
 P=(p_0,\ldots,p_{q-1}) 
```

 be the cyclically ordered force-hull vertices of a sufficiently large cyclic C65 survivor. Then `P` is a local minimizer of diameter among convex equilateral `q`-gons of side length one. More precisely, there is a neighborhood `U` of `P` in the space of labeled vertex tuples such that every convex equilateral tuple 

```math
 P'=(p'_0,\ldots,p'_{q-1})\in U, \qquad |p'_{i+1}-p'_i|=1, 
```

 satisfies 

```math
 \boxed{\operatorname{diam}\{p'_0,\ldots,p'_{q-1}\}\ge D.} \tag{SL.1} 
```

 Since the original shell has diameter `D`, equality holds at `P`.

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. UFB gives F=conv(A). CY/C-I says the only actual unit contacts are the q consecutive shell edges. C65 says each interior rattler is not a diameter endpoint. Since A is finite, all interior-shell distances have positive slack from both 1 and D, all nonadjacent shell pairs have positive slack from 1, and all inactive shell pairs have positive slack from D. Therefore fix…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 201).

#### 202. [Erdős Problem #99 — cyclic ordinary-gap audit: path inference is false, star-run saturation survives](../../reports/target_c_cyclic_star_run_audit_2026-09-09.md)

**Reported result and scope:** ### Theorem SR — star-run saturation Let `H` be a spanning diameter tree on `q` loaded shell terminals with `h=q-1`. Suppose its `q-1` actual diameter states occur in one projective linear block 

```math
 e_0,e_1,\ldots,e_{q-2} 
```

 and every consecutive projective gap is the ordinary radius-`D` unit-chord gap 

```math
 \delta=2\arcsin\frac1{2D}. 
```

 Then: 1. every consecutive pair `e_j,e_{j+1}` shares exactly one terminal; 2. for every terminal `v`, all `deg_H(v)` incident diameter edges form one contiguous interval in the projective list; 3. the `q-2` ordinary transitions are partitioned exactly among the terminal stars, with terminal `v` owning `deg_H(v)-1…

**Next obligation recorded in the source:** No explicit remaining/next section was identified by the migration parser. Independent proof audit and the global Level-I implication remain outstanding; source lifecycle is unreviewed.

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 202).

#### 207. [Erdős Problem #99 — every `d_H=0` KKT stress has asymptotically uniform shell-contact weights](../../reports/target_c_cyclic_uniform_contact_stress_2026-09-09.md)

**Reported result and scope:** <!-- theorem-state: {"artifact_id":"ART-F814C5D87563","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} --> # Erdős Problem #99 — every `d_H=0` KKT stress has asymptotically uniform shell-contact weights **Date:** 2026-09-09 **Run type:** exact finite stress-cone estimate with asymptotic consequence **Target:** Target C cyclic `d_H=0` Reinhardt endpoint **Depends on:** KL/EZ/PP in this PR; PS path-stress reduction; PR #125 AE bound `phi_max=O(D^-1/3)` **External literature:** none **Computation:** none ## LEVEL I STATUS `STILL OPEN` The normalized KKT poly…

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Signed cycle vectors satisfy r_{i+1}=-R_{phi_i}r_i, so pair cancellation gives every KL partial sum |R_t|<=1+pi. EZ beta-functional vertices are K_i=D r_i + sec(theta/2) J M_i, thus |K_i-D r_i|<=C_D=sec(theta/2)(1+pi)=O(1). In step-two convex order, r_{i+2}=R_{phi_i+phi_{i+1}}r_i. AE gives phi_max=O(D^-1/3), so conv{Dr_i} contains a centered disk of radius D cos(phi_ma…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 207).

#### 210. [Erdős Problem #99 — Wegner finite-packing upgrade in the exact cyclic Reinhardt branch](../../reports/target_c_cyclic_wegner_packing_upgrade_2026-09-09.md)

**Reported result and scope:** ### Theorem WG — exact Wegner lower bound for the force-hull area Every exact cyclic `d_H=0` survivor satisfies 

```math
 \boxed{ \operatorname{area}(F) \ge \frac{\sqrt3}{2}(n-1) -\frac q2 +\frac{2-\sqrt3}{4} \left\lceil\sqrt{12n-3}-3\right\rceil.} \tag{WG.1} 
```

 Using the strict global diameter comparison 

```math
 n>\frac\pi{2\sqrt3}D^2, 
```

 this gives the finite consequence 

```math
 \boxed{ \operatorname{area}(F) > \frac\pi4D^2 -\frac q2 -\frac{\sqrt3}{2} + rac{2-\sqrt3}{4} \left( \sqrt{2\pi\sqrt3\,D^2-3}-3 \right).} \tag{WG.2} 
```

 Since RE gives 

```math
 q=\pi D- rac\pi{24D}+O(D^{-3}) 
```

 exactly through the Reinhardt relation, the disk-area deficit satisfies 

```math
 \boxe…
```

**Next obligation recorded in the source:** ## 10. Compact handoff ```text LEVEL I STATUS: STILL OPEN. FB gives F=conv(A), per(F)=q. Scale radius-1/2 source disks by two. The convex hull of the resulting unit disks is Dcal=2F+B_1, so area(Dcal)=4 area(F)+2q+pi. Wegner gives area(Dcal)>=2sqrt3(n-1)+(2-sqrt3)ceil(sqrt(12n-3)-3)+pi. Therefore area(F)>=sqrt3/2(n-1)-q/2 +(2-sqrt3)/4 ceil(sqrt(12n-3)-3). Using n>pi D^2/(2sqrt3) and RE q=pi D+o(D): pi D^2/4-area(F) <= (C_W+o(1…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 210).

### Multi-phase topology, surplus, and capacity

#### 185. [Erdős Problem #99 — cyclic pocket complexity after the exceptional-face floor](../../reports/target_c_cyclic_pocket_complexity_2026-09-11.md)

**Reported result and scope:** ### Theorem CP — pocket degree excess is paid by loaded-loaded surplus Let a post-ZF fully force-visible source satisfy the outer-pocket identities above, and write `d_H` for the loaded diameter-graph defect and `s_Z` for the mixed-rank surplus. Then 

```math
 \boxed{ 0\le \sum_P(k_P-3) \le e_{BB}-Q-2d_H-2s_Z. } \tag{CP.1} 
```

 In particular, 

```math
 \boxed{e_{BB}\ge Q+2d_H+2s_Z.} \tag{CP.2} 
```

 In the cyclic circuit branch `s_Z=d_H=0`, let 

```math
 \nu_D=\frac{e_{BB}+2s_C}{D}. 
```

 If an unbounded sequence has `limsup nu_D <= 1`, then 

```math
 \boxed{ \liminf\frac aD \ge \frac12\left(\pi+\frac45\sqrt{\frac\pi{2\sqrt3}}\right)-1 =0.9517214495\ldots . } \tag{CP.3} 
```

 If,…

**Next obligation recorded in the source:** ## 8. Compact handoff ```text New exact synthesis (cyclic C-II): 0 <= sum_P(k_P-3) <= e_BB-Q-2d_H-2s_Z. In the cyclic circuit branch, if nu=(e_BB+2s_C)/D <= 1 along a sequence, then liminf a/D >= (pi + (4/5)sqrt(pi/(2sqrt3)))/2 - 1 = 0.9517214495... At the formal atomic endpoint nu -> lambda_A=0.99554058458..., Q/D -> lambda_A, e_BB/D -> lambda_A, sum_P(k_P-3)=o(D), so all but o(D) of the linear number of outer pockets are tri…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 185).

#### 203. [Erdős Problem #99 — cyclic surplus cap and the remaining capacity gap](../../reports/target_c_cyclic_surplus_cap_and_capacity_gap_2026-09-11.md)

**Reported result and scope:** ## 6. Classification | Statement | Classification | |---|---| | cyclic surplus cap (2.5) | proved conditional on the promoted/current post-ZF cyclic identities | | piecewise cap (3.5) | proved conditional on local attachment sparsity and planar incidence | | cyclic C-II closure | not proved | | full Erdős Problem #99 settlement | not proved | The next decisive result must charge the exceptional-face boundary or the contact-isolated population by a **quadratic** amount, or produce a source-preserving finite competitor. Boundary-order contact bookkeeping cannot close the remaining interval.

**Next obligation recorded in the source:** # Erdős Problem #99 — cyclic surplus cap and the remaining capacity gap **Date:** 2026-09-11 **Repository state:** `643a06bc28354ec06167a7b8529129640bb689ad` **Run type:** exact ledger consequence and obstruction audit **Target:** Target C, C-II, cyclic post-ZF branch **Status:** STILL OPEN; hold as an unpromoted report

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 203).

#### 204. [Erdős Problem #99 — cyclic endpoint: convex-thrackle tree cuts and reciprocal parallelograms](../../reports/target_c_cyclic_thrackle_tree_cut_2026-09-09.md)

**Reported result and scope:** ### Theorem TC — two-interval cut theorem For every edge `e` of a convex straight-line thrackle tree `T`, each connected component of 

```math
 T-e 
```

 occupies at most two cyclic intervals of the ambient convex vertex order. Applied to the cyclic Target C endpoint, if a full diameter-tree edge has zero KKT coefficient in a selected stress, summed equilibrium over either component gives zero contact-force resultant. TC reduces that condition to either two or four boundary cycle edges. The two-edge case is impossible; hence every such zeroed diameter edge forces an exact reciprocal parallelogram on four cycle-force vertices. ---

**Next obligation recorded in the source:** ## 12. Compact handoff ```text LEVEL I STATUS: STILL OPEN. TC (proved directly): Delete any edge of a straight-line thrackle tree on convex vertices. Each component occupies at most two cyclic vertex intervals. Proof core: Every A-edge crosses every B-edge. For one A-edge xy, every B-edge toggles sides of xy, so B's two tree-bipartition classes lie on opposite xy boundary arcs. Two vertices of the same B color are on the same…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 204).

#### 205. [Erdős Problem #99 — cyclic `d_H=1` zeroed edges force four-block corner cuts](../../reports/target_c_cyclic_tree_endpoint_unification_2026-09-09.md)

**Reported result and scope:** ### Theorem EU — four-block corner-cut theorem Let `H` be the full spanning diameter tree in the cyclic `d_H=1` phase. Let `s` be a KKT endpoint and let 

```math
 e=uv\in E(H),\qquad \beta_e(s)=0, 
```

 be any zeroed nonleaf full-tree edge. Put 

```math
 H-e=T_A\sqcup T_B. 
```

 Then: 1. `T_A,T_B` are nontrivial trees covering all `q` terminals; 2. their bipartition classes form four nonempty cyclic blocks, after relabeling, 

```math
 \boxed{A_0\mid B_0\mid A_1\mid B_1;} \tag{EU.1} 
```

 3. the four cycle contacts crossing the `A|B` cut satisfy the endpoint reciprocal parallelogram 

```math
 \boxed{v_i+v_k=v_j+v_\ell,\qquad v_r=\alpha_r t_r;} \tag{EU.2} 
```

 4. the zeroed actual d…

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Correction: a d_H=1 endpoint may zero more than one beta coordinate. CG proves selected scalar-stress rank q-3, not selected mixed-rigidity rank 2q-3. Do not identify the positive endpoint support with H-e or call it a rigidity circuit. What is exact: Choose any zeroed nonleaf full-tree edge e=uv. Since H is a spanning tree, H-e has two nontrivial full-tree components…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 205).

#### 206. [Erdős Problem #99 — cyclic `d_H=2` collapses to a four-block two-tree normal form](../../reports/target_c_cyclic_two_tree_four_block_normal_form_2026-09-09.md)

**Reported result and scope:** ### Theorem D2 — four alternating diameter-color blocks Let the two full diameter-tree components be `T_A,T_B`, with unique bipartitions 

```math
 A=A_0\sqcup A_1, \qquad B=B_0\sqcup B_1. 
```

 Each of the four color classes is a single nonempty cyclic interval of the convex force-hull order. After swapping color names and rotating the cyclic order, 

```math
 \boxed{ A_0\;|\;B_0\;|\;A_1\;|\;B_1 } \tag{D2.1} 
```

 are the four consecutive terminal blocks around the boundary. Thus each diameter component occupies exactly two cyclic intervals, and those intervals are precisely its two tree-bipartition classes. Moreover, if the four contact-cycle transitions occur a…

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Cyclic d_H=2: H=T_A disjoint union T_B, both nontrivial trees. Every A-edge crosses every B-edge. Write tree bipartitions A=A0+A1, B=B0+B1. For a fixed A-edge, every B-edge toggles sides, so B0/B1 lie on opposite boundary arcs. Two same-color B vertices lie on the same side of every A-edge; connectedness then shows no A vertex can split a B-color block. Thus each A0,A1…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 206).

#### 208. [Erdős Problem #99 — every cyclic force hull is uniformly constant-width to order `1/D`](../../reports/target_c_cyclic_uniform_width_collapse_2026-09-09.md)

**Reported result and scope:** ### Theorem UW — uniform width collapse Put 

```math
 \delta:=2\arcsin\frac1{2D}, \qquad q_R(D):=\frac\pi\delta, \qquad s:=q_R(D)-q\ge0, \qquad d:=d_H\in\{0,1,2\}. \tag{UW.1} 
```

 Then every directional width of the cyclic force hull satisfies the exact finite bound 

```math
 \boxed{ D\cos\left(\frac{(d+s+1)\delta}{2}\right) \le w_F(\theta) \le D \qquad(\theta\in\mathbb R/\pi\mathbb Z).} \tag{UW.2} 
```

 Equivalently the centered difference body obeys the concentric sandwich 

```math
 \boxed{ D\cos\left(\frac{(d+s+1)\delta}{2}\right)B_2 \subseteq F-F \subseteq DB_2.} \tag{UW.3} 
```

 Using R2, this yields the phase-specific asymptotics 

```text
 \boxed{ 0\le D-w_F(\theta) \le \…
```

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Let delta=2asin(1/(2D)), q_R=pi/delta, s=q_R-q, d=d_H. Actual projective diameter gaps satisfy g_i>=delta and sum pi. Since h=q-d, sum(g_i-delta)=pi-h delta=(s+d)delta. Hence G=max g_i <=(s+d+1)delta. The diameter-vector polygon P_H=conv{+/-D u_h} is a centered polygon inscribed in the radius-D circle. Its inradius is D cos(G/2). Since P_H subset F-F subset D B_2, we g…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 208).

#### 209. [Erdős Problem #99 — all cyclic phases have no external force-hull population](../../reports/target_c_cyclic_universal_force_bulk_closure_2026-09-09.md)

**Reported result and scope:** ### Theorem UFB — universal cyclic force-bulk closure For every sufficiently large cyclic primitive survivor, in any of the three phases 

```math
 d_H\in\{0,1,2\}, 
```

 the complete source lies in the force hull: 

```math
 \boxed{A\subseteq F.} \tag{UFB.1} 
```

 Since the `q` force-hull vertices are source points, 

```math
 \boxed{F=\operatorname{conv}A.} \tag{UFB.2} 
```

 Thus the cyclic endpoint has **no external force-hull rattlers in any topology phase**. All contact-isolated source points are strictly interior to the same convex equilateral `q`-gon whose boundary is the positive contact cycle. The proof compares two incompatible scales: - unit separation forces any…

**Next obligation recorded in the source:** ## 11. Compact handoff ```text LEVEL I STATUS: STILL OPEN. Suppose x is a source point outside the cyclic force hull F. Let h=dist(x,F). Because every hull side has length 1 and x is unit-separated from its endpoints: h>=sqrt(3)/2. For K=conv(F union {x}), nearest-point support geometry gives per(K)-per(F) >= 2(sqrt(D^2+h^2)-D) >= 2(sqrt(D^2+3/4)-D) = 3/(4D)+O(D^-3). K has at most q+1 vertices and diameter <=D. Reinhardt gives…

**Status:** unreviewed; no promotion. [Migration record](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl) (frozen index 209).

## Shared proof obligations

- Audit each full argument at the exact destination report hash; preserve source assumptions, constants, and quantifiers. The registry above links 28 reports to source and destination hashes and groups them by mathematical role.
- Trace report-declared PR and theorem dependencies to exact source refs and destination artifacts. These are presently prose references, not verified dependency edges.
- Prove the global-to-cyclic reduction without relying on withdrawn inverse-phase claims. Keep the `d_H=0`, `d_H=1`, and `d_H=2` endpoint conditions separate until a valid common argument joins them.
- The q=13 shell shows signed closure, strictly positive full-support KKT weights, and maximal-rank PSD stress can all coexist. Use the exact regression artifacts [`target_c_s1_q13_shell_regression.py`](../../../../research/target_c_s1_q13_shell_regression.py) and [`verify_s1_q13_kkt_endpoints.py`](../../../../research/verify_s1_q13_kkt_endpoints.py); they establish finite numerical checks only.
- A valid closure must either yield an actual same-cardinality strict-`D` competitor for every sufficiently large global minimizer or a finite contradiction whose limiting hypotheses and endpoint are proved.
