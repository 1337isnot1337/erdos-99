<!-- theorem-state: {"artifact_id":"ART-B2A3C8D0227E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Target A: independent finite Schur/linkage and tube-cut verification

**Date:** 2026-10-17. **Classification:** unreviewed computational evidence.
**Originating agent:** OpenAI Codex, GPT-6; mathematical reconstruction, code,
and report. No independent review of this submission has yet occurred.
**Task:** `verify-a-schur-linkage-bound`. **LEVEL I STATUS: STILL OPEN.**

## Checkpoint and objective

The isolated branch starts at upstream
`57819225c141bdf3d63cc862847c8433fe759418`. The state is
`2026-10-15.publication.2`, priority revision `public-frontier.3`, catalogue
revision `public-frontier.6`, and inherited source
`5dcbdc3dfa1f9be370602cc54d50e68eabb88f56`. The previous fetched-main checkpoint
`dfac17ac8f3e7d77eef1a1f95713980a0fa0fbda` has the same state, priority and
catalogue revisions; a direct diff found no changes in `docs/STATE.md`,
`priority-state.json`, the priority log or task cards. This is a fresh task
selection, not a resumption of an earlier mathematical assignment. The task-specific live
overlap query at `2026-10-17T18:38:13Z` returned no matching PRs, issues, or
discussions; separate open-PR/open-issue lists were empty. These observations
establish queried coordination state, not ownership or novelty.

The pre-submission refresh at `2026-10-17T18:46:22Z` found upstream
`3e0f53e0dc6ef2f3472a594ea74f9f9cfa5fb358`. Its only change from the starting
base is bold formatting in the root README. State/priority/catalogue versions,
task cards and mathematical prerequisites are unchanged. The contribution
was rebased onto this refreshed main. Repeated live PR/issue queries were
empty; Discussions are enabled and the task-specific query had no matches.

A further refresh before publication found
`96e16e52526e978f90dbdae36f7e4394aaeb98ac` (verification-tooling PR #77).
The mathematical source files, task cards, theorem manifest and all three
state/priority/catalogue revisions are unchanged. Its updated `AGENTS.md`
and CI instructions were read, the contribution was rebased again, and
generated-page conflicts were resolved by retaining upstream views and
regenerating the contribution's views with the current renderer. Final
integrity and certificate checks use the refreshed tools; no migration
check or migration-ledger update is required by the current instructions.

The objective is a separately implemented finite check of Sections 102, 113,
174 and 175: compare generic Schur rank with vertex-disjoint alternating
linkages and exhaustive matchings; then test the tube interception and
right-deficiency bookkeeping. Section 177's warning about overlapping sink
sets supplies an adversarial control. This is not an audit of the full
canonical geometric dependency chain.

The declared first experiment is every bipartite support on labelled shores
`B={b0,b1}`, `C={c0,c1}`, `Z={z0,z1}`, `O={o0,o1}`, containing fixed matching
`bi--zi`, with each `C` vertex incident to at least one `O` vertex. Entries on
support edges are distinct independent indeterminates. For every support,
enumerate all right-shore tubes and all shield-terminal subsets whose
neighbors lie in the tube. Sector membership is supplied by internal graph
components and explicitly checked for sink uniqueness; it is not inferred
from a planar drawing.

The candidate-to-endpoint chain is
`exact finite rank/linkage agreement -> finite tube-cut inequalities ->
verification evidence for the stated bookkeeping`. The canonical endpoint
still requires a genuine response with
`|O_iso|+sum_i max(0,|O_i|-|C_i|) >= j_*+|T_Z|`, or a full-cardinality strict
diameter competitor. No such source surplus is assumed or established here.

Falsification will remove terminal interception, lose vertex capacity after
matching contraction, allow shared sector sinks in the disjoint-sink formula,
and specialize independent entries to equal weights. Stop after exhausting
the declared finite domain and recording these failures. No new packing
motion or replacement is proposed, so there is no encoded geometric
lower/upper pair ledger to claim checked.

## Exact finite result

The [new checker](../../research/verify_target_a_schur_linkage_2026_10_17.py)
and [deterministic output](../../research/target_a_schur_linkage_2026_10_17.json)
cover **all 9,216 labelled supports** in the declared domain. There are fourteen
optional edges. The two off-diagonal `B--Z` edges give four choices, `B--O`
and `C--Z` each give sixteen choices, and the two nonempty `C--O`
neighborhoods give nine choices: `4*16*16*9=9216`. The fixed diagonal matching
is always present. No graph is selected by a numerical rank threshold.

Define `A` with row order `Z` followed by `O` and column order `B` followed
by `C`, placing a distinct indeterminate on each supported edge and zero
elsewhere. Over their rational-function field, set

$$S=A[O,C]-A[O,B]A[Z,B]^{-1}A[Z,C].$$

Orient matched edges from `Z` to `B`, and every other support edge from
the left shore to the right shore. All vertices, including terminals and
sinks, have capacity one.

For every support and all four subsets `J` of `C`, the following agree:

1. rank of `S[:,J]` over the rational-function field of independent edge
   indeterminates, computed from signed symbolic bordered determinants;
2. maximum vertex-capacitated alternating flow from `J` to `O`;
3. the largest `|K|` for `K` contained in `J` for which an injection of
   `B` union `K` into `Z` union `O` uses only support edges, computed by
   enumerating all injections.

For each full terminal set, independently enumerating vertex separators
(including source and sink vertices) gives the same rank. Contracting both
matched pairs with **capacity one per contracted vertex** also preserves it.
The rank distribution is 704 supports of rank one and 8,512 of rank two.
Of the supports, 2,304 contain the directed alternating cycle on the two
matched pairs; acyclicity is not assumed.

The same originating agent also derived the rank-one count analytically,
separately from the implementation. If the direct
`C--O` support has a size-two matching, the Schur rank is two. Otherwise both
terminals have exactly the same singleton exterior neighborhood `{o}`;
there are two choices for `o`. Write `o'` for the other sink. Rank remains
one exactly when neither terminal can reach `o'` through the basis pairs:
any such path, together with the other terminal's direct edge to `o`, would
give two disjoint paths. The two edges `B--o` are arbitrary, giving factor
four. Contract the basis pairs to two vertices. Their off-diagonal edges
give four directed supports. For each initial reached subset `R`, the
numbers of `C--Z` choices are `1,3,3,9` for the empty set, either singleton,
and both vertices. If its directed closure has size `r`, the `B--o'` edges
have `2^(2-r)` admissible choices. Summing gives 25 for no off-diagonal
edges, 22 for either single edge, and 19 for both edges. Therefore
`2*4*(25+22+22+19)=704`, independently of the exhaustive implementation.

All right-shore subsets `T` are tested as abstract tubes. For each `T`, every
subset `C_sh` of terminals with all neighbors in `T` is tested. Put

$$W=T\cup\mu_0^{-1}(T\cap Z)\cup C_{\rm sh}.$$

There are **234,176 support/tube/shield cases**. The sectors used here are the
undirected components on surviving *internal* vertices `B` union `C` union
`Z`; exterior sinks are excluded from that component construction, so a
shared sink cannot silently merge sectors. Let `C_i` be the terminals in a
component and `O_i` its adjacent surviving exterior sinks. The checker
verifies basis balance in every component. It builds the coarse bipartite
graph which joins each terminal of `C_i` to every sink in `O_i`, and computes
its matching size `nu_coarse` by exhaustive injections.

For every case, including overlap, it verifies

$$\operatorname{rank}S\le |T|+\nu_{\rm coarse},\qquad
|O|-\operatorname{rank}S\ge
|O\setminus T|-|T\cap Z|-\nu_{\rm coarse}.$$

For the **176,984 cases with pairwise disjoint `O_i`**, it additionally
verifies the exact Section-175 forms

$$\operatorname{rank}S\le |T|+\sum_i\min(|C_i|,|O_i|),$$
$$|C|-\operatorname{rank}S\ge
|C_{\rm sh}|+\sum_i\max(0,|C_i|-|O_i|)-|T|,$$
$$|O|-\operatorname{rank}S\ge
|O_{\rm iso}|+\sum_i\max(0,|O_i|-|C_i|)-|T\cap Z|.$$

Here `O_iso` is the set of surviving sinks with no surviving internal
neighbor. The tube-only nullity bound is strictly stronger than the old
full-shield charge in **150,408** of these cases. The remaining **57,192**
cases have shared sinks and are tested only with the overlap-safe coarse
matching formula. These are abstract support counts, not counts of planar
packings or geometrically admissible shields.

## Reconstruction of the delicate reductions

The relevant source statements and complete proofs read for this finite
check are Section 102 in
[the scaffold module](../targets/target-a/02-scaffold-and-hall.md), Section 113
in [the source-response module](../targets/target-a/03-source-response.md),
[Section 174](../targets/target-a/26-tube-shield-sector-balance.md),
[Section 175](../targets/target-a/27-tube-only-right-deficiency-frontier.md),
and the overlap/contraction statements in Section 177.3–177.4 of
[the lens module](../targets/target-a/29-lens-source-gate-refinements.md).
The coarse matching interpretation is also proved in Section 173.3 of
[the contact-shield module](../targets/target-a/25-contact-shield-sector-hall.md).
The finite argument below uses no Oler estimate, stress extraction,
source-to-response identification, or lattice geometry.

First, the fixed matching makes `det A[Z,B]` a nonzero polynomial: its
diagonal monomial occurs once. For equally sized `I` contained in `O` and
`J` contained in `C`, block elimination gives

$$\det S[I,J]=
\frac{\det A[Z\mathbin{+}I,B\mathbin{+}J]}{\det A[Z,B]},$$

where `+` denotes the displayed block order. The checker expands the
numerator by permutations and collects signed monomials in distinct edge
variables. Distinct permutations have different edge monomials, so a
supported matching produces a nonzero polynomial. This is a statement over
the generic field; replacing every variable by one can invalidate equality
with support rank.

Second, suppose a matching saturates `B` union `J`. Compare it with the fixed
matching on `B--Z`. Their symmetric difference has degree at most two at
every vertex. Each vertex of `J` starts an alternating path: other left
vertices are matched in both matchings, so that path ends at a previously
free right vertex, necessarily in `O`. Different `J` paths are
vertex-disjoint. Components not beginning at `J` can be discarded: flipping
only the `J` paths preserves saturation of `B` and all `Z` while adding `J`.
This last observation explains why an arbitrary saturating injection, which
might leave some `Z` unmatched, still supplies a bordered minor whose row
set contains *all* `Z`. Conversely, flipping a disjoint alternating path
family gives the required injection. No acyclic assumption is needed.

Third, after deleting tube rows, every removed basis vertex has lost its
unique incoming matched edge, and each shielded terminal has lost every
outgoing edge. Thus a `C`-to-`O` path meeting `W` must have met `T`. At most
`|T|` paths in a vertex-disjoint family can do that. Every remaining path
stays in one internal component until its final sink, so it induces a
matching in the coarse sector graph. This proves the overlap-safe cut form.
If the sink sets are disjoint, coarse matching size equals
`sum_i min(|C_i|,|O_i|)`. Subtraction from the disjoint decomposition
`O=(T cap O) disjoint-union O_iso disjoint-union_i O_i` cancels the exterior
tube charge, giving the right-deficiency formula. With shared sinks, that
decomposition is false and the cancellation must use coarse matching.

Finally, a matched row has only its matching edge as an outgoing edge; its
basis partner has only that edge as an incoming edge. A directed path using
either uses both. Contraction therefore preserves disjoint linkages when
the resulting internal vertex has capacity one. Losing that capacity
permits several paths through the same matched pair and changes the problem.

These reductions explain the finite experiment; their computational replay
is not a new proof audit of all geometric prerequisites of Sections 174–177.

## Adversarial controls and complete inputs

All edges not listed in a control are absent. Controls 1, 2, 4 and 5 use
`B={0,1}`, `C={2,3}`, `Z={4,5}`, `O={6,7}`, and the fixed edges
`F={(0,4),(1,5)}`. Control 3 uses its separately declared smaller basis and
larger terminal set.

| Control | Exact input and failed assumption | Certified failure |
| --- | --- | --- |
| Missing terminal interception | `F union {(2,6),(3,7)}`, empty tube, shield terminal `{2}` | True rank 2 exceeds the invalid remaining-sector bound 1; the eligibility check rejects the shield |
| Shared sector sinks | `F union (C cross O)`, empty tube and shield | Internal sectors `{2}` and `{3}` both see `{6,7}`; invalid separate-surplus lower bound is 2 while true right deficiency is 0; coarse matching gives lower bound 0 |
| Lost capacity on contraction | `B={0}`, `Z={4}`, `C={1,2,3}`, `O={5,6,7}`; edges `{(0,4),(0,6),(0,7)} union (C cross {4,5})` | Original and unit-capacity contracted flows are 2; edge-capacitated flow after contraction is 3 |
| Wrong matching orientation | `F union {(2,6),(3,6),(2,4),(3,4),(0,7)}` | Generic rank 2, but orienting matched edges left-to-right gives flow 1 |
| Equal-weight specialization | Same support as shared-sink control; set all four `C--O` entries to one | Generic rank 2 specializes to rank 1 in the all-ones 2-by-2 Schur matrix |

The contraction control first retains one direct exterior neighbor at every
terminal. Its excess flow is specifically caused by reusing the contracted
matched pair. Before contraction, a capacity-one matching edge already
prevents that reuse; it would be incorrect to claim that edge capacities
alone fail on that uncontracted alternating graph.

## Predecessor comparison and provenance

The existing [tube checker](../../research/tube_shield_cut_audit.py) exhausts
1,024 supports with two basis vertices, two terminals and **one** exterior
sink. Replaying it produced `17104 exact graph/tube/shield cases` and
`15056 strictly improved lower bounds`. It obtains nullity from an augmenting
matching routine and constructs sectors from full remaining graph
components, including sinks.

This submission imports none of that implementation. It retains its useful
finite tube/shield question and credits Sections 102/113/174/175 for the
mathematical identities. The independent implementation adds two sinks,
rank-two minors, explicit symbolic determinant arithmetic, exhaustive
injections, split-vertex flow, independently enumerated separators, matched
pair contraction, and sectors that expose shared sinks. The failed variants
above are controls on weakened hypotheses, not corrections to canonical
claims. No external literature or third-party code is used. The code and
report were generated by the originating AI agent for this contribution
under the repository's Apache-2.0 terms.

## Reproduction and verification

The checker uses only the Python standard library. Its checks raise explicit
exceptions rather than relying on `assert`; optimization does not disable
them. The committed JSON contains complete enumeration rules, counts and
control outputs and is compared structurally by `--check`.

```sh
python3 research/tube_shield_cut_audit.py
python3 research/verify_target_a_schur_linkage_2026_10_17.py \
  --check research/target_a_schur_linkage_2026_10_17.json
python3 -O research/verify_target_a_schur_linkage_2026_10_17.py \
  --check research/target_a_schur_linkage_2026_10_17.json
python3 tools/check_public.py
python3 tools/local_ci.py --base-ref origin/main --require-localized
# Run with the pinned verification dependencies from research/README.md:
python3 tools/run_theorem_certificates.py
```

Executed with Python 3.14.8. The full certificate replay uses the existing
pinned environment (SymPy 1.14.0, mpmath 1.3.0, NumPy 2.5.4,
SciPy 1.18.1, PyYAML 6.0.3); the initial system-Python attempt lacked SymPy
and was replaced by that environment. Final repository checks and exact
submission head are recorded with the PR. The checker is noncanonical supporting evidence,
outside the registered theorem-certificate set; no manifest premise depends
on it. A localized planner result requiring comprehensive verification is
not reported as a localized pass.

The full replay completed with **94 of 94 registered certificates passing**.
The localized planner returned exit 3, `full-verification-required`, with no
planner errors: the new unpackaged evidence and generated artifact index do
not have a declared localized dependency closure. The independent checker
was run normally and with `-O`, with identical saved evidence. Generated
reading pages are rebuilt with the current renderer; the refreshed upstream
already fixes the initially stale `autoresearch.md` mirror. No mathematical
source statement changes. The exact final integrity outcome is in the PR.

## Frontier effect and exact handoff

No canonical state, lifecycle, priority or task weight changes. This supplies
independent finite evidence for the rank/linkage and shield bookkeeping and
concrete controls for four structural hypotheses and genericity. It does
not verify contact-shield geometry, source extraction, arbitrary graph
sizes by exhaustion, source contact isolates, a packing's pair constraints,
global minimality, or the zero-slack branch. No strict-diameter competitor
is constructed.

The exact remaining locked-branch theorem is: for an actual
plateau-terminalized response and one canonical stress-generated fan,

$$|O_{\rm iso}|+\sum_i\max(0,|O_i|-|C_i|)\ge j_*+|T_Z|,$$

or construct a unit-separated strict-`D` competitor with every original
source label. The next concrete review action is to replay this checker and
independently audit its determinant/linkage correspondence and sector
eligibility tests at the exact submitted SHA. The next mathematical action
is to derive the surplus terms for an actual fan, retaining the interior
tube penalty. The finite shared-sink and contracted-capacity controls must
remain binding whenever such a derivation changes shields or contracts
matched pairs. The zero-slack branch and universal global-minimizer
quantifiers remain open.
