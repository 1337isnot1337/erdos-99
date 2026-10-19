# Independent exact-head audit: supplied-packet joint exchange

**Audit result: CONDITIONAL.** On the exact definition in the pinned full
report, the supplied-packet identity and its global-minimizer consequence are
valid. The catalogue's shortened claim says the cross graph `G` *contains*
every actual conflict, without excluding extra edges. Read literally, that
weaker hypothesis is false; use the exact `iff` definition in the report. The
candidate remains unreviewed in the theorem state. This audit does not promote
it or prove packet existence.

## Reviewed objects and source state

- Destination source/head: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- Theorem state: `2026-10-15.publication.2`.
- Priority: `public-frontier.3`; catalogue: `public-frontier.9`.
- Candidate: `GLOBAL-JOINT-DIAMETER-COVER-EXCHANGE-PR957`, frozen source PR
  [#957](https://github.com/1337isnot1337/e-99/pull/957), imported by
  destination PR [#28](https://github.com/1337isnot1337/erdos-99/pull/28).
- Load-bearing report:
  `docs/reports/global_joint_diameter_cover_exchange_2026-10-12.md`, SHA-256
  `b804a22586186c7162cbff4f028b0b2ec3185e0353f9eb47dcd7d77e57a7e8cd`.
- Published verifier:
  `research/verify_global_joint_exchange_2026_10_12.py`, SHA-256
  `86b4f68c0510a7b3d2fea81456728751c3946daf7adcc6ae85a4af13d86f98a8`.
- Candidate registry at the reviewed head:
  `docs/targets/target-c/candidate-registry.json`, SHA-256
  `16b1c0e7c6eb747a954d7310a526543c28a62d7f99206a5537c0c61c83b0f081`.
- Canonical problem definition:
  `docs/problem/statement.md`, SHA-256
  `cd658816999c19ab88bae4d497f3150403dffeb6a8b508e9c92a0ae60bb2926d`.

The report and verifier hashes agree with both recorded source and destination
hashes. The registry also records `docs/audits/pr957_autonomous_proof_audit_2026-10-15.md`
as source-proof provenance, but its recorded destination SHA-256
`76690fa8d2616ef6a5104b77ee9d1c1785a2aafb93355bab4dc3fbece7db72b4` and blob
`a366b97aafc87f7d1bae96cecb32febde7c54e9f` do not match that file at this
reviewed head: actual SHA-256 `a7b0ba682d107135802294b5dc2a70022955f2a90fecada17c0234874f7f00a7`
and blob `3a1d94fb5fca7c01067c18b3966ad2bdee01c060`. The source audit is not a
load-bearing premise here, and the exact theorem report/verifier pins match.

Prior destination evidence was checked before this audit. Merged destination
PR #28 says the source audit was retained as provenance, leaves all three
records unreviewed, and has no GitHub review records. It does not supply the
assigned independent exact-head audit. Current Discussion #83 contains no
handoff for this candidate. The sole open destination PR, #102, concerns a
separate Target A Hall-overlap result.

## Candidate statement and canonical quantity

Let `A` be a finite labelled unit-separated planar source with `n >= 2` and
actual diameter `D > 0`. Let `B` be a separately labelled unit-separated
packet with `m >= 1` and `diam(B) < D`; coordinate coincidences across the two
families are allowed. Define `H` **exactly** by `ij in H iff |a_i-a_j|=D`, and
define the bipartite graph `G` **exactly** by

```text
(i,j) in G iff |a_i-b_j| < 1 or |a_i-b_j| >= D.
```

For every vertex cover `T` of `H`, let `nu_T` be the maximum matching in `G`
induced on the source labels outside `T` together with all of `B`. Then

```text
max {|S| : S subset A union B, S unit-separated, diam(S) < D}
    = n + m - min_T (|T| + nu_T).
```

If `A` is a global minimizer at its cardinality, a supplied `B,T` with
`|T|+nu_T <= m` would produce at least `n` feasible labels of diameter below
`D(n)`, contradicting the definition of `D(n)`. Therefore every supplied
packet and every cover obey `|T|+nu_T >= m+1`. This can affect `D(n)` only
when a packet satisfying that threshold is actually found. It does not provide
the packet for every sufficiently large triangle-free global minimizer that
would close Level I. It makes no C-II endpoint claim.

## Independent proof reconstruction

For any cover `T` of `H`, all pairs in the source labels outside `T` have
distance in `[1,D)`: the
source is unit-separated, its diameter is `D`, and every pair at `D` is covered.
Every pair inside `B` also has distance in `[1,D)`. Thus the only remaining
infeasibilities in the mixed labelled union are precisely the edges of the
induced bipartite cross-conflict graph.

In a finite bipartite graph, the largest independent set has size
`|V|-tau`, where `tau` is the minimum vertex-cover size. König's equality
gives `tau=nu`. One direct proof starts with a maximum matching and an
alternating search from unmatched left vertices; the complement of the
reached-left set together with the reached-right set is a vertex cover of
matching size. A matching supplies the opposite inequality because its edges
are vertex-disjoint. Therefore, for this fixed `T`, the maximum feasible
subset size is

```text
(n-|T|) + m - nu_T.
```

Conversely, for any feasible subset `S`, let `T` be its omitted source labels.
They cover `H`; otherwise two retained source labels would be at distance
exactly `D`. The subset is independent in the cross graph induced by the
source labels outside `T` together with `B`, so its size is no larger than the
fixed-`T` maximum above.
Maximizing over all covers proves the identity in both directions. The
matching-cover equality attains every fixed-cover bound; no assumption that
separate exchanges combine is used.

If the maximum is at least `n`, choose any `n` labels. The conflict graph
excludes coordinate coincidences and every pair at distance at least `D`, so
these are `n` distinct unit-separated points with diameter strictly below
`D`. Integrality makes the negation of `|T|+nu_T <= m` exactly
`|T|+nu_T >= m+1`. This applies to all source labels, including every
contact-isolated label.

The Hall deficiency rewrite is also valid: `m-nu_T = max_{S subset B}
(|S|-|N_{A without T}(S)|)`, with the empty subset allowed. It is a reformulation of
the same supplied-packet criterion, not a construction of `B`.

## Adversarial scope test: exact edges are required

The full report defines `G` with an `iff`, which is sufficient. The registry's
short form instead says `G` “contain every cross pair” satisfying the conflict
condition. If that permits extra edges, the exact identity fails:

```text
A = {(0,0),(2,0)}, D=2; B={(1,0)}.
```

The source is unit-separated, `B` is a unit-separated singleton with diameter
`0 < 2`, and both cross distances are exactly `1`. Thus the true conflict graph
is empty (`1` is neither `<1` nor `>=2`). The actual maximum strict-`D`
unit-separated subset has size `2`, and the exact-graph formula also returns
`2`. If one adds both false cross edges, the cost formula returns `1`. So the
wording should be tightened to “`G` has exactly the conflict edges,” or be
treated expressly as shorthand for the report's `iff` definition.

The report's other relevant scope controls are sound and useful: every actual
diameter pair is in `H`; every `<1` lower cross conflict and every `>=D` upper
cross conflict is in `G`; equality at `D` is forbidden because the target is
strict; coincident labels are lower conflicts; and no source label is silently
removed. The square regression distinguishes failure of one supplied packet
from a universal packet theorem. The all-`k` dense-star construction blocks a
minimum-cover-first shortcut but is explicitly nonglobal. The report also
correctly rejects planarizing the full cross graph, since upper conflicts can
form `K_(4,3)`.

## Reproduction and falsification

The original source checker independently enumerates all 4,096 3-by-3
cross-graph/source-deletion cases against direct matching enumeration, then
checks four exact geometric fixtures with rational squared distances and
exhaustive mixed-subset enumeration. This audit adds `verify.py`, which tests
the formula against direct independent-set enumeration for all 4,096 abstract
3-source/3-packet pairs of diameter-edge graph `H` and cross graph `G`, then
replays the exact rational false-edge control above. The abstract enumeration
checks the graph identity; it does not certify geometric realizability or the
global packet-existence bridge.

Reproduction commands from the repository root:

```text
python research/verify_global_joint_exchange_2026_10_12.py
  PASS: 4096 matching/deletion cases against direct enumeration; JSON replay
  and four certificate-corruption controls. All four geometric fixtures
  passed exact pair-ledger and exhaustive mixed-subset checks.

python research-packages/e99-pass-20261018-homelab-09/verify.py
  PASS: all 4096 abstract 3-by-3 H/G patterns agree with direct independent-set
  enumeration; the exact rational false-edge control predicts 2 under the iff
  graph and 1 after adding false edges, while the true maximum is 2.
```

In this pass, both Python commands were run serially under the assigned shared
compute lock using the provisioned Python 3.14.6 environment.
No repository-wide theorem-certificate suite was run; any required full replay
is deferred to the merging agent. Package metadata continues to list the
unresolved universal packet-existence bridge and the two artifact-specification
discrepancies; finite graph checks do not discharge those obligations.
`python scripts/research_package.py --package research-packages/e99-pass-20261018-homelab-09 --check-only`
reports `metadata-valid`, `full_verified: false`, and `replay_authorized: false`;
its capability scan also leaves dynamic/import closure from the pinned original
verifier unresolved. This is a metadata result, not an isolated replay.

## Classification, predecessor and open question

The review verdict is **CONDITIONAL** on reading the candidate with the exact
`iff` cross-conflict definition from the report. Under that definition the
finite identity and global-minimizer consequence pass this audit. The registry
short form needs the stated clarification; the stale hash for its historical
source-audit provenance should also be corrected before citing that file by
the registry's recorded digest. Neither point changes the proof report's
matching/mixed-subset mathematics. The candidate stays unreviewed and
noncanonical until a separate maintainer decision.

**Open next question.** Can one prove that for every sufficiently large
triangle-free global minimizer `A` there exists a finite unit-separated `B`
with `diam(B)<D(n)` and a cover `T` of the actual diameter graph such that
`nu_T <= |B|-|T|`? This would provide an `n`-point strict-`D(n)` competitor and
close Level I. The audited report proves the consequence only after `B,T` are
supplied. A first bounded step is to propose one source-realized packet with
all lower and upper cross pairs checked, then test whether its joint cost can
meet the threshold without discarding isolates. Stop here: a new search for
that universal packet is outside this assigned exact-theorem audit.

**Provenance and credit.** The theorem report and original verifier are
first-party agent-generated material preserved from source PR #957 and
destination PR #28. The retained source-side audit says it was prepared with
Codex (GPT-6), and explicitly does not satisfy the destination exact-head audit
requirement. No outside mathematical text or data is copied. This audit and
`verify.py` were produced by a separate OpenAI Codex GPT-6 Luna xhigh reviewing
agent; no human mathematical reviewer is claimed. The package is Apache-2.0
compatible and does not change the theorem manifest, priority, canonical
lifecycle, or theorem state.
