> Generated reading edition · [exact source](../../../docs/reports/target_c_one_vacancy_collective_strictification_2026-10-05.md) · source SHA-256 `f0257acc588d5e3d2b437bf4df73d8ebda768c5d733d7489934feba475e54a69`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C32C5C6B486E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — one vacancy releases a complete oblique grid behind its fixed wall

**Date:** 2026-10-05. **Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f.
**Run checkpoint:** 70e7ba9e. **State:** 2026-09-14.audit.51.
**Classification:** proved candidate awaiting independent audit; capacity-gap
regression. Unreviewed and noncanonical. **LEVEL I STATUS: STILL OPEN.**

## 1. Exact purpose and source accounting

One actual interior vacancy permits a collective, same-cardinality motion
of an otherwise complete strict oblique unit grid which releases **every**
interior contact. No wall point moves. Every remaining source label stays
inside the original container, and every distance involving an interior
point becomes strictly greater than one.

The starting source already lacks the vacant point. Deleting a point from
a given Erdős source is not part of the theorem. No missing point is
silently counted in the final population.

Composing this construction with the
[fixed-wall lock candidate](target_c_large_near_triangular_fixed_wall_lock_2026-10-05.md)
gives arbitrarily large containers whose ordinary interior capacity is
exactly one larger than their strict interior capacity. Thus quadratic
contact-isolated population behind linear unit-wall complexity need not
have a strict spare slot. The containers are not certified global
minimum-diameter sources, and their pinned boundary is not certified
actual diameter loading. This does not eliminate the canonical
macroscopic-container branch.

## 2. Statement

Fix integers $`m,n\ge2`$, $`0<a<m`$, $`0<b<n`$, and
$`\pi/3<\phi<\pi/2`$. Put $`u=(1,0)`$,
$`v=(\cos\phi,\sin\phi)`$, $`p_{ij}=iu+jv`$, and
$`K=\{iu+jv:0\le i\le m,\ 0\le j\le n\}`$, where the real
coefficients in the last set describe the parallelogram container.
Let $`W`$ be all integer grid points with $`i\in\{0,m\}`$ or
$`j\in\{0,n\}`$, and start with the labelled source

```math
X^- =\{p_{ij}:i,j\text{ integer in these ranges}\}\setminus\{p_{ab}\}.
```

**Theorem V.1.** There is a piecewise linear continuous motion of $`X^-`$
which fixes $`W`$, retains every label, stays unit-separated throughout,
keeps every interior point strictly inside $`K`$, and ends with

```math
|p'_x-p'_y|>1\quad\text{whenever at least one of }x,y
\text{ is an interior label}.\tag{V.1}
```

Only horizontal and vertical grid steps are original contacts: for
positive integers $`r,s`$, $`|ru-sv|^2>r^2+s^2-rs\ge1`$;
the other nonbasis integer steps are immediate. All noncontacts are strict.

## 3. Stage one: release the row and column through the vacancy

Let $`J`$ be counterclockwise quarter-turn and $`A`$ the interior
labels in row $`j=b`$ or column $`i=a`$, excluding the vacancy.
Set all other velocities, including the wall, to zero. Set

```math
w_{i,b}=\begin{cases}-(i/a)Jv&i<a,\\
((m-i)/(m-a))Jv&i>a,\end{cases}\qquad
w_{a,j}=\begin{cases}(j/b)Ju&j<b,\\
-((n-j)/(n-b))Ju&j>b.\end{cases}\tag{V.2}
```

On each horizontal contact along the vacant row, including its fixed-wall
end, the $`Jv`$ coefficient strictly decreases as $`i`$ increases.
Since $`u\cdot Jv=-\sin\phi`$, its squared length has strictly
positive derivative under $`p\mapsto p+r w`$. Each vertical contact
along the vacant column has strictly increasing $`Ju`$ coefficient
and $`v\cdot Ju=\sin\phi`$, hence positive derivative as well.

Every other original contact touching $`A`$ has nonzero relative
velocity perpendicular to its edge. Its squared length is
$`1+r^2|\Delta w|^2>1`$ for $`r>0`$. There is no unit edge
connecting the vacant row to the vacant column except through the absent
point. Original contacts disjoint from $`A`$ remain fixed.

All original noncontacts have positive slack, and every interior point
starts strictly inside $`K`$. There are finitely many such conditions.
A sufficiently small $`r>0`$ preserves them on the **whole** segment
$`0\le r'\le r`$, and releases every contact touching $`A`$.

