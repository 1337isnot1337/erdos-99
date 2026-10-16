<!-- migration-source: path=docs/reports/target_c_isolate_paid_aggregate_detour_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=b6390d4e8f43a165d57558f2b857593c593b3fa7; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — isolate-aware aggregate detour payment

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-12.audit.46`
**Run type:** closing proof / source-level synthesis
**Target:** Target C-II / Level I
**Starting status:** canonical Sections 121–123; full-core residual outer detour open
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** not used
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This report does not claim a Level I solution. It records an isolate-aware finite
payment theorem and identifies exactly why it does not yet close the canonical
full-core branch.

## 1. Starting canonical endpoint

The canonical full-core inputs are

\[
 \liminf_{D\to\infty}{1\over D}
 \sum_r(L_r+P_{{\rm exc},r}-2d_r)
 \ge {\pi\over2}(2-\sqrt3),
 \tag{IP.1}
\]

and

\[
 \sum_rP_{{\rm exc},r}\le10(e_{BB}-k),
 \qquad k=d_H+s_Z.
 \tag{IP.2}
\]

The residual is the occurrence-counted outer-walk detour
\[
 T_{\rm out}:=\sum_r(L_r-2d_r).
\]
The attempted bridge was

```text
global full-source Oler slack + attachment-cell refinement
    -> upper bound on T_out
    -> contradiction with (IP.1)--(IP.2), strict sub-D source, or exact triangle
    -> Level I
