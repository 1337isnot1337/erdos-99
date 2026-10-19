# Independent audit: finite palette transversals

**Classification:** unreviewed audit artifact. The candidate and theorem state remain unchanged.

**Assignment:** reviewer for broad card target-c-face-coupled-move; exact investigation exact-head-audit-global-finite-palette-independent-transversal-pr958.

**Audit target:** GLOBAL-FINITE-PALETTE-INDEPENDENT-TRANSVERSAL-PR958, published at destination base 7d0a450fe66991036541023f95c44c064a04b6a8. Source PR #958 is pinned at head 0a72556e786024c9313c7d6287e26c20c1e9b9b8, tree 7b37e2fc5af3bb2e0471a690195a21f9d9fd0d2c, against source base 42f0296d1aca068c809f74cee5dcdb4ebdb27c73.

## Exact statement and hypotheses

Let O_i be a finite set of points in the Euclidean plane for each label i in a finite label set of size n >= 2. Fix a real D. A strict full-label endpoint is a selection y_i in O_i such that every pair of distinct labels satisfies 1 <= |y_i-y_j| < D. In the intended source application, D is the source diameter and is at least 1. The palettes may be empty; an empty class makes both existence statements false.

Form the graph whose vertices are the labelled options (i,y). Join every pair of distinct options in one label class. For different labels, join (i,y) to (j,z) exactly when |y-z| < 1 or |y-z| >= D. Then a strict full-label endpoint exists if and only if this graph has an independent transversal, meaning an independent set containing exactly one vertex from every label class.

## Independent proof reconstruction

Given an endpoint, select (i,y_i) for each label. There is exactly one selected vertex in each class. No same-class edge is selected, and each selected cross-class pair has distance in [1,D), so it is not a conflict edge. The selected vertices form an independent transversal.

Conversely, an independent transversal selects exactly one option per label. A selected cross-class pair is not joined, so its distance is neither below 1 nor at least D. Real-number trichotomy gives 1 <= |y_i-y_j| < D. The chosen points lie in the plane by definition of the option sets, and the pair inequalities prove unit separation and diameter strictly below D. The same-label clique enforces at most one option per class; the transversal condition supplies at least one.

The bounds are strict on the correct sides for this endpoint: distance exactly 1 is allowed, while distance exactly D is forbidden. If the target were a merely nonexpanding endpoint with diameter at most D, the upper conflict would instead use distance greater than D; that is a different statement.

If the labelled source is a global minimizer of D(n) and every one of its n labels has an option in the palette, such a transversal gives an n-point planar unit-separated set of diameter below D(n), a contradiction. This implication uses the complete label set, including contact-isolated labels. It does not require the endpoint itself to be triangle-free. It also supplies no option sets or transversal for any source.

## Falsification controls and reproduction

verify.py compares direct rational pair checks with graph independence on all 784 ordered two-label palettes whose classes are one- or two-element subsets of seven rational planar points. It also checks 125 selected three-label palettes, an empty class, and the boundary cases:

- squared distance 1 is allowed;
- squared distance 4 (distance D=2) is forbidden;
- squared distance 1/4 is forbidden;
- squared distance 9/4 is allowed.

These finite cases are regression controls only; the two-direction proof above establishes the general finite equivalence. The published verifier was also rerun with:

~~~sh
flock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock \
  python3 research/verify_global_palette_transversal_2026_10_12.py --core-only
~~~

It passed the 4,100 Boolean kernel/replay controls, found the 43-label palette endpoint in 13 nodes, and checked all 903 endpoint pairs. Its output states this is a finite 43-gon result and draws no global-minimizer conclusion. The full 132/175-label run was not repeated: its external coordinate files are not present in the published corpus and are withheld pending redistribution permission.

## Byte identity, prior evidence, and scope

At the pinned destination base, the four candidate artifact SHA-256 values match the registry's recorded destination hashes:

| Artifact | Destination SHA-256 |
| --- | --- |
| docs/reports/global_palette_endpoints_and_full_source_exhaustion_2026-10-12.md | e0ac1c388070ae91c00e716d1b511924978c029ba90797a6ba562b12e811450c |
| research/verify_global_palette_transversal_2026_10_12.py | 20f09bd8016fc8e5e0e187cf9da23d5e95f5f6f7ebb0e7da3a0689b738e8badf |
| research/fixtures/global_palette_translation_2026_10_12/provenance.json | a478df25d12190a279cccfc3f069f5f4cc2f8e17a5bbbef8b76597f7541840a3 |
| docs/audits/pr958_autonomous_proof_audit_2026-10-15.md | d32fa3e8b2d267d28e2963f653671989aee7584c5e456ca5e3730a7d8fa0b90a |

The candidate registry and artifact index mark the candidate/report/audit as unreviewed. The registry row has no existing_checks field; the declared validation is only the historical --core-only check, so broader prior-check coverage is unknown here. The source AI audit is useful provenance and contains a reconstruction of this implication, but it explicitly is not a destination exact-head review. This audit therefore checks only the finite transversal equivalence on the published destination bytes. It does not re-audit the colour-lift route, the interval arithmetic, the 132/175 coordinate-table claims, or the independent 175-label competitor.

The controlling revisions at the launch base are theorem state 2026-10-15.publication.2, priority public-frontier.3, and catalogue public-frontier.9. The target candidate has no canonical theorem dependencies. Its lifecycle remains unreviewed; no theorem-state, route, priority, or manifest entry is promoted by this audit.

## What this does and does not establish

The equivalence is correct as stated for a complete finite family of planar option sets and a strict diameter target. It is an exact finite constraint encoding, not a universal palette theorem. A failure to find a transversal excludes only the encoded palette. The 43-gon is a finite nonglobal control. Level I, A, B and C-II remain open; C-I remains closed.

**Stopping condition:** this pass stops after the finite equivalence and its boundary behavior are established. No source-to-palette implication was found, so there is no basis to extend this audit into the other PR #958 routes.

**Remaining lemma:** derive, for every sufficiently large triangle-free global minimizer, complete finite planar option sets whose conflict graph has an independent transversal, or prove a different complete-source strict-diameter contradiction. The quantity this could change is D(n) for the same cardinality n; either a universal construction supplies a contradiction or a source-specific obstruction leaves the palette route conditional.

**Attribution:** the retained source audit identifies the originating research as prepared with Codex (GPT-6). This independent audit was prepared by OpenAI Codex, GPT-6 Luna xhigh, reviewer slot local-11; its role was proof reconstruction and exact finite boundary checks. Existing source and predecessor attribution is retained. This contribution is offered under Apache-2.0.
