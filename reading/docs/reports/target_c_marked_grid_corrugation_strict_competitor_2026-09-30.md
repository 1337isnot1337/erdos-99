> Generated reading edition · [exact source](../../../docs/reports/target_c_marked_grid_corrugation_strict_competitor_2026-09-30.md) · source SHA-256 `4db56598509faa870298e6282a32135af749869d84f0784e50e4bf0153ed2897`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-FB44E1E56FF6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_marked_grid_corrugation_strict_competitor_2026-09-30.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=0a29f72004a28fc95314deb5d18eeb4deb12111f; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C: marked-grid corrugation gives a strict full-source competitor

**Date:** 2026-09-30

**Base main:** `c00bb08090cf3a7a89fc195cbe3ab450983a5de0`

**State version:** `2026-09-14.audit.51`

**Classification:** proved candidate awaiting promotion; finite analytic proof.

**Level I:** open. C-II remains open.

## 1. Exact obligation and source hypotheses

The implication in this report is

> one actual additive unit-grid chart with fewer than $`D`$ unmatched bars
> $`\longrightarrow`$ shorten every actual diameter pair while preserving
> every actual unit contact $`\longrightarrow`$ strict same-cardinality
> sub-$`D`$ competitor for the full source.

Let $`A\subset\mathbb R^2`$ be a finite unit-separated source, with
$`|A|\ge2`$ and diameter $`D`$. Write $`B_H`$ for all endpoints of
its actual diameter pairs. Assume that a subset $`W\subseteq A`$ has
the following properties.

1. $`B_H\subseteq W`$.
2. Each point of $`W`$ has distinct integer coordinates $`(i,j)`$, and
   its actual position is
   
   ```math
   p_{ij}=p_0+X_i+Y_j.
   \tag{1.1}
   ```

   The sequences are defined on integer intervals containing all coordinates
   used by $`W`$, and every increment
   $`a_i=X_{i+1}-X_i`$, $`b_j=Y_{j+1}-Y_j`$ has length one.
3. Every actual unit contact incident with $`W`$ joins two points of
   $`W`$ whose indices differ by $`(\pm1,0)`$ or $`(0,\pm1)`$.
   Contacts wholly in $`A\setminus W`$ may be arbitrary.

Hypothesis 2 is a global chart of actual source positions. Independently
charted harmonic cells, a response grid, or a scaffold do not satisfy it.
Virtual grid positions and bars between unoccupied indices are only a way
to describe the motion; no new source points are inserted.

Let $`i_1<\cdots<i_r`$ be the distinct first coordinates occurring in
$`B_H`$, and $`j_1<\cdots<j_s`$ the distinct second coordinates.
Define the integer
```math
U=\sum_{k=1}^{r-1}\mathbf1_{i_{k+1}-i_k\text{ odd}}
 +\sum_{k=1}^{s-1}\mathbf1_{j_{k+1}-j_k\text{ odd}}.
\tag{1.2}
```
An empty sum is zero.

**Theorem.** If $`U<D`$, then there is a continuous motion of the
full source, fixing $`A\setminus W`$, which preserves every original
unit contact exactly and yields a unit-separated source of the same
cardinality with diameter strictly less than $`D`$.

In particular such an $`A`$ is not a global minimum-diameter source.
The theorem is exact and finite. It does not assume global optimality,
contact-minimality, stresses, positive area, or a quantitative contact slack.

## 2. A pair of unit bars can shorten its sum exactly

For unit vectors $`a,b`$ and $`\lambda<1`$ sufficiently close to one,
there are unit vectors $`a(\lambda),b(\lambda)`$, continuous at one,
such that
```math
a(\lambda)+b(\lambda)=\lambda(a+b),
\qquad a(1)=a,\quad b(1)=b.
\tag{2.1}
```

If $`a+b=0`$, leave both vectors fixed. Otherwise set
$`c=|a+b|/2\in(0,1]`$, let $`m=(a+b)/|a+b|`$, and choose the
unit perpendicular $`n`$ so that
```math
a=cm+\sqrt{1-c^2}\,n,\qquad b=cm-\sqrt{1-c^2}\,n.
```
When $`c=1`$, either perpendicular can be used. Put
```math
a(\lambda)=\lambda cm+\sqrt{1-\lambda^2c^2}\,n,
\qquad
b(\lambda)=\lambda cm-\sqrt{1-\lambda^2c^2}\,n.
\tag{2.2}
```
These are unit vectors and satisfy (2.1). This also covers parallel bars;
the motion then has size proportional to $`\sqrt{1-\lambda}`$.
For each moved bar,
```math
|a(\lambda)-a|,\ |b(\lambda)-b|
 \le\sqrt{2(1-\lambda)}.
\tag{2.3}
```
Indeed its scalar product with its original value is at least
$`\lambda c^2+(1-c^2)\ge\lambda`$. Thus this is an actual
finite motion, including at the parallel degeneracy, rather than an
infinitesimal flex requiring an integration theorem.

