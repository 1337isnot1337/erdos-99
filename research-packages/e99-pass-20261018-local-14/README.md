# PR #950 endpoint-inclusive cut audit

**Disposition: conditional PASS for the separator implication below.** This is
an independent audit of one subclaim in `TARGET-C-PR950-ENDPOINT-INCLUSIVE-CUT-REPAIR`.
The candidate registry and theorem state are unchanged; the broader PR #950
linkage program remains unreviewed here, and C-II and Level I remain open.

Contributor and reviewing agent: OpenAI Codex (GPT-6 Luna xhigh), reviewer slot
`local-14`, in one independent session. Prepared with AI assistance. This
first-party research contribution is offered under Apache-2.0. The reviewed proof
is the published destination copy at baseline
`7d0a450fe66991036541023f95c44c064a04b6a8`,
with theorem state `2026-10-15.publication.2`, priority `public-frontier.3`,
and catalogue `public-frontier.9`.

## Exact statement and hypotheses

Let `C` be the full source unit-contact graph, `I` one unloaded connected
component of the positive-contact core, `A_I` the complete set of loaded source
vertices adjacent to `I`, and `X_D subset I` the connected contact subgraph
selected as the common grid. Assume:

1. every connected unloaded core set `U` under consideration obeys the
   componentwise brace `|delta_C(U)| >= diam(U) + 2`;
2. every source vertex has at most five unit-contact neighbors; and
3. every contact neighbor of `I` that is loaded is included in `A_I`.

Then for every vertex set `S` such that deleting `S` leaves no path from
`A_I - S` to `X_D - S`, including `S` that meets either terminal set or splits
the grid,

```text
diam(X_D) <= 5 |S|.
```

Consequently the minimum endpoint-inclusive vertex separator has size at least
`diam(X_D)/5`. If the source's separate grid-area estimate gives
`diam(X_D) >= (gamma - o(1))D`, vertex Menger yields at least
`(gamma/5 - o(1))D` vertex-disjoint paths with distinct loaded-attachment and
grid endpoints.

This is conditional on the brace and on the source's loaded-attachment,
connected-grid, and grid-diameter hypotheses. The brace itself is a separate
unreviewed candidate in the registry. This audit does not reprove the global
extraction of `I` or `X_D`, audit the other PR #950 corollaries, prove overlap
with train-return labels, pay face costs, construct a feasible move, or close
C-II/Level I. Contact-isolated source labels remain in the full source; this
cut calculation moves or deletes none.

## Independent proof reconstruction

Fix an endpoint-inclusive separator `S`. Let `U_1,...,U_m` be the components
of the contact graph on `I union A_I` after deleting `S` that meet `X_D - S`.
Each `U_j` is wholly unloaded: if it contained a surviving loaded vertex of
`A_I`, that vertex would be connected to `X_D - S`. An unloaded contact
neighbor outside `I` would belong to the same unloaded component, while every
loaded neighbor is in `A_I`; hence every contact leaving each `U_j` ends in
`S`.

Write `e_S` for the number of actual contact edges internal to `S`. Summing
the brace over any chosen subfamily gives

```text
sum_j (diam(U_j) + 2) <= sum_j |delta_C(U_j)| <= 5|S| - 2e_S.       (1)
```

For the second inequality, charge each boundary edge to its endpoint in `S`.
The full contact degree there is at most five; every edge internal to `S` uses
two of those incidences and is not a boundary edge of a `U_j`.

Choose `p,q in X_D` with `|p-q| = diam(X_D)`. Since the grid contact subgraph
is connected, take a simple grid path from `p` to `q` and contract each
component of the deleted graph that meets `X_D-S`. Components can be separated
only through vertices of `S`: an edge between two different components of the
deleted graph would join them. Let `l` be the number of component nodes used,
`e_U` the number of path endpoints lying in such components, and `t_S` the
number of path edges internal to `S`. Each component appears once. Its path
entry-to-exit displacement is at most its diameter, and the number of
component-to-`S` edges on this quotient path is exactly `2l-e_U`. All its
`S`-to-`S` edges are actual contacts, so `t_S <= e_S`. Therefore

```text
diam(X_D)
  <= sum_selected_j diam(U_j) + (2l - e_U) + t_S
  <= 5|S| - 2e_S - e_U + t_S
  <= 5|S|.                                                        (2)
```

