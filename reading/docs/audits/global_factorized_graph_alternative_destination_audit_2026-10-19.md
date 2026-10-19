> Generated reading edition · [exact source](../../../docs/audits/global_factorized_graph_alternative_destination_audit_2026-10-19.md) · source SHA-256 `f2ac8d9ca3fc9f88c371797aaaa4bf219302f9486acb70b9debd0fa14cdb9743`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-82430C245D1E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Independent destination audit: PR #960 factor graph alternative

## Scope and exact destination

This is an independent reconstruction of candidate
`GLOBAL-FACTOR-GRAPH-ALTERNATIVE-PR960` at destination `main`
`7d0a450fe66991036541023f95c44c064a04b6a8`, tree
`db766e0e25b562054df26aeec7e627d5a579dd6d`. The theorem state, priority and
catalogue revisions are `2026-10-15.publication.2`, `public-frontier.3` and
`public-frontier.9`.

The three destination inputs matched their assignment SHA-256 pins:

| Destination file | SHA-256 |
| --- | --- |
| [`global_factorized_distance_barrier_2026-10-12.md`](../reports/global_factorized_distance_barrier_2026-10-12.md) | `bd5e04fc103c1d172af746c44595c7c9efeec68918ba30d7f71f4d00339e54e2` |
| [`global_factorized_graph_alternative.py`](../../../research/global_factorized_graph_alternative.py) | `0a7962ef2adf6ed8c656f999aa5d8a4f6e9abfad312a9263dc91571d092483ea` |
| [`verify_global_factorized_graph_alternative.py`](../../../research/verify_global_factorized_graph_alternative.py) | `39cb42efc7b519c2e2454a4f6f4b9b92334eadf63e1dca9670aaf42` |

The report is a transformed destination copy of the source PR #960 report;
its destination hash is the one audited here. The older
[`PR #960 source audit`](pr960_autonomous_proof_audit_2026-10-15.md) records a
source-PR review at its own head. It explicitly does not constitute this
destination exact-head review. That provenance is useful but was not used as
the proof: I reconstructed the graph and margin arguments before reading it.

The destination candidate registry classifies the result as **unreviewed,
noncanonical research**. This report is review evidence only. It changes no
claim lifecycle or theorem state. Level I, A, B and C-II remain open; C-I
remains closed.

## Candidate lemma, hypotheses and decision boundary

Let a finite, labeled, unit-separated source have pair distances
`1 <= d_ij <= D`, with `D > 1`; let `C` be its actual unit-contact pairs and
`H` its actual diameter pairs. Assume every pair outside `C union H` has the
strict margins `1 < d_ij < D`, and keep every source label in the argument,
including labels incident to no contact. Form the two-state directed graph on
`(i,+)` and `(i,-)` by adding `i+ -> j-` and `j+ -> i-` for `ij in C`, and
`i- -> j+` and `j- -> i+` for `ij in H`.

The candidate lemma is: either this graph has an alternating directed cycle,
which yields probability weights on `C` and `H` with equal incidence at every
label, or it is acyclic and has half-integers `z_i` with
`z_i+z_j >= 1` on `C` and `z_i+z_j <= -1` on `H`. In the latter case a
sufficiently small positive `lambda` makes the complete abstract array
`d_ij exp(lambda (z_i+z_j))` strictly greater than one and strictly less than
`D` at every pair.

The exact quantity affected is the complete-array minimum and maximum after a
positive vertex-factor change. A cycle blocks a strict distortion improvement
within that factorized class; a DAG gives an abstract strict endpoint under the
finite inactive-margin hypothesis. Either result could inform a C-II or Level I
endpoint search only if the abstract array were realized by planar coordinates
for a global source. Neither branch supplies that bridge or changes `D(n)`.

## Proof reconstruction

**Cycle branch.** Every graph arc switches sign. Thus every directed cycle has
even length `2m` and alternates contact and diameter arcs. Count occurrences of
each unordered edge in the projected closed walk and divide each count by `m`.
This gives nonnegative weights of total one in each color. At every visit to a
label the entering and leaving arc have opposite colors, so its contact and
diameter incidences agree. This remains true if the projection repeats a label
or an edge: occurrences, rather than distinct edges, are counted.

For the factorized obstruction, if `q_ij = s_i s_j d_ij` with `s_i > 0`, the
balanced incidence identity cancels all `log(s_i)` terms and gives

`sum_H b_ij log(q_ij) - sum_C a_ij log(q_ij) = log(D)`.

The left side is at most `log(max q) - log(min q)`, where both extrema range
over the complete pair set. Hence `diam(q)/min(q) >= D`; newly active pairs
cannot evade the bound because they are included in those extrema.

**Acyclic branch.** Let `w(s)` be the maximum directed-path length from state
`s` to a sink. For every arc `s -> t`, `w(s)-w(t) >= 1`. Flipping both signs
and reversing an arc gives another arc. Set
`z_i = (w(i,+)-w(i,-))/2`, which is half-integral. For a contact `ij`, add
the inequalities from `i+ -> j-` and its flipped reverse `j+ -> i-`:

`w(i,+)-w(j,-) >= 1`, `w(j,+)-w(i,-) >= 1`.

Their sum is `2(z_i+z_j) >= 2`. For a diameter pair, the arcs
`i- -> j+` and `j- -> i+` instead give
`-2(z_i+z_j) >= 2`. This proves the two separation inequalities. The path
lengths are defined on all `2n` states, so isolated labels are not dropped.

