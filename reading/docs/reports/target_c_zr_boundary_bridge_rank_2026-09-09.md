> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_boundary_bridge_rank_2026-09-09.md) · source SHA-256 `1fdd6873f30f9c61e38b2a741795bc9053567ccc12fce0a416cde570b80f6c6b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-42E91C06A863","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZR bridge response and body-bar rank

**Date:** 2026-09-09  
**Repository state:** branch `sol/2026-09-09-zr-kernel-consequences`; reconciled against concurrent main commit `a8efd00fa7fca0c4a20911e86efd46cb0aadeb9c`  
**Run type:** closing-proof continuation / exact structural audit  
**Target:** Target C, Gate C-II  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`, with the run-specific C–Z instructions supplied separately  
**External web search:** no theorem imported  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

This report continues
[`target_c_zr_full_kernel_rigidity_2026-09-09.md`](target_c_zr_full_kernel_rigidity_2026-09-09.md), which proves, relative to the audited report-level ZR/ZF chain, exact terminal Schur nullity, strict response domination on every proper terminal cut, universal rigidity, redundant infinitesimal rigidity, and 3-vertex-connectivity of the mixed active core.

During this run `main` advanced by
[`target_c_zf_boundary_surplus_collapse_2026-09-09.md`](target_c_zf_boundary_surplus_collapse_2026-09-09.md). That concurrent report independently records

```math
q\ge h\ge\delta\ge\lceil D\rceil
\tag{0.1}
```

and the C18 linear off-star support consequence. Those statements are therefore treated here as report-level inputs, not as new claims of this branch.

The genuinely new result below concerns **contact bridges**. A physical contact bridge has rank-one terminal transfer. Under the ZR/ZF rigidity package its crossing diameter bars must simultaneously have enough geometry to constrain the relative rigid motion of the two contact sides. The resulting bridge theorem is:

- rank-one electrical transfer across the bridge;
- strict electrical/mechanical cut sandwich
  
  ```math
  w_e<C_e\le\alpha_e\le Dw_e;
  ```

- at least two nonparallel crossing diameter bars for a singleton side;
- full three-dimensional relative body-bar rank, hence at least three nonconcurrent crossing diameter bars, when both sides are nonsingleton.

No lower bound on the individual `beta` weights of the mechanically necessary extra bars is obtained. That quantitative gap remains the decisive obstruction in the bridge-dominant branch.

## 1. Setup

Work with a sufficiently large triangle-free global minimizer in the lexicographic C-II normal form: first minimize the number of contacts, then minimize the number of diameter pairs. Let

- `V` be the nonisolated contact core;
- `C` be its complete unit-contact set;
- `H` be the actual active diameter-pair set;
- `B=V(H)=B_+` be the loaded terminal set;
- `alpha_e>0` for every `e in C` and `beta_h>0` for every `h in H` be a relative-interior normalized KKT stress.

Use the audited ZR/ZF conclusions and the preceding ZK report:

```math
\Omega=L_C(\alpha)-L_H(\beta)\succeq0,
\qquad
\ker\Omega=\operatorname{span}\{\mathbf1,P_x,P_y\},
\tag{1.1}
```

and the mixed active bar framework

```math
J=(V,C\cup H)
\tag{1.2}
```

is redundantly infinitesimally rigid. In addition, if `Lambda` is the positive-contact Dirichlet response on `B`, then

```math
M=\Lambda-L_H(\beta)\succeq0
\tag{1.3}
```

has exact affine kernel, so every nonempty proper terminal cut has **strict** response excess.

Let `e=uv` be a bridge of the contact graph. Removing it gives contact components `X,Y`, with `u in X`, `v in Y`. C20 gives nonempty complementary cyclic terminal intervals

```math
B_X=B\cap X,
\qquad
B_Y=B\cap Y.
\tag{1.4}
```

Define the active diameter edges crossing the bridge cut and their total KKT weight by

```math
H_e=\{xy\in H:x\in X,\ y\in Y\},
\qquad
w_e=\sum_{h\in H_e}\beta_h.
\tag{1.5}
```

