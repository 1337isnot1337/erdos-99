> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_exterior_train_far_arc_2026-10-01.md) · source SHA-256 `4f78741af6c566e30c811a5ccab24f948f61f195d66f994614842189d3f6990b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2E2C42DD84DA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: a finite exterior-train rotation passes all old diameter constraints

**Phase 2 preservation provenance:** PR #597, branch swarm/root/c2-gap-reaction-20261001, audited source head c89adbcd2e008e1d01141fa38ff54b1bcae85678. Preserve as conditional exact-chart exterior-train geometry; its finite blockers do not establish a global release.

Date: 2026-10-01.
Starting checkout: 7b3fd8e2ad15532c0d40b761da381ac7d5c36074.
Fetched research base: 14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79.
Parent checkpoint: 9953b400.
State version: 2026-09-14.audit.51.
Branch: swarm/root/c2-gap-reaction-20261001.
Mission: integrate a full-system exact-phase release beyond the local angular barrier.
Classification: proved candidate awaiting promotion; source application conditional.
Level I OPEN; C-I CLOSED; C-II OPEN.

Implication chain:

finite exterior-train rotation satisfying every old active diameter constraint
-> actual inactive source-pair obstruction, or a same-contact source with fewer diameters
-> target: exclude the inactive obstruction using actual contact co-embedding
-> contradiction in the normalized C-II source.

The inactive obstruction is not excluded here. Other C-II branches remain open.

## 1. Inputs and precise scope

This report assumes the explicit geometric hypotheses of
[the star-ray staircase packet](target_c_star_ray_staircase_reactions_2026-10-01.md),
and reuses its proved paired staircase and representative angle order.
That packet is unpromoted. Its October 1 common-star, nested-cut and rank
extraction dependencies remain unpromoted as well.

For application to the actual lexicographically normalized source, the canonical
normal form and mixed rigidity are
[Section 56](../targets/target-c/56-ci-restored-frontier.md) and
[Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md).
The actual finite global-cut chart is an additional source hypothesis. No
contact-isolated source point is removed or assigned to the contact core.

The independent hostile audit [PR #602](https://github.com/1337isnot1337/e-99/pull/602)
checks the initial staircase and angle order at checkpoint 87375fe0, not the new
finite arguments below. The concurrent [PR #599](https://github.com/1337isnot1337/e-99/pull/599)
rules out a finite deformation remaining inside the witness directions. Its
proof was checked; it is not a premise of this report. The move below generally
passes outside those directions and never asserts feasibility along an
intermediate path.

Let the nested intervals be

```math
I_1=(0,m],\ I_2,\ldots,I_m,
\qquad |I_t|=m-t+1.
```

Each successive interval deletes one exterior coordinate. Let
$`j_0\in\{1,m\}`$ be the coordinate deleted from $`I_1`$ to form $`I_2`$.
It belongs to no proper-support diameter. Assume $`m\ge2`$ and $`D\ge9`$.

For each actual nonparallel full-span diameter, orient its vector $`n_h`$
from layer 0 to layer $`m`$. Its transverse sign is nonzero. Write the
positive-sign vectors as $`D(\cos\alpha_h,\sin\alpha_h)`$, and the negatives
as $`-D(\cos\gamma_h,\sin\gamma_h)`$, in coordinates $`u=(1,0)`$.
All $`\alpha_h,\gamma_h`$ lie in $`(0,\pi)`$. Put

```math
\alpha_*=\max_h\alpha_h,\qquad
\gamma_*=\min_h\gamma_h.
```

Every original diameter row is retained in these extrema, not merely a basis.
The strict staircase order gives $`\alpha_*<\gamma_*`$.

## 2. Exact allowed phases for one exterior train

Rotate train $`j_0`$ alone to $`w=(\cos\theta,\sin\theta)`$, with
$`0<\theta<2\pi`$, and apply the exact cut translation $`w-u`$.
Every proper-support or empty-support diameter is unchanged. Every full-span
diameter has new vector $`n_h+w-u`$.

Since $`|n_h|=D`$ and $`|w|=|u|=1`$, its squared change is exactly

```math
|n_h+w-u|^2-D^2
=2(n_h-u)\cdot(w-u).                                  \tag{1}
```

Define the upper-half-plane arguments

```math
f_+(\alpha)=\arg(De^{i\alpha}-1),\qquad
f_-(\gamma)=\arg(De^{i\gamma}+1).
```

Both are in $`(0,\pi)`$ and strictly increasing. Their derivatives are

```math
f_+'(\alpha)=\frac{D(D-\cos\alpha)}
                  {D^2-2D\cos\alpha+1}>0,\qquad
