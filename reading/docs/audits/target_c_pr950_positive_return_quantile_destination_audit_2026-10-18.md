> Generated reading edition · [exact source](../../../docs/audits/target_c_pr950_positive_return_quantile_destination_audit_2026-10-18.md) · source SHA-256 `0b0bdfbaf912fe015f48bf0b4c37b12b4889a39b70593cbbac2b336bc3ab7894`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-AA8F6FF70E4D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Destination audit of the PR #950 positive-return quantile

Date: 2026-10-18. Audit base: `7d0a450fe66991036541023f95c44c064a04b6a8`,
state `2026-10-15.publication.2`, priority `public-frontier.3`, catalogue
`public-frontier.9`.

**Verdict: PASS at the assigned subclaim only.** Under the recorded canonical
quadratic-core hypotheses, the long-train bank, hull-train depletion,
loaded-near-unit adjacency, and Audit 235 separator inequality imply a linear
family of nontrivial, vertex-disjoint actual-contact paths. Full-source Oler
counting gives the stated fixed-fraction `O(D)` route-length quantile. This is
an independent destination audit of those implications. The full imported
candidate remains unreviewed: this report does not audit its common-grid or
attachment-to-grid arguments, and it does not change any theorem lifecycle.

## Exact scope

The audited claim is the positive-length and length-quantile part of
`TARGET-C-PR950-TRAIN-RETURN-LENGTH-QUANTILE` in the candidate registry. Use an
unbounded canonical C-II quadratic-core sequence with `D -> infinity` and
`R_4/D^2 -> r > 0`; fix `epsilon` in `(0,r)`. Set

```text
a_* = (2/3) sqrt(r-epsilon),  ell = epsilon/(3 pi),
beta = 40/(pi sqrt(3)),
kappa = (sqrt(25 ell^2 + 4 beta a_* ell) - 5 ell)/(2 beta).
```

All source labels, including contact isolates, remain in the population count.
The graph used for paths is the actual positive-contact core and the target set
is the actual loaded set. The result controls only the number of returned trains
with bounded contact-edge count; it gives no route payment, movement, strict
diameter improvement, or C-II/Level-I closure.

## Independent reconstruction

The canonical quadratic-core train-bank statement supplies at least
`(a_* - o(1))D` distinct physical strict-rhombus trains, each with degree at
least `L_D = floor(epsilon D/(3 pi)) = ell D + O(1)`. Let `H_L` be the trains
having a terminal occurrence on an actual unit side of the loaded hull.
Canonical Audit 206 gives `R_H = O(D^(5/3))` actual rhombus crossings incident
to `H_L`. Counting train-crossing incidences counts a rhombus with two
`H_L`-trains twice, so

```text
L_D |A_D intersect H_L| <= sum_{tau in H_L} d_tau <= 2 R_H.
```

Only `O(D^(2/3))` members of the selected long bank are therefore removed.
For each remaining train, choose one of its two terminal unit edges. If both
endpoints were in the actual loaded set `B`, the canonical loaded-near-unit
adjacency theorem (positive-area `conv(B)`, `D >= 6`) makes this edge an actual
loaded-hull side. That would place the train in `H_L`, contrary to its
retention. Choose an endpoint outside `B`. These choices need not be distinct
as source vertices; their set `X` is, however, disjoint from `B`.

Apply canonical Audit 235 to the retained train family and these chosen rail
endpoints. If `k_D` is the minimum endpoint-inclusive vertex separator from
`X` to `B`, its train inequality is

```text
(a_D - 5 k_D)_+ (L_D + 1) <= beta k_D^2 + 10 k_D.
```

For `x = liminf k_D/D`, an infinite `x` is already stronger than required. If
`x` is finite and `x < a_*/5`, divide along a subsequence attaining this liminf
by `D^2`; the linear terms vanish and give

```text
ell (a_* - 5x) <= beta x^2.
```