## 3. Pair bars separately between successive marks

Inside each interval $`[i_k,i_{k+1})`$, partition the $`a`$-bars into
consecutive pairs. If the interval has odd length, leave its last bar
unchanged. Apply (2.2), with the same $`\lambda`$, to every pair.
Leave bars outside the marked range unchanged. Do the same independently
for the $`b`$-bars between successive $`j`$-marks. There are exactly
$`U`$ unmatched bars in the two marked ranges together.

Anchor $`X_{i_1}(\lambda)=X_{i_1}`$ and
$`Y_{j_1}(\lambda)=Y_{j_1}`$, and reconstruct both sequences by
summing the new increments in either direction. Move each actual point
of $`W`$ using (1.1), and fix all points outside $`W`$.

Every original unit contact is preserved. For a contact within $`W`$,
the new difference is one new unit increment by hypothesis 3. All other
contacts join fixed points. Holes or omitted grid vertices cause no
problem, because the bar sequences, not the set of virtual points, define
the motion.

For two marked first coordinates, the sum of all complete pairs between
them is multiplied by $`\lambda`$, and each unmatched bar is fixed.
The same holds for marked second coordinates. Consequently every original
diameter vector $`d_e`$ satisfies the exact identity
```math
d_e(\lambda)=\lambda d_e+(1-\lambda)E_e,
\qquad |E_e|\le U,
\tag{3.1}
```
where $`E_e`$ is the signed sum of the unmatched original bars between
its endpoint coordinates. Bars are counted once; reversed index order
only changes the sign. Hence
```math
|d_e(\lambda)|\le\lambda D+(1-\lambda)U
 =D-(1-\lambda)(D-U)<D.
\tag{3.2}
```
This simultaneously treats every active diameter constraint.

## 4. Full-source feasibility and the finite parameter

Every pair that was not a unit contact initially has distance strictly
greater than one. Every pair that was not a diameter pair initially has
distance strictly less than $`D`$. There are finitely many pairs, and
the constructed positions are continuous at $`\lambda=1`$.
Therefore for some $`\lambda<1`$ close enough to one all these strict
inequalities persist. Together with contact preservation and (3.2),
this proves the theorem.

The parameter can be bounded using the source's actual finite slacks.
Let $`\gamma`$ be the minimum of all the positive quantities
$`|p-q|-1`$ for original noncontacts and $`D-|p-q|`$ for original
nondiameter pairs, ignoring empty collections. Let
```math
T=\max_{(i,j)\in W}(|i-i_1|+|j-j_1|).
```
By (2.3), each source displacement is at most
$`T\sqrt{2(1-\lambda)}`$. If $`\gamma`$ is finite, choosing
```math
0<1-\lambda<\min\{1/2,\gamma^2/(32T^2)\}
\tag{4.1}
```
suffices for the nonactive constraints. If the collection defining
$`\gamma`$ is empty, any sufficiently small positive choice works.
In a nonempty theorem instance $`T>0`$, since the loaded set has at
least two distinct source points. No lower bound on $`\gamma`$ uniform
over sources is needed.

This fixes a common asymptotic pitfall: an arbitrarily tiny angular or
noncontact slack is enough for a finite improvement of the original
source. The improvement itself may be arbitrarily tiny.

## 5. Consequences and limitations

Writing $`q=|B_H|`$, $`h`$ for the number of actual diameter pairs,
```math
U\le(r-1)+(s-1)\le2q-2\le4h-2.
\tag{5.1}
```
Thus any such globally charted source with $`h=o(D)`$ along a sequence
is eventually excluded. More strongly, if all loaded coordinates have
the same parity on each axis, then $`U=0`$, and the deformation works
at every diameter for which the source hypotheses hold.

Contact-isolated points outside $`W`$ are retained and may stay fixed,
provided they are not diameter endpoints. Arbitrarily many such points
do not change the argument; their finite positive slacks enter (4.1).
Loaded isolates must belong to $`W`$. A contact interface crossing from
the chart to fixed points is excluded by hypothesis 3.

**Exact next target:** prove $`U<D`$ for an exact oblique-lattice source,
then determine whether a canonical C-II survivor admits this motion or a
compatible modification across its actual train interfaces. A local
rhombus grid or one quadratic harmonic carrier alone is not a global
chart and does not prove this extension.

## 6. Dependencies, audit, and computation

The analytic proof uses only finite Euclidean geometry and continuity.
No earlier candidate theorem is a premise. The exact example audit is
`research/verify_marked_grid_corrugation.py`; its finite examples do not
prove the general theorem or certify global optimality.

Hostile checks incorporated above: unoccupied indices; parallel and
antiparallel bar pairs; odd marked gaps; reversed endpoint coordinates;
fixed contact-isolated points; all actual diameter pairs; arbitrary tiny
positive slack; and explicit integration of the finite motion.

The result remains noncanonical pending independent audit and promotion.
