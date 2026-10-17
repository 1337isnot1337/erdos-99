> Generated reading edition · [exact source](../../../docs/reports/global_reflected_scale_competitors_2026-10-12.md) · source SHA-256 `63f9abd9de3a50d6d52a5ca37354ef6e461425250fea379bd928fe6a6e7dff35`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F3C61ADE5F89","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Whole-source competitors by reflected coordinates and two scales

**Date:** 2026-10-12
**Base commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**State version:** `2026-10-10.audit.234`
**Target:** literal global Level I, outside the A/B/C bookkeeping
**Classification:** proved candidates awaiting promotion; artifact unreviewed
**Dependencies:** problem definition and elementary Euclidean/signed-graph identities
**Computation:** `research/verify_global_reflected_scale_2026_10_12.py`

## Level I status and closure chain

**Level I remains open.** All labels, including contact isolates, are retained.
The decision result applies to arbitrary finite sources; the explicit sources
below are nonglobal. No endpoint is extracted from the canonical C-II hypotheses.

```text
feasible reflected/scaled placement of the whole source
  -> n distinct planar labels, every distance >= 1 and < D
  -> contradiction to global minimality
  -> Level I only after proving such endpoint existence for all sufficiently
     large triangle-free global minimizers
```

The new ingredient is a discontinuous simultaneous assignment. No continuous
motion between the source and competitor is needed for a global contradiction.

## 1. Exact decision theorem for a fixed line and scales

Let `p_i`, `1<=i<=n`, be all labels of a unit-separated planar source of
diameter `D`. Choose a unit normal `u`, perpendicular unit tangent `v`, line
offset `c`, and positive squared scales `A,B`. Write

$$
x_i=|u\cdot p_i-c|,\qquad y_i=v\cdot p_i,
\qquad q_i=(\sqrt A\,\sigma_i x_i,\sqrt B\,y_i),
\quad \sigma_i\in\{-1,1\}.
$$

These are actual planar positions. Every source label has one chosen position.
Define, for every pair,

$$
s_{ij}=A(x_i-x_j)^2+B(y_i-y_j)^2,
\qquad o_{ij}=A(x_i+x_j)^2+B(y_i-y_j)^2.
$$

Always `s_ij<=o_ij`. A placement with every squared distance in `[1,D^2)`
exists **if and only if** both conditions hold:

1. no pair has `o_ij<1` or `s_ij>=D^2`;
2. the signed graph with an opposite-sign edge whenever `s_ij<1` and a
   same-sign edge whenever `o_ij>=D^2` has consistent parity on every cycle.

Parallel contradictory edges count as a cycle of length two. A pair can
contribute both constraints, so it must not be silently treated as just one edge.

**Proof.** A same-sign pair has squared length `s_ij`, an opposite-sign pair
has squared length `o_ij`. A forbidden pair in condition 1 has no valid choice.
Otherwise `s_ij<1` forces opposite signs and `o_ij>=D^2` forces equal signs.
These are the only restrictions. Their simultaneous solvability is exactly
cycle-parity consistency: assign one root bit in each component, propagate
bits along edges, and check every edge. A solution satisfies every lower and
strict upper bound. This proves necessity and sufficiency. Building all costs
and deciding parity takes `O(n^2)` arithmetic operations. Strict separation
ensures distinct labels, so the resulting source has exactly `n` points. QED.

This is a finite source-wide theorem. It makes no selected-stress, chart,
wall-safe capacity, source-point deletion, or inactive-pair omission assumption.
Positive results are exact competitor certificates. Failure for one line and
two scales says nothing about another parameter choice or global optimality.

## 2. An infinite explicit family escaping affine obstruction

For integers `K>=1`, `M>=20(K+1)`, take every square-grid point

$$
P_{M,K}=\{(i,j):i,j\in\mathbb Z,\ |i|\le M,\ |j|\le K\}.
$$

