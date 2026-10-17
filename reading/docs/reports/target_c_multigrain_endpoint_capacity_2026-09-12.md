> Generated reading edition · [exact source](../../../docs/reports/target_c_multigrain_endpoint_capacity_2026-09-12.md) · source SHA-256 `4355729cd33db28ca806c52c8379d1db80f284f9911963f15dc104080ca9c807`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AB296D8872A8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_multigrain_endpoint_capacity_2026-09-12.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=6f5ddc991425bc027eddba8b54a7dac5b86a8c4a; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C multi-grain endpoint-capacity lemma

Status: **proved candidate awaiting hostile audit**.  This is proof-only research;
canonical theorem state is unchanged and C-II is not claimed closed.

This note attacks the multi-grain gap left by the phase-component endpoint
inequality.  The key point is that the safe Section-118 carrier has both a
quadratic rhombus mass and an unusually small total train ceiling.  Those two
facts prevent the quadratic mass from being distributed among arbitrarily many
small, phase-separated grains without forcing too many train endpoints onto the
three principal routes.

## 1. Inputs and reduction

Work in the proof-only Section-118 safe window, with a Type-II carrier whose
normalized slack is at most 0.0088.  Use the audited conservative constants

    A_4 / D^2 >= 0.4703752 - o(1),
    T / D <= 1.8488 + o(1),
    B_bad / D <= 0.1163 + o(1),
    E_route / D <= 1.8693 + o(1).

Here A_4 is the total area of strict rhombi in the carrier, T is the number
of complete local trains, B_bad is the Section-118 bad-train capacity for one
collapsed projective direction interval, and E_route is the total number of
principal-route edge occurrences.  A strict unit rhombus has area at most one,
so the carrier crossing graph has at least 0.4703752 D^2 edges.

Let delta_e be the positive reduced-phase difference across a rhombus crossing.
The canonical total angle-defect budget is

    sum_e delta_e <= 5.317 D.

Fix K = 10000.  Discard crossings with delta_e > K/D.  Fewer than
0.0005317 D^2 crossings are discarded.

On the remaining crossing graph, repeatedly delete any train vertex whose
current degree is below eta D, with eta = 10^-5.  Since the full carrier has at
most 1.8488 D + o(D) train vertices, this removes fewer than
0.0000185 D^2 edges.  Therefore the surviving graph has at least

    0.4697 D^2

crossing edges for all sufficiently large D.  Every surviving connected
component has minimum degree at least eta D.

## 2. Phase collapse of every surviving component

Let K_i be a connected component of the surviving graph, with n_i train
vertices.  Choose any two vertices and a shortest graph path between them.
Vertices at path positions 0, 3, 6, ... have pairwise disjoint closed
neighborhoods.  Each such neighborhood contains at least eta D + 1 vertices,
and the whole carrier has at most 1.8488 D + o(D) trains.  Thus every
shortest path has bounded length:

    length <= 3(1.8488/eta) + 2 + o(1).

Every surviving edge changes reduced phase by at most K/D.  Hence the phase
diameter of K_i is O(1/D).  For each of the at most three projective phase
labels, the trains in K_i lie in a single projective direction interval of
width tending to zero.  The proof-only Section-118 bad-train estimate therefore
applies separately to at most three label intervals in K_i.

This is the only place where connectedness is used.  No Euler-trail or
incident-diameter path inference is made.

## 3. Endpoint capacity over all grains

For each nonempty surviving component put x_i = n_i / D and define

    K_0 = 3 B_bad = 0.3489,
    S = sum_i max(x_i - K_0, 0).

The two physical terminal occurrences of each retained train are distinct
occurrence-counted boundary objects.  A component contains at most K_0 D bad
trains in total, because it has at most three label intervals and each interval
has bad capacity B_bad D.  Hence at most 2 min(n_i, K_0 D) of its endpoint
occurrences can be off the principal routes.  Summing components and using
the principal-route budget gives

    2 sum_i max(x_i - K_0, 0) <= 1.8693 + o(1),

or

    2 S <= 1.8693 + o(1).                         (3.1)

This estimate is safe even if different components have overlapping phase
intervals: charging the bad capacity separately only enlarges the allowed
off-route population.

## 4. Mantel forces too much excess

Let e_i be the number of retained crossings in component i.  The train
crossing graph is simple and triangle-free, so Mantel gives

    e_i <= n_i^2 / 4.

For x_i <= K_0, one has x_i^2 <= K_0 x_i.  For x_i > K_0 write
x_i = K_0 + y_i.  Then

    x_i^2 = K_0 x_i + x_i y_i.

Summing, using sum_i x_i <= 1.8488 and
sum_{x_i>K_0} x_i y_i = K_0 S + sum y_i^2 <= K_0 S + S^2, gives

    4 sum_i e_i <= K_0 C_0 + K_0 S + S^2,

where C_0 = 1.8488.

The retained graph has at least 0.4697 D^2 edges.  Consequently S is at least
the positive root of

    S^2 + K_0 S + K_0 C_0 - 4(0.4697) = 0.

The exact scalar certificate gives

    S >= 0.9499.

Thus

    2 S - 1.8693 > 0.0305,

contradicting (3.1).

## 5. Consequence

The proof-only Section-118 safe-window full-core carrier is impossible even when
its quadratic train-crossing mass is split among multiple phase grains.  The
argument closes the multi-grain endpoint-accounting gap by combining:

1. angular-defect pruning;
2. a graph-distance phase-collapse lemma for every surviving component;
3. the three-label bad-capacity bound; and
4. a sharp scalar Mantel/capacity inequality.

It retains every source point and only counts a selected subgraph of the
nonisolated carrier.  It does not invoke the ZR/ZF affine kernel for
contact-isolated points, and it does not produce a same-cardinality competitor.

This is a structural strengthening of the safe proof-only carrier exclusion,
not a full C-II closure: it leaves the full-core regime with slack above the
Section-118 window and leaves the macroscopic inactive-container branch
untouched.

## 6. Hostile scope audit

- The original crossing graph need not be connected; components are handled
  separately.
- No assertion is made that the crossing graph is an Euler trail or path.
- Mantel is applied to each simple triangle-free component, not to a generic
  dense graph with an assumed bipartition.
- The phase-collapse estimate uses minimum degree only after explicit pruning;
  the discarded edge loss is included in the numerical margin.
- Bad capacity is charged per component, which overestimates off-route endpoints
  and is therefore safe.
- Principal-route occurrences are counted with physical multiplicity.
- Contact-isolated source points remain in the full source and are never put
  into the phase graph or affine kernel.

The companion script checks the finite scalar margin with exact source inputs
rounded outward.  It does not establish the inherited carrier or
global-minimality hypotheses.
