> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_loaded_chord_elimination_2026-09-14.md) · source SHA-256 `ff86603be7b46d8c682c869996a0b6e5f844b8572ea38ca174bdea5f1fd61634`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-579DC70FA3F3","canonical":true,"claim_ids":["C-FULLCORE-LOADED-CHORD"],"claim_statuses":{"C-FULLCORE-LOADED-CHORD":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — full-core loaded-chord elimination

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.49
**Run type:** closing proof / exact geometric reduction / promotion
**Target:** Target C-II / Level I
**Starting status:** canonical full-core near-disk branch, canonical component deatomization and loaded-hull ledgers
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** not used for the result
**Computation:** not used

## LEVEL I STATUS

STILL OPEN

This report proves a near-disk geometric elimination of nonconsecutive loaded-loaded unit chords. It sharpens the full-core ledger to $`c_B=0`$. Its earlier $`\mu_D=1`$ endpoint discussion is superseded numerically by the canonical train-coupled floor, but the loaded-chord lemma remains a live dependency. It does not produce an exact unit equilateral triangle, a strict source-preserving diameter decrease, or a Level-I settlement.

## 1. Starting endpoint and candidate chain

The canonical full-core route has:

    full-core near-disk force hull
        -> every unit chord between loaded hull vertices is a hull side
        -> c_B=0 and e_BB=q-m_B
        -> sharpened exact ledger for mu_D
        -> use the canonical mu_D>=1 and q/h lower bound
        -> eliminate or isolate the remaining endpoint

The last arrow is not completed. The endpoint analysis below shows that the remaining scalar possibility has linear $`s_Z`$; the current theorem library has no support-to-motion or source-capacity theorem that excludes that branch.

## 2. Loaded-chord theorem

### Theorem LC.1

Consider a sequence in the canonical full-core, no-macroscopic-container, near-disk Type-II branch, with diameter $`D`$ tending to infinity. Let $`F`$ be the actual loaded force hull and let $`B=\operatorname{Vert}(F)`$. Let $`p,q`$ be distinct vertices of $`F`$ which are unit-separated source points. For all sufficiently large members of the sequence, $`p`$ and $`q`$ are consecutive vertices of $`F`$.

Equivalently, every loaded-loaded unit contact is a side of the loaded convex hull. With the Section-63 notation, if $`m_B`$ is the number of nonunit sides of $`F`$, then

```math
\boxed{c_B=0,\qquad e_{BB}=q-m_B.}
\tag{LC.1}
```

Here $`c_B`$ counts loaded-loaded contacts beyond the unit sides of the convex loaded hull, and $`e_{BB}`$ counts every loaded-loaded unit contact. All source points, including contact-isolated points, remain in the global source; this is only a statement about the loaded vertices.

### Proof

The canonical C-FULLCORE-NEAR-DISK theorem gives, after translation and normalization by $`D`$,

```math
 D^{-1}F\longrightarrow B(0,1/2)
\tag{LC.2}
```

in Hausdorff distance along every full-core subsequence. Thus there are numbers $`r_D,R_D`$ with

```math
 r_D/D\to1/2,\qquad R_D/D\to1/2,\qquad B(0,r_D)\subset F\subset B(0,R_D).
\tag{LC.3}
```

Let $`p,q`$ be a unit chord of $`F`$, and suppose that the positively oriented boundary arc from $`p`$ to $`q`$ contains another loaded hull vertex. Since $`p`$ and $`q`$ lie in the annulus in (LC.3), their minor polar angular separation $`\gamma_D`$ satisfies

```math
 2r_D\sin(\gamma_D/2)\le |p-q|=1,\qquad \gamma_D=O(D^{-1}).
\tag{LC.4}
```

Because $`F`$ contains the inner disk, it is strictly star-shaped about the
translation center: every radial direction meets $`\partial F`$ once, and the
radial parametrization preserves cyclic boundary order. Thus the shorter polar
interval is the corresponding short boundary arc. For a point $`x`$ on this arc,
let $`n`$ be an outward supporting normal and let $`e=x/|x|`$ be the radial
direction. The support inequality for the inner and outer disks gives

```math
 n\cdot e\ge r_D/R_D.
\tag{LC.5}
```

The radial directions on the short arc differ from the radial direction of $`p`$ by $`O(D^{-1})`$; hence the tangent directions of all hull sides on this arc lie in a cone of width

```math
 \tau_D=2\arccos(r_D/R_D)+O(D^{-1})=o(1).
\tag{LC.6}
```

