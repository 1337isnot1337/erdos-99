<!-- theorem-state: {"artifact_id":"ART-85E01791693F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_harmonic_cap_endpoint_turning_2026-09-25.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=92eb23cbca3cc4c4820b448c99afca30067b2dfa; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — endpoint turning forbids many populated unit-side caps

**Date:** 2026-09-25
**Repository commit:** `404e8d49ddb1ee14cd0f69a83e7f120e77b3ab33`
**State version:** `2026-09-14.audit.51`
**Run type:** closing-proof attempt and exact geometric regression audit
**Target:** C-II full-core branch
**Starting status:** canonical Sections 62, 80, 83, 122--123
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** no imported theorem
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

## 1. Exact starting endpoint and implication chain

In the canonical Type-II full-core branch, Section 122 forces linear
aggregate harmonic-cell detour, and Section 123 pays exceptional perimeter
through `e_BB-k`. The promoted diameter-budget floor also permits excess
total cell diameter. A geometric regression in open PR #583 stores linear
total diameter in `Theta(sqrt(D))` shallow caps of total area `O(D)`; open
PR #585 proves that its original width is too small for populated harmonic
cells, but its larger fixed-thickness regular-polygon caps retain the same
area/diameter scaling as abstract convex cells.

The tested chain is

```text
an actual attachment at each end of a unit-side cap arc
  -> strictly more than 120 degrees of loaded-hull turning per cap
  -> at most two such actual harmonic cells
  -> no linear diameter stored in subquadratic-area cells of this topology
  -> a narrower full-core aggregate-detour obligation (not Level I closure).
```

The first three arrows are finite and proved below. The fourth uses the
canonical Type-II near-disk force hull. Other harmonic-cell topologies and
the high-surplus regime remain.

## 2. Finite endpoint-wedge theorem

**Classification:** proved candidate awaiting independent audit; this
report is `unreviewed` and noncanonical.

Let `A` be any finite unit-separated planar set with no unit equilateral
triangle. Let `F` be a convex polygon whose vertices are points of `A`.
Suppose `I` is a nonempty connected vertex set in the unit-contact graph
(canonically, a component of the induced unloaded contact graph), and
`T` is its set of distinct unit-contact neighbors outside `I`, all on `F`.
Assume every `u in T` has a unit-contact neighbor in `I` and
`I subset P:=conv(T)`. The canonical Section-62 harmonic component has
exactly these properties, with `F` the full actual loaded force hull.

Suppose `P` is a **cap cell**: its vertices, in cyclic order, are
`v_0,...,v_M`, a consecutive block of vertices of `F`, and its boundary
is the corresponding `F` arc followed by the closing chord `v_Mv_0`.
Write `s_0=|v_1-v_0|`, `s_M=|v_M-v_{M-1}|`, and let `turn_F(v)` denote the
nonnegative exterior turning angle of `F` at a vertex. Define

\[
 \psi(s)=\begin{cases}\arccos(s/2),&1\le s<2,\\0,&s\ge2.\end{cases}
\]

### Theorem 1 (endpoint and global turning charge)

For every cap cell,

\[
 \boxed{\displaystyle
 \sum_{i=1}^{M-1}turn_F(v_i)
 \ge\psi(s_0)+\psi(s_M).}
 \tag{1}
\]

If `s_0=1`, its contribution in (1) is **strictly greater** than
`pi/3`; likewise for `s_M=1`. Hence a cap cell whose two endpoint sides
are unit contacts consumes strictly more than `2pi/3` of the actual
loaded-hull turning.

For any family of cap cells with pairwise interior-disjoint polygons, their
loaded-hull arcs are edge-disjoint and their internal-vertex turn sets are
disjoint. Consequently

\[
 \boxed{\displaystyle
 \sum_{r}\bigl(\psi(s_{0,r})+\psi(s_{M,r})\bigr)
 \le 2\pi.}
 \tag{2}
\]

In particular, **at most two** actual harmonic cap cells can have both
endpoint sides unit. This includes every cap cell with `M` consecutive
unit loaded-hull sides and one nonunit closing chord, the topology used
in PR #585's closing-chord charge. More generally, if `m_B` is the
number of nonunit sides of `F`, the number of all cap cells of this
one-chord/consecutive-block topology is at most `m_B+2`: at most two
have both endpoint sides unit, and each remaining cell uses a distinct
nonunit endpoint side.

### Proof

Fix the first endpoint `u=v_0`, its next hull vertex `w=v_1`, and an
actual unit-contact neighbor `x in I` of `u`. Harmonic trapping puts
`x in P`. Let `alpha_0` be the interior angle of `P` between the side
`uw` and the closing chord `uv_M`. Then the angle
`theta=angle xuw` lies in `[0,alpha_0]`. By the cosine rule,

\[
 |x-w|^2=1+s_0^2-2s_0\cos\theta\ge1,
\]

so `cos(theta)<=s_0/2`. If `s_0<2`, this gives
`alpha_0>=theta>=arccos(s_0/2)=psi(s_0)`. If `s_0=1`, equality
`theta=pi/3` would give `|x-w|=1`, making `u,x,w` an exact unit
equilateral triangle. Triangle-freeness therefore makes
`alpha_0>pi/3`. The same argument at `v_M` gives
`alpha_M>=psi(s_M)`, strictly `>pi/3` when `s_M=1`.

The sum of exterior turns around the convex polygon `P` is `2pi`.
Its exterior turns at the two chord endpoints are `pi-alpha_0` and
`pi-alpha_M`. At each internal arc vertex `v_i`, both incident sides
of `P` are the corresponding consecutive sides of `F`, so its exterior
turn in `P` equals `turn_F(v_i)`. Subtracting the endpoint turns gives

\[
 \sum_{i=1}^{M-1}turn_F(v_i)=alpha_0+alpha_M,
\]

which proves (1), including strictness.

Now take two positive-area cap polygons with disjoint interiors. If they
shared a side of `F`, each would contain points arbitrarily close to the
relative interior of that side on the **same inward side** of `F`, so
their interiors would overlap. Thus their `F` arcs are edge-disjoint.
An internal vertex of one arc uses both adjacent `F` edges, and hence
cannot be an internal vertex of another edge-disjoint arc. All exterior
turns of `F` are nonnegative and sum to `2pi`; summing (1) proves (2).
Three cells with two unit endpoint sides would demand strictly more
than `3(2pi/3)=2pi`, proving the two-cell bound. A cell not counted
there uses at least one nonunit endpoint side. Its assigned endpoint
side is distinct from every other cell's because the arcs are
edge-disjoint, giving the `m_B+2` bound. `square`

### Scope check for the canonical cells

Section 62 gives `T=A_r`, every attachment vertex has a contact into
`I_r`, and `I_r subset conv(A_r)`. Section 83 proves that distinct
positive-area attachment cells have disjoint interiors. Every member
of `A_r` is an extreme vertex of `F`, so a cell whose attachment set
is a consecutive loaded block has exactly the cap polygon described
above. Contact-isolated source points are retained globally and are
never used as harmonic-component vertices.

The theorem does not assume that the unit-side cap is itself globally
optimal, that its loaded hull is circular, or that a diameter pair is
confined to the cap. The angle bound uses only the **actual** trapped
unit-contact neighbor of each endpoint.

## 3. Full-core area/diameter consequence

**Classification:** proved candidate awaiting independent audit; depends
on canonical Type-II near-disk force-hull convergence.

Let `S_D` be the set of actual Type-II harmonic cap cells whose attachment
polygons have consecutive **unit** loaded-hull sides and one closing
chord. Then `|S_D|<=2` for every source. If

\[
 \sum_{r\in S_D}area(P_r)=o(D^2),
\]

then

\[
 \boxed{\displaystyle\sum_{r\in S_D}diam(P_r)=o(D).}
 \tag{3}
\]

To prove this, suppose along a subsequence one such cell has diameter
`d_r>=epsilon D` for some fixed `epsilon>0`. Its diameter is attained by
two attachment vertices `a,b`. Choose the consecutive unit-edge subarc
of its loaded-hull arc from `a` to `b`. Canonical Section 80 gives,
after suitable translation, `F/D` converging in Hausdorff distance to
the radius-`1/2` disk. Every vertex of the subarc is on `partial F`,
hence lies `o(D)` from that circle. Its normalized edge mesh is `1/D`.
After subsequence extraction, the normalized subarc therefore has a
connected limit in the circle containing two distinct limit points
`a_infty,b_infty` at distance at least `epsilon`. Any connected subset
of the circle containing those points contains a nontrivial circular
arc. The convex hull of that arc has strictly positive area. Since
`P_r` contains the subarc, lower semicontinuity of convex-hull area
gives `area(P_r)>=c(epsilon)D^2` for some `c(epsilon)>0`, contrary to
the assumed `o(D^2)` total area. Thus every one of the at most two
cells has `d_r=o(D)`, proving (3).

For the regular near-disk polygon caps of PR #583 and PR #585, with
`M=Theta(sqrt(D))` consecutive unit sides, the endpoint angle between
the first side and closing chord is
`(M-1)arcsin(1/D)=o(1)` (the shell radius is `D/2`). It violates
the strict `>pi/3` endpoint requirement regardless of the cap's fixed
thickness. Thus **neither the original shallow nor the rescaled
fixed-thickness regular-polygon caps can be actual harmonic cells**.
This does not invalidate those reports' geometric regressions; they
explicitly do not construct a canonical source.

## 4. Failed closures and exact remaining lemma

The turning theorem kills a specific linear-diameter storage mechanism,
but it does not upper-bound the whole aggregate detour of Section 122.
Cells with nonunit endpoint hull sides can evade the `120`-degree
charge; their count is paid only by `m_B`, which may be linear in the
open high-surplus regime. Cells whose attachment sets are not one
consecutive loaded block are outside the cap topology. Two
macroscopic-area cap cells also remain possible and can contribute
linear diameter.

The next geometric proposition for this mechanism is precise:

> **Noncap/high-surplus release.** In every canonical Type-II survivor,
> either all subquadratic-area harmonic cells outside the two-unit-end
> cap class have total diameter `o(D)`, or their actual nonunit endpoint
> sides and noncap attachment topology force an exact triangle or a
> same-cardinality unit-separated configuration of diameter `<D`.

This proposition is **not proved**. A pure area/diameter scalar bound is
also insufficient by the existing full-core scalar compatibility
regression. The new finite turning charge must be coupled to the
loaded-hull/diameter graph or to an explicit source replacement.

## 5. Claim and regression audit

| Claim | Classification | Exact check |
| --- | --- | --- |
| Endpoint wedge (1) | proved candidate awaiting independent audit | Cosine rule uses the actual unit attachment and separation from the neighboring loaded vertex. |
| Global turning (2), at most two unit-end cap cells | proved candidate awaiting independent audit | Section-83 cell interiors and disjoint loaded-hull edge arcs. |
| Subquadratic unit-side cap diameter (3) | proved candidate awaiting independent audit | Canonical Type-II force-hull near-disk convergence and unit edge mesh. |
| Fixed-width regular-polygon caps can realize harmonic cells | rejected inference | Endpoint angles tend to zero, violating (1). |
| All cap or full-core regimes eliminated | not proved | Nonunit endpoints, noncap cells, and high surplus remain. |

Relevant regressions remain respected: no source point is dropped; a
geometric cap tiling is not identified with a positive-contact source;
no collection of individually feasible motions is assumed simultaneous;
no Euler trail is inferred from incident diameter edges; no finite
release is inferred from a KKT zero multiplier. The theorem is finite
where claimed and uses `o(D^2)` only for the Type-II corollary, whose
conclusion is merely `o(D)` aggregate cap diameter.

## 6. Dependencies and promotion recommendation

- `C-ATTACH-CURRENCY`: `docs/targets/target-c/62-attachment-incidence-currency-audit.md`, harmonic trapping and actual attachment definition; canonical.
- `C-HARMONIC-CELL-TILING`: `docs/targets/target-c/83-attachment-cell-disjoint-tiling-audit.md`, pairwise interior-disjoint actual cells; canonical.
- `C-FULLCORE-NEAR-DISK`: `docs/targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md`, (80.34); canonical, used only for (3).
- Sections 122--123 determine why aggregate cell diameter and detour matter; they are not used in the finite proof.
- Open PRs #583 and #585 are research context/regressions, not theorem dependencies.

**Promotion recommendation: unreviewed.** An independent audit should check
the endpoint-neighbor scope, equality of cap and force-hull turns, the
disjoint-arc argument, and the near-disk compactness step before any
canonical-state change. No state manifest or active prompt is edited here.
