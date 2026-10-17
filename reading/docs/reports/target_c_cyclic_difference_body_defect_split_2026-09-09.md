> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_difference_body_defect_split_2026-09-09.md) · source SHA-256 `7cbf36ad46e7bc57baaafcbbec118e386034a0e4a9823dc15117c3751e087342`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A09C2281B3A1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic diameter defect splits exactly into parallel-side and short-antipodal defects

**Date:** 2026-09-09  
**Repository branch:** PR #118 after DA/RP/R2/MT  
**Run type:** exact difference-body combinatorics  
**Target:** complete cyclic primitive endpoint  
**Depends on:** CY `h=q-d_H`, C67 distinct diameter directions, elementary Minkowski-sum polygon geometry  
**External literature:** none needed for the count; rotating-calipers terminology is interpretive only  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The maximal-thrackle completion MT shows that the full diameter graph is at most two chords short of an odd-cycle-plus-leaves extremal thrackle. The difference body gives a more canonical defect decomposition which does not depend on choosing a maximal completion.

Let

```math
K:=F-F.
```

Then `K` is centrally symmetric, has perimeter `2q`, lies in the radius-`D` disk, and has at most `2q` vertices.

### Theorem AD — exact antipodal defect split

Let

```math
r_\parallel
```

be the number of unordered pairs of parallel sides of the strictly convex equilateral force hull `F`. Then

```math
\boxed{|V(K)|=2q-2r_\parallel.}
\tag{AD.1}
```

Exactly

```math
\boxed{2h=2(q-d_H)}
\tag{AD.2}
```

vertices of `K` lie on the Euclidean circle of radius `D`. Every such circular vertex is one of the oriented actual diameter vectors

```math
\pm(p_i-p_j),
\qquad ij\in H.
```

Consequently

```math
\boxed{r_\parallel\le d_H,}
\tag{AD.3}
```

and the number `a_short` of antipodal pairs of vertices of `K` lying strictly inside the radius-`D` circle is exactly

```math
\boxed{a_{short}=d_H-r_\parallel.}
\tag{AD.4}
```

Thus the complete cyclic defect satisfies the exact integer partition

```math
\boxed{d_H=r_\parallel+a_{short}.}
\tag{AD.5}
```

Because `d_H<=2`, there are only six nominal cases, reduced phase-by-phase to:

```text
d_H=0:
    r_parallel=0, a_short=0.

d_H=1:
    (r_parallel,a_short)=(1,0) or (0,1).

d_H=2:
    (r_parallel,a_short)=(2,0), (1,1), or (0,2).
```

In particular every cyclic tree phase has at most two parallel side pairs and at most two short antipodal vertex pairs in its difference body.

---

## 1. Difference-body perimeter and disk containment

Minkowski perimeter is additive in the plane. Hence

```math
\operatorname{per}(K)
=\operatorname{per}(F)+\operatorname{per}(-F)
=2q.
\tag{1.1}
```

Every point of `K` has the form

```math
x-y,
\qquad x,y\in F.
```

Since `diam F=D`,

```math
|x-y|\le D.
```

Therefore

```math
\boxed{K\subseteq D B_2.}
\tag{1.2}
```

---

## 2. Count the difference-body vertices from side directions

Orient the `q` sides of `F` counterclockwise. Strict convexity implies their oriented tangent directions are all distinct modulo `2pi`.

The polygon `-F` has the opposite tangent direction for every side of `F`. The edge directions of the Minkowski sum

```math
F+(-F)=K
```

are the cyclic merge of the edge-direction lists of `F` and `-F`; equal oriented directions merge into one Minkowski edge.

An oriented direction from `-F` coincides with one from `F` exactly when `F` contains a pair of oppositely oriented parallel sides. Each unordered parallel-side pair creates exactly two such coincidences, one for each orientation.

Because strict convexity gives at most one side in any fixed oriented direction, these coincidences are disjoint. Hence the merged edge-direction list has size

```math
2q-2r_\parallel.
```

A nondegenerate convex polygon has equally many edges and vertices, proving AD.1. `square`

---

