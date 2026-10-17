> Generated reading edition · [exact source](../../../docs/reports/target_c_d6_approximate_orbit_stability_2026-09-14.md) · source SHA-256 `71cee4bcafee38cffb1bfdb50edc8df7a7faccbadb23f9790e6ebbfc591a7f83`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6280DCCB022D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — approximate sixfold affine-window stability

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.47
**Run type:** exact comparison / source-level deformation criterion
**Target:** C-II / Level I
**Starting status:** canonical full-core budget floor promoted; C-II remains open
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** status only; no theorem imported
**Computation:** exact rational certificate

## LEVEL I STATUS

STILL OPEN

This report strengthens the exact sixfold affine-window comparison from the companion
report target_c_d6_symmetric_affine_window_comparison_2026-09-14.md. It tolerates a
finite orbit defect in the index difference set. It still assumes an affine lattice
source and supplies no theorem that a general C-II minimizer has such coordinates or
such orbit control.

## 1. Candidate chain

    approximate sixfold orbit of a diameter-realizing index difference
        -> explicit lower bound for the sheared diameter
        -> strict same-cardinality equilateralized competitor
        -> exclusion of the affine source from global minimizers

The first arrow is an additional affine-source hypothesis. The last arrow is an exact
global-minimality contradiction once the first three arrows hold.

## 2. Definitions

Let $`S\subset\mathbb Z^2`$ be finite with $`|S|\ge2`$, and put

```math
\Delta=S-S.
```

Let

```math
r(i,j)=(-j,i+j),
\qquad q_c(i,j)=i^2+j^2+2cij,
\qquad q_e=q_{1/2}.
```

For $`c\in(-1/2,1/2)`$, choose unit vectors $`u,v_c`$ with
$`u\cdot v_c=c`$, and define

```math
A_c(S)=\{iu+jv_c:(i,j)\in S\}.
```

Let

```math
D_c^2=\max_{z\in\Delta}q_c(z),
\qquad
D_e^2=\max_{z\in\Delta}q_e(z).
```

Define $`\|z\|_e=\sqrt{q_e(z)}`$. Let $`z_0\in\Delta`$ attain $`D_e^2`$. Say that
the diameter-realizing difference has orbit defect at most $`E\ge0`$ if, for every
$`0\le k<6`$, there is $`w_k\in\Delta`$ with

```math
\|w_k-r^kz_0\|_e\le E.
\tag{AO.1}
```

Exact $`D_6`$-difference symmetry is the special case $`E=0`$, with the condition
imposed for every $`z\in\Delta`$.

## 3. Approximate-orbit theorem

### Theorem AO.1

Under these definitions, $`A_c(S)`$ is unit-separated and triangle-free. Put

```math
K_c:=\sup_{x\ne0}\frac{q_c(x)}{q_e(x)}.
```

The orbit-defect hypothesis (AO.1) implies

```math
\boxed{
D_c^2\ge
\frac{4-2c}{3}D_e^2-K_cE(2D_e+E).
}
\tag{AO.2}
```

Consequently, if

```math
\boxed{
\frac{1-2c}{3}D_e^2>K_cE(2D_e+E),
}
\tag{AO.3}
```

then $`D_c>D_e`$. The equilateralized source $`A_{1/2}(S)`$ has the same cardinality,
remains unit-separated, and has strictly smaller diameter. Therefore $`A_c(S)`$ cannot
be a global minimum-diameter source for its cardinality.

### Proof

For a nonzero integer pair $`z=(i,j)`$, put $`a=|i|`$, $`b=|j|`$. Since
$`|2c|<1`$,

```math
q_c(i,j)\ge a^2+b^2-ab=(a-b)^2+ab\ge1.
```

If both coordinates are nonzero, equality in the last lower bound can occur only for
$`a=b=1`$, but then $`q_c(i,j)=2\pm2c>1`$. If one coordinate vanishes, the value
is an integer square. Thus the only possible unit differences are
$`(\pm1,0)`$ and $`(0,\pm1)`$. These change the parity of $`i+j`$, so the unit-contact
graph is bipartite and contains no unit equilateral triangle.

