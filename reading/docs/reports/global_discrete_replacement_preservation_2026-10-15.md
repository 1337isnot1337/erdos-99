> Generated reading edition · [exact source](../../../docs/reports/global_discrete_replacement_preservation_2026-10-15.md) · source SHA-256 `84dc414ecc9a7dd4ae6e946168314b80ec0051e653097140baa4b75416dfdfda`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D9935CD21E8D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Two global discrete-replacement sources: preservation audit

**State:** `2026-10-10.audit.234`; Level I remains open.
**Classification:** AI substantive source audit; noncanonical candidates;
independent human mathematical review and owner rights decisions remain required.

## Frozen sources and historical coverage

The mixed-exchange source is
`research/sol/global-attainment-gap-20261012` at
`3e4e99da8d83c4be85302c9e3a3192c034b54e69`; the discrete-isometry source is
`research/sol/global-e99-20261012` at
`de0c978a385f6e4863f0e5fbd22924ebe967226b`.
Each has exactly one source-only commit above the common base
`ab6dd3336f9f8d440f2bada76edb32153391cddc`. The complete 205/211-line reports,
251/220-line scripts, README additions and generated-index deltas were read.
There are no earlier source-only revisions to reconcile. These exact report
and script paths were absent from current main, and their distinct complete
source claims are preserved here rather than inferred from other routes.
Original file hashes, original patches and the recovery identities are in
the private preservation receipt; no private operational data is imported.

## Mixed exchange: proof and scope

The [report](global_mixed_exchange_and_diameter_cut_2026-10-12.md) prices a
cover `T` of **all** old pairs of length at least the new threshold `R`,
where `1<R<=D`. Consequently `A\T` has strict diameter below `R`.
The replacement cloud is itself separated and has strict diameter below
`R`. Its bipartite graph includes every mixed pair below one or at least
`R`; coincidences and contact isolates are included. Alternating reachability
from unmatched left labels gives a cover with exactly one endpoint of each
matching edge and no unmatched labels. Matching/cover duality therefore
proves the exact maximum compatible population
`n-|T|+|X|-nu`. An independent set corresponds to distinct actual positions,
and any n-point subset retains strict diameter. Reversing the alternating
construction gives the right-side Hall deficiency identity. The necessary
inequality for every global minimizer follows by contradiction, with no
triangle-free restriction on the replacement.

For the square source, the parallelogram identity on its two corner
diagonals proves resistance to every affine map using only retained unit
steps. This is not globality. The two explicit replacements have matching
and cover sizes 745 and 1,055, compatible populations 1,001 and 1,753,
and n-point squared diameters 1,429 and 2,689. The source upper cuts each
cover all 420 threshold pairs and are minimum by a matching/cover dual.
For all `k>=33`, the radius-15 triangular packet contains 817 sites and
its lower conflicts lie among at most 793 integer sites in radius 16.
Removing these and the two left corners covers both old diameter pairs.
The mixed upper bound
`15+sqrt(2)*ceil((k-1)/2) < sqrt(2)*(k-1)` follows from the complementary
floor being at least 16. All cloud distances are below 30. This supplies
at least `k^2+22` compatible sites at strict smaller diameter, hence an
infinite nonglobal family. The integer counts are finite enumerations;
the all-k conclusion uses this analytic argument.

The original script independently checked final pair distances but emitted
only certificate sizes. The preserved version emits the actual label sets,
matching and cover; a separate replay recomputes every conflict, validates
the dual and checks the full union and n-point subset without matching
search. JSON round trips pass. Mutations deleting a retained label or
repeating a matching endpoint fail. Original negative controls for equality
at the upper threshold, uncovered diameter edges and lower violations also
pass. The universal cloud-extraction/Hall-surplus theorem remains absent.

