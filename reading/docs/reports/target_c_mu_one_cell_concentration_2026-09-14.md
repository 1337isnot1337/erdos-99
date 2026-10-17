> Generated reading edition · [exact source](../../../docs/reports/target_c_mu_one_cell_concentration_2026-09-14.md) · source SHA-256 `3219725fdfff3edcc886ac78ec55cbc0d97762e2abaa16f7cf4b5c17ac3462d6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A1DD590E9A7D","canonical":true,"claim_ids":["C-FULLCORE-MU-ONE-CELL"],"claim_statuses":{"C-FULLCORE-MU-ONE-CELL":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — Target C-II equality-budget one-cell concentration

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.49`
**Run type:** closing proof / synthesis
**Target:** C-II
**Starting status:** canonical full-core budget-floor endpoint
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used for orientation only; no external theorem imported
**Computation:** not used; the argument is an exact inequality proof

## LEVEL I STATUS

`STILL OPEN`

This report records a new asymptotic equality-case reduction. It does not settle the
original universal quantifiers over all sufficiently large cardinalities and all global
minimizers.

## 1. Starting canonical endpoint

The current canonical full-core endpoint is the stronger train-coupled surplus floor
`C-FULLCORE-TRAIN-SURPLUS-FLOOR`; the earlier budget floor
`C-FULLCORE-DIAMETER-BUDGET-FLOOR` is also canonical. With

```math
  \mu_D:=\frac{e_{BB}+2s_C-3(d_H+s_Z)}{D},
  \qquad k:=d_H+s_Z,
```

that theorem gives

```math
  \liminf \mu_D\ge
  \frac{2\pi+2\sqrt{\pi/(2\sqrt3)}}5
  =1.6375621841815\ldots
```

for every canonical full-core near-disk rhombic-saturation sequence. The exact
source-level chain sought here was

```text
mu_D -> 1
    -> one attachment cell carries all diameter-scale cell area and diameter
    -> equality geometry for the near-disk harmonic carrier
    -> exact unit triangle or source-preserving strict sub-D competitor
```

The one-cell implication below was proved against the earlier scalar floor. The
stronger canonical train-coupled floor makes its antecedent $`\mu_D\to1`$
impossible for a canonical Type-II sequence, so it is a formally valid but vacuous
equality-case consequence in the current state. The genuine high-surplus closure
remains open.

## 2. Strongest genuinely new result

**Classification:** canonical theorem C-FULLCORE-MU-ONE-CELL, promoted after the
independent audit cited below

### Statement

Let $`D_j\to\infty`$ be a sequence in the canonical Target C-II full-core branch.
For each $`j`$, let $`P_{r,j}=\operatorname{conv}(A_{r,j})`$ be the actual convex
attachment cells of the unloaded positive-contact components, with all source points
retained. Let

```math
  \alpha_{r,j}:=\operatorname{area}(P_{r,j}),
  \quad d_{r,j}:=\operatorname{diam}(P_{r,j}),
  \quad \delta_{r,j}:=\operatorname{diam}_{\rm graph}(I_{r,j}).
```

Assume the canonical hypotheses

```math
\begin{aligned}
 \sum_r\alpha_{r,j}&=\frac\pi4D_j^2-o(D_j^2),\\
 \sum_r\sqrt{\alpha_{r,j}}&\le C D_j,\\
 d_{r,j}&\le \delta_{r,j}+2,\\
 \sum_r\delta_{r,j}&\le 6+\mu_jD_j,\\
 c_{I,j}&=O(D_j^{2/3}),
\end{aligned}
```

where $`c_{I,j}`$ is the number of unloaded positive-contact components, and suppose
$`\mu_j\to1`$. Then there is a choice of one actual cell $`P_{*,j}`$ such that

```math
\frac{d_{*,j}}{D_j}\longrightarrow1,
\qquad
\frac{\operatorname{area}(P_{*,j})}{D_j^2}\longrightarrow\frac\pi4,
```

and

```math
 \sum_{r\ne *}d_{r,j}=o(D_j),
 \qquad
 \sum_{r\ne *}\operatorname{area}(P_{r,j})=o(D_j^2),
 \qquad
 \sum_{r\ne *}\operatorname{per}(P_{r,j})=o(D_j).
```