The middle inequality uses (1) on the selected path components. If the
quotient path uses only vertices of `S`, it has at most `|S|-1` unit edges,
which gives the same conclusion. If `p` and `q` lie in one remaining component,
then `l=1`, `e_U=2`, and the component-diameter term alone pays for their
separation. If either endpoint is in `S`, it is a retained quotient-path node;
the same accounting applies. Thus the argument does not require the cut to
avoid terminals or leave the grid connected.

The terminal sets are disjoint because `A_I` is loaded and `X_D` is unloaded.
For disjoint terminal sets, vertex Menger with vertex capacities one has the
same value as the minimum separator when separators may delete terminals; in
the node-split formulation the terminal vertices also receive capacity one.
Together with (2), this proves the stated conditional linkage bound.

## Adversarial checks and source comparison

`verify.py` checks an exact finite square-lattice contact fixture. It verifies
the unit-separation, triangle-free, degree, and every connected-subset brace
hypotheses, then enumerates all `2^21` vertex-deletion sets. It checks every
endpoint-inclusive separator against `diam(X)^2 <= 25|S|^2`, with explicit
coverage counts for partial/full terminal deletion and grid splitting. A
separate collinear path control violates the conclusion when the componentwise
brace is omitted; it confirms that the brace is load-bearing, not a
counterexample to the conditional claim. These finite controls do not prove
the universal statement.

The replay checked 218 connected unloaded subsets and all 2,097,152 deletion
sets; 101,250 were separators. Among those, 100,736 partially deleted the
attachment terminal set, 512 deleted it entirely, 4,096 deleted the full grid,
42,920 split the remaining grid into at least two components, and 96,643 left
both terminal sets nonempty. The omitted-brace path control has
`diam(X)=6 > 5|S|=5`, while its chosen connected subset has one boundary edge
and diameter five. These category counts overlap.

The published destination bytes at the pinned base match all four hashes in
the candidate record:

| Artifact | Destination SHA-256 |
| --- | --- |
| `docs/reports/target_c_train_return_length_budget_worker03_2026-10-10.md` | `4ba5214ff20a2548c7e04d01e821f85ea941ffce40dd1ee1d7673c905892941f` |
| `docs/audits/pr950_autonomous_proof_audit_2026-10-15.md` | `8ea063ae82c8d4149fee0d21ab6f2eb0d53a6702c62c162a5dd5cfd08a56bb70` |
| `docs/reports/target_c_full_cell_common_grid_preservation_2026-10-15.md` | `07036803e35a5cf4848d32b6e868edcc30ea883e60349f2f2eaf90ff4e7c3c5f` |
| `research/verify_full_cell_linkage_composition_2026_10_15.py` | `6e2a5a1e84cd43da6f87b86e3e7749b3e6a4b8f66f3edbb573d908fbb13d079b` |

The reviewed source PR #950 is still open at corrected head
`cbf066bb7489115559bcda34f9f810a1d78826ce` (tree
`80dd0d6db99d9aa6698ee6500c91a3f670c63aae`); its original head
`6433d1db49a1363bfa65008eb78f6b15d6ef4ed7` carried the terminal-disjoint-only
cut argument. The source PR's maintenance comment is limited to that original
head; the body separately links a source-side proof audit whose status is
provenance only here. At the destination, candidate registry status remains
`unreviewed`; the only open
destination PR at the live check was the unrelated Target A PR #102, and
Discussion #83 had no PR #950 handoff. The source audit document is preserved
as provenance and comparison, not as a completed destination audit.

I derived (1)–(2) from the report before reading the detailed source audit
record. The live source PR body had already exposed a short summary of that
record during the required overlap check. Comparing afterward, the source
audit and the follow-up report use the same componentwise and quotient-path
accounting; I found no discrepancy in this scoped implication. The follow-up
finite verifier checks a different two-family composition statement and is
not evidence for this separator inequality.

## Reproduction

```sh
flock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock \
  python research-packages/e99-pass-20261018-local-14/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-local-14 --check-only
```

## Open next question

The downstream decision is whether the two linear path families in the PR #950
route share a positive-density set of loaded attachment labels. This cut bound
controls `lambda(A_I, X_D)` but does not control its intersection with the
train-return attachment family. A useful changed hypothesis would be an
upper bound or structural restriction on the complete loaded attachment set
`A_I` that forces common labels; either a proof or a counterexample would decide
whether the two linkages can be composed. First action: formulate a direct
source-wide flow or common-label theorem with explicit capacities at every
attachment. The obstruction is that the existing candidate gives separate
lower bounds only and permits disjoint attachment-label sets.
