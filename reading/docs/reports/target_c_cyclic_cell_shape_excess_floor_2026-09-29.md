> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_cell_shape_excess_floor_2026-09-29.md) · source SHA-256 `d30126123e1c79db3cb6e10427df077c35edf3d3b7adc18ca7ac9d71ee431703`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-D67352416C8F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — cyclic-cell shape-excess floor

**Date:** 2026-09-29
**Base main:** `77d418e49da08328f126fcd5bbab21cccb15b639`
**Status:** unreviewed proof-only candidate; C-II and Level I remain open. This salvage did not independently audit every dependency or change canonical theorem status.
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

**Salvage source:** `proof/target-c-cyclic-cell-shape-excess-20260929-v2` at `1b4c3414afc661131a2ac7387401b290cf9b5439`. Preserved from that branch onto current main without route or theorem-state changes.

## 1. Theorem

On the canonical full-core Type-II branch, for each harmonic attachment cell
```math
P_r=\operatorname{conv}(A_r),\qquad
p_r=\operatorname{per}(P_r),\qquad
d_r=\operatorname{diam}(P_r),
```
put
```math
S_{\rm shape}:=\sum_r(p_r-2d_r),\qquad
S_{\rm out}:=\sum_r(L_r-2d_r),
```
and
```math
X_D:=q-k-\sum_r d_r,\qquad k=d_H+s_Z.
```

Then
```math
\boxed{\liminf_{D\to\infty}{S_{\rm shape}\over D}\ge\pi-2.}
\tag{1.1}
```
Since $`L_r\ge p_r`$,
```math
\boxed{\liminf_{D\to\infty}{S_{\rm out}\over D}\ge\pi-2.}
\tag{1.2}
```

Current main proves
```math
S_{\rm out}\le2X_D+4c_I-4-Q_{\rm loc},
\tag{1.3}
```
with $`c_I=o(D)`$ and $`Q_{\rm loc}\ge0`$. Hence
```math
\boxed{
\liminf_{D\to\infty}{X_D\over D}
\ge{\pi-2\over2}
={\pi\over2}-1
=0.5707963267\ldots .
}
\tag{1.4}
```
This replaces the previous proof-only floor
$`0.0905130297\ldots`$.

Also $`q-k\le q\le\operatorname{per}(F)\le\pi D`$, so
```math
\boxed{
\limsup_{D\to\infty}{1\over D}\sum_r d_r
\le{\pi\over2}+1
=2.5707963267\ldots .
}
\tag{1.5}
```

No computation is used below.

## 2. Shape excess under cyclic chord cuts

For a compact planar convex body $`K`$, write
```math
E(K):=\operatorname{per}(K)-2\operatorname{diam}(K)\ge0.
\tag{2.1}
```

### Lemma 2.1
Let a cyclic convex polygon $`P`$, inscribed in a circle of radius $`R`$, be cut
by a chord $`ab`$ of length $`c`$ into cyclic polygons $`P_1,P_2`$. Then
```math
E(P_1)+E(P_2)\ge E(P).
\tag{2.2}
```

### Proof
The two circle arcs from $`a`$ to $`b`$ have total angular length $`2\pi`$.
One has angular length at most $`\pi`$. The subpolygon supported on that arc has
diameter at most $`c`$, since chord length is increasing with angular separation
on an arc of length at most $`\pi`$. The other subpolygon is contained in $`P`$,
so its diameter is at most $`d:=\operatorname{diam}(P)`$. Thus
```math
\operatorname{diam}(P_1)+\operatorname{diam}(P_2)\le c+d.
```
Also
```math
\operatorname{per}(P_1)+\operatorname{per}(P_2)
=\operatorname{per}(P)+2c.
```
Subtract twice the first inequality from the second. $`\square`$

Iterating over any finite noncrossing chordal partition of a cyclic polygon gives
```math
\boxed{\sum_jE(Q_j)\ge E(P).}
\tag{2.3}
```

## 3. Sharp area upper bound for cyclic shape excess

### Lemma 3.1
If $`T`$ is a triangle inscribed in a circle of radius $`R`$, then
```math
\boxed{E(T)\le {4\over3R}\operatorname{area}(T).}
\tag{3.1}
```
Equality holds for the equilateral triangle.

