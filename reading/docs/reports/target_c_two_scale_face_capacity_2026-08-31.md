> Generated reading edition · [exact source](../../../docs/reports/target_c_two_scale_face_capacity_2026-08-31.md) · source SHA-256 `061c800e4fadd946ae467414c41eeb2a6c99abddfa7917c8f52d6001d6fc8d0c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B9637175FB5B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C49: two-scale strict-rhombus capacity

**Date:** 2026-08-31
**Run type:** closing proof / synthesis
**Target:** C-II
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`
**External web search:** not used
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This report proves a new finite-capacity inequality for the fully force-visible
branch. It combines the C42 strict-rhombus bulk with the harmonic attachment-cell
geometry, while retaining a whole-hull fallback that does not require a cell-area
gap.

The key improvement over a cellwise Oler estimate is that a convex-hull loaded
vertex of contact degree at most three has at most two bounded-face incidences. The
cellwise boundary loss is therefore `2|B_+|`, not `3|B_+|`. The whole-hull estimate
charges every quadrilateral face and has no boundary-incidence loss at all.

## 1. Starting endpoint

Work in the C-II branch `C=C_*`, with a contact-minimal triangle-free global
minimizer and a relative-interior normalized KKT stress. Use the canonical notation

- `m` for the number of vertices in the nonisolated contact core;
- `q=|B_+|` for the positive diameter endpoint set;
- `c_I` for the number of components after deleting `B_+`;
- `e_BB` for the number of direct loaded-loaded unit contacts;
- `F=conv V(C)` for the contact-core hull;
- `A_F=area(F)`;
- `F_4` for the number of bounded degree-four contact faces; and
- `G=area(F)-sum_r area(P_r)` when `c_I>=1`, where
  `P_r=conv(A_r)` are the C36 attachment cells.

C42 gives

`F_4 >= m-5q+3c_I+3e_BB+5`.

The proposed September 5 force-bulk transport proof was withdrawn for a missing
whole-configuration jamming hypothesis. The estimate `n-m=O(D)` still needs a
valid proof. The present theorem isolates the core-capacity side of that bridge:

```text
C42 rhombic bulk + C36-C38 cells
    -> two exact core-capacity bounds
    -> a quantitative test for force-bulk transport / cell-area closure.
```

## 2. Convex-cell lemma needed for the refined bound

For each unpinned component `I_r`, let `A_r` be its distinct loaded attachment set
and `P_r=conv(A_r)`. C36 gives `I_r subset P_r`, `|A_r|>=3`, and noncrossing of
the attachment sets. C37 gives the planar incidence inequality.

### Lemma C49.1 — attachment cells have disjoint interiors

For distinct components `r!=s`,

`int(P_r) cap int(P_s)=emptyset`.

Consequently, with `G` as above, `G>=0`.

#### Proof

If the boundaries of `P_r` and `P_s` crossed properly, two sides would have four
endpoints alternating in the cyclic order on the convex force hull. This is exactly
the alternating configuration excluded by the C36 noncrossing attachment theorem.

It remains to exclude containment. Suppose `P_s subset P_r`. Every point of `A_s`
is an extreme vertex of `F`, while `P_r subset F`. An extreme vertex of `F` that
does not belong to `A_r` cannot lie in `conv(A_r)=P_r`; hence `A_s subset A_r`.
Since `|A_s|>=3`, the two components share at least three loaded attachments.

Restrict the C37 incidence graph to these two component nodes and three common
loaded vertices. It has six incidence edges. It is a connected simple bipartite
plane graph with three outer loaded vertices and two interior component vertices,
so C37's Euler bound gives

`6 <= 3+2*2-2=5`,

a contradiction. Thus neither proper crossing nor containment is possible. The
interiors are disjoint, and additivity of area gives `G>=0`. ∎

This proof is included so that the result uses only the promoted C36-C38 inputs;
it does not rely on an unpromoted attachment-cell report.

## 3. Two elementary face charges

Every bounded degree-four face in the C42 core is a strict unit rhombus. Therefore

`area(face)>sqrt(3)/2`.

All bounded faces of a straight-line plane graph lie in `F`, and distinct faces have
disjoint interiors. Thus every one of the `F_4` quadrilateral faces can be charged
to `F`, giving

`(sqrt(3)/2)F_4 < A_F`.

The inequality is also valid when `F_4=0`, since the C-II force hull is
two-dimensional and `A_F>0`.

For the cell charge, call a quadrilateral face **internal** if none of its vertices
lies in `B_+`, and let `F_4^I` be their number. At a convex-hull vertex `b`, all
contact edges lie in the interior wedge of the hull. The complementary exterior
wedge is one sector of the unbounded face, so at most `deg_C(b)-1` bounded face
corners occur at `b`. C35 gives `deg_C(b)<=3`; hence at most two bounded face
corners occur at each loaded vertex. Counting face corners therefore gives

`F_4-F_4^I <= 2q`,

or

`F_4^I >= F_4-2q`.  (C49.1)

Every internal quadrilateral has all four vertices in one unpinned component:
its boundary is a contact cycle, and deleting `B_+` leaves that cycle connected.
By C36 it lies in the corresponding cell `P_r`. The cells have disjoint interiors
by Lemma C49.1, so the internal quadrilateral faces can be charged disjointly to
the cell union:

`(sqrt(3)/2)F_4^I < sum_r area(P_r)=A_F-G`.

Together with (C49.1), this gives

`F_4 < (2/sqrt(3))(A_F-G)+2q`.  (C49.2)

## 4. Theorem C49 — two-scale strict-rhombus capacity

Under the hypotheses above,