For all sufficiently large $`D`$, $`\tau_D<\pi/3`$. Orient every hull side on this
short boundary arc from $`p`$ toward $`q`$, and write its vector as
$`v_j=\ell_jt_j`$, with $`\ell_j\ge1`$ by unit separation. The preceding support-normal
estimate implies that all directed unit tangents $`t_j`$ lie in one cone of width
$`\tau_D=o(1)`$. Choose a unit axis $`t_0`$ through the middle of this cone. Then

```math
 t_0\cdot(q-p)=\sum_j\ell_j(t_0\cdot t_j)
 \ge N\cos\tau_D,
\tag{LC.7}
```

where $`N`$ is the number of side occurrences on the arc. If an intervening loaded hull
vertex exists, $`N\ge2`$, and hence
$`1=|q-p|\ge t_0\cdot(q-p)\ge2\cos\tau_D>1`$, a contradiction. The same argument
applies if the intervening vertex is on the other boundary arc, by reversing orientation.
Thus no loaded hull vertex can lie strictly between the endpoints of a loaded-loaded
unit chord, proving (LC.1). $`\square`$

The proof uses only convexity, unit separation, and the full-core near-disk limit. It does not use a KKT weight lower bound, a simple outer walk, an Euler-path claim, or any deletion of contact-isolated points.

## 3. Exact ledger consequences

Use canonical Section 63 and Section 75. The exact loaded-hull split is

```math
e_{BB}=q-m_B+c_B,\qquad c_I+s_C+c_B=m_B+k-2,\qquad k=d_H+s_Z.
\tag{LC.8}
```

Theorem LC.1 gives, for all sufficiently large full-core survivors,

```math
\boxed{e_{BB}=q-m_B,}
\tag{LC.9}
```

and hence

```math
\boxed{s_C=m_B+k-c_I-2.}
\tag{LC.10}
```

Substituting in $`\mu_D=(e_{BB}+2s_C-3k)/D`$ gives the exact finite identity

```math
\boxed{\mu_DD=q+m_B-k-2c_I-4.}
\tag{LC.11}
```

Canonical C-COMP-DEATOMIZATION gives $`c_I=O(D^{2/3})`$, so asymptotically

```math
\mu_D={q+m_B-k\over D}+o(1).
\tag{LC.12}
```

The exact Section-63 payment $`e_{BB}\ge Q+2k`$ becomes

```math
\boxed{q-m_B\ge Q+2k.}
\tag{LC.13}
```

This is a genuine strengthening of the high-surplus endpoint description: the loaded-contact currency can no longer be stored in additional loaded chords.

## 4. Adversarial analysis of the $`\mu_D=1`$ endpoint

Let

```math
c:=2\rho=1.478170\ldots,\qquad \rho=\cos\rho,
\tag{LC.14}
```

be the canonical difference-body lower constant. Canonical Section 75 gives

```math
\liminf {q\over D}\ge\liminf {h\over D}\ge c,\qquad
\liminf\left(\mu_D+{2k\over D}\right)\ge c.
\tag{LC.15}
```

Suppose, for the endpoint audit, that a full-core sequence had $`\mu_D\to1`$. Pass to a subsequence on which $`q/D`$, $`m_B/D`$, and $`k/D`$ converge, writing their limits as $`q_0,m_0,k_0`$. Equations (LC.12) and (LC.13) imply

```math
1=q_0+m_0-k_0,\qquad q_0-m_0\ge2k_0.
\tag{LC.16}
```

Thus

```math
q_0+3m_0\le2,\qquad q_0\le2.
\tag{LC.17}
```

Because $`h=q-d_H`$ and $`h/D\ge c`$,

```math
{d_H\over D}\le q_0-c.
\tag{LC.18}
```

Since $`k=d_H+s_Z`$, (LC.16) and (LC.18) force

```math
\boxed{\liminf {s_Z\over D}\ge k_0-q_0+c=m_0+c-1\ge c-1=0.478170\ldots .}
\tag{LC.19}
```

Therefore the $`\mu_D=1`$ endpoint is not a low-defect endpoint. It requires a linear mixed-rigidity surplus, while simultaneously having $`q_0\le2`$ and $`m_0\le(2-q_0)/3`$. This is an exact narrowing, not a contradiction.

The current canonical library does not provide the missing implication

