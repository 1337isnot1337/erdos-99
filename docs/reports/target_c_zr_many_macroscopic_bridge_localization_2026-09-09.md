<!-- theorem-state: {"artifact_id":"ART-1A168CA453AB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — many macroscopic bridges localize in the near-zero ZR phase

**Date:** 2026-09-09  
**Repository state:** branch `sol/2026-09-09-zr-kernel-consequences`, reconciled against main `a8efd00fa7fca0c4a20911e86efd46cb0aadeb9c`  
**Run type:** closing-proof continuation / quantitative bridge reduction  
**Target:** Target C, Gate C-II bridge-dominant and near-zero response intersection  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`, with the run-specific C–Z instructions supplied separately  
**External web search:** no theorem imported  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The existing C27 bridge theorem extracts one macroscopic bridge from bridge-dominant contact stress. The new ZBR report proves that every physical contact bridge has rank-one terminal transfer and that a nonsingleton bridge cut requires a rank-three, nonconcurrent family of crossing diameter bars.

This note strengthens the bridge-dominant reduction in the C66 near-zero response phase:

1. bridge-dominant stress actually forces **linearly many** macroscopic contact bridges;
2. for any bridge, the KKT diameter mass not incident to a chosen diameter vertex controls the distance from that vertex to the bridge's supporting line by an exact torque inequality;
3. at the C66 stress-star center, all of the linearly many macroscopic bridge lines pass within `o(D)` of that center when `D epsilon -> 0`;
4. C68 radialization then forces all but `o(D)` of those macroscopic bridges to make arbitrarily close to unit radial progress from the same center.

Thus the bridge-dominant near-zero survivor is no longer “one macroscopic cut plus an arbitrary bridge tree.” It is a linear family of `Theta(D)`-stress bridge edges whose geometry is asymptotically radial around the mechanical stress-star center.

This still does not yield a contradiction. A two-dimensional source can in principle carry geometrically essential branches with very small KKT weight while most contact stress runs along radial bridge chains.

## 1. Inputs and notation

Work in the lexicographically normalized C-II source with a relative-interior stress. Normalize

\[
\sum_{h\in H}\beta_h=1,
\qquad
\sum_{e\in C}\alpha_e=D^2.
\tag{1.1}
\]

Let

\[
S_{\rm br}:=\sum_{e\text{ bridge of }C}\alpha_e.
\tag{1.2}
\]

C27 gives two exact inputs:

- the bridge-block tree has at most
  \[
  m_{\rm br}\le2|B_+|-3\le2\pi D-3
  \tag{1.3}
  \]
  contact bridges;
- every bridge `e` satisfies
  \[
  \alpha_e\le Dw_e\le D,
  \tag{1.4}
  \]
  where `w_e` is the total active diameter weight crossing its cut.

Let

\[
\varepsilon=rac12\operatorname{tr}(\Lambda-L_H)
\tag{1.5}
\]

be the C41/C66 response defect. C66 supplies a diameter vertex `z` such that

\[
S_z:=\sum_{h\ni z}\beta_h
\ge1-C_0D\varepsilon,
\qquad
C_0=\frac{2\pi}{\kappa_0},
\tag{1.6}
\]

with the canonical constant `kappa_0>0`. Put

\[
\tau_z:=1-S_z
=\sum_{h\not\ni z}\beta_h.
\tag{1.7}
\]

Thus

\[
\tau_z\le C_0D\varepsilon.
\tag{1.8}
\]

C68, for the same center `z`, defines

\[
r_i:=|p_i-z|
\tag{1.9}
\]

and the contact radial defect

\[
Q_z:=
\sum_{ij\in C}\alpha_{ij}
\left[1-(r_i-r_j)^2\right]
\ge0.
\tag{1.10}
\]

It proves

\[
Q_z\le C_0D^3\varepsilon.
\tag{1.11}
\]

## 2. Strongest genuinely new audited theorem

### Theorem ZBL — linear macroscopic bridge localization

Fix `eta in (0,1]` and suppose

\[
S_{\rm br}\ge\eta D^2.
\tag{ZBL0}
\]

Put

\[
c_\eta:=\frac{\eta}{4\pi}
\tag{2.1}
\]

and call a contact bridge **eta-heavy** when

\[
\alpha_e\ge c_\eta D.
\tag{2.2}
\]

Then:

1. **Linearly many heavy bridges.** If `N_eta` is the number of eta-heavy bridges,
   \[
   \boxed{
   N_\eta
   \ge
   \eta D-c_\eta(2\pi D-3)
   =
   \frac{\eta}{2}D+rac{3\eta}{4\pi}.
   }
   \tag{ZBL1}
   \]
   In particular `N_eta>=eta D/2`.

2. **Exact torque localization for every bridge.** Let `e=uv` be any contact bridge and let `H_e` be its crossing active diameter edges. For any diameter vertex `z`, define the crossing mass not incident to `z` by
   \[
   \tau_e(z):=
   \sum_{\substack{h\in H_e\\z\notin V(h)}}\beta_h.
   \tag{2.3}
   \]
   If `ell_e` is the infinite line through `u,v`, then
   \[
   \boxed{
   \alpha_e\,\operatorname{dist}(z,\ell_e)
   \le
   D^2\tau_e(z).
   }
   \tag{ZBL2}
   \]

3. **Near-zero stress-star localization.** For the C66 center `z`, every eta-heavy bridge satisfies
   \[
   \boxed{
   \frac{\operatorname{dist}(z,\ell_e)}D
   \le
   \frac{\tau_z}{c_\eta}
   \le
   \frac{4\pi C_0}{\eta}\,D\varepsilon.
   }
   \tag{ZBL3}
   \]
   Hence if `D epsilon -> 0`, all eta-heavy bridge lines pass within `o(D)` of the same point `z`.

4. **Near-unit radial progress on almost every heavy bridge.** Fix `xi in (0,1)`. Let `N_{eta,xi}^{bad}` count eta-heavy bridges `uv` satisfying
   \[
   |r_u-r_v|\le1-\xi.
   \tag{2.4}
   \]
   Then
   \[
   \boxed{
   N_{\eta,\xi}^{bad}
   \le
   \frac{Q_z}{c_\eta D\,\xi(2-\xi)}
   \le
   \frac{C_0}{c_\eta\xi(2-\xi)}D^2\varepsilon.
   }
   \tag{ZBL4}
   \]
   Therefore, if `D epsilon -> 0`,
   \[
   N_{\eta,\xi}^{bad}=o(D),
   \tag{2.5}
   \]
   while `N_eta>=eta D/2`. For every fixed `xi>0`, all but `o(D)` of the linearly many eta-heavy bridges satisfy
   \[
   |r_u-r_v|>1-\xi.
   \tag{2.6}
   \]

### Proof of ZBL1

Let `m=m_br` be the total number of contact bridges and `N=N_eta`. By C27,

\[
m\le2\pi D-3
\tag{2.7}
\]

and every bridge has `alpha_e<=D`. Every bridge outside the eta-heavy set has `alpha_e<c_eta D`. Therefore

\[
S_{\rm br}
\le
ND+(m-N)c_\eta D
\le
ND+mc_\eta D.
\tag{2.8}
\]

Using `S_br>=eta D^2` and (2.7),

\[
N
\ge
\eta D-c_\eta m
\ge
\eta D-c_\eta(2\pi D-3).
\]

Substitute `c_eta=eta/(4pi)` to obtain ZBL1. QED.

### Proof of ZBL2

Orient the bridge cut so the contact side `X` contains `u` and the other side `Y` contains `v`. Orient each crossing diameter edge `h=xy` with `x in X`, `y in Y`, and regard

\[
f_h:=\beta_h(x-y)
\tag{2.9}
\]

as the force on the `X` side. Its magnitude is `beta_h D` and its line of action is the diameter line `xy`.

Summing equilibrium over `X` gives the C20 bridge resultant

\[
F_e:=\sum_{h\in H_e}f_h
=\alpha_e(u-v).
\tag{2.10}
\]

C20.13 gives the accompanying exact moment statement: the resultant line of action passes through `u`. Therefore the total moment of the crossing diameter-force system about an arbitrary point `z` is

\[
M_z=(u-z)\times F_e.
\tag{2.11}
\]

If a crossing diameter edge `h` is incident to `z`, its individual force line passes through `z`, so its moment about `z` is zero. Hence only crossing edges not incident to `z` contribute to `M_z`.

For such an edge `h=xy`,

\[
|(x-z)\times f_h|
\le
|x-z|\,|f_h|
\le
D\cdot(\beta_h D)
=\beta_hD^2,
\tag{2.12}
\]

because every two source points are at distance at most `D`. Summing gives

\[
|M_z|
\le
D^2\tau_e(z).
\tag{2.13}
\]

On the other hand, by (2.10)–(2.11),

\[
|M_z|
=
\alpha_e\operatorname{dist}(z,\ell_e),
\tag{2.14}
\]

because `|u-v|=1`. Combining (2.13) and (2.14) proves ZBL2. QED.

### Proof of ZBL3

At the C66 center `z`, every crossing non-`z` diameter edge is part of the global non-star tail, so

\[
\tau_e(z)\le\tau_z.
\tag{2.15}
\]

If `e` is eta-heavy, `alpha_e>=c_eta D`. Apply ZBL2:

\[
\frac{\operatorname{dist}(z,\ell_e)}D
\le
\frac{\tau_e(z)}{c_\eta}
\le
\frac{\tau_z}{c_\eta}.
\tag{2.16}
\]

Insert C66's `tau_z<=C_0D epsilon` and `c_eta=eta/(4pi)` to obtain ZBL3. If `D epsilon->0`, the right side tends to zero. QED.

### Proof of ZBL4

For any unit contact `uv`, C68's radial-defect summand is

\[
\alpha_e\left[1-(r_u-r_v)^2\right].
\tag{2.17}
\]

If `|r_u-r_v|<=1-xi`, then

\[
1-(r_u-r_v)^2
\ge
1-(1-\xi)^2
=\xi(2-\xi).
\tag{2.18}
\]

Every eta-heavy bad bridge therefore contributes at least

\[
c_\eta D\,\xi(2-\xi)
\tag{2.19}
\]

to `Q_z`. Since all contact contributions to `Q_z` are nonnegative,

\[
N_{\eta,\xi}^{bad}
\,c_\eta D\,\xi(2-\xi)
\le Q_z.
\tag{2.20}
\]

This proves the first inequality in ZBL4. Insert C68's `Q_z<=C_0D^3 epsilon` for the second. Finally

\[
D^2\varepsilon=D(D\varepsilon)=o(D)
\]

when `D epsilon->0`, giving (2.5). QED.

## 3. Interaction with ZBR body-bar rank

For a nonsingleton bridge cut, ZBR requires the crossing diameter bars to have relative body-bar rank three. In particular they cannot all be incident to the C66 star center `z`; at least one crossing bar has a line not through `z`. ZBL2 quantifies the only way this can coexist with a macroscopic bridge whose `beta` mass is nearly star-supported:

\[
\operatorname{dist}(z,\ell_e)
\le
D^2\tau_e(z)/\alpha_e.
\tag{3.1}
\]

Thus the mechanically indispensable nonconcurrent bars can rotate the resultant line away from `z` only in proportion to their **aggregate weight times the diameter lever arm**. If their total weight tends to zero, every macroscopic bridge line is forced macroscopically through the stress-star center.

This is a quantitative bridge between the support theorem ZBR and the weight-concentration theorem C66. It still allows an `o(1)` tail to exert `o(D^2)` torque, which can move a `Theta(D)` bridge resultant by an `o(D)` transverse distance.

## 4. Exact Target C implication

Assume simultaneously

\[
S_{\rm br}\ge\eta D^2
\qquad\text{and}\qquad
D\varepsilon\to0.
\tag{4.1}
\]

Then, for fixed `eta>0`, the source contains at least

\[
(\eta/2+o(1))D
\tag{4.2}
\]

distinct contact bridges with all of the following properties:

1. `alpha_e>=eta D/(4pi)`;
2. `w_e>=eta/(4pi)` by `alpha_e<=Dw_e`;
3. their supporting lines pass at distance `o(D)` from the single C66 star center `z`;
4. for every fixed `xi>0`, all but `o(D)` satisfy `|r_u-r_v|>1-xi`;
5. if both contact sides are nonsingleton, their crossing diameter support has ZBR body-bar rank three and contains a nonconcurrent triple.

The bridge-dominant near-zero phase is therefore a **macroscopic radial bridge forest with low-weight transverse diameter corrections**.

This is substantially narrower than the old C27 endpoint of one macroscopic reciprocal diagonal.

## 5. Exact remaining lemma

The global scalar endpoint remains

\[
\boxed{
 b+\sum_F(\deg F-4)>2h.
}
\tag{5.1}
\]

For the bridge-dominant near-zero subbranch, the shortest geometric substitute is now:

> **BR — radial macroscopic bridge exclusion.** For every fixed `eta>0`, no sufficiently large lexicographically normalized triangle-free global minimizer can simultaneously have
> \[
> S_{\rm br}\ge\eta D^2,
> \qquad
> D\varepsilon=o(1),
> \]
> together with a C66 star center `z` for which a linear family of contact bridges has stress `Theta_eta(D)`, supporting-line distance `o(D)` from `z`, and radial progress `1-o(1)`, while the ZBR-required nonconcurrent crossing diameter bars carry vanishing aggregate non-star weight.
>
> It is enough to derive an `Omega(1/D)` response-defect lower bound, a strict sub-`D` competitor, or the face inequality (5.1).

The missing step must use actual geometry of the linearly many radial loaded bridge blocks. Rank, tree depth, and stress support alone remain compatible with a heavily weighted radial skeleton plus lightly weighted two-dimensional branches.

## 6. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| C27 one macroscopic bridge | already canonical/report input | Existing theorem. |
| Linearly many eta-heavy bridges (ZBL1) | proved | `O(D)` bridge count plus `alpha_e<=D` and total bridge stress `Omega(D^2)`. |
| Torque localization (ZBL2) | proved | Exact C20 resultant/moment identity; star-incident force lines have zero moment about `z`. |
| Heavy bridge lines are `o(D)` from C66 center | proved in `D epsilon->0` phase | ZBL2 plus C66 non-star mass bound. |
| Almost all heavy bridges make near-unit radial progress | proved in `D epsilon->0` phase | C68 radial defect and each heavy bridge's `Omega(D)` contact stress. |
| Linear radial bridge family is impossible | not proved | Requires new geometry/global packing. |
| Level I | still open | General bridge-light/two-edge-connected and exceptional-face/isolate branches remain. |

## 7. Regression tests and failed implications

### Radial bridge tree

An abstract tree of long radial arms with positive but highly nonuniform stresses is compatible with ZBL1–ZBL4. Loaded blocks may carry tiny transverse branches. Therefore

```text
Omega(D) heavy near-radial bridges -> contradiction
```

is not a graph-theoretic theorem.

### Tiny non-star diameter weights

ZBR forces nonconcurrent support at a nonsingleton bridge, but the necessary extra bars can have arbitrarily small positive `beta`. ZBL2 explicitly allows their total mass `tau_e` to tend to zero while their `D`-scale lever arms provide the residual torque.

### Supporting-line localization is macroscopic, not absolute

From C66, ZBL3 gives

\[
\operatorname{dist}(z,\ell_e)
=O_\eta(D^2\varepsilon).
\]

Under only `D epsilon->0`, this is `o(D)` but need not be `O(1)`. It is invalid to replace macroscopically radial by an exact ray or a bounded-width tube.

### Radial progress does not imply one contact chain

C68 controls contact stress measure, not contact support. A two-dimensional framework can have most stress on near-radial edges and geometrically necessary low-stress transverse contacts. The earlier C68 regression remains binding.

## 8. Literature imported

No new literature theorem is imported. Inputs are internal C20, C27, C66, C68, ZBR, and the standard source diameter bound.

## 9. Computation and reproducibility

No computation is used. Every inequality is exact at finite `D`; only the final `o(D)` descriptions invoke the stated asymptotic hypothesis `D epsilon->0`.

## 10. Canonical promotion recommendation

**Hold as report.**

ZBL depends on report-level ZR/ZF/ZK/ZBR and on C66/C68. If those dependencies are promoted, update the bridge frontier by replacing the one-cut bridge-dominant endpoint with:

```text
S_bridge >= eta D^2
+ D epsilon -> 0
  -> Omega_eta(D) bridges with alpha=Omega_eta(D)
  -> all their lines pass o(D) from one stress-star center
  -> all but o(D) make 1-o(1) radial progress
  -> nonsingleton cuts still require low-weight nonconcurrent diameter corrections.
```

Do not promote BR; it is the open geometric endpoint.

## 11. Next run

The most concrete next attack is to combine ZBL with C29/C39 loaded-block accounting. There are `Omega_eta(D)` macroscopic near-radial bridge cuts, while no reaction-free degree-two block exists and a nonsingleton cut requires ZBR rank-three diameter support. A closure must show that the required loaded/transverse events either

- consume `Omega(D^2)` radial-defect energy, contradicting C68;
- force an `Omega(1/D)` response defect through C66/C64; or
- create enough exact face/train currency to prove (5.1).

A local per-block positive charge is not available without an additional quantitative hypothesis; existing near-degenerate rhombic and degree-five regressions prohibit that shortcut.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem ZBL, conditional on the audited ZR/ZF/ZK/ZBR stack:

If S_bridge >= eta D^2, set c_eta=eta/(4pi). Then at least eta D/2 contact
bridges satisfy alpha_e >= c_eta D.

For any bridge e and any diameter vertex z,
  alpha_e * dist(z, line(e))
    <= D^2 * (crossing beta mass on edges not incident to z).

At the C66 stress-star center,
  tail beta <= C0 D epsilon.
Hence every eta-heavy bridge satisfies
  dist(z,line(e))/D <= (4pi C0/eta) D epsilon.
So if D epsilon->0, Omega_eta(D) macroscopic bridge lines all pass o(D) from z.

C68 also gives, for every fixed xi>0, only o(D) of those heavy bridges can have
  | |u-z|-|v-z| | <= 1-xi.
Thus almost all make near-unit radial progress from the same center.

Exact remaining bridge lemma BR:
exclude this linear macroscopic radial bridge family with low-weight nonconcurrent
diameter corrections, or derive epsilon=Omega(1/D), the exact face inequality,
or a strict sub-D competitor.
```
