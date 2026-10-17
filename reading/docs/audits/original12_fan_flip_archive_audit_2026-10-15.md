> Generated reading edition · [exact source](../../../docs/audits/original12_fan_flip_archive_audit_2026-10-15.md) · source SHA-256 `58e1f7be6b65e7cbd6c90e13b132842836664c973292360a3922228b07ad1e4d`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-6CE5D7647538","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Original worktree12: fan-flip and isolate-escape archive audit

**Original head:** `75aac1464f80ca91256e96dc70ca0c865e0b3b0e`.
**Comparison main:** `bc429cc834e38be7a17b10d8e55622d463864931`.
**Authority:** `2026-10-10.audit.234`; Level I/C-II remain open.
**Status:** AI substantive proof/certificate audit and preservation. Independent
human mathematical review remains required; no canonical claim is promoted.

Both working files were absent from main: a565-line report and188-line exact
checker. Their complete archived bytes, all proofs and code were read. They are
preserved in the verified177-file private archive and restored with corrections
below. The original index has no staged delta; full Git metadata and the original
commit are recoverable on both hosts. No ignored working file belongs to this
particular archive entry.

## Complete geometric proof reconstruction

The [restored report](../reports/target_c_fan_flip_isolate_escape_2026-10-02.md)
requires an actual unit-separated source of diameter `D>=4`, a supplied same-carrier
fan with unit adjacent chords and angular width at most pi/3, and all source labels.
It does not extract a fan from an arbitrary canonical source.

FF.1 reflects an internal leaf by exactly `1/D`. Its two unit chords stay unit.
The new point is a positive convex combination of the carrier and two adjacent
source points, with coefficient `epsilon/(D-epsilon)` at the carrier. Their
positive variance makes every old-source upper distance strict. In the degree-two
canonical application, absence of an additional retained-label blocker preserves
contacts and loses an actual diameter, contradicting the global/lexicographic
selection. The removed old label is excluded from the lower test; new contacts at
an endpoint remain blockers, rather than being discarded.

For FF.2 write the blocker displacement as `r u+s t`. The old carrier upper bound
gives `r>=epsilon*|v|^2`; equality at `r=epsilon` would be an excluded adjacent fan
vertex. The two neighbor separation inequalities and new unit-disk condition give
`|s| <=40/63`. The supplied triangle has half-width at least `693/1024`, and
`0<D-r<D-epsilon`. Thus every additional blocker lies strictly in that source
triangle and, by the same variance identity, has every old upper distance strict.
This is an arbitrary-source statement, also covering additional old contacts;
its degree-two canonical blockers are strict noncontacts and diameter-inactive.

FF.3 treats one ordered fan. Three angular steps separate reflected positions by
more than two, using `(1-D^-2)(3-D^-2)>2`. A two-step common-blocker lens has radius
`(3-D^-2)/(2D)` about its midpoint, while the unchanged middle fan vertex lies at
that same radius. Their combined radius is below one, excluding an additional
source blocker. The excluded original adjacent fan vertex is not counted as an
additional blocker. Consequently at most two consecutive flips share one blocker.
For consecutive leaves, the squared endpoint bounds give the stated tangential
and height inequalities. The outward height violates the actual carrier disk;
the inward height is within the claimed `5/D` of the equilateral completion.
This supplies a near triangle only.

For FE the near-contact graph is on every original label except the moved leaf,
with threshold `1+1/D`, not only on the positive core. If its blocker components
contain no core vertex, all their labels are genuine contact isolates. Translate
all of them and the leaf by the same finite vector. Internal distances stay fixed,
and component closure makes every moved-to-fixed lower pair strict. The two old
leaf contacts stay unit. Old diameter pairs incident with these isolates are
absent by the explicitly assumed canonical normalization; all leaf diameters open.
If no new upper pair reaches D, the unchanged contact graph and lost diameter
contradict secondary minimality. Hence the indicated inactive near-diameter cross
pair exists. The support-cap bound makes its moving endpoint lie at projection
at most `sqrt(3)D/2+1/D`, and the actual graph path gives the displayed linear
length estimate. The core-hit alternative may be local; no macroscopic core path
is inferred there. No source label is deleted or silently fixed outside the pair
ledger.

## Exact regressions and current successors

The rational blocked fans have actual contact path and diameter star graphs.
Their additional blockers are strict noncontacts. All68 internal co-moves preserve
every old contact and remove the specified diameter; every pair is checked.
The two-row ladders have the claimed contact graph and actual diameter star.
Positive reciprocal vertical-gap weights and strict concavity give every interior
reaction, and `lambda+zeta=C` gives the exact outer-row diameter balance.
Carrier and row endpoints are not globally equilibrated; the local identities do
not furnish a complete KKT stress or canonical rigidity.

The relevant current canonical successor is
[the simultaneous-reflection theorem](../reports/target_c_centered_fan_simultaneous_reflections_2026-10-02.md),
under its independent-leaf and midpoint hypotheses. Audit152 gives a directed
full-source blocker path and Audit166 strengthens its large-source depth and
first-blocker matching. Those conclusions do not create a fan population or
cross-leaf path disjointness. The restored report retains its own smaller-D,
single-fan geometry, conservative undirected-component alternative and distinct
rational ladder/co-move fixtures as noncanonical candidates/regressions. It does
not expand a canonical theorem's registered scope.

One stale stress-budget identifier in the active Audit166 prose is aligned with
the manifest's `C-FAN-KKT-MULTIPLIER-BUDGET`; its proof, hypotheses and conclusion
are unchanged. The manifest and all route/theory/problem/prompt authority remain
unchanged.

## Provenance and certificate repairs

The archived full StartingHEAD is nonexistent, while its explicitly given short
identifier `75aac146` resolves uniquely to the actual archived worktree head
recorded above. That verified full identity replaces the erroneous one. The raw
old bytes remain in recovery; no historical identity is invented.

The checker now refuses optimized Python. It also certifies an explicit strict
competitor for each of its12 finite sources, by moving only the isolated carrier
slightly in the positive x direction. For these fixtures every other point has
positive x and squared norm above one. Choose a positive rational step at most
`1/100`, each x coordinate, and `(norm2-1)/(4*(2*abs(x)+1))`. This preserves all
carrier lower slacks and strictly shortens every carrier distance. All old actual
diameters touch that carrier, and other pairs stay fixed, so the complete endpoint
has strict smaller diameter and the same contacts. The checker independently
verifies all5,440 endpoint pairs. This proves these finite sources nonglobal;
it supplies no competitor for a canonical global minimizer.

The original24 flip identities,1,968 blocked-source pair bounds,68 blocked flips,
40 isolated blockers,3,472 ladder pairs and136 positive interior equilibrium
identities still pass. The new12 strict endpoints preserve all contacts, and the
optimized-execution control fails before any PASS. Finite checks do not prove
the universal analytic claims or full KKT existence.

The private per-file receipt pins original SHA-256 identities, corrected current
files, tests, recovery and subsequent exact stale-registration/branch disposition.
Registration retirement requires fresh identity, metadata, locks and normalized
cwd/fd checks; absence of the physical directory alone is insufficient. Prepared
with Codex (GPT-6); this is AI assistance, not external human peer review or
publication authorization.