The source's discussion of Connelly and Dickinson is a scope warning, not
an imported theorem. Their primary *Periodic Planar Disk Packings*,
[Conjectures 2–3](https://pi.math.cornell.edu/~connelly/Connelly-Dickinson-V3.pdf),
does state the triangular-torus gaps as conjectures. No fixed-period claim
is transferred to finite diameter minimizers here.

## Discrete isometries: proof and scope

The [report](global_discrete_isometry_blocker_closure_2026-10-12.md) gives
an exact finite endpoint equivalence for a common two-isometry dictionary.
Each clause excludes precisely one lower or strict-upper pair violation.
All clauses together preserve all labels and every pair. The original
statement omitted `n>=2`; this is now explicit because a singleton has
diameter zero and vacuous clauses cannot certify strict improvement.

For rational sources and a nonzero rational translation direction, all
mixed squared distances are rational quadratics. Their roots at one and
`D^2` partition the parameter line into constant-conflict cells. Each root
is tested separately; one rational representative suffices in each open
cell. Exact algebraic ordering, equality and sign are required. A sign
change of the parameter is equivalent after complementing moved labels
and translating the entire endpoint. Beyond displacement `2D`, mixed
pairs violate the upper bound, so constant states are the only possibilities
and do not improve the diameter. The O(n^4) bound counts graph operations,
with root/sign bit costs explicitly excluded.

The global blocker theorem first chooses a triangle-free global minimizer
with minimum contact count and then minimum diameter-pair count. These are
integer minima in a nonempty class; no compactness of the open triangle-free
subclass is needed. For a generic isometry, a forward-closed moved set
satisfies all non-strict pair constraints, creates no new contact or
diameter pair, and retains triangle-freeness. Distinct SCCs can always be
separated by a forward-closed union in their condensation DAG. Separating
an actual contact contradicts the first minimum; separating a diameter
edge contradicts the first or second minimum, or global diameter
minimality itself. This normalization does not apply automatically to
every original minimizer, and contact isolates remain graph vertices.

The odd-diameter-cycle obstruction follows because every original diameter
edge must change state in a strict two-state endpoint. The Cartesian-grid
obstruction follows from the spans of its top and bottom rows; even
independent horizontal relocations force a cross-row squared distance at
least the original diameter squared. Neither is a global-optimality
certificate. The inactive upper-pair fixture explicitly includes the
offending contact isolate.

The exact sweeps pass for 38 cells of the two-chain fixture, 10/10/14/16
cells of the four square directions and 28 cells of the 3-by-3 axis grid.
The first has a full-source competitor at offset 1/2; square/grid tests
have none within their tested dictionaries. Small cases also compare
2-SAT to exhaustive assignments. Endpoint validation now rejects truncated
and nonbinary states and enforces two-dimensional coordinates. Both
preserved scripts refuse optimized Python. A universal dictionary or
assignment theorem remains unproved. No canonical claim, certificate
registration, route prompt or Level I status changes.

## Dirty three-state extension

The original worktree at `de0c978a` also contained an uncommitted 215-line
[three-isometry report](global_three_isometry_competitors_2026-10-12.md),
186-line exact checker, 113-line numerical discovery script, README addition
and index delta. All five original file hashes match the initial private
archive. This is unique research beyond the branch tip, so preserving the
tip alone would not permit worktree cleanup. All files and deltas were read.

The general finite independent-transversal equivalence follows by including
all alternatives of each actual label and all forbidden actual pairs.
The statement now requires `n>=2`, matching the repaired binary theorem.
The diameter-coloring necessity remains only a necessary condition.

The regular-heptagon positive stress, Fourier rank and nonglobality already
appear in canonical Audit 122. The new data are a distinct rational
three-isometry endpoint with only four old unit contacts retained, plus
quantitative rational margins and an independent interval certificate.
The cubic `8c^3+4c^2-4c-1` has derivative at least six on `[1/2,1]` and
opposite endpoint signs. The seventh-root identity identifies its unique
root there with `cos(2pi/7)`. Rational bisection and outward integer-square-root
enclosures therefore bound all coordinates. Exact polygon identities prove
the old unit lengths, diameter chords and zero Fourier modes; interval
inclusion alone would not prove these equalities. Rational orthogonality
proves each motion is an isometry. Every mixed squared distance exceeds
`1000005/1000000`, all endpoint squared distances are below `4477/1000`,
and the old squared diameter exceeds five. Two positive Fourier-mode
classes exceed `8/5` and `23/10`; conjugate modes and the exact zeros give
PSD rank four. This proves nonglobality, with no arbitrary-source conclusion.

For the all-m row benchmark, adjacent row offsets differ by one half and
vertical spacing is `sqrt(3)/2`; rows two or more apart have vertical
distance above one. The endpoint squared diameter is bounded by
`(m-1/2)^2+3(m-1)^2/4`, strictly below `2(m-1)^2` for every `m>=6` because
`m^2-6m+4>0`. This retains all `m^2` labels and uses m dictionary states.
It cannot be inserted into an unknown surrounding source without new pair
checks. Finite cases 6, 7, 8, 17 and 31 support only their explicit inputs;
the infinite family follows analytically.

The seeded rotated search independently reproduced trial 8 and all 21
proper three-group patterns. Floating discovery is not a certificate.
The exact checker passes, replays JSON rational parameters independently
of discovery, rejects truncated states and all-identity substitutions, and
refuses optimized Python. Original bytes, tracked patches, numerical logs
and the adapted source remain recoverable. The regenerated index and
replacement README entry preserve the two tracked deltas' research content.
