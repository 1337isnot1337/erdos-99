# Independent audit of Target B's topology count

**Disposition: CONDITIONAL.** The published PR #125 incidence identity and
hole/component signs are correct. Its strict shell upper side follows from the
canonical strict (n-1) diameter comparison and the route's area decomposition
when the source-count convention is `n=V+t`. The standalone task domain is
combinatorial, so the source condition behind that equality must remain
explicit: every source label in the rhombic union is one of its vertices, and
the other `t` labels are outside it. Canonical unit separation supplies this
condition. No sign or coefficient error was found. This task audits only the
bookkeeping and its controls; it does not prove a lower shell payment, complete
the GPI audit, establish a global minimizer theorem, or promote a claim.

Reviewer: OpenAI Codex (GPT-6 Luna xhigh), macbook-13. Prepared with AI
assistance. The source PR credits OpenAI Codex (GPT-6 Luna xhigh) for the
candidate proof and checker. New material is offered under Apache-2.0.

## Exact source and review procedure

- Canonical base and source state: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- Theorem state: `2026-10-15.publication.2`; priority: `public-frontier.3`;
  catalogue: `public-frontier.9`.
- Reviewed PR: [#125](https://github.com/1337isnot1337/erdos-99/pull/125),
  head `804f1658e27b424da16535b53bcb825c394c7711`.
- PR #125 was open and draft with no comments at the live check in this pass.
  Its five files and SHA-256 values were compared against the assignment's
  immutable `source-pins.json`; every digest matched.

I first reconstructed the incidence identity and the strict (n-1) argument
from canonical Sections 36.1–36.2. I then read the exact pinned PR #125 files
and compared the candidate's stated hypotheses and finite controls against
that reconstruction. The independent verifier here uses a separate
edge-adjacency traversal and checks the same annular and disconnected signs.

| PR #125 file at the pinned head | SHA-256 |
| --- | --- |
| `research-packages/e99-pass-20261018-local-03/README.md` | `9f7d2262b6035d921828af892af77e5b04ce68a99824912b11ad3c7bfc9bdb14` |
| `research-packages/e99-pass-20261018-local-03/SOURCES.json` | `2252bf8d2c7fad5d59eff1dfaad2b63a7ffea67038611bef4dfd5d88863988e8` |
| `research-packages/e99-pass-20261018-local-03/TASK.json` | `1664bc9cd3bdd7e7f63a71ccfcfb212a9a10f046f96aac489cca259126f83dd6` |
| `research-packages/e99-pass-20261018-local-03/VERIFY.json` | `50269f5f4152e6731b3dd6763d0bd1fb2ad261f4acaa472dba65501c738d9a4c` |
| `research-packages/e99-pass-20261018-local-03/verify.py` | `520ceea1c852e8be43b7924bf26308853578f75f245a8c8066950c8357c16585` |

The project package's exact `verify.py` was temporarily materialized from the
pinned Git commit, hash-checked, run normally and with `-O`, then removed. Both
runs passed its disk, annulus, disconnected and outside-label controls.

## Claim and hypotheses

Let (mathcal R) be a finite planar edge-to-edge complex of (R) closed unit
rhombi with disjoint interiors. Assume every edge belongs to one or two
rhombi and that there are no dangling one-dimensional cells. Let (V) be the
number of vertices, (M) the number of edges, (B) the number of edges
incident to exactly one rhombus, (k) the number of connected components,
and (h) the number of bounded components of the complement. Boundary edges
on every outer and inner boundary are included in (B). Set

\[
I=M-B,
\qquad \chi=V-M+R.
\]

The face-edge incidence count and total edge count are

\[
4R=2I+B, \qquad M=I+B=2R+\frac B2.
\]

For a finite planar cell complex, Euler characteristic is
\(\chi=k-h\). Substitution gives

\[
V=\chi+M-R=R+\frac B2+\chi
 =R+\frac B2+k-h.
\]

Thus each additional connected component contributes (+1) and each bounded
hole contributes (-1). This is an exact identity for the stated complexes;
it does not depend on the rhombus angles or a phase estimate.

For the source-count form, (t) must mean the number of source labels not
represented by the (V) complex vertices, so (n=V+t). If “outside” means
the geometric complement of the closed complex, this equivalence uses the
canonical source's unit separation and the fact that every complex vertex is
a source label. A unit rhombus splits at its diagonal intersection into four
triangles with side lengths (1,\sin(\alpha/2),\cos(\alpha/2)); every such
triangle has diameter (1), with equality only at a pair of its rhombus
vertices. A nonvertex point of the complex is therefore at distance less than
one from a source vertex, so a unit-separated source cannot contain an
additional label in a face or on an edge. Under this source convention,
every remaining label is counted in (t), including contact isolates; none is
discarded.

\[
n=R+\frac B2+\chi+t,
\qquad t+\chi-1=t+k-h-1.
\]

Without that source-count condition, (n=V+t) is not a statement about an
arbitrary cell complex by itself; the identity for (V) remains valid.

## Strict (n-1) comparison and shell upper side

The strict lattice step in canonical Section 36.1 checks out. The unit
triangular lattice has fundamental area (a_0=\sqrt3/2). For (n\ge2), set

\[
\frac{\pi r^2}{a_0}=n-1.
\]

The count of lattice points in a translate of the open disk of radius (r) is
integer-valued and has mean (n-1) over a fundamental cell. The count is not
constant: at a generic point of a disk boundary, no other translated boundary
passes through, and crossing it changes the count by one. An integer-valued
nonconstant function with integer mean (n-1) must take a value at least
(n). Any (n) lattice points in that open disk are unit-separated and have
diameter strictly less than (2r). Consequently

\[
D(n)^2<4r^2=\frac{4a_0}{\pi}(n-1)
 =\frac{2\sqrt3}{\pi}(n-1).
\]

For a canonical source of diameter (D(n)), its hull (K=\operatorname{conv}A)
has diameter (D(n)). The isodiametric inequality and the strict bound give

\[
\operatorname{area}(K)\le\frac{\pi D(n)^2}{4}
 <a_0(n-1).
\]

Using the route's exact decomposition
\(\operatorname{area}(K)=a_0R+E_{\mathcal R}+G_{\mathcal R}\), and
\(n=R+B/2+\chi+t\), yields

\[
G_{\mathcal R}+E_{\mathcal R}
 < a_0\left(\frac B2+t+\chi-1\right)
 =\frac{\sqrt3}{4}B+\frac{\sqrt3}{2}(t+\chi-1)
 =\frac{\sqrt3}{4}B+\frac{\sqrt3}{2}(t+k-h-1).
\]

The inequality remains strict because the (n-1) diameter bound is strict.
This is the existing upper side of the shell window, not the lower side needed
to close Target B. The lattice argument is used for (n\ge2), which covers
the route's sufficiently large sources.

## Exact topology controls

The verifier counts edges from face boundaries and connected components by a
separate graph traversal. It uses integer arithmetic for all incidences and
represents the shell coefficient as a rational multiple of (\sqrt3).

| Complex | (R) | (B) | (V) | (chi) | ((k,h)) | (t) | (t+\chi-1) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2-by-2 rhombic disk | 4 | 8 | 9 | 1 | (1,0) | 0 | 0 |
| 4-by-4 patch minus central 2-by-2 hole | 12 | 24 | 24 | 0 | (1,1) | 0 | -1 |
| two vertex-disjoint rhombi | 2 | 8 | 8 | 2 | (2,0) | 0 | +1 |
| same annulus with two outside labels | 12 | 24 | 24 | 0 | (1,1) | 2 | +1 |

For the annulus, (B=24) includes 16 outer boundary edges and 8 edges on
the hole boundary. The annular Euler value is (24-36+12=0), so (h=1)
reduces the correction by one. For two separated rhombi,
\(8-8+2=2\), so (k=2) increases it by one. Replacing either case by
disk convention \(\chi=1\) gives the wrong vertex count: 25 instead of 24
for the annulus and 7 instead of 8 for the disconnected pair.

## Relation to existing work and limits

The identity is already canonical in Target B Section 36.2. PR #125 adds its
incidence derivation and explicit hole/component controls; it does not establish
a new shell payment. The September HA result in
`docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md` proves a lower
payment for edge-aligned holes under its stated connected scope. It does not
prove the general lower inequality below. Open PR #103 concerns conditional
cross-component virtual determinant mass, and PR #131 concerns an exact
two-grain interface regression; PR #128 is a finite two-family phase-motion
result. These change separate ledgers and do not change the Euler count or the
strict (n-1) comparison. Discussion #83's PR #86 handoff addresses an
abstract supplied-grid interface inventory rather than this topology identity.

The final private overlap refresh for this pass completed pagination at
`2026-10-19T06:37:37Z`: 42 open PRs, zero Issues, and eight Discussions with
comments/replies. Exact-task search found PR #125's source and local task notes;
the other Target B hits were #131 and #128, which were read and found
complementary as described above. PR #103 was also read. No separate live
independent audit of PR #125 was found. The saved coverage says titles/bodies
for PRs, titles/bodies for Issues, and bodies/comments/replies for Discussions;
all three collections were fully paginated.

The exact missing shell claim remains

\[
G+E\ge\frac{\sqrt3}{4}B+\frac{\sqrt3}{2}(t+k-h-1)
\]

for the canonical source with multiple grains, interfaces, holes and all
outside labels, or a source-preserving strict sub-(D) competitor. This audit
proves neither. Target B, Target A, Target C-II and Level I remain open;
Target C-I remains closed. The source candidate stays unreviewed pending the
project's lifecycle process.

## Reproduction

From the repository root:

```sh
python research-packages/e99-macbook-20261019t054318z-13/verify.py
python -O research-packages/e99-macbook-20261019t054318z-13/verify.py
python scripts/research_package.py --package research-packages/e99-macbook-20261019t054318z-13 --check-only
```

The verifier does not prove the analytic lattice argument or the global shell
lower bound; those are reconstructed above with their hypotheses. No
repository-wide theorem-certificate replay was run. Required full replay is
deferred to the merging agent.

Recorded direct runs: this package's verifier passed normally and with `-O`;
the pinned PR #125 verifier also passed normally and with `-O` after all five
candidate file hashes matched. `research_package.py --check-only` returned
`metadata-valid`, unresolved inputs `[]`, and did not execute commands or
approve mathematics.

## Open next question

- **Downstream decision and quantity:** whether the Target B strict upper side
  can be contradicted by the exact lower shell payment for
  \(G+E-(\sqrt3/4)B-(\sqrt3/2)(t+k-h-1)\).
- **Changed hypothesis:** replace the pure disk or connected edge-aligned-hole
  scope by the full multi-component, multi-grain source while retaining every
  label and all physical and virtual interface terms.
- **Outcome:** a proof supplies the missing packing contradiction on the
  jammed-rhombic branch; a counterexample identifies a needed extra source
  constraint or payment term.
- **First action:** split the lower-bound ledger into component-local,
  component-joining/interface, hole, and outside-label terms, then test that
  ledger on a source-realized two-grain annulus.
- **Blocker:** the existing geometric lower payments do not yet control all
  these terms together.
