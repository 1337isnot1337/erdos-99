<!-- theorem-state: {"artifact_id":"ART-2CCAD338F9E1","canonical":true,"claim_ids":["C-EXACT-OBLIQUE-WALL-POPULATION","C-TRIANGULAR-TWO-INTERIOR-HOLE-STRICTIFICATION","C-UNIT-WALL-PACKET-POPULATION-BOUND"],"claim_statuses":{"C-EXACT-OBLIQUE-WALL-POPULATION":"canonical","C-TRIANGULAR-TWO-INTERIOR-HOLE-STRICTIFICATION":"canonical","C-UNIT-WALL-PACKET-POPULATION-BOUND":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: funded unit-wall activation

**Date:** 2026-10-09
**Audit base:** `origin/main=60d544f14e1fe82b80c1d05e92f251407c4b1238`, state `2026-10-09.audit.190`
**Frozen source:** `origin/research/sol/target-c-level1-gpt61-2026-10-04=9875cd6a77939bb6347353fc798ab8f9ab03ec3e`
**Verdict:** **PASS — promote three exact claims; one source consequence is superseded; one remains conditional.**
**Target effect:** C-II and Level I remain open; no complete wall is extracted from an arbitrary canonical source.

## Frozen artifacts and finite verification

The audited source is [`target_c_vacancy_funded_unit_wall_activation_2026-10-05.md`](../reports/target_c_vacancy_funded_unit_wall_activation_2026-10-05.md), SHA-256 `372a10ce01e1aa8c5a70b39c215b070164eaf851383739d0d0129acd0b1d753b`, at the frozen source commit above. Its verifier is [`verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05.py`](../../research/verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05.py), SHA-256 `53660a5a8d61c512065d1b188a3e6259a03cc4cf59f3510090c2c3d10b282746`. The script imports the frozen one-vacancy strictification helper (SHA-256 `a7dde4b19c70f31266d3e17c781d2523238e25d4e1abc04b251d8d5c7ec1249a`) and exact arithmetic helpers (SHA-256 `7ea533bea43281167b84a78fa53b6a291d1570eb`).

I inspected and reran the verifier at that immutable snapshot. It passes 7,016 exact sequential-move pair checks, 282 final strict interior-pair checks, and 15,244 complete old/new source-pair checks in six guarded replacements; the fixtures remove 83 contacts. Arithmetic is rational or in \(\mathbb Q(\sqrt3)\). It also checks one finite pinned-stress fixture and the crossing equality/noncrossing guard examples. These checks validate only the encoded finite instances. They do not prove the general release order, the wall-capacity implication, or global optimality.

## W.1 — already covered by canonical crossing separation

The claimed unit-edge crossing shield is not a new theorem. At threshold \(t=1\), canonical `C-UNIT-SIDE-CROSSING-SEPARATION` gives the same \(\sqrt3\) lower bound. I rely on that canonical statement below, rather than registering a duplicate.

## W.2 — strict wall packets bound the source interior population

**Promote `C-UNIT-WALL-PACKET-POPULATION-BOUND`.** Let \(A\) be a triangle-free global minimum-diameter source selected with the fewest unit contacts in that class. Let \(W\subset A\) be a simple polygonal cycle whose edges are actual unit contacts. Write

\[
Z=A\cap\operatorname{int}(W),\qquad z=|Z|.
\]

Suppose \(Y\subset\operatorname{int}(W)\) has \(M\) points, with every pair of distinct points of \(Y\) farther than one and every point of \(Y\) farther than one from every vertex of \(W\). Then

\[
\boxed{z\ge M.}
\]

If \(z=M\), every point of \(Z\) is contact-isolated. This count includes all interior source points, including isolates. The conclusion is for the selected global source and does not claim that a suitable packet exists.

**Proof reconstruction.** The canonical `C-EMBEDDED-WALL-REFILL` wall shield applies to any interior packet point that is strictly farther than one from every wall vertex: it is strictly unit-clear from every retained source point outside the wall, including isolates. Also, \(\operatorname{int}(W)\subset\operatorname{int}(\operatorname{conv}A)\); every pair involving a packet point is therefore strictly shorter than the source diameter \(D\).

There are no extra source points on the open wall edges: any such point would be less than one from an edge endpoint. Thus all retained old source points are either wall vertices or lie outside the wall interior.

If \(z<M\), choose a wall vertex \(w\), delete \(Z\cup\{w\}\), and insert \(z+1\) packet points. This preserves cardinality. Packet points have no new unit contacts with each other, retained wall vertices, or retained exterior points. Deleting \(w\) removes its two distinct cycle contacts; the cycle cannot be a triangle because \(A\) is triangle-free. The new diameter is at most \(D\). A smaller diameter contradicts global minimality; equality contradicts contact-minimality. Hence \(z\ge M\).

If \(z=M\) and a point of \(Z\) has a contact, replace \(Z\) by the \(M\) strict packet points and keep the wall. The same full-source shield gives a feasible triangle-free source of diameter at most \(D\) with fewer contacts, again impossible. Thus equality forces every point of \(Z\) to be isolated.

The deleted wall vertex in the first comparison is only a geometric reference: the shield is applied to its original unit edges, whose endpoints were source points before deletion. It is not retained in the competitor or assigned a diameter load.

This is a new integer population consequence beyond the canonical contact-loss corollary of `C-EMBEDDED-WALL-REFILL`. It uses that theorem's source shield and strict-diameter logic, and it adds the one-wall-vertex deletion case when the packet has one more site than the old interior population.

## W.3 — exact oblique rectangular walls force the full grid count

**Promote `C-EXACT-OBLIQUE-WALL-POPULATION`.** Let \(m,n\ge2\), \(\pi/3<\phi<2\pi/3\), \(u=(1,0)\), \(v=(\cos\phi,\sin\phi)\), and let \(W\) be the complete boundary grid of \(\{iu+jv:0\le i\le m,\ 0\le j\le n\}\). If this exact simple unit-contact wall is contained in a canonical triangle-free contact-minimal global minimum-diameter source, then

\[
\boxed{|A\cap\operatorname{int}(W)|\ge(m-1)(n-1).}
\]

Every interior source point, including a contact isolate, is counted. This exact-wall theorem covers thin frames and obtuse angles beyond the acute, near-wall `C-ONE-PIN-OBLIQUE-WALL-POPULATION` scope; on the overlap it is consistent with that stronger perturbative wall theorem. It does not extract such a wall from an arbitrary source.

**Proof reconstruction.** The canonical one-vacancy strictification `C-OBLIQUE-ONE-VACANCY-STRICTIFICATION` supplies a strict packet of \(M=(m-1)(n-1)-1\) interior sites: omit any one interior label and move all other interior labels, keeping the complete wall fixed. Apply `C-UNIT-WALL-PACKET-POPULATION-BOUND`; it gives \(z\ge M\), and equality would make all enclosed source points contact-isolated.

Equality is impossible. The bottom wall vertex \(p=u\) lies between the wall vertices \(0\) and \(2u\), so it is not an extreme point of \(\operatorname{conv}A\) and cannot be an endpoint of a diameter pair. If every contact neighbor \(q\) of \(p\) had \(q_y\le0\), moving \(p\) a sufficiently small distance upward would strictly open every contact: for a unit contact, the squared distance changes from one to \(1-2\varepsilon q_y+\varepsilon^2>1\). All noncontacts have finite positive lower slack, and all pairs involving \(p\) have strict upper slack below \(D\). A sufficiently small move preserves both lower and upper constraints, keeps the old diameter pair away from \(p\), and lowers the contact count. Global minimality/contact-minimality forbids this. Hence \(p\) has a unit-contact neighbor with positive height.

For \(|k|,|l|\ge1\), put \(a=|k|,b=|l|\). Since \(|2\cos\phi|<1\),
\[
|ku+lv|^2\ge a^2+b^2-ab\ge1,
\]
with equality in the second inequality only at \(a=b=1\); there the first inequality is strict. Hence all such lattice differences have length strictly greater than one, and the only unit lattice differences are \(\pm u,\pm v\). Thus no positive-height unit neighbor of \(p\) is another wall vertex: \(p+v\) is strictly interior and the other wall neighbors lie on the bottom side. If such a contact neighbor were exterior to the parallelogram, the segment from \(p\) to it enters through the bottom interior and exits through a nonincident unit wall edge. All four distances to that edge's endpoints are at least one, so canonical `C-UNIT-SIDE-CROSSING-SEPARATION` gives source-pair distance at least \(\sqrt3\), contradicting that it is a contact. Therefore an interior source point is contact-incident, contradicting the isolate-only equality case. Consequently \(z\ge M+1=(m-1)(n-1)\).

This also handles \(m=n=2\): the one-vacancy packet is empty, while the same local contact argument forces at least one interior source point.

## W.5 — a distinct two-interior-vacancy triangular strictification

**Promote `C-TRIANGULAR-TWO-INTERIOR-HOLE-STRICTIFICATION`.** For \(m,n\ge3\), take the triangular lattice parallelogram \(p_{ij}=i(1,0)+j(1/2,\sqrt3/2)\), omit the two interior labels \((1,1),(2,1)\), keep every boundary label fixed, and move every other interior label. There is a finite sequence of continuous straight moves that preserves all pairwise distances at least one throughout, keeps every mover strictly inside the parallelogram, and ends with every pair involving a moved point strictly farther than one. The amplitudes can be chosen so each point moves less than \(1/100\); no uniform lower bound on the amplitudes as \(m,n\) grow is asserted.

The six contact directions are \(\pm u,\pm v,\pm(u-v)\). If two adjacent contact directions are absent because their neighbor labels are holes or have already been released, move the current point along the sum \(h\) of those two directions. Then \(|h|^2=3\), and \(h\cdot r\le0\) for each remaining contact direction \(r\). Along the move, the squared distance to that neighbor is

\[
|th-r|^2=1-2t(h\cdot r)+3t^2>1\quad(t>0).
\]

Release in this order: for \(j=2,\ldots,n-1\), release \((1,j)\) using the missing/released \((1,j-1),(2,j-1)\), then \((2,j)\) using \((1,j),(2,j-1)\). For \(i=3,\ldots,m-1\), release \((i,1)\) using \((i-1,1),(i-1,2)\), then release \((i,j)\), \(j=2,\ldots,n-1\), using \((i-1,j),(i,j-1)\). At each step the two directions are adjacent and their labels have already been released or omitted. This order covers each non-hole interior label exactly once. All noncontact pairs have finite positive slack at that step, so choose a sufficiently small positive amplitude to preserve them throughout the segment and keep the mover inside. Finitely many choices give the claimed endpoint; further cap each amplitude by \(1/(100\sqrt3)\) for the displacement bound.

This is a fixed-container finite-motion theorem, not a triangle-free-source theorem: the triangular reference wall itself may contain unit triangles. The stronger near-wall population conclusion from Audit.192 (`C-TRIANGULAR-TWO-BOUNDARY-HOLE-POPULATION`, with \(z\ge(m-1)(n-1)-1\)) supersedes W.6's weaker \(z\ge(m-1)(n-1)-2\) source consequence. No near-wall theorem or vacancy creation is claimed here.

## Remaining dispositions and frontier

- W.4 remains **conditional only** on the source report's unpromoted fixed-wall uniqueness window L.2. The equality-population theorem does not establish uniqueness of the interior grid or an Oler equality classification.
- W.6 is **superseded** on the shared fixed-frame near-wall scope by Audit.192's stronger \(z\ge(m-1)(n-1)-1\) result. Its frame tolerance may differ; the two positive tolerances can be intersected for each fixed frame.
- The finite one-interior-vacancy pinned-stress fixture is reproduced but is not a new canonical regression. It is only a finite local obstruction and is not used in any promoted proof.
- The crossing lemma is subsumed; no duplicate theorem ID is added.

The reusable source consequence is now: **a strict wall packet cannot outnumber the old interior population of a canonical contact-minimal source, and equality leaves only isolates.** For an exact oblique rectangle in the stated angle range, the one-vacancy packet plus contact-minimal activation raises this to the full \((m-1)(n-1)\) population. The outstanding C-II obligation remains to force a qualifying complete wall and its finite capacity deficit in every surviving source branch. No worker branch or source artifact was edited.
