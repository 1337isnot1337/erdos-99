> Generated reading edition · [exact source](../../../docs/reports/target_c_global_convex_bank_defect_audit_2026-10-02.md) · source SHA-256 `ff219c5351cc3c0806d106964106634a31f8a55be60a81815238624413236827`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6D682AC6DADC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_global_convex_bank_defect_audit_2026-10-02.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=652f4a719e8c3f2e0f56afa370e0b71339425238; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C-II — independent convex-bank audit and global defect charge

**Date:** 2026-10-02  
**Starting commit:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`  
**State version:** `2026-09-14.audit.51`  
**Owned branch:** `swarm/sol/convex-bank-audit-20261002`  
**Assignment:** hostile audit of PR #609, followed by a global C-II defect inequality  
**Audited packet:** [PR #609](https://github.com/1337isnot1337/e-99/pull/609),
commit `72c97c32db7ca5d5cda8313ccc78dd99afd0ed9a`  
**Classification:** proved candidate awaiting independent promotion audit;
scoped audit of the bank mechanism; regression against scalar-only closure  
**Literature:** no new import  
**LEVEL I:** OPEN. **C-II:** OPEN.

```text
uniform convex-bank phase capacity
 -> actual aggregate Z=sum(L_r-per(P_r)) and Q=sum Q_r
 -> positive full-core defect cost, usable in an upper ledger
 -> contradiction only if that same upper ledger supplies a smaller cost.
