<!-- theorem-state: {"artifact_id":"ART-6085FC666894","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — exact-phase support caps and one-sided gap vertices

**Date:** 2026-10-01  
**Starting local HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`  
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`  
**State version:** `2026-09-14.audit.51`  
**Branch/mission:** `swarm/gap-thrackle-20261001`; exact-phase gap graph plus actual diameter geometry.  
**Classification:** proved candidate awaiting promotion; application conditional on the explicitly unpromoted fixed-star extraction.  
**Level I:** OPEN; C-I CLOSED; C-II OPEN.  
**Literature:** no external theorem imported.  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.

```text
support-cap localization -> exact-phase gap graph has no internal vertex with
neighbors on both sides, and almost all edge-disjoint axial reaction bundles
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

\[
2r\cdot(z-x)+|z-x|^2\le0.
\]

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

\[
G_i=\lambda_i^- n_i^-+\lambda_i^+n_i^+\ne0,
\qquad \lambda_i^\pm>0,
\]

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

\[
\frac{\deg(v_u)+\deg(v_{-u})}{2}\le\Delta(H)
\]

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
every internal gap is left-only or right-only;
each switching packet uses both middle boundary arcs;
an odd diameter cycle has a same-layer edge in one exceptional layer;
a linear independent packet family is CROSS after an o(D) deletion.
```

This rules out the proposed closure via repeated mixed left/right cusps and
reduces the internal STAR alternative. It does not eliminate a one-sided
connected gap graph. In particular, a tree basis does not make a private
basis leaf free of the other actual diameter constraints.

The next attack in this run is an exact near-circular odd-shell realization
of the remaining graph/sign data, followed by an audit of which actual
unit-cut compatibility hypothesis it omits. That regression and its verifier
will be recorded in a separate report. A surviving shell is not a global
minimizer or a Level I disproof.

The nonconstant-phase swap fork, split-star O–O branch, inactive-interface
branch, and macroscopic inactive-container/exterior-cap branch remain open.
No canonical state or prompt is promoted by this report.

## 7. Self-audit

| Claim/possible shortcut | Classification | Audit result |
| --- | --- | --- |
| Strict diameter normal | Proved candidate awaiting promotion | Direct squared-distance inequality |
| Exterior axial support caps | Proved candidate awaiting promotion | Uses common-star full-span witnesses, not arbitrary full-span rows |
| No mixed gap vertex | Conditional application | Needs actual positive axial cut balance and absence of a switching parallel diameter |
| Bipartite gap graph | Conditional application | Does not imply the actual diameter graph is bipartite; empty rows remain |
| STAR bundles are sublinear | Conditional application | Counts only an edge-disjoint packet family; uses canonical maximum degree |
| Connectivity or a tree leaf alone forces release | Rejected shortcut | Full matrix can have several rows at the same gap |
| Exact-phase branch or C-II closed | Rejected claim | CROSS/unit-cut compatibility and other source branches survive |

No numerical experiment, unexecuted code, or external theorem is used in
these proofs. The separate regression certificate checks discrete identities;
it will not certify global optimality or a contact-preserving finite move.
