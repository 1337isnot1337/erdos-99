# Global Level I: attainment and annular matching route

**Status:** source PR #955 research is retained as unreviewed, noncanonical
work. Its proofs and finite checks do not change Level I, C-II, or the
theorem-state. The source PR's included reports were already present in this
repository; this track adds the mathematical map, exact provenance, and
remaining obligations.

Frozen source main is `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source
PR #955 head is `d5afc236a7b1de9567dcb6dda65d957ed91c726b`, tree
`5233d9c8b7774e29609ffaa68cc8dd346c4afa1c`, with merge base
`8c6f37127fbf119fe7ae3745babd1130a6628a09`. The six mathematical/evidence
files are retained at their original paths. The one-contact report's local
third-party PDF/extraction paths were replaced with its publisher DOI; no
paper or extracted text was copied. Per-file source hashes and treatments are
in the [migration ledger](../migration/2026-10-16/ledger/source-pr-files.jsonl).

## Two global routes and their exact scope

### One-contact approximation: the open question is nonattainment

For every finite unit-separated planar set with minimum distance one and at
least one contact, the report moves the endpoints of one actual contact
toward one another, then dilates about their midpoint. This retains all labels,
restores exactly the selected contact, makes every other pair strictly longer
than one, and increases diameter by at most an arbitrary `epsilon`. Thus the
infimum over triangle-free unit-separated `n`-point sets equals the unrestricted
minimum `D(n)` for every `n >= 2`; there is no positive uniform diameter gap
above `D(n)` at any fixed cardinality.

Consequently, the Level I question at a given `n` is exactly whether the
triangle-free infimum is attained: a triangle-free global minimizer exists
precisely when that restricted infimum is attained. The approximation does not
show nonattainment, and a strict pointwise inequality for every triangle-free
configuration is still compatible with equality of infima. A second
proposition shows that an exactly one-contact configuration is nonglobal for
`n >= 3`; it does not extend to sources with multiple contacts.

The reports retain finite controls that block broader inferences: square and
regular pentagon global optima; a connected family of global `n=8` minimizers
whose triangle status changes; and nonglobal regressions against connected
contact or stress-connectivity shortcuts. The `n=8` premise is cited to
Bezdek--Fodor's [publisher DOI](https://doi.org/10.1006/jcta.1998.2889). None is
an unbounded-cardinality counterexample. The weaker positive-stress-component
route is already subsumed by the destination's canonical Section 64.3 and is
explicitly discarded in the report.

Full argument and finite proof scope: [attainment and one-contact report](../../reports/global_level_i_attainment_and_one_contact_2026-10-11.md),
[one-contact verifier](../../../research/verify_global_one_contact_2026_10_11.py).

### Annular conflict graph: exact deletion currency and the missing source bound

For a specified unit-separated comparison packet `X` inside
`B(o,S)`, with `S = D/2 + delta < D/sqrt(2)`, the report joins every pair at
distance **at least** `D` in a conflict graph. A retained subset has diameter
strictly below `D` exactly when its deletions cover every conflict edge, so
its maximum possible size is exactly `M_D(X) = |X| - tau(G_D(X))`; distance-D
ties and all labels are included.

Writing `nu` for maximum matching, the source proves a wedge deletion that
makes the graph bipartite. With `N_ann` labels in the full radial band and
`alpha = 2 arccos(D/(2S))`, it gives
`nu <= tau <= nu + floor(alpha N_ann/pi)`. For `D-S > 1/2`, disk packing
gives `N_ann <= 4D(1+2delta)`. At `delta = c D^(-1/3)` this yields
`r <= floor(8 sqrt(c) D^(1/3) + 16 c^(3/2))` for arbitrary unit-separated
clouds. A translated triangular-lattice packet has `r = O_c(1)` only with the
stated translation-uniform circle-count input already in canonical Audit 245;
the report assumes no stronger discrepancy exponent.

Exact full-packet searches and rational deformations produce triangle-free,
same-cardinality, strict-sub-`D` competitors for three finite packets. Their
retained diameter-squared values are `63`, `4093`, and `46641` at packet sizes
`63`, `3733`, and `42344`, respectively. The original packets are also
explicitly shown to be nonglobal relative to those competitors. The two-row
complete-bipartite construction shows that edge-count deletion can overpay by
`Theta(D^(2/3))`; it does not prove a better universal asymptotic coefficient.

The decisive global bridge is absent: for every sufficiently large
triangle-free global minimizer, construct an admissible comparison packet
`X` with `M_D(X) >= n` (or otherwise prove the equivalent nonattainment route).
Neither lattice closeness, a density ceiling for all triangle-free packings,
nor the finite nonglobal packets establishes that source-specific bound. Keep
the exact lower and upper pair constraints, all isolates, and the full
cardinality in any proposed endpoint.

Full argument and finite proof scope: [annular matching report](../../reports/global_annular_matching_competitor_2026-10-11.md),
[saved graph evidence](../../../research/global_annular_matching_2026_10_11.json),
[annular verifier](../../../research/verify_global_annular_matching_2026_10_11.py),
and the committed [52-graph exact cover/matching proof certificate](../../../research/certificates/global_annular_matching_proofs_2026_10_16.json).
The certificate is reproduced by passing `--certificate-json PATH` to the
verifier; its generation command, hash, and finite scope are in the candidate
registry.
The exact-head source AI audit is preserved at
[PR #955 audit](../../audits/pr955_autonomous_proof_audit_2026-10-15.md); it is
provenance and mathematical evidence, not a destination promotion review.

Candidate records `GLOBAL-LEVEL-I-ONE-CONTACT-PR955` and
`GLOBAL-LEVEL-I-ANNULAR-MATCHING-PR955` in the
[machine-readable registry](../../targets/target-c/candidate-registry.json)
connect these claims to dependencies, source hashes, regressions, validation,
and the remaining proof obligations. The source README's summaries are
represented here; its global catalog is not copied over destination
navigation. The source index was replaced by a locally rebuilt destination
artifact index.
