> Generated reading edition · [exact source](../../../docs/reports/target_c_harmonic_cell_strip_width_2026-09-25.md) · source SHA-256 `ac5e28579556bdab5a189adf506858ec636cfa509e30821b6ee8957e7ea50797`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A31631266C12","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_harmonic_cell_strip_width_2026-09-25.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=ed36019846b3250cbe4e23133dd5053f20f99279; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — sharp strip and closing-chord charges for harmonic cells

**Date:** 2026-09-25  
**Repository commit:** `404e8d49ddb1ee14cd0f69a83e7f120e77b3ab33`  
**State version:** `2026-09-14.audit.51`  
**Run type:** closing-proof attempt and geometric regression audit  
**Target:** C-II full-core branch  
**Starting status:** canonical Sections 62, 83, 122--123  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**External literature search:** no imported theorem  
**Computation:** not used

## LEVEL I STATUS

STILL OPEN.

## 1. Starting endpoint and tested implication chain

In the canonical full-core branch, Section 122 requires a linear aggregate
`sum_r(L_r+P_exc,r-2d_r)`, while Section 123 pays exceptional-face perimeter
by `10(e_BB-k)`. The remaining target is a source-level restriction on the
attachment-cell geometry that either charges the aggregate outer-walk detour
or yields a strict same-cardinality sub-`D` configuration.

The chain tested here was

```text
positive-contact component with at least three loaded attachments
    -> a fixed minimum width and area per cell diameter
    -> exclusion of shallow thin-cap storage of excess cell diameter
    -> hoped-for stronger Section-122 area-weighted detour demand.
```

The first two arrows are proved. The last arrow does not follow: caps of a
larger fixed thickness retain the same linear-diameter/subquadratic-area
scaling. A second exact lemma below charges the long closing chord of any
populated cap to the canonical augmented-cell defect `e_BB-k`. Neither
charge alone closes C-II.

## 2. Sharp finite theorem

**Classification:** proved candidate awaiting independent audit; noncanonical.

Let `A` be any finite unit-separated planar set whose unit-contact graph has
no triangle. Let `I` be a nonempty connected set of contact vertices, and let
`T` be its distinct neighbors outside `I`. Suppose `|T|>=3` and
`I subset conv(T)`. Then, with `P=conv(T)` and `d=diam(P)`, the minimum width
of `P` satisfies

```math
\boxed{\operatorname{width}(P)>\sqrt3/2,\qquad
       \operatorname{area}(P)>(\sqrt3/4)d.}
\tag{SW.1}
```

In particular (SW.1) holds for every actual harmonic attachment cell
`P_r=conv(A_r)` of canonical Target C: Section 62 supplies a connected
unloaded component `I_r`, harmonic trapping `I_r subset P_r`, and at least
three distinct loaded attachments. Contact-isolated source points play no
role in the proof and remain present in the source.

The historical width lemma for convex **unit-sided contact faces** does not
give this statement: attachment-cell sides can be long noncontact chords.
The connected three-attachment source graph is the new hypothesis here.

### Strip lemma

If a unit-separated, triangle-free finite set lies in a strip of width at
most `sqrt(3)/2`, its unit-contact graph has maximum degree at most two.

To prove this, rotate the strip to be horizontal and fix a vertex `p`.
Relative to `p`, the vertical coordinates of its unit neighbors lie in
`[-s,t]`, where `s,t>=0` and `s+t<=sqrt(3)/2`: the interval also contains
the vertical coordinate zero of `p`. On either the right or left open
semicircle about `p`, the available directions occupy an angular interval
of length

```math
\arcsin s+\arcsin t\le\arcsin(s+t)\le\pi/3.
\tag{SW.2}
```

The first inequality follows from the addition formula, or by observing
that `arcsin s+arcsin(w-s)` has its maximum at an endpoint for
`0<=s<=w<=sqrt(3)/2`. The endpoints at horizontal displacement zero are
unavailable because they would have vertical displacement one. If two
unit neighbors occupy the same open semicircle, their angular separation
is at most `pi/3`. Their mutual distance is then at most one; unit
separation makes equality necessary, creating a unit triangle with `p`.
Since triangles are excluded, there is at most one neighbor in each
semicircle and at most two in total.

### Application to an attachment component

If `width(P)<=sqrt(3)/2`, then `I union T subset P` lies in such a strip.
Consider only the contacts internal to `I` and the contacts from `I` to
`T`. By the strip lemma every vertex of `I` has degree at most two in this
graph. If `I` has more than one vertex, its connected internal graph is a
path or cycle. A cycle admits no attachment edge. A path admits an
attachment only at either end, at most one per end. If `I` is a singleton,
it has at most two attachment edges. Thus in every case `|T|<=2`, contrary
to the hypothesis. This proves the strict width inequality.

