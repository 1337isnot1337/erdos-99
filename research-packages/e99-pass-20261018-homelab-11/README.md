# Independent scope audit: midpoint moments on the full C-II diameter graph

**Reviewed base/tree:** `7d0a450fe66991036541023f95c44c064a04b6a8` / `db766e0e25b562054df26aeec7e627d5a579dd6d`  
**State / priority / catalogue:** `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`  
**Candidate:** `TARGET-C-CII-DIAMETER-EDGE-MIDPOINT-MOMENTS-PR947`  
**Source PR:** [#947](https://github.com/1337isnot1337/e-99/pull/947), head `1afb7e64d47c5619d872d32759b0e01f1526fd5a`, source main base `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`  
**Audit role:** independent AI-agent review of the edge-to-endpoint transfer only; no theorem-state change or promotion.

## Question and verdict

Does the endpoint-partner midpoint tail and moment bound transfer to **every**
actual diameter edge of a canonical C-II source, including diameter pairs not
in a stress-loaded edge set? The affected quantities are the unweighted tail
count and first and second absolute midpoint moments over the complete actual
diameter edge set.

**Verdict: PASS, conditional on the endpoint midpoint bounds.** The transfer is
valid when Woodall's generic straight-line-thrackle classification is applied
to the graph whose vertices are the endpoints of *all* actual diameter pairs.
This direct application matters: the canonical `C-ZRF` stress matrix removes
weak diameter rows, so the topology of that active support alone would not
cover inactive actual diameter edges. The all-edge graph itself has the
diameter-thrackle property and has the required Woodall structure.

The bounds proved here apply for the range of `D` in the upstream endpoint
estimate (the published source proof states sufficiently large `D`; the audit
record gives `D >= 216`). The endpoint estimate is a separate, unreviewed
destination candidate. This audit does not independently establish it.

## Exact conditional statement

Let `A` be a finite noncollinear unit-separated global minimum-diameter source,
with diameter `D`, and let `E_D` be **all** unordered pairs `xy` with
`|x-y| = D`. Let `B` be the set of all endpoints of edges in `E_D`, and let
`o` be the center used by the full-source endpoint theorem. For every map
`p -> p'` selecting one actual diameter partner independently for each
`p in B`, put `m_p = (p+p')/2`.

Assume the published endpoint theorem gives, uniformly over all these partner
choices, `N_B(s) <= C D^2/s^2` for `s >= 4*3^(1/4)*sqrt(D)`, as well as
`sum_B |m_p-o| = O(D^(3/2))` and
`sum_B |m_p-o|^2 = O(D^2 log D)`. Then the same tail and moment bounds hold
over every edge midpoint `m_e=(x+y)/2`, `e=xy in E_D`.

## Independent proof reconstruction

1. Draw every edge in `E_D` as its straight segment. Any two edges sharing a
   vertex meet only at that vertex: distinct length-`D` segments from one point
   cannot overlap on a ray, and opposite rays would put their other endpoints
   `2D` apart. Any two disjoint diameter edges cross in their interiors by the
   planar diameter-graph crossing property. Thus the graph on `B` with edge
   set `E_D` is itself a finite straight-line thrackle. This argument uses all
   diameter edges and no stress support.
2. Apply the generic Woodall classification to this full graph. If it has no
   odd cycle, it is a disjoint union of caterpillar trees. If it has an odd
   cycle, every vertex is adjacent to the cycle. With `q=|B|` and
   `h=|E_D|`, the cycle contributes `r` edges and the other `q-r` vertices
   contribute at least one edge each, so `h >= q`. The planar diameter-graph
   edge bound `h <= q` forces equality: there is one odd cycle and every
   off-cycle vertex is a pendant leaf. In particular the full graph is a
   forest of trees or one unicyclic component with leaves.
3. In each tree, choose a root and assign each edge to its child endpoint.
   In the odd-unicyclic case, assign cycle edges to their cyclic heads and
   pendant edges to their leaf endpoints. The assigned vertices are distinct,
   so this gives an injection `phi:E_D -> B` covering every actual diameter
   edge.
4. For every assigned endpoint `phi(e)`, select the other endpoint of `e` as
   its partner. Choose any actual diameter neighbor for each unassigned
   endpoint. This is an allowed endpoint-partner selection. On assigned
   endpoints, the selected midpoint is exactly `m_e`; all remaining endpoint
   contributions are nonnegative. Therefore for every `s` and `k in {1,2}`,

   `#{e in E_D: |m_e-o| >= s} <= #{p in B: |m_p-o| >= s}` and
   `sum_{e in E_D} |m_e-o|^k <= sum_{p in B} |m_p-o|^k`.

This preserves all source labels in the endpoint theorem: `B` is only the
index set for actual diameter endpoints, while the support function and hull
in the endpoint estimate are built from the full source `A`. Contact-isolated
points need not be vertices of the diameter graph and are not removed from
that full-source geometry.

## Adversarial scope check

The destination's canonical `C-ZRF` scope describes the positive-contact core
and an active diameter-edge set after weak rows are removed; `C-WOODALL` is
recorded for the loaded terminal graph. Merely citing that restricted graph
would leave a real logical gap for inactive actual diameter pairs. I checked
the stronger object directly: the complete graph on all diameter-edge
endpoints is a straight-line thrackle, so Woodall applies before any stress
filtering. This resolves the loaded-versus-full-graph scope seam for this
injection. An abstract graph formed by taking a loaded odd cycle and adjoining
an unrelated component shows why topology of the loaded subgraph alone is not
an adequate premise; it is excluded here by applying the classification to
the full diameter graph, not inferred from the loaded subgraph.

The exact finite checker below tests the tree and odd-cycle endpoint
assignments, including nonnegative tail and moment domination on finite
fixtures. It checks the bookkeeping only; the thrackle classification and
the upstream analytic endpoint estimate are proof inputs, not consequences
of those finite fixtures.

## Evidence and limits

At the reviewed base, the candidate record gives the destination SHA-256
`a815cfd48e4f208a1891b853726897069909704fa0f359dad9f828c12668d797` for
`docs/audits/target_c_diameter_midpoint_mean_tail_independent_audit_2026-10-10.md`;
the working-tree bytes match it (destination Git blob
`b4266040d3e8004984f9fa090b075f915433ef6a`). The candidate record maps this
to source blob `16fcb7a8c1e8552f152709fa24fcdb37542061eb` and source SHA-256
`e4bf989843db0d85a6594d4129eed8cc2c59ec3605442d1ba722c2a219c3c4cf`.
The second-referee note has blob `ae888872f83e4d3520ffe41acaef4f71cc7db600`
and SHA-256 `1a9ab31c0fa492cc56b4c625b279654a69005ad2d531a02da553b707da2a3d52`;
the run-ledger destination is SHA-256
`a113dd7604cad043df72e0fe29cfc8487b808acc6ce0dd86ea1d9d09859f7e7e`.
All three destination files are pinned in `SOURCES.json`. Those predecessor
artifacts are source-PR review evidence; this review records the all-edge scope
check independently. Source PR #947 remains open and unmerged, and the
destination keeps the result unreviewed pending its own lifecycle decision.

This conditional transfer gives no stress-weighted midpoint bound, no
near-diameter pair count, no source-extracted set, no finite motion, and no
C-II or Level-I closure. C-II and Level I remain open. The upstream endpoint
tail/moment proof remains outside this audit's exact scope.

## Reproduction

Run from the repository root:

```sh
python research-packages/e99-pass-20261018-homelab-11/verify.py
python tools/check_public.py
python tools/local_ci.py --base-ref origin/main
```

The finite verifier is a bookkeeping regression, not a proof certificate.
Repository-wide theorem-certificate replay is **deferred to the merging
agent**.

## Attribution

This audit and finite bookkeeping checker were produced by OpenAI Codex,
GPT-6 Luna xhigh, in an independent reviewer session. The predecessor proof
and audits are credited in the pinned source artifacts. The generic
straight-line-thrackle classification is due to D. R. Woodall, “Thrackles and
deadlock,” in *Combinatorial Mathematics and its Applications*, Proc. Oxford
Combinatorial Conference (1969), Academic Press (1971), 335–347. The repository's
[`C-WOODALL` report](../../docs/reports/target_c_woodall_diameter_topology_2026-09-10.md)
records its application to diameter edges. Woodall's author bibliography and
abstract are available at [the author's publication page](https://www.maths.nottingham.ac.uk/plp/pmadw/abstracts.html);
the same generic classification wording appears as Theorem 2.3 in
[Collins and Roberts, *Great-circle Tree Thrackles*](https://arxiv.org/abs/2110.09679).
No third-party paper text is reproduced.