## 3. Every actual diameter direction gives two circular vertices of `K`

Take an actual diameter edge

```math
ij\in H.
```

Then

```math
x_{ij}:=p_i-p_j\in K,
\qquad
|x_{ij}|=D.
```

By (1.2), `K` is contained in the strictly convex radius-`D` disk. A point of a convex subset which lies on the boundary circle cannot be a nontrivial convex combination of two distinct points of the subset: strict convexity of the Euclidean disk would put that combination inside the circle.

Therefore

```math
x_{ij}
```

is an extreme point of `K`, hence a polygon vertex. So is `-x_{ij}`.

C67 says distinct actual diameter edges have distinct projective directions. Thus the `h` edges give exactly

```math
2h
```

distinct circular vertices of `K`.

---

## 4. Every circular vertex of `K` is an actual diameter vector

Conversely let

```math
x\in V(K),
\qquad |x|=D.
```

A vertex of the polygonal Minkowski difference `F-F` is representable as

```math
x=p_i-p_j
```

for vertices `p_i,p_j` of `F` whose normal cones support that Minkowski vertex.

Then

```math
|p_i-p_j|=D,
```

so `ij` is an actual diameter pair and belongs to the full diameter graph `H`.

Therefore there are no extra circular vertices beyond the `2h` oriented diameter vectors. This proves AD.2 exactly. `square`

---

## 5. Subtract circular vertices from total vertices

The off-circle vertex count is

```math
\begin{aligned}
|V(K)|-2h
&=(2q-2r_\parallel)-2(q-d_H)\\
&=2(d_H-r_\parallel).
\end{aligned}
\tag{5.1}
```

It is nonnegative, giving

```math
r_\parallel\le d_H.
```

Central symmetry pairs every off-circle vertex with its negative, so the number of antipodal off-circle pairs is

```math
a_{short}
=\frac{|V(K)|-2h}{2}
=d_H-r_\parallel.
```

This proves AD.3-AD.5. `square`

---

## 6. Canonical antipodal-pair interpretation

Each vertex of `F-F` corresponds to a vertex-vertex antipodal pair of the convex polygon `F` in the rotating-calipers sense: the two vertices admit parallel supporting lines with opposite normals.

Modulo sign, `K` therefore gives exactly

```math
q-r_\parallel
```

canonical antipodal vertex pairs. Among them

```math
h=q-d_H
```

are actual diameter pairs, and exactly

```math
a_{short}=d_H-r_\parallel
```

are strictly subdiametral.

Thus the difference body provides a canonical completion of the diameter graph by only `a_short` short antipodal pairs. This can be strictly smaller than MT's arbitrary maximal-thrackle completion size `d_H`: the remaining defect is accounted for by parallel force-hull sides rather than a missing antipodal vertex pair.

No maximal-completion choice is involved.

---

## 7. Phase normal forms

### `d_H=0`

AD forces

```math
r_\parallel=a_{short}=0.
```

Thus `F-F` has exactly `2q` vertices, every one on the radius-`D` circle. RE strengthens this to the regular `2q`-gon.

### `d_H=1`

There are exactly two branches.

#### P1: one parallel-side pair

```math
r_\parallel=1,
\qquad
a_{short}=0.
```

Then `F-F` has `2q-2` vertices and **every one lies on the radius-`D` circle**. Equivalently every canonical antipodal vertex pair is already a diameter pair.

#### S1: one short antipodal pair

```math
r_\parallel=0,
\qquad
a_{short}=1.
```

Then `F-F` has the maximal `2q` vertices; exactly one antipodal vertex pair lies strictly inside the radius-`D` circle and all other `2q-2` vertices lie on it.

### `d_H=2`

There are three branches:

```text
P2: r_parallel=2, a_short=0
    K has 2q-4 vertices, all circular.

PS: r_parallel=1, a_short=1
    K has 2q-2 vertices, exactly one antipodal pair short.

S2: r_parallel=0, a_short=2
    K has 2q vertices, exactly two antipodal pairs short.
```

This is a finite exact replacement for an unrestricted near-Reinhardt difference body.

---

