<!-- theorem-state: {"artifact_id":"ART-19037C1FE64C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c76ebec794fcd04e2b2d439b500122f23cf2a520", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/source_scaffold_response_transport_2026-08-30.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0c4a0a6ca63319b7b7fecbfd2cc0223c915dcc82d30641f8696f7fa410dbd269"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — source/scaffold/response transport synthesis

**Date:** 2026-08-30
**Run type:** closing-proof continuation and audit
**Target:** A
**Base main:** `0ecb0927d82b7a53c3c8133b821b5261c81b75f7`
**External literature search:** yes; no theorem imported
**Computation:** none used as a theorem input; exact arithmetic was checked independently

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

The exact surviving Target A statement is
\[
\dim\ker S\ge s,
\qquad s=\Delta_\Lambda-d_{\rm int},
\tag{R.1}
\]
equivalently
\[
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
\tag{R.2}
\]
A second exact closure is an `N`-point unit-separated set of diameter strictly below
`D=D(N)`.

The run started from the Section-155 common-placement gap: the genuine source `A` and
the smaller optimum/scaffold could be placed in one hull, but the canonical record did
not identify source geometry with the plateau-terminalized Schur terminals.

## 2. Promoted theorem chain

### Section 163 — planar two-shadow transport

A strict-conflict matching between two unit-separated planar sets has pairwise disjoint
straight matching segments. If two matched segments met at `z`, then
\[
2\le |u_1-u_2|+|v_1-v_2|
\le |u_1-v_1|+|u_2-v_2|<2.
\]

Applied to the two Section-155 source shadows, this gives an exact crossing rule: a
crossing between an `X_m->A` shadow edge and a lattice-to-`A` shadow edge with distinct
source endpoints forces the opposite `X_m` and lattice endpoints to be at distance
`<1`. For the actual scaffold phase, every such crossing is therefore an actual
scaffold conflict.

The two near-perfect source matchings also have a common source image of size at least
\[
m-\widehat p_H-(M-|Y|).
\]
This gives vertex-disjoint source-mediated V-paths. A width-one parallel-body packing
argument purifies all but an explicit boundary-order exceptional set into paths ending
at actual `Y_in` sites.

### Section 164 — triangular-lattice common-neighbor lift

For the unit triangular lattice, if `x` is generic and `|x-a|<1`, then there is a
lattice site `y` with
\[
|x-y|<1,
\qquad |a-y|<1.
\tag{R.3}
\]
The proof is a two-cell classification. The strict lattice neighborhood of `x` is the
vertex set of either an elementary triangle or a unit lozenge containing `x`. The
union of the unit disks centered at those vertices contains the entire open unit disk
about `x`; the exposed arcs are at distance at least one because the next lattice
vertices are not strict neighbors of `x`.

Applying (R.3) to a source matching `X_m->A` of size at least
`m-widehat p_H` and using the lattice-side degree-five bound gives at least
\[
\frac{m-\widehat p_H}{5}
\tag{R.4}
\]
vertex-disjoint triples `(x,a,y)` with all three pairwise distances `<1`.

### Section 165 — plateau-wide alignment and actual Schur-terminal labeling

The pre-terminalized `X_m` shore is not the response shore. Section 99 replaces it by
an `m^*`-point optimum `X^*` at the right endpoint of the same diameter plateau,
\[
m^*=\max\{q\ge m:D(q)=d\}.
\]
This scope difference was audited explicitly rather than ignored.

The new plateau-wide Bonnesen theorem fixes it. For every `q` with `D(q)=d` and every
q-point optimum `X_q`, the degenerate hull case is immediate from the Section-155
source inner disk. In the full-dimensional case, Oler plus the canonical strict
translated-lattice inequality `q-1>d^2/c` give
\[
P_q^2-4\pi A_q<\pi^2\sqrt3\,d.
\]
Hence `R_q-r_q<3^{1/4}sqrt(d)`. Under the existing Section-155 threshold
`t>=(1+3 eta(D))`, circumcenter alignment yields
\[
\boxed{K_q+\mathbb B\subset H.}
\tag{R.5}
\]
Thus (R.5) applies in particular to the actual plateau endpoint `X^*`.

The fixed-source Hall theorem therefore gives a matching
\[
X^*\longrightarrow A
\quad\text{of size at least}\quad
m^*-\widehat p_H.
\tag{R.6}
\]
Combining (R.6) with Section 164 on the actual response lattice proves:

- all but at most `widehat p_H` vertices of `X^*` have distinct genuine-source labels
  and a common response-lattice conflict;
- consequently all but at most `widehat p_H` actual Schur terminals in `C^partial`
  have such distinct source labels;
- at least
  \[
  \frac{\max\{0,|C^\partial|-\widehat p_H\}}5
  \]
  Schur terminals can be selected with both distinct source labels and distinct
  response-lattice neighbors.

This is the first theorem in the route that attaches genuine-source labels directly to
the actual Schur source terminals, rather than to a pre-terminalized or independently
chosen scaffold.

The plateau endpoint also amplifies the source-backbone count. With
`ell=m^*-m` and `tau=tau_D(A)`, at least
\[
\max\{0,\tau-\widehat p_H+\ell\}
\]
source-matching edges from `X^*` end in genuine strict rattlers, and at least one fifth
as many give vertex-disjoint rattler-certified response conflicts.

### Section 167 — source-label crossings in the actual response graph

Overlay the noncrossing source matching `X^*->A` with the planar radial response graph.
If a source segment `x-a` properly crosses a response edge `u-y`, then
\[
\boxed{|a-y|<1.}
\tag{R.7}
\]
Otherwise `{x,u}` and `{a,y}` would be two unit-separated shores joined by two
intersecting strict matching segments, contradicting Section 163.

For a phase generic for both `X^*` and `A`, a source point has at most four strict
lattice neighbors and a response lattice vertex has degree at most five. Hence:

- one source segment has at most 20 proper crossings with response edges;
- it can properly cross at most four paths of any vertex-disjoint Menger family that
  do not contain its left endpoint;
- one response edge has proper crossings with at most five source segments.

Every proper crossing of a source-label segment with a Schur/Menger path therefore
creates a specific additional source-to-right conflict with constant congestion.

## 3. Exact regression discovered during audit

Section 166 records a two-pair rational counterexample to the tempting strengthening
that every source-matched left vertex can be assigned a *distinct* common lattice
neighbor.

With the unit triangular lattice generated by `e1=(1,0)` and
`e2=(1/2,sqrt(3)/2)`, take
\[
x_1=(-3/10,-1/10),\qquad a_1=(1/2,-13/20),
\]
\[
x_2=(3/5,7/20),\qquad a_2=(-1/4,3/20).
\]
Then each shore is unit-separated and both paired distances are `<1`, but
\[
N_\Lambda(x_1)\cap N_\Lambda(a_1)
=N_\Lambda(x_2)\cap N_\Lambda(a_2)=\{0\}.
\]
Thus even two noncrossing source-matching edges can be forced to use the same unique
common lattice site. The local factor-five extraction cannot be replaced by a perfect
SDR theorem without additional global hypotheses.

## 4. Audit checks

The final common-neighbor proof is analytic. The exact rational regression arithmetic
was checked independently, and an incorrect nonessential distance display was caught
and corrected before promotion. An unneeded equality-case sharpness sentence was also
removed from Section 164.

The following binding regressions were checked explicitly:

- coherent strained-monomer bounded-displacement matchings can be Hall-neutral;
- Sections 152–153 and 156–159 forbid activation-rank, positive-KKT-load, or local
  critical-cone shortcuts;
- planar response networks may have full linkage rank;
- `tau_D(A)` need not be super-boundary;
- the exact fixed-source Hall ceiling `widehat p_H` cannot be exceeded inside `H` by
  capacity bookkeeping alone;
- Sections 161–162 forbid another claimed support-exponent improvement from local rigid
  translations of the same five Kuperberg blocks.

No theorem in Sections 163–167 conflicts with these examples because the new content is
an exact *transport of source labels into the actual response geometry*, not a claim
that local incidence or planarity alone forces nullity.

## 5. Literature search

A targeted search revisited finite-packing and hexagonal-stability literature,
including Oler's slackness work, Graham--Witsenhausen--Zassenhaus on tightest packings,
and Bárány--Dolbilin on stability of the densest circle packing. The exact equality
characterization of tight finite packings is relevant background, but no located theorem
supplies the needed quantitative finite-container statement at the present vanishing
slack and boundary scale. No external result was imported into the proof chain.

## 6. Exact new endpoint

The old Section-155 wording said that the source and response objects still lacked a
usable common identification. That is no longer accurate in the very-super-boundary
subbranch.

The exact remaining lemma can now be stated on the actual Schur graph:

> **Source-labeled planar Menger lemma.** Let `C^partial_src` be the Schur terminals
> carrying the distinct genuine-source labels from Section 165. Use those labels, the
> noncrossing source matching, the crossing-generated source conflicts of Section 167,
> and global minimum-diameter data to prove that every directed
> `C^partial-to-O` linkage omits at least
> \[
> s=\Delta_\Lambda-d_{\rm int}
> \]
> terminals, or else construct an `N`-point unit-separated configuration of diameter
> `<D`.

Equivalently, prove
\[
\operatorname{rank}S\le |C^\partial|-s.
\]

A proof using only the number of local triples is invalid by Section 166 and the older
strained-monomer regression. The next theorem must use the source labels globally,
not merely count them.

## 7. Promotion recommendation

Promote Sections 163–167, with Section 166 explicitly classified as a regression.
Advance the active prompt so future runs start from the actual source-labeled Schur
terminals and the bounded-congestion crossing rule.

The theorem state remains Level I open.
