> Generated reading edition · [exact source](../../../docs/audits/target_c_isolate_normalization_independent_audit_2026-10-08.md) · source SHA-256 `bfcb8f58c6419b62692405ff440cd9fc650fb6263bbcb676cb17fb69935f4153`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-349A53AB9CE5","canonical":true,"claim_ids":["C-CORE-DIAMETER-REPLACEMENT-AFTER-ISOLATE-NORMALIZATION","C-FULL-SOURCE-ISOLATE-NORMALIZATION"],"claim_statuses":{"C-CORE-DIAMETER-REPLACEMENT-AFTER-ISOLATE-NORMALIZATION":"canonical","C-FULL-SOURCE-ISOLATE-NORMALIZATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: full-source isolate normalization and core diameter replacements

**Date:** 2026-10-08  
**Audit base:** `origin/main=333a4384287603b72fbb44dc4fc99f729160ad53`, state `2026-10-08.audit.172`.  
**Target:** C-II. C-II and Level I remain open.

## Frozen source and scope

The source is `origin/research/level-i-closure-20261007` at the immutable tip
`12f6833725f281ce39a6d04ebcb45630b3a6768f`. The candidate report was introduced at
`3457d175bafad554b71c442a3a3667b077025dcf`:

- `docs/reports/target_c_isolate_normalization_core_diameter_replacement_2026-10-07.md`
  SHA-256 `c3e1baac507b2ad0e28e5de1d69c5eb8db619e21a4d9370b5103d08df615828e`;
- `research/verify_target_c_isolate_diameter_normalization_2026_10_07.py`
  SHA-256 `475cb5da56328e245716e5b740c31bdf44d7227789a7fe184140f5a905bce9f1`.

This audit covers only the finite full-source normalization in source Section 2 and its
core diameter-replacement corollary in Section 3. The cubic-moment and support estimates
in Sections 4 onward were not audited and are not promoted here.

## Verdict

- **PASS — promote `C-FULL-SOURCE-ISOLATE-NORMALIZATION`.** The centroid contraction
  preserves every full-source lower constraint and the upper diameter bound, retains the
  exact contact graph, and makes every isolate-involving pair strictly shorter than the
  diameter.
- **PASS — promote `C-CORE-DIAMETER-REPLACEMENT-AFTER-ISOLATE-NORMALIZATION`.** Any
  feasible same-cardinality exact-contact endpoint with noncongruent core must create at
  least as many new diameter pairs inside the core as it removes old ones.
- **Not audited:** the source report's zero-width cubic moment, changed-label bound, and
  matching bound. They remain discovery-branch claims without canonical force.

The proof does not construct the assumed feasible endpoint. It makes no C-II or Level I
closure claim.

## Exact statements

### 1. Finite normalization of contact isolates

Let $`Q=(Q_i)_{i\in V\sqcup Z}\subset\mathbb R^2`$ be a finite unit-separated labelled
placement with all pair distances at most $`D>0`$. Assume $`V\ne\varnothing`$ and every
label in $`Z`$ is a contact isolate, so each pair with at least one endpoint in $`Z`$ has
length strictly greater than one. If $`Z\ne\varnothing`$, set

```math
 w=\frac1{|V|}\sum_{i\in V}Q_i,
 \qquad
 \sigma=\min_{\{i,j\}:\{i,j\}\cap Z\ne\varnothing}
             (|Q_i-Q_j|^2-1)>0.
```

For every $`0<t\le\sigma/(8D^2)`$, keep $`Q_i`$ fixed on $`V`$ and put

```math
 Q_z(t)=(1-t)Q_z+tw\qquad (z\in Z).
```

Then the full placement remains unit-separated, its complete unit-contact graph is
unchanged, and every pair incident to $`Z`$ satisfies

```math
 1+\sigma/2\le |Q_i(t)-Q_j(t)|^2<D^2.
```

More precisely, a core-isolate distance is at most $`D(1-t/|V|)`$, and an
isolate-isolate distance is at most $`D(1-t)`$. If $`Z=\varnothing`$, the identity
placement is the normalization and there are no isolate-involving pairs.

### 2. Diameter replacements must lie in the core

Let $`P`$ be the canonical contact-minimal, then actual-diameter-pair-minimal
triangle-free global minimizer in Target C's normal form, with $`D=D(n)\ge9`$. Let
$`V`$ be its nonisolated positive-contact core and retain all source labels. Suppose
$`Q`$ is a unit-separated placement of the same labels, has diameter at most $`D`$,
preserves the complete contact graph of $`P`$, and $`Q|_V`$ is noncongruent to $`P|_V`$.
Normalize the contact isolates of $`Q`$ as in part 1, obtaining $`Q'`$. Let $`L`$ be
the number of old diameter pairs of $`P`$ whose lengths in $`Q'`$ are below $`D`$, and
let $`N_V`$ be the number of formerly non-diameter unordered pairs with both endpoints
in $`V`$ that have length $`D`$ in $`Q'`$. Then

```math
 \boxed{N_V\ge L\ge1.}
```

This is a theorem about an already feasible endpoint. It does not assert that such a
placement $`Q`$ exists.

## Independent proof reconstruction

Because $`V`$ and $`Z`$ are both nonempty, the set of isolate-involving pairs is
nonempty and $`0<\sigma\le D^2-1`$, so $`0<t\le\sigma/(8D^2)<1/8`$.
For each $`z\in Z`$, convexity of the norm gives

```math
 |Q_z-w|=\left|\frac1{|V|}\sum_{i\in V}(Q_z-Q_i)\right|\le D.
```