Write

```math
c_{bk}:=-\Lambda_{bk}\ge0
\qquad(b\ne k)
\tag{1.6}
```

and define total response conductance across the same terminal shore by

```math
C_e=
\sum_{b\in B_X,\ k\in B_Y}c_{bk}.
\tag{1.7}
```

## 2. Strongest genuinely new audited theorem

### Theorem ZBR — bridge transfer and relative body-bar rank

Under the preceding hypotheses:

1. **Rank-one electrical transfer.**
   
   ```math
   \boxed{\operatorname{rank}\Lambda_{B_X,B_Y}=1.}
   \tag{ZBR1}
   ```

   Equivalently, the nonnegative cross-conductance block factors as
   
   ```math
   c_{bk}=\kappa x_b y_k
   \qquad
   (b\in B_X,\ k\in B_Y)
   \tag{2.1}
   ```

   for nonnegative vectors `x,y` and some `kappa>0`.

2. **Exact bridge sandwich.**
   
   ```math
   \boxed{
   w_e<C_e\le\alpha_e\le Dw_e.
   }
   \tag{ZBR2}
   ```


3. **Singleton bridge side.** If one contact side is a singleton, then at least two active diameter bars cross the bridge cut, and their directions are nonparallel.

4. **Nonsingleton bridge body-bar rank.** If `|X|,|Y|>=2`, orient every `h=x_hy_h in H_e` from `X` to `Y`, put `r_h=x_h-y_h`, and associate the relative-body constraint row
   
   ```math
   \ell_h=
   \bigl(r_{h,x},r_{h,y},r_h\cdot Jx_h\bigr)
   \in\mathbb R^3.
   \tag{2.2}
   ```

   Then
   
   ```math
   \boxed{
   \operatorname{rank}\{\ell_h:h\in H_e\}=3.
   }
   \tag{ZBR3}
   ```

   Consequently:
   - `|H_e|>=3`;
   - some three crossing diameter supporting lines are not concurrent and are not all parallel;
   - `H_e` contains a matching of size at least two.

### Proof of ZBR1

Delete the bridge `uv`. The positive contact network splits into two subnetworks on `X` and `Y`, joined by one scalar-current channel, the bridge.

Fix terminal voltages on `B_X` and `B_Y`. Any effect of the `Y`-shore voltages on terminal currents in `B_X` must pass through the single bridge current. By linearity, the induced current vector on `B_X` is a fixed vector times that scalar current, and the scalar bridge current is a linear functional of the `B_Y` voltages. Hence the cross map from `B_Y` voltages to `B_X` currents is an outer product and has rank at most one.

The cross map is nonzero. Both terminal shores are nonempty by C20, and the positive contact network is connected through `uv`; assigning constant potential one to `B_X` and zero to `B_Y` produces nonzero bridge current. Thus the cross block has rank exactly one.

Because every off-diagonal response entry is nonpositive, the cross-conductance matrix `(-Lambda_bk)` is entrywise nonnegative. A nonzero rank-one nonnegative matrix admits the factorization (2.1) after choosing the signs of its factors consistently.

For an explicit Schur calculation, if neither bridge endpoint is retained as a terminal, Kron-reduce each contact side to `B_X union {u}` and `B_Y union {v}`. Write the port coupling vectors as `a,b` and the port diagonal terms as `d_X,d_Y`. The two-port matrix has the form

```math
\begin{pmatrix}
A_X&0&-a&0\\
0&A_Y&0&-b\\
-a^T&0&d_X+\alpha_e&-\alpha_e\\
0&-b^T&-\alpha_e&d_Y+\alpha_e
\end{pmatrix}.
\tag{2.3}
```

Eliminating the two ports produces a cross block proportional to `-a b^T`. If one or both ports are themselves terminals, the same calculation degenerates to an outer product with the corresponding coordinate vector. This proves ZBR1.

### Proof of ZBR2

Apply ZK strict cut domination to the proper terminal cut `B_X|B_Y`:

