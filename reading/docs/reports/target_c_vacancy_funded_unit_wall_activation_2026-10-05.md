> Generated reading edition · [exact source](../../../docs/reports/target_c_vacancy_funded_unit_wall_activation_2026-10-05.md) · source SHA-256 `372a10ce01e1aa8c5a70b39c215b070164eaf851383739d0d0129acd0b1d753b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E101C71471F3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — vacancy-funded contact loss behind actual unit walls

**Date:** 2026-10-05. **Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f.
**Run checkpoint:** 0526296a. **State:** 2026-09-14.audit.51.
**Classification:** proved source-replacement candidate awaiting independent audit.
Unreviewed and noncanonical. **LEVEL I STATUS: STILL OPEN.**

## 1. Exact frontier change

The [one-vacancy motion](target_c_one_vacancy_collective_strictification_2026-10-05.md)
can be spent through contact minimality, with an actual unit wall shielding
every exterior source point. A second construction works at the triangular
limit and gives a replacement margin for sufficiently close, potentially
nonconvex, unit-wall cycles.

The source implications proved below are:

- Every exact strict-oblique rectangular grid wall in a canonical C-II
  source encloses at least the full rectangular interior count.
- For a fixed rectangular triangular reference wall, a sufficiently close
  actual unit cycle cannot enclose a population deficient by three slots.
- At deficiency two in the latter setting, all enclosed source points must
  be contact-isolated.

These are finite activation criteria, not near-unit-to-force assertions.
They retain every source label and invoke actual global optimality and
contact minimality. No current train theorem is asserted to furnish the
required complete enclosing wall or its population deficit. Neither the
general full-core branch nor the macroscopic-container branch is closed.

## 2. A unit edge shields a crossing pair

**Lemma W.1.** Suppose $`|a-b|=1`$, all four distances from
$`x,y`$ to $`a,b`$ are at least one, and segments $`[a,b]`$ and
$`[x,y]`$ cross. Then $`|x-y|\ge\sqrt3`$.

For a proper crossing, the vertices form the convex quadrilateral in
order $`a,x,b,y`$. If $`r=|x-a|,s=|x-b|\ge1`$, then

```math
\cos\angle axb=\frac{r^2+s^2-1}{2rs}\ge\frac12,
```

because $`(r-s)^2+rs\ge1`$. Thus each of the angles at $`x,y`$
is at most $`\pi/3`$. The angles at $`a,b`$ sum to at least
$`4\pi/3`$, so one is at least $`2\pi/3`$. Its adjacent side
lengths are at least one, and the cosine law gives $`|x-y|^2\ge3`$.
Degenerate crossings follow by continuity; if the segments meet at an
endpoint of $`[a,b]`$ lying between $`x,y`$, the simpler lower
bound is $`|x-y|\ge2`$. Collinear overlap also has an endpoint
between $`x,y`$, since neither $`x`$ nor $`y`$ can lie in the
interior of the unit segment.

Consequently, if an actual simple unit-contact cycle $`W`$ bounds a
region $`C_W`$, an interior point strictly separated from all its
vertices is farther than one from every old exterior source point.
The joining segment crosses a unit edge and W.1 applies. Source points
on the wall are precisely its vertices: an additional point on a unit
side would be less than one from an endpoint.

Opposite half-planes without a crossing do not suffice. The certificate
checks the counterexample $`a=(0,0),b=(1,0)`$,
$`x=(2,1/100),y=(2,-1/100)`$, where all endpoint distances exceed
one but $`|x-y|=1/50`$.

## 3. The funded replacement theorem

Let $`A`$ be a triangle-free global minimizer, selected with minimum
unit-contact count among the triangle-free global minimizers of its
cardinality. Let $`W\subset A`$ be a simple unit cycle, let
$`Z=A\cap\operatorname{int}(C_W)`$, and suppose an interior set
$`Y_*`$ of $`M`$ points has all mutual and wall-vertex distances
strictly greater than one.

**Theorem W.2.**

1. If $`|Z|\le M`$, no point of $`Z`$ is incident to an actual
   unit contact of $`A`$.
2. Necessarily $`|Z|\ge M`$.

For (1), replace all $`Z`$ by a subset of $`Y_*`$ of the same
cardinality. Lemma W.1 gives strict separation from every retained
exterior point. All inserted points are in
$`\operatorname{int}\operatorname{conv}W\subset
\operatorname{int}\operatorname{conv}A`$, so every pair involving
an inserted point has distance strictly less than the old diameter.
Old retained pairs are unchanged. Global optimality forces the resulting
diameter to equal $`D(n)`$, and the new source is triangle-free because
inserted points have no unit contacts. If $`Z`$ had any contact, its
deletion lowers the total contact count, contradicting selection.

For (2), if $`|Z|\le M-1`$, choose any $`w\in W`$, delete
$`Z\cup\{w\}`$, and insert $`|Z|+1`$ points of $`Y_*`$.
Every old wall vertex had two cycle contacts, so at least one old contact
is lost. There are no new contacts. Cardinality remains exactly $`|A|`$,
giving the same contradiction.

**Deleted wall vertices remain geometric references only.** In the proof
of exterior separation, an old unit wall segment may have the deleted
$`w`$ as an endpoint. Every retained old exterior point was separated
from that old coordinate by at least one, and every inserted point is
strictly separated from it by construction. W.1 therefore still applies.
The deleted point is not counted in the final source, assigned a new
diameter load, or falsely retained as an actual constraint. Its old
coordinate certifies a lower-distance inequality between two actual
retained/inserted points. The removed label can be assigned to the one
extra inserted point, preserving the complete label set.

This comparison is between finite configurations. No feasible continuous
path from the old source to the replacement is needed or claimed.
All exterior isolates remain fixed and are checked by the same shielding
argument as every other exterior point.

## 4. Exact oblique grid walls force the full population

Fix $`m,n\ge2`$, $`\pi/3<\phi<\pi/2`$, $`u=(1,0)`$,
$`v=(\cos\phi,\sin\phi)`$, and let $`W`$ consist of the complete
integer boundary of $`\{iu+jv:0\le i\le m,0\le j\le n\}`$.
Put $`K_0=(m-1)(n-1)`$. V.1 supplies $`M=K_0-1`$ strict
interior points. For $`K_0=1`$, this is the empty set.

**Theorem W.3.** If $`W`$ is coembedded in a canonical triangle-free
C-II source, then its enclosed population satisfies $`|Z|\ge K_0`$.
Every source point inside the wall, including every isolate, is counted.

By W.2, $`|Z|\ge K_0-1`$, with equality possible only if all
enclosed points are contact-isolated. We rule out that equality using
actual positive equilibrium.

Take the flat bottom-side vertex $`p=u`$, lying strictly between
the two side endpoints. Its two wall contacts have directions $`\pm u`$.
It is a core point, but cannot be an extreme point of the full force
hull because it lies between other core points. Canonical Section 67
therefore makes it unloaded, with positive contact degree at least three.
Positive equilibrium forces some contact direction to have positive
component into the upper half-plane: otherwise all positive contact
vectors lie in the exterior closed half-plane, equilibrium forces every
one onto its boundary line, and there are at most two unit neighbors.

An inward unit neighbor cannot be exterior to the parallelogram: the
unit joining segment would leave through another, nonincident wall side,
contradicting W.1's $`\sqrt3`$ crossing lower bound. Nor is it another
wall vertex. The exact contacts between distinct grid-wall vertices are
basis steps, and all wall neighbors of this flat vertex are tangent;
the inward basis neighbor $`u+v`$ is strictly interior. Thus there
is an actual contact incident to an enclosed point. W.2 excludes
$`|Z|\le K_0-1`$, proving W.3.

**Corollary W.4.** For each fixed $`m,n`$, in the independently
unpromoted fixed-wall uniqueness window L.2, choose the angle excess
small enough also that the Oler residual is less than one. Any canonical
source containing this exact wall has precisely $`K_0`$ interior
points, and they are the full oblique grid. No exceptional contact face,
extra isolate or vacancy can be enclosed by this frame.

The extra uniqueness dependency is needed only for W.4. W.3 uses V.1
and canonical positive equilibrium, without an angle-window assumption.
No theorem in this report produces a complete grid wall from arbitrary
local rhombic pieces.

## 5. Two triangular vacancies give a robust strict capacity

Now fix $`m,n\ge3`$, $`u=(1,0)`$,
$`v_0=(1/2,\sqrt3/2)`$, and keep the triangular grid wall $`W_0`$
fixed. Omit the two interior labels $`(1,1),(2,1)`$.

**Lemma W.5.** All $`K_0-2`$ remaining interior points can be moved
to strictly separated positions inside this fixed wall, with every
remaining label retained and every lower constraint preserved throughout.

The six contact directions have successive angular gaps $`\pi/3`$.
If two adjacent direction neighbors have already been omitted or released,
the remaining contact rays occupy a closed semicircle. Move the point in
the sum of the two missing unit directions. Its dot product with every
remaining contact ray is nonpositive. Negative products strictly lengthen
contacts linearly; zero products strictly lengthen them quadratically.
All pairs to previously released points have strict slack. A sufficiently
small positive move therefore releases the point, stays strictly inside
the container, and preserves every lower constraint along its full segment.
Freeze it at the new position and proceed.

The following order releases every remaining interior point:

1. For $`j=2,\ldots,n-1`$, release $`(1,j)`$, using missing
   $`(1,j-1),(2,j-1)`$; then release $`(2,j)`$, using missing
   $`(1,j),(2,j-1)`$.
2. For $`i=3,\ldots,m-1`$, first release $`(i,1)`$, using missing
   $`(i-1,1),(i-1,2)`$; then for $`j=2,\ldots,n-1`$, release
   $`(i,j)`$, using missing $`(i-1,j),(i,j-1)`$.

Each named pair is adjacent in the six-direction cycle and was already
released or initially vacant. The order covers every interior label
exactly once. All interior contacts have disappeared at its end. This
proves W.5 without a numerical extrapolation. The restrictions $`m,n\ge3`$
ensure the two initial vacancies and the second-row propagation exist;
thin width-two walls are not covered.

Nor may two vacancies be silently replaced by one at the triangular limit.
The certificate checks the $`3`$-by-$`3`$ wall with only $`(1,1)`$
vacant. Its three remaining interior labels have a positive pinned stress
on all thirteen contacts touching them. Each interior label has two
independent contact directions to fixed wall vertices. Positive equilibrium
makes every weak fixed-wall strut velocity a bar flex, and those wall rows
force the flex to zero. The packet is locally jammed. This does not claim
that every distant alternative refill is impossible; it certifies failure
of a uniform one-vacancy sequential-release assertion at the limit.

## 6. A positive margin for nearby actual unit cycles

Fix the strict endpoint set $`Y_*`$ of W.5. It has a positive minimum
mutual/wall distance excess and positive distance to the polygonal wall.
Choose $`\eta_{m,n}>0`$ smaller than one third of the latter distance
and one third of its wall-distance excess.

Let an actual simple unit cycle have vertices in the same order as $`W_0`$,
each within $`\eta_{m,n}`$ of its reference vertex after one Euclidean
isometry. Every $`Y_*`$ point is still strictly separated from every
wall vertex. Interpolate the two closed polygonal curves linearly at their
vertices. Every interpolated edge stays within $`\eta_{m,n}`$ of its
reference edge, so none passes through $`Y_*`$. The winding number about
each point is unchanged and equals one. Thus $`Y_*`$ stays strictly
inside the actual cycle, even if the actual cycle is nonconvex.

Apply W.2 with $`M=K_0-2`$:

```math
\boxed{|A\cap\operatorname{int}(C_W)|\ge K_0-2,}
\tag{W.6}
```

and equality implies every enclosed point is contact-isolated.
In particular, a triangle-free contact-minimal global minimizer cannot
have this actual near-triangular unit wall enclosing $`K_0-3`$ or fewer
source points. The reference triangular wall is allowed to contain unit
triangles; it is an auxiliary packing for constructing strict interior
positions. The actual source wall is triangle-free by the source
hypothesis, and the replacement creates no contacts or triangles.

**Order of limits.** Fix $`m,n\ge3`$ first. The positive wall tolerance
depends only on this finite reference packet. Any asymptotic sequence
of canonical sources containing these actual cycles with vertex errors
tending to zero and populations at most $`K_0-3`$ is excluded eventually.
No tolerance uniform in frame size or growing-frame conclusion is asserted.

## 7. Exact certificate and remaining gap

```bash
python3 research/verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05.py
```

The script verifies the triangular release order and exact full-pair
lower constraints in four finite packets. Six complete oblique source
replacements include exterior guards, delete a wall vertex, retain all
labels, strictly separate the new interior population from every old
wall coordinate, remove contacts and preserve the full maximum diameter.
Every new/exterior-guard distance is at least $`\sqrt3`$. A shield
equality and a noncrossing failure are checked exactly.

The one-vacancy triangular regression additionally checks every positive
equilibrium coefficient and the independent pinned directions. It retains
the essential two-vacancy hypothesis of the robust construction.

Arithmetic is in $`\mathbb Q(\sqrt3)`$. The finite guarded packets
are not asserted globally diameter-optimal. Global optimality enters the
analytic W.2 contradiction, not a numerical optimality certificate.
Sequential feasible amplitudes can decay rapidly; neither this computation
nor the proof supplies a uniform motion radius in growing patch size.

The closing obligation remains to force, in every surviving source branch,
an **actual complete enclosing unit wall** with the stated integer
population deficit, or to enlarge this capacity theorem to the actual
interfaces forced by the train/phase frontier. Near-unit pairs, many
separate rhombi and disjoint returns do not supply those hypotheses.