```

The source is the full canonical source. Contact-isolated points are retained.

## 2. Strongest genuinely new result

**Classification:** unreviewed candidate; finite source-level payment theorem.

### Statement

Let `G` be the nonisolated positive-contact core of a canonical C-II representative,
let `F=conv(V(G))` be its force hull, and let

\[
 P_r=\operatorname{conv}(A_r),\qquad
 p_r=\operatorname{per}(P_r),\qquad
 d_r=\operatorname{diam}(P_r)
\]

be the canonical harmonic attachment cells. Let `A_{4,r}` be the total area of
strict quadrilateral contact faces in the induced graph on `I_r\cup A_r`, and put

\[
 G_r:=\operatorname{area}(P_r)-A_{4,r}.
\]

Let `Z_cell` be the number of contact-isolated source points assigned to the portions
of the global force-hull dissection lying in \(\bigcup_rP_r\). Then, in the Type-II
full-core branch,

\[
 \boxed{
 \sum_rG_r\le a_0 Z_{\rm cell}+C_0D+C_1,
 }
 \tag{IP.3}
\]

for universal constants `C_0,C_1`; here \(a_0=\sqrt3/2\). The constants are not
optimized. The bound is finite for every source and does not delete isolates.

Using canonical Section 121,

\[
 G_r\ge {3c_0\over5}(L_r+P_{{\rm exc},r}-p_r),
 \qquad c_0={\sqrt3\over4},
 \tag{IP.4}
\]

and the canonical perimeter bound \(\sum_rp_r=O(D)\), (IP.3) implies

\[
 \boxed{
 \sum_r(L_r+P_{{\rm exc},r}-2d_r)
 \le {10\over3}Z_{\rm cell}+C_2D+C_3.
 }
 \tag{IP.5}
\]

The coefficient `10/3` is only the exact isolate coefficient forced by
\(a_0=2c_0\); the boundary constants are deliberately left coarse.

Thus any super-boundary-order aggregate detour must be paid by contact-isolated
population inside the attachment-cell region. In particular, if a separate argument
gave `Z_cell=o(D)`, the residual detour would be boundary order. The canonical Type-II
statement only gives an `o(D^2)` inactive population globally, so it does not supply
that premise.

### Scope

This is a statement about the actual full source and actual canonical attachment
cells. It is not a scaffold estimate. Outer walks retain repeated vertices and bridge
occurrences. Isolates are counted rather than removed. The theorem is finite, with
the Type-II/full-core hypotheses used only to place the harmonic cells in the force
hull and to invoke the canonical global Oler-slack bound. No global-minimizer
contradiction is claimed.

## 3. Proof

### 3.1 Global force-hull dissection and its slack

Augment the straight-line positive-contact graph on the core by all missing sides of
the convex force hull `F`. Its bounded faces are convex; let `sigma_Q` denote the
canonical Oler slack of a bounded face `Q`, including any assigned isolated source
points in that face. The full-source cap/slack identity gives

\[
 W_F+W_{\rm ext}=\mathcal O_A+a_0L_F,
 \tag{IP.6}
\]

where `W_F,W_ext` are the sums of the nonnegative face and exterior-cap slacks,
\(\mathcal O_A\) is the global Oler slack, and `L_F` is the total force-hull-side
defect from the common source hull. The strict triangular-lattice comparison gives

\[
 \mathcal O_A<c_0P_K,
 \qquad L_F\le P_F,
 \qquad P_K,P_F\le\pi D.
 \tag{IP.7}
\]

Consequently

\[
 W_F\le W_F+W_{\rm ext}< (c_0+a_0)\pi D.
 \tag{IP.8}
\]

Only the boundary-order conclusion is needed below. This use of the full-source
slack is valid with contact-isolated points because their populations are included in
the face/cap Oler slacks.

### 3.2 Refinement by attachment-cell sides

Add every side of every `P_r` that is not already an edge of the global augmented
graph. The attachment cells have pairwise interior-disjoint interiors, so these
segments form a noncrossing refinement. Let \(\ell_{\rm add}\) be their total
Euclidean length. Since every pre-existing contact side has length one,

\[
 \ell_{\rm add}\le\sum_rp_r.
 \tag{IP.9}
\]

Canonical Section 62 gives

\[
 \sum_rp_r\le2\pi(q+1-k)\le2\pi(q+1)=O(D),
 \tag{IP.10}
\]

because `q<=pi D` and `k>=0`.

When a straight chord of length `ell` splits a convex face, the sum of the two
child Oler slacks exceeds the parent slack by exactly `ell`: the two child perimeters
gain `2ell`, while their boundary-vertex counts gain two. Applying this sequentially
to all added attachment sides gives

\[
 \sum_{Q\ {\rm refined\ inside}\ F}\sigma_Q
 \le W_F+\ell_{\rm add}=O(D).
 \tag{IP.11}
\]

This identity is an occurrence-counted planar refinement identity; it does not
identify distinct local outer-walk occurrences.

### 3.3 Which refined faces contribute to `G_r`

There is one geometric point that must be checked before identifying the local and
global face decompositions. The components' attachment-cell interiors are disjoint,
and every unloaded component is trapped in its own attachment cell. Thus an unloaded
vertex in the interior of `P_r` belongs to `I_r`. A loaded vertex in `A_r` is an
extreme vertex of the convex force hull `F`. For a convex polygon `P_r` whose
vertices are a subset of the extreme vertices of `F`, every segment from a vertex of
`A_r` to a vertex of `F\setminus A_r` leaves `P_r` immediately (the strict convexity
of `F` puts the omitted hull vertex outside the tangent cone of `P_r` at the chosen
vertex). Consequently a global contact edge from `A_r` to another loaded force-hull
vertex cannot cross the interior of `P_r`. If the other endpoint is an unloaded
vertex in a different component `I_s`, then the first endpoint also belongs to
`A_s`; the two convex cells `P_r` and `P_s` have disjoint interiors and share that
endpoint, so their interior tangent cones there are disjoint. The edge, which lies in
`P_s`, again cannot enter `int(P_r)`. Edges with both endpoints in `A_r` are included
in the induced local graph, and an edge with an unloaded endpoint in `I_r` has its
other endpoint in `I_r\cup A_r` by the definition of the unloaded component and its
attachment set.

Therefore every global contact edge meeting `int(P_r)` is an edge of the induced
local graph. This is the required source/face-embedding bridge; it is not a generic
scaffold assertion. If a contact-isolated point lies on an added attachment side, it
is inserted as a subdivision point and assigned to one adjacent refined face; this
only increases the recorded `Z_cell` or boundary count by an already counted source
point. Adding `partial P_r` now gives exactly the local convexified graph used in
canonical Section 121, up to shared-boundary conventions.

Its bounded faces consist of:

1. strict quadrilateral contact faces, whose total area is `A_{4,r}`; and
2. nonquadrilateral contact faces and the added-side pockets.

These faces partition `P_r` up to boundaries. Therefore the sum of the areas in
class 2 over all `r` is exactly \(\sum_rG_r\). If a global face is further split by
an attachment side, the corresponding pieces are the refined faces in (IP.11).
No contact rhombus is counted as class 2: a convex unit four-face is a strict unit
rhombus in the triangle-free source, and every such face inside `P_r` belongs to the
induced local graph.

### 3.4 Boundary-vertex count for the bad local faces

For one local graph write `L_r` for its occurrence-counted outer walk, `Q_r` for
the sum of `deg-4` over bounded nonquadrilateral faces, and `f_r` for their number.
Canonical Section 82 gives

\[
 L_r+Q_r=4a_r-6-2s_r-2c_r,
 \qquad Q_r\le2a_r,
 \tag{IP.12}
\]

and \(f_r\le Q_r\). Hence the total boundary-vertex occurrences on local
nonquadrilateral contact faces are at most

\[
 4f_r+Q_r\le5Q_r.
 \tag{IP.13}
\]

If `h_r` attachment sides are added, the sum of boundary-edge/vertex occurrences
over the resulting outer pockets is

\[
 L_r+2h_r-a_r\le L_r+a_r.
 \tag{IP.14}
\]

Thus the total boundary-vertex occurrence count `K_bad` over all refined non-rhombic
faces satisfies, with a deliberately coarse bound,

\[
 K_{\rm bad}
 \le\sum_r(5Q_r+L_r+a_r)=O\!\left(\sum_ra_r\right)=O(D).
 \tag{IP.15}
\]

The last step uses (IP.12), the canonical \(\sum_ra_r\le\sum_rp_r=O(D)\), and
nonnegativity. Repeated vertices and bridge occurrences are counted in `L_r` and
therefore only increase the right side.

### 3.5 Oler area estimate and the isolate term

For a refined non-rhombic face `Q`, let `k_Q` be its boundary source-vertex
occurrence count, `z_Q` the assigned isolate count, and `sigma_Q` its Oler slack.
The definition of the slack gives

\[
 {\operatorname{area}(Q)\over a_0}
 =\sigma_Q-{\operatorname{per}(Q)\over2}-1+k_Q+z_Q
 \le\sigma_Q+k_Q+z_Q.
 \tag{IP.16}
\]

Sum (IP.16) over all refined non-rhombic faces. The refined slack sum is `O(D)` by
(IP.11), the boundary-occurrence sum is `O(D)` by (IP.15), and the isolate sum is
exactly `Z_cell`. This proves

\[
 \sum_rG_r
 \le a_0Z_{\rm cell}+C_0D+C_1,
 \tag{IP.17}
\]

which is (IP.3).

### 3.6 Convert area payment to aggregate detour payment

Canonical Section 121 gives the finite local inequality (IP.4). Summing and using
(IP.17), with \(a_0/c_0=2\), gives

\[
 \sum_r(L_r+P_{{\rm exc},r}-p_r)
 \le {5\over3c_0}\sum_rG_r
 \le {10\over3}Z_{\rm cell}+O(D).
 \tag{IP.18}
\]

Finally `d_r>=0`, so

\[
 L_r+P_{{\rm exc},r}-2d_r
 \le (L_r+P_{{\rm exc},r}-p_r)+p_r.
\]

Sum this, apply (IP.10), and obtain (IP.5).

## 4. Exact frontier effect

The result identifies a source-level alternative that was previously hidden by
writing only `G_loc=o(D^2)`:

```text
aggregate outer detour
    <= isolate population in the attachment cells
       + boundary-order face/chord currency.