```math
s_Z\ge(2\rho-1-o(1))D
\quad\Longrightarrow\quad
\text{an exact unit equilateral triangle or a strict source-preserving decrease}.
\tag{LC.20}
```

In particular, the ZR/ZF affine-kernel statement is scoped to the nonisolated positive-contact core and cannot be used to turn (LC.19) into a full-source motion. The mixed-surplus branch remains live.

## 5. Exact frontier effect

This result removes the nonconsecutive-loaded-chord subbranch from the full-core near-disk analysis. It changes the live high-surplus alternatives from

    loaded unit sides + loaded interior chords + pinned/mixed surplus

to

    loaded unit hull sides + pinned surplus + mixed surplus.

It does not remove the aggregate Section-122 detour, the macroscopic-container branch, or the high $`s_Z`$ source-level obstruction. No canonical state or route map is changed by this report.

## 6. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Full-core force hull converges to a radius-$`D/2`$ disk | canonical | C-FULLCORE-NEAR-DISK | exact stated scope of the canonical dichotomy |
| Short-arc tangent cone has width $`o(1)`$ | proved here | convexity and (LC.3)–(LC.6) | support/radial calculation |
| Every loaded-loaded unit chord is a hull side | proved here | previous row; unit separation | two side occurrences would have length projection $`>1`$ |
| $`c_B=0,\ e_{BB}=q-m_B`$ | proved here | Section 63 definitions | all extra loaded contacts are excluded |
| $`c_I=O(D^{2/3})`$ | canonical | C-COMP-DEATOMIZATION / Section 75 | retained as the exact canonical bound |
| Endpoint restriction (LC.19) | proved here | (LC.11)–(LC.18), Section 75 difference-body floor | asymptotic algebra; no source deletion |
| Full-core C-II closure | not proved | missing high-$`s_Z`$ bridge | (LC.20) remains open |

## 7. Regression checks

* **Regular odd shell:** its loaded unit contacts are hull sides, so $`c_B=0`$; the theorem is compatible with this canonical regression and does not claim that a shell is globally optimal.
* **Near-disk vanishing-shear lattice:** its geometric loaded boundary can satisfy the chord conclusion; the family is not a global minimizer and supplies no source-level closure.
* **Non-near-disk polygons:** LC.1 is not claimed there. A convex polygon can have short nonconsecutive chords with a wide intervening arc; the near-disk annulus and support cone are essential.
* **Contact-isolated source points:** they never enter $`B,c_B`$, or the affine-kernel theorem; they remain in the full source.
* **Repeated outer-walk occurrences:** the proof is on the convex hull boundary and does not simplify any contact walk.
* **Diameter graph:** no Euler path or simple diameter-edge order is inferred.

## 8. Literature and computation

No external theorem or computation is logically required. The only non-elementary inputs are the canonical repository claims named above. The endpoint calculation is exact asymptotic algebra; the decimal $`c-1`$ is only an orientation value and is not used as a certified closure margin.

## 9. Promotion record

The independent audit
docs/audits/target_c_fullcore_loaded_chord_elimination_independent_audit_2026-09-14.md
checked the annular radial estimate, the short-arc correspondence for a nonsmooth
convex force hull, the cone-sum contradiction, the exact loaded-hull ledger
substitution, and the endpoint algebra. The theorem is promoted as
C-FULLCORE-LOADED-CHORD in state 2026-09-14.audit.49.

The promotion is scoped to the canonical full-core near-disk branch. It does not
promote the high-$`s_Z`$ implication, does not apply to the macroscopic-container
branch, and does not change the C-II or Level-I status.

## 10. Handoff

1. Strongest new result: every full-core near-disk loaded-loaded unit contact is a hull side; equivalently $`c_B=0`$ and $`e_{BB}=q-m_B`$.
2. Canonical dependency chain: C-FULLCORE-NEAR-DISK + Section 63 loaded-hull ledger + C-COMP-DEATOMIZATION + C-DB-DENSITY.
3. Exact remaining lemma: exclude the linear mixed-surplus endpoint (LC.19), or convert it into a source-preserving strict diameter decrease/exact triangle.
4. Binding dead routes: scalar ledger elimination, density-only near-unit lattice comparisons, contact creation without force transfer, and full-source affine-kernel extension.
5. Read next: docs/targets/target-c/64-extreme-circuit-transfer-audit.md, docs/targets/target-c/66-forest-doubled-gap-audit.md, docs/reports/target_c_stress_transversal_reinsertion_2026-09-12.md, and the current Section-122/123 full-core reports.