Choose endpoints `a,b` of a diameter of `P` and let `W` be the width
perpendicular to `ab`. The triangles with base `ab` and respective points
on the top and bottom support lines lie in `P` and have disjoint interiors.
Their combined area is `dW/2`. Since `W>=width(P)>sqrt(3)/2`, the area
inequality in (SW.1) follows.

### Sharpness, including harmonic balance

The constants cannot be increased under these hypotheses. Put an unloaded
point at the origin and three loaded attachment points on the unit circle
at angles

```math
0,\quad \pi/3+\varepsilon,\quad 4\pi/3-\varepsilon,
\qquad 0<\varepsilon<\pi/6.
```

All three origin-to-attachment edges are unit contacts. Their pairwise
angular gaps are `pi/3+epsilon`, `pi-2epsilon`, and
`2pi/3+epsilon`; each is strictly between `pi/3` and `pi`, so the three
attachments are pairwise farther than one apart and the origin lies
strictly inside their triangle. Hence positive contact weights balancing
the origin exist, and the contact graph is a triangle-free star. As
`epsilon` decreases to zero, the two latter attachments become antipodal,
the attachment triangle has diameter tending to two, minimum width
tending to `sqrt(3)/2`, and area tending to `sqrt(3)/2`. Thus its
area/diameter ratio tends to `sqrt(3)/4`. In this limit one balancing
contact weight tends to zero; harmonicity alone gives no uniform width gap.

This four-point example is a feasible contact geometry, not a global
minimizer or a canonical post-ZF source.

## 3. Exact closing-chord defect charge

**Classification:** proved candidate awaiting independent audit; a finite
corollary of canonical Section 123.

Work in the canonical full-core branch, and let `S` be any collection of
actual harmonic attachment cells. Suppose each `P_r`, `r in S`, has `M_r`
consecutive unit loaded-hull sides and one closing nonunit attachment
chord of length `ell_r>3` (this is a chord length, not Section 123's
local surplus `s_r`). Thus `a_r=M_r+1`. Then

```math
\boxed{\quad
2(e_{BB}-k)\ge
\sum_{r\in S}\bigl(M_r+\lceil \ell_r\rceil-3\bigr).
\quad}
\tag{CC.1}
```

For a short convex cap whose closing chord realizes its diameter
`d_r=ell_r`, this implies

```math
\boxed{\quad
e_{BB}-k\ge
\sum_{r\in S}d_r-\frac32|S|.
\quad}
\tag{CC.2}
```

The proof uses the actual augmented graph `J_r^+` of Section 123. Every
edge except the closing chord is a unit edge: internal and attachment
edges are contacts, and the remaining attachment-polygon sides are the
specified unit hull sides. The closing chord borders one bounded face
inside `P_r`. Delete that chord from the face boundary walk. The remaining
walk joins its endpoints using unit edges and therefore has at least
`ceil(ell_r)` edge occurrences. The face degree is at least
`ceil(ell_r)+1`, so its contribution to the augmented degree defect is at
least `ceil(ell_r)-3`:

```math
Q_r^+\ge\lceil \ell_r\rceil-3.
\tag{CC.3}
```

Every edge of `J_r^+` other than the closing chord is an actual unit
contact of the source. A triangular face omitting the chord would
therefore be a forbidden source unit triangle. Every triangular face
must contain the closing chord, which borders only one bounded face;
hence `T_r<=1`. Consequently

```math
a_r-T_r+Q_r^+
\ge M_r+\lceil \ell_r\rceil-3.
\tag{CC.4}
```

Canonical Section 123's exact identity is

```math
2(e_{BB}-k)
=\sum_r(a_r-T_r+Q_r^+)+2d_{tile},
\qquad d_{tile}\ge0.
```

Each omitted cell summand is nonnegative by its local Section-123 identity.
Keeping only cells in `S` and using (CC.4) proves (CC.1). Since the
unit-side arc gives `ell_r<=M_r`, (CC.1) implies (CC.2) when
`d_r=ell_r`.
Repeated contact-walk vertices are counted as edge occurrences in
(CC.3); no simple-path assumption is made.

## 4. Effect on the thin-cap regression

The geometric cap construction in open PR #583 uses blocks of
`M=floor(sqrt(D))` consecutive unit sides of a regular near-disk polygon.
Its cap sagitta is

```math
h={D\over2}\bigl(1-\cos(M\arcsin(1/D))\bigr)
  \longrightarrow {1\over4}.
\tag{SW.3}
```

The cap lies in a strip of width `h`. For large `D`, (SW.3) is below
`sqrt(3)/2`; no such cap can be an actual harmonic attachment cell with
three loaded attachments in a triangle-free source. This does not invalidate
PR #583, which explicitly constructs only an abstract convex-cell tiling.

