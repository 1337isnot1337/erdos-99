> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_fixed_angle_reaction_braid_2026-10-01.md) · source SHA-256 `b4cd53e128b8512a7ba29da1e0c7d3d15e7f3e238651cad417f06d7c96b5665a`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E1B5750443B2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- fixed-angle reaction braid on an exact-phase shore

Date: 2026-10-01
Base main: 5ff8caddec4bd2b56b1934abe8602f071b0c61ba
Status: proof-only, unreviewed. C-II remains open.

## Theorem

Assume the current fixed-star complete O--O rectangle and fix one retained shore on
which all retained train directions have the same coherent unit direction u. Let S
be its active adjacent interfaces. The exact-phase clause of the current rank-switching
theorem gives

    |S| >= (c_* - o(1)) D.

At each i in S the current witness-cell blocker theorem is in its exact-direction TB2
case. Thus the nonzero strip reaction is axial,

    G_i = rho_i u, rho_i != 0,

and has an exact positive representation by two actual switching diameter vectors

    G_i = lambda_i^- n_i^- + lambda_i^+ n_i^+,
    lambda_i^-, lambda_i^+ > 0,
    |n_i^-| = |n_i^+| = D.

No selected switching diameter is parallel to u, and the two vectors have opposite
strict transverse signs.

Set e_i = G_i/|G_i| in {u,-u}. Positive coefficients and the exclusion of a
parallel switching bar put e_i strictly inside the positive cone of the two selected
vectors. Let theta_i in (0,pi) be the ordinary opening angle of that cone. Put

    rho_* = min(c_*/16, pi/8).

Then, for all sufficiently large D:

1. at least (3c_*/8-o(1))D active exact-phase interfaces have theta_i >= rho_*;
2. at least (c_*/8-o(1))D of these can be chosen so that the selected reaction
   pairs are pairwise edge-disjoint;
3. every pair in that family has four distinct endpoints and hence its two diameter
   bars cross properly;
4. a final degree thinning leaves Omega(D^(1/4)) pairs with mutually disjoint
   four-endpoint sets, so every diameter bar in the final family crosses every other
   bar.

All final reactions point in one common ordinary direction e in {u,-u}; every pair
retains its exact positive KKT identity. No common routing hub or one-sided
switching-half-plane theorem is used.

The angle theta_i is an ordinary oriented force-cone angle. It is not claimed to be a
projective supporting-line gap.

## Proof

There are only two oriented reaction axes, so one sign class S_e has

    |S_e| >= (c_*/2-o(1))D.

Call i in S_e narrow if theta_i < rho_*. Because e lies strictly inside the positive
cone, both inward diameter directions of a narrow pair lie within ordinary angle
rho_* of e. Since rho_* <= pi/8, their projective directions lie in one projective
interval of length at most 2 rho_*.

Canonical diameter-direction separation gives

    delta_D = 2 asin(1/(2D)) >= 1/D

between distinct actual diameter directions. Hence that interval contains at most

    2 rho_* D + 1

actual diameter directions.

Each narrow interface contributes two distinct switching-edge occurrences. The
current complete-grid joint switch theorem gives

    t_A(h) + t_B(h) <= 2

for every actual diameter edge h. In particular one fixed edge can occur in the
switching support of at most two interfaces on this shore. Distinct diameter edges
have distinct projective directions by parallel-diameter uniqueness. Therefore if
N_nar is the number of narrow interfaces, its 2 N_nar edge occurrences use at least
N_nar distinct directions. Since 2 rho_* <= c_*/8,

    N_nar <= 2 rho_* D + 1 <= (c_*/8)D + 1.

Subtracting from |S_e| leaves at least (3c_*/8-o(1))D wide interfaces.

Now choose one two-bar certificate at each wide interface and join two interface tags
when the chosen certificates share an edge. Each chosen edge can occur at only one
other interface, and a certificate has two edges. The conflict graph has maximum
degree at most two. A greedy independent set keeps at least one third, proving the
(c_*/8-o(1))D edge-disjoint family.

It remains to rule out a shared endpoint inside one wide pair. The audited adjacent
switching topology says every switching edge has exactly one endpoint in the physical
middle layer M_i, and its inward vector points from the exterior endpoint toward the
middle endpoint. If two selected bars share a vertex, that vertex is either the
middle endpoint of both or an exterior endpoint of both; it cannot have different
layer roles. A left-switch and right-switch edge also cannot share an exterior
endpoint because the two exterior regions are disjoint. Therefore the ordinary angle
between the two inward vectors equals the ordinary angle between two diameter rays
incident to one common source vertex, not its supplement.

Canonical full-source geometry gives uniform diameter-star angular width
O(D^(-1/4)). This is eventually smaller than the fixed rho_* > 0, contradicting
theta_i >= rho_*. Hence every wide selected pair has four distinct endpoints. The
convex diameter-thrackle property then makes its two bars cross.

Finally build a conflict graph on the edge-disjoint pairs, joining two pairs when
their four-endpoint sets meet. One pair has four endpoints. Each endpoint is incident
with at most Delta(H) actual diameter edges, so its bundle degree is at most
4 Delta(H). Canonical full-source geometry gives

    Delta(H) = O(D^(3/4)).

Greedy selection from a linear number of pairs therefore leaves Omega(D^(1/4))
endpoint-disjoint pairs. Every two diameter bars in this final family are
vertex-disjoint, so the convex diameter-thrackle property makes all bars pairwise
crossing.

## Remaining bottleneck

This removes the degeneration in which a linear exact-phase TB2 family is supported
only by arbitrarily narrow positive reaction cones. It does not exclude theta_i
approaching pi. In that near-antipodal regime the two supporting lines may still be
projectively close, so no fixed-area central diamond follows.

The next exact-phase target is to combine the ordered interface tags and exact
positive reactions with the common complete transverse O--O grid, either excluding a
growing ordered near-antipodal force braid or turning it into a source-preserving
strict diameter decrease or an exact unit triangle.

No computation, verifier execution, numerical experiment, CI result, or unexecuted
verifier code is used.

## Slot 2 recovery provenance — 2026-10-05

Source branch: `research/exact-phase-fixed-angle-reaction-braid-2026-10-01` at exact tip `bbb61ed6155b9ec220b582052a3bcf211b1cc181`. No original PR was associated with this branch. This report is preserved as an unreviewed, proof-only Target C-II candidate; it does not change the current theorem state. No standalone verifier or computational certificate was present on the source branch.