Moreover,

```math
 \frac{\operatorname{per}(P_{*,j})}{D_j}\longrightarrow\pi,
 \qquad
 \sum_r\operatorname{per}(P_{r,j})=\pi D_j+o(D_j),
```

and, after translating and scaling by $`D_j`$, the dominant cells converge in Hausdorff
distance along every subsequence to a Euclidean disk of radius $`1/2`$. Equivalently,

```math
 \inf_{o\in\mathbb R^2}
 \frac1{D_j}d_H\left(P_{*,j},B(o,D_j/2)\right)\longrightarrow0.
```

This is an equality-case theorem for the earlier scalar budget. Since the stronger
canonical train-coupled floor gives $`\liminf\mu_D\ge1.637562\ldots`$, no canonical
Type-II sequence can actually satisfy $`\mu_D\to1`$. Thus the implication is
formally valid but vacuous on the current canonical branch. It is not a theorem
that the source itself is a lattice patch, that all phases agree, or that any cell can
be moved while preserving the source cardinality and the global optimum.

### Scope

The statement is asymptotic and subsequential in the equality regime $`\mu_j\to1`$.
It concerns actual attachment-cell convex hulls inside the full source-level
full-core branch; the cells are not being substituted for the source. Contact-isolated
source points are not deleted or bounded by this argument. Global optimality enters only
through the canonical Target C-II normal form and the promoted full-core hypotheses;
the new argument itself does not construct a competitor and does not use an unproved
finite deformation.

### Proof

Write $`D=D_j`$, $`\alpha_r=\alpha_{r,j}`$, $`d_r=d_{r,j}`$, and similarly for
the other quantities while proving the finite-$`j`$ estimates.

#### Step 1: a fixed threshold leaves only a small amount of cell area

Fix $`\eta>0`$, and call a cell large when $`\alpha_r\ge\eta D^2`$. The square-root
budget gives

```math
 \#\{r:\alpha_r\ge\eta D^2\}\,\sqrt\eta D
 \le\sum_r\sqrt{\alpha_r}\le CD,
```

so the number of large cells is at most $`C/\sqrt\eta`$. Every small cell satisfies
$`\alpha_r\le\sqrt\eta D\sqrt{\alpha_r}`$, and therefore

```math
 \sum_{r\ {\rm small}}\alpha_r
 \le C\sqrt\eta D^2.
\tag{2.1}
```

Since the total cell area is $`\pi D^2/4-o(D^2)`$,

```math
 \sum_{r\ {\rm large}}\alpha_r
 \ge \left(\frac\pi4-C\sqrt\eta-o(1)\right)D^2.
\tag{2.2}
```

#### Step 2: the diameter-square mass is almost $`D^2`$

The planar isodiametric inequality applied to each convex cell gives

```math
 \alpha_r\le\frac\pi4d_r^2.
```

Thus, with

```math
 Q_\eta:=\sum_{r\ {\rm large}}d_r^2,
```

equation (2.2) implies

```math
 Q_\eta\ge
 \left(1-\frac{4C}{\pi}\sqrt\eta-o(1)\right)D^2.
\tag{2.3}
```

On the other hand, the canonical component-diameter budget and
$`d_r\le\delta_r+2`$ give, for the sum over all cells,

```math
 S:=\sum_r d_r
 \le \sum_r\delta_r+2c_I
 \le 6+\mu_jD+2c_I
 =D+o(D),
\tag{2.4}
```

because $`\mu_j\to1`$ and $`c_I=O(D^{2/3})`$. In particular, the same upper bound
holds for the large-cell sum $`S_\eta:=\sum_{r\ {\rm large}}d_r`$. Since
$`Q_\eta\le S_\eta^2\le S^2`$, equations (2.3)--(2.4) give

```math
 S^2-Q_\eta\le
 \left(\frac{4C}{\pi}\sqrt\eta+o(1)\right)D^2.
\tag{2.5}
```