```

The last implication is a named missing obligation, not a claim of closure.
The result below is global across the harmonic tiling. It does not require the
rooted threshold, a fixed star, an exact phase, a complete crossing grid, or a
global outer-to-outer extraction. It therefore avoids the numerical threshold
counting in PRs #603–607.

## 1. Exact new conclusion

Use the canonical full-core near-disk Type-II source and all its unloaded
positive-contact components. For component `I_r`, retain

```math
H_r=C[I_r\cup A_r],\quad P_r=\operatorname{conv}A_r,\quad
p_r=\operatorname{per}P_r,\quad L_r=|\text{outer walk of }H_r|,
```

```math
Q_r=\sum_{f\text{ bounded in }H_r}(\deg f-4),\qquad
Z_r=L_r-p_r.
```

The graph `H_r` includes actual loaded-loaded contacts on its vertices.
`Q_r` is the induced-graph defect of Section 82, not the augmented `Q_r^+`
of Section 123 and not a phase-cut subcomplex defect. Put

```math
Z_D=\sum_r Z_r,\qquad Q_D=\sum_r Q_r.
```

For every subsequence on which `Z_D/D -> z` and `Q_D/D -> q`, and every
`0<epsilon<pi/8`, the new candidate theorem is

```math
\boxed{
{\pi\over4}\le 5q+
{\sqrt3\over6}(2\pi^2+z+5q)
\left[\left(1+{1\over1-\cos\epsilon}\right)z
+2\tan\epsilon\right].
}
\tag{1}
```

In particular, for `0<=z<=1/66`,

```math
\boxed{
{\pi\over4}\le 5q+
{\sqrt3\over6}(2\pi^2+z+5q)(66z)^{1/3}.
}
\tag{2}
```

Consequently every canonical full-core sequence satisfies

```math
\boxed{
\liminf_{D\to\infty}{Z_D+Q_D\over D}\ge {1\over26000}.
}
\tag{3}
```

No positive lower bound on `Z_D` alone is asserted. Exceptional-face defect
can supply the cost. All contact-isolated source points remain in the source;
the theorem uses the canonical full-core theorems to locate the required
quadratic rhombic area in the positive-contact harmonic cells.

The novelty over PR #609 is an all-cell, all-phase area charge. There is no
loss through the Section-91 complete-grid coefficient. The coefficient
`1/26000` is a safe rational consequence, not an optimized constant.

## 2. Canonical inputs and exact objects

Only the following canonical mathematics is used:

1. [Section 62](../targets/target-c/62-attachment-incidence-currency-audit.md):
   harmonic trapping, extreme loaded attachments, attachment incidence, and
   `sum p_r <= 2 pi^2 D+O(1)`.
2. [Section 82](../targets/target-c/82-harmonic-cell-near-quadrangulation-audit.md),
   especially Lemma 82.1: local hull augmentation is 2-connected with convex
   bounded faces; all four-faces are strict unit rhombi; their physical
   boundary satisfies `P_R,r <= L_r+5Q_r`.
3. [Section 83](../targets/target-c/83-attachment-cell-disjoint-tiling-audit.md):
   distinct cell interiors are disjoint and unloaded-only rhombic area sums
   to `pi D^2/4-o(D^2)` in the full-core near-disk branch.
4. [Section 80](../targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md):
   after translating, `B(0,r_D) subset F_D subset B(0,R_D)` with
   `r_D/D,R_D/D -> 1/2`.
5. [Section 68](../targets/target-c/68-punctured-packing-phase-audit.md):
   total rhombic area excess and acute-angle defect are `O(D)`; one global
   reduced-phase cut removes `O(D)` rhombi and gives real phases with
   `x_v-x_u=delta_R>0` at every retained crossing, with three phase labels.
6. [Shared Theory 01, Theorem 10.6](../theory/01-local-structure.md): complete
   local trains have two distinct physical ends, two trains cross at most
   once, their crossing graph is triangle-free, and each train's total
   incident rhombic area is its exact transverse span, at most `D`.

Section 89 independently records the last span and boundary identities.
Sections 90–91 and all current-main rooted-detour packets are unnecessary
premises for (1)–(3).

PR #609 is inspected as an unpromoted packet. Its geometric argument is
reconstructed in Sections 3–4 rather than assumed as a theorem. Its rooted
endpoint application remains conditional on the unpromoted rooted stack;
this audit does not promote or independently audit that stack.

## 3. Independent hostile audit of the finite bank mechanism

Fix one component, temporarily suppressing `r`. Enumerate the attachments
`a_1,...,a_s` counterclockwise. The outer walk decomposes into banks `W_i`
from `a_i` to `a_{i+1}`. Write `d_i=|a_{i+1}-a_i|`,
`t_i=(a_{i+1}-a_i)/d_i`, and `ell_i=|W_i|`.

### 3.1 Boundary occurrences and articulation vertices

Deleting one attachment leaves `I`, with all other attachments, connected,
so an attachment is not an articulation vertex of `H`. Each has one outer
occurrence; planarity inside their convex hull gives the convex cyclic order.
If a bank revisits an unloaded vertex, the enclosed outer excursion gives
a component of `H-x` containing no attachment. Positive harmonicity with
sole boundary value `x` collapses that component, contradicting distinct
points. Thus each bank is a simple path with only unloaded internal vertices.
An unloaded articulation can still lie on two different banks. Its separate
occurrences are retained; no quotient identifies them.

After adding a missing polygon side, its face has that side as its only
added side. At every attachment an actual edge to `I` lies strictly inside
the tangent cone and separates the two adjacent polygon sides. Lemma 82.1
makes the pocket boundary a simple convex cycle. Thus the directed bank
edges, with orientation from `a_i` to `a_{i+1}`, turn clockwise.

The exact account is

```math
Z=L-p=\sum_i(\ell_i-d_i),\qquad
\ell_i-d_i=\sum_{e\in W_i}(1-e\cdot t_i).
\tag{4}
```

Every summand is nonnegative. This uses unit contact lengths and physical
outer-walk occurrences.

### 3.2 Strictness only at actual rhombic ends

Call a terminal unit edge good if its induced directed bank angle differs
from `t_i` by at most `epsilon`. Convexity orders good directions
nonincreasingly clockwise. If two terminal edges had equal directed angle,
all intervening bank edges would be collinear. An internal endpoint would
have pocket angle `pi`. All its incident contact vectors lie in the opposite
closed half-plane. Strictly positive equilibrium then places all neighbors
on the line. But the incident rhombus supplies a nonparallel neighbor.
Contradiction. An extreme attachment cannot be an internal collinear point;
a direct contact bank contains just one edge.

Therefore good terminal angles strictly decrease along each bank. This is
not strict convexity at every bank vertex, a quantitative angle gap, or a
multiplier floor.

Different complete trains consume different physical terminal occurrences.
Thus the number of bad ends in any selected family is at most

```math
Z/(1-\cos\epsilon).
\tag{5}
```

### 3.3 One train per good pair of banks

Take one family of projective phase width `w`, with
`w+2epsilon<pi/2` and `w<pi/3`. It is internally noncrossing. Each train's
two ends have opposite induced outer-boundary orientations, by its strictly
increasing transverse coordinate. At one bank all good ends in the family
use the same sign, so a two-good-ended train uses two distinct banks.

Extend centerlines through their convex outer pockets to the attachment
polygon boundary. The pocket interiors contain no train centerline and are
disjoint faces, so extensions preserve endpoint order and can be disjoint.
Two noncrossing crosscuts between the same two boundary intervals have
opposite orders on those intervals in counterclockwise traversal. Strict
clockwise bank order would then require both `phi_1>phi_2` and
`phi_2>phi_1`, after subtracting each bank's common sign offset. Equal phases
also contradict strictness. Therefore at most one family member has good
ends on any given unordered bank pair.

This proof covers stars, paths, holes and repeated outer-walk vertices;
it uses no diameter-Euler-path assertion or basis-leaf deformation.

**Audit disposition:** PR #609's scoped bank-order and bank-pair argument
survives these checks under its stated positive-equilibrium hypotheses.
Its geometry-only extension to an unstressed grid remains false, exactly
as its own regression records.

## 4. Uniform narrow-phase capacity across every cell

Let `rho_D=acos(r_D/R_D) -> 0`, and choose `eta>0` sufficiently small.
There are at most `pi/eta` banks with chord length greater than `eta D`,
because each cell has perimeter at most `pi D`. By Section 3, at most
`pi^2/(2eta^2)` trains have good ends on two such banks.

For a short chord, its endpoint minor polar separation is at most

```math
2\arcsin(d_i/(2r_D))\le4\eta
```

for large `D`. Each force-hull support normal differs from its radial
direction by at most `rho_D`. A short chord is the integral of tangents on
its short hull arc, all in the same small cone. If it has a good end from
the family, both endpoints lie in the two polar bands centered at the
transverse directions, each of half-width

```math
a_D=\epsilon+w+\rho_D+4\eta.
```

Except for at most one consecutive attachment gap (the gap exceeding `pi`),
the corresponding short hull arcs are disjoint and lie in these bands.
Projection along the family direction bounds their total length by

```math
{4R_D\sin a_D\over\cos(a_D+\rho_D)}.
```

The exceptional short chord contributes at most `eta D`. The number of
short-bank good ends is at most this chord sum plus `Z`, by (4).
Combining good-long pairs, bad ends, and good-short ends gives

```math
M\le {\pi^2\over2\eta^2}
+\left(1+{1\over1-\cos\epsilon}\right)Z
+\eta D+{4R_D\sin a_D\over\cos(a_D+\rho_D)}.
\tag{6}
```

The constants are uniform in the component, its attachment count, the
family's central direction, and the phase bin. In particular, if
`Z_D/D -> z`, every such family in every component obeys

```math
{M\over D}\le
\left(1+{1\over1-\cos\epsilon}\right)z
+\eta+2\tan(\epsilon+w+4\eta)+o(1).
\tag{7}
```

Here we used `Z_r<=Z_D`. We will use this *uniform maximum* in a graph
sum, not sum the `eta D` error once for every component. This prevents an
uncontrolled `c_I eta D` loss.

The short-arc proof in PR #609 survives the support-normal and exceptional
major-gap checks. This report uses its actual near-disk hypothesis, not a
near-disk property of each individual attachment polygon.

## 5. Exact tripartite crossing bound

### Lemma

If a simple triangle-free tripartite graph has part sizes `a,b,c<=M` and
`N=a+b+c`, then

```math
\boxed{E\le\max\{a(b+c),b(a+c),c(a+b)\}\le {2M\over3}N.}
\tag{8}
```

### Proof

Within one independent part, replace every vertex by a twin of a vertex
having maximum degree in that part. This cannot decrease the number of
edges. It preserves triangle-freeness: a triangle through a new twin would
already have existed through its original representative. Do this in all
three parts. Previously made twin classes remain twins, because every
vertex in a later part has identical adjacency to each earlier twin class.

The final graph has either all or none of the edges between each part
pair. Its three-vertex quotient is triangle-free, so at most two part pairs
are complete. This gives the first inequality. For the second, each ratio
`a(b+c)/(a+b+c)` increases in each nonnegative variable, and is at most
`M(2M)/(3M)=2M/3`. The same applies to the other two ratios. Empty parts
are handled by continuity or directly. Equality is attained by `K_(M,2M)`
with three parts of size `M`. This coefficient cannot be improved using
only the encoded graph hypotheses. QED.

## 6. All-cell, all-phase proof of (1)

Take the full local strict-rhombus complex in each `H_r`. Its complete
trains, including those through loaded rhombi, have total count

```math
T_D\le {1\over2}\sum_r(L_r+5Q_r)
= {1\over2}\left(\sum_rp_r+Z_D+5Q_D\right).
\tag{9}
```

Remove every train having an end on a bounded nonquadrilateral face.
There are at most `5Q_D` such trains: each consumes a distinct physical
boundary edge and the exceptional-face perimeter is at most `5Q_D`.
The union of their incident rhombi has area at most

```math
5Q_D D.
\tag{10}
```

Indeed each removed train's incident rhombic area is its exact transverse
span, at most `diam(P_r)<=D`; summing spans overcounts overlaps, which is
the correct direction. Every surviving train is locally outer-to-outer.
Nothing here transfers its ends to the global outer walk.

Perform the canonical global reduced-phase cut, losing `O(D)` rhombi.
Fix `0<w<pi/3`, then randomly shift bins of width `w` on the real reduced
phase line. A retained rhombus with endpoint phase difference `delta_R`
is separated by a bin boundary with probability at most `delta_R/w`.
Since `sum delta_R=O(D)`, one shift leaves only `O(D/w)` separated rhombi.
For fixed `w`, this is `o(D^2)`. No inverse-diameter bin or biclique is needed.

Inside a single component and bin, use its three phase labels as the
tripartition of the surviving train crossing graph. Same-label directions
have projective separation below `pi/3`, so cannot cross. The graph is
simple and triangle-free by Theorem 10.6. Each part has the uniform maximum
`M_D` from (7). Lemma (8) bounds its crossing count by `2M_D N/3`.
Summing over all bins and components counts each remaining train at most
once, so the total retained crossing count is at most `2M_D T_D/3`.

Every counted rhombus has area `a_0+epsilon_R`, with
`a_0=sqrt(3)/2` and `sum epsilon_R=O(D)`. The all-cell rhombic area is
`pi D^2/4-o(D^2)`: Section 83 proves this already for the unloaded-only
subcollection, while cell disjointness bounds the full collection above
by `area(F)=pi D^2/4+o(D^2)`. Thus (9)–(10) yield

```math
{\pi\over4}\le5q+{2a_0\over3}
\limsup{M_D\over D}\,
{2\pi^2+z+5q\over2}.
\tag{11}
```

First let `D -> infinity`, at fixed `epsilon,w,eta`. Then let `eta -> 0`
and then `w -> 0`, using the uniform bound (7). This gives (1).
These limits do not discard a boundary-order term: the constant in (6),
multiplied by `T_D=O(D)`, contributes only `O(D)` crossing count. The
`eta D` and phase-width errors occur in a maximum, not a component sum.

All local rhombi are actual global strict-rhombus faces, so they inherit
the canonical reduced phases. No independently chosen scaffold is used.
Holes, bounded exceptional faces and contact isolates are retained in
their own exact roles.

## 7. Cubic simplification and the rational floor

For `0<z<=1/66`, put `gamma=(66z)^(1/3)<=1` and
`epsilon=gamma/3<pi/8`. Elementary Taylor bounds give

```math
\cos\epsilon\ge17/18,\quad
1-\cos\epsilon\ge(107/216)\epsilon^2,\quad
2\tan\epsilon\le(12/17)\gamma.
```

Consequently

```math
\left(1+{1\over1-\cos\epsilon}\right)z+2\tan\epsilon
\le\left({2051\over7062}+{12\over17}\right)\gamma
<\gamma.
\tag{12}
```

The positive rational margin in the final coefficient is `443/120054`.
For `z=0`, let `epsilon -> 0`. Equation (2) follows.

Suppose a subsequential limit has `u=z+q<=1/26000`. Then
`z<=u<1/66` and

```math
{\pi\over4}\le5u+
{\sqrt3\over6}(2\pi^2+6u)(66u)^{1/3}.
\tag{13}
```

But `(137/1000)^3 > 66/26000`, while the elementary bounds
`157/50<pi<22/7` and `sqrt(3)<26/15` give

```math
5u+{\sqrt3\over6}(2\pi^2+6u)(66u)^{1/3}
\le {5\over26000}
+{13\over45}\left(2(22/7)^2+{6\over26000}\right){137\over1000}
< {157\over200}< {\pi\over4}.
```

The exact gap in the strict rational inequality is
`84146693/28665000000`. Contradiction.

The aggregate quantities are boundary-order, so this subsequence argument
proves (3). For completeness, `a_r>=3` and the canonical incidence bound
give `c_I<=|B|-2` and `sum a_r<=3|B|-6`. Summing Section 82's exact
`L_r+Q_r=4a_r-6-2s_r-2c_r` therefore gives `Z_D+Q_D=O(D)`.
Thus every sequence violating the liminf conclusion has a convergent
subsequence of normalized `Z_D,Q_D`, as used above.

## 8. Attempts to turn the charge into closure

### 8.1 The positive-cost scalar account survives

Equation (2) is compatible with `q=0,z=1/100`. The verifier proves this
using rational lower bounds, rather than mistaking a lower cost for an
upper bound. This tuple is a scalar regression only; no Euclidean source
or global minimizer is claimed.

The rooted defect stability packet has an upper account for the same
`Z_D+Q_D`. Substitution of (3) would exclude any regime where that upper
account has limsup below `1/26000`. That implication is conditional on
the unpromoted account and supplies no global upper bound. This report
does not recompute a rooted numerical threshold.

### 8.2 Local filling does not pay an arbitrary boundary-order cost

An attempted closure was to infer `Z_D=o(D)` from the canonical local
nonrhombic area `o(D^2)`. That scale conversion is unjustified. A pocket
with base and width `O(1)` but length `Theta(D)` has only `O(D)` area and
can have `Theta(D)` route excess. Positive equilibrium at a nearly flat
bank provides strict angle order but no uniform angle/force floor. The
existing exact local force-star regression in PR #609 specifically rules
out that floor.

For long attachment chords the convex-pocket area controls macroscopic
height, but the cost can remain on short chords. No source-level theorem
here excludes those thin pockets. This is a precise failed implication,
not a constructed global-minimizer counterexample. It is the same reason
that the rejected Section-121 conversion `o(D^2)/Theta(D)=o(1)` cannot be
reintroduced through a bank-area argument.

### 8.3 Contact ledgers allow positive defect

The exact local ledger gives
`Z_D+Q_D=4 sum a_r-6c_I-2s_C-2 sum c_r-sum p_r`.
Attachment incidence and the loaded perimeter ceiling make this quantity
`O(D)`; they do not make it `o(D)` or negative. No diameter support weight
or source-specific finite motion appears in (1). Adding this positive
defect cost to those ledgers therefore does not close the higher-defect
full-core branch.

The next actual closure obligation is to use the actual diameter graph or
source minimality to upper-bound this same aggregate currency below (3),
or turn its unavoidable short-bank/exceptional-face contribution into a
simultaneous source-preserving strict competitor. The macroscopic inactive
container branch remains outside the full-core hypothesis.

## 9. Scope and hostile checks

| Check | Result and boundary |
| --- | --- |
| Articulations and repeated boundary vertices | Separate physical occurrences retained; no-attachment excursions excluded by harmonicity. |
| Flat bank edges | Strictness only at actual train ends; arbitrary convex faces may have flat portions. |
| Stars and paths | No diameter traversal or private-basis leaf premise. |
| Holes and exceptional interfaces | Ends on bounded nonquadrilateral faces paid through their actual area spans. |
| Same global train split into local segments | Segments remain separate local graph vertices and inherit the same phase; no false global injectivity. |
| Many cells/bins | Capacity used as a uniform maximum; train counts, not capacity errors, are summed. |
| Source isolates | Retained; near-disk full-core hypotheses supplied by canonical source theorem. |
| Triangle-free graph coefficient | Exact `K_(M,2M)` equality shows `2M/3` is sharp at the abstract graph level. |
| Positive-defect survivors | Scalar compatibility remains; no fake C-II closure. |
| Finite motion | None constructed or inferred. |

## 10. Computation, reproducibility and disposition

Run

```bash
python3 research/verify_global_convex_bank_defect_2026_10_02.py
```

The verifier exhaustively checks all triangle-free simple tripartite graphs
with each part of size at most two, verifies the rational constants in
(12)–(13), and certifies the scalar nonclosure example. Its universe omits
Euclidean coordinates, stresses, bank geometry, phase inheritance,
asymptotics and global optimality. The human proofs above, not finite
enumeration, prove the unrestricted tripartite lemma and geometric bridge.

**Audit scope:** PR #609 Sections 2–7 survive this hostile reconstruction.
The finite bank-pair claim and its near-disk capacity mechanism may be
treated as audited-working for this packet, under the stated canonical
equilibrium hypotheses. Its Section-8 rooted application is still
conditional and was not audited through its complete unpromoted stack.

**New claim status:** (1)–(3) are proved candidates awaiting independent
audit and promotion; the artifact lifecycle is unreviewed. No theorem-state
manifest, canonical route or prompt is changed.

**Handoff:** the durable new object is the aggregate full-core inequality
(1), with exact `Z_D` and induced `Q_D`, and rational floor (3). Its missing
bridge is a source-specific upper payment or finite release, not another
complete-grid extraction or a decimal-only threshold improvement. Read
Sections 3–7 here, canonical Sections 62/68/82/83, and the actual upper
ledger before importing it. C-II and Level I remain OPEN.