f_-'(\gamma)=\frac{D(D+\cos\gamma)}
                  {D^2+2D\cos\gamma+1}>0.              \tag{2}
```

For a positive-sign row, (1) is nonpositive exactly when
$`\theta\ge2f_+(\alpha_h)`$. For a negative-sign row it is nonpositive
exactly when $`\theta\le2f_-(\gamma_h)`$. This follows by factoring out
the positive $`2\sin(\theta/2)`$; there is one nonzero phase root.
Consequently the complete nonzero allowed phase set is the closed arc

```math
\boxed{\mathcal F=
[\,2f_+(\alpha_*),\,2f_-(\gamma_*)\,].}                 \tag{3}
```

An empty interval means no allowed nonzero phase. A singleton is allowed but
has no strict interior. A possible parallel full-span diameter has vector
$`Du`$, whose squared change is
$`2(D-1)(\cos\theta-1)<0`$; it imposes no extra restriction on (3).

For any $`\theta`$ in the strict interior of (3), **every** original
full-span diameter strictly shortens. All other actual diameter pairs remain
at their old length. This is a finite endpoint calculation.

## 3. The arc has strict interior when at least two trains are retained

Let $`\Delta=\gamma_*-\alpha_*`$ and
$`\mu=(\alpha_*+\gamma_*)/2`$. The determinant of the two transformed
upper-half-plane vectors is

```math
\begin{split}
\det(De^{i\alpha_*}-u,\ De^{i\gamma_*}+u)
&=D^2\sin\Delta-D(\sin\alpha_*+\sin\gamma_*)\\
&=2D\cos(\Delta/2)
       [D\sin(\Delta/2)-\sin\mu].
