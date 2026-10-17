> Generated reading edition · [exact source](../../../docs/reports/target_c_unit_pentagon_perimeter_capacity_2026-10-05.md) · source SHA-256 `6ece09aac79da36dee38b049531de339ce8a2ec2e41e9dc773221be330d3c674`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C43C839B73BA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — universal convex unit-pentagon capacity and deletion deficit

**Date:** 2026-10-05. **Checkpoint:** 993c2991.
**State:** 2026-10-05.audit.54.
**Classification:** proved candidate awaiting independent audit; capacity
regression against individual-pentagon activation. Unreviewed and noncanonical.
**LEVEL I STATUS: STILL OPEN.**

## 1. Exact frontier effect and hypotheses

Let $`P`$ be a strictly convex pentagon with five sides of length one
and with mutually unit-separated vertices, as for an actual source wall.
Its closed container has a unique five-point unit-separated packing: its
five vertices. If $`d\ge1`$ wall vertices are deleted and the other
$`5-d`$ retained, at most $`d-1`$ unit-separated replacement points can
lie strictly inside $`P`$. With no deletion, even one interior point is
impossible. These are finite universal statements; they require no KKT
stress or global-minimizer assumption.

For a source-vertex-disjoint bank of $`a`$ activated pentagon walls, with
$`d_j\ge1`$ deletions at wall $`j`$, the exact capacity bound is
```math
\boxed{\sum_j M_j\le\sum_j d_j-a.}\tag{P5.1}
```
Consequently these interiors alone cannot fund the deleted labels. This
remains true after simultaneous contact-preserving motions, provided each
final wall is still a simple strictly convex unit pentagon and the final
packets satisfy their retained-wall separations. The statement strengthens
the regular-pentagon fixed-wall obstruction to every such pentagon and to
contact-preserving changes of its shape.

The implication is: pentagon perimeter rigidity $`\longrightarrow`$ at
least one uncompensated deletion per activated wall $`\longrightarrow`$
rejection of a replacement funded solely inside the individual pentagons.
It gives neither a new scalar term in the full-core inequality nor an
exclusion of replacements using a larger collective region.

## 2. Five-point perimeter lemma

**Lemma P5.2.** For every set $`X\subset\mathbb R^2`$ of five distinct
points at mutual distance at least one,
```math
\operatorname{per}(\operatorname{conv}X)\ge5.\tag{P5.2}
```
For a segment its perimeter is twice its length.

**Proof.** If the hull has five vertices, its five edges have length at
least one. If it is a segment, the five ordered points have span at least
four, giving perimeter at least eight.

If the hull is a triangle with perimeter $`p\le5`$, Heron's formula and
AM--GM give area at most $`p^2/(12\sqrt3)`$. The canonical finite
[Oler inequality, Lemma 21.1](../theory/03-oler-shell.md), applied to all
five points in this hull, then gives
```math
5\le\frac{p^2}{18}+\frac p2+1
\le\frac{25}{18}+\frac52+1=\frac{44}{9}<5,
```
a contradiction. This step includes points on triangle edges.

It remains to treat a quadrilateral hull with cyclic vertices
$`v_1,\ldots,v_4`$ and the fifth point $`z`$ in its closed hull.
The point $`z`$ differs from every vertex. Put $`r_i=|v_i-z|\ge1`$.
The consecutive polar gaps $`\theta_i`$ lie in $`[0,\pi]`$ and sum
to $`2\pi`$. For an interior point this follows from convexity and
winding number one. For a point in the relative interior of a hull edge,
one gap is $`\pi`$, and the other three traverse the opposite half
plane in order. Thus the same assertion holds on the boundary.

Writing $`c_i=\cos\theta_i`$, the exact identity
```math
|v_{i+1}-v_i|^2-2(1-c_i)
=(r_i-r_{i+1})^2+2(1-c_i)(r_ir_{i+1}-1)\ge0
```
shows that each edge has length at least
$`2\sin(\theta_i/2)`$, as well as at least one. For
$`0\le\theta\le\pi`$,
```math
\max\{1,2\sin(\theta/2)\}
\ge\frac12+\frac{3\theta}{2\pi}.\tag{P5.3}
```
For $`\theta\le\pi/3`$ the right side is at most one. On
$`[\pi/3,\pi]`$, concavity places $`2\sin(\theta/2)`$ above
the chord joining $`(\pi/3,1)`$ and $`(\pi,2)`$, which is the
displayed affine function. Summing the four edge estimates gives
$`p\ge4/2+3=5`$. These cases exhaust the hull possibilities. $`\square`$

## 3. Unique packing in any strictly convex unit pentagon

