> Generated reading edition · [exact source](../../../docs/reports/global_dense_factorized_barrier_2026-10-12.md) · source SHA-256 `cea8009b28aeedeacad8e9731a8cae6964524e778382c404d6c55e95d38fa65f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-616855D04589","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Sharp population reserve and a finite transformation barrier do not imply globality

**Date:** 2026-10-12
**Repository commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**State version:** `2026-10-10.audit.234`
**Run type:** global-mechanism falsification and exact computation
**Target:** whole-source Level I
**Classification:** unreviewed candidate / regression
**Level I:** STILL OPEN

## 1. Global proposition being tested

The earlier finite product barrier might be dismissed as a low-density rim
phenomenon. This report proves that the obstruction can coexist with the sharp
all-minimizer population-reserve coefficient, at unbounded diameters and quadratic
cardinalities, in triangle-free sources with an explicit strict competitor.

The rejected proposed implication is

```text
triangle-freeness + sharp D^(2/3) population reserve
 + stability under every factorized-distance transformation
 -> global minimum-diameter optimality or a unit triangle.
```

This is not a rejection of canonical source KKT, stress, or mixed-rigidity inputs.
The constructed sources explicitly fail the KKT tensor identity. It demonstrates
why source globality must contribute more than population and stability under one
large transformation family.

## 2. Precise unbounded statement

Put `a0=sqrt(3)/2` and

```math
\kappa_0=\frac{3\pi}{5a_0}\left(\frac{3a_0}{16}\right)^{2/3}.
```

For every fixed `theta` with `131/208<theta<2/3`, there are constants `C,D0`
such that for every `D>=D0` there is a planar source `A_D` with the following
properties.

1. It is unit-separated, triangle-free, and has actual diameter exactly `D`.
2. Its **actual** unit-contact graph consists of two disjoint edges. Its actual
   diameter graph consists of two crossing edges on the same four labels.
   Every other source label is a contact isolate and is retained.
3. Its population `n_D` satisfies

   ```math
   n_D-1-\frac{\pi D^2}{2\sqrt3}
   \ge\kappa_0D^{2/3}-CD^\theta.
   \tag{1}
   
   ```

4. Every finite-valued inversion/Möbius transformation, or any realized placement
   with positive endpoint-factor distances, has normalized diameter at least `D`.
5. An arbitrarily small affine contraction in one coordinate gives a same-label,
   same-cardinality, unit-separated source of diameter strictly below `D`.

Thus these sources are nonglobal. They are not local minima, are not canonical
Target C sources, and do not disprove Level I.

## 3. Dependencies and authority

The sole non-elementary input is the finite lattice comparison constructed in
canonical [Audit.243](../audits/target_c_population_excess_sharp_coefficient_independent_audit_2026-10-10.md),
`C-GLOBAL-POPULATION-EXCESS-ASYMPTOTIC-COEFFICIENT`. Its independently reconstructed
proof supplies a finite triangular-lattice subset `Y_D`, in some translate of an
open disk of radius

```math
S=D/2+c_*D^{-1/3},\qquad c_*=(3a_0/16)^{2/3}<1,
```

with diameter strictly below `D` and population at least

```math
\frac{\pi D^2}{4a_0}+\kappa_0D^{2/3}-C_\theta D^\theta.
\tag{2}
```

We use the comparison construction proved there, not an inference that every
packing obeys an all-minimizer theorem. The strict-deletion and finite perturbation
scope is also independently recorded in canonical
[Audit.245](../audits/target_c_triangle_free_lattice_competitor_reserve_independent_audit_2026-10-10.md),
`C-TRIANGULAR-LATTICE-STRICT-D-COMPETITOR-RESERVE`.
No other Target C structural premise is imported.

The new factorized-distance obstruction is the complete proof in
[the accompanying unreviewed report](global_factorized_distance_barrier_2026-10-12.md).
The KKT failure uses the canonical tensor identity (4.4) in
`docs/theory/01-local-structure.md` only to classify these examples as nonglobal;
their strict affine competitors already prove that directly.

## 4. Construction and complete proof

### 4.1 Open the comparison contacts with a finite uniform scaling

Choose a sufficiently small `eta_D>0` and uniformly scale `Y_D` about the disk
center by `1+eta_D`. Since its diameter was strictly below `D`, its diameter
remains strictly below `D`. Every lower distance becomes strictly greater than one.
Choose the scale still smaller if needed so the resulting packet `X_D` lies in

```math
B_R(0),\qquad R=D/2+\delta,\qquad\delta=2c_*D^{-1/3}.
\tag{3}
```

This scaling is separate for each finite packet. There is no source-uniform
lower bound on its size. Its cardinality still obeys (2).

### 4.2 Insert four exact active labels

Let `L=sqrt(D^2-1)` and introduce

```math
q_1=(-L/2,-1/2),\quad q_2=(-L/2,1/2),\quad
q_3=(L/2,-1/2),\quad q_4=(L/2,1/2).
\tag{4}
```

Each has norm `D/2`. Their only unit pairs are `q1 q2` and `q3 q4`, and their
only diameter pairs are `q1 q4` and `q2 q3`. The two horizontal distances are
`L`, strictly between one and `D` for sufficiently large `D`.

Delete from `X_D` every point whose distance from any `q_i` is at most one or
at least `D`. All ties are deleted. The first type removes at most 36 points:
unit-separated centers in one closed unit disk have disjoint radius-1/2 open
disks contained in the radius-3/2 disk, so there are at most nine per `q_i`.

The second type removes only `O(D^(1/3))` points. Here is the full geometric bound,
which uses separation alone and does not assume uniform lattice discrepancy for
varying caps.

Fix `q=(D/2)e`, `|e|=1`, and write `x=-u e+v e_perp`. If `|x|<=R` and
`|x-q|>=D`, then

```math
u\ge D/2-\delta-\delta^2/D,
\qquad u\le D/2+\delta.
```

For large `D`, when `delta<=D/4`, this places `u` in an interval of length
at most `3delta`. Also

```math
v^2\le(D/2+\delta)^2-(D/2-\delta-\delta^2/D)^2
\le4D\delta.
```

The bad set lies in a rectangle with side lengths `3delta` and
`4sqrt(D delta)`. Its unit-separated points have disjoint radius-1/2 disks
inside the rectangle enlarged by 1/2 in each coordinate. Therefore their number
is at most

```math
\frac4\pi(3\delta+1)(4\sqrt{D\delta}+1)=O(D^{1/3}).
\tag{5}
```

Repeat for the four `q_i`. Add arbitrary deletions if necessary so at least four
packet labels are deleted. There remain `|X_D|-O(D^(1/3))-O(1)` packet labels.
Let `A_D` be those remaining labels together with the four `q_i`.

Every packet pair has distance strictly between one and `D`, and every
packet/quartet pair has the same strict lower and upper bounds by the deletion
rule. Thus the actual contact and diameter graphs are exactly those in item 2.
The full source is triangle-free, its minimum distance is exactly one, and its
actual diameter is exactly `D`.

Combining (2) and (5) proves (1), since `theta>1/3`; the loss of the one integer
in `n_D-1` is absorbed into the fixed error constant. This preserves the leading
coefficient `kappa0`, not merely the exponent.

The original independent packet has at least `n_D` labels, because at least four
were deleted before adding the quartet. Any `n_D` labels of `X_D` already give
a strict-sub-`D` competitor.

### 4.3 The factorized barrier survives the entire interior population

Give the two quartet contacts weight `1/2` each and the two quartet diameter
pairs weight `1/2` each. Every quartet vertex has incidence `1/2` in each
weighted graph; every other source label has zero incidence in both. The weighted
product theorem in the companion report applies to the **full source**, proving
item 4. There is no restriction on the number of contact isolates.

### 4.4 A direct full-source affine escape

Map every source label `(x,y)` to `(alpha x,y)`, with `alpha<1` sufficiently
close to one. The two active unit contacts are vertical, so their lengths stay
exactly one. Every other lower pair had positive strict slack, and the source is
finite, so all those lower bounds persist for a common sufficiently small
contraction. Every pair distance is nonincreasing under this map, while both old
diameter pairs shorten strictly from `D` to

```math
\sqrt{\alpha^2(D^2-1)+1}<D.
```

All previously inactive upper pairs remain strictly below `D`. Thus the actual
full-source maximum is strictly below `D`, and all `n_D` labels are retained.
This proves item 5 without an independent packing-number upper bound.

### 4.5 The missing global premise is visible, rather than hidden

The contact tensor has zero horizontal entry, since both actual contacts are
vertical. Every normalized convex combination of the two diameter tensors has
horizontal entry `D^2-1>0`. Thus no nonnegative normalized KKT stress can satisfy
the canonical tensor identity. These are explicitly nonglobal, nonstationary
sources. The theorem does not counterfeit the source hypotheses of Target C.

## 5. Exact finite certificates

Run `python3 research/verify_global_dense_factorized_barrier.py`. It reconstructs
four actual examples with `D^2=M^2+1`, at `M=32,64,96,128`, using rational lattice
indices, a rational translated phase, and the physical triangular basis. The
quartet has rational coordinates. Every mixed squared distance is in `Q(sqrt(3))`.

The checker certifies all source-pair classes:

- All lattice-packet lower pairs follow from the nonzero integral lattice norm and
  the strict rational scaling `1+M^-4`.
- All lattice-packet upper pairs are certified by an explicit vertex cover of
  every conflict at integral squared distance at least `M^2+1`. Every possible
  conflict has both endpoints in the exact finite outer band; points outside that
  band cannot form a conflict by the triangle inequality.
- Every quartet/packet pair and every quartet pair is checked explicitly in exact
  arithmetic, both before and after the rational affine contraction `alpha=1-M^-8`.
- A full-source factorized graph certificate includes all contact-isolated labels.
- Rational Machin-series bounds for pi and the exact lower bound
  `989/571<sqrt(3)` verify that each finite source satisfies the stronger inequality
  `n-1-pi D^2/(2sqrt(3))>kappa0 D^(2/3)`.

The finite checks are not the proof of the unbounded theorem. Its population input
is the canonical analytic comparison construction; its new cap-loss and source
replacement steps are proved above.

## 6. Frontier effect and disposition

**Recommendation:** preserve as an unreviewed regression. No canonical state
changes and no Level I closure.

The transformation barrier is compatible with the exact leading population scale
of genuine global minimizers, including the sharp coefficient. Source globality
still has to enter through genuine equilibrium/finite optimality or a different
whole-source mechanism. The remaining research objective retains every sufficiently
large global minimizer; none of this report's sources is substituted for one.

## Autonomous audit (2026-10-15)

The [PR #960 AI proof audit](../audits/pr960_autonomous_proof_audit_2026-10-15.md)
records the full argument, dependencies and computational repairs. The checkers
require assertions and refuse optimized Python. This remains noncanonical;
the destination independent exact-head AI-agent mathematical audit required for consequential promotion is not completed.
