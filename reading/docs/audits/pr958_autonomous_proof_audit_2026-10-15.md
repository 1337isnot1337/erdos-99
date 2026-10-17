> Generated reading edition · [exact source](../../../docs/audits/pr958_autonomous_proof_audit_2026-10-15.md) · source SHA-256 `d32fa3e8b2d267d28e2963f653671989aee7584c5e456ca5e3730a7d8fa0b90a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9FAA8DEBDCFB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# PR #958 substantive autonomous proof audit

**Initial head:** `d11ec97ae330b1301426aa332e9fee7450521bc6`.
**Integration base:** `d6f953100d62a84de72e991642041fdd026e82ba`.
**Frozen migration head:** `0a72556e786024c9313c7d6287e26c20c1e9b9b8`
(tree `7b37e2fc5af3bb2e0471a690195a21f9d9fd0d2c`) against frozen source main
`42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
**Authority:** `2026-10-10.audit.234`; Level I/C-II remain open.
**Status:** Source AI substantive proof/certificate audit and repairs. This audit is
retained as provenance; the destination policy requires a separate independent
AI-agent exact-head review before consequential theorem promotion. No canonical
claim is promoted.

The two complete reports and three Python files were read. The source audit also
records hashes for both external coordinate tables. The destination preserves
only the provenance metadata; it does not redistribute either table while
explicit permission remains unclear.

## Lift, rank and endpoint arguments

In [the colour-lift report](../reports/global_colouring_lift_and_planar_rank_barrier_2026-10-12.md),
the uniform distance interpolation has centered Gram matrix
`lambda G+(1-lambda)J/2`, positive definite on `1^perp`; its rank is exactly
`n-1`. A planar strict competitor cannot be inferred when `n>=4`.
This overlaps the Gram-rank argument in PR960, while the colour-specific lift,
flattening criterion and palette computations are distinct.

For a proper contact colouring, different-colour unit contacts stay unit and
strict pairs stay strict; the finite positive same-colour slack gives a common
admissible parameter. Every pair, including those involving isolates, obeys
the strict new upper bound. Eppstein's original Theorem1 was rechecked in the
journal paper, Section2, pages489–490: triangle-free penny graphs have degeneracy
at most two. Reverse greedy colouring therefore uses at most three colours,
including isolates, and the orthogonal lift has dimension at most four.
[Eppstein, original journal paper](https://www.maths.tcd.ie/EMIS/journals/JGAA/accepted/2018/463.pdf).
No flexibility theorem or broader near-quadrangulation claim is imported.

For a noncollinear source, centered source coordinates have rank two; the lifted
rank remains two exactly when every centered colour column is in their column
space. Two nonempty colours correspond to two parallel level lines. With three
nonempty colours the affine colour map has invertible linear part, so every colour
has one preimage and at most three source points are possible. The unit square's
rank-three lift and the affine-coloured rectangle's actual planar flattening check
both sides. The lower and strict upper endpoint quadratics are obtained directly
by clearing `1+t^2`; one common endpoint parameter must satisfy every pair.
The deliberate intermediate collision does not invalidate its feasible endpoint.

## Whole-source palette and interval certificates

In [the palette report](../reports/global_palette_endpoints_and_full_source_exhaustion_2026-10-12.md),
choosing one allowed option per source label is exactly an independent transversal.
The sufficient system permits only certified valid pairs; the permissive system
forbids only certainly invalid pairs. Therefore sufficient SAT certifies an actual
endpoint, while permissive UNSAT excludes every geometric assignment within that
one palette, even with unresolved interval comparisons. Full-source exhaustion is
not a conclusion about arbitrary endpoints or global optimality.

Arc-consistency deletion removes only values with no support in a current adjacent
domain. This preserves every satisfying assignment. Splitting a non-singleton
domain into every remaining value is exhaustive and terminates. The supplied
relations are bidirectional transposes, as required by the propagation kernel.
Positive assignments are independently checked over every chosen geometric pair.

The interval helper rounds every rational operation outward on its fixed grid.
Multiplication uses all endpoint products, division requires a strictly positive
denominator, squaring handles zero crossing, and square roots use exact integer
floor/ceiling bounds. The Machin alternating-series enclosures bound pi.
Periodic reduction places the Taylor argument below seven; the common
`7^119/119!` remainder covers both truncations, including the sine remainder since
`7/120<1`. Recurrence rounding remains outward. No floating value decides a bound.

For the 43-gon, exact sine identities supply the unit and diameter equalities;
all other chord classes have certified strict bounds. The 132-label rational
packet is normalized from its exact measured minimum and strictly inflated.
The certified radial gap and radius sum cover every rim/interior pair. Every
interior pair is checked, so the 175-label source's only contacts/diameters are
the actual rim cycles. The independent 175-label packet is checked over all
15,225 pairs and has squared diameter below183.2352, strictly less than the source.
The known prime-rim local obstruction uses canonical Proposition13.1 only at
its stated scope; it is not an assertion of globality for either filled source.

Both primary coordinate files were fetched afresh and matched the frozen hashes:

- 132 labels, 9,900 bytes: `64c8a85573a5ced26e666fa25b713c4fc6264c409d811eab101cd13ff65ef00a`.
- 175 labels, 13,125 bytes: `6f889e1143dbb5aee039224198617355070104f161a2bdd0705166eaf814f140`.

The exact URLs, hashes and prior fixture lineage remain in the provenance JSON.
No published packing-optimality assertion is used. The destination retains the
source audit's verification notes but excludes the coordinate tables pending
explicit redistribution permission.

## Computational and integration repairs

All three Python files now refuse optimized execution, which otherwise removes
their assertion checks. The palette checker now emits a JSON certificate containing
the 43-label positive assignment, source/parameter/fixture identities, and an
exhaustive negative proof for all175 labels. Each negative node records justified
domain prunings and, when needed, a complete split over the remaining domain.
A separate replay validates those deductions and every branch without search.
The CLI supports `--certificate-json PATH` and `--replay-certificate-json PATH`.
It verifies fixture identities, source count, palette parameter, interval scale,
positive assignment and all endpoint geometry before accepting the saved proof.
Positive option indices must be valid; negative Python indices are refused.

The propagation/branching kernel and negative-proof replay match independent direct
assignment enumeration on all4,096 three-label, two-option systems with arbitrary
binary relation on each unordered pair, plus the original four controls. Mutated
pruning and incomplete branch coverage are rejected. The actual 175-label saved
proof also replays with `solve` replaced by a function that always fails, establishing
that replay does not invoke the global or control search.

The finite results are unchanged: the rim endpoint checks903 pairs and is found
in13 nodes; the full-source permissive system has2,039 constrained pairs and is
exhausted in4 nodes. This certifies failure of all `3^175` assignments for exactly
the stated palette. The independent full-source winner still passes15,225 pairs.
The lift/Gram/planar endpoint and interval special-value suites also pass.

The only source-side merge conflict against that branch's main was the generated
artifact index, which was regenerated from merged sources. The source audit
reported canonical state, routes, theory, problem, prompts and certificate
registrations unchanged. Its state/transaction, prelaunch-link, whitespace and
recovery checks are source-side evidence; they are not destination-hosted results.
The reports remain noncanonical candidates/regressions. This audit is source
provenance, not a destination exact-head promotion review. Prepared with Codex
(GPT-6); this is AI assistance, not external peer review.
