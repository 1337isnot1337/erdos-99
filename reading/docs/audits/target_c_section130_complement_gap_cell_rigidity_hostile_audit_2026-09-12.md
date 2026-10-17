> Generated reading edition · [exact source](../../../docs/audits/target_c_section130_complement_gap_cell_rigidity_hostile_audit_2026-09-12.md) · source SHA-256 `4595a6760d913d0e10e63b32afa44cf8b7efd310d0bba0674059cecfc934faad`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-22D93968BF33","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C complement-gap cell rigidity

**Date:** 2026-09-12
**Reviewed:** proof-only Section 130 candidate.
**Disposition:** **PASS at proof-only Type-II endpoint scope.** C-II remains open.

## 1. Exact implication chain

```text
wrapping carrier limit + circle-segment decomposition
 -> residual cell area fills every fixed positive gap
 -> laminar cap superadditivity forces one full-gap support arc
 -> residual diameter moment >= sum_j sin(g_j/2)
 -> stronger endpoint inequality for 4h-d_H-5s_Z.
```

The argument is conditional on the candidate’s explicit common diameter cap at the
Section-118 endpoint. It is not an all-regime C-II closure.

## 2. Residual-cell localization

For a limiting wrapping support (S) on the radius-(1/2) circle, canonical circle
geometry decomposes the disk outside (operatorname{conv}(S)) into disjoint circular
segments (mathcal C_j), one for each complement gap (g_j<\pi).  Pairwise interior
disjointness of harmonic cells prevents a positive-area convex residual limit from
meeting two distinct segments: the segment between interior points in the two regions
would cross the interior of the wrapping convex hull.

The square-root area bound controls the discarded small-cell tail by (O(\sqrt\eta)
in normalized area.  Therefore, for any fixed positive gap, sending (D\to\infty)
and then (eta\downarrow0) forces the residual cell area in that segment to approach
the full segment capacity (G(g_j)).  This order of limits is essential and is
stated explicitly in the candidate.

**Verdict:** PASS at the stated limiting scope.

## 3. Full-gap support from cap superadditivity

Within a fixed gap, retain inclusion-maximal laminar support arcs of lengths

```math
0<\theta_i\le g,qquad \sum_i\theta_i\le g.
```

Canonical circular-segment geometry gives the superadditivity

```math
G(a)+G(b)\le G(a+b),
```

with strict inequality for positive (a,b) and (a+b<\pi).  Thus

```math
\text{residual area in the gap}
\le\sum_iG(\theta_i)
\le G\left(\sum_i\theta_i\right)
\le G(g).
```

Area saturation forces equality.  Strict superadditivity then allows at most one
positive maximal arc, and its length is (g).  Its endpoint support points have chord
length (sin(g/2)), so the corresponding cell diameter has at least that normalized
size.

**Verdict:** PASS.  Nested cells are charged collectively below their maximal arc;
no pointwise tiling or unproved equality uniqueness is assumed.

## 4. Summing gaps and inserting the moment

For any finite set of gaps, the forced cells are distinct because one convex residual
cell cannot occupy two gap components.  Summing the diameter lower bounds and then
using monotone convergence gives

```math
\liminf_D D^{-1}\sum_{r\ne w}d_r
\ge\sum_j\sin(g_j/2).
```

Canonical Section 101 supplies the lower bound on this same complement-chord scalar,
which yields the candidate value (M(\theta_*)) at the Section-118 endpoint.  The
wrapping carrier contributes (mu_*D+o(D)) under the common diameter cap.

**Verdict:** PASS, conditional on the named canonical endpoint and gap-scalar input.

## 5. Aggregate and degree ledgers

The completion-triangle payment cancels the loaded-contact and cell-dissection terms
in the Section-124 capped-diameter inequality.  Therefore a lower bound

```math
\sum_rd_r\ge(S-o(1))D
```

gives

```math
3(h-s_Z)-2s_C
\ge\left(S+\frac\pi4(2-\sqrt3)\right)D-o(D).
```

The additional inequalities

```math
t_r\ge d_r+1,qquad e_{BI}+2e_{BB}\le3q,qquad e_{BB}=q-m,
```

then yield (q+2m\ge SD-o(D)).  Using the proof-only Section-75/Section-125
relation (s_C=m+k+o(D)) gives (3q-2m-5k\ge(S+c_{det}/2)D-o(D)).  Adding the two
inequalities and substituting (q=h+d_H), (k=d_H+s_Z) gives

```math
4h-d_H-5s_Z\ge(2S+c_{det})D-o(D),
```

matching the candidate’s coefficient.  All these downstream steps are explicitly
proof-only and Type-II conditional; none is treated as canonical here.

**Verdict:** PASS at the stated dependency scope.

## 6. Limitations

- The common cap (max_r d_r\le(\mu_*+o(1))D) is an endpoint branch assumption.
- The theorem does not provide an upper bound on (4h-d_H-5s_Z).
- The macroscopic inactive-container branch is untouched.
- Contact-isolated source points remain outside the positive-contact core ledgers.
- No exact unit triangle or source-preserving strict diameter decrease follows.

## Final classification

**Audited-working.** Section 130 is a sound proof-only conditional strengthening of the
full-core endpoint branch and should be preserved with its explicit hypotheses. C-II
and Level I remain open.