The contact graph is triangle-free and the diameter squared is
`D^2=4(M^2+K^2)`. Set

$$
u=(351,280)/449=(c,s),\quad v=(-s,c),\quad
A=1/2,\quad B=9/5,\quad L=4K+2.
$$

Choose the original sign of `u dot p` on `|i|<=L`, and positive sign on every
other label. This gives a strictly unit-separated whole-source competitor
of strictly smaller diameter.

### Complete pair proof

The affine map before changing signs is strictly unit-separated on the
integer lattice. For integer differences of norm squared at least two,

$$
|Tz|^2=\tfrac12|z|^2+\tfrac{13}{10}(v\cdot z)^2\ge1.
$$

Equality would require a norm-squared-two vector perpendicular to `v`, which
the stated rational direction excludes. The two coordinate unit vectors have
squared images `405441/403202>1` and `1304809/1008005>1`.

Consequently every opposite cost is above one, and every pair with same cost
below one must have opposite original normal signs. Such a pair also has
`|y_i-y_j|<1`, hence `|i-i'|<(2cK+1)/s`. Opposite original normal signs give

$$
|i|,|i'| < (s/c+2c/s)K+1/s <4K+2=L.
$$

For example, if `i>K`, its normal sign is positive and an opposite-sign label
has `i'<(s/c)K`; the displayed bound follows. The other cases follow by
interchanging labels or changing signs. Thus **every lower-forcing edge has
both endpoints in the central strip**.

Since `K<=M/20`, the absolute normal coordinates have range at most
`133M/160<M`, and tangential differences at most `133M/100<4M/3`. Every same
cost therefore satisfies

$$
s_{ij}<\left(\tfrac12+\tfrac95\tfrac{16}{9}\right)M^2
=\tfrac{37}{10}M^2<4M^2\le D^2.
$$

If one endpoint is in the central strip, both its opposite normal sum and
tangential difference are at most

$$
M+L+2K\le M+6(K+1)\le13M/10.
$$

Thus its opposite cost is at most `3887M^2/1000<4M^2<=D^2`.
**No upper-forcing edge touches the central strip**. Original signs satisfy
all lower edges there; positive signs satisfy all upper edges outside it.
The decision theorem now verifies every pair, not just contacts or diameters.

All resulting squared lengths have form

$$
(5X^2+18Y^2)/(10\cdot449^2),\qquad X,Y\in\mathbb Z.
$$

Equality to one is impossible: modulo five it forces `5|Y`, and modulo 25 it
would force `X^2=2 (mod 5)`. Therefore every distance is strictly above one.
One may normalize the minimum distance back to one and further shorten the
diameter. No normalization is needed for the global contradiction. QED.

### Why every affine competitor fails

Write the squared metric of an arbitrary affine linear part as `G`. Actual
horizontal and vertical unit contacts force `G_xx,G_yy>=1`. The two original
diameter vectors `(2M,2K)` and `(2M,-2K)` force the maximum squared diameter
to be at least

$$
4M^2G_{xx}+4K^2G_{yy}+8MK|G_{xy}|
\ge4(M^2+K^2)=D^2.
$$

Translations do not change this. The finite reassignment evades an exact
affine obstruction; it is not an affine descent in disguise.

### Positive equilibrium and PSD stress on the boundary

Let `lambda=1/[8(M^2+K^2)]`. Give each horizontal boundary unit edge weight
`2M lambda`, each vertical boundary unit edge weight `2K lambda`, and each of
the two actual diameters weight `lambda`. Set all other contact weights to
zero. This is a nonnegative normalized equilibrium at every source label;
both the contact-weight sum and weighted diameter-square sum equal one.

The signed stress `Omega=L_C-L_H` is PSD. For a scalar vector `z`, applying
Cauchy--Schwarz to each boundary chain leaves nonnegative chain-variance
terms, and the corner contribution is

$$
\lambda(z_{BL}+z_{TR}-z_{TL}-z_{BR})^2.
$$