```math
C_e>w_e.
\tag{2.4}
```

For the electrical upper bound, prescribe boundary potential one on `B_X` and zero on `B_Y`. Its response energy is exactly `C_e`. The harmonic extension minimizes contact-network Dirichlet energy. As a competitor, put potential one on every vertex of `X` and zero on every vertex of `Y`. Every contact edge has zero drop except `uv`, whose drop is one. Hence

```math
C_e\le\alpha_e.
\tag{2.5}
```

Finally sum KKT equilibrium over all vertices of `X`. Internal contact and diameter forces cancel. C20's exact bridge cut law gives

```math
\alpha_e(u-v)
=
\sum_{xy\in H_e}\beta_{xy}(x-y)
\tag{2.6}
```

with a consistent shore orientation. Taking norms and using `|x-y|=D` on every active diameter edge gives

```math
\alpha_e
\le
D\sum_{h\in H_e}\beta_h
=Dw_e.
\tag{2.7}
```

Together (2.4)–(2.7) prove ZBR2.

### Proof of the singleton-side statement

Assume `X={u}`. Because `uv` is a contact bridge and `X` is a singleton, `u` has no other contact edge. Delete the contact bar `uv`. ZK redundant rigidity says the remaining mixed framework is still infinitesimally rigid.

Keep every vertex of `Y` fixed and give `u` an arbitrary velocity `t in R^2`. All bars internal to `Y` remain fixed. The only first-order constraints on `t` are

```math
(u-y)\cdot t=0
\qquad(uy\in H_e).
\tag{2.8}
```

Infinitesimal rigidity forces these linear functionals to span the two-dimensional translation space. Thus at least two active diameter bars cross the cut, and their directions are nonparallel. The argument is symmetric if `Y` is the singleton.

### Proof of ZBR3

Assume `|X|,|Y|>=2`. Delete the contact bridge bar `uv`. By ZK, `J-uv` is infinitesimally rigid.

Restrict attention to velocity fields for which `Y` is fixed while all of `X` undergoes one planar infinitesimal rigid-body motion:

```math
u_x=t+\omega Jx
\quad(x\in X),
\qquad
u_y=0
\quad(y\in Y),
\tag{2.9}
```

with parameter vector `(t_x,t_y,omega) in R^3`. Every bar internal to `X` or to `Y` is automatically preserved to first order. A crossing diameter bar `h=x_hy_h` imposes

```math
(x_h-y_h)\cdot(t+\omega Jx_h)=0,
\tag{2.10}
```

which is exactly

```math
\ell_h\cdot(t_x,t_y,\omega)=0.
\tag{2.11}
```

If the rows `ell_h` had rank at most two, a nonzero parameter triple would satisfy every crossing diameter equation. Equation (2.9) would then define an infinitesimal flex of `J-uv`.

That flex cannot be a global Euclidean infinitesimal motion. It vanishes on every point of `Y`, and `Y` contains two distinct vertices, so any planar Euclidean infinitesimal motion agreeing with it must be the zero motion. Since `X` also contains two distinct points, a nonzero parameter triple in (2.9) produces a nonzero velocity field on `X`. Contradiction. Therefore the crossing body-bar rows have rank three.

Rank three requires at least three crossing diameter bars.

The geometric meaning is exact. A nonzero relative rigid-body motion is either:

- a translation (`omega=0`), which preserves all crossing bars when their supporting lines are parallel to a common direction perpendicular to the translation; or
- a rotation about some finite point `z` (`omega ne 0`), which preserves all crossing bars when their supporting lines pass through `z`.

Thus rank three rules out both a parallel family and a concurrent family. Some three supporting lines form a nonconcurrent triple.

Finally, a bipartite crossing graph with matching number one has a one-vertex cover, hence is a star. Its supporting lines are concurrent at the star center, contradicting ZBR3. Therefore `H_e` has a matching of size at least two.

This proves Theorem ZBR. QED.

## 3. Exact Target C implication