**Theorem P5.4.** If $`P=\operatorname{conv}\{v_1,\ldots,v_5\}`$
is strictly convex and $`|v_{i+1}-v_i|=1`$ cyclically, every
unit-separated five-point set $`B\subset P`$ equals
$`\{v_1,\ldots,v_5\}`$.

**Proof.** Suppose otherwise. Some extreme vertex $`v_i`$ is absent
from $`B`$; it cannot lie in the convex hull of the remaining points
of $`P`$. Since $`B`$ is finite, $`K=\operatorname{conv}B`$
is a compact proper convex subset of $`P`$. For completeness, convex
perimeter is strictly monotone under such inclusion: in a separating
support direction the support function of $`K`$ is strictly smaller,
and by continuity this persists on an open angular interval. The
opposite support is no larger. Thus the width is strictly smaller on
that interval and no larger elsewhere. Integrating widths in Cauchy's
perimeter formula, with the same formula for degenerate hulls, yields
$`\operatorname{per}K<\operatorname{per}P=5`$. Lemma P5.2 gives
the opposite inequality. $`\square`$

The theorem also implies that no six-point unit-separated set lies in
$`P`$, by considering two different five-point subsets. It does not
assume the five original vertices themselves are unit-separated; if
nonadjacent wall vertices violated separation there would simply be no
five-point packing. For actual source contact walls they are separated.

## 4. Deletion deficit and simultaneous source accounting

Under the mutually separated wall hypothesis of Section 1, retain any
$`5-d`$ original vertices, where $`1\le d\le5`$.
If a unit-separated interior packet, separated from all retained
vertices, contained $`d`$ points, choose $`d`$ of them. Together
with the retained vertices these would be five points in $`P`$
different from its vertex set, contradicting Theorem P5.4. Therefore
$`M\le d-1`$. For $`d=0`$, one admissible interior point together
with any four original vertices gives the same contradiction.

For $`a`$ walls with disjoint source vertex sets, total wall deletions
are exactly $`\sum_j d_j`$. The local bounds sum to (P5.1), even if
replacement labels are reassigned globally. Any old population needing
replacement or additional diameter-cover deletion only increases the
number of labels that must be funded. Cross-wall lower or upper
constraints cannot increase this local capacity bound. Each simple
strictly convex contact-preserving final pentagon still has perimeter
five, so the argument applies separately to every final container.

This is a cardinality obstruction, not deletion of source points from
a proposed competitor. It says that a competitor restricted to these
interiors fails to retain the original cardinality. Contact-isolated
points and external blockers have not been omitted from an alleged
feasibility proof: no feasible full-source competitor is claimed here.

## 5. Hostile checks, certificate, and remaining scope

- The four-hull-vertex case cannot be skipped. Equality at perimeter
  five occurs for the five points
  $`(0,0),(-1,0),(1,0),(1/2,\sqrt3/2),(-1/2,\sqrt3/2)`$.
  The script checks all ten lower pairs and the four hull-edge lengths.
  This example contains a unit triangle and is not a negative settlement.
- The triangle case has an exact Oler margin $`1/9`$; no equality
  classification or Rogalski--Saint Raymond uniqueness claim is used.
- The argument treats boundary points, collinear hulls, weak unit
  separation and every deletion size, including deletion of all vertices.
  It does not rely on positive force activation or contact minimality.
- Wall vertex disjointness is required to identify the sum of wall
  deletions with distinct source labels. The estimate is not claimed
  with repeated deletion charges or arbitrary overlapping walls.
- Final strict convexity and unit sides are actual hypotheses. Releasing
  wall lengths, changing the container topology, or moving points into a
  larger union falls outside the result.

Run
`python3 research/verify_target_c_unit_pentagon_capacity_2026_10_05.py`.
It verifies the exact polynomial distance identity, rational Oler margin,
support-line endpoints, and the boundary equality packet over
$`\mathbb Q(\sqrt3)`$. The infinite geometric proof is the argument
above; passing this small algebraic certificate does not independently
audit it or certify global optimality.

Audit.54's
[wall-disjoint pentagon bulk](target_c_pentagon_terminal_wall_disjoint_quadratic_bulk_2026-10-05.md)
can supply the physical wall bank under its stated hypotheses. Applying
the present theorem to that bank rejects individual convex-unit-pentagon
refills as the proposed deletion currency. A collective replacement must
use capacity outside these individual interiors or release their wall
constraints, while paying the actual diameter cover and preserving every
source separation. Full-core C-II and the macroscopic-container branch
remain open. Promotion requires independent audit; no canonical state
surface is changed by this report.
