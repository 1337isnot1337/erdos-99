> Generated reading edition · [exact source](../../../docs/audits/pr955_autonomous_proof_audit_2026-10-15.md) · source SHA-256 `69a42884e36eacc29fc987dd004bc2570bcc174402aad2ced478b1bf03f8e63f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-BBD3B40A9B41","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# PR #955 substantive autonomous proof audit

**Initial head:** `bfe1424f4b8308c72f438394a7f511188d6e778a`.
**Integration base:** `8c6f37127fbf119fe7ae3745babd1130a6628a09`.
**Authority:** `2026-10-10.audit.234`; Level I/C-II remain open.
**Status:** Source AI substantive audit and repairs; it is preserved as
provenance and does not satisfy the destination's exact-head promotion review
policy in [REVIEW_POLICY.md](../REVIEW_POLICY.md). This record promotes no
claim.

Both complete reports (381 and 396 original lines), both Python files (129
and 414 lines), the complete saved JSON result and the README/index changes
were inspected. The private receipt pins the final repaired head, tree,
files and verification logs. The exact original remote head was checked
before work began. Canonical prerequisites are taken only at their recorded
scope, without a fresh audit of every inherited theorem.

## One-contact approximation, descent and finite global regressions

In [the attainment report](../reports/global_level_i_attainment_and_one_contact_2026-10-11.md),
moving an actual contact's endpoints inward by t leaves their mutual length
`1-2t`, every other moved-involving length at least `1-t`, and unchanged
pairs at least one. The old convex hull contains the moved set. Midpoint
dilation restores exactly that selected contact, makes all other pairs
strictly longer than one and bounds the diameter by `D/(1-2t)`.
The chosen `t=epsilon/(2(D+epsilon))` gives the stated additive tolerance
and labeled convergence. The selected endpoints return to their old places.
Compactness after fixing one label proves existence of an unrestricted
minimizer; its minimum separation is one by strict contraction. Thus both
restricted infima equal D(n). The second displayed feasible class now
explicitly says unit-separated; omitting that condition would allow invalid
subunit pairs. Nonattainment is exactly the original global question, and
continuous non-strict inequalities transfer without an invariance premise.
No positive uniform diameter gap is possible; strict pointwise inequalities
are not excluded.

For a uniquely contacting source with n at least three, contracting all
other labels about the contact midpoint gives strictly negative derivative
for every nonfixed squared distance. The endpoint inequalities imply
`|x|^2>3/4+|x dot u|`, supplying that sign. Finitely many strict lower
margins and derivatives admit one common positive contraction. The old
diameter exceeds one and every maximizing pair shortens, so the new
diameter is strictly smaller. This does not extend to multiple contacts.

The nonextreme-label argument uses a two- or three-point convex combination;
the latter has a ray gap at least 120 degrees, yielding diameter at least
sqrt(3). A convex quadrilateral has an angle at least 90 degrees, and a
convex pentagon one at least 108 degrees. The adjacent unit lower bounds
then prove respectively sqrt(2) and the golden-ratio diameter floors.
At equality all angles and adjacent side inequalities are equalities,
giving precisely the square and regular unit pentagon. These are finite
actual global optima and genuine regressions against connected-contact
extensions of the one-contact theorem.

The n=8 import was checked afresh from the actual local primary journal
PDF, Theorem 1.1, printed page 106: the stated diameter and regular-heptagon
optimal hull, with the eighth point not uniquely placed.
[Bezdek–Fodor, publisher DOI](https://doi.org/10.1006/jcta.1998.2889).
The publisher URL was inaccessible through the web tool; direct PDF text
extraction was performed over SSH using the exact local PDF bytes, with
hash and excerpt locations recorded privately. For the displayed interval,
top-vertex distances are smallest and stay at least one; all other new
distances are strict and the hull remains fixed. It is therefore a
connected family of actual eight-point optima with triangle status changing
at its endpoint. It supplies no unbounded-cardinality counterexample.
The discarded stress-connectivity idea is correctly subsumed by canonical
Section 64.3, which applies to arbitrary normalized stresses.

## Annular cut and matching theorem

In [the annular report](../reports/global_annular_matching_competitor_2026-10-11.md),
the graph includes every pair of length at least D, so deleting a cover
is equivalent to a strict-sub-D subset. A conflict endpoint lies in the
closed annular band. Since `S<D/sqrt(2)`, conflict angles are obtuse;
maximizing each radius gives angle at least `pi-alpha`. Same-half-plane
conflicts therefore have an endpoint in the positive-ray wedge of width
`2alpha`. Rotating and averaging yields the integer deletion bound with
the stated floor. All other edges cross the dividing line. Matching and
equal-sized covers in the remaining bipartite graph give the additive
cover/matching error. Distance-D and inner-radius ties remain included.

The odd-cycle angular sum gives the stated cycle-length lower bound;
the regular odd polygon attains it and the one-label cut. Expanded
half-unit disks give `N_ann<=4D(1+2delta)`. The cosine inequality gives
the explicit `8sqrt(c)D^(1/3)+16c^(3/2)` bound. The optional bounded
lattice error uses precisely canonical Audit 245's translation-uniform
O(r^(2/3)) disk count, subtracting an open inner count from a closed outer
count. No smaller translation-uniform discrepancy exponent is imported.

For q=k cubed, thickening the selected circular labels and comparing to
the enlarged antipodal union proves the exact independence bound. A
surviving complementary gap accounts for at least twice the enlargement
radius. Consecutive labels attain the bound, and the old diameter cycle
has a maximum-cardinality matching, giving the claimed order-k gap.
The dilation exponent 3/4 gives exactly any fixed positive c without
decreasing unit separation. Added interior lattice points have strict
lower margins and, once delta is below one half, no threshold conflicts.
The leading-density extension remains nonglobal and D remains a conflict
threshold, not its actual diameter.

## Complete packets, exact optimization and deformation

The two-row triangular packet is strictly inside the stated disk by direct
squaring, and its threshold graph is exactly complete bipartite. Deleting
one row saves `4k^2+2k` against edge-count deletion, including when that
subgraph is embedded in the full disk packet. This is an unbounded saving
regression, not an improved universal reserve coefficient.

The enumeration bounds cover the entire translated lattice disks: the
quadratic norm bounds each individual index by `2r/sqrt(3)`, within the
given integer ranges. Every omitted nonhalo label has radius strictly
below D-S; the other radius is below S, so their pair is strictly below D.
All halo pairs are compared using integer predicates. For each retained
cut subset, all its outside neighbors are forced deletions; the residual
bipartite optimum is certified by a matching/cover dual. Exhausting every
independent cut subset proves the exact whole-graph cover optimum. All
nonconflict labels remain in the full cardinality count. Convex hull
distances independently verify the retained diameter.

The rational basis deformation keeps every nonzero lattice lower distance
at least one and leaves only axis unit steps, giving a bipartite contact
graph. Coordinate spans bound every upper-distance change by `2rho B`,
strictly below the available margin. Actual retained axis pairs keep
minimum separation one. For the three displayed cases the old packet
strictly beats its deformed triangle-free version, certifying nonglobality.

## Computational, provenance and integration repairs

Both checkers now refuse optimized Python. The one-contact checker validates
the full planar label domain, actual selected unit contact, parameter range
and genuinely unique contact before descent. Rational conversion avoids
accidental float arithmetic from integer input. Its four malformed-input
controls pass and successful descents retain all other lower pairs strictly.

The matching helper now emits its actual matching and equal-sized cover.
Every independent cut branch is recorded and replayed, including the full
domain, graph, mask coverage and chosen optimum. JSON round trips are checked
without optimizer calls. The optional `--certificate-json PATH` writes
proofs for all 48 disk packets, three full-column packets and the odd-cycle
case. All 52 graph proofs replay with matching/cut searches disabled.
Their scope is the emitted conflict graph; the source constructors separately
verify metric correspondence, full population and strict retained diameter.

An independent direct enumeration of all 32 subsets checks every one of
the 1,024 five-label graphs. Four mutations reject repeated matching edges,
missing cut branches, incomplete domains and changed winning covers.
The repaired aggregate JSON agrees exactly with the frozen original.
The one-contact suite retains 16 transformations/descents, four exact
equilateral checks and all ten pentagon pairs. These finite suites do not
prove the universal angular/circle statements or the cited n=8 theorem.

Current main's README plus the one original 37-line insertion are retained;
the artifact index is regenerated from merged source. Canonical state,
route/theory/problem/prompt files and certificate registrations remain
unchanged. Both reports remain unreviewed and the PR stays a draft for
independent human mathematical review. Prepared with Codex (GPT-6); no
human peer review or publication authorization is implied.