## 8. Immediate perimeter inequalities

Put

```math
N:=|V(K)|=2(q-r_\parallel).
```

Because `K subset D B_2`, the maximum perimeter of an `N`-vertex polygon in the radius-`D` disk is attained by the regular `N`-gon. Therefore

```math
2q=\operatorname{per}(K)
\le
2N D\sin\frac\pi N.
```

Equivalently

```math
\boxed{
q
\le
2(q-r_\parallel)D
\sin\frac{\pi}{2(q-r_\parallel)}.}
\tag{8.1}
```

For `r_parallel>0`, this is a phase-specific lower bound on `D` stronger than the formal `q`-gon Reinhardt lower bound. Its leading excess is only of order `D^-2`, so it does not by itself contradict R2; the constants remain compatible.

The useful gain is structural: in the `a_short=0` branches the complete difference body is an inscribed cyclic polygon, while in the other branches only one or two antipodal vertex pairs can leave the circle.

---

## 9. Relation to the 2026 difference-body proof architecture

Recent work on the power-of-two Reinhardt problem uses the difference body and a sign-code reconstruction, with a key saturation step forcing all difference-body vertices onto the unit circle for an extremizer.

AD shows that Target C is already within at most two antipodal vertex pairs of that saturation **before** any such classification theorem is imported. The remaining defects are explicitly separated into:

1. loss of a difference-body vertex pair caused by parallel primal sides;
2. retention of a difference-body vertex pair at radius strictly below `D`.

This is the natural state space for importing or adapting sign-code/strong-convexity methods.

No unreviewed 2026 proof candidate is used as a theorem here.

---

## 10. Regression audit

### Parallel sides

Correctly reduce the number of difference-body vertices. They are not miscounted as short antipodal pairs.

### Multiple representations of one Minkowski vertex

Allowed. A circular Minkowski vertex needs only one vertex-difference representation; that pair is an actual diameter pair. C67 prevents two distinct full-H edges from contributing the same projective circular vertex.

### MT completion nonuniqueness

Irrelevant. AD is canonical and depends only on `F-F`.

### Power-of-two near-extremizers

Compatible: they can live in S1/P1-type near-saturated difference-body branches. AD does not falsely promote near-saturation to exact Reinhardt equality.

---

## 11. Next theorem

The tree phases have now split into only five finite defect patterns. The best next targets are:

1. **parallel branch:** use SL local diameter minimality to test whether P1/P2 can contain parallel unit hull sides without an admissible side-preserving diameter-lowering motion;
2. **short-antipodal branch:** quantify the radial defect of the one/two off-circle difference-body vertex pairs using R2's explicit `D^-2` global ladder defect;
3. adapt the difference-body sign-code Hessian from the Reinhardt power-of-two literature to a configuration with only one or two unsaturated antipodal pairs.

---

## 12. Promotion recommendation

**Hold as report pending independent audit.**

AD is an elementary exact consequence of the cyclic normal form and difference-body geometry. It introduces no external theorem dependency.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let K=F-F. Then K is centrally symmetric, per(K)=2q, K subset D disk.
If r_parallel is the number of parallel side pairs of F, the edge-direction merge in
F+(-F) gives
  |V(K)|=2q-2r_parallel.
Every actual diameter vector +/- (p_i-p_j) lies on the radius-D circle and is therefore
an extreme vertex of K. C67 gives 2h distinct such vertices. Conversely every circular
vertex of K is a vertex difference of length D, hence an actual diameter pair. Thus
  # circular K vertices =2h=2(q-d_H).
Subtract:
  # off-circle K vertices=2(d_H-r_parallel).
Therefore
  d_H = r_parallel + a_short,
where a_short is the number of antipodal off-circle vertex pairs.

Phases:
 d0: (0,0)
 d1: P1=(1,0) or S1=(0,1)
 d2: P2=(2,0), PS=(1,1), S2=(0,2).

So F-F is completely circle-saturated except for at most two antipodal pairs, and at
most two primal side pairs can be parallel. Next: parallel-side local-motion exclusion
or R2 quantitative control of the one/two radial defects.
```
