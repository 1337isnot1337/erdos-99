> Generated reading edition · [exact source](../../../docs/reports/target_c_fsjc_endpoint_disk_exclusion_2026-09-10.md) · source SHA-256 `f57ff40514ffd36ad10bee010a168b606ac7dfc293c947bcfd625f22eb7f13e2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4CF945C41322","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fsjc_endpoint_disk_exclusion_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=ef9ce099eb5612331c5887ee5500446da92a8d30; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FSJC endpoint exclusion by central-symmetric disk rigidity

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-full-source-closure-2026-09-10`, based on `1ea7a3c5970d614c9f860841eea5ad3718ca171f`  
**Run type:** closing-proof continuation / equality-case audit  
**Target:** Target C, C-II after ZF/FS/FSDB/FSJC  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** decimal evaluation only; no computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The FSJC floor

```math
\lambda_*:=0.5882283437736394387\ldots
```

is **not attainable asymptotically** by a post-ZF survivor. More precisely, there is
an absolute, presently nonexplicit `eta_FS>0` such that every sufficiently large
survivor in the audited post-ZF class satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}\ge \lambda_*+\eta_{FS}.
}
\tag{FJN.1}
```

The decisive new step is that FS.4 supplies asymptotic central symmetry of the actual
force hull about the full-source circumcenter. Equality in the JC capacity bound would
also force `per(F)/D -> pi`. After normalization, Cauchy's perimeter formula then makes
the force-hull limit a body of constant width one. Central symmetry upgrades this to
the **radius-one-half disk**, so its area is `pi/4`. This is incompatible with the
same attachment-cell/cavity equality which defines the FSJC endpoint.

No Blaschke--Lebesgue stability theorem is needed.

---

## 1. Starting endpoint

Let

```math
\lambda_*
```

be the positive root of

```math
(\pi^2+1)\lambda^2+\pi\lambda-\frac{\pi^2}{4}-\pi=0.
\tag{1.1}
```

FSJC proves

```math
\liminf\frac{e_{BB}+2s_C}{D}\ge\lambda_*
\tag{1.2}
```

and proves that any sequence approaching equality must have

```math
\frac hD\to\frac\pi2.
\tag{1.3}
```

The implication attacked here is

```text
lambda -> lambda_*
  -> h/D -> pi/2 and e_BB/D -> lambda_*
  -> simultaneous saturation of the JC cavity bound
  -> per(F)/D -> pi
  + FS.4 central symmetry
  -> normalized force hull -> radius-1/2 disk
  -> area(F)/D^2 -> pi/4
  -> attachment-cell gap exceeds the saturated JC capacity by (pi-2)/8
  -> contradiction.
