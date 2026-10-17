> Generated reading edition · [exact source](../../../docs/reports/target_c_forest_double_diameter_gap_2026-09-11.md) · source SHA-256 `ea8aff531118fa3401df43d7aa06e23c5d6cd0b8df91fe23554fbf1b61cbc8d9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-278B52705132","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — doubled direction gaps force outer-walk excess in the forest circuit branch

**Date:** 2026-09-11  
**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact convex-geometric sharpening / forest branch theorem  
**Target:** Target C C-II, post-ZF `s_Z=0` forest diameter topology  
**Depends on:** C65/C67 diameter visibility and convex-thrackle order, DB difference-body perimeter, ZT/ZE circuit identities, Woodall diameter topology  
**Computation:** none used in the proof

## LEVEL I STATUS

`STILL OPEN`.

This report proves a metric strengthening of C67 that is specific to **vertex-disjoint** diameter pairs. If two actual diameter chords do not share an endpoint, their projective directions are separated by twice the C67 minimum:

```math
\boxed{\theta\ge 4a_D,\qquad a_D:=\arcsin\frac1{2D}.}
```

The factor two is sharp for the underlying equal-diagonal diameter geometry.

Combining this with the cyclic ordering of all diameter directions gives a new forest-side perimeter theorem. Let `H` be the full actual diameter graph on `q` loaded vertices, with `h` edges and

```math
d_H=q-h>0.
```

Except for the one-center star graph, at least `d_H` consecutive projective direction gaps come from vertex-disjoint diameter edges and therefore have size at least `4a_D`; every other gap is at least `2a_D`. Consequently

```math
\boxed{
\operatorname{per}F
\ge h-d_H+2(d_H-1)\cos a_D
 +2D\cos\bigl((q-2)a_D\bigr).
}
\tag{DG.1}
```

For sufficiently large post-ZF survivors the star exception is impossible by the already proved DB lower bound `h/D>=2rho+o(1)` versus the elementary star bound `h/D<=pi/3+o(1)`.

In the exact circuit phase `s_Z=0`, where `b=q+x_B` and `per(F)<=b`, DG.1 gives

```math
\boxed{
x_B
\ge
2D\cos\bigl((q-2)a_D\bigr)
-2-2(d_H-1)(1-\cos a_D).
}
\tag{DG.2}
```

Thus along any unbounded forest sequence with `q/D->x`,

```math
\boxed{
\liminf {x_B\over D}\ge2\cos(x/2).
}
\tag{DG.3}
```

In particular, for every fixed `eta>0`, if `q/D<=pi-eta` along a subsequence then

```math
\liminf {x_B\over D}\ge2\sin(\eta/2)>0.
\tag{DG.4}
```

This is stronger than the existing statement that only the combined branching currency `x_B+Q=2h-q` is linear. Away from the near-maximal terminal-perimeter regime `q/D->pi`, the forest branch must pay linear **outer-walk excess itself**; the mandatory defect cannot be hidden entirely in bounded exceptional faces.

No contradiction with C-II is obtained. The remaining near-maximal regime `q/D->pi` is still compatible with `x_B=o(D)` and a linear exceptional-face budget, so a new stability or source-capacity input is still required.

---

## 1. A sharp equal-diagonal metric lemma

The new geometric input does not use KKT stress.

### Lemma DG.1 — two diameter segments with distinct endpoints

Let `AB` and `CD` be two distinct segments of common length `D` in a planar set of diameter at most `D`. Let `theta in (0,pi/2]` be the acute projective angle between their supporting lines. Then

```math
\boxed{
\min\{|A-C|,|A-D|,|B-C|,|B-D|\}
\le2D\sin(\theta/4).
}
\tag{1.1}
```

### Proof

Scale by `D` and place the midpoint of `AB` at the origin. Choose unit direction vectors `u,v` for the two segments so that the angle between them is `theta`. If `m` is the normalized displacement from the midpoint of `AB` to the midpoint of `CD`, then the four cross distances are the norms of

```math
m\pm {u-v\over2},
\qquad
m\pm {u+v\over2}.
```

Put

```math
w={u-v\over2},\qquad z={u+v\over2},
```
so `w perpendicular z`,

```math
|w|=s:=\sin(\theta/2),
\qquad
|z|=c:=\cos(\theta/2).
```

Write

```math
m=\alpha \widehat w+\beta\widehat z.
```

All cross distances are at most one because the whole set has diameter at most one. In particular

```math
|m+z|\le1,
\qquad
|m-z|\le1.
```

Therefore

```math
\alpha^2+(|\beta|+c)^2\le1.
\tag{1.2}
```

It follows that `|alpha|<=s` and

```math
|\beta|\le\sqrt{1-\alpha^2}-c.
\tag{1.3}
```

The smaller of the other two cross distances satisfies

```math
\min\{|m+w|^2,|m-w|^2\}
=(s-|\alpha|)^2+\beta^2.
\tag{1.4}
```

Set `|alpha|=sin phi`. Since `0<=|alpha|<=s` and `theta<=pi/2`, we have `0<=phi<=theta/2`. Using (1.3),

```math
\begin{aligned}
(s-|\alpha|)^2+\beta^2
&\le (s-\sin\phi)^2+(\cos\phi-c)^2\\
&=2-2\bigl(s\sin\phi+c\cos\phi\bigr)\\
&=2-2\cos(\theta/2-\phi)\\
&\le2-2\cos(\theta/2)\\
&=4\sin^2(\theta/4).
\end{aligned}
```

Taking square roots and restoring the factor `D` proves (1.1). `square`

### Sharpness

Equality is possible in the metric optimization. Take `alpha=0`, `|beta|=1-c`; then one pair `m+-z` reaches the diameter bound and the smaller pair `m+-w` has length exactly `2sin(theta/4)` after normalization. Thus the factor `2sin(theta/4)` cannot be uniformly reduced under only the equal-diagonal and diameter hypotheses.

---

## 2. Disjoint actual diameter edges have a doubled projective gap

Assume now that the source is unit-separated. For two actual diameter edges with four distinct endpoints, every cross distance is at least one. Lemma DG.1 therefore gives

```math
1\le2D\sin(\theta/4).
```

Hence, whenever `4a_D<=pi/2` (in particular for all sufficiently large `D`),

```math
\boxed{\theta\ge4a_D.}
\tag{2.1}
```

For comparison, if two diameter edges share an endpoint, their two other endpoints are unit-separated, so the elementary isosceles-triangle estimate gives only

```math
\boxed{\theta\ge2a_D.}
\tag{2.2}
```

C67 already provides (2.2) for all distinct projective diameter directions. The content of (2.1) is the exact factor-two improvement for vertex-disjoint pairs.

The full actual diameter graph is a convex geometric thrackle, so two vertex-disjoint diameter edges cross. The proof above actually needs only the common-diameter and pairwise-distance bounds, but the thrackle property identifies exactly which consecutive direction pairs are disjoint in the application below.

---

## 3. At least `d_H` cyclic direction adjacencies are disjoint

Order the `h` projective diameter directions cyclically as

```math
e_1,e_2,\ldots,e_h
```

and let `N_sh` be the number of cyclic consecutive pairs `(e_i,e_{i+1})` that share a vertex.

Assume `H` is not a star centered at one vertex. For a vertex `v`, the set of positions occupied by edges incident to `v` is then a proper subset of the `h` cyclic positions. If `deg_H(v)=d_v`, at most `d_v-1` cyclic adjacencies can have both members incident to `v`.

Two distinct simple edges share at most one endpoint, so summing over vertices does not double-count a shared adjacency. Since every loaded vertex has positive diameter degree,

```math
\begin{aligned}
N_{sh}
&\le\sum_v(d_v-1)\\
&=2h-q.
\end{aligned}
\tag{3.1}
```

Therefore the number `N_dis` of consecutive pairs with disjoint endpoints obeys

```math
\boxed{
N_{dis}=h-N_{sh}\ge q-h=d_H.
}
\tag{3.2}
```

This bound is combinatorially sharp for caterpillar forests: their line graphs can realize long consecutive shared-edge runs. The gain below comes from the larger metric gap on the unavoidable `d_H` breaks, not from claiming extra breaks that Woodall does not supply.

---

## 4. Heterogeneous difference-body perimeter bound

Let the cyclic projective gaps be `g_1,...,g_h`, with sum `pi`. By Section 2 every gap is at least `2a_D`, and by (3.2) at least `d_H` gaps are at least `4a_D`.

For the weakest lower bound, downgrade all but `d_H` of the doubled gaps to the lower value `2a_D`. The function

```math
f(g)=\sin(g/2)
```

is concave on `[0,pi]`. Under lower bounds and a fixed total sum, its sum is minimized at an extreme point: all but one gap are at their lower bounds.

Because `d_H>=1`, the free gap can be chosen among the `4a_D`-lower-bound coordinates. This gives the smaller extreme value. Indeed, writing `a=a_D` and using feasibility `2aq<=pi`, the difference between putting the free coordinate on a `2a` gap and on a `4a` gap is

```math
2\sin(a/2)
\left[
\cos(3a/2)-\sin\bigl(a(q-3/2)\bigr)
\right]\ge0.
```

Hence

```math
\boxed{
\sum_{i=1}^h\sin(g_i/2)
\ge
(h-d_H)\sin a_D
+(d_H-1)\sin(2a_D)
+\cos\bigl((q-2)a_D\bigr).
}
\tag{4.1}
```

As in DB, define

```math
P_H=D\,\operatorname{conv}\{\pm u_e:e\in E(H)\}.
```

Then `P_H subset F-F`, so Cauchy perimeter monotonicity and Minkowski additivity give

```math
\operatorname{per}F
\ge2D\sum_i\sin(g_i/2).
\tag{4.2}
```

Use

```math
\sin a_D={1\over2D},
\qquad
2D\sin(2a_D)=2\cos a_D.
```

Equations (4.1)--(4.2) yield DG.1:

```math
\boxed{
\operatorname{per}F
\ge h-d_H+2(d_H-1)\cos a_D
+2D\cos\bigl((q-2)a_D\bigr).
}
```

When `d_H/D->d` and `q/D->x`, this becomes

```math
\liminf {\operatorname{per}F\over D}
\ge x+2\cos(x/2).
\tag{4.3}
```

The cancellation of `d` in the first-order term is not accidental: each unavoidable disjoint direction adjacency spends one additional `2a_D` gap, exactly matching the one additional terminal represented by `q-h=d_H`.

---

## 5. The star exception is absent in sufficiently large post-ZF survivors

Suppose `H` is a star with `h` leaves around center `b`. Every leaf lies at distance `D` from `b`, and every pair of leaves is at distance at most `D`. Their rays from `b` therefore lie in an angular arc of width at most `pi/3`.

Unit separation of the leaves gives consecutive angular separation at least `2a_D`. Hence

```math
(h-1)2a_D\le\pi/3,
```
so

```math
\boxed{h\le1+{\pi\over6a_D}.}
\tag{5.1}
```

Therefore

```math
\limsup h/D\le\pi/3=1.04719\ldots .
\tag{5.2}
```

The already proved DB theorem gives every post-ZF survivor

```math
\liminf h/D\ge2\rho=1.47817\ldots,
\qquad \rho=\cos\rho.
```

Thus the full actual diameter graph is not a star for all sufficiently large post-ZF survivors. The exception in Section 3 does not survive in the intended asymptotic branch.

---

## 6. Forest circuit consequence: linear outer-walk excess

Now assume the exact post-ZF circuit branch

```math
s_Z=0,
\qquad d_H=q-h>0.
```

Woodall identifies this as the caterpillar-forest branch. ZE gives

```math
b+Q=2h,
```
while by definition of outer-walk excess

```math
b=q+x_B.
```

The closed outer contact walk has convex hull `F`, hence

```math
\operatorname{per}F\le b=q+x_B.
\tag{6.1}
```

Combine (6.1) with DG.1 and use `h=q-d_H`:

```math
q+x_B
\ge q-2d_H+2(d_H-1)\cos a_D
+2D\cos((q-2)a_D).
```

Rearranging gives the exact finite estimate DG.2:

```math
\boxed{
x_B
\ge
2D\cos((q-2)a_D)
-2-2(d_H-1)(1-\cos a_D).
}
```

Since `d_H=O(D)`,

```math
(d_H-1)(1-\cos a_D)=O(D^{-1}).
```

Also `a_D=1/(2D)+O(D^{-3})`. Therefore, along any convergent unbounded sequence with `q/D->x`,

```math
\boxed{
\liminf {x_B\over D}\ge2\cos(x/2).
}
```

The heterogeneous gap feasibility itself gives `x<=pi`. If `x<=pi-eta`, then

```math
2\cos(x/2)\ge2\cos((\pi-\eta)/2)=2\sin(\eta/2),
```
proving DG.4.

Using the exact circuit branching identity

```math
x_B+Q=2h-q,
```
DG.3 can equivalently be written as the exceptional-face restriction

```math
\limsup {Q\over D}
\le
\lim {2h-q\over D}-2\cos(x/2)
```
whenever the displayed limits exist.

---

## 7. Interaction with the current forest frontier

The current `s_Z=0` theorem uses

```math
\nu_D={e_{BB}+2s_C-3d_H\over D}
```

and proves `nu_D>0.597+o(1)`. DG does not improve that scalar floor by itself: the new currency is `x_B`, and DD's outer-pocket upper bound is increasing rather than decreasing in `x_B+a`.

What DG does remove is a previously live allocation pattern. A forest survivor with terminal density bounded away from `pi` cannot have

```math
x_B=o(D),\qquad Q=\Theta(D).
```

Thus a future forest closure may split cleanly into:

1. `q/D<=pi-eta`: DG supplies a fixed linear outer-walk-excess floor;
2. `q/D->pi`: unit-separated loaded vertices and `per(F)<=q+x_B` force a near-maximal-perimeter force hull whenever `x_B=o(D)`, so a Bonnesen/disk-stability plus diameter-branching argument is the relevant remaining target.

The second branch is not closed here. In particular, the theorem does not infer that near-maximal perimeter makes the diameter graph a matching; FS.3/FS.4 allow many near-antipodal partners with vanishing angular spread, and no individual KKT weight floor is available.

---

## 8. Regression audit

- **Regular odd shell:** has `d_H=0` and `s_Z=2`; the forest consequence does not apply.
- **Perfect matching / even near-circle:** has `d_H` linear and can have `q/D->pi`; DG.3 then permits `x_B/D->0` because the cosine term vanishes. This is necessary and shows why DG alone cannot close the near-maximal-perimeter endpoint.
- **Star diameter graph:** is the unique combinatorial exception to `N_sh<=2h-q`; Section 5 excludes it asymptotically in the post-ZF branch.
- **Caterpillar with long shared-edge runs:** allowed. Section 3 uses only the guaranteed `d_H` disjoint cyclic adjacencies and does not assume more.
- **Repeated outer-walk edges/contact bridges:** harmless. The only use of the outer contact walk is the valid geometric inequality `per(F)<=b` with occurrences counted in `b`.
- **Contact-isolated source points:** retained. DG concerns the actual loaded force hull and does not replace the full source or assume force-hull saturation.
- **No extension to `s_Z>0`:** DG.1 is geometric and survives, but DG.2 uses the exact circuit perimeter identity. No `s_Z>0` conclusion is asserted.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| equal-diagonal bound (1.1) | proved | midpoint orthogonal decomposition |
| disjoint diameter gap `>=4a_D` | proved for sufficiently large `D` | unit separation + (1.1) |
| at least `d_H` disjoint cyclic adjacencies | proved for nonstar `H` | cyclic incidence count |
| forest perimeter DG.1 | proved | heterogeneous concave gap minimization + difference body |
| star absent asymptotically post-ZF | proved | elementary star packing vs DB |
| outer-excess DG.2-DG.4 | proved in `s_Z=0` forest branch | `per(F)<=b=q+x_B` |
| forest C-II contradiction | not proved | `q/D->pi` endpoint survives |
| Level I | still open | cyclic, forest near-maximal-perimeter, and `s_Z>0` branches remain |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New metric lemma:
For two distinct diameter segments AB,CD of length D in a diameter-D set,
if theta is their acute projective angle then
    min cross-distance <= 2D sin(theta/4).
Hence four distinct endpoints in a unit-separated source imply
    theta >= 4 asin(1/(2D)).
Shared-endpoint diameter pairs only force the old 2 asin(1/(2D)) gap.

Order all h diameter directions cyclically. If H is not a star, at most
    sum_v(deg_H(v)-1)=2h-q
consecutive pairs can share a vertex. Therefore at least
    q-h=d_H
consecutive gaps are disjoint and have the doubled lower bound.

Concave minimization of the difference-body perimeter then gives
    per(F) >= h-d_H + 2(d_H-1)cos(a_D)
              +2D cos((q-2)a_D).

The star exception has h/D<=pi/3+o(1), contradicting DB's post-ZF
h/D>=2rho+o(1), so it is absent for sufficiently large survivors.

In the s_Z=0 forest branch, per(F)<=b=q+x_B yields
    x_B >= 2D cos((q-2)a_D)
           -2-2(d_H-1)(1-cos a_D).
Thus if q/D->x,
    liminf x_B/D >= 2 cos(x/2).
In particular q/D<=pi-eta forces x_B/D>=2 sin(eta/2)+o(1).

This removes the allocation pattern where a forest with terminal density bounded
away from pi pays all mandatory linear branching through exceptional faces while
x_B=o(D). The unresolved forest endpoint is q/D->pi; DG alone does not exclude it.
```
