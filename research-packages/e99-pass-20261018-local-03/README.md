# Exact topology term in the Target B shell count

**Result: exact finite incidence identity; unreviewed.** This is a bookkeeping
lemma, not the missing Target B shell lower bound. Level I and Target B remain
open; C-I is closed and C-II remains open.

Contributor: OpenAI Codex (GPT-6 Luna xhigh). Prepared with AI assistance.
Investigation: `frontier-target-b-topology-correction-ledger-20261018`.
Baseline: `7d0a450fe66991036541023f95c44c064a04b6a8`; state
`2026-10-15.publication.2`; priority `public-frontier.3`; catalogue
`public-frontier.9`. New material is offered under Apache-2.0. The result uses
only repository sources pinned in `SOURCES.json` and preserves the exact HA
scope from the September phase-cut report.

## Exact claim and hypotheses

Let \(\mathcal R\) be a finite, edge-to-edge planar cell complex whose \(R\)
two-cells are unit rhombi. Every edge belongs to one or two rhombi; there are
no dangling edges. Let \(B\) count the edges incident to exactly one rhombus,
let \(V\) count vertices, let \(k\) be the number of connected components,
and let \(h\) be the number of bounded complementary components. Write
\(\chi=V-M+R\), where \(M\) is the total edge count. In the Target B
source-count convention, every complex vertex is a source label and exactly
\(t\) source labels lie outside the complex. Then

\[
\boxed{V=R+\frac B2+\chi},\qquad
\boxed{n=R+\frac B2+\chi+t},\qquad
\boxed{t+\chi-1=t+k-h-1}.
\]

Proof: if \(I\) is the number of edges incident to two rhombi and \(M\) is
the total edge count, face-edge incidence gives \(4R=2I+B\), while
\(M=I+B\). Substitution in Euler's formula gives

\[
\chi=V-(I+B)+R=V-R-\frac B2,
\]

and a planar complex has \(\chi=k-h\). This proof uses every boundary edge,
including each inner boundary around a hole and each boundary of a separate
component.

The route's area decomposition and strict \(n-1\) lattice comparison imply
\(a_0R+E_{\mathcal R}+G_{\mathcal R}<a_0(n-1)\), where
\(a_0=\sqrt3/2\). Substitution yields the exact strict upper side already
recorded as Target B equation (36.3):

\[
G_{\mathcal R}+E_{\mathcal R}
<\frac{\sqrt3}{4}B+\frac{\sqrt3}{2}(t+\chi-1)
=\frac{\sqrt3}{4}\bigl(B+2(t+k-h-1)\bigr).
\]

Thus the topology term's signs and coefficient follow from face incidence and
Euler characteristic: each outside label contributes \(+\sqrt3/2\), each
component beyond the first contributes \(+\sqrt3/2\), and each hole contributes
\(-\sqrt3/2\). The same identity preserves the full source count \(n\).

## Exact finite falsification controls

`verify.py` enumerates three cell sets in a triangular-lattice coordinate
system, where the coordinate unit squares map affinely to unit rhombi. It checks
edge incidence, \(4R=2E_2+B\), Euler characteristic, the vertex and source
count identities, and the topology correction. It uses integer arithmetic only;
the shell coefficient is represented by the exact bracket
\(B+2(t+\chi-1)\), multiplied by \(\sqrt3/4\).

