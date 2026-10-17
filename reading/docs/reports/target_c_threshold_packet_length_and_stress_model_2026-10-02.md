> Generated reading edition · [exact source](../../../docs/reports/target_c_threshold_packet_length_and_stress_model_2026-10-02.md) · source SHA-256 `c2057db1fb60f634ecca9f8cbe476623a0db96dd645d0626b1c75b48ac15dcad`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-0536CA14406C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: long packet reactions and a consistent cut stress model

**Phase 2 preservation provenance:** PR #618, branch swarm/sol/threshold-rail-packet-20261002, audited source head 9e042ddb7144cbc2f47baac0fa63e9a8ac316761. Preserve as a conditional length theorem plus an abstract cut-stress regression; PSD cut data are not asserted to come from a global-minimizer source.

Date: 2026-10-02. Research base: `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
Starting checkout: `78a65968d51af7871a0ce5a865bf2db1a2c2e0ec`.
State: `2026-09-14.audit.51`. Branch: `swarm/sol/threshold-rail-packet-20261002`.

Classification: **proved candidate awaiting independent audit/promotion** for
the conditional length theorem; **regression** for the abstract cut-data
model. Artifact lifecycle is unreviewed. Level I and C-II remain **OPEN**.

```text
actual endpoints in every intervening layer
 -> packet reaction >= multiplier mass times a truncated interval length
 -> weighted staircase support incidence in exact KKT peak pressure
 -> abstract PSD stress still survives; closure needs actual source coupling
