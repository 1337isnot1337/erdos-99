> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_surplus_triangulation_exclusion_2026-09-09.md) · source SHA-256 `cca3240e32484f054dbb3b3279f33f41bd69e6b5a9408966568f5397e985bbb2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6A622B21A2E9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact zero-surplus triangulation exclusion

**Date:** 2026-09-09  
**Repository base:** current post-ZF research branch  
**Run type:** exact structural closure of one post-ZF subbranch  
**Target:** Target C Gate C-II / Level I  
**LEVEL I STATUS:** STILL OPEN

This report closes one exact post-ZF subbranch.

Assume the audited report-level ZR/ZF/ZS state and the exact post-ZF ledgers. If the
contact core has an unloaded component and

```math
e_{BB}=s_C=0,
```

then the C37 incidence inequalities are all at equality. More importantly, C49.1
supplies the geometric fact needed to use that equality safely: the attachment cells
`P_r=conv(A_r)` have pairwise disjoint interiors. The post-ZF ledger forces exactly
`q-2` such cells and exactly three loaded vertices in each cell. A maximal-family
argument for noncrossing triangles on `q` convex vertices then shows that these cells
form a triangulation of the force hull.

The component-diameter ledger leaves only six units of total internal graph diameter,
so the total area of those `q-2` triangles is `O(q)=O(D)`. This contradicts the
post-ZF force-hull area theorem, which gives

```math
\operatorname{area}(F)\ge
\left(\frac12\sin1-o(1)\right)D^2.
```

Thus the literal zero loaded-loaded/pinned-stress-surplus branch is impossible for all
sufficiently large post-ZF survivors.

## 1. Exact zero-surplus normal form

Put

```math
k:=d_H+s_Z.
```

Assume `c_I>0` and

```math
e_{BB}=s_C=0.
\tag{1.1}
```

The post-ZF incidence identity ZJ is

```math
s_C+r_Q=k+u_A+p_A+(s-1),
```

where every term is nonnegative. C38 gives `s>=1` and, under `e_BB=0`,

```math
s=1,\qquad q_{used}=q,\qquad r_Q=0.
```

Therefore

```math
\boxed{k=0,\qquad u_A=0,\qquad p_A=0.}
\tag{1.2}
```

ZU gives

```math
\boxed{c_I=q-2.}
\tag{1.3}
```

Since

```math
u_A=\sum_r(|A_r|-3)=0
```

and every `|A_r|>=3`,

```math
\boxed{|A_r|=3\quad\text{for every }r.}
\tag{1.4}
```

The sharpened component-slack ledger ZK gives

```math
\sum_r\delta_r+R_I+s_B+3k=6+e_{BB}+2s_C.
```

Hence in the present branch

```math
\boxed{\sum_r\delta_r\le6.}
\tag{1.5}
```

## 2. Geometric triangulation lemma

The earlier draft tried to obtain the triangulation from the abstract C37 equality
graph alone. That is stronger than necessary and leaves an avoidable embedding issue.
The correct proof uses the actual convex attachment cells.

C49.1 proves that for distinct unloaded components

```math
\boxed{
\operatorname{int}(P_r)\cap\operatorname{int}(P_s)=\varnothing,
\qquad P_r:=\operatorname{conv}(A_r).
}
\tag{2.1}
```

Its proof uses C36 noncrossing to exclude proper crossing and C37 to exclude
containment or three shared loaded attachments. This theorem applies without the old
`\sigma_B=o(D)` phase assumption.

Under (1.4), every `P_r` is a nondegenerate Euclidean triangle whose vertices belong
to the loaded set `B`. Every point of `B` is an extreme vertex of the convex force
hull `F`, so no loaded vertex lies in the interior of a triangle spanned by three
other loaded vertices.

### Lemma ZQ.1 — maximal disjoint triangular cells triangulate the force hull

Let `B` consist of `q>=3` vertices in strictly convex cyclic position. Let

```math
P_1,\ldots,P_{q-2}
```

be distinct nondegenerate triangles with vertices in `B` and pairwise disjoint
interiors. Then their union is a straight-line triangulation of `conv(B)`. In
particular,

```math
\boxed{
\operatorname{area}(\operatorname{conv}B)
=\sum_{r=1}^{q-2}\operatorname{area}(P_r).
}
\tag{2.2}
```

### Proof

Let `G_T` be the straight-line graph on `B` obtained by taking the union of all sides
of the triangles `P_r`.

No two edges of `G_T` cross properly. If two triangle sides crossed at an interior
point, the interiors of the two triangles would locally occupy two open half-planes
whose intersection contains a nonempty wedge, contradicting the disjoint-interior
hypothesis.

No edge of `G_T` passes through another loaded vertex, because every loaded point is
an extreme vertex of `conv(B)`. It follows that `G_T` is a simple outerplanar
straight-line graph on the cyclic vertex set `B`.

Each `P_r` is a bounded face of `G_T`. Indeed, no other loaded vertex lies in its
interior, and no edge of `G_T` can enter its interior without crossing one of its
three sides. The triangles are distinct because two equal triangles would have the
same nonempty interior, violating (2.1).

A simple outerplanar graph on `q` vertices has at most `q-2` bounded triangular
faces; equivalently, a triangulation of a convex `q`-gon has the maximal possible
`q-2`. Here `G_T` already has the `q-2` distinct bounded triangular faces `P_r`.
Therefore equality holds in the outerplanar Euler bound: `G_T` is connected and
maximal outerplanar, its outer boundary is the cyclic `q`-gon, and its bounded faces
are exactly the `P_r`. Hence the triangles partition `conv(B)`. `square`

Apply the lemma to the C49 cells. Since `conv(B)=F`,

```math
\boxed{
\operatorname{area}(F)
=\sum_r\operatorname{area}(P_r).
}
\tag{2.3}
```

This is the only triangulation statement used below.

## 3. Size of one attachment triangle

For two attachments `a,b in A_r`, choose their contact neighbors in `I_r` and join
those neighbors by a shortest path inside `I_r`. This gives a contact path from `a`
to `b` with at most `\delta_r+2` unit edges. Hence

```math
\boxed{
\operatorname{diam}(A_r)\le\delta_r+2.
}
\tag{3.1}
```

A planar triangle of diameter `L` has area at most

```math
\frac{\sqrt3}{4}L^2.
```

Therefore

```math
\boxed{
\operatorname{area}(P_r)
\le\frac{\sqrt3}{4}(\delta_r+2)^2.
}
\tag{3.2}
```

## 4. Theorem ZQ — exact zero-surplus branch is impossible

### Theorem ZQ

For every sufficiently large post-ZF C-II survivor with `c_I>0`,

```math
\boxed{e_{BB}+s_C>0.}
\tag{ZQ.1}
```

### Proof

Assume (1.1). From (2.3) and (3.2),

```math
\operatorname{area}(F)
\le\frac{\sqrt3}{4}
\sum_r(\delta_r+2)^2.
```

By (1.5),

```math
\sum_r\delta_r^2
\le\left(\sum_r\delta_r\right)^2
\le36.
```

Also `c_I=q-2`. Hence

```math
\begin{aligned}
\sum_r(\delta_r+2)^2
&=\sum_r\delta_r^2+4\sum_r\delta_r+4c_I\\
&\le36+24+4(q-2)\\
&=4q+52.
\end{aligned}
```

Thus

```math
\boxed{
\operatorname{area}(F)
\le\sqrt3\,q+13\sqrt3.
}
\tag{ZQ.2}
```

The loaded force-hull vertices are unit separated along a convex polygon of diameter
`D`, so

```math
q\le\operatorname{per}(F)\le\pi D.
```

Therefore

```math
\operatorname{area}(F)=O(D).
\tag{ZQ.3}
```

But the post-ZF area upgrade ZA inserts ZS's `h>=\lceil D\rceil` into C67's audited
projective-direction theorem and proves

```math
\boxed{
\liminf_{D\to\infty}
\frac{\operatorname{area}(F)}{D^2}
\ge\frac12\sin1>0.
}
\tag{ZQ.4}
```

Equations ZQ.3 and ZQ.4 contradict each other for all sufficiently large `D`. `square`

## 5. Boundary-only case

If `c_I=0`, ZU gives

```math
e_{BB}+s_C=q-2+k.
```

Post-ZF `q>=\lceil D\rceil`, so the combined surplus is already linear in `D`.
Thus the literal zero-surplus case is impossible there as well.

### Corollary ZQ.2

Every sufficiently large post-ZF survivor satisfies

```math
\boxed{e_{BB}+s_C\ge1.}
```

The important content is the excluded equality geometry, not the integer `1`.

## 6. What this closes and what it does not

ZQ closes exactly

```text
e_BB=0 and s_C=0.
```

It does not prove `e_BB+s_C=\Omega(D)`. A sublinear number of incidence defects may
border a geometrically macroscopic uncovered region. The subsequent gap theorem makes
that obstruction explicit: small `e_BB+2s_C` forces a quadratic attachment-cell area
gap, which in turn localizes to a macroscopic outer-face region or a linear-perimeter
exceptional face.

Thus the next stability target is no longer an abstract triangulation statement. It is
a macroscopic cavity/container theorem for the actual global minimizer.

## 7. Regression audit

- **Abstract C37 equality embeddings:** no longer used as a geometric classification.
  The proof now depends on C49.1's actual disjoint convex cells.
- **Regular odd shell:** `e_BB=q`, so it is outside the zero-surplus branch.
- **Unit square:** `e_BB=4`, outside the branch.
- **One large harmonic component:** ZU forces substantial `e_BB+s_C` when `q` is
  large.
- **Quadratic external rattler population:** irrelevant to ZQ; the contradiction uses
  only the force hull.

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| C49 attachment cells have disjoint interiors | canonical/proved input | C49.1. |
| `q-2` disjoint triangular cells triangulate `F` | proved here | Outerplanar maximal-face argument. |
| `area(F)<=sqrt(3)q+13sqrt(3)` | proved | ZK + contact-path diameter + triangle area. |
| exact zero-surplus branch excluded | proved | Linear upper area contradicts ZA quadratic lower area. |
| abstract C37 equality graph is always a radial graph | not needed / withdrawn | Avoids an unnecessary embedding claim. |
| `e_BB+s_C=Omega(D)` | not proved | Macroscopic cavity stability remains. |
| Level I | still open | Positive-surplus/cavity branches remain. |

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Assume post-ZF c_I>0 and e_BB=s_C=0.
Then ZJ/C38/ZU give
    k=d_H+s_Z=0,
    c_I=q-2,
    every |A_r|=3,
    q_used=q.
ZK gives
    sum delta_r<=6.

C49.1: the cells P_r=conv(A_r) have pairwise disjoint interiors.
There are q-2 distinct triangular cells on q convex loaded vertices. Their side union
is outerplanar; each cell is a bounded triangular face. An outerplanar q-vertex graph
has at most q-2 bounded triangular faces, so equality forces a triangulation of F.
Thus
    area(F)=sum area(P_r)
           <=(sqrt3/4)sum(delta_r+2)^2
           <=sqrt3 q+13sqrt3=O(D).

Post-ZF ZA gives
    liminf area(F)/D^2 >= (1/2)sin1 >0.
Contradiction.

Therefore the exact e_BB=s_C=0 branch is impossible for sufficiently large survivors.
```
