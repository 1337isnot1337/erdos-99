# Independent destination audit: PR #950 attachment-to-grid linkage

**Verdict: CONDITIONAL PASS for the stated linkage implication.** The conditional
result is still unreviewed in the destination candidate registry; this audit does
not change theorem state or promote any claim.

Reviewer: OpenAI Codex, GPT-6 Luna xhigh, slot local-07. The candidate was
reconstructed from destination main before I read the historical source audit.
I later inspected that audit and the live PRs #108, #112, and #119 to compare
scope and provenance. No human review or external validation is claimed.

## Exact target and source pins

Reviewed destination base: 7d0a450fe66991036541023f95c44c064a04b6a8.
Theorem state: 2026-10-15.publication.2. Priority: public-frontier.3.
Catalogue: public-frontier.9.

| Destination artifact | SHA-256 | Git blob |
| --- | --- | --- |
| docs/reports/target_c_train_return_length_budget_worker03_2026-10-10.md | 4ba5214ff20a2548c7e04d01e821f85ea941ffce40dd1ee1d7673c905892941f | 31c04a46396771ac41d9237e55af1538c0e8af3b |
| docs/audits/pr950_autonomous_proof_audit_2026-10-15.md | 8ea063ae82c8d4149fee0d21ab6f2eb0d53a6702c62c162a5dd5cfd08a56bb70 | 61d91aac5e797ef6fd29aa7d5c7cfa6f6ca7891f |
| docs/targets/target-c/57-zr-zf-rigidity-audit.md | 754086809cdfd077235829e3e7647f3163fd73d9bcdce925097cd1716743ed06 | pinned in SOURCES.json |

The source report is from e-99 PR #950 at corrected head
cbf066bb7489115559bcda34f9f810a1d78826ce. The destination copy adds lifecycle
context and has different bytes from the source report. The imported audit is
also a historical source audit: the destination registry records its original
source SHA-256 as e93ba8c89d98b56b74e6b0f5c96c1b1dd8e28f8d14c8c11b537008ce61221603,
while the destination copy is pinned above. The current destination record says
the candidate is still unreviewed and that no destination audit has validated
this asymptotic linkage.

## Statement audited

Let D tend to infinity along a canonical Type-II quadratic-core sequence. In one
unloaded positive-contact component I_D, assume:

1. X_D is a connected, source-realized actual-contact subgraph supplied by
   TARGET-C-PR950-TYPEII-COMMON-GRID-ACCESS. Its two crossing shores each have at least c_grid D
   vertices for a fixed c_grid > 0, and distinct shore crossings give distinct
   strict unit rhombi with disjoint interiors.
2. Every connected unloaded core vertex set U obeys the brace
   |delta_C(U)| >= diam(U) + 2. The core contact graph is triangle-free and
   planar, has maximum contact degree at most five, and the complete set A_I of
   loaded source vertices adjacent to I_D is used.
3. C-ZRF applies to the nonisolated positive-contact core V, with no strong
   active diameter row incident to an unloaded set. Contact-isolated source
   labels remain in the full source.

Writing a_0 = sqrt(3)/2, the grid area and isodiametric inequality give

    area(conv(X_D)) >= a_0 c_grid^2 D^2,
    diam(X_D) >= gamma D,  gamma = c_grid sqrt(2 sqrt(3) / pi) > 0.

The brace and the endpoint-inclusive cut argument give every separator S
between A_I and X_D size at least diam(X_D)/5. Vertex Menger therefore gives
at least (gamma/5 - o(1))D pairwise vertex-disjoint actual-contact paths, with
distinct loaded attachments and distinct grid endpoints.

For each fixed theta in (0,1), finite Oler on the entire unit-separated source
gives n_D <= pi D^2/(2 sqrt(3)) + pi D/2 + 1. If ell_i is the edge count of
the Menger paths, disjointness gives sum_i(ell_i+1) <= n_D. Thus at least
(theta gamma/5 - o(1))D paths have at most

    5 pi / (2 sqrt(3) (1-theta) gamma) D

contact edges. This Oler count includes every source label, including contact
isolates.