```

## 1. Inputs

This continues [the packet reaction report](target_c_threshold_packet_reaction_floor_2026-10-02.md),
Sections 2--6. Its new finite geometry is re-used as an unpromoted dependency.
The only canonical analytic input is FS.1 in
[the full-source audit](../targets/target-c/58-full-source-geometry-audit.md).
The threshold staircase, layer occupancy and laminar cut equation remain
conditional on main's explicitly named unpromoted reports in the first packet.

For each tree edge $`e=\{a,b\}`$, put $`s_e=b-a`$, let $`B_e`$ be its total
diameter multiplier mass and $`R_eu`$ its axial resultant. The theorem is

```math
\boxed{R_e\ge B_e\min\left\{\frac D{16},\frac{2s_e}3\right\}
\qquad(D\ge512).} \tag{1}
```

This applies to boundary and internal packets, with every actual source point
retained. In particular, for $`s_e\ge\varepsilon D`$, the reaction per
multiplier mass is at least $`D\min\{1/16,2\varepsilon/3\}`$.
There is no assumed lower bound on the masses $`B_e`$.

## 2. Proof of the length theorem

Use the positive-pair convex average from the first report. Fix any one pair
and denote its reaction by $`\rho`$. Shared-endpoint pairs have
$`\rho\ge D/2`$, so satisfy the required bound. The same is immediate if
$`\rho\ge D/16`$. Assume four distinct endpoints and $`\rho<D/16`$.

The midpoint argument in the first report gives a same-arc corresponding-end
chord of length $`L`$ satisfying

```math
L\le F_D(\rho):=
\sqrt{2D\left(D-\sqrt{D^2-\rho^2}\right)}
=\rho\sqrt{\frac{2D}{D+\sqrt{D^2-\rho^2}}}
<\frac D{15}. \tag{2}
```

The last bound follows by squaring
$`\sqrt{255/256}>449/450`$. The multiplicative factor in (2) is less than
(16/15); a weaker rational estimate suffices here.

Let (x,y) be this chord's two actual diameter endpoints. They are in layers
(a,b) on the same physical hull arc, ordered from the reference diameter
endpoint $`z`$ to its other endpoint $`w`$. Use FS.1 to take a containing
radius $`R<9D/16`$, $`r_0=D-R>7D/16`$, as in the first report.
The two chosen outward diameter normals differ by at most

```math
\Delta=2\arccos(r_0/R)+2\arcsin(L/(2r_0)).
```

Here $`t=L/(2r_0)<8/105<1/13`$, so

```math
\cos(\Delta/2)
>\frac79\sqrt{1-t^2}-\frac69t
>\frac79\frac{168}{169}-\frac6{9\cdot13}
=\frac{1098}{1521}>\frac1{\sqrt2}. \tag{3}
```

Thus $`\Delta<\pi/2`$. The two supporting lines bound the exterior triangle
used in the first report. Its diameter is less than $`\sqrt2L<D`$, so it
cannot contain the two reference diameter endpoints (z,w). Consequently
the exterior boundary arc between (x,y) is the arc within the relevant
physical shore, rather than its complement containing (z,w).

Convexity puts every directed hull-side tangent on that short arc into the
cone of width at most $`\Delta`$ between the two endpoint tangents. The
layer-occupancy theorem supplies at least one distinct actual diameter vertex
at every intervening layer $`a+1,\ldots,b-1`$. These occur strictly between
(x,y) in monotone arc order. Hence the short arc contains at least $`s_e`$
full-source hull sides, each of length at least one. Project their sum onto
the middle tangent direction to obtain

```math
L\ge s_e\cos(\Delta/2)>\frac{1098}{1521}s_e.
```

Together with (2), this gives

```math
\rho>\frac{15}{16}\frac{1098}{1521}s_e>\frac23s_e.
```

Every pair reaction therefore satisfies the truncated bound. Its convex
average proves (1). The proof counts actual distinct source vertices in
intervening layers; it does not identify a layer with one vertex or discard
isolated source points.

## 3. Exact effect on the cut ledger

The exact KKT equation now yields

```math
\boxed{A_r\ge\beta_0D+
\sum_{e\in E(T)}B_e\min\{D/16,2s_e/3\}.} \tag{4}
```

The unweighted staircase identity is still
$`\sum_es_e=m(m+1)/2`$. It cannot be substituted into (4) without a theorem
controlling the **actual multiplier masses**. All masses are positive, but
that fact alone does not prevent arbitrarily small mass on long intervals.

## 4. The attempted aggregate/PSD closure fails exactly

One tempting next lemma was that a connected paired staircase, positive packet
masses, strict single-peak pressures, normalized diameter weights and PSD of
the scalar cut stress matrix are incompatible with (1). They are compatible
as abstract cut data, even with distinct projective directions assigned to
all diameter rows.

Let $`T`$ be any staircase tree on gaps $`0,\ldots,m`$; let $`v_e`$ be its
interval indicator in $`\mathbb R^m`$. Choose $`D=1024m`$, positive $`B_e`$ with
$`\sum_eB_e<1`$, and $`\beta_0=1-\sum_eB_e>0`$. Number the edges $`e=1,\ldots,m`$
and put

```math
d_e=s_e+\frac{e}{10m},\qquad R_e=B_ed_e,
\qquad A=\beta_0D\mathbf1+\sum_eR_ev_e.
```

Assign two formal rows $`d_eu\pm\sqrt{D^2-d_e^2}Ju`$ of weight (B_e/2)
to each packet, and (Du) of weight $`\beta_0`$ to the reference row.
They have length $`D`$, positive weights, exact transverse balance, normalized
total weight, and mutually distinct projective directions. Their axial sums
give precisely the displayed cut pressures. The interval incidence has full
rank; the pressure profile has the strict staircase peak.

The scalar cut matrix is

```math
K=\operatorname{diag}(A)-\beta_0\mathbf1\mathbf1^T
-\sum_eB_ev_ev_e^T.
```

It is **positive definite**, because

```math
K=\beta_0(DI-\mathbf1\mathbf1^T)
+\sum_eB_e\left[s_e\operatorname{diag}(v_e)-v_ev_e^T\right]
+\sum_e\frac{eB_e}{10m}\operatorname{diag}(v_e).
```

The first term is positive definite since $`D>m`$. Each bracket is PSD by
Cauchy--Schwarz on its $`s_e`$ supported coordinates; the last term is PSD.
All reaction floors in (1), and indeed $`R_e>B_es_e`$, hold.
One may take $`B_e=\varepsilon/m`$ with arbitrarily small $`\varepsilon>0`$,
preserving every statement. This is an exact obstruction to an inference
from positivity or PSD to a uniform coefficient lower bound.

These formal rows are **not asserted to be co-embedded diameter segments of
one source**. There is no supplied full positive-contact graph, equilibrium
at actual vertices, affine stress kernel, or finite feasible train motion.
The model is a counterexample to the abstract cut-data lemma, not to a
source-geometric closing theorem, C-II, or Level I. It identifies the missing
hypothesis: joint realization at actual train ports and outer faces.

## 5. Computation and hostile audit

[The exact verifier](../../../research/verify_threshold_packet_length_stress_2026_10_02.py)
enumerates all 255 staircase trees through eight cuts and three rational
mass scales. It checks connectivity/full interval rank, the staircase
incidence identity, distinct formal row projections, normalized weights,
strict peak inequalities, and all 765 positive-definite cut matrices by
exact rational LDL pivots. The general consistency result has the preceding
analytic proof; enumeration is a finite regression certificate.

Hostile checks: stars and paths are included; actual sources and formal row
models are separated; no weight floor is inferred from positivity; no
infinitesimal motion is called finite or feasible; the reference and every
intervening actual diameter endpoint are retained. The full-source radius
bound holds also with contact isolates and outside the full-core branch.

## 6. Remaining source obligation

The unresolved bridge is **joint source realization of the two-shore KKT
port reactions**, with all outer-face and inactive-pair constraints. It must
either exclude the formal-compatible actual staircase, supply a feasible
finite release, or force a unit triangle. The unique weak adjacent pivot in
the first report remains a real strict-slack possibility at the geometric
level. Both positive strong reactions and that pivot must be handled.

No other C-II branch has been eliminated. Open-cell exact phase, nonconstant
phase, split-star, inactive interfaces, the macroscopic-container/exterior-cap
branch and the rest of the full-core branch are explicitly still open.
Canonical state and promotion status are unchanged.