### 3.1 A macroscopic bridge is automatically electrically and mechanically macroscopic

If

```math
\alpha_e\ge cD
\tag{3.1}
```

for fixed `c>0`, then ZBR2 gives

```math
w_e\ge c,
\qquad
C_e>c.
\tag{3.2}
```

Thus a macroscopic reciprocal bridge diagonal cannot hide behind negligible total diameter reaction or negligible total terminal transfer across the same cyclic shore.

This improves the bridge-dominant endpoint. The missing theorem is no longer to prove that a macroscopic bridge is visible. It is to show that its **rank-one** cross response and **rank-three** crossing-bar geometry cannot coexist with response defect tending to zero.

### 3.2 A nonsingleton bridge cannot be mechanically star-supported

For `|X|,|Y|>=2`, the crossing diameter support cannot consist of

- one edge;
- two edges;
- any star;
- any collection of bars whose supporting lines are concurrent;
- any parallel family.

It must contain at least three active crossing bars with full relative-body rank three and a two-edge matching.

C66 nevertheless allows the **weights** to be asymptotically star-concentrated: the extra geometrically indispensable bars may have positive `beta` tending to zero. ZBR is therefore a support theorem, not yet a weight theorem.

### 3.3 Reconciliation with the concurrent boundary-surplus report

The concurrent main report now supplies the stronger global source normal form

```math
q\ge h\ge\delta\ge\lceil D\rceil,
\qquad
\sigma_B\ge\lceil D\rceil-2,
\tag{3.3}
```

and shows that every diameter star misses `Omega(D)` active diameter edges. ZBR is complementary: when articulation is present in the contact network, it forces an exact local rank pattern on the diameter edges crossing each bridge cut.

## 4. Exact remaining lemma

The shortest Level I scalar endpoint remains

```math
\boxed{
 b+\sum_{F\text{ bounded}}(\deg F-4)>2h.
}
\tag{4.1}
```

For the bridge-dominant subbranch, the next precise theorem is:

> **BM3 — weighted nonconcurrent bridge exclusion.** For every fixed `c>0`, no sufficiently large lexicographically normalized triangle-free C-II global minimizer has a contact bridge `e` with `alpha_e>=cD` such that
> ```math
> w_e<C_e\le\alpha_e\le Dw_e,
> ```
> the cross response block has rank one, the crossing diameter body-bar rows have rank three, and the mechanically necessary nonconcurrent bars outside the dominant stress star are allowed arbitrarily small positive `beta` weights.
>
> It is enough to derive either an absolute C41 response defect, an `Omega(1/D)` defect in the relevant near-zero scaling, the global face inequality (4.1), or a strict sub-`D` competitor.

The last clause about tiny positive weights is essential. Rank and support alone do not control KKT mass.

## 5. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| `q>=h>=delta>=ceil D` | already recorded on concurrent main | `target_c_zf_boundary_surplus_collapse_2026-09-09.md`; not claimed as new here. |
| Bridge cross-response rank one | proved | A physical bridge couples the two terminal shores through one scalar current channel. |
| `w_e<C_e<=alpha_e<=Dw_e` | proved under ZK | Strict cut defect, Dirichlet principle, and C20's exact bridge resultant. |
| Singleton side requires two nonparallel diameter bars | proved | Delete the bridge bar and constrain two translational degrees of freedom. |
| Nonsingleton sides require body-bar rank three | proved | Delete the bridge bar and constrain all three relative planar rigid-body degrees of freedom. |
| Nonsingleton bridge has at least three nonconcurrent crossing bars | proved | Immediate from rank three. |
| Macroscopic bridge gives absolute response defect | not proved | Rank-one response may concentrate on near-diameter pairs; extra body-bar rows may have vanishing `beta`. |
| Macroscopic bridge is impossible | still open | BM3 remains quantitative/metric. |