\end{split}                                           \tag{4}
```

Thus (3) has strict interior exactly when

```math
D\sin(\Delta/2)>\sin\mu.                               \tag{5}
```

This is a test on actual extremal diameter vectors, independent of KKT weights.

Choose one representative from each remaining orientation class. The strict
order from the staircase report gives

```math
\alpha_*<\alpha_2<\cdots<\alpha_m
<\gamma_m<\cdots<\gamma_2<\gamma_*.
```

Distinct diameter directions have projective separation at least
$`\delta_D=2\arcsin(1/(2D))`$. Each displayed ordinary increment is at
least that amount, hence

```math
\Delta\ge(2m-1)\delta_D\ge3\delta_D.
```

Because $`0<\Delta<\pi`$,

```math
D\sin(\Delta/2)
\ge D\sin(3\delta_D/2)
=\frac32-\frac1{2D^2}>1\ge\sin\mu.                    \tag{6}
```

This proves (5). Therefore an exterior train has an open arc of finite
rotations that shortens every old full-span diameter and leaves all proper
diameters unchanged.

The argument bounds all original full-span rows using their extrema.
It does not claim a private leaf in the complete derivative multigraph.
It uses a coordinate absent from all *proper* supports after the full-span
rows have been retained and handled exactly.

For quantitative scope, the two argument corrections have size at most
$`\arcsin(1/D)`$. Thus

```math
|\mathcal F|
\ge2(2m-1)\delta_D-4\arcsin(1/D).                      \tag{7}
```

If $`m\ge(c_*-o(1))D`$, its limiting lower bound is $`4c_*`$.
The allowed phase need not be small and need not lie inside the witness cell.

## 4. Exact source consequence: an inactive-pair blocker

Now assume the actual global cut chart and the contact-minimal, then
diameter-pair-minimal triangle-free global source.

Under this exterior-train substitution, every old unit contact remains exactly
unit: a cut contact changes from $`u`$ to $`w`$, while all others are unchanged.
The source retains its labels and cardinality unless an inactive pair collides,
which is already a unit-separation failure.

There are only finitely many phases at which a previously strict moving pair
becomes exactly unit or exactly diameter. Indeed its squared new length is a
constant plus a linear combination of $`\cos\theta,\sin\theta`$. An identically
unit equation would require its old vector to be $`u`$ (or $`-u`$ in reverse
orientation), making it an old contact, contrary to strictness. An identically
diameter equation would then require $`D=1`$, also excluded.

Choose any phase in the open arc avoiding those finitely many equalities.
If every inactive constraint remained strict, the result would be unit-separated,
have the same contact graph, and have diameter $`D`$, since at least one proper
diameter survives for $`m\ge2`$. Its contact graph would still be triangle-free.
Every full-span diameter would have disappeared and no new diameter would have
appeared. This contradicts the canonical diameter-pair minimality.

Hence every such generic phase has a previously strict moving pair that
violates unit separation or exceeds diameter $`D`$. Writing
$`q=|w-u|=2|\sin(\theta/2)|`$, the triangle inequality gives the exact fork

```math
\boxed{1<|xy|<1+q
\quad\text{or}\quad
D-q<|xy|<D.}                                         \tag{8}
```

The new pair violates its bound, rather than merely having a negative
first derivative. Its endpoints straddle the actual exterior train cut.
All source points, including contact isolates, remain eligible endpoints.

This does not exclude the blocker. In general $`q`$ can be of constant order,
so (8) is not claimed to be an inverse-diameter near-activity theorem.
Feasible exceptional phases with new contacts are not silently excluded:
the generic argument is what avoids them.

## 5. What literal exact grid patches can and cannot block

The far arc (3) must still be compared with the transverse train direction.
Here is an exact finite grid-immunity lemma, stronger than checking just
individual rhombus diagonals.

Take a literal unit oblique grid with directions
$`u=(1,0)`$ and $`v=(\cos\psi,\sin\psi)`$,
$`\pi/3\le\psi\le2\pi/3`$. Rotate one $`u`$-cut to $`w`$ with phase

```math
\psi-2\pi/3\le\theta\le\psi-\pi/3.                    \tag{9}
```

Every old same-shore grid pair is unchanged. An oriented cross-cut grid pair
has new difference

```math
(k-1)u+w+\ell v,\qquad k\ge1,\quad \ell\in\mathbb Z.  \tag{10}
```

If $`k\ge2`$, its projection perpendicular to $`v`$ has magnitude at least

```math
(k-1)\sin\psi-\sin(\theta-\psi)
\ge k\sqrt3/2>1.
```

If $`k=1`$, the cases $`\ell=0,\pm1`$ follow from $`|w|=1`$ and
$`|w\pm v|\ge1`$, which is exactly (9). For $`|\ell|\ge2`$, the triangle
inequality gives $`|w+\ell v|\ge|\ell|-1\ge1`$.
Thus every pair in the literal grid remains unit-separated, including
nonadjacent rows and columns.

This applies to finite subsets of that literal grid as well. It does not assert
that the extracted sparse train rectangle is one affine lattice patch. Other
train crossings, exceptional faces and exterior source points remain distinct
objects. For a single actual rhombus the same window protects its two diagonals
without that stronger affine assumption.

If $`\mathcal F`$ meets the strict interior of (9), the exact grid cannot supply
the blocker in (8); a blocker must involve a source pair outside that literal
patch. The intersection is not proved for every canonical source. Replacing
$`w`$ by $`-u`$ can instead make the two-step grid vector $`u+w`$ zero.
Therefore a phase in the diameter-feasible arc need not be source-feasible.

### Two transverse phases can block all large rotations locally

This attempted inactive-blocker exclusion fails without control of the transverse
phases outside the retained cell. Let
```math
u=(1,0),\qquad v_-=(8/17,15/17),\qquad
v_+=(-8/17,15/17),
```
and take the nine source points
```math
p_{i,0}=iu,\quad p_{i,1}=iu+v_-,\quad
p_{i,2}=iu+v_-+v_+,\qquad i=0,1,2.
```
All 36 pair distances are at least one. Exactly the 12 horizontal and
successive-row edges are unit contacts, so the source is triangle-free and its
four contact faces are strict rhombi. The two $`u`$-train cuts are actual global
outer-to-outer cuts of this finite contact patch.

Put $`\psi=\arg v_-\in(\pi/3,\pi/2)`$ and
$`\varepsilon=\psi-\pi/3\in(0,\pi/6)`$.
After rotating the first $`u`$-train, both rows' old inactive diagonals require
```math
|w\pm v_-|\ge1,\qquad |w\pm v_+|\ge1.
```
Their exact joint phase set consists of
$`[-\varepsilon,\varepsilon]`$ and
$`[\pi-\varepsilon,\pi+\varepsilon]`$, modulo $`2\pi`$.
The old two-step pair $`p_{0,j}p_{2,j}`$ has new vector $`u+w`$.
Its unit-separation condition excludes the second interval.
Thus every contact-preserving rotation outside the first small interval violates
an actual formerly strict grid pair.

Conversely all moving adjacent-row pairs are safe in the first interval by the
grid proof above, applied to each of $`v_-,v_+`$. For a two-row pair the
absolute vertical component is at least
$`30/17-\sin\varepsilon>30/17-1/2>1`$.
Same-row pairs are $`w`$ or $`u+w`$. Hence
$`[-\varepsilon,\varepsilon]`$ is the **complete** phase set passing the
unit-separation constraints of this source patch.

The exact verifier checks this contact graph and all distances, and exhibits
violations for $`w=(3/5,-4/5)`$ and $`w=-u`$.
This is a local obstruction to the proposed far-rotation mechanism.
It does not co-embed this patch with the paired staircase and bracing stars:
its actual diameter graph has only two disjoint edges and its two-column
diameter derivative has rank one. Full-source positive KKT, mixed rigidity
and global optimality are not claimed. The repair would have to use those
missing source conditions to forbid these transverse phase excursions.

## 6. A narrow failure of the arc test forces near-unit pairs

This observation applies to a general paired support class, not only full span.
If its extreme angles give an empty far arc, (4) says
$`a:=D\sin(\Delta/2)<\sin\mu\le1`$.
For $`D\ge9`$, its two extremal bars cannot share a source endpoint:
shared-endpoint diameters have ordinary star opening at most $`\pi/3`$,
which in these opposite orientation classes would give
$`\Delta\ge2\pi/3`$ and $`a>1`$.

Let $`d`$ be the midpoint difference of these two disjoint, upward oriented
diameters. In the bisector basis $`t=(\cos\mu,\sin\mu)`$, $`Jt`$, write
$`d=(x,y)`$, and put $`b=D\cos(\Delta/2)`$.
The two far cross-pair bounds give exactly

```math
x^2+y^2+2b|x|\le a^2.
```

The two near same-arc cross-pair squared lengths are

```math
x^2+(y-a)^2,\qquad x^2+(y+a)^2.
```

Since their minimum is at least one and $`|y|\le a`$,
```math
a|y|\le x^2+a^2-1\le x^2,\qquad |x|\le a^2/(2b).
```
Their maximum is therefore at most
```math
a^2+4x^2
\le1+\frac1{D^2-1}.
```

Both actual same-arc source pairs are thus at distance at most
$`D/\sqrt{D^2-1}=1+O(D^{-2})`$.
If the actual cut-contact hypothesis holds, neither can be unit:
orient their vectors from the lower layer to the higher as
$`q_1=d-aJt`$, $`q_2=-d-aJt`$.
If $`q_1=u`$, then
```math
|q_2|^2=1+4a(a-\sin\mu)<1,
```
contrary to source separation; the reverse case is identical. A unit pair
across these selected cuts must have vector $`u`$.
Consequently an empty far arc forces two *inactive* near-unit source pairs.

For a staircase class of length at least two, Section 3 applied to its nested
subsystem already gives $`a>1`$, so this failure can occur only in the
innermost length-one class. No inference that these inactive pairs are active
or have positive KKT multipliers is made.

## 7. Exact checks and remaining gap

The [exact staircase verifier](../../../research/verify_target_c_star_ray_staircase_2026_10_01.py)
checks an explicit exterior-train finite substitution on its seven-point source:
$`w=(3/5,-4/5)`$, so $`w-u=(-2/5,-4/5)`$.
Move all points except the layer-zero anchor by this vector.
All 21 new pair distances remain in $`[1,13]`$. The two old unit contacts
remain the only contacts. Both old full-span diameters shorten, and the two
proper-support diameters remain the only diameters. This certifies the finite
diameter-count reduction at geometric scope, not global optimality or actual
complete train extraction.

The rational grid check uses $`v=(8/17,15/17)`$, for which
$`u\cdot v=8/17`$ and $`w\cdot v=-36/85`$, both strictly between $`-1/2`$
and $`1/2`$. It verifies (10) for $`1\le k\le20`$, $`-20\le\ell\le20`$.
The arbitrary-grid proof is Section 5, not the finite sample.

### The one-train exception is real at geometric scope

Set
```math
a=1999/2000,\quad x=1/28,\quad
D^2=a^2+13^2,\quad y=(13+x)/2,\quad
z^2=D^2-(13-x)^2/4.
```
Use the five points
```math
v=(a-z,y),\quad A=(0,0),\quad C=(a,x),\quad
B=(a,13),\quad E=(0,13+x).
```
Their strict convex hull order is $`v,A,C,B,E`$. All ten pair distances
are strictly greater than one and at most $`D`$. Their exact actual
diameter graph is $`vB,vC,AB,CE`$, a four-edge caterpillar.
Give $`v,A,E`$ layer zero and $`B,C`$ layer one. The two witnesses
$`vB,vC`$ straddle $`u`$, have opening strictly below $`\pi/3`$, and
all four rows are full-span. Equal positive weights $`1/4`$ give zero
projected work and rank one.

The extremal vectors are $`AB=(a,13)`$, $`EC=(a,-13)`$.
Their transformed determinant in (4) is
```math
2\cdot13(a-1)=-13/1000<0.
```
Thus the far arc is empty, despite the common star and positive projected
balance. The two source pairs $`AC,EB`$ have squared distance
```math
a^2+x^2=196054049/196000000>1,
```
and both satisfy the inverse-square near-unit bound from Section 6.

The exact verifier checks all pair distances, every hull support
orientation, the four actual diameters, the angle ordering by determinants,
and this negative transformed determinant. No actual train cuts are encoded:
the source has no unit contacts. It has no full-source KKT equilibrium at
$`v`$, and a five-point unit-spaced line of diameter four explicitly beats
its diameter. This is a regression against removing $`m\ge2`$, not a
triangle-free global-minimizer disproof.

| Result | Classification | Limit |
| --- | --- | --- |
| Full-system exterior-train far arc | proved candidate awaiting promotion | Explicit paired staircase; $`m\ge2`$ |
| Inactive-pair fork | conditional | Actual cuts and canonical lexicographic global source |
| Whole literal grid immunity | proved candidate awaiting promotion | Exact affine grid and window (9) |
| Empty arc near-unit localization | proved candidate awaiting promotion | Disjoint extremal bars; actual cuts for strict inactivity |
| Five-point empty-arc source | regression | $`m=1`$; geometric and projected balance scope |
| Two-phase grid obstruction | regression | Actual unit cuts; no full-rank staircase or global optimality |
| C-II closure | not claimed | The inactive source blocker remains |

The finite release now passes every old actual diameter constraint and preserves
every old contact under the actual cut hypothesis. The missing step is to find
a phase in its open arc that also passes every previously strict source pair,
or to use the forced inactive blockers to construct a second finite move.
The transverse grid alone does not supply that step. Nonconstant phase,
split-star O-O, inactive interfaces and macroscopic inactive containers remain
outside this report.