## 4. Stage two: expand the four remaining blocks in the dual basis

The stationary interior labels outside $`A`$ occupy four possibly
empty blocks. Each touches two adjacent outer sides. Every contact
between distinct blocks would cross $`A`$, so has already been
released or was never a contact. Use the dual vectors

```math
u^*=(1,-\cos\phi/\sin\phi),\quad v^*=(0,1/\sin\phi),
```

with $`u\cdot u^*=v\cdot v^*=1`$ and both crossed products zero.
For each remaining interior label define

```math
(I,s_x)=\begin{cases}(i,+1)&i<a,\\(m-i,-1)&i>a,\end{cases}
\quad (J_0,s_y)=\begin{cases}(j,+1)&j<b,\\(n-j,-1)&j>b,\end{cases}
```

and give it velocity $`z_{ij}=s_x Iu^*+s_y J_0v^*`$.
Freeze $`A`$ at its first-stage positions and keep the wall fixed.
Within a block every remaining horizontal contact has
$`u\cdot\Delta z=1`$, and every vertical contact has
$`v\cdot\Delta z=1`$. For a unit edge to either adjacent fixed
outer wall, its outward displacement has the same positive radial
component. Every unreleased interior contact therefore has positive
squared-length derivative. This dual-basis calculation also handles
obtuse corners; Euclidean homothety about a corner would not suffice.

After fixing $`r>0`$, choose a sufficiently small second amplitude
$`s>0`$. Finiteness and strict slack preserve all previously released
pairs, all original noncontacts, and strict interior containment on
$`0\le s'\le s`$. The remaining contacts strictly lengthen for
every $`s'>0`$. All conditions (V.1) hold at the endpoint. Cardinality
is exactly $`(m+1)(n+1)-1`$ at every time. This proves V.1.

Both amplitudes may depend on the complete finite source and its slacks.
No uniform radius in $`m,n`$, strict diameter improvement, or actual
diameter feasibility beyond containment is asserted.

## 5. Ordinary capacity and strict capacity differ by exactly one

Put $`K_0=(m-1)(n-1)`$. Ordinary interior capacity with wall $`W`$
is the largest number of added interior points satisfying all distances
$`\ge1`$; strict capacity requires all distances involving an added
point to be $`>1`$.

For each fixed $`m,n\ge3`$, choose a positive angle excess in the
fixed-wall lock window of Theorem L.2, small enough also that

```math
mn\left(\frac{\sin\phi}{\sqrt3/2}-1\right)<1.
```

Oler's integer bound prohibits $`(m+1)(n+1)+1`$ points in the container.
The full grid attains $`(m+1)(n+1)`$, so ordinary interior capacity is
$`K_0`$. Fixed-wall uniqueness says any full packing is that grid,
which has interior contacts. Strict capacity is at most $`K_0-1`$,
and V.1 supplies a strict packing of exactly $`K_0-1`$. Hence

```math
\boxed{\operatorname{cap}_{\ge1}(K;W)=K_0,
\qquad\operatorname{cap}_{>1}(K;W)=K_0-1.}\tag{V.4}
```

Taking $`m=n\to\infty`$ gives $`\Theta(D^2)`$ contact-isolated
interior points behind $`O(D)`$ unit-wall vertices, without a strict
one-point refill. This angle window is not effective or uniform. The
wall has pinned vertices which do not meet the canonical minimum-diameter
contact-minimal normalization. Thus V.4 is a capacity regression, not a
counterexample to canonical §162 or the Level I quantifiers.

## 6. Exact certificate and audit scope

```bash
python3 research/verify_target_c_one_vacancy_collective_strictification_2026_10_05.py
```

The certificate uses $`\mathbb Q(\sqrt3)`$ coordinates with rational
half-angle parameter $`t=1/[100mn(m+n)]`$. Four patches check all
1,915 distinct source pairs and 46 remaining interior points, exact
wall fixation, unchanged labels and strict container inequalities.
Rational halving selects both amplitudes with exact comparisons.

The analytic proof supplies termination. Endpoint checks supplement that
proof; they alone would not certify every time along a segment. Explicit
test angles are not claimed inside the nonexplicit uniqueness window of
V.4. No certificate asserts global diameter optimality or Level I closure.

To spend V.1 in an actual source replacement, one must obtain a vacancy
without losing a source point, retain the actual external interface and
all upper constraints, and gain a strict spare slot or a same-cardinality
strict sub-$`D`$ competitor. Ordinary saturation does not supply this.
