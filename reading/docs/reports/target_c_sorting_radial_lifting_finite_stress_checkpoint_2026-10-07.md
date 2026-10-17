> Generated reading edition · [exact source](../../../docs/reports/target_c_sorting_radial_lifting_finite_stress_checkpoint_2026-10-07.md) · source SHA-256 `15c1e7e97fe8be17cf9bf4546a2cd35f8a104f673bf11391e67ae42fa637a139`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A042C91956A5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: finite radial-lifting stress checkpoint

Date: 2026-10-07. Authority at wrap-up: `2026-10-07.audit.95`.
**Proved candidate awaiting independent audit, for the listed finite cases
only.** The proposed universal continuation remains exploratory.

## Exact finite statement

For each of the 33 sorting packets listed in
`research/target_c_sorting_radial_lifting_stress_certificate_2026_10_07.json`,
the piecewise affine lifting with height `H(p)=rad(p)^2` gives a strictly
positive pinned equilibrium stress on every unit row involving a moving
vertex. Here `rad(i,j)=max(|i|,|j|,|i+j|)` in the packet's triangular chart;
the full outer ring is pinned.

The cases are all 24 permutations of the arithmetic profile for M=4, and
the descending, ascending and alternating-subsequence orders for each of
M=6,8,10. Each case uses exactly `t=tan(theta/2)=1/(200M^2)`, hence
`0<theta<1/(100M^2)`. No interval of theta is certified by these samples.

## Construction and certificate

Use the exact sorting geometry from
`verify_target_c_sorted_rate_packets_2026_10_06.py`. The flat chart has
`6M^2` elementary triangles. On each triangle, solve its two affine
gradient equations in `Q(sqrt(3))`. Across an internal oriented edge q,
the left-minus-right gradient is `lambda Jq`. The verifier checks this
identity exactly and sums `lambda q` at every moving vertex.

Every nonunit diagonal has zero gradient jump. Every unit moving row has
positive lambda. The listed ring weights lie in [2,3], radial weights are
at least 1, and weak weights exceed t. The total weight is less than
`30M^2`. These are finite certified comparisons, not inferred universal
bounds. The sum at each moving vertex is exactly zero, so the resulting
stress is a pinned equilibrium. All packet pair distances are also checked
to be at least one.

Aggregate exact checks:

| Quantity | Count |
| --- | ---: |
| Cases | 33 |
| Full packet pair comparisons | 302,076 |
| Triangle affine gradients | 5,904 |
| Internal gradient-jump compatibility checks | 8,352 |
| Positive unit rows | 5,904 |
| Zero nonunit diagonal jumps | 2,448 |
| Moving-vertex equilibria | 2,481 |

Reproduce with
`python3 research/verify_target_c_sorting_radial_lifting_stress_2026_10_07.py`.
The output certificate records case orders, parameter values and counts.
The verifier reconstructs and checks the exact coefficients; no floating
LP tolerance or numerical rank is used.

## Scope and continuation lead

This certificate supplies positive pinned stresses for the listed packets.
It does not classify arbitrary clouds, prove rigidity or a finite isolation
radius, verify any full-source replacement ledger, or establish global
optimality. It gives no universal all-M statement and no C-II closure.

A prospective analytic proof would show that each annular sector is made
of coplanar lifted unit rhombi and one new unit triangle, then bound its
gradient jumps uniformly over every arithmetic rate permutation. A separate
prospective inverse estimate would propagate bar angular rates through
unit triangles and opposite sides of unit rhombi to the pinned wall.
Neither argument was completed in this checkpoint. Before using them,
prove the all-permutation face structure, propagation connectivity and
quantified estimates. The implication sought is:

`uniform positive lifting stress + uniform pinned inverse
-> wider finite isolation window
-> arbitrary-cloud maximum-population classification
-> specified wall-class exclusion`.

Even that result would still need an extraction or direct replacement
theorem for arbitrary canonical macroscopic containers. The run was
wrapped up at the user's request before pursuing these further arguments.