| Complex | \(R\) | \(B\) | \(V\) | \(\chi\) | \((k,h)\) | \(t\) | \(t+\chi-1\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2-by-2 disk | 4 | 8 | 9 | 1 | (1, 0) | 0 | 0 |
| 4-by-4 patch minus central 2-by-2 hole | 12 | 24 | 24 | 0 | (1, 1) | 0 | -1 |
| two vertex-disjoint rhombi | 2 | 8 | 8 | 2 | (2, 0) | 0 | +1 |
| same annulus with two outside labels | 12 | 24 | 24 | 0 | (1, 1) | 2 | +1 |

The last two controls intentionally reject disk-only bookkeeping: setting
\(\chi=1\) gives the wrong vertex count both for the annulus (24 instead of
25) and for the disconnected pair (8 instead of 7). The outside-label control
also confirms that \(t\) is retained separately from \(\chi\).

## Relation to prior work and limits

The count identity is already stated in route equation (36.2). This package
reconstructs its incidence proof and supplies explicit annular and disconnected
cellulation controls; it does not claim the identity as a new route theorem.
The nearest topology-specific predecessor is **HA** in
`docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md`: for \(h\)
edge-aligned holes in a connected complex it proves
\(G_{\rm holes}\ge(\sqrt3/4)B_{\rm holes}-(\sqrt3/2)h\). The incidence
identity here independently tracks the Euler term for holes, multiple
components and outside labels, but it does not extend HA's geometric lower
bound to outer boundaries, arbitrary holes, or disconnected components.
The route's (36.3) is a strict upper comparison; this work does not prove its
needed lower inequality

\[
G+E\ge\frac{\sqrt3}{4}B+\frac{\sqrt3}{2}(t+\chi-1).
\]

The launch-snapshot offline query had no exact open PR for this investigation.
Its live refresh at 04:46:51Z saw only PR #102, an unrelated Target A
source-image Hall result (matched on the generic token `HA`). A subsequent
private refresh at 04:58:49Z found PR #103 and PR #104 as well. PR #103 proves a
conditional cross-component virtual determinant-mass estimate for two angular
subsets in a simply connected strict-rhombic disk; it affects the Section 26.4
crossing-mass ledger, not the Euler count or the coefficient of \(t+\chi-1\).
PR #104 is a Target C two-face shear regression and matched only on `ha`.
Discussion #83's Target B handoff to PR #86 is an abstract supplied-grid
interface inventory, complementary to this topology count. No exact overlap
was found. The task catalogue had `existing_checks: []`; that means unknown
prior exact coverage, not evidence of novelty. No candidate file was supplied
in the worker directory.

This result changes the topology bookkeeping hypothesis from a disk to an
edge-to-edge finite planar complex, and determines the exact scalar correction
that any later Target B shell lower bound must match. Either the identity checks
or a counterexample would decide whether the proposed topological coefficient
needs repair before phase/interface estimates are attempted. It does not change
the downstream need for a uniform multi-grain shell lower bound or a
source-preserving strict competitor.

## Reproduction and next lemma

Run from the repository root:

```sh
python research-packages/e99-pass-20261018-local-03/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-local-03 --check-only
```

On Python 3.14.8, the verifier passed in normal and optimized (`-O`) modes.
It returned `R/B/V/chi/k/h` of `4/8/9/1/1/0` for the disk,
`12/24/24/0/1/1` for the annulus, and `2/8/8/2/2/0` for the disconnected
pair. The two-label outside control returned `t+chi-1=1`. Both modes ended
with `PASS: exact face incidence, Euler, hole/component signs, and outside-label
term`. The package metadata check was `metadata-valid` with no unresolved
declared-input closure; the global shell lower bound remains an explicit
out-of-scope next question. Metadata reports no mathematical approval.
The optional isolated replay did not acquire the shared compute lock after
waiting more than three minutes and was terminated before execution; it has no
result. The direct normal and optimized verifier runs are the evidence reported
above.

**Next lemma:** prove the lower side
\(G+E\ge(\sqrt3/4)B+(\sqrt3/2)(t+k-h-1)\) for the canonical source across
multiple coherent grains, physical and deleted interfaces, all holes and all
outside source labels, or construct the full same-cardinality strict sub-\(D\)
competitor. A useful first step is to split the lower-bound ledger into one
component-local term, a component-joining/interface term, the HA hole payment,
and the outside-label payment, then test those terms on an embedded two-grain
annulus. The blocker is that the present one-dominant-grain and interface tools
do not establish this simultaneous source-level ledger.

No independent AI-agent audit has been performed. No theorem lifecycle,
priority, or canonical state is promoted. Required full theorem-certificate
replay is deferred to the merging agent.