The width theorem does not eliminate the geometric storage mechanism.
Replacing its block length by `M=floor(lambda sqrt(D))` for any fixed
`lambda>sqrt(2sqrt(3))` changes the sagitta limit to `lambda^2/4`, above
the strip threshold. With `N=floor(cD/M)` caps, `0<c<1`, the exact regular
polygon formulas still give `N=Theta(sqrt(D))`, cap diameters
`M(1+o(1))`, total cap diameter `cD+o(D)`, and total cap area `O(D)`.
No positive-contact components or global-minimality certificate are
constructed by this rescaling. It shows why (SW.1), by itself, cannot
raise the area-weighted Section-122 detour floor by a fixed multiple of
`D`.

If the rescaled geometric caps were actual harmonic cells, (CC.2) would
charge their `cD+o(D)` total diameter almost one-for-one to `e_BB-k`,
because their number is only `Theta(sqrt(D))`. The original shallow caps
fail the sharper finite width requirement (SW.1); fixed-thickness caps
above that threshold remain geometrically possible and would require
linear `e_BB-k` currency. The currently open high-surplus Type-II regime
can pay a linear amount, so neither theorem proves a contradiction.

One tempting stronger inference fails at the direction of the canonical
diameter-budget inequality. The promoted budget floor uses
`sum_r delta_r <= 6+mu_D D`, with `d_r<=delta_r+2`; it does **not** say
`sum_r d_r` is close to `mu_D D`. Thus the necessary floor
`mu_D>=mu_TC+o(1)` does not force a cap tail of length
`(mu_TC-1)D`. Applying (CC.2) with that invented tail would be invalid.

## 4. Scope, dependencies, and remaining lemma

The strip lemma and (SW.1) are finite statements for arbitrary feasible
triangle-free unit-separated sets. Their only canonical input in the
Target C application is Section 62 (`C-ATTACH-CURRENCY`): connected
unloaded components, at least three loaded attachments, and harmonic
trapping inside `P_r`. The area bound is elementary convex geometry.
The closing-chord charge (CC.1) additionally uses canonical Section 123
(`C-AUGMENTED-CELL-DEFECT-BUDGET`) and applies only to actual cells with
the specified unit-side attachment polygon. The comparison with PR #583
is a scope audit of an unreviewed regression, not a theorem dependency.
No external literature or computation is used.

The new theorem rules out cells whose thickness is below a fixed unit
scale. It does not bound the number of fixed-thickness caps, their total
diameter, `e_BB-k`, or the actual source diameter; no canonical frontier
changes. Formula (CC.2) pays long cap chords almost one-for-one through
`e_BB-k`, but the live ledger permits that currency to be linear. A
precise next lemma for this mechanism would have to show that **actual
fixed-thickness, `Theta(sqrt(D))` cap cells either pay strictly more than
(SW.4) in a currency with a matching upper bound, force an exact unit
triangle, or admit a same-cardinality strict sub-`D` replacement**. A
mere positive width or area-per-diameter bound cannot do so, as rescaled
caps retain `Theta(D)` total diameter at `O(D)` total area.

## 5. Claim and regression audit

| Claim | Classification | Reason |
| --- | --- | --- |
| Strip maximum-degree-two lemma | Proved candidate awaiting promotion | Exact circle-arc proof above; triangle-free hypothesis is used at equality |
| Harmonic-cell width and area bounds (SW.1) | Proved candidate awaiting promotion | Section-62 attachments plus strip lemma |
| A uniform improvement above `sqrt(3)/2` from positive harmonic weights | Rejected under these hypotheses | Sharp star has positive weights and tends to equality |
| PR #583 shallow caps realize harmonic cells | Rejected as an inference | Their width tends to `1/4`, violating (SW.1); PR #583 did not claim source realization |
| Width bound closes the Section-122 aggregate detour | Rejected as an inference | Rescaled fixed-thickness caps preserve the relevant scalar scaling |
| Closing-chord charge (CC.1)--(CC.2) | Proved candidate awaiting promotion | Section 123 identity, unit-side exclusion, and face-degree lower bound |
| The `mu_D` floor forces cap diameter excess `(mu_TC-1)D` | Rejected as an inference | The canonical ledger gives an upper budget for `sum delta_r`, not an equality or lower bound on cap diameters |

The argument retains contact-isolated source points, never identifies a
convex-cell construction with a global minimizer, and does not infer a
finite motion from contact geometry. It does not use the rejected
full-source ZR/ZF extension, Euler-path inference, FB4 localization,
RSR uniqueness, or the Section-121 normalization error.

## 6. Promotion and handoff

**Promotion recommendation:** preserve as an unreviewed proved candidate
for independent audit. Its proof is elementary and exact, but it does not
change the current C-II or Level I endpoint, so this report does not edit
the theorem-state manifest, route map, or prompt.

The next agent should use canonical Sections 62, 122, and 123, then test
fixed-thickness populated cap cells against the actual loaded-hull and
diameter graph. The open PR #583 cap construction remains a valid
*geometric* regression; (SW.1) rules out its shallow version as a source
cell, while (CC.1) identifies the source currency needed by longer caps.