### Proof
Let $`A,B,C`$ be the angles with $`C\ge A,B`$, so the side opposite $`C`$ is
the longest. By the sine rule,
```math
E(T)=2R(\sin A+\sin B-\sin C).
```
Since $`C=\pi-A-B`$,
```math
\sin A+\sin B-\sin(A+B)
=
4\sin{A\over2}\sin{B\over2}\sin{A+B\over2}.
\tag{3.2}
```
Put $`x=A/2,\ y=B/2`$. The inequalities $`A\le C`$ and $`B\le C`$ are
```math
2x+y\le{\pi\over2},\qquad x+2y\le{\pi\over2}.
\tag{3.3}
```
On this compact convex quadrilateral,
```math
f(x,y)=\log\cos x+\log\cos y+\log\cos(x+y)
```
is concave, so its minimum is attained at a vertex. The vertices are
```math
(0,0),\quad(\pi/4,0),\quad(\pi/6,\pi/6),\quad(0,\pi/4),
```
where
```math
\cos x\cos y\cos(x+y)=1,\ {1\over2},\ {3\over8},\ {1\over2}.
```
Therefore
```math
\cos{A\over2}\cos{B\over2}\cos{A+B\over2}\ge{3\over8}.
\tag{3.4}
```
Using
```math
\operatorname{area}(T)=2R^2\sin A\sin B\sin C,
```
inequality (3.1) is exactly (3.4). $`\square`$

### Lemma 3.2
If $`K`$ is the convex hull of a compact subset of a circle of radius $`R`$, then
```math
\boxed{E(K)\le {4\over3R}\operatorname{area}(K).}
\tag{3.5}
```

### Proof
For a cyclic polygon, triangulate using its vertices. By (2.3),
```math
E(K)\le\sum_TE(T)
\le {4\over3R}\sum_T\operatorname{area}(T)
={4\over3R}\operatorname{area}(K).
```
For a compact circle support, approximate by finite support subsets and pass to the
Hausdorff limit. Area, perimeter, and diameter are continuous for planar compact
convex bodies. $`\square`$

## 4. Nearly filling circle-supported cells

### Lemma 4.1
Let $`K_1,\ldots,K_m`$ be compact convex bodies with pairwise disjoint interiors,
each the convex hull of a compact subset of the same radius-$`R`$ circle. Put
```math
H=\operatorname{conv}\Bigl(\bigcup_iK_i\Bigr).
```
Then
```math
\boxed{
\sum_iE(K_i)
\ge E(H)
-{4\over3R}
\left(\operatorname{area}(H)-\sum_i\operatorname{area}(K_i)\right).
}
\tag{4.1}
```

### Proof
First take finite circle supports. The cell boundary chords have no proper
crossings because the cell interiors are disjoint. Include the cyclic boundary of
$`H`$. The resulting finite outerplanar straight-line graph is connected and its
cell interiors are faces. Triangulate only the other faces by adding noncrossing
chords. This gives a chordal subdivision of $`H`$ whose pieces are the $`K_i`$
and cyclic complement polygons $`Q_j`$.

By the iterated chord-cut inequality (2.3),
```math
\sum_iE(K_i)+\sum_jE(Q_j)\ge E(H).
```
Lemma 3.2 gives
```math
\sum_jE(Q_j)
\le {4\over3R}\sum_j\operatorname{area}(Q_j)
=
{4\over3R}
\left(\operatorname{area}(H)-\sum_i\operatorname{area}(K_i)\right).
```
Subtract. General compact supports follow by simultaneous finite-support
approximation inside each $`K_i`$ and Hausdorff continuity. $`\square`$

Let $`B=B(0,1/2)`$. By compactness there is a modulus
$`\omega(\delta)\to0`$ as $`\delta\downarrow0`$ such that every convex
$`H\subset B`$ with
```math
\operatorname{area}(H)\ge{\pi\over4}-\delta
```
satisfies
```math
E(H)\ge\pi-2-\omega(\delta).
\tag{4.2}
```
Indeed, otherwise a Blaschke-convergent countersequence would limit to a convex
subset of $`B`$ with full disk area, hence to $`B`$, contradicting continuity of
perimeter and diameter.

Therefore any family as in Lemma 4.1 with $`R=1/2`$ and
```math
\sum_i\operatorname{area}(K_i)\ge{\pi\over4}-\delta
```
obeys
```math
\boxed{
\sum_iE(K_i)
\ge\pi-2-\omega(\delta)-{8\over3}\delta.
}
\tag{4.3}
```

## 5. Apply the filling lemma to harmonic cells