The dependency graph records canonical C-ZRF,
C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY, C-HARMONIC-CELL-TILING,
C-COHERENT-GRAINS, and C-PSEUDO-GRID inputs, plus the separate candidate
relations TARGET-C-PR950-TYPEII-COMMON-GRID-ACCESS,
TARGET-C-PR950-UNLOADED-RIGIDITY-BRACE, and
TARGET-C-PR950-ENDPOINT-INCLUSIVE-CUT-REPAIR. This audit reconstructs the
brace and cut implications used here, but does not re-audit how the common
grid is extracted from the canonical inputs. That grid-access relation remains
unreviewed in the destination.

## Independent proof reconstruction

For a connected unloaded X, straight unit-contact edges cannot cross: if two
unit segments cross in their interiors, the squared distances of the two
opposite endpoint pairs sum to strictly less than 2, contradicting unit
separation. Triangle-freeness makes every face of a 2-connected contact block
have length at least four. If B is such a block with outer facial length p_B,
Euler's formula gives e_B <= 2v_B - p_B/2 - 2. A bridge block contributes
2v_B - e_B - 2 = 1. The block-cut identity
v_X = 1 + sum_B(v_B-1) therefore yields

    2v_X - e_X >= 2 + sum_(2-connected B) p_B/2 + number_of_bridges
                 >= diam(X) + 2.

For the last step, p_B/2 is at least the Euclidean diameter of the block:
the outer cycle encloses its vertices and any curve enclosing two points has
length at least twice their distance. Along the block-cut path between a
diametral pair, the sum of block diameters bounds their Euclidean separation.
The one-vertex and bridge-only cases also satisfy the inequality.

The contact rows internal to X have rank at most e_X, so their infinitesimal
flex space has dimension at least 2v_X-e_X >= diam(X)+2. If fewer than
diam(X)+2 actual contacts leave X, their linear equations leave a nonzero
flex that vanishes on all crossing rows. Extending it by zero to the rest of
the core satisfies every contact and strong diameter row because X is
unloaded. C-ZRF says the mixed framework on V has rank 2|V|-3, so this flex
must be a rigid motion. It vanishes at the two distinct fixed endpoints of
an active diameter edge outside X, which forces that rigid motion to be zero,
a contradiction. This proves the conditional brace.

Now fix any endpoint-inclusive vertex separator S in the contact graph on
I_D union A_I: after deleting S, no surviving vertex of A_I-S connects to
X_D-S. Each component U_j meeting X_D-S is wholly unloaded. Every actual
contact leaving U_j ends in S: unloaded neighbors remain in I_D, and a
loaded neighbor outside S would be in the complete attachment set A_I-S and
would connect U_j to X_D-S. Since every source vertex has at most five
contact neighbors and e_S counts contacts internal to S,

    sum_j (diam(U_j)+2) <= sum_j |delta_C(U_j)|
                         <= 5|S| - 2e_S.                 (1)

Choose diametral p,q in X_D and a simple contact path between them inside the
connected subgraph X_D. In the quotient by the deleted components visited by
this path, let l be the number of component nodes, e_U the number of path
endpoints in components, and t_S the number of path edges internal to S.
There are 2l-e_U component-to-S edges and t_S <= e_S. The Euclidean
triangle inequality, (1), and the two units in each brace give

    |p-q| <= sum_j diam(U_j) + 2l-e_U+t_S
           <= 5|S| - 2e_S - e_U + t_S
           <= 5|S|.

If the path lies entirely in S, its simple unit-edge path has at most
|S|-1 edges and the same bound follows. This covers cuts that delete
terminals, split the remaining grid, or put a diametral pair in one
component. The path is chosen inside X_D, so every deleted component it
visits meets X_D-S and is covered by the brace sum. Endpoint capacities are
one; endpoint-inclusive Menger therefore supplies distinct endpoints as
well as vertex-disjoint paths.

Finally, for the Menger family, each path with ell_i edges contains ell_i+1
distinct labels, and the paths are vertex-disjoint. Full-source Oler gives

    n_D <= pi D^2/(2 sqrt(3)) + pi D/2 + 1,
    sum_i ell_i <= n_D - K_D.