Choose $`*`$ to be a cell of maximum diameter among all cells. A large cell exists
for all sufficiently large $`j`$, by (2.2), so $`*`$ is at least as large as a
large cell. Also

```math
 Q_\eta\le d_* S,
```

and therefore (2.3)--(2.4) imply

```math
 \frac{d_*}{D}
 \ge 1-\frac{4C}{\pi}\sqrt\eta-o(1).
\tag{2.6}
```

Because $`P_*=P_{*,j}\subseteq F_j`$ and $`\operatorname{diam}(F_j)=D_j`$, we also
have $`d_*\le D`$. Since $`\eta`$ is arbitrary, this proves

```math
 d_*/D\to1.
\tag{2.7}
```

Let $`T:=S-d_*`$ be the sum of the diameters of all other cells. The cross terms in
$`S^2-\sum_r d_r^2`$ include $`2d_*T`$. Since
$`\sum_r d_r^2\ge Q_\eta`$, equation (2.5) gives

```math
 d_*T
 \le S^2-Q_\eta
 \le\left(\frac{4C}{\pi}\sqrt\eta+o(1)\right)D^2.
```

Using (2.7), then taking $`j\to\infty`$ and finally $`\eta\downarrow0`$, yields

```math
 \sum_{r\ne *}d_r=T=o(D).
\tag{2.8}
```

This argument uses the sum over all cells in $`S`$, so small cells cannot hide a
large total diameter outside the selected dominant cell.

#### Step 3: all cell area and perimeter outside the dominant cell vanish

For every cell, again by isodiametry,

```math
 \sum_{r\ne *}\alpha_r
 \le \frac\pi4\sum_{r\ne *}d_r^2
 \le \frac\pi4\left(\sum_{r\ne *}d_r\right)^2
 =o(D^2).
\tag{2.9}
```

Subtracting this from the full-core cell-area saturation gives

```math
 \alpha_*/D^2\to\pi/4.
\tag{2.10}
```

The convex perimeter-diameter inequality gives

```math
 \sum_{r\ne *}\operatorname{per}(P_r)
 \le\pi\sum_{r\ne *}d_r=o(D).
\tag{2.11}
```

For the dominant cell, the isoperimetric inequality and (2.10) give

```math
 \operatorname{per}(P_*)
 \ge2\sqrt{\pi\alpha_*}=\pi D-o(D).
\tag{2.12}
```

The canonical attachment-perimeter identity, followed by the exact component budget,
gives

```math
 \begin{aligned}
 \sum_r\operatorname{per}(P_r)
 &\le \pi\left(6+e_{BB}+2s_C-3k+2c_I\right)\\
 &=\pi\left(6+\mu_jD+2c_I\right)
 =\pi D+o(D).
 \end{aligned}
\tag{2.13}
```

Combining (2.11)--(2.13),

```math
 \operatorname{per}(P_*)/D\to\pi,
 \qquad
 \sum_r\operatorname{per}(P_r)=\pi D+o(D).
\tag{2.14}
```

#### Step 4: near-disk equality geometry

Translate each normalized dominant convex body $`D_j^{-1}P_{*,j}`$ so that it lies
in one fixed bounded disk; this is possible because $`P_{*,j}\subseteq F_j`$, and the
canonical full-core near-disk theorem supplies the corresponding bounded normalization
for $`F_j/D_j`$. By Blaschke selection, every subsequence has a Hausdorff-convergent
subsubsequence with a compact convex limit $`K`$. Equations (2.7) and (2.10) imply

```math
 \operatorname{diam}(K)=1,
 \qquad
 \operatorname{area}(K)=\pi/4.
```

Equality in the planar isodiametric inequality forces $`K`$ to be a disk of radius
$`1/2`$. Since every convergent subsequence has only this form, the distance of the
dominant cells from the family of radius-$`1/2`$ disks tends to zero:

```math
 \inf_o d_H(D_j^{-1}P_{*,j},B(o,1/2))\to0.
\tag{2.15}
```

Rescaling gives the claimed statement. No equality uniqueness theorem for a different
functional (in particular, no Rogalski--Saint Raymond equality-uniqueness claim) is
used.

### Dependencies