Translate by the canonical Type-II near-disk center and scale by $`D`$.
Canonical full-core near-disk convergence gives
```math
D^{-1}F\to B(0,1/2).
\tag{5.1}
```
Canonical harmonic-cell tiling gives pairwise interior-disjoint cells and
```math
\sum_r\operatorname{area}(P_r)
={\pi\over4}D^2-o(D^2),
\tag{5.2}
```
together with
```math
\sum_r\sqrt{\operatorname{area}(P_r)}=O(D).
\tag{5.3}
```

Fix $`\eta>0`$ and retain
```math
\mathcal M_\eta(D)
=\{r:\operatorname{area}(P_r)\ge\eta D^2\}.
```
There are uniformly finitely many such cells. From (5.3), for one constant
$`C_{\rm cell}`$ independent of $`\eta`$,
```math
\sum_{r\notin\mathcal M_\eta(D)}
\operatorname{area}(P_r)
\le C_{\rm cell}\sqrt\eta\,D^2.
\tag{5.4}
```
Hence
```math
\sum_{r\in\mathcal M_\eta(D)}
{\operatorname{area}(P_r)\over D^2}
\ge{\pi\over4}-C_{\rm cell}\sqrt\eta-o(1).
\tag{5.5}
```

Pass to a subsequence and relabel the bounded retained family so that
```math
D^{-1}P_{r,D}\to K_r.
\tag{5.6}
```
The canonical harmonic-wrapping compactness argument gives simultaneous attachment
limits
```math
K_r=\operatorname{conv}(S_r),\qquad S_r\subset\partial B(0,1/2).
\tag{5.7}
```
The positive $`\eta`$-area floor preserves nonempty interiors, and cell-interior
disjointness passes to the limits.

Area, perimeter, and diameter are continuous in (5.6), so by (4.3),
```math
\begin{aligned}
\liminf_{D\to\infty}{S_{\rm shape}\over D}
&\ge
\sum_{r\in\mathcal M_\eta}
E(K_r)\\
&\ge
\pi-2
-\omega(C_{\rm cell}\sqrt\eta)
-{8C_{\rm cell}\over3}\sqrt\eta.
\end{aligned}
\tag{5.8}
```
Let $`\eta\downarrow0`$. This proves (1.1).

The small-cell tail is discarded only after using the elementary nonnegativity
$`p_r-2d_r\ge0`$. No finite harmonic cell is asserted to lie on an exact circle;
exact cyclic geometry is used only for the canonical macroscopic near-disk limits.

## 6. Current-main consequence

For each harmonic component the convex hull of the occurrence-counted outer walk is
$`P_r`$, hence $`L_r\ge p_r`$. Thus (1.1) implies (1.2).

Current main gives
```math
S_{\rm out}
\le2X_D+4c_I-4-Q_{\rm loc}.
```
With $`c_I=o(D)`$ and $`Q_{\rm loc}\ge0`$, division by $`D`$ and (1.2) give
```math
\liminf {X_D\over D}\ge{\pi-2\over2}.
```
Finally
```math
\sum_r d_r=q-k-X_D\le\pi D-X_D,
```
which gives (1.5).

## 7. Remaining bottleneck

This does not close C-II. It moves the full-core obstruction sharply.

Every surviving full-core sequence must now satisfy
```math
q-k-\sum_r d_r
\ge\left({\pi\over2}-1-o(1)\right)D
\tag{7.1}
```
and
```math
\sum_r d_r
\le\left({\pi\over2}+1+o(1)\right)D.
\tag{7.2}
```

Using the exact proof-only component remainder identity
```math
G_D=m+2+X_D,
```
the same theorem forces
```math
G_D-m\ge\left({\pi\over2}-1-o(1)\right)D.
\tag{7.3}
```

The next closing target is to show that the loaded-hull/diameter topology cannot
supply this $`0.570796D`$ remainder gap, or to turn the forced global chordal
shape excess into a source-preserving strict diameter decrease or an exact unit
equilateral triangle.

The separate macroscopic inactive-container branch is untouched.

## 8. Scope

- Remote `main` was rechecked immediately before the branch write.
- Dependencies: canonical C-FULLCORE-NEAR-DISK, C-HARMONIC-CELL-TILING,
  the C-HARMONIC-WRAPPING circle-support compactness step, component
  deatomization, and the current-main global outer-detour upper bound.
- No Section-122 return floor is used.
- No exceptional-face local/global identification is used.
- Contact-isolated source points remain retained.
- No full-source extension of the core affine-kernel theorem is used.
- No rejected Euler-path, FB4, Reuleaux-cap, or Section-121 scaling inference is used.
- No verifier or numerical search is load-bearing.
- The theorem-state manifest is unchanged.

**Classification:** unreviewed candidate; C-II and Level I remain open.