The rotation $`r`$ is an isometry of $`q_e`$, so
$`\|r^kz_0\|_e=D_e`$. By definition of $`K_c`$,

```math
\|x\|_c\le\sqrt{K_c}\,\|x\|_e.
```

For each $`k`$, the reverse triangle inequality and (AO.1) give

```math
\left|\|w_k\|_c-\|r^kz_0\|_c\right|\le\sqrt{K_c}E.
```

Also $`\|w_k\|_e\le D_e+E`$, hence

```math
\|w_k\|_c+\|r^kz_0\|_c
\le\sqrt{K_c}(2D_e+E).
```

Using the difference of squares,

```math
q_c(w_k)\ge q_c(r^kz_0)-K_cE(2D_e+E).
\tag{AO.4}
```

Direct expansion over the six rotations gives

```math
\sum_{k=0}^5q_c(r^kz_0)
=6\frac{4-2c}{3}q_e(z_0)
=6\frac{4-2c}{3}D_e^2.
\tag{AO.5}
```

Every $`w_k`$ lies in $`\Delta`$, so $`D_c^2`$ is at least the maximum of the six
$`q_c(w_k)`$, and therefore at least their average. Equations (AO.4) and (AO.5)
prove (AO.2). Subtracting $`D_e^2`$ from its right side gives

```math
\frac{1-2c}{3}D_e^2-K_cE(2D_e+E),
```

which is positive under (AO.3). Finally,
$`q_{1/2}(i,j)=i^2+j^2+ij\ge1`$ for every nonzero integer pair, so the
equilateralized source is feasible and has the same number of points. This is an
explicit strict global-minimality contradiction. $`\square`$

## 4. Uniform elementary constant

For $`|c|<1/2`$,

```math
|ij|\le\frac{i^2+j^2}{2},\qquad
q_e(i,j)\ge\frac{i^2+j^2}{2},\qquad
q_c(i,j)\le\frac32(i^2+j^2).
```

Consequently $`K_c\le3`$, and the sufficient condition

```math
\frac{1-2c}{3}D_e^2>3E(2D_e+E)
\tag{AO.6}
```

is exact after clearing the one square root. In particular, fixed positive shear
margin and $`E=o(D_e)`$ imply strict exclusion eventually. More generally, the
finite condition holds whenever $`E=o((1-2c)D_e)`$.

## 5. Exact consequence and limitation

The theorem excludes an affine source whenever its diameter-realizing difference has
six approximate rotated copies with defect smaller than the shear scale. It therefore
handles bounded index defects or boundary perturbations for any fixed
non-equilateral shear, and handles vanishing shear down to the explicit scale

```math
1-2c\gg E/D_e.
```

It does not cover arbitrary asymmetric windows with orbit defect $`O(D_e)`$, holes or
interfaces without a controlled difference-set defect, an affine chart not supplied by
a source-level theorem, contact-isolated points outside the affine source, a
non-coembedded carrier/scaffold, or the macroscopic inactive chamber/exterior-cap
branch.

The square-window regression remains decisive against unrestricted
equilateralization. For $`S_m=\{-m,\ldots,m\}^2`$, the orthogonal source has
$`D_0^2=8m^2`$, while $`q_{1/2}(2m,2m)=12m^2`$. This is not a global-minimizer
claim; it shows that orbit control is load-bearing.

## 6. Proof-obligation ledger and status

**Proved candidate:** the finite inequality (AO.2) and the strict same-cardinality
global-minimality exclusion under (AO.3).

**Canonical inputs:** none are needed for the affine theorem. The canonical C-II stack
is motivation only.

**Unresolved implication:** prove an affine description with
$`E=o((1-2c)D)`$ for every relevant triangle-free full-core global minimizer, or
replace it by a source-preserving deformation handling asymmetric windows, holes,
interfaces, and isolated points. The current canonical theorem state does not supply
that implication.

The exact certificate is
research/verify_target_c_d6_approximate_stability.py. It uses the uniform exact bound
$`K_c\le3`$, performs no optimization, and proves no statement outside the explicit
affine hypotheses. This report is unreviewed/proved-candidate-awaiting-promotion; no
canonical state, route map, prompt, or Level I status is changed.