- Canonical `C-FULLCORE-NEAR-DISK` / `docs/targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md` supplies full-core force-hull area saturation, the near-disk normalization, and the branch scope.
- Canonical `C-HARMONIC-CELL-TILING` / `docs/targets/target-c/83-attachment-cell-disjoint-tiling-audit.md` supplies actual convex attachment cells, area saturation, and the square-root cell budget. All source points remain retained.
- Canonical `C-ATTACH-CURRENCY` / `docs/targets/target-c/62-attachment-incidence-currency-audit.md` supplies the exact component-diameter budget, (d_r\le\delta_r+2), and the total attachment-perimeter estimate.
- Canonical `C-COMP-DEATOMIZATION` in `docs/state/theorem-state.yaml` supplies (c_I=O(D^{2/3})), used only to remove the additive (2c_I) term after division by (D).
- Standard planar isodiametric, isoperimetric, and convex perimeter-diameter inequalities are used with their usual Euclidean normalization.

No external theorem, numerical optimization, source/scaffold identification, or finite
motion is load-bearing.

## 3. Exact frontier effect

This does not change canonical theorem authority. It isolates the following exact
full-core subproblem:

```math
\boxed{
 \liminf\mu_D=1
 \quad\Longrightarrow\quad
 \text{one actual attachment cell is asymptotically a radius-}D/2\text{ disk and
 carries all diameter-scale cell mass.}
}
```

Before the stronger train-coupled floor was promoted, the full-core branch could be
described as splitting into:

1. a scalar-gap regime $`\liminf\mu_D>1`$, which still needs a source-level use of
   the aggregate detour/payment inequality; and
2. the formal equality regime $`\mu_D\to1`$, where the one-cell near-disk
   implication proved here would apply. The stronger canonical floor excludes this
   regime, so it is not a live C-II branch.

The theorem does not force an equilateral unit triangle. A near-disk convex attachment
cell can still support a sheared, phase-separated, or boundary-defective contact model;
the missing bridge must use actual source geometry or global diameter minimality.

## 4. Exact remaining lemma

The next precise closure target is:

> **Formal one-cell equality implication.** Under the canonical full-core hypotheses and
> $`\mu_D\to1`$, prove that the dominant actual cell either contains a unit
> equilateral triangle or admits an explicit finite source-preserving deformation to a
> unit-separated configuration of the same cardinality and diameter strictly below
> $`D`$.

This must retain all points of the source, including contact-isolated points, and must
address phase interfaces and the occurrence-counted outer walk. A proof about an abstract
rhombic scaffold or a selected lattice subset is insufficient.

The complementary scalar-gap target is:

