<!-- theorem-state: {"artifact_id":"ART-529F1202FE2E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Independent audit: PR #958 squared-distance interpolation

**Date:** 2026-10-18. **Verdict:** PASS for the stated Euclidean metric descent
and rank barrier. It does not give a planar strict-diameter endpoint for
`n >= 4`, and therefore does not close Level I. The candidate remains
unreviewed in the theorem state.

## Exact source and scope

I reviewed the published candidate bytes at destination base
`7d0a450fe66991036541023f95c44c064a04b6a8` (tree
`db766e0e25b562054df26aeec7e627d5a579dd6d`). The authoritative state is
`2026-10-15.publication.2`, the priority revision is `public-frontier.3`, and
the catalogue revision is `public-frontier.9`. The candidate registry marks
`GLOBAL-SQUARED-DISTANCE-INTERPOLATION-PR958` unreviewed and lists no canonical
dependencies.

The two reviewed destination files are the [full report](../reports/global_colouring_lift_and_planar_rank_barrier_2026-10-12.md) and the
[PR #958 source audit record](pr958_autonomous_proof_audit_2026-10-15.md).
Their recorded destination SHA-256 values match the bytes at the pinned base:

| File | Destination SHA-256 | Git blob at pinned base |
| --- | --- | --- |
| `docs/reports/global_colouring_lift_and_planar_rank_barrier_2026-10-12.md` | `ab1fc0f0d2cdd3b1f72b801a7b873d56f5db6bed68bfd231f29d88b5945538bc` | `927961c6a25c0044de5bf9258bda79e1de4c9ce6` |
| `docs/audits/pr958_autonomous_proof_audit_2026-10-15.md` | `d32fa3e8b2d267d28e2963f653671989aee7584c5e456ca5e3730a7d8fa0b90a` | `f623b43b9895a325b12710d6770eb8968d42a39a` |

This audit covers only the uniform squared-distance interpolation and its
planar rank consequence. It does not audit PR #958's colour lift, flattening,
palette certificates, or the distinct results added by PR #960.

## Candidate lemma and proof reconstruction

Let `p_1,...,p_n` be a finite, pairwise distinct planar source, with
`d_ij = |p_i-p_j| >= 1` for every pair and diameter `D > 1`. Fix
`0 < lambda < 1`. For every off-diagonal pair define

```text
d'_ij^2 = 1 + lambda (d_ij^2 - 1),   i != j;
d'_ii = 0.
```

Contacts remain exactly unit. Every noncontact remains strictly above one and
strictly shortens, since `d_ij^2 > 1` and `0 < lambda < 1`. The function
`s -> 1 + lambda(s-1)` is increasing, so the maximum is attained on exactly
the former diameter pairs and
`D'^2 = 1 + lambda(D^2 - 1) < D^2`. This uses every label and every pair,
including labels isolated in the unit-contact graph.

The metric is Euclidean: take vectors `r_i` forming a regular unit simplex in
`R^(n-1)`, and set
`q_i = (sqrt(lambda) p_i, sqrt(1-lambda) r_i)`. Then
`|q_i-q_j|^2 = lambda d_ij^2 + (1-lambda) = d'_ij^2` for `i != j`.

For the dimension test, let `P` have rows `p_i`, let
`J = I - 11^T/n`, and set `G = J P P^T J`. Write `Delta` for the full
squared-distance matrix, with zero diagonal. The off-diagonal definition and
zero diagonal give

```text
Delta' = lambda Delta + (1-lambda)(11^T-I).
```

Using `G = -J Delta J/2`, `J 11^T J = 0`, and `J I J = J`, the centered
Gram matrix of the interpolated metric is

```text
G' = -J Delta' J/2 = lambda G + (1-lambda)J/2.
```

It annihilates `1`. For every nonzero `x` perpendicular to `1`,

```text
x^T G' x = lambda |P^T x|^2 + (1-lambda)|x|^2/2 > 0.
```

Thus `G'` is positive definite on the `(n-1)`-dimensional subspace
`1^perp`, and `rank(G') = n-1`. Double-centering uniquely determines the
centered Gram matrix from all pair distances; any Euclidean realization of
this same metric therefore has affine dimension `n-1`. The construction is
planar for `n <= 3`; for `n >= 4` this particular interpolated metric has no
planar realization.

## Adversarial scope checks

- For `n=3`, the rank is two, so the metric is realizable in the plane. If a
  three-point global minimizer had `D>1`, this same-cardinality realization
  would strictly reduce its diameter. This finite-cardinality implication
  uses global minimality only at the final contradiction.
- For `n>=4`, rank `n-1 > 2` blocks the proposed interpolated metric as a
  planar endpoint. This obstruction is specific to the complete metric above;
  it says nothing against a different planar rearrangement.
- The diagonal convention matters: the interpolation formula is for `i != j`.
  Setting the diagonal of `Delta'` to zero yields the displayed matrix
  identity. Applying the scalar formula to diagonal entries would be wrong.
- The argument proves a Euclidean higher-dimensional endpoint, not a planar
  endpoint or a path of planar feasible configurations. No density estimate,
  source-to-scaffold identification, or local optimality premise is used.

The published exact verifier was run at this source. Its rational
Gram-interpolation fixtures use `lambda=3/5` and returned rank `n-1` for a
four-point square, a four-point rectangle, a three-point right triangle, and
a five-point square with one contact-isolated label: ranks `3, 3, 2, 4`.
These are useful controls for the algebra and label coverage; the universal
rank conclusion comes from the proof above, not from the finite fixtures.

## Prior evidence, disposition, and remaining lemma

The retained PR #958 source AI audit already records the same rank identity,
but identifies itself as source provenance rather than a destination exact-head
independent review. The destination candidate and artifact index both remain
unreviewed. The candidate registry also records that the interpolation and
rank-`n-1` claim is duplicated in the PR #960 source report; that overlap is
not independent confirmation. The merge review bundle at this base covers
destination PRs #86--98 and does not review this frozen source PR candidate.

**Disposition:** PASS for the finite metric identity, Euclidean realization,
and exact rank obstruction. The only effect on the canonical quantity is a
strict same-cardinality planar improvement when `n <= 3`; for `n >= 4` this
candidate cannot lower the planar minimum diameter `D(n)`. It supplies no
consequence for the universal sufficiently-large-cardinality statement.
The decision it changes is whether this interpolation itself can be used as
the general planar route: the rank calculation rules that out for `n >= 4`.
No theorem lifecycle, priority, route, or claim status is changed here.

The remaining lemma is: for every sufficiently large triangle-free planar
global minimizer, construct a same-cardinality planar endpoint satisfying all
lower pair bounds and having diameter strictly below `D(n)`, by a mechanism
that is not this complete squared-distance interpolation (or prove a different
planar realization theorem). This audit does not supply that endpoint.

## Reproduction, limits, and attribution

At the pinned base, the recorded SHA-256 values above were checked against the
published files. The source verifier command was run under the fleet's shared
single-process compute lock:

```sh
python research/verify_global_colouring_lift_rank_2026_10_12.py
```

It was run with the provisioned verification Python while holding the fleet's
shared compute lock, and exited successfully; all listed rational fixtures and
exact controls passed.
The verifier checks finite instances and does not certify global optimality.
No repository-wide theorem-certificate replay is claimed; if required by the
final integration candidate, it is deferred to the merging agent.

This first-party audit adds no third-party text or data. It is offered under
the repository's Apache-2.0 contribution terms. OpenAI Codex (GPT-6 Luna
xhigh) performed the independent proof reconstruction, scope checks, and
write-up; the source PR #958 AI audit is predecessor provenance, not this
reviewer's evidence. Level I remains open; C-I is closed and C-II remains open.
