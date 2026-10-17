> Generated reading edition · [exact source](../../../docs/reports/target_c_single_gap_stationary_diameter_core_2026-10-01.md) · source SHA-256 `78815fa04f12e25ac4b6b830271333783203112aee013f6f490dbde2b0a4efb9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-AD8D52FEFF25","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — stationary diameter bars occupy one gap

**Phase 2 preservation provenance:** PR #594, branch swarm/gap-reaction-cut-20261001, audited source head 02d4cc04e2df2e0f0aa1eb2a9ec3cf21cc53f18f. Preserve its finite diameter-thrackle localization; the train-chart application remains conditional on the unpromoted boundary-order input.

`proper source boundary layers -> one gap contains every empty-support
actual diameter -> a single stationary diameter-carrying region for the
selected train chart -> remaining whole-region/source exchange -> Level I`

**Date:** 2026-10-01<br>
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`<br>
**Prior checkpoint:** `6b9cfd92`<br>
**State:** `2026-09-14.audit.51`<br>
**Mission:** push paired-gap classification into the stationary-diameter remainder.<br>
**Classification:** proved candidate awaiting promotion, with conditional train application.<br>
**LEVEL I:** OPEN. C-I closed; C-II open.

## 1. Finite source theorem

Let $`A`$ be any finite planar source of diameter $`D>0`$. Give its actual
diameter endpoints gap labels $`0,\ldots,m`$ in proper cyclic bitonic order:
one hull-boundary arc has nondecreasing labels and the other has
nonincreasing labels, with the two extreme blocks contiguous. A diameter
has **empty cut support** when its endpoints have the same gap label.

If empty-support actual diameters exist, all of them have the same
endpoint gap label $`k`$.

This statement needs no KKT stress, no exact phase, no optimality, and
no deletion of any source point. Its exact geometric input is the convex
diameter-thrackle property. Its actual-train interpretation is conditional
on the unpromoted proper nested-cut/boundary-order theorem.

### Proof

Suppose two empty-support diameters have distinct labels $`j<k`$. Their
four endpoints are distinct. If either diameter has both endpoints in
one monotone boundary arc, the subarc between those endpoints contains
only vertices with their common label. No endpoint of the other diameter
lies on that subarc, so the four endpoints do not alternate.

Otherwise both diameters join the two monotone arcs. One arc orders the
$`j`$ endpoints before the $`k`$ endpoints, and the other reverses that
order. The cyclic order is therefore $`j,k,k,j`$, again nonalternating.
The same argument includes extreme blocks by choosing the monotone-arc
split inside those blocks. Thus the two vertex-disjoint chords do not
cross, contradicting the actual diameter-thrackle property. ∎

The hypothesis is an actual hull-boundary label order. Arbitrarily
assigned interval labels do not supply it; the eight-point regression
in the predecessor report fails exactly this hypothesis.

## 2. Exact-phase refinement: only one central gap is used

In the paired antitone tree from this branch, order each simple support
edge as $`(a,b)`$ with $`a<b`$. Antitonicity implies that when $`a<c`$, the
other endpoints obey $`b\ge d`$. Together with the cases $`a=c`$, all the
closed intervals $`[a,b]`$ form one nested chain. Its shortest interval
is adjacent, say $`[r-1,r]`$, by the adjacent-contraction theorem.

Let an empty-support diameter have label $`k`$. Compare it with any paired
edge interval $`[a,b]`$. If $`k<a`$ or $`k>b`$, the empty-support chord has no
endpoint in common with either actual representative of that paired
edge. Boundary order gives nonalternating endpoints with those chords,
contradicting the diameter-thrackle property. Thus

```math
k\in\bigcap_{(a,b)}[a,b]=\{r-1,r\}.
```

Section 1 strengthens this localization: **one** of the two central gaps
contains every empty-support actual diameter. Their simultaneous
occupation by two actual empty-support diameters is impossible.

