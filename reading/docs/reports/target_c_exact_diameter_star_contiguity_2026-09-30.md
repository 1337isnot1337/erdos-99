> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_diameter_star_contiguity_2026-09-30.md) · source SHA-256 `5014deda8388b7236a260f3a963aaf030b20db9e7fbaf65835b7490a7a16e252`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-17B2DB88C121","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: exact contiguity of diameter stars

**Date:** 2026-09-30<br>
**Base main:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**State version:** `2026-09-14.audit.51`<br>
**Classification:** proved candidate awaiting promotion; noncanonical.<br>
**Level I:** open. C-II remains open.

## Statement

Let $`A\subset\mathbb R^2`$ be a finite set of diameter $`D>0`$. Let
$`H=(B,E)`$ be its full diameter graph, with isolated vertices omitted, and
suppose $`F=\operatorname{conv}B`$ is two-dimensional. Write
$`q=|B|`$, $`h=|E|`$, and $`d_H=q-h`$. Order the distinct projective
directions of the diameter edges on $`\mathbb R/\pi\mathbb Z`$.

1. Every vertex's incident edges form one cyclic interval of that order.
2. If $`H`$ is not a star, every interval is proper. With the notation of
   `target_c_rooted_direction_reentry_defect_2026-09-30.md`, exactly
   ```math
   t_v=1\quad(v\in B),\qquad R_D=0,\qquad m_D=d_H.
   
   ```
3. In the non-star case, every consecutive direction pair with a shared
   endpoint $`v`$, say $`vx,vy`$, generates a hull side $`xy`$. These
   generated sides are distinct. There are exactly
   ```math
   2h-q=q-2d_H
   
   ```
   such sides. Exactly $`2d_H`$ sides of $`F`$ are not generated.

No separation assumption, global minimality, near-disk limit, stress theorem,
Woodall classification, or computational certificate is needed for this finite
geometric statement.

## Proof

### A diameter endpoint is uniquely exposed

For a diameter pair $`vw`$, put $`u=(v-w)/D`$. For any $`p\in A`$,
$`|p-w|\le D`$. Expanding at $`v`$ gives
```math
2D\,u\cdot(p-v)+|p-v|^2\le0.
```
Thus $`u\cdot p<u\cdot v`$ whenever $`p\ne v`$. In particular, $`v`$
is the unique maximizer of the linear functional $`u\cdot p`$, even on
$`\operatorname{conv}A`$. Similarly $`w`$ uniquely minimizes it.
Consequently every member of $`B`$ is an exposed vertex of $`F`$, and two
distinct diameter edges cannot have the same projective direction: that
direction has a unique ordered pair of support endpoints.

For a vertex $`v`$ of the polygon $`F`$, let $`I_v`$ denote its open arc
of unique supporting directions. This arc has length strictly less than
$`\pi`$. Every oriented diameter direction $`(v-w)/D`$ belongs to $`I_v`$.
Conversely, if a projective diameter direction lies in the projection of
$`I_v`$, orient it into $`I_v`$; its maximizing endpoint must then be $`v`$.
The projection is injective since $`|I_v|<\pi`$. Hence the incident edge
positions are exactly all diameter-direction positions in this one projective
arc. They form one cyclic interval. It is the whole order precisely when
every diameter edge has endpoint $`v`$, which is the star exception.

### Exact adjacency count

Assume the graph is not a star. A vertex of degree $`d_v`$ contributes exactly
$`d_v-1`$ shared consecutive pairs, since its incident positions form one
proper cyclic run. Two distinct simple-graph edges share at most one endpoint,
so these contributions do not overlap. Therefore
```math
N_{\rm sh}=\sum_{v\in B}(d_v-1)=2h-q,
\qquad
m_D=h-N_{\rm sh}=q-h=d_H.
```
This also proves $`t_v=1`$ and $`R_D=0`$ with the current report's conventions.

### Shared direction neighbors generate hull sides

