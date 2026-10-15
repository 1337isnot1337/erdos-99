<!-- theorem-state: {"artifact_id":"ART-0F9326ECA9C8","canonical":true,"claim_ids":["C-DIAMETER-LEAF-CONTACT-INCIDENCE"],"claim_statuses":{"C-DIAMETER-LEAF-CONTACT-INCIDENCE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: diameter-leaf contact incidence

Date: 2026-10-08. Audit base: `origin/main=f7a94825acb709ad278ffd9160fa0915b7fa1201`, state `2026-10-07.audit.118`; Target C C-II remains open.

Frozen source: `origin/swarm/sol/contact-convexity-exclusion-20261002` at `b79aa0cfd8ceb2d10685890fe06b12a71607745b`. Source report `docs/reports/target_c_finite_core_rigidity_and_cut_anchoring_2026-10-02.md`, SHA-256 `3e28bda1b7b64d86a220d77aae1ee036a4cd47770a1ef9ead556082669bbc99d`.

## Verdict

**PASS — promote `C-DIAMETER-LEAF-CONTACT-INCIDENCE`.** The source report's Section 4.2 inequality is correct for the canonical `D>=9` source. Its exact loaded-loaded accounting is valid, and the claimed `2d_H` leaf lower bound follows from canonical Woodall topology. The theorem does not assign contacts to distinct faces, trains, or components and does not change the active C-II frontier.

## Exact statement and scope

Use the canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer with `D>=9`. Let `V` be the nonisolated positive-contact core, `C` all actual unit-contact edges on `V`, `H` the full actual diameter graph, `B` its loaded endpoint set, `q=|B|`, `h=|E(H)|`, and `d_H=q-h`. Let `ell_H` be the number of degree-one vertices of `H`, `e_BB` the number of contacts with both endpoints in `B`, and `t_BI` the number of contacts with one endpoint in `B` and one in `V minus B`. Then

\[
\boxed{
t_{BI}+2e_{BB}
=\sum_{b\in B}\deg_C(b)
\ge q+\ell_H
\ge q+2d_H.
}
\]

All graphs and contacts in this statement are the actual source objects. Every actual diameter endpoint belongs to `V`; contact-isolated source labels are not included in `B` or `V`.

## Independent proof reconstruction

First, every actual diameter endpoint `b` is a strictly exposed source-hull vertex. Choose `p` with `|b-p|=D` and set `u=(b-p)/D`. For every other source point `x`,

\[
u\cdot(x-p)\le |x-p|\le D=u\cdot(b-p),
\]

and equality at the right endpoint forces `x=b`. Thus `u` strictly exposes `b`. In the canonical relative-interior stress, every actual diameter edge has positive coefficient. If `b` had no contact edge, its equilibrium equation would consist only of the negative diameter-force terms. Taking its dot product with `u` gives a strictly negative sum, impossible. Therefore every `b\in B` has `deg_C(b)\ge1`. This also verifies the loaded-endpoint/contact-support premise directly, rather than importing it as an unexplained phrase.

Next, `C-ZRF` gives `h\ge\lceil D\rceil\ge9`, so the simple mixed graph has at least five vertices. Its three-vertex connectivity implies minimum mixed degree at least three: if a vertex had at most two neighbors, deleting those neighbors would leave it isolated and at least one other vertex. Therefore, if `b` is a degree-one vertex of the full diameter graph `H`,

\[
\deg_C(b)=\deg_{C\cup H}(b)-\deg_H(b)\ge3-1=2.
\]

Summing over loaded vertices gives

\[
\sum_{b\in B}\deg_C(b)
\ge 2\ell_H+(q-\ell_H)=q+\ell_H.
\]

For `d_H>0`, canonical `C-WOODALL` says `H` is a forest of exactly `d_H` caterpillar components. Since every vertex of `H` is loaded and has positive diameter degree, these components are nontrivial; each has at least two leaves. Hence `ell_H\ge2d_H`. For `d_H=0`, `ell_H\ge0=2d_H` is immediate.

Finally, each contact from `B` to `V minus B` contributes once to `\sum_B deg_C`, while each loaded-loaded contact contributes twice. Thus

\[
t_{BI}+2e_{BB}=\sum_{b\in B}\deg_C(b),
\]

which proves the displayed bound.

## Sharpness and scope checks

- The exact unit square has four loaded vertices, two diameter diagonals, `q=4`, `h=2`, `d_H=2`, four diameter leaves, four loaded-loaded contact sides, and no loaded-to-unloaded contacts. Both sides of the bound equal eight. Each diameter leaf has exactly two contacts, so a universal three-contact-per-leaf bound is false. This square has `D=sqrt(2)<9`; it is a finite sharpness check, not a counterexample to the canonical `D>=9` theorem.
- The degree sum counts incidences, not distinct recipients. A loaded-loaded contact contributes two, and multiple contacts may meet the same unloaded vertex. No distinct face, train, harmonic component, or packet payment follows.
- The topology used is that of the full actual diameter graph. A selected stressed subgraph need not have the same leaf count or component count.
- No verifier in the source report encodes this incidence theorem. The proof above is analytic; the square check is an exact finite count. No computational sample is offered as evidence for the universal inequality.

## Dependencies and disposition

| Claim | Verdict | Canonical dependencies |
| --- | --- | --- |
| `t_BI+2e_BB >= q+ell_H >= q+2d_H` | PASS — promote `C-DIAMETER-LEAF-CONTACT-INCIDENCE` | `C-ZRF`; `C-WOODALL`; `C-MIXED-CORE-THREE-VERTEX-CONNECTIVITY` |
| Distinct assignment of incidences to faces, trains, or harmonic components | Not claimed; no such theorem follows from this count | — |
| C-II or Level I closure | NOT CLAIMED; both remain open | — |

This exact linear contact-incidence payment may constrain later separator or owner arguments, but it supplies no global contact budget improvement, source-level cut, packet capacity, or strict sub-`D` competitor.