$$
\boxed{
 m < \min\left\{
 \frac{2}{\sqrt3}A_F+5q-3c_I-3e_{BB}-5,
 \\
 \frac{2}{\sqrt3}(A_F-G)+7q-3c_I-3e_{BB}-5
 \right\}.}
\tag{C49.1}
$$

The first term is unconditional within C-II. The second is available when
`c_I>=1` and uses the attachment cells. In particular, using
`A_F<=pi D^2/4` and `q<=pi D`,

$$
\boxed{
 m < \Delta_2D^2+5\pi D-3c_I-3e_{BB}-5,
 \\[-1mm]
 m < \Delta_2D^2-\frac{2}{\sqrt3}G
       +7\pi D-3c_I-3e_{BB}-5,
 }
\tag{C49.2}
$$

where `Delta_2=pi/(2sqrt(3))`.

### Proof

Put

`d:=m-F_4`.

C42 gives the exact defect estimate

`d <= 5q-3c_I-3e_BB-5`.  (C49.3)

The whole-hull face charge in Section 3 gives

`m=F_4+d < (2/sqrt(3))A_F+d`.

Substituting (C49.3) proves the first member of (C49.1).

For `c_I>=1`, the cell charge (C49.2) instead gives

`m=F_4+d < (2/sqrt(3))(A_F-G)+2q+d`.

Substitution of (C49.3) proves the second member. Taking the smaller of the two
valid estimates proves (C49.1).

Finally, `F` has diameter `D`, so the isodiametric inequality gives
`A_F<=pi D^2/4`. The unit-separated convex-hull vertices satisfy
`q<=per(F)`, and the convex perimeter-diameter inequality gives
`per(F)<=pi D`; hence `q<=pi D`. Applying these estimates gives (C49.2). ∎

## 5. Exact target implication

The prior cellwise capacity route paid a component-perimeter error of order
`D c_I`. C49 replaces it by the C42 defect plus a loaded-boundary term:

`m < 2(A_F-G)/sqrt(3) + 7q - 3c_I - 3e_BB - 5`.

The theorem also supplies the fallback

`m < 2A_F/sqrt(3) + 5q - 3c_I - 3e_BB - 5`,

which remains available even when `G` is too small to help. Thus the exact
remaining capacity problem is narrower:

> prove either a force-bulk estimate for `n-m`, or a lower bound on `G` (or on a
> different strict-packing charge) that exceeds the explicit linear error in
> (C49.2).

C49 does not assert either missing statement. It is a core theorem, not a Level I
closure.

## 6. Why this is new and helpful

1. C42 supplied `F_4=m-O(D)` but did not charge the rhombi to area.
2. The cellwise capacity report charged internal faces but used a `3q` loaded-face
   incidence loss. C49 proves the sharper geometric `2q` loss and retains a whole-
   hull fallback with zero incidence loss.
3. The result is a single exact minimum of two bounds. A future response-area or
   force-bulk theorem can use whichever scale is stronger without assuming that the
   cell union has a macroscopic area deficit.

## 7. Scope and regression audit

| Claim | Classification | Reason |
| --- | --- | --- |
| C49.1 two-scale capacity | proved | Euler/C42 defect, strict rhombus area, convex-face incidence, and C36-C38 geometry suffice |
| `F_4-F_4^I<=2q` | proved | each loaded hull vertex has one unbounded-face sector and degree at most three |
| positive uniform rhombus area gap | rejected | rhombus angles may approach `60` degrees; only strict `>sqrt(3)/2` is used |
| `n-m=O(D)` | open; September 5 proof withdrawn | pinned core jamming does not make every isolated source point diametral |
| `G=Omega(D^2)` | open | one cell may equal the whole force hull, and near-partitions may have small gap |
| Level I resolution | open | C-I and the global C-II force-bulk/response endpoint remain |

Binding regressions are respected:

- an oblique rhombic grid with linear boundary defect is not excluded;
- a single attachment cell with `G=0` is allowed;
- cells can share boundary vertices or chords, since only interiors are charged;
- no lower bound on any KKT or response conductance is used; and
- contact-isolated source points are explicitly not counted by `m`.

## 8. Dependencies

- `docs/targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md`, C35;
- `docs/targets/target-c/04-near-minimal-response-frontier.md`, C36-C38;
- `docs/targets/target-c/05-quadrangulation-defect-frontier.md`, C42;
- the canonical convex perimeter-diameter and isodiametric inequalities already
  used in C30/C42; and
- the C37 planar attachment-incidence Euler bound.

No literature or computation is imported.

## 9. Canonical promotion recommendation

**Promote now.** The proof is exact, the added `2q` incidence lemma is audited, and
the fallback/cellwise minimum changes the quantitative C-II capacity frontier. It
does not change the Level I status.

Recommended edits:

- index this report in `docs/targets/target-c/README.md`;
- add the exact two-scale statement to
  `docs/targets/target-c/05-quadrangulation-defect-frontier.md`; and
- add the two-scale capacity theorem to the active Target C prompt while preserving
  the force-bulk gap.

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem C49:
In fully force-visible C-II, strict unit-rhombic bounded faces give

  m < min{ 2 area(F)/sqrt(3) + 5q - 3c_I - 3e_BB - 5,
            2(area(F)-G)/sqrt(3) + 7q - 3c_I - 3e_BB - 5 }.

The first bound charges every quadrilateral to the whole force-core hull. The second
charges quadrilaterals without loaded vertices to pairwise interior-disjoint harmonic
attachment cells. The loaded-face loss is 2q because a loaded convex-hull vertex has
one unbounded-face sector and degree at most three.

Exact endpoint:
prove n-m=O(D), or prove an area/response gap exceeding the explicit linear error.

LEVEL I remains open; C-I shear and the global C-II obstruction are not closed.
```
