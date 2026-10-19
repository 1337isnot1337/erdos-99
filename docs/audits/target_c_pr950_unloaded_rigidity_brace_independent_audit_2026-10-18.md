<!-- theorem-state: {"artifact_id":"ART-8E0E780DA596","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit of the PR #950 unloaded rigidity brace

**Review verdict:** PASS for the boundary-contact brace lemma only, conditional on
the canonical `C-ZRF` input and the exact scope below. This audit does not accept
the other PR #950 corollaries, update the candidate registry, or promote a theorem.

**Reviewed destination base:** `7d0a450fe66991036541023f95c44c064a04b6a8`  
**Theorem state:** `2026-10-15.publication.2`  
**Priority / catalogue:** `public-frontier.3` / `public-frontier.9`  
**Candidate:** `TARGET-C-PR950-UNLOADED-RIGIDITY-BRACE`  
**Reviewing agent:** OpenAI Codex, GPT-6 Luna xhigh, homelab-13; independent
review session. I did not author, edit, or verify the source proof or its checker.

## Exact artifacts and lifecycle

The destination report bytes at the reviewed base are
`docs/reports/target_c_train_return_length_budget_worker03_2026-10-10.md`,
SHA-256 `4ba5214ff20a2548c7e04d01e821f85ea941ffce40dd1ee1d7673c905892941f`.
The imported source-side audit is
`docs/audits/pr950_autonomous_proof_audit_2026-10-15.md`, SHA-256
`8ea063ae82c8d4149fee0d21ab6f2eb0d53a6702c62c162a5dd5cfd08a56bb70`.
Both match the hashes in the assigned candidate record. The source report traces
to PR #950 head `cbf066bb7489115559bcda34f9f810a1d78826ce` in
`1337isnot1337/e-99`.

The destination candidate record is still `unreviewed`, and its validation says
that a destination independent audit had not been performed. The imported audit
also explicitly says it is source-side provenance. Discussion #83 has no handoff
for this candidate; the only open destination PR at the launch snapshot is PR
#102, whose Target A Hall-overlap formula and full-shore extension countermodel
are separate work. I reconstructed the lemma below before reading the imported
source-audit conclusions. The current destination candidate lifecycle remains
unchanged by this report.

## Audited statement and hypotheses

Let (P) be a canonical contact-minimal, then actual-diameter-pair-minimal,
triangle-free global minimizer in the C-II sequence, with (D\ge9). Let (V)
be its nonisolated positive-contact core, (C) its actual unit-contact edges,
and (H) the strong active actual-diameter rows used by canonical `C-ZRF`
(weak diameter rows have been removed). For any nonempty (X\subseteq V) that
is connected in the actual unit-contact graph and has no endpoint incident to
an edge of (H), write (q=|X|), (e_X=|E(G[X])|), and let
\(\delta_C(X)\) be the actual unit contacts with exactly one endpoint in (X).
Then

\[
|\delta_C(X)|\;\ge\;\operatorname{diam}_{\mathbb R^2}(P(X))+2.
\]

The diameter here is Euclidean diameter in the source embedding. The claim is
about core labels and the mixed framework on (V). Contact-isolated source
labels remain part of the full configuration but are not assigned core
coordinates, counted as vertices of (X), or removed from the source.

## Independent reconstruction

First, the straight unit-contact graph is planar. If two nonincident unit
segments cross in their interiors, let the crossing divide them into lengths
\(s,1-s\) and \(t,1-t\), with (0<s,t<1). Choose the two endpoint pairs in
opposite acute sectors; if \(\phi\le\pi/2\) is the angle between the selected
rays, their squared distances sum to

\[
s^2+(1-s)^2+t^2+(1-t)^2
-2\cos\phi\,[st+(1-s)(1-t)] < 2.
\]

Each distance is between two distinct source labels and must be at least one,
so their squares must sum to at least two. This contradiction excludes the
crossing. The induced graph is triangle-free because the source is triangle-free.

For every 2-connected plane block (B\subseteq G[X]), let (p_B) be its outer
facial-cycle length. Every face has length at least four. With Euler's formula,
\(f=e_B-|V(B)|+2\), and the inner-face lower bound,
\(2e_B\ge p_B+4(f-1)\), so

\[
|E(B)|\le 2|V(B)|-p_B/2-2.
\]

For each bridge block (B),
\(2|V(B)|-|E(B)|-2=1\). The block-cut identity
\(q=1+\sum_B(|V(B)|-1)\) therefore gives

\[
2q-e_X
=2+\sum_{B\text{ 2-connected}}(2|V(B)|-|E(B)|-2)
  +\#\{\text{bridge blocks}\}
\ge 2+\sum_{B\text{ 2-connected}}p_B/2
  +\#\{\text{bridge blocks}\}.
\]

Take a pair of vertices realizing the Euclidean diameter of (P(X)). Its
block-cut-tree path uses a sequence of blocks. In a 2-connected block, the
outer cycle encloses the block and its perimeter is at least twice the
Euclidean diameter of its vertices; a bridge contributes its unit length.
Applying the triangle inequality along the block path shows that the sum of
\(p_B/2\) and bridge contributions on this path is at least
\(\operatorname{diam}_{\mathbb R^2}(P(X))\). Off-path blocks contribute
nonnegative terms. Thus

\[
2q-e_X\ge \operatorname{diam}_{\mathbb R^2}(P(X))+2.
\tag{1}
\]

The rigidity matrix of (G[X]) has rank at most (e_X), hence its infinitesimal
flex space has dimension at least the left side of (1). If
\(|\delta_C(X)|<\operatorname{diam}(P(X))+2\), the crossing-contact rows add
fewer constraints than this dimension. A nonzero flex of (G[X]) then satisfies
all rows crossing from (X) to (V\setminus X). Extending it by zero to the
rest of (V) satisfies every contact row. No strong diameter row is incident
to (X), so it also satisfies every row of (H).

Canonical `C-ZRF` gives rank \(2|V|-3\) for this mixed framework, so its kernel
contains only Euclidean rigid motions. Canonical `C-ZRF` also gives
\(|H|\ge\lceil D\rceil\), so an active diameter edge exists; both of its
distinct endpoints are outside (X) and fixed by the extension. A Euclidean
infinitesimal motion vanishing at two distinct points is zero. The constructed
nonzero flex is therefore not a rigid motion, contradicting `C-ZRF`. This
proves the boundary inequality.

## Adversarial scope checks

- **One vertex:** (q=1,e_X=0), so (1) is exactly (2\ge0+2). A boundary
  cut of size at most one leaves a nonzero two-coordinate flex after its
  crossing rows are imposed.
- **Bridge path:** with (b) bridge blocks, (q=b+1,e_X=b), and
  (2q-e_X=b+2\). Its Euclidean diameter is at most the sum (b) of its unit
  edges, so the bound covers the path case including equality for a straight
  chain.
- **Articulations:** only blocks on the block-cut path between a diametral pair
  are needed to pay its Euclidean distance; branches off that path add
  nonnegative terms to (2q-e_X-2\).
- **Loaded anchors:** the contradiction uses an edge of the same strong set
  (H) appearing in `C-ZRF`. It does not rely on arbitrary placement pins or
  on a diameter row omitted from that matrix.
- **Isolates and weak rows:** isolates are outside (V) by definition. The
  flex is only a vector on (V), and the lemma does not assert a full-source
  motion. The conclusion uses the exact strong-row notion of unloaded; it
  does not silently include weak diameter rows in (H).
- **Metric and graph scope:** the diameter paid is Euclidean, not graph
  distance. Connectedness is in the actual unit-contact graph, and the cut
  counts actual contacts in the canonical source, not scaffold edges.

I found no gap in this implication under these hypotheses. No finite verifier
is supplied or needed for the unbounded block-counting argument; these checks
are exact proof reconstruction, not numerical evidence.

## Limits and next missing lemma

This PASS is restricted to the brace inequality. It does not independently
audit the report's train-return quantile, Type-II common-grid extraction,
endpoint-inclusive Menger assembly, or Oler estimates. It yields no positive
KKT weight bound on boundary contacts, no stress-mass payment, and no finite
source-wide competitor satisfying every lower and active/inactive upper pair
constraint. The report's two linkage endpoint families can still have disjoint
labels. Contact isolates remain in the original full source throughout.

The next missing lemma for using this candidate downstream is a positive-density
endpoint overlap between the train-root-to-loaded-attachment family and the
loaded-attachment-to-grid family, or a direct source-wide flow theorem with
the same actual labels. That changes the quantity from two separate linear
path counts to a linear count of composable source paths; either a positive
bound enables a train-root-to-grid linkage, while a counterexample would rule
out this composition route without an additional hypothesis. Even a successful
overlap result would still need a finite move or discrete replacement checking
all source pairs and retaining every source label.

The report and this audit are first-party mathematical work contributed under
the repository's Apache-2.0 contribution terms. The source PR #950 report and
its source-side audit retain their provenance and credit. This audit copies no
third-party paper text. AI roles are stated above; no human mathematical review
or external validation is claimed.