Thus each moved label has displacement at most $`tD`$; for any pair meeting $`Z`$,
the difference vector changes by at most $`2tD`$. If $`a=Q_i-Q_j`$ is the old pair
vector and $`b=Q_i(t)-Q_j(t)-a`$, then

```math
 |a+b|^2\ge |a|^2-2|a||b|
           \ge 1+\sigma-4tD^2
           \ge 1+\sigma/2.
```

Core-core pairs are fixed. Therefore all lower-distance constraints are preserved,
and no isolate-involving pair becomes a new unit contact.

For $`i\in V`$,

```math
 |w-Q_i|=\left|\frac1{|V|}\sum_{j\in V,\,j\ne i}(Q_j-Q_i)\right|
       \le \frac{|V|-1}{|V|}D.
```

Consequently

```math
 |Q_z(t)-Q_i|
 \le (1-t)|Q_z-Q_i|+t|w-Q_i|
 \le D(1-t/|V|)<D.
```

For two isolates their difference is multiplied exactly by $`1-t`$, so it is at most
$`D(1-t)<D`$. These estimates are simultaneous for every full-source pair; no
contact-isolated point is deleted or left unchecked.

For the second statement, $`Q`$ has the same cardinality as a global minimizer and
$`\operatorname{diam}Q\le D(n)`$, so it is itself a global minimizer. The normalization
keeps all labels, lower constraints, and the exact contact graph, and gives
$`\operatorname{diam}Q'\le D(n)`$; hence $`Q'`$ is also a global minimizer. The
contact graph is the same triangle-free graph as $`P`$, so $`Q'`$ ties the minimal
contact count. Every isolate-involving pair is now strictly below $`D`$.

By canonical `C-ZRF`, every old diameter pair of $`P`$ has both endpoints in $`V`$.
The restriction $`Q'|_V=Q|_V`$ is noncongruent. Every old diameter pair is bounded
above by $`D`$, so the audited `C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN` theorem gives
$`L\ge1`$. The diameter-pair-minimal choice of $`P`$ gives

```math
 |H(P)|\le |H(Q')|=|H(P)|-L+N_V,
```

because all diameter pairs of $`Q'`$ also lie in $`V`$. Thus $`N_V\ge L\ge1`$. The
argument uses the full-source lexicographic minimum and counts every old source pair;
the normalization is what localizes every surviving/new diameter equality to $`V`$.

## Hostile checks and exact limits

- **Exact contact graph:** the strict lower margin $`1+\sigma/2`$ prevents new unit
  contacts; old core contacts are unchanged. A label with an incident unit edge cannot
  be put in $`Z`$.
- **All lower and upper pairs:** the proof bounds every pair incident to an isolate;
  core-core pairs do not move. It does not assume an external scaffold or move only the
  positive-contact core.
- **No deleted isolates:** every label remains. The theorem does not infer a full-source
  affine kernel from the core stress theorem.
- **Globality:** only the second statement uses the canonical global minimizer and its
  secondary diameter-pair minimum. The finite normalization alone is not an optimality
  theorem.
- **Endpoint existence:** neither statement constructs a contact-isometric placement or
  proves its feasibility. The source's Section 4 moment estimate and all its corollaries
  are outside this audit.
- **Uniformity:** $`t`$ depends on the actual finite-source slack σ; no positive
  uniform contraction size across a sequence is claimed.

A useful closure chain is

```text
already feasible full-source contact-isometry with a noncongruent core
  -> normalize all contact isolates without changing contacts or diameter bounds
  -> every lost old diameter pair requires a new core diameter pair
  -> contradiction only if another theorem supplies an endpoint with no such replacement
```

Thus this promotion sharpens an endpoint count but leaves the C-II finite-move/payment
obligation unchanged.

## Verifier audit

The frozen standard-library verifier was inspected and rerun at the source snapshot. It
uses exact rational coordinates and squared distances; it checks an eight-label fixture
with a six-label core, two simultaneous isolates, active upper equalities, exact contact
graph retention, all 84 pair-at-time checks, and two rejected hypotheses (treating a
unit neighbor as an isolate; using an arbitrary external anchor). It also checks the
no-isolate identity case. The verifier does not prove the analytic normalization lemma,
canonical optimality, the core replacement corollary, the cubic moment, or endpoint
existence.

An additional exact rational edge case with two isolates, a retained unit contact, and
minimum isolate slack $`\sigma=2001/1000000`$ was checked at the endpoint value
$`t=\sigma/(8\cdot9)=667/24000000`$. All six squared distances stayed in $`[1,9]`$,
and all five isolate-involving pairs were strictly below the diameter bound and at
squared distance at least $`1+\sigma/2`$.

## Canonical dependencies and disposition

| Claim | Verdict | Dependencies |
| --- | --- | --- |
| `C-FULL-SOURCE-ISOLATE-NORMALIZATION` | PASS — promote | none; finite Euclidean distance argument |
| `C-CORE-DIAMETER-REPLACEMENT-AFTER-ISOLATE-NORMALIZATION` | PASS — promote | `C-FULL-SOURCE-ISOLATE-NORMALIZATION`, `C-ZRF`, `C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN`, canonical contact/diameter-pair lexicographic minimality |
| Source Section 4 cubic moment and support/matching consequences | Not audited; leave unreviewed | `C-INACTIVE-NEAR-DIAMETER-CUBIC-BUDGET`, `C-FS-GEOM` |
| C-II / Level I closure | Not claimed | — |

## Validation and promotion

The frozen candidate verifier passed. Its registered copy additionally includes the exact
near-unit-gap edge case above; that extended verifier also passes. Repository integration
and CI results are recorded in the final handoff and the audit ledger.