```

---

## 2. Theorem FJN — the FSJC endpoint is impossible

Assume an unbounded sequence of triangle-free global minimizers has been chosen first
to minimize contacts and then diameter pairs, and assume the audited post-ZF chain
applies to the relative-interior force hull `F`. Put

```math
\lambda_j:=\frac{e_{BB,j}+2s_{C,j}}{D_j}.
```

Then no such sequence satisfies

```math
\lambda_j\to\lambda_*.
\tag{FJN.2}
```

Consequently there exists an absolute `eta_FS>0` for which (FJN.1) holds for all
sufficiently large audited post-ZF survivors.

### Proof

Assume for contradiction that (FJN.2) holds. Pass to subsequences whenever necessary.
Write

```math
t_j:=\frac{e_{BB,j}}{D_j},
\qquad
y_j:=\frac{h_j}{D_j}.
```

FSJC endpoint localization gives

```math
y_j\to\frac\pi2.
\tag{2.1}
```

Also `0<=t_j<=lambda_j`, so take `t_j->t<=lambda_*`.

FSDB and GU give the lower gap estimate

```math
\liminf\frac{G_j}{D_j^2}
\ge
\Phi(\pi/2)-\frac\pi4\lambda_*^2,
\qquad
\Phi(y)=\frac{y+\sin y}{4}.
\tag{2.2}
```

The unrelaxed JC cavity estimate gives

```math
\limsup\frac{G_j}{D_j^2}
\le
\frac{(t+\pi/2)^2}{4\pi}.
\tag{2.3}
```

By the defining equation (1.1),

```math
U_*:=
\Phi(\pi/2)-\frac\pi4\lambda_*^2
=
\frac{(\lambda_*+\pi/2)^2}{4\pi}.
\tag{2.4}
```

If `t<lambda_*`, then the right side of (2.3) is strictly smaller than `U_*`,
contradicting (2.2). Hence

```math
\boxed{t=\lambda_*.}
\tag{2.5}
```

In particular

```math
\boxed{\frac{s_C}{D}\to0,}
\tag{2.6}
```

and (2.2)--(2.4) force

```math
\boxed{\frac G{D^2}\to U_*.}
\tag{2.7}
```

We now retain the exact remainder that JC discarded in its scalar relaxation. With
`P_F=per(F)`, `d_H=q-h`, and `s_Z` the mixed-row surplus, the JC derivation gives

```math
E_{out}+Q
\le
P_F-h+e_{BB}-3d_H-2s_Z.
\tag{2.8}
```

Every term `d_H,s_Z` is nonnegative, and `P_F<=pi D`. Moreover the same proof gives

```math
G\le H_{out}+A_{exc}+O(D),
\qquad
H_{out}+A_{exc}
\le\frac{(E_{out}+Q)^2}{4\pi}+o(D^2).
\tag{2.9}
```

Equations (2.1), (2.5), (2.7), and (2.9) imply

```math
\frac{E_{out}+Q}{D}\to\frac\pi2+\lambda_*.
\tag{2.10}
```

Indeed the left side is nonnegative and (2.8) bounds its limsup by
`pi/2+lambda_*`, while a smaller subsequential limit would make the quadratic upper
bound in (2.9) strictly smaller than `U_*`.

Substituting (2.10) back into (2.8) therefore forces every nonnegative remainder to
vanish at linear scale:

```math
\boxed{
\frac{P_F}{D}\to\pi,
\qquad
\frac{d_H}{D}\to0,
\qquad
\frac{s_Z}{D}\to0.
}
\tag{2.11}
```

Now use the full-source geometry, which is the point not available in the older JC
nonattainment argument. Let `o_j` be the full-source circumcenter from FS.1/FS.4 and
normalize

```math
\widetilde F_j:=D_j^{-1}(F_j-o_j).
\tag{2.12}
```

FS.1 puts every `\widetilde F_j` in a fixed bounded disk. Blaschke selection gives a
Hausdorff-convergent subsequence

```math
\widetilde F_j\to F_\infty.
\tag{2.13}
```

FS.4 gives

```math
d_{Haus}(F_j-o_j,-(F_j-o_j))=o(D_j),
```

so

```math
\boxed{F_\infty=-F_\infty.}
\tag{2.14}
```

Every force hull contains an actual diameter pair, hence

```math
\operatorname{diam}F_\infty=1.
\tag{2.15}
```

Perimeter is continuous under planar Hausdorff convergence of convex bodies, so
(2.11) gives

```math
\operatorname{per}F_\infty=\pi.
\tag{2.16}
```

For every unit direction `u`, let `w(u)` be the width of `F_\infty` in that direction.
Cauchy's perimeter formula and (2.15) give

```math
\pi
=\operatorname{per}F_\infty
=\int_0^\pi w(\theta)\,d\theta,
\qquad
0\le w(\theta)\le1.
\tag{2.17}
```

The width function is continuous. Equality in (2.17) therefore implies

```math
w(\theta)=1\quad\text{for every }\theta.
\tag{2.18}
```

Thus `F_infty` has constant width one. Since (2.14) makes it centrally symmetric about
the origin, its support function satisfies

```math
w(u)=h(u)+h(-u)=2h(u).
```

Equation (2.18) gives `h(u)=1/2` for every unit `u`. Hence

```math
\boxed{F_\infty=\tfrac12 B_2.}
\tag{2.19}
```

Area is also continuous under Hausdorff convergence, so

```math
\boxed{
\frac{\operatorname{area}F_j}{D_j^2}\to\frac\pi4.
}
\tag{2.20}
```

GU's attachment-cell estimate remains

```math
\limsup
\frac{\sum_r\operatorname{area}(P_r)}{D_j^2}
\le\frac\pi4\lambda_*^2.
\tag{2.21}
```

Therefore (2.20)--(2.21) give

```math
\liminf\frac{G_j}{D_j^2}
\ge
\frac\pi4(1-\lambda_*^2).
\tag{2.22}
```

But by (2.4),

```math
\begin{aligned}
\frac\pi4(1-\lambda_*^2)-U_*
&=\frac\pi4-\Phi(\pi/2)\\
&=\frac{\pi-2}{8}>0.
\end{aligned}
\tag{2.23}
```

This contradicts the exact limit (2.7). Thus no endpoint sequence (FJN.2) exists.
`square`

To obtain the uniform gap, suppose no `eta_FS>0` works. For every integer `m` choose
an audited survivor with `D>=m` and

```math
\lambda<\lambda_*+\frac1m.
```

FSJC's universal asymptotic lower bound forces the resulting sequence to satisfy
`lambda->lambda_*`, contradicting Theorem FJN. This proves (FJN.1). `square`

---

## 3. Exact endpoint population consequences

Although the endpoint sequence has just been proved impossible, its forced normal form
is useful for quantitative stability work.

The exact ZU ledger is

```math
c_I+e_{BB}+s_C=q-2+d_H+s_Z.
\tag{3.1}
```

Since `q=h+d_H`, equations (2.1), (2.5), (2.6), and (2.11) would force

```math
\boxed{
\frac{c_I}{D}\to\frac\pi2-\lambda_*
=0.9825679830212571\ldots .
}
\tag{3.2}
```

ZK gives the exact component ledger

```math
\sum_r\delta_r+R_I+s_B+3(d_H+s_Z)
=6+e_{BB}+2s_C.
\tag{3.3}
```

Hence an endpoint sequence would satisfy

```math
\limsup\frac{\sum_r\delta_r}{D}\le\lambda_*.
\tag{3.4}
```

Every nonsingleton unloaded component has integer contact-graph diameter at least one.
Therefore the number `N_1` of singleton unloaded components would obey

```math
\boxed{
\liminf\frac{N_1}{D}
\ge
\frac\pi2-2\lambda_*
=0.3943396392476177\ldots .
}
\tag{3.5}
```

Finally ZK's component decomposition has

```math
s_C=\sum_r s_r,
\qquad
s_r=t_r-\delta_r-3-r_r,
\qquad s_r,r_r\ge0.
```

For a singleton, `delta_r=r_r=0`, so `s_r=t_r-3`. Since `s_C=o(D)`, all but `o(D)`
of the singleton components counted in (3.5) have exactly three loaded neighbors.
Thus the impossible endpoint would contain at least

```math
\left(\frac\pi2-2\lambda_*-o(1)\right)D
```

interior positive-stress tripods, each with three distinct loaded attachments.
Triangle-freeness makes all three attachment-to-attachment distances strictly greater
than one.

This population statement is not used in the disk contradiction; it is retained as a
stability target for the next stage.

---

## 4. Dependency audit

The positive proof uses the following inputs only.

1. `docs/targets/target-c/56-ci-restored-frontier.md`: C-I closure and the
   contact/diameter lexicographic representative, so the relative-interior stress sees
   all actual active rows.
2. `docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md` plus
   `campaign_zero_transfer_defect_review_2026-09-09.md`: ZR/ZF. The consolidated review
   independently records that Z, ZC, ZR, and ZF survive under the promoted C53/C63
   inputs and retain isolates outside the core.
3. `docs/reports/target_c_zf_exact_defect_budget_addendum_2026-09-09.md`: exact ZU
   ledgers used only in Section 3.
4. `docs/reports/target_c_full_source_circumradius_response_2026-09-10.md`: FS.1 and
   FS.4. Their source-radius step was rechecked against canonical Oler 21.1, the strict
   translated-lattice comparison, and the Bonnesen source-hull estimate in Target A
   Section 155. Their central-symmetry estimate is the direct midpoint/parallelogram
   consequence recorded in FS.4.
5. `docs/reports/target_c_fs_symmetric_difference_body_area_2026-09-10.md`: FSDB
   functional area floor.
6. `docs/reports/target_c_component_slack_cancellation_2026-09-09.md` and
   `target_c_db_upgraded_component_gap_2026-09-09.md`: ZK/GU attachment-cell upper
   bound.
7. `docs/reports/target_c_post_pi_joint_cavity_budget_2026-09-09.md`: JC cavity bound
   and its exact perimeter remainder (2.8).
8. `docs/reports/target_c_fsdb_joint_cavity_surplus_05882_2026-09-10.md`: exact FSJC
   root and unique `y=pi/2` endpoint localization.

The only convex-geometric facts newly used here are Blaschke selection, continuity of
area/perimeter under Hausdorff convergence for planar convex bodies, and Cauchy's
perimeter formula. The constant-width-to-disk step is proved directly from central
symmetry and the support function. No quantitative stability theorem is assumed.

Because several ZF/FSDB/FSJC inputs are still report-level rather than promoted route
modules, FJN should remain a report-level audited consequence until those dependencies
are promoted together.

---

## 5. Exact target implication

Before this report, FSJC allowed an extremal sequence with

```math
\frac{e_{BB}+2s_C}{D}\to\lambda_*.
```

FJN removes that entire equality regime and upgrades the asymptotic lower bound to a
**uniform strict gap**

```math
\frac{e_{BB}+2s_C}{D}\ge\lambda_*+\eta_{FS}
```

for some absolute `eta_FS>0` and all sufficiently large survivors.

The gap is intentionally not assigned a numerical value. Doing so requires a
quantitative stability version of the perimeter/central-symmetry argument, or a direct
finite cyclic-gap inequality. Reporting another unsupported decimal would weaken the
audit.

This still does not close C-II: the current theorem stack has no universal upper bound
on `(e_BB+2s_C)/D` below `lambda_*+eta_FS`.

---

## 6. Regression audit

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | its loaded-loaded currency has ratio asymptotic to `pi`, far above the excluded FSJC endpoint; it can also approach the disk force-hull shape |
| dense isolated shell fillings | yes | FS.1/FS.4 use all source points only to obtain the common containing center/radius; no force-bulk population statement is assumed |
| half-weight matching obstruction | yes | FJN never converts reciprocal-perimeter saturation into a large matching or beta-mass floor |
| shell response trace defect `2D^2-2` | yes | no arbitrary-data response operator bound is used; only the geometric force-hull symmetry from FS.4 enters |
| near-equilateral strict rhombi | yes | no uniform local angular or face-area gap is assumed |
| heptagon plus isolated center | yes | isolates remain outside the ZF core and are never declared diametral |

The decisive hypothesis absent from the shell regressions is the **FSJC endpoint
capacity equality for a globally optimal lexicographic source**. That equality forces
`per(F)/D->pi` at the same time that the globally sourced FS.4 symmetry acts on the
actual force hull.

---

## 7. Failed routes / cautions

1. The argument does not imply that near-maximal reciprocal perimeter makes the
   diameter graph an almost-full-weight matching. The exact odd-shell regression still
   blocks that inference.
2. The argument does not promote coordinate-field radialization to an operator norm
   estimate for `Lambda`.
3. `per(F)/D->pi` alone would only give a constant-width limit. The new contradiction
   uses FS.4 to obtain **central symmetry of the same limit**; without it a Reuleaux-type
   constant-width body remains possible.
4. The conditional singleton-tripod density in Section 3 is not itself a contradiction:
   triangle-free degree-three positive barycenters can exist locally.

---

## 8. Computation and reproducibility

No computational certificate is required. The defining constant is the exact positive
root (1.1). For reference,

```math
\lambda_*=0.5882283437736394387149516348687\ldots,
```

```math
\frac\pi2-\lambda_*=0.9825679830212571805\ldots,
\qquad
\frac\pi2-2\lambda_*=0.3943396392476177418\ldots.
```

The fixed normalized area margin in the contradiction is exact:

```math
\frac\pi4-\Phi(\pi/2)=\frac{\pi-2}{8}>0.
```

---

## 9. Canonical promotion recommendation

**Hold as report pending joint dependency promotion.** FJN itself is proof-complete
relative to the audited post-ZF report stack. If FS/FSDB/FSJC and the ZF/JC ledgers are
promoted, FJN should be promoted with them and the old `0.588228...` endpoint language
should be replaced by a strict nonattainment statement.

---

## 10. Next run

The highest-value next theorem is a **quantitative force-hull cyclic-gap stability
inequality**. FS.4 says every normalized force hull is `o(1)`-close to a centrally
symmetric convex hull of points on the radius-one-half circle. Retain the actual
force-hull perimeter in JC instead of replacing it by `pi D`, and relate its perimeter
deficit to its area deficit by the cyclic angular gaps. This can turn the qualitative
`eta_FS>0` into an explicit stronger feasible-region inequality rather than another
standalone scalar iteration.

In parallel, retain the exact ZU/ZK currencies. A near-endpoint source must have a
linear family of nearly slack-free degree-three singleton harmonic components; any
finite-capacity charge extracted from those tripods would feed directly into the
whole-source `O(D)` allowance.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem FJN:
No audited post-ZF survivor sequence can satisfy
    (e_BB+2s_C)/D -> lambda_*,
where lambda_* is the positive root
    (pi^2+1)lambda^2+pi lambda-pi^2/4-pi=0
    =0.5882283437736394387...
Hence some absolute eta_FS>0 exists with
    (e_BB+2s_C)/D >= lambda_*+eta_FS
for every sufficiently large survivor.

Proof mechanism:
FSJC equality -> h/D->pi/2 and e_BB/D->lambda_*.
Exact JC remainder -> per(F)/D->pi, d_H/D->0, s_Z/D->0.
FS.4 -> normalized F is asymptotically centrally symmetric.
Cauchy equality -> limit has constant width one.
Central symmetry -> limit is radius-1/2 disk, area pi/4.
GU then gives gap >= pi(1-lambda_*^2)/4,
which exceeds the saturated JC value by exactly (pi-2)/8.
Contradiction.

Endpoint normal form (inside the contradiction):
    c_I/D -> pi/2-lambda_*,
    singleton unloaded components/D >= pi/2-2lambda_*-o(1),
    s_C/D,d_H/D,s_Z/D ->0.
Almost all of those singleton components are degree-three loaded tripods.

Level I remains open because no universal upper bound on the pinned/contact currency
has yet crossed the new strict lower gap.
```