```

It does not close C-II. The canonical no-macroscopic-container branch supplies only
`Z_ch+Z_ext=o(D^2)`, not `Z_cell=o(D)`; the latter is the hypothesis needed to make
the isolate term boundary order. The macroscopic-container branch remains separately
open. Even with `Z_cell=0`, the coarse `O(D)` term in (IP.5) is not below the
canonical detour floor with the present constants.

The theorem also does not convert the detour into a strict source-preserving
diameter decrease. It is an upper bound on the actual source-associated aggregate,
not a deformation certificate.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Global face/cap Oler slack is `O(D)` | canonical inputs plus elementary strict comparison | C-II full-source Oler/cap ledger; `C-FULLCORE-NEAR-DISK` | Isolates are included in the slack; only `P_K,P_F<=pi D` is used |
| Adding a chord raises total face slack by its length | proved here | convex face refinement; Oler-slack definition | Exact perimeter and boundary-vertex cancellation |
| Attachment-cell sides have total added length `O(D)` | proved from canonical perimeter currency | `C-ATTACH-CURRENCY`, `C-HARMONIC-CELL-TILING` | `ell_add<=sum p_r=O(D)` |
| Local non-rhombic boundary occurrences are `O(D)` | proved here | canonical Section 82 identity; `sum a_r=O(D)` | Bridge and repeated-vertex multiplicity are retained |
| `sum G_r <= a0 Z_cell+O(D)` | unreviewed candidate | preceding claims; no isolate deletion | Requires the stated co-embedding/refinement identification of local faces |
| `sum detour <= (10/3) Z_cell+O(D)` | unreviewed candidate | candidate area payment plus canonical Section 121 | No contradiction claimed |
| `Z_cell=o(D)` in Type II | not proved | current C-II only gives global `o(D^2)` inactive population | This is the exact remaining isolate obstruction |
| Candidate closes Level I | rejected | missing isolate bound and strict competitor | No global quantifier discharged |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Contact-isolated source points | pass | They appear as `z_Q` and produce the explicit `a0 Z_cell` term |
| Full-source versus positive-contact core | pass | The refinement starts from the full-source force-hull dissection and never extends the ZR/ZF kernel theorem |
| Repeated outer walks and bridges | pass | All local occurrence counts are upper-bounded with multiplicity |
| Loaded-touching rhombi | pass | A rhombus inside a cell is included in that induced component; no global rhombus is silently discarded |
| Boundary chord splitting | pass | A chord adds perimeter `2ell` and two boundary occurrences, so slack rises by exactly `ell` |
| Macroscopic inactive chamber | uncovered | Its isolate population is retained and can make `Z_cell` quadratic |
| Vanishing-shear lattice regression | pass | The theorem uses no uniform angle gap or global-minimality inference |
| Square-grid boundary regression | pass | No claim that `p_r-2d_r=o(d_r)` is made |

## 7. Literature imports

None.

## 8. Computation

None was needed. The argument is a finite Euler/Oler/refinement calculation. No
floating-point constant is load-bearing.

## 9. Corrections / supersessions

This report does not supersede canonical Section 121's correction. In particular it
does not use the invalid implication `G_loc=o(D^2) => G_loc/d=o(1)`. It replaces that
discarded route with an explicit isolate term.

## 10. Promotion recommendation

**unreviewed**. Before promotion, independently audit the face-identification step
in §3.3 against shared boundaries of attachment cells and against isolates lying on
added attachment sides. Promotion would not change Level I status unless a separate
bound on `Z_cell` or a strict source-preserving deformation were also proved.

## 11. Handoff

1. New theorem: isolate-aware area and aggregate-detour payment (IP.3)–(IP.5).
2. Dependency chain: `C-HARMONIC-CELL-TILING` + `C-ATTACH-CURRENCY` + Section 82
   local face ledger + `C-LOCAL-RETURN-OLER-BRIDGE`.
3. Exact remaining lemma: prove `Z_cell=o(D)` with a global-minimality bridge, or
   use the explicit isolate population to construct a strict same-cardinality
   sub-diameter source.
4. Binding dead routes: density-only vanishing-shear exclusion, contact creation
   without force transfer, and `G_loc=o(D^2) => G_loc/d=o(1)`.
5. Next files: `docs/targets/target-c/77-inactive-chamber-saturation-audit.md`,
   `docs/targets/target-c/79-inactive-chamber-rhombic-saturation-dichotomy-audit.md`,
   `docs/reports/target_c_simultaneous_inactive_activation_2026-09-11.md`.
