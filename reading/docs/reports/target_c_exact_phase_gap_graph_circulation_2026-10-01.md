> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_gap_graph_circulation_2026-10-01.md) · source SHA-256 `fa1c1ff87341ed06619f97a8941d9ebcbe5b1f4578488a9ae1128be5e257a681`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B7659CDF9C23","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- exact-phase gap graph KKT circulation

Date: 2026-10-01
Base main: 14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79
Status: proof-only; C-II remains open.

## Theorem

On an exact-phase retained O--O shore, write every nonzero diameter-derivative row as

M_h = c_h 1_[a_h,b_h],  c_h != 0,

and let Gamma_u have gap vertices 0,...,m and edge {a_h-1,b_h}. Current main proves
Gamma_u is connected.

Choose the canonical relative-interior KKT stress, so beta_h>0 for every actual
diameter edge, and put w_h=beta_h c_h. Then w_h!=0 and

sum_h w_h (e_{a_h-1}-e_{b_h}) = 0.                 (1)

Therefore Gamma_u supports a nowhere-zero real circulation. In particular Gamma_u
has no bridges. Hence every nonempty proper gap-vertex cut is crossed by at least two
transversely active diameter rows, with both signs of the signed KKT cut flux.
Consequently every gap vertex has degree at least two and

|E(Gamma_u)| >= m+1.                                (2)

This strictly strengthens the previous connectivity theorem: a path or star cannot be
the full transversely active gap graph, and a leaf of a chosen spanning-tree basis is
never private in the full active system.

## Proof

For each selected train shear coordinate j, all positive-contact lengths have zero
first derivative. KKT virtual work gives

sum_h beta_h M_h = 0 in R^m.                        (3)

Apply the discrete-difference isomorphism already used on main,

L(1_[a,b]) = e_{a-1}-e_b.

Equation (3) becomes (1). If e were a bridge, let S be one component after deleting
e. Pair (1) with the indicator of S. Every internal edge cancels and the only
remaining term is plus or minus w_e, contradicting w_e!=0. The same cut calculation
gives the two-signed cut-flux statement. Since Gamma_u is connected and loopless,
minimum degree is at least two, proving (2).

## Hub refinement

The usual diameter-thrackle/Helly argument also applies to the same selected path.
Two actual diameter support intervals intersect: shared-endpoint edges share an
endpoint region, while vertex-disjoint diameter chords cross, and disjoint support
intervals would put their endpoint pairs into two disjoint boundary intervals,
contradicting alternating hull order. Thus all support intervals contain one common
gap/region index k.

Therefore every gap edge incident with j<k starts at j, and every gap edge incident
with j>k ends at j. Combined with the circulation theorem, every nonhub internal
interface has a completely one-sided switching bundle toward the hub, at least two
transversely active switching rows, and exact cancellation of the original
KKT-weighted transverse endpoint flux with both signs.

## Relation to the earlier chain-prefix circulation

The circulation mechanism is not new in isolation: the older special chain-face report
`target_c_chain_prefix_kkt_circulation_2026-09-01.md` applies the same
KKT-plus-discrete-derivative conversion to its chain-prefix interval graph. The new
point here is that current main has now identified the exact-phase fixed-star
derivative matrix itself with the gap graph Gamma_u and proved that graph connected.
Applying the circulation mechanism at this new scope upgrades the current main
connectivity statement to connected-and-bridgeless, rules out the path/star full-graph
regressions named in the preceding report, and invalidates a descent based on a
private spanning-tree leaf.

## Remaining bottleneck


The exact-phase branch is now a connected bridgeless hub-spanning interval multigraph
with a nowhere-zero KKT circulation. The next step is to combine one circulation
cycle with the convex diameter-thrackle endpoint order and the transverse complete
O--O shore.

No computation, verifier execution, CI result, or unexecuted verifier code is used.
