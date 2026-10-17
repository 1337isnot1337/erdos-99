> Generated reading edition · [exact source](../../../docs/audits/target_c_near_triangular_curved_wall_capacity_independent_audit_2026-10-06.md) · source SHA-256 `3dfb22d35095db8a7e5b1a26dbe52a4ef324dcdc5c41453c0e68b537798097b3`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E82433421949","canonical":true,"claim_ids":["C-CURVED-WALL-OLER-POPULATION-BOUND","C-NEAR-TRIANGULAR-CURVED-WALL-EXCLUSION"],"claim_statuses":{"C-CURVED-WALL-OLER-POPULATION-BOUND":"canonical","C-NEAR-TRIANGULAR-CURVED-WALL-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent promotion audit — near-triangular curved-wall capacity exchange

**Date:** 2026-10-06
**Audit base:** `e36344063111dd267668945119049f46e9d004da` (`2026-10-06.audit.67`)
**Audited source snapshot:** `research/sol/target-c-owner-order-closure-20261006` at
`91b61011eb3db25f5d603492f78d124cad9eed65`
**Candidate:** `docs/reports/target_c_near_triangular_curved_wall_exact_capacity_exchange_2026-10-06.md`
**Verdict:** PASS for the finite Oler population bound and the conditional whole-interior exchange, under the exact curved-wall and strict-area hypotheses.
**Frontier effect:** excludes a nonempty family of curved-wall chambers at every fixed size; does not establish that a canonical source contains such a wall. C-II and Level I remain open.

## Exact promoted statements

### C-CURVED-WALL-OLER-POPULATION-BOUND — PASS

Let `F` be a convex wall with `4M` actual unit edges, `M>=4`, and area

`area(F) < (sqrt(3)/2)(M^2+1)`.

Let a unit-separated source contain all `4M` wall vertices and let `z` be its
number of points strictly inside `F`. No source point can lie in the relative
interior of a wall edge: each edge has length one and such a point would be
less than one from an endpoint. Therefore the points of the source in `F` are
exactly the wall vertices and the `z` interior points. Apply the canonical
finite Oler inequality (Theory 03, Lemma 21.1) to these `4M+z` points. Since
`per(F)=4M`,

`4M+z <= (2/sqrt(3))*area(F) + 2M + 1`
`      < M^2+1 + 2M + 1 = (M+1)^2+1`.

The left side is an integer, so `4M+z <= (M+1)^2` and
`z <= (M-1)^2`. The strict area hypothesis is essential to this exact
rounding: at equality, the Oler line only yields `z <= (M-1)^2+1`.

### C-NEAR-TRIANGULAR-CURVED-WALL-EXCLUSION — PASS

For every `M>=4`, there is a nonempty parameter family of the already audited
curved unit walls with `u dot v=c` in `(0,1/2)`, sufficiently small positive
curvature, and

`area(F_theta) < (sqrt(3)/2)(M^2+1)`.

For each such wall, let `B` be the bank of `4 floor((M-1)/3)` selected wall
vertices and let `N=(M-1)^2`. The prior audit.67 construction supplies `N`
strictly interior unit-separated packet sites, roots for all `b in B`, strict
separation of every site/root pair, pairwise root distance greater than two,
and strict clearance from the old wall vertices. The Oler bound above proves
that any actual source inside this wall has `z<=N` interior points.

Now let the old source be a contact-minimal triangle-free global minimizer
containing the complete wall. Delete its `z` actual interior points and the
selected vertices `B`. Place the `z` interior labels at any `z` distinct
packet sites and replace each deleted wall vertex by its root. This is a
same-cardinality exchange. The packet sites are in the wall-safe region, so
the canonical embedded-wall shield gives strict separation from retained
exterior source points. Each root separately satisfies the one-deleted-vertex
wall shield with its own old vertex removed. Analytic packet checks give every
new-to-new lower constraint. Thus every full-source lower constraint holds
and no new contact appears; retained old-old distances are unchanged.

All inserted points lie in `int(F_theta)`, hence in the interior of the old
full-source convex hull. Every pair involving an inserted point is therefore
strictly shorter than the old actual diameter `D`, including pairs with
retained contact isolates. The roots open at least `2|B|` distinct original
wall contacts. The old contact graph is only vertex-deleted and the inserted
points are contact-isolated, so triangle-freeness is preserved. If the new
diameter is below `D`, global minimality fails; if it equals `D`,
contact-minimality fails. Consequently no canonical source contains a wall
from this stated family satisfying the strict area hypothesis.

This theorem replaces all old interior points. It does not assume that they
are isolates, near the explicit lattice, mutually contact-free, or free of a
blocking collar. The capacity comes from the explicit packet; Oler supplies
only the exact upper bound on the old count.

## Independent checks and scope

The analytic nonvacuity argument chooses `Q=10^6 M^4`,
`p=floor(sqrt(floor(Q^2/3)))+1`, `T=p/Q`, and
`c=(1-T^2)/(1+T^2)`. Then `T>1/sqrt(3)`, `T-1/sqrt(3)<=1/Q`, and
`0<1/2-c<=2/Q`. With `s=2T/(1+T^2)` and `a0=sqrt(3)/2`,
`0<s-a0<1/2-c`, so `M^2(s-a0)<2/(10^6M^2)<a0`. The zero-curvature
parallelogram therefore has strict area slack. Continuity preserves that
slack for positive curvature small enough to meet the already proved packet
conditions. This gives a nonempty chamber for every fixed `M`; it is not a
canonical-source extraction theorem.

The independent exact verifier is
`research/verify_target_c_near_triangular_curved_wall_capacity_audit_2026_10_06.py`.
It uses rational arithmetic, imports the already canonical audit.67 geometry
checker, and certifies seven instances `M=4,5,6,7,8,9,12`. It checks the
shoelace area threshold by squaring positive rational quantities, every old
and new pair, every moved-point upper pair against the actual old diameter,
all integer population ledgers through `(M-1)^2`, and the strict one-integer
cutoff. Across these instances it checks 26,508 old and 26,508 new source
pairs and 327 old-population values. The certificate proves those finite
packets only. Oler, the wall shields, and the all-`M` continuity argument are
analytic inputs and are not inferred from the samples.

The audit uses the canonical Oler inequality in
`docs/theory/03-oler-shell.md`, the canonical `C-EMBEDDED-WALL-REFILL` and
`C-ONE-VERTEX-CONVEX-WALL-SHIELD`, and the audit.67 curved-wall packet theorem.
The exact D(8) heptagon-plus-center regression is outside this four-side
curved-wall scope. No arbitrary canonical chamber is shown to satisfy the
four-side direction pattern or area threshold; no asymptotic C-II closure
follows.