For an inactive pair put `sigma_ij = z_i+z_j`. If `sigma_ij < 0`, its lower
bound is preserved whenever
`lambda < log(d_ij)/(-sigma_ij)`. If `sigma_ij > 0`, its upper bound is
preserved whenever
`lambda < log(D/d_ij)/sigma_ij`. Each finite bound is positive by the strict
inactive margins. Choose `lambda` below the minimum of these finitely many
bounds (with no restriction from a pair whose sign is favorable or zero).
Contacts then grow strictly because `sigma_ij >= 1`; diameter pairs shrink
strictly because `sigma_ij <= -1`; every inactive pair retains both bounds.
This gives an explicit finite-source choice rule, but no lower bound on
`lambda` uniform over sources.

The two outcomes are mutually exclusive: summing the DAG inequalities against
balanced probability weights would force the same weighted sum of `z_i+z_j`
to be both at least `1` and at most `-1`. The two weighted sums are equal
because each is the sum over labels of `z_i` times that color's incidence at
`i`. Conversely the directed cycle constructs balanced weights. The finite
graph dichotomy and the separation argument are therefore valid under the
stated source and margin assumptions.

## Adversarial boundary checks

- The report's source setting is normalized and has `D > 1`. If a unit-separated
  source has `D = 1`, every pair is simultaneously a contact and a diameter;
  as a two-colored graph it has a 2-cycle for any pair. The helper deliberately
  rejects overlapping edge sets, so its executable domain is the `D > 1`
  branch. This is a boundary case, not a counterexample to the graph statement.
- The destination helper also requires nonempty contact and diameter edge sets.
  Nonempty `C` follows from the normalized `min d_ij = 1` premise, and nonempty
  `H` follows for `n >= 2`. If “finite source” were read as an arbitrary array
  without unit separation, that premise must be stated: for the one-pair array
  `d_01 = 1/2`, there is no unit contact and shrinking the diameter cannot
  produce a length at least one. The report's packing-source hypothesis rules
  this out; the compressed registry wording should be read in that context.
- The exponential endpoint is only an abstract complete pair array. The
  six-point regular-pentagon-plus-center control has `z=(-1/2,...,-1/2,3/2)`.
  With `exp(lambda)=21/20`, normalization leaves center-to-rim lengths one and
  scales every rim length by `(20/21)^2`. All 15 normalized pair bounds hold
  exactly in `Q(sqrt(5))`, but the centered Gram rank rises from two to three.
  The array has a three-dimensional apex realization and no planar realization.
  Thus the proof does not imply the needed Euclidean or planar competitor.
- A global source must still retain all labels and satisfy every lower and upper
  pair constraint in a planar endpoint, or yield a unit triangle. The graph
  result establishes neither source extraction nor global-minimizer optimality.

## Finite controls and exact outcomes

At the pinned destination bytes, the published verifier enumerates every
disjoint three-state contact/diameter edge labeling with both colors present
through five labels. It checks half-integral inequalities or replays a supplied
alternating cycle and its exact normalized incidence weights. Four corrupted
certificates (weight, cycle state, certificate kind and potential direction)
are rejected. The pentagon-center fixture checks all 15 abstract endpoint
pairs with exact `Q(sqrt(5))` signs and the centered-Gram rank change.

Commands actually run in this review:

| Command | Outcome |
| --- | --- |
| `sha256sum` on the three pinned destination inputs | All three values matched `source-pins.json`. |
| `flock -x /home/cinna/.local/state/erdos99-host-compute.lock python research/verify_global_factorized_graph_alternative.py` | Passed: 43,286 abstract improvements, 14,330 factorized barriers, four corruptions rejected, all 15 pentagon-center pairs checked; Gram rank `2 -> 3`. |
| `flock -x /home/cinna/.local/state/erdos99-host-compute.lock python -O research/verify_global_factorized_graph_alternative.py` | Failed before `PASS` with the intended `RuntimeError` that certificate assertions are required. |

The finite census is not an embedding census, a global-minimizer result or a
proof of the universal E-99 quantifiers. Its scope is exactly the enumerated
edge colorings and the named six-point realization obstruction.

## Lifecycle, overlap and disposition

The source PR #960 audit is retained as historical provenance; it is not
substituted for this exact destination review. The task-scoped offline overlap
snapshot had complete pagination over 47 open and 97 closed PRs, zero open
issues, and eight discussions, with no exact audit match. A targeted live PR
scan likewise found no exact candidate or investigation match. No matching
previous local, homelab or MacBook handoff was present. This audit is therefore
not a duplicate of an already completed destination review.

**Audit result:** the graph dichotomy, balanced-cycle construction,
half-integral DAG separator and finite strict-margin perturbation are correct
for the report's normalized finite-source hypotheses. The destination
candidate remains unreviewed and noncanonical pending the project's separate
lifecycle process. No promotion is requested. The next lemma is a source-wide
planar construction preserving every lower and upper pair constraint for an
acyclic global source, or a different full-source planar endpoint that yields
a unit triangle or a same-cardinality strict sub-`D` competitor.

OpenAI Codex (GPT-6 Luna xhigh) independently reconstructed the proof,
checked the destination bytes and replayed the finite controls. This is AI
assistance, not a claim of human mathematical review. No third-party text or
data was copied; the work relies on the cited first-party destination sources
and remains compatible with the repository's Apache-2.0 contribution terms.