The positive root of the corresponding quadratic is `kappa`. If
`x >= a_*/5`, then `x > kappa` as well. Thus
`liminf k_D/D >= kappa > 0`. The argument remains valid when multiple trains
select the same terminal vertex: the Audit 235 cut proof counts train rails,
and at most five distinct rails pass through any one core vertex. Menger uses
the resulting set `X`, producing paths with distinct starts and distinct
loaded endpoints. Since `X` and `B` are disjoint, none is a zero-edge path.

For the length count, let `n_D` be the cardinality of the full source. Finite
Oler, the isodiametric inequality, and Cauchy's perimeter formula give

```text
n_D <= (pi/(2 sqrt(3))) D^2 + O(D).
```

This counts every source label, including the contact isolates. If the Menger
paths have edge lengths `s_i`, vertex-disjointness gives
`sum_i (s_i+1) <= n_D`, hence `sum_i s_i <= n_D`. For any fixed `t > 0`, at most
`n_D/(tD) = (pi/(2 sqrt(3)t))D + O(1)` paths have more than `tD` edges. Since
`k_D >= (kappa-o(1))D`, at least

```text
(kappa - pi/(2 sqrt(3)t) - o(1))D
```

paths have at most `tD` edges. Substituting
`t = pi/(2 sqrt(3)(1-theta)kappa)` gives the candidate's
`(theta*kappa-o(1))D` paths and its stated threshold, for each fixed
`theta` in `(0,1)`.

## Adversarial checks and limits

- The factor `2` in the hull-train deletion estimate includes crossings whose
  two incident train labels both lie in `H_L`.
- The loaded-adjacency input is used only for the endpoints of an actual unit
  terminal edge, inside its recorded positive-area loaded-hull scope.
- Shared selected roots do not invalidate the separator estimate: its
  multiplicity bound counts distinct train rails through a cut vertex. Menger
  paths themselves start at distinct vertices of the deduplicated set `X`.
- The Oler population is the complete source. Replacing it by the positive
  contact core is unnecessary and would omit isolated labels from the stated
  bound.
- The quantile is aggregate: it does not bound every path, Euclidean route
  length, or any face/interface charge. It supplies no source-realized move.

The prior source proof-audit artifact records the same broad return and Oler
steps, but its own lifecycle states it is provenance rather than a destination
audit. At this base both imported artifacts remain `unreviewed` in the artifact
index. This report independently reconstructs only the assigned implication
against the destination report bytes; no canonical manifest, candidate status,
route, priority, or certificate registration is changed.

## Evidence pins and next obligation

- Candidate report: `docs/reports/target_c_train_return_length_budget_worker03_2026-10-10.md`,
  destination SHA-256 `4ba5214ff20a2548c7e04d01e821f85ea941ffce40dd1ee1d7673c905892941f`.
- Preserved source audit: `docs/audits/pr950_autonomous_proof_audit_2026-10-15.md`,
  destination SHA-256 `8ea063ae82c8d4149fee0d21ab6f2eb0d53a6702c62c162a5dd5cfd08a56bb70`.
- Canonical inputs: `C-QUADRATIC-CORE-TRAIN-BANK`,
  `C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS`,
  `C-ALL-BRANCH-HULL-TRAIN-DEPLETION`,
  `C-LOADED-NEAR-UNIT-ADJACENCY`, and Audit 235's
  `C-LONG-TRAIN-SEPARATOR-INEQUALITY` and finite Oler input.

The next candidate-level bridge remains a linear endpoint overlap or direct
linkage between the train-root-to-loaded-attachment family and the separate
loaded-attachment-to-grid family. Any later endpoint argument must retain every
source label and verify every lower and active/inactive upper pair constraint.
The full imported candidate and C-II remain open.

This is first-party mathematical review work compatible with Apache-2.0.
OpenAI Codex (GPT-6 Luna xhigh) performed the independent proof reconstruction
and adversarial checks; no external text or theorem is imported.