This sharpens the two-central-gap localization in the unpromoted
`target_c_star_ray_staircase_reactions_2026-10-01.md`, Section 7,
at remote commit `9953b40011ff31df00597fdd2ca7d9791fa29765` (PR #597).
Its two examples choosing either central gap separately remain valid.
No claim in that report is rejected by this refinement.

## 3. What remains fixed in the full finite contact chart

In the exact train chart,

```math
p_x(t)=p_x+z_{\ell(x)}(t),\qquad
z_j(t)=\sum_{i\le j}(R_{t_i}u-u),
```

both endpoints of an empty-support diameter translate by the same vector
$`z_k(t)`$. Its diameter is unchanged exactly, for all chart parameters;
this is a finite statement. In the canonical regime $`D>1`$, these are
precisely the actual diameters intrinsically stationary for every chart
parameter. Indeed, for nonempty support vary just one coordinate. The
identity $`|r+\sigma(R_tu-u)|^2\equiv D^2`$ would force $`r=\sigma u`$,
hence $`D=1`$. Therefore all intrinsically stationary diameter bars belong
to one gap whenever such bars exist.

There is an explicit exception to **derivative-row** terminology. A
diameter parallel to $`u`$ can have nonempty full support and zero first
variation. Its endpoints are in distinct extreme gaps, and its finite
length need not be fixed. For example, with a singleton interval and
$`r=Du`$,

```math
|Du+(R_tu-u)|^2-D^2=2(1-D)(1-\cos t),
```

which strictly decreases for nonzero small $`t`$ when $`D>1`$. This parallel
bar is not included among the empty-support stationary diameters.
No inactive pair is promoted to activity, and no source cardinality is
changed.

## 4. Checked parallel research and dependency boundary

PR #597 and the independent hostile audit PR #602 at
`004fdd2c0ccd9b3cffcd5aa5a16840d77d2b372d` were inspected.
The ray-anchor proof yields opposite physical arcs without an actual
parallel diameter. The determinant argument proves strictly positive
original axial bundles: every positive-orientation upward angle is
below every reverse-orientation upward angle; cotangent decreases,
and the original transverse flows balance separately in each bundle.
The resulting actual contact masses are strictly unimodal **when the
actual contact-cut law is supplied**.

Those audited-working claims remain conditional for the complete C-II
route and were not promoted here. In particular, the geometric examples
there certify projected balance, not full source vertex equilibrium.
The new Section-1 theorem does not require their axial conclusions.

Canonical interpretation inputs are the exact Level I statement,
C-I full-support normalization, and core-only ZR/ZF. The new geometric
theorem is proved directly. The precise remaining noncanonical source
input is the proper nested-cut order on actual diameter endpoints.

## 5. Exact finite checks

The updated `verify_ordered_gap_circulation_2026_10_01.py` enumerates
pairs of equal-layer chords in bitonic boundary label orders, checks
their disjoint/nonalternating endpoints, and rejects simultaneous
different-layer empty diameters. It separately retains the earlier
antitone-flow, shared-endpoint, and rational source regressions.

Arithmetic is exact integer/rational arithmetic. Enumeration is a
regression check of the boundary-order argument, not a global-optimality
certificate or a substitute for the arbitrary-size proof.

## 6. Exact closing obligation

If the chart has empty-support actual diameters, a closing source move
must account for one common stationary gap region; it cannot silently
discard those diameter constraints or claim strict global decrease
merely by shortening the moving rows. A diameter-pair-count contradiction
still requires all inactive source pairs to be checked after the move.

The next obligation is a whole-source exchange or deformation compatible
with that stationary region and the transverse complete shore. Neither
the paired tree nor its now-localized stationary remainder provides
such a move by itself. The nonconstant-phase, split-star, inactive
interface, macroscopic-container, and other full-core branches remain
open.

**Promotion recommendation:** unreviewed candidate. Independently audit
the proper boundary-label hypothesis before a route promotion; canonical
theorem state is unchanged.