Consider a consecutive shared pair $`vx,vy`$. Its two oriented directions
$`(v-x)/D,(v-y)/D`$ lie in $`I_v`$. They are consecutive along that proper
interval. The opposite directions uniquely support $`F`$ at $`x,y`$.

As a polygon's supporting direction rotates, its uniquely exposed vertices
occur in boundary order. If a vertex $`z\in B`$ occurred strictly between
$`x,y`$ on the corresponding boundary chain, its entire supporting arc
$`I_z`$ would lie strictly between those two support directions. But $`z`$
is a diameter endpoint; one of its diameter directions lies in $`I_z`$.
Its projective direction would lie strictly between the two consecutive
directions of $`vx,vy`$, a contradiction. Thus $`x,y`$ are consecutive
vertices of $`F`$.

There is at most one common diameter partner for a fixed pair $`x,y`$.
Indeed, the two possible intersections of the radius-$`D`$ circles centered
at $`x,y`$ are separated by
```math
2\sqrt{D^2-|x-y|^2/4}\ge\sqrt3D>D.
```
Both cannot belong to $`A`$. For a fixed common partner the two edges are
unique. The map from shared direction pairs to hull sides is therefore
injective. Since $`F`$ has exactly $`q`$ sides and there are exactly
$`2h-q`$ shared direction pairs, the complement has exactly $`2d_H`$ sides.

## Application and exact frontier effect

The canonical C-II source has $`B`$ equal to the loaded force-hull vertex
set. Section 66 excludes the star for sufficiently large survivors. The
theorem therefore applies to its actual full diameter graph, without changing
the source or discarding contact-isolated points.

This strengthens the recent re-entry bound to the exact identity $`R_D=0`$.
The putative obstruction
$`\sum_{v:t_v\ge2}\deg_H(v)`$ is identically zero. The earlier re-entry
report's inequalities remain valid; their suggested nonzero re-entry mechanism
is superseded by this stronger geometric statement.

It also proves an exact diameter-V cover with $`2d_H`$ missing hull sides.
At the rooted wrapping endpoint, the current unpromoted defect-stability
report gives $`d_H=o(D)`$, so only $`o(D)`$ sides are missing. Unlike the
previous cover, this conclusion does not need a near-unit free-end chord or
near-disk geometry. The near-unit lengths and width estimates in the earlier
endpoint cover remain additional endpoint conclusions, not hypotheses here.

This theorem does not bound the degree or total incidence of a small set of
ordinary, contiguous diameter stars. It does not eliminate the wrapping,
two-half-disk, or inactive-container branches.

## Hostile audit and dependencies

| Issue | Result |
| --- | --- |
| Projective wraparound | The normal arc projects injectively; cyclic intervals can cross the chosen cut. |
| Tied supports | The displayed squared-distance identity proves strict exposure. |
| Repeated/parallel diameter directions | Strict exposure excludes distinct parallel pairs. |
| High-degree star inside a non-star graph | Contiguity uses support intervals, independently of degree. |
| Whole graph is a star | Contiguity survives, but the proper-run count and side count are explicitly excluded. |
| Matching/caterpillar/odd cycle with leaves | The proof assumes none of these classifications. |
| Degenerate force hull | Excluded by the stated two-dimensional hypothesis. |
| Asymptotic incidence transfer | None is used: the re-entrant set is empty exactly. |

The theorem has an elementary analytic proof and no load-bearing computation
or external literature dependency. Its C-II application uses canonical
Section 60 for the loaded hull interpretation and Section 66 for asymptotic
star exclusion. The rooted endpoint interpretation is conditional on the
unpromoted report `target_c_wrapping_root_defect_stability_2026-09-30.md`.

## Exact next target

Couple the **contiguous** diameter-star side cover to actual harmonic trains.
A closing theorem must force a positive linear defect in the rooted ledger,
a unit triangle, or a same-cardinality strict sub-$`D`$ competitor. A count
of re-entrant stars cannot furnish that defect, because re-entry is absent
for every admissible diameter graph.

**Promotion disposition:** preserve as a proved candidate awaiting promotion;
the theorem-state manifest and canonical claims are unchanged.