For paths longer than tD, each contributes more than tD to this sum, so
their number is at most pi D/(2 sqrt(3)t) + o(D). Subtracting from
K_D >= (gamma/5-o(1))D and choosing
t = 5 pi/(2 sqrt(3)(1-theta)gamma) proves the claimed quantile.

## Adversarial checks and finite controls

The main interface risk is the use of all actual loaded neighbors A_I. If an
arbitrary subset were used, a component boundary could contain uncharged
loaded contacts, invalidating (1). Restricting separators away from terminals
would also be insufficient for distinct-endpoint Menger. The proof instead
uses endpoint-inclusive cuts and the complete attachment set. It needs a
connected X_D and a fixed positive gamma; no path-count conclusion follows
from shore size alone without the disjoint-rhombus area and diameter step.

I replayed the exact 21-vertex square-lattice finite control from PR #112,
head fd02d4d36b1953a217680d889ce830f894a41096. The source checker was
downloaded from that immutable head, SHA-256
c47f7878280e1ea47e8de0231199d6a91006543a74bd388c1ead414e58daf4aa, and is
copied unchanged as verify.py with its provenance retained. The exact command
was:

    flock -x /home/cinna/.local/state/erdos99-host-compute.lock python /tmp/e99_pr112_cut_verifier.py

Actual output: 218 connected unloaded subsets passed the exact brace check;
all 2,097,152 deletion sets were enumerated, with 101,250 separators,
including partial-terminal, full-attachment, full-grid, grid-splitting,
both-terminal-surviving, and diametral-endpoint-deletion cases. The missing-
brace control has diam(X)=6 > 5|S|=5 and boundary 1 < diam(U)+2=7.
The checker uses integer coordinates and squared distances.

This is a finite square-lattice control only. It does not prove the universal
brace, the common-grid extraction, C-ZRF, the asymptotic Menger count, or
global minimality. In particular, the candidate report contains no finite
checker for the Oler quantile; that step is checked analytically above using
the full source population.

## Lifecycle, overlap, and remaining lemma

The destination candidate registry still classifies
TARGET-C-PR950-ATTACHMENT-GRID-LINKAGE as unreviewed. The source-side audit
and its corrected endpoint cut are provenance, not this destination review.
The live open PRs are complementary: #119 audits the brace; #112 audits the
endpoint-inclusive cut; #108 audits the positive-length return quantile and
explicitly excludes attachment-to-grid linkage. The common-grid extraction
remains a separate unreviewed dependency. Discussion
#83 and the predecessor handoffs have no exact attachment-grid audit.

The current Type-II track also links
docs/reports/target_c_full_cell_common_grid_preservation_2026-10-15.md
(destination SHA-256 07036803e35a5cf4848d32b6e868edcc30ea883e60349f2f2eaf90ff4e7c3c5f),
a source-main follow-up variant of the same PR #950 program. Its Section 3
repeats the brace/cut/area/Menger/Oler linkage implication; its Sections 1-2
use a distinct full-cell common-grid route, and Section 4 proves a separate
finite two-family composition lemma. The registry keeps that variant and its
composition candidate unreviewed. This review is pinned to the original
destination report above and does not validate the full-cell extraction or
the composition lemma; the latter's finite checker is not evidence for the
analytic attachment-to-grid cut.

This result controls only the number and length quantile of disjoint
attachment-to-grid contact paths. It does not imply overlap with the separate
train-return attachment labels, path congestion bounds beyond the stated
disjoint family, stress-mass payment, an infinitesimal or finite motion, or a
same-cardinality competitor. The next lemma is a positive-density overlap of
those attachment labels, or a direct flow theorem from selected train roots
to the common grid. Then a full-source endpoint must still preserve every
lower pair and every old or newly active upper pair, retaining all isolates.
Level I and C-II remain open; C-I remains closed.

Source PR #950 / Worker Slot 03 is credited for the report and its proof.
The finite control is credited to PR #112 and is reproduced byte-for-byte.
This package adds an independent destination proof reconstruction by OpenAI
Codex (GPT-6 Luna xhigh, local-07). No third-party text or theorem is
reproduced. Required repository-wide theorem-certificate replay is deferred
to the merging agent.