Its kernel restricted to the boundary is the three-dimensional affine space:
zero variance makes each side affine, and the corner equality is the only
corner restriction. All other labels add zero rows and their own kernel
directions. This support distinction is essential: no full-source ZR/ZF or
mixed-rigidity claim follows. PSD equilibrium also does not prove optimality.

## 3. Finite certificate with two contact isolates

Take the `31 by 5` grid `-15<=i<=15`, `-2<=j<=2`, and the two points
`(0,16/5)`, `(0,-16/5)`. There are 157 labels, all retained; both added points
are contact-isolated. The diameter squared is exactly 916. The decision
theorem with the same normal and scales produces an endpoint whose exact
full-source squared-distance range is

$$
\left[\frac{405441}{403202},\frac{865065744}{1008005}\right].
$$

Thus all contacts open, all 12,246 pairs remain separated, and the squared
diameter improves by `58266836/1008005>0`. This smaller-aspect fixture uses the
exact solver rather than the conservative sufficient bound of Section 2.
The verifier independently reconstructs all endpoint pairs and checks the
normalized nonnegative equilibrium at all 157 original labels.

## 4. Scope, regressions, and next global obligation

| Claim | Classification | Exact limit |
| --- | --- | --- |
| fixed-parameter full-source decision theorem | proved candidate awaiting promotion | does not extract parameters |
| infinite rectangle-family finite competitors | proved candidate awaiting promotion | sources are nonglobal |
| affine/stress obstruction escaped | regression | does not refute canonical C-II source theorems |
| 157-label endpoint with both isolates | exact regression certificate | no global-minimizer hypothesis |
| density alone implies exact triangle | rejected shortcut | canonical triangle-free density-cap regression |
| one reflected-scale endpoint exists for every large triangle-free minimizer | unresolved | not inferred from any finite search |

Exploratory floating searches found no endpoint for regular unit odd rims of
sizes 7, 9, and 11 in the tested one-step parameter grid. This is neither an
impossibility certificate nor evidence of global optimality. Iteration may
be necessary. A sequence may pass through infeasible intermediate placements:
global comparison needs only the final same-cardinality feasible source.

The companion
[`global_reflection_moment_obstruction_2026-10-12.md`](global_reflection_moment_obstruction_2026-10-12.md)
proves a full-source obstruction: at leading optimal density, a feasible
one-step endpoint of diameter at most `(1+o(1))D` must have both squared scales
tending to one. It also audits unrestricted composition: at most one selective
reflection per label realizes any prescribed target, so representability alone
adds no bridge. These are unreviewed candidate results, not canonical inputs.

The exact global obligation remains to extract a strict same-cardinality
competitor using actual global source geometry. A bounded coherent packet
reassembly theorem would be one substantive bridge. The source population,
original diameter pairs, inactive pairs, and isolates must enter it together.

## Computation and provenance

Run `python3 research/verify_global_reflected_scale_2026_10_12.py`.
Arithmetic is exact rational; algebraic endpoint coordinates are represented
by rational normal/tangent coordinates and their squared scales. The script
checks the 157-label certificate and independent explicit-formula fixtures
`(M,K)=(40,1),(60,2)`. The analytical proofs above establish the infinite-family
and decision statements. No computation proves canonical-source extraction,
global optimality, a uniformly dense family, or Level I closure.

The whole-problem prompt and canonical state were bootstrap context. No
unpromoted mathematics or external theorem is a proof premise. The literature
search checked the problem setting but supplied no theorem used here.
Preserve this as unreviewed research; theorem promotion has not occurred.

## Autonomous audit (2026-10-15)

The [PR #959 AI audit](../audits/pr959_autonomous_proof_audit_2026-10-15.md)
records the full proof scope and computational repairs. This remains a
noncanonical artifact; the destination's independent exact-head AI-agent mathematical audit has not been completed. Claims remain unreviewed and unpromoted.
