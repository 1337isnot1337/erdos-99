<!-- theorem-state: {"artifact_id":"ART-1D2B6FF468DE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — small-swap contact blockers require a source face or a transverse train end

**Date:** 2026-10-01  
**Starting local HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`  
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`  
**Checkpoint before this attack:** `5782724a812082e6aae7b4edb8df54f603005fd8`  
**State version:** `2026-09-14.audit.51`  
**Branch/mission:** `swarm/gap-thrackle-20261001`; actual unit-cut compatibility after the geometric common-pivot reduction.  
**Classification:** proved candidate awaiting promotion; conditional application to the unpromoted finite swap and complete-train extraction; exact regression.  
**Level I:** OPEN; C-I CLOSED; C-II OPEN.  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.  
**Literature:** none imported.

```text
source-face localization and exact opposite-train immunity -> lower-constraint
blockers of an actual finite swap need transverse terminal capacity, bounded-face
capacity, or exterior/isolate capacity -> eliminating those capacities would make
the source-preserving swap a strict competitor or contradict H-minimality ->
Level I only after the other C-II branches are also excluded.
```

The capacity elimination is not asserted. An exact seven-point source below
shows why protection of every rhombus cannot replace that obligation.

## 1. Dependencies and explicit source hypotheses

Canonical inputs for the application are contact-minimal, then diameter-pair-minimal
normalization in [Section 56](../targets/target-c/56-ci-restored-frontier.md),
the nonisolated-core convention in [Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md),
and the actual plane unit-contact graph. The elementary geometric statements below
are rederived for arbitrary unit-separated sources.

Unpromoted inputs are the exact actual-train cutsets, the at-most-one crossing
of two complete trains, and the finite displacement in the
[block-transposition report](target_c_open_cell_block_transposition_2026-10-01.md)
and its [local-immunity dependency](target_c_tb1_swap_grid_local_immunity_2026-10-01.md).
No source global-optimality theorem is imported from a shell regression.

For the train application assume the source is unit-triangle-free. Let the two
bounding actual O–O trains be `tau_p,tau_q`, with coherently oriented
unit contact vectors `u_p,u_q`, whose projective angle is less than `pi/3`.
Their middle slab is `M`. Move every point of `M` by

\[
\Delta=u_q-u_p,\qquad s=|\Delta|<\sqrt2-1.
\tag{1}
\]

Initially keep other points fixed. The exact cutsets make every old contact
unchanged: the lower cut vector changes from `u_p` to `u_q`, and the upper cut
vector from `u_q` to `u_p`. If an isolate-dispatch extension is used, the
same arguments apply to source-pair localization, while the rhombus statements
refer to the unchanged binary motion on the nonisolated core.

All source points are retained. No assertion of unit separation at the new
endpoint is made before the blockers are checked.

## 2. Every new lower-constraint blocker is cofacial in the old source

**Lemma 1.** For any unit-separated planar source and `0<=s<sqrt2-1`, all pairs
of length at most `1+s`, together with the actual unit contacts, form a simple
plane straight-line graph. A previously strict pair whose length becomes at
most one under a binary displacement of amplitude `s` has its old segment
inside the closure of one old contact face.

**Proof.** Crossing edges would be the two diagonals of a convex quadrilateral
whose four sides are at least one. Some interior angle is at least `pi/2`;
the opposite diagonal then has length at least `sqrt2`. This contradicts both
diagonals having length at most `1+s<sqrt2`. A third source vertex cannot lie
on such an edge: the two distances to its endpoints would sum to at least two.
Overlapping distinct edges are excluded by the same argument. The graph is
therefore plane.

The reverse triangle inequality gives old length at most `1+s` for a new
contact or overlap. Its open old segment crosses neither an old contact nor
an old vertex, so is in one connected contact-face region. Isolates can lie in
such a region; cofaciality does not declare them contact vertices. QED.

In particular, an inactive blocker between two corners of a bounded strict
unit rhombus is one of its two diagonals. There is no source isolate in the
interior of such a rhombus: splitting along its shorter diagonal gives two
acute or right triangles with circumradius at most `1/sqrt2`; their vertex
disks cover them. Every interior point is within distance strictly less than
one of a corner. Nor can a different source point lie on one of its unit sides.

## 3. Protection extends beyond the retained complete rectangle

**Theorem 2 (opposite-train immunity).** Suppose a strict rhombus `F` is crossed
by one bounding train, say `tau_p`, and by a complete opposite train `sigma`.
If `sigma` also crosses `tau_q` in any actual strict rhombus of the source,
neither diagonal of `F` becomes a unit contact or overlap after (1).
The two rhombi need not belong to the retained complete rectangle or lie near
each other.

**Proof.** Write the coherently oriented direction of `sigma` as `v`. Before
the move the diagonal squares of `F` are

\[
|u_p\pm v|^2=2\pm2u_p\cdot v>1.
\]

Since the two bounding trains have projective separation less than `pi/3`,
they cannot cross each other in a strict unit rhombus. Thus `F` meets only the
lower boundary, and its two moving corners differ from its two fixed corners
by `u_p`. After the move its diagonal squares are exactly

\[
2\pm2u_q\cdot v.
\tag{2}
\]

At the actual crossing of `sigma` with `tau_q`, source unit separation and
triangle-freeness give `2\pm2u_q\cdot v>1`. Thus both new diagonals are
strictly greater than one. For a face at the upper boundary exchange `p,q`.
QED.

This uses physical train directions and actual rhombus crossings, not a
virtual grid embedding. A face wholly inside or outside the slab does not
change. Every remaining quadrilateral face meets exactly one boundary in two
opposite contact edges, so the argument lists all rhombus possibilities.

## 4. Each unprotected rhombus consumes a terminal occurrence inside the slab

**Theorem 3 (terminal injection).** Suppose an originally strict rhombus
diagonal becomes at most one. Its opposite complete train `sigma` crosses
exactly one bounding train and has exactly one terminal occurrence inside
`M`. Distinct bad rhombi inject into these terminal occurrences.
The direction of `sigma` lies in one of the two projective angular intervals
between the corresponding boundary directions `theta_p+/-pi/3` and
`theta_q+/-pi/3`, modulo `pi`.

**Proof.** Theorem 2 excludes a second boundary crossing. Two complete
trains cross at most once, so `sigma` crosses the first bounding cut once
and the second zero times. Its midpoint path therefore enters the middle
component once and cannot leave it: leaving would require another crossing
of the first cut or a crossing of the second. One of its two ends is in
`M`, the other outside. The physical terminal face occurrence is in the
same component. Bounded defect faces are not traversed by an O–O cut;
outer terminal occurrences are assigned with their physical face side.

A train contributes at most one rhombus at each boundary. It cannot contribute
a bad rhombus at both by Theorem 2. Moreover at most one diagonal of a unit
parallelogram can be at most one, since its two diagonal squares sum to four.
The resulting assignment of a bad rhombus to its unique middle terminal
occurrence is injective.

For the angular statement, the old crossing imposes `|u_p dot v|<1/2`,
whereas (2) imposes `|u_q dot v|>=1/2`. Vary the boundary direction on its
short angular interval: the crossing from the open allowed region to its
complement occurs at one of the two projective boundary directions offset
by `+/-pi/3`. This gives exactly the asserted two intervals. Each has
angular length

\[
|\theta_q-\theta_p|=2\arcsin(s/2).
\tag{3}
\]

Endpoint equality in (2) creates a unit equilateral triangle at the new
endpoint; it does not imply one existed in the source. QED.

Thus the genuinely unprotected quadrilateral witnesses are not arbitrary
grid diagonals. They require a transverse train that stops before reaching
the other bounding train. In particular every opposite train of the retained
complete rectangle is protected globally.

For `k` swaps with disjoint moving core slabs, all the assigned terminal
occurrences are distinct. A complete train has only two terminal occurrences,
so `k` rhombus-blocked swaps need at least `ceil(k/2)` distinct transverse
trains outside the protected full-span family. This is an exact capacity
statement; it is not a contradiction to the available linear train population.

## 5. Bounded nonquadrilateral witnesses have a separate exact budget

Assume the nonisolated contact core is connected. For each bounded
nonquadrilateral face let `d_F>=5` be its occurrence-counted boundary degree,
and let `z_F` be the number of source isolates in its open region. Let
`l_F` be the number of previously strict pairs of length at most `1+s`
whose old open segments lie in that face. Then

\[
\boxed{l_F\le d_F-3+3z_F.}
\tag{4}
\]

To prove this, insert all these edges in the face. Lemma 1 makes them
noncrossing. Adding `l_F` edges can reduce the number of connected components
by at most `z_F`, since the old core is connected. Euler therefore gives at
least `l_F-z_F` extra bounded regions. The original bounded region is
replaced by at least `l_F-z_F+1` regions, all with boundary degree at least
three. The sum of their degrees is `d_F+2l_F`, including bridge and
articulation occurrences. Hence

\[
d_F+2l_F\ge3(l_F-z_F+1),
\]

which is (4). If `l_F<z_F`, (4) already follows from `d_F>=5`; the same
inequality still applies. A component disjoint from the old boundary must
contain a source isolate, so no hidden component loss was omitted.

Writing the **global** exceptional-face currency

\[
Q=\sum_F(d_F-4),\qquad f=\#\{F\},\qquad z_{\rm bd}=\sum_Fz_F,
\]

gives

\[
\boxed{\sum_Fl_F\le Q+f+3z_{\rm bd}\le2Q+3z_{\rm bd}.}
\tag{5}
\]

This does not count witnesses in the unbounded face. It also does not replace
global `Q` by the sum `Q_D` of harmonic-cell defects from the rooted-threshold
report; an additional comparison theorem would be required. In particular,
the near-root statement `Q_D=o(D)` alone supplies no deletion of (5).

A pair changes under at most two of a family of disjoint binary moving sets.
For isolate-dispatched swaps the same conclusion holds when one fixed root
assignment is used for all swaps. Thus bounded nonquadrilateral blockers can
explain at most `2(Q+f+3z_bd)` such failed attempts. All outer-face blockers
and all the term `3z_bd` remain explicit.

## 6. Rejected strengthening: every actual rhombus is immune

The following exact seven-point source has actual unit-contact cutsets and two
strict near-triangular rhombi, yet a boundary rhombus diagonal becomes less
than one under the finite contact-preserving transposition.

Let `t` be rational with `0<t<=1/100`, put `eta=2 atan(t)`, and define

\[
u=(1,0),\qquad w=R_{2\eta}u,\qquad
v=R_\eta(1/2,\sqrt3/2),\qquad
a=R_{3\eta}(1/2,\sqrt3/2).
\]

All coordinates are in `Q(sqrt3)`, using
`cos eta=(1-t^2)/(1+t^2)` and `sin eta=2t/(1+t^2)`.
The labeled source is

\[
\begin{array}{c|ccccccc}
\text{label}&0&1&2&3&4&5&6\\\hline
\text{point}&0&u&v&u+v&u+v+w&u+v+a&u+v+w+a.
\end{array}
\tag{6}
\]

Its only unit contacts are

```
01, 02, 13, 23; 34, 35, 46, 56.
```

They form two strict rhombi meeting at vertex `3`. The first has angle
`pi/3+eta` between `u,v`, the second the same angle between `w,a`.
Their two short diagonals are strictly greater than one. Every other
noncontact difference is a sum of at least two of `u,v,w,a`, all lying
in a cone of aperture less than `pi/2`; its length is greater than one.
Thus (6) is unit-separated and its actual contact graph is triangle-free.

The actual complete O–O trains of directions `u,w` are the contact pairs
`{01,23}` and `{34,56}`. Their midpoint crosscuts give layers

```
L={0,2}, M={1,3,5}, R={4,6}.
```

Move `M` by `Delta=w-u`. Both old cutsets exchange direction, and all
eight actual contacts remain unit. But

\[
|p'_1-p'_2|=|w-v|
=2\sin((\pi/3-\eta)/2)<1,
\tag{7}
\]

where the original `12` length was `2 sin((pi/3+eta)/2)>1`.
The opposite `v`-train crosses only the lower bounding train and ends in
`M`, exactly as required by Theorem 3. The second rhombus stays feasible:
its new short diagonal is `|u-a|=2 sin((pi/3+3eta)/2)>1`.

The amplitude `2 sin eta` tends to zero. All four projective directions
fall into two narrow phase windows near `0,pi/3`. This regression therefore
survives actual contact preservation, near-triangular rhombi, exact O–O cuts,
and arbitrarily small phase separation. It does not satisfy full-support
source KKT equilibrium, local trapping, the retained complete rectangle,
or global optimality. Its old diameter does not provide the required
strictly shortening moving-diameter condition. It rejects only the claimed
automatic immunity of all source rhombi, not the minimality fork or Level I.

## 7. Computation and hostile checks

[verify_target_c_swap_face_endpoints_2026_10_01.py](../../research/verify_target_c_swap_face_endpoints_2026_10_01.py)
uses exact `Q(sqrt3)` arithmetic to certify (6)--(7), the complete original
contact graph, both actual cutsets, all old contact lengths at the endpoint,
and the unprotected/remaining-rhombus diagonal comparison for 100 rational
parameters. No numerical tolerance is used. The universal proofs above do
not depend on the finite parameter sample.

The test omits global optimality, vertex equilibrium, actual diameter
decrease, a quadratic-size core, and fixed-star full-span diameter witnesses.
It is an exact geometric regression and does not prove a source competitor.

The following tempting upgrades were attacked and rejected or kept conditional:

| Claim | Classification | Decisive issue |
| --- | --- | --- |
| All near-unit blockers are old-face diagonals | Rejected as stated | Isolates may lie inside exceptional or outer faces |
| Every actual rhombus survives the swap | Rejected | Exact seven-point source (6) |
| A full-span opposite train protects all its boundary crossings | Proved candidate | Exact replacement directions (2) |
| Bad rhombi inject into middle terminal occurrences | Proved candidate | One-crossing property plus opposite-train immunity |
| Root harmonic defects absorb all global exceptional faces | Unproved | `Q_D` and global `Q` are different quantities |
| Linear failed swaps exceed endpoint capacity | Rejected counting shortcut | The available transverse train population is also linear |
| A new equilateral triangle at a feasible endpoint proves every source minimizer triangular | Rejected | Does not preserve the universal source quantifier |

## 8. Frontier effect and next obligation

The ONE-SIGN lower-distance obstruction now has a source-level trichotomy:

1. an unprotected rhombus, charged injectively to a transverse train end in
   the moving slab in the narrow arcs (3);
2. a bounded nonquadrilateral face, with the exact budget (5);
3. the unbounded face, including any dispatched isolate there.

The repair must exclude or release these obstructions together while using
actual positive equilibrium and the retained source embedding. For example,
a bound on terminal capacity in the narrow transverse arcs of all disjoint
ONE-SIGN slabs, strictly below the number of attempts after (5), would force
a fully lower-feasible swap. Existing geometry does not supply that bound:
the seven-point source demonstrates how a terminal witness can occur.

Other branches remain: exact phase, TWO-SIGN, split-star O–O, inactive
interfaces, macroscopic inactive containers/exterior caps, and sources
outside the fixed-star extraction. No canonical state, dependency graph,
or prompt is changed. Promotion recommendation: **unreviewed**, pending
independent audit of the new source-face and terminal proofs.
