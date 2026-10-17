> Generated reading edition · [exact source](../../../docs/audits/pr957_autonomous_proof_audit_2026-10-15.md) · source SHA-256 `a7b0ba682d107135802294b5dc2a70022955f2a90fecada17c0234874f7f00a7`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1D6333BF17AD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# PR #957 substantive autonomous proof audit

**Frozen source-PR head:** `a11e16998094ab3d7afd9fd07eff8b55909ec406` (tree `77ce8dd135c2b4233f121bd448621d362841da06`). The original audit lineage began at `fe926fb95060995cb5339ffbaa9eb3e2f03e4b0c`; source PR merge base is `d6f953100d62a84de72e991642041fdd026e82ba`.

**Initial head:** `fe926fb95060995cb5339ffbaa9eb3e2f03e4b0c`.
**Integration base:** `d6f953100d62a84de72e991642041fdd026e82ba`.
**Authority:** `2026-10-10.audit.234`; Level I/C-II remain open.
**Status:** Source PR AI proof and certificate audit; this audit is provenance
and does not satisfy the destination's independent AI-agent exact-head review
requirement for consequential promotion. No canonical claim is promoted.

The complete report, research run note and both exact Python checkers were
read. The source PR audit records the reviewed head, tree, files and checks.

## Joint finite optimization

In [the joint-exchange report](../reports/global_joint_diameter_cover_exchange_2026-10-12.md),
removing a diameter cover T makes every surviving source pair strict at the
upper endpoint. The supplied comparison packet already satisfies both bounds.
The remaining obstruction is exactly the bipartite graph of every lower and
upper cross conflict, including coincidences and diameter equalities. Its
maximum independent set has cardinality `n-|T|+m-nu_T` by the explicitly proved
matching/minimum-cover identity. Every geometric mixed subset conversely omits
a source diameter cover, so minimizing `|T|+nu_T` gives the exact optimum.
Integrality yields the stated `m+1` obstruction for a global source. All source
isolates remain in the cross graph and the cardinality calculation.

The alternating-reachability proof correctly handles unmatched left labels,
matched return edges, equal cardinalities and covering every edge. The Hall
form follows by choosing the reachable comparison labels. Removing k extra
source vertices can destroy at most k edges of a maximum matching; this proves
monotonicity of the joint cost and justifies searching inclusion-minimal covers.
It does not justify restricting to minimum-cardinality covers. The rational
three-label example and all four complete geometric fixtures verify that
critical distinction, strict upper inequalities, and the role of coincidences.

Only the lower cross graph is planar: if two short cross edges crossed, their
same-family separation bounds would sum to at least two while the two crossed
edge lengths sum to less than two. An edge through a same-family endpoint is
likewise impossible. Coincident cross-family pairs are isolated edges.
Six opposite-family neighbors in an open unit disk would have an angular gap
at most pi/3 and a pair at distance below one; the stated degree-five bound is
valid. Upper cross conflicts can instead form the exhibited `K_(4,3)`.

## All-k dense star construction

The rational leaf parametrization has norm exactly R and chord distances
between `32/17` and `2(k-1)`. Each leaf's distance to the packet center is
between `R/2` and `R/2+2`. The interior disk radius `R/2-4` therefore gives
all displayed leaf/interior, origin/interior and interior/interior margins.
The rounded rational lattice height is above `sqrt(3)/2`, so every nonzero
lattice difference is strictly longer than one. Only the inserted pair is unit.
The actual diameter graph is exactly the k-leaf star, and exactly `n-2` labels
are contact isolates.

The new leaves move by exactly1/8. Every noncorresponding cross pair keeps its
lower margin, and all cross upper bounds remain strict. Thus the complete cross
graph, including coincident interior copies, is exactly the indicated matching.
The unique one-label diameter cover has profit-1; the other inclusion-minimal
cover, all k leaves, has profit0. The simultaneous packet with the old origin
has the same source cardinality and diameter exactly `R-1/8`, certifying that the
sources are nonglobal. No KKT, globality or optimal-population assertion is made.

The fundamental-cell diameter is uniformly below three for `k>=4`; its tiling
sandwich proves the disk count with error `O(R)`. At most18 sites are removed near
the inserted pair. Since the cell area is `sqrt(3)/2+O(R^-2)`, the final population
has the claimed triangular leading coefficient with the explicit `O(D)` error.
This is not the sharper all-minimizer reserve and does not supply globality.

## Run-note regression and literature scope

The four-label weak-cage example is unit-separated and triangle-free: all three
neighbor-neighbor distances exceed one. The weights `a,1,b` give the stated
positive surrounding relation. The affine span of the first two contacts has
distance `t/sqrt(1+t^2)` from the origin, which tends to zero. For the proposed
free ball, direct substitution gives the displayed positive excess squared
distances when `t<min(1,1/(4R))`. It supplies a local geometry regression, without
a free-ball-in-hull extraction or global-source premise.

The primary Schurmann paper was rechecked at Definition1, Theorem2 and its
proof setup. Its nonattainment theorem uses a smooth fixed convex container and
a limited-complexity family, including a uniform positive affine-span separation;
the proof chooses a seed radius at least its reciprocal. Section4 discusses
other optimization problems but does not prove those hypotheses for arbitrary
triangle-free diameter minimizers.
[Schurmann, original publisher paper](https://ems.press/content/serial-article-files/25994).
The finite matching theorem itself imports no external theorem.

## Certificate and integration repairs

Both assertion-based Python files now refuse optimized execution. The matching
helper can emit a JSON-safe witness containing the complete right-label domain,
comparison-label count, matching edges, and source/comparison cover labels.
A separate replay verifies injectivity, actual edges, full coverage and equality
of the matching/cover sizes without calling the optimizer. Small-fixture output
includes that witness and the actual selected source/packet labels; dense star
covers are also replayed after JSON round-trip.

An independent direct matching enumeration checks all512 graphs on three labels
per side and all eight retained-source subsets, totaling4,096 cases. Four controls
reject an invalid edge, duplicate matching edge, incomplete cover and missing
right-label domain. The original exhaustive geometric mixed-subset checks remain
independent of graph construction and matching. At `k=4,5`, the full rational star
ledgers still check7,924 and162,945 pairs, including55 and254 source contact isolates.
The proofs above establish all-k scope; finite runs do not prove packet existence
for arbitrary minimizers.

README integration retains current main and appends the one original PR insertion;
its exact source-PR provenance is retained in the migration ledger. The generated artifact index is rebuilt from
merged sources. State, routes, theory, problem, prompts and certificate registrations
remain byte-identical to current main. State/transaction, prelaunch links, whitespace,
optimized-execution and recovery checks are recorded at the repaired head.
The source draft was unreviewed at freeze. Destination promotion requires an
independent AI-agent exact-head mathematical audit under the repository policy.
Prepared with Codex (GPT-6); this assistance is not that independent audit or
publication clearance.
