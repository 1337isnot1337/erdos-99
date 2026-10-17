> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_support_caps_2026-10-01.md) · source SHA-256 `6d89b921ff73d7aa260107c54e8953a11f78d9db959a472056656fe63bc15a01`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-6085FC666894","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — exact-phase support caps force one common diameter-cut pivot

**Date:** 2026-10-01<br>
**Starting local HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`<br>
**State version:** `2026-09-14.audit.51`<br>
**Branch/mission:** `swarm/gap-thrackle-20261001`; exact-phase gap graph plus actual diameter geometry.<br>
**Classification:** proved candidate awaiting promotion; application conditional on the explicitly unpromoted fixed-star extraction.<br>
**Level I:** OPEN; C-I CLOSED; C-II OPEN.<br>
**Literature:** no external theorem imported.<br>
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.

```text
support-cap localization -> every nonempty exact-phase diameter interval shares
one actual train-cut pivot, and almost all edge-disjoint axial reaction bundles
are internally vertex-disjoint -> a remaining crossing-pair/unit-cut compatibility
theorem would give a source-preserving competitor or contradiction -> Level I
only after every other C-II branch is covered.
```

The last implication is an obligation, not a theorem of this report.

## 1. Inputs and scope

Canonical inputs actually used are the diameter-thrackle property recorded in
`C-WOODALL`, the positive full-support normal form, and the degree bound
`Delta(H)=O(D^(3/4))` in Section 58, FS.5. The positive-contact-core convention of
Section 57 remains in force. No source point is removed and no motion is claimed.

The application uses the following **unpromoted** October 1 reports:

- [complete O–O rectangle](target_c_oo_dual_tree_complete_rectangle_2026-10-01.md);
- [common witness cell](target_c_local_witness_cell_2026-10-01.md);
- [rank switching](target_c_complete_grid_rank_switching_2026-10-01.md);
- [joint switch budget](target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md);
- [axial reaction dichotomy](target_c_witness_cell_blocker_dichotomy_2026-10-01.md);
- [gap graph](target_c_exact_phase_gap_graph_connectivity_2026-10-01.md).

Their source-level extraction is assumed explicitly. The geometric lemmas below
are proved here from their stated hypotheses, including the one-arc order step;
they do not silently import an older branch's audit as canonical mathematics.

Let `F` be the convex hull of the actual diameter endpoints. Work with `m`
pairwise disjoint proper crosscuts ordered on one complement-dual path. Their
boundary layer labels are `0,...,m`. In cyclic order the layer blocks are

```
0, 1+, 2+, ..., (m-1)+, m, (m-1)-, ..., 2-, 1-.
```

Each internal layer has two boundary arcs; each exterior layer has one cap arc.
Orders here are the orders of diameter endpoints, which agree with their convex
hull order. Other source vertices, including isolates, are not assumed to lie in
the contact core or in `F`.

For a diameter `xy` with different layer labels `p<q`, its selected-cut support is
`[p+1,q]`. At an internal layer `i`, the switching set consists of all diameters
with one endpoint in layer `i` and the other in a different layer. Orient each
switching vector `n_h` from outside this layer into it.

The exact-phase hypotheses are:

1. all coherently oriented train directions equal a unit vector `u`;
2. two fixed full-span actual diameters have a common endpoint `v`, and their
   transverse projections relative to `u` have opposite strict signs;
3. no switching diameter is parallel to `u`;
4. for every nonempty switching set, positive weights satisfy
   `sum beta_h n_h = G_i`, where `G_i` is parallel to `u`.

The witnesses in (2) have endpoint labels `0,m`. Their common endpoint is in
one exterior cap; their other endpoints are in the other cap. In the open-cell
case (3) follows because `u` is not a diameter direction. In the threshold case
the unique parallel diameter has full support, so cannot switch internally.

Only the transverse identity `sum beta_h(n_h dot Ju)=0` is needed for the
one-sided-gap theorem. Reaction nondegeneracy is not needed there.

## 2. Strict diameter normals and support-cap localization

**Lemma 1 (strict normal).** If `xy` is an actual diameter and `r=x-y`, then
`r` strictly exposes `x` in the source hull and in `F`.

For any different source point `z`, expand `|z-y|^2<=|x-y|^2` to obtain

```math
2r\cdot(z-x)+|z-x|^2\le0.
```

Thus `r dot (z-x)<0`. In particular `r` lies in the interior of the normal
cone at `x`. The same argument applies to `-r` at `y`. This also proves that
every diameter endpoint is an extreme vertex.

**Lemma 2 (both axial support directions are exterior).** Under hypothesis 2,
the normal direction `u` occurs in one exterior cap's normal sweep and `-u`
occurs in the other. Neither direction occurs in the normal sweep of any
internal layer arc.

Orient both common-star witnesses from `v` toward their other endpoints,
giving `r_-` and `r_+`. Diameter neighbors of one point lie in a cone of
aperture at most `pi/3`: their mutual distance is at most `D`, while both
distances from `v` are `D`, so the chord formula gives the bound.

Opposite strict transverse signs imply that one of the two rays `t=u` or
`t=-u` lies strictly between `r_-` and `r_+` in this ordinary cone. At `v`,
both `-r_-` and `-r_+` are strict normal directions. Their positive cone
therefore contains `-t` in the interior of `N_F(v)`. Consequently `-t`
uniquely exposes `v`.

The other witness endpoints `x_-,x_+` are in the opposite exterior cap.
Their strict normal directions are `r_-,r_+`. The outward Gauss direction
increases in the cyclic order of a convex polygon. The cap arc containing
`x_-,x_+` cannot sweep through `-t`, because that direction occurs uniquely
at `v`, outside the cap. It must therefore sweep through the short interval
between `r_-` and `r_+`, which contains `t`. This locates both axial normal
directions in the two exterior caps.

Normal sweeps of disjoint cyclic vertex intervals have disjoint interiors;
adjacent sweeps can meet only at a separating edge normal. The two axial
directions above are interior to their exterior-cap sweeps: `-t` is inside
the normal cone at `v`, and `t` is strictly between the strict normals at
`x_-` and `x_+`. Hence no internal arc's sweep contains either axial direction.

This proof uses `F`, rather than identifying the entire contact outer boundary
with the full source hull. Isolated source points introduce no omitted premise.

## 3. No internal gap has both left and right neighbors

**Theorem 3.** Under the four exact-phase hypotheses, every internal layer's
nonempty switching set has one switch orientation only. All its other endpoint
labels are either strictly smaller, or all are strictly larger. Moreover its
switching middle endpoints occur on both of its boundary arcs.

Suppose both orientations occur at layer `i`. Write the four boundary blocks
relative to its two bounding cuts as

```
L, M+, R, M-.
```

A diameter joining `L` to `M+` cannot coexist with one joining `R` to `M-`:
their four endpoints are distinct and occur in nonalternating cyclic order,
so the chords do not cross. The diameter-thrackle property forbids this.
The same argument forbids `L–M-` together with `R–M+`.

Choose one left and one right switching edge. They must use the same middle
arc. That right edge forbids every left edge from using the opposite arc;
that left edge forbids every right edge from using the opposite arc. Thus
all switching middle endpoints lie on one common arc.

By Lemma 1, every `n_h` is a strict outward normal at its middle endpoint.
By Lemma 2, the normal sweep of this internal arc avoids both `u` and `-u`.
It is connected, so lies wholly in one of the two open semicircles cut out
by those directions. Therefore all `n_h dot Ju` have the same strict sign.
Their positive weighted sum cannot have zero transverse component,
contradicting hypothesis 4. Mixed orientation is impossible.

The identical normal-sign argument shows that even a one-orientation
switching set cannot have all its middle endpoints on one arc. Therefore
both internal boundary arcs are occupied.

The argument does not equate switch orientation (left/right endpoint label)
with transverse sign. Opposite transverse signs persist in each one-sided
packet. Confusing these two notions would produce a false closure.

## 4. Gap graph consequences and the surviving odd cycle

**Corollary 4.** The connected exact-phase gap graph is bipartite. Every
internal vertex is an order extremum of its neighbor set. The full diameter
graph can have same-layer diameter edges in at most one layer. If it has
an odd cycle, that cycle contains a same-layer diameter edge.

Assign a nonisolated gap vertex to `L` if all its neighbors have larger labels,
and to `R` if all have smaller labels. Theorem 3 makes this well defined for
internal vertices; exterior vertices `0,m` belong respectively to `L,R`.
Every edge `p<q` then joins `L` to `R`. Connectivity from the unpromoted rank
theorem removes isolated gap vertices, proving bipartiteness. The possible
parallel-to-`u` full-span diameter also joins `0` to `m`, so adding its zero
derivative row does not affect this coloring.

For two different layer labels, the boundary vertices of one layer do not
alternate with the boundary vertices of the other: the displayed layer-block
order is nested. Thus a diameter with both endpoints in one layer and a
diameter with both endpoints in a different layer would be vertex-disjoint
noncrossing chords. This is forbidden. Only one layer can contain such edges.

Pull the gap coloring back to the actual diameter vertices. Every edge whose
endpoint labels differ joins opposite colors. An odd cycle cannot consist
solely of such edges, so it contains a same-layer edge. This is compatible
with the canonical odd-unicyclic Woodall branch; it does not exclude it.

## 5. Almost all independent reaction bundles are CROSS

**Theorem 5.** Consider any family of pairwise edge-disjoint two-bar axial
reaction bundles at internal exact-phase layers:

```math
G_i=\lambda_i^- n_i^-+\lambda_i^+n_i^+\ne0,
\qquad \lambda_i^\pm>0,
```

with opposite strict transverse signs. If the two bars in a bundle share an
endpoint, their common endpoint is outside the layer and strictly exposes
one of the two axial directions `u,-u`. Consequently all such centers belong
to at most two fixed vertices, and the number of STAR bundles is at most
`Delta(H)`.

If the common endpoint were the middle endpoint, both strict normals would
be in its normal cone. Their positive combination `G_i`, a nonzero axial
vector, would be in the interior of that cone. This would put an axial
support direction in an internal arc, contrary to Lemma 2.

If the common endpoint is exterior, the two strict normals there are
`-n_i^-,-n_i^+`. Their positive combination is `-G_i`, so that vertex strictly
exposes `u` or `-u`. For each direction there is at most one strictly exposing
vertex. If the corresponding support face is an edge, it has no such vertex.

Each STAR bundle consumes two different incident edges at its center. Edge
disjointness gives at most

```math
\frac{\deg(v_u)+\deg(v_{-u})}{2}\le\Delta(H)
```

STAR bundles, treating a nonexistent exposing vertex as degree zero.

The unpromoted October 1 packet selection supplies a linear edge-disjoint
family. Canonical FS.5 gives `Delta(H)=O(D^(3/4))=o(D)`. Hence deleting only
`o(D)` bundles leaves a **linear** family whose two bars are internally
vertex-disjoint. There is no need for a CROSS/STAR pigeonhole at this step.

Different bundles may still share exterior vertices. The existing degree
thinning yields a fully vertex-disjoint family only of order `D^(1/4)`.
No stronger cross-bundle matching claim is made here.

## 6. Frontier effect and next attack

The exact-phase branch is sharpened to

```
connected bipartite ordered gap graph;
one common actual train-cut pivot for all nonempty diameter supports;
every internal gap is left-only or right-only;
each switching packet uses both middle boundary arcs;
an odd diameter cycle has a same-layer edge in one exceptional layer;
a linear independent packet family is CROSS after an o(D) deletion.
```

This rules out the proposed closure via repeated mixed left/right cusps and
reduces the internal STAR alternative. It does not eliminate a one-sided
connected gap graph. In particular, a tree basis does not make a private
basis leaf free of the other actual diameter constraints.

The next attacks were performed in the
[odd-shell regression](target_c_odd_shell_gap_regression_2026-10-01.md) and the
[joint cut-stress test](target_c_unit_cut_stress_projection_regression_2026-10-01.md).
The shell survives one- and two-shore geometry and the necessary joint scalar
PSD projection, while omitting actual contact-train cuts and their rhombus
faces. It is explicitly nonglobal. The blockwise sharpening below pushes
the geometric theorem further without reusing the refuted sufficiency claim.

The nonconstant-phase swap fork, split-star O–O branch, inactive-interface
branch, and macroscopic inactive-container/exterior-cap branch remain open.
No canonical state or prompt is promoted by this report.

The next actual contact-embedding attack is preserved in
[source-face and train-terminal localization](target_c_small_swap_face_endpoint_localization_2026-10-01.md).
It extends finite swap immunity to every opposite train crossing both
boundaries and injects an unprotected rhombus into a transverse end in the
middle slab. An exact seven-point source rejects immunity of all source
rhombi and preserves the outer-face/terminal obligation.

## 7. Self-audit

| Claim/possible shortcut | Classification | Audit result |
| --- | --- | --- |
| Strict diameter normal | Proved candidate awaiting promotion | Direct squared-distance inequality |
| Exterior axial support caps | Proved candidate awaiting promotion | Uses common-star full-span witnesses, not arbitrary full-span rows |
| No mixed gap vertex | Conditional application | Needs actual positive axial cut balance and absence of a switching parallel diameter |
| One common train-cut pivot | Conditional application | Applies the same balance to every internal slab, then finite interval Helly |
| Bipartite gap graph | Conditional application | Does not imply the actual diameter graph is bipartite; empty rows remain |
| STAR bundles are sublinear | Conditional application | Counts only an edge-disjoint packet family; uses canonical maximum degree |
| Connectivity or a tree leaf alone forces release | Rejected shortcut | Full matrix can have several rows at the same gap |
| Exact-phase branch or C-II closed | Rejected claim | CROSS/unit-cut compatibility and other source branches survive |

No numerical experiment, unexecuted code, or external theorem is used in
these proofs. The separate regression certificate checks discrete identities;
it will not certify global optimality or a contact-preserving finite move.

## 8. Next closing attack performed: all blocks, not just adjacent gaps

**Theorem 6 (common actual train-cut pivot).** Retain the exact-phase
hypotheses above and the exact slab cutset identity for any two selected
trains. Then all nonempty actual diameter support intervals have a common
selected train index `k`. Equivalently, every actual diameter with endpoints
in different selected layers crosses the same actual train shore cut `tau_k`.
In particular, the gap graph's bipartition is the contiguous split

```
{0,...,k-1} versus {k,...,m}.
```

Every internal gap below `k` is right-only; every internal gap at or above
`k` is left-only. The exact-phase support system has one global switch pivot,
rather than an arbitrary pattern of order extrema.

For a slab consisting of consecutive internal layers `p,...,q`, sum actual
KKT equilibrium over the whole slab. Its only crossing contacts are the
two boundary train contact families, with opposite boundary vectors `u,-u`.
Consequently the full moving-diameter resultant is parallel to `u`, just
as for an adjacent gap. The common full-span witnesses still have both
endpoints outside this slab, on its opposite exterior caps, and the support-cap
lemma still places both axial normal directions outside the slab's two middle
arcs. Parallel diameters do not move because their support is full-span.

If there are moving diameters to both the left and right of this slab, the
same four-block thrackle proof as in Theorem 3 puts all their middle
endpoints on one arc. All their inward vectors then have the same strict
transverse sign, contradicting the slab's axial balance. Thus **no internal
contiguous slab has diameter neighbors on both sides**.

Suppose two nonempty diameter supports are disjoint. Write their endpoint
labels as `a<b<=c<d`; their supports are `[a+1,b]` and `[c+1,d]`. The
slab of layers `b,...,c` is internal, because `b>=1` and `c<=m-1`.
The first diameter connects it to the left and the second to the right,
contradicting the preceding block theorem. Therefore all nonempty supports
are pairwise intersecting. For finite intervals, pairwise intersection means
`max(left endpoints)<=min(right endpoints)`. Any integer between these
two values is the required common index `k`.

Every support `[a+1,b]` then has `a<k<=b`, giving the contiguous gap
bipartition and the stated one-sided switching order. There is no Euler-path
inference, and the graph may still have parallel rows and many cycles.

The exact slab contact identity is the one used in the unpromoted
[arbitrary block-transposition theorem](target_c_open_cell_block_transposition_2026-10-01.md),
Section 1. No finite transposition is needed here; it supplies the actual
contact-cutset input for this equilibrium sum.

If both shores are exactly constant, there are two such pivot trains. They
cross in one actual retained rhombus. Every diameter with nonempty support
on both shores crosses both pivot cuts in the **endpoint-incidence sense**.
This does not assert that its straight segment passes through that rhombus.
Each shore can still have empty-support diameters in its one exceptional
layer; those edges are retained in the full source graph.

The regular odd-shell supports are prefixes, so they already have common
pivot 1. Thus the attempted next contradiction, that one common pivot is
geometrically impossible, is refuted by the existing exact regression. The
genuine remaining bridge is source-level: constrain the actual unit-train
extensions, their rhombus faces and the exceptional empty-support layers,
or construct a finite strict competitor. No claim of closure follows from
Helly intersection alone.

## 9. Nonconstant phase: mixed slabs force the inactive fork

**Theorem 7.** Work instead in one common **open** witness cell, with
possibly varying retained train directions. Choose any two boundary trains
`tau_p,tau_q`, `p<q`, with distinct directions, and their finite block
transposition from the October 1 report. If moving actual diameters connect
the slab to both its left and right exterior regions, the transposition is
ONE-SIGN. It therefore forces a previously strict source pair within
`4K/D` of contact or diameter activity, outside the protected boundary
rhombus diagonals. Conversely, a TWO-SIGN active obstruction can only use
one exterior side and must occupy both middle boundary arcs.

Let `a` be the projective midpoint of the two boundary directions. The
fixed common-star witnesses bracket the whole open cell. Lemma 2 therefore
applies to `a`: the two normal directions `a,-a` lie in the exterior caps
of this slab. This is a statement about the fixed witness cone, independent
of whether the other retained directions equal either boundary direction.

Mixed left/right moving diameters have all their middle endpoints on one
arc by the four-block thrackle argument. Its normal sweep avoids `a,-a`,
so all moving inward diameter vectors have one strict sign against the
swap axis `w=+/-Ja`. The exact block-swap KKT identity gives
`G dot w=(s/2)(A_p+A_q)>0`; hence the common sign is positive. This is
ONE-SIGN. The finite non-grazing estimate and endpoint minimality argument
of the block-transposition report then give the inactive near-activity pair.
That report's local-immunity theorem excludes retained boundary-grid
rhombus diagonals from the witness.

If TWO-SIGN holds, the preceding argument rules out mixed left/right
orientation. A one-arc middle packet would again have only one transverse
sign, so both middle arcs must be occupied. This proves the converse.

**Corollary 8 (nonconstant disjoint supports).** If two nonempty actual
diameter support intervals are disjoint, their intervening internal slab
has diameter neighbors on both sides. Its boundary train directions cannot
be equal, because the axial-balance proof of Theorem 6 would contradict
the one-arc normal signs even if the intervening train phases vary.
Therefore those two boundary phases differ and Theorem 7 forces the
nonlocal inactive near-activity witness.

Consequently a shore with no such inactive source pair has a common
actual diameter-cut pivot even in nonconstant phase. No uniform inactive
slack is asserted for a canonical source. Near-active pairs are strict
pairs, not newly promoted contacts, positive multipliers, or exact triangles.

This sharpens the current finite fork by attaching an exact support-order
label to each branch. It leaves the one-sided TWO-SIGN mechanism and the
nonlocal inactive witness mechanism unresolved; it does not dismiss them.