## 6. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Diameter star across a nonsingleton bridge | excluded | All crossing lines concur at the star center, contradicting body-bar rank three. |
| Diameter star on a singleton bridge side | allowed | A singleton has only two translational degrees of freedom; two nonparallel star edges can pin it. |
| Three-edge concurrent fan | excluded on nonsingleton sides | It leaves a relative infinitesimal rotation about the concurrence point. |
| Crossing matching/caterpillar | allowed | Three or more nonconcurrent crossing bars can have full body-bar rank. |
| Star plus tiny nonstar structural bars | binding | Rank is qualitative; indispensable bars may have arbitrarily small positive `beta`. |
| Near-star electrical network | binding quantitatively | Rank-one cross transfer can have arbitrarily small strict defect without an additional geometric rate. |
| Contact-isolated source points | untouched | ZBR concerns the nonisolated contact core and actual bridge cut. |

## 7. Failed implications

### Body-bar rank -> KKT weight floor

False as a linear-algebra inference. Rank depends on the geometry and nonzero support of the rows, not on the positive coefficients `beta_h`. A rank-three family can have two indispensable row weights tend to zero.

### Macroscopic bridge stress -> macroscopic C41 defect

Not yet proved. ZBR2 gives macroscopic **cross response conductance** `C_e`, but the C41 defect weights response conductance by normalized squared-distance deficit. A rank-one product measure can concentrate its mass on pairs approaching diameter `D`.

### Rank-one response + rank-three mechanics -> immediate contradiction

No. The electrical cross block and mechanical body-bar matrix are different operators. Their ranks being one and three respectively are compatible unless a new quantitative theorem couples response mass to the nonconcurrent mechanical rows.

## 8. Literature imported

No new literature theorem is used. The proof is finite electrical-network Schur reduction, KKT cut balance, and planar rigidity. Hopf–Pannwitz and the circular-planar response theory remain upstream repository inputs only.

## 9. Computation and reproducibility

No computation is used. Every new statement is an exact finite consequence of the stated ZR/ZF/ZK and C20 dependencies.

## 10. Canonical promotion recommendation

**Hold as report.**

ZBR depends on report-level ZR/ZF and on the ZK report in this branch. If those dependencies are promoted after synthesis, update the bridge frontier to record:

- rank-one cross response for every physical contact bridge;
- `w<C<=alpha<=Dw`;
- two nonparallel crossing bars for singleton sides;
- rank-three, at least three nonconcurrent crossing diameter bars for nonsingleton sides;
- BM3 as the remaining weighted bridge theorem.

Do not promote BM3; it is the open endpoint.

## 11. Next run

The highest-value bridge question is the weighted near-star regime. C66 says that very small response defect forces almost all `beta` mass onto one star. ZBR says a nonsingleton bridge still requires a nonconcurrent rank-three crossing family. The exact unresolved configuration is therefore

```text
one macroscopic star-like diameter reaction across the bridge
+ geometrically indispensable nonconcurrent crossing bars with vanishing beta
+ rank-one macroscopic electrical cross response
+ strict defect on the same bridge terminal cut.
```

A successful theorem must use actual source geometry, global packing, or stress propagation to prevent the indispensable bars from becoming KKT-weight invisible. Pure rank, connectivity, and circular-planar topology do not supply that rate.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Concurrent main already records:
  q >= h >= delta >= ceil(D),
  sigma_B >= ceil(D)-2,
  and Omega(D) active diameter support outside every star.

New bridge theorem ZBR:
- every contact bridge has rank-one terminal cross response;
- for its cut, w_e < C_e <= alpha_e <= D w_e;
- singleton side: at least two nonparallel crossing diameter bars;
- nonsingleton sides: crossing body-bar rank = 3,
  hence at least three crossing diameter bars,
  a nonconcurrent triple of supporting lines,
  and a matching of size at least two.

Exact bridge obstruction BM3:
exclude a macroscopic bridge whose beta mass is nearly star-supported while the
extra rank-three bars have arbitrarily small positive beta, or derive a numerical
response defect / the global face inequality / a strict sub-D competitor.

Level I scalar endpoint remains:
  b + sum_F(deg F - 4) > 2h.
```
