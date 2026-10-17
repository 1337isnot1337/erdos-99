> Generated reading edition · [exact source](../../../docs/audits/pr960_autonomous_proof_audit_2026-10-15.md) · source SHA-256 `4f58ca2acb7c57ad468470e7f936202830e34401262ec4d590207b4449c13fb3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1AA0645355FC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# PR #960 substantive autonomous proof audit

**Initial head:** `3d546fcf0e73284e88bd71752100b53d55d73880`.
**Integration base:** `a43c69dac7e7b0627dec2900e12c60fd4608d519`.
**Authority:** state `2026-10-10.audit.234`; Level I and C-II remain open.
**Status:** Source AI proof audit and certificate repairs, retained as provenance. This is not the destination independent exact-head AI-agent mathematical audit required for consequential theorem promotion. No claim is promoted by this record.

The complete three reports and five Python files introduced by this PR were read.
The source closeout receipt is not imported; exact source and destination file identities are recorded in the migration ledger and local verification receipt.
This audit checks the new arguments, taking the explicitly canonical finite lattice
comparison in Audit.243 at its registered scope. It is not a fresh independent
audit of Huxley's discrepancy theorem or of every canonical prerequisite.

## Proof reconstruction and dependencies

1. In [the factorized-distance report](../reports/global_factorized_distance_barrier_2026-10-12.md),
   normalized contact and diameter edge weights have equal incidence at every
   label. Weighted logarithms therefore cancel every positive vertex factor.
   Bounding the two averages by the actual full-source minimum and maximum gives
   the claimed normalized diameter obstruction. Added labels may have zero
   certificate weight but remain in that minimum and maximum. For regular rims,
   contact incidence is `2/m`; both the odd diameter cycle and even antipodal
   matching have the same incidence. The inversion and finite-valued Mobius
   identities give exactly the positive factors used by the theorem. No claim
   that arbitrary factors have a planar realization is made.
2. The two-state graph alternative is valid. A directed cycle alternates colors;
   dividing edge multiplicities by half its length gives two normalized balanced
   incidence vectors, even when a projected vertex or edge repeats. For a DAG,
   longest path lengths decrease by at least one along every arc. Averaging an
   arc inequality with its reversed state-flipped counterpart gives the stated
   half-integral separating direction. Finiteness preserves every inactive
   pair's strict margin for a sufficiently small common parameter. Weighted
   separation excludes balanced incidence in the DAG case. This is an abstract
   distance-array alternative, not a coordinate realization theorem. The scaled
   pentagon distances determine the planar rim and its unique circumcenter;
   the prescribed center distance is incompatible with it, while the displayed
   apex realizes the array in three dimensions.
3. In [the dense-family report](../reports/global_dense_factorized_barrier_2026-10-12.md),
   Audit.243 actually constructs the required strict-sub-D finite lattice packet
   in a disk of radius `D/2+c_* D^(-1/3)`. Its use here does not replace globality
   by an arbitrary-packing density theorem. A separate sufficiently small finite
   scaling makes every packet lower pair strict without losing its upper margin.
   The quartet's only contacts are vertical and its only diameter pairs are the
   two diagonals. A bad upper cap has longitudinal width at most `3 delta` and
   transverse width at most `4 sqrt(D delta)`: the inequality
   `u >= D/2-delta-delta^2/D` follows directly from the two disk inequalities.
   Disjoint radius-one-half disks give the stated `O(D^(1/3))` loss. Constant
   lower-neighborhood losses and at least four deletions retain the sharp
   leading population coefficient, since the fixed error exponent exceeds
   `1/3`. Every surviving packet/quartet pair is strictly internal. The balanced
   quartet certificate includes all other labels with zero weights. A small
   horizontal contraction preserves the two unit contacts, retains every finite
   lower slack, and strictly shortens both old diameters; all upper distances
   are nonincreasing. The contact tensor's horizontal entry is zero while every
   normalized diameter tensor has horizontal entry `D^2-1`, so these sources
   fail KKT and cannot be confused with canonical global minimizers.
4. The dense finite checker correctly reduces packet conflicts to the complete
   outer band. If either original norm is below `M/2-delta`, its sum with the
   other norm is below `M`, hence cannot reach `sqrt(M^2+1)`. After the cover is
   removed, integrality gives every squared packet distance at most `M^2`.
   Rational scaling and the displayed contraction margin control all packet
   lower and upper pairs. Mixed distances are exact in `Q(sqrt(3))`.
   The constant comparison is also correct:
   `kappa0^3=243*pi^3/(16000*sqrt(3))`; the Machin alternating-series bounds and
   rational lower bound on `sqrt(3)` produce the correct inequality directions.
   The floats printed at the end are summaries, not inputs to certification.
5. In [the planarity/radius report](../reports/global_planarity_and_radius_barriers_2026-10-12.md),
   the interpolated centered Gram matrix is positive definite on `1^perp`,
   hence has rank `n-1` for positive interpolation parameter, including collinear
   sources. The exact distance array is therefore nonplanar for `n>=4`.
   For noncollinear sources and parameter strictly below one, rank-two truncation
   retains the original coordinate column space and yields an affine image;
   the tied endpoint is explicitly excluded. Bounded corrective vectors give
   enclosing radius at most `alpha R+tau`; the proposed diameter certificate
   forces it below `R`, obstructing radius minimizers of the same cardinality.
   The six-angle pigeonhole argument proves `r(6)=1`, and every pair of the
   pentagon-plus-center replacement obeys the stated strict diameter bound.
   Its enclosing radius stays one by the zero centroid of the rim. This is a
   finite mechanism regression, with no eventual-minimizer conclusion.

The product/cycle part overlaps the independently preserved
[vertex-factor predecessor](../reports/global_vertex_factor_relocation_2026-10-12.md),
source `83d1d60c6d41812a8f28d39d9ca0a09c36ab78a7`, preserved in PR #995.
This PR retains its distinct dense sharp-coefficient construction, complete graph
alternative, Gram-rank and enclosing-radius regressions. No novelty or independent
human-review claim is inferred from the overlap.

## Corrected certificate and integration defects

The original assertion-based checkers printed `PASS` under `python -O`, which
removes their certification checks. All five Python files now refuse optimized
Python. The graph replay also validates its kind and supplied alternating cycle,
including source states, colors, actual edges, and exact occurrence weights.
Four corruption controls reject altered weight, cycle, kind and direction data.
The existing exhaustive domain remains every disjoint contact/diameter coloring
with both colors nonempty through five labels, not a geometric realization census.

The smallest dense fixture additionally checks all 435,711 retained packet pairs
directly using integer arithmetic with cleared denominators, before and after
contraction. This independently crosschecks the optimized band/cover reduction;
the larger fixtures retain the complete pair-class certificates. Every mixed and
quartet pair is still checked directly. This is a finite crosscheck, not a new
asymptotic proof.

The stale branch conflicted with current main only in the generated artifact
index. That index is regenerated from the merged source; current main's theorem
state, routes, registrations, and unrelated provenance are preserved.

## Validation and remaining gate

Run the four `research/verify_global_*barrier*.py` / graph verification programs
named in the reports, without `-O`. The exact graph census contains 43,286
abstract improvements and 14,330 barriers. The four dense examples retain 938,
3,734, 8,378 and 14,885 labels. Optimized execution of every new Python file must
fail before printing `PASS`. The destination local verification receipt records the exact-head checks actually run. It does not assert mathematical audit completion, Gate 2, or Gate 3.

All reports remain noncanonical research candidates or regressions. Consequential
promotion requires the destination independent exact-head AI-agent mathematical
audit and its own promotion transaction; owner-controlled visibility decisions
remain separate. Audit and repairs were prepared with Codex (GPT-6); this is AI
assistance, not external peer review.