> **Detour closure.** If the full-core sequence has $`\liminf\mu_D>1`$, upper-bound
> $`\sum_r(L_r-2d_r)`$, or convert the canonical Section-122 detour floor and
> Section-123 payment into a finite source-preserving strict diameter decrease.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Fixed-threshold small-cell area is $`O(\sqrt\eta D^2)`$ | proved candidate | `C-HARMONIC-CELL-TILING` | Direct square-root-budget estimate |
| Large-cell squared diameters carry $`1-O(\sqrt\eta)`$ of $`D^2`$ | proved candidate | isodiametric inequality, previous row | Exact summation; no source replacement |
| $`\mu_D\to1`$ forces one actual cell to have diameter $`D-o(D)`$ | proved candidate | `C-ATTACH-CURRENCY`, `C-COMP-DEATOMIZATION` | Cross-term estimate using the full cell sum |
| All other attachment cells have total diameter $`o(D)`$ | proved candidate | previous row | Same cross-term estimate; small cells are included |
| Dominant cell has area $`\pi D^2/4-o(D^2)`$ | proved candidate | isodiametric inequality, full-core area saturation | Source-level consequence for actual cells |
| Dominant cell and total attachment cells are near perimeter equality | proved candidate | `C-ATTACH-CURRENCY`, isoperimetric inequality | The upper bound is $`\pi D+o(D)`$ because $`c_I=O(D^{2/3})`$ |
| Dominant attachment cell converges to a disk | proved candidate | Blaschke selection, planar isodiametric equality | Does not invoke rejected RSR equality uniqueness |
| Near-disk dominant cell forces an exact unit triangle | unresolved but vacuous under the stronger floor | none | The antecedent $`\mu_D\to1`$ is excluded by `C-FULLCORE-TRAIN-SURPLUS-FLOOR`; this supplies no live branch |
| Scalar gap $`\mu_D>1`$ contradicts global minimality | unresolved | Sections 122--123 | Aggregate outer-walk detour remains uncoupled to a strict competitor |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Contact-isolated source points | pass | No source point is deleted; only the canonical full-core cell ledger is used |
| Source versus scaffold | pass | The conclusion is only about actual $`P_r=\operatorname{conv}(A_r)`$; no scaffold is embedded into the source |
| Fixed-hull Hall capacity | pass | No Hall or matching count is used |
| Boundary-order loss | pass | Additive $`6+2c_I`$ terms are retained and divided only after $`D\to\infty`$; no finite integer contradiction is claimed |
| Rejected RSR disk-equality uniqueness | pass | Only the standard planar isodiametric equality case is used |
| Rejected Eppstein near-quadrangulation inference | pass | No near-quadrangulation conclusion is drawn from disk convergence |
| Sheared oblique-hexagon regression | pass | It shows a restricted affine-window comparison, but does not apply to the arbitrary dominant cell; this is recorded as the remaining bridge |
| Local jammed versus global optimum | pass | No local rigidity is promoted to global optimality |
| Many one-at-a-time exchanges | pass | No exchange or finite integration is asserted |
| Occurrence-counted boundary walks | pass | The new proof uses only cell diameters, areas, and total perimeters, not injectivity of outer-walk occurrences |

## 7. Literature imports

No external theorem was imported. The internet search was used only to confirm the public
problem orientation; all mathematical inputs are the repository's canonical theorem
entries or standard planar convex inequalities. In particular, no equality or uniqueness
claim from Rogalski--Saint Raymond, Eppstein, or another cited source is used.

## 8. Computation

No computation is logically required for the new statement. The argument consists of
the exact inequalities (2.1)--(2.15). Existing repository certificates for the
full-core budget floor and related regressions were not used as proof steps here; they
remain available for auditing the canonical dependencies.

## 9. Corrections / supersessions

This report does not supersede a canonical theorem. The stronger canonical train-coupled
floor supersedes its apparent status as a live boundary regime: the $`\mu_D\to1`$
implication is retained as a formally correct equality-case consequence, but its
antecedent is incompatible with the current Type-II theorem library.

## 10. Promotion record

The independent audit target_c_mu_one_cell_concentration_independent_audit_2026-09-14.md
verified the fixed-threshold order of limits, the cross-term estimate including small
cells, the perimeter upper bound, and the ordinary isodiametric equality step. The
theorem is canonical as C-FULLCORE-MU-ONE-CELL. Its promotion does not close C-II,
and the equality antecedent is already excluded by C-FULLCORE-TRAIN-SURPLUS-FLOOR.

## 11. Handoff

1. Strongest new theorem: $`\mu_D\to1`$ forces one actual attachment cell to carry
   asymptotically all cell area and diameter, with disk equality geometry.
2. Canonical dependency chain:
   `C-FULLCORE-NEAR-DISK` + `C-HARMONIC-CELL-TILING` + `C-ATTACH-CURRENCY` +
   `C-COMP-DEATOMIZATION` $`\to`$ the proved candidate above.
3. Exact remaining lemma: use the surviving high-surplus regime in a source-level
   detour/deformation/triangle argument. The formal $`\mu_D\to1`$ branch is excluded
   by the stronger canonical floor.
4. Binding dead routes: abstract scalar compatibility, one-anchor retraction, restricted
   affine-window shearing, and the rejected full-source affine-kernel extension.
5. Next files to read: `docs/targets/target-c/122-aggregate-two-arc-detour-audit.md`,
   `docs/targets/target-c/123-augmented-cell-defect-budget-audit.md`, and the exact
   phase/inner-grid modules only if an attempted one-cell rigidity lemma uses them.
