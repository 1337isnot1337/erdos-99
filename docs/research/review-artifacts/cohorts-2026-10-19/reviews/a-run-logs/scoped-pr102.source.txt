<!-- theorem-state: {"artifact_id":"ART-E6CEB840E77E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Target A: exact two-shore source-image overlap via Hall deficiency

**Status:** unreviewed finite-incidence lemma and rational regression; no canonical theorem promotion.  **Date:** 2026-10-17 (America/Chicago).  **Upstream main:** `7d0a450fe66991036541023f95c44c064a04b6a8`.  **Theorem state:** `2026-10-15.publication.2`. **Priority:** `public-frontier.3`; **catalogue:** `public-frontier.9`.  **Task:** `target-a-zero-slack-source-transfer` (also relevant to `verify-a-source-capacity-coupling`).

## Question and downstream decision

Section 168.2 supplies independently saturating strict-conflict matchings from the full response shores `X*` and `Y_in` into the same maximum-cardinality source `A0`. Section 177.5B restricts them to `C^partial` and `O` and forms a V-gate `c-a-o` for each common source-image label. The existing gate floor uses a generic `20d+25` boundary-band capacity, and the repository's later population audit shows this floor can be vacuous.

The decision affected by this note is whether **actual source incidence**, rather than just boundary-band population, can certify a nonzero number of common-source gates. The quantity is the maximum matching number of the *combined* strict-conflict graph. A positive result supplies gate candidates; it does not by itself change `rank S`, the Section-175 tube charge, or the global Target A endpoint. The falsification test is to compare the proposed exact identity to all small source-incidence graphs and distinguish restricted-shore matchings from restrictions of full-shore matchings.

## Lemma: the exact unrestricted two-shore overlap

Let `C` and `O` be finite **disjoint labelled** demand shores, `A` a finite source shore, and `E` any bipartite incidence relation on `(C sqcup O) x A`. Assume `C` and `O` each have a matching saturating their entire shore (not necessarily the same matching). Write `nu` for the maximum matching cardinality in the combined graph, and

`delta = |C| + |O| - nu = max_{U subset C sqcup O} (|U| - |N_A(U)|)_+`.

Then, over all independently chosen matchings `M_C:C -> A` and `M_O:O -> A` saturating their respective shores,

`min |im(M_C) cap im(M_O)| = delta`.

**Proof.** For any pair of saturated matchings put `I=im(M_C) union im(M_O)`. For each distinct `a in I`, choose one incident matched demand vertex. These chosen edges form a combined matching of size `|I|`: the source endpoints differ by construction, and no demand vertex was matched twice within its own shore. Consequently `|I| <= nu`, and inclusion-exclusion gives `|im(M_C) cap im(M_O)| = |C|+|O|-|I| >= delta`.

Conversely take any combined matching of size `nu` and restrict its edges separately to `C` and `O`, obtaining two partial matchings. Because each whole shore is independently saturable, the standard augmenting-path theorem extends each partial matching to a saturating matching on that shore. During augmentation, **every previously occupied source vertex remains occupied**: an alternating augmenting path begins at an unmatched demand vertex and ends at a previously unused source vertex, with all intermediate used sources remaining matched. Thus the union of the two final image sets contains the source set of the original combined matching, of size `nu`. The first paragraph bounds that union by `nu`, so its size is exactly `nu` and the overlap is `delta`. Hall's maximum-deficiency formula yields the alternative expression. QED.

The construction proves **existence among arbitrary restricted-shore matchings**. It does not guarantee that such a pair can be extended to separately saturate larger specified shores `X* superset C` and `Y_in superset O`.

## Section-177 consequence and its limit

For the actual Section-168 zero-slack source, take adjacency to mean strict Euclidean distance below one. Restrict *any* two full-shore saturating matchings to `C=C^partial` and `O`. Since these restrictions are valid independent matchings, their common image population `L` always satisfies

`L >= delta_A(C,O) := |C|+|O|-nu_A(C sqcup O)`.

Assuming the geometric crossing/interference argument of Theorem 177.5B, each common source gives one V-gate and at most nine other gate paths interfere with any given one. Therefore its greedy selection gives the conditional **source-incidence-specific** bound

`G_CO >= ceil(delta_A(C,O) / 10)`.

The boundary-band upper bound used in Section 177.5A also implies `nu_A(C sqcup O) <= 20d+25` (indeed the union of *all* strict source neighbors of `C sqcup O` lies in the two-sided width-two boundary band). Hence this bound is at least as strong as the old nonnegative floor `(|C|+|O|-20d-25)/10`, but may be positive when that floor is zero. It requires actual source-incidence information: neither global minimum-diameter geometry nor the Schur nullity gap is supplied by the identity.

**Important distinction.** The unavoidable overlap under restrictions of *full* response-shore matchings may be strictly larger than `delta_A(C,O)`. To see this, let the source labels be `a,b`, full shores `U={c,u}` and `V={o,v}`, and allowed incidence sets `N(c)=N(o)={a,b}`, `N(u)=N(v)={b}`. The restricted graph on `{c,o}` has a size-two matching and `delta_A({c},{o})=0`. But the unique separate full-shore matchings send both `u,v` to `b`, forcing both `c,o` to `a`, with overlap one. This abstract control is not claimed to be a canonical planar packing; it rejects an overstrong equality assertion for inherited full-shore matchings. The lower bound above remains valid.

## Exact evidence and predecessor

The independent standard-library verifier `research/verify_target_a_common_source_overlap_2026_10_17.py` enumerates all `2^(n(|C|+|O|))` incidence matrices for the declared six shapes `(1,1,2), (1,1,3), (1,2,3), (2,2,3), (2,2,4), (1,3,4)`, retaining only graphs where each shore is saturable. Across **98,212** such graphs, a direct enumeration of source-image masks agrees with an independent combined-matching dynamic program and a brute-force Hall-subset computation. **22,266** have strictly positive forced overlap. Full-shore assignments are enumerated separately for the extension control.

It also reproduces the exact **rational** five-source configuration from [PR #98](https://github.com/1337isnot1337/erdos-99/pull/98), whose `C` and `O` source-incidence masks are respectively `(1,2,4)` and `(1,2)`. There are three distinct combined source neighbors for five demand vertices; maximum matching size is three, and both direct minimum overlap and Hall deficiency are two. Exact rational squared-distance tests confirm both incidence masks and unit separation within all three sets. The previous report already explains why its geometry is **nonglobal** and does not realize Section 168's zero-slack hull-capacity assumptions. This note adds the general exact incidence identity, independent enumeration, and full-shore extension distinction; it does not claim a second novel geometric counterexample.

Run from repository root with assertions enabled:

```sh
python3 research/verify_target_a_common_source_overlap_2026_10_17.py
python3 tools/check_public.py
```

The independent code does not inspect every canonical Schur variable or certify that `C`, `O`, and `A0` come from one global source. Test output documents exact graph counts and controls. Repository-wide theorem-certificate replay is **deferred to the merging agent**; it has not been run for this contribution.

## Open next questions

The missing implication is a **source-extraction comparison** involving `delta_A(C,O)` and the Section-175 or Section-177 rank/nullity currency. A larger `delta_A(C,O)` proves more geometrically disjoint source gates, but does not require these gates to traverse a contact shield, avoid one another in the Schur alternating network, or produce the needed rank deficiency. A useful next experiment is an **actual Section-168 co-phased response/source fixture**, retaining all contact isolates and both full-shore incidence maps, where one computes `delta_A`, the minimum overlap under full-match extension, the Schur rank, and the precise shield/tube cost together. Either a sharp positive coupling or a counterexample with its missing geometric hypothesis would change this decision. Stop if the experiment only reproduces abstract Hall deficiency or another arbitrary overlapping matching.

**Credit and review:** OpenAI GPT-6 derived the lemma, implemented the finite checker, reconstructed PR #98's rational incidence regression, and wrote this note. Predecessors are Sections 168, 175 and 177 and PR #98. No independent agent review has been performed. Source code and new prose are offered under this repository's Apache-2.0 terms.