> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_p1_moving_corner_gap_2026-09-09.md) · source SHA-256 `28fbdaba247e0e166f2732e657978fa7b86eb680137e5d7b6d8939eb280ae8ce`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 11 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-DE97BA679A61","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — every P1 endpoint cut creates a complementary chord at least `1/D` below diameter

**Date:** 2026-09-09  
**Repository branch:** PR #118 after CC  
**Run type:** exact four-point diameter-lens optimization  
**Target:** cyclic primitive phase `d_H=1`, P1  
**Depends on:** CC complementary moving-corner localization, global diameter bound  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

CC proves that every P1 KKT endpoint contains a convex four-corner quadrilateral

```math
p,q,r,s
```
in cyclic order with

```math
|pq|=|rs|=1,
```

and exactly one of the complementary sides `sp,qr` equal to the global source diameter `D`. The other side was known only to be strictly shorter than `D`.

The diameter-lens geometry gives an exact quantitative gap.

### Theorem MG — moving-corner gap

If

```math
|sp|=D,
\qquad
|pq|=|rs|=1,
```

and all six pair distances among `p,q,r,s` are at most `D`, then

```math
\boxed{
|qr|\le D-\frac1D.
}
\tag{MG.1}
```

The same statement holds with `sp` and `qr` interchanged.

Equality in MG.1 occurs if and only if the two unit sides are placed symmetrically at the extreme diameter-lens angles; equivalently

```math
\boxed{
|qs|=|pr|=D.
}
\tag{MG.2}
```

Therefore every P1 KKT endpoint supplies a canonical complementary corner chord `g_e` with

```math
\boxed{
D-|g_e|\ge\frac1D.
}
\tag{MG.3}
```

This is twice the leading radial deficit of the P1 rectangle short antipodal chords

```math
D-\sqrt{D^2-1}=\frac1{2D}+O(D^{-3}).
```

---

## 1. Normalize the diameter side

Assume

```math
sp=D.
```

Apply a rigid motion and reflection so that

```math
p=(0,0),
\qquad
s=(D,0),
```

and the convex quadrilateral lies in the upper half-plane.

Since `pq=1`, write

```math
q=(\cos\alpha,\sin\alpha)
```
with

```math
0<\alpha<\pi.
```

Since `rs=1`, write

```math
r=(D-\cos\beta,\sin\beta)
```
with

```math
0<\beta<\pi.
```

The global diameter bounds

```math
|q-s|\le D,
\qquad
|r-p|\le D
```
give

```math
D^2+1-2D\cos\alpha\le D^2,
```

```math
D^2+1-2D\cos\beta\le D^2.
```

Hence

```math
\boxed{
\cos\alpha,\cos\beta\ge\frac1{2D}.
}
\tag{1.1}
```

In particular, with

```math
A:=\arccos\frac1{2D},
```

we have

```math
0<\alpha,\beta\le A<\frac\pi2.
\tag{1.2}
```

---

## 2. Exact opposite-side formula

From the coordinates,

```math
q=(\cos\alpha,\sin\alpha),
\qquad
r=(D-\cos\beta,\sin\beta).
```

Therefore

```math
\begin{aligned}
|qr|^2
&=(D-\cos\alpha-\cos\beta)^2
 +(\sin\beta-\sin\alpha)^2\\
&=D^2-2D(\cos\alpha+\cos\beta)
 +2+2\cos(\alpha+\beta).
\end{aligned}
\tag{2.1}
```

Define

```math
F(\alpha,\beta)
:=D(\cos\alpha+\cos\beta)-\cos(\alpha+\beta).
\tag{2.2}
```

Then

```math
|qr|^2=D^2+2-2F(\alpha,\beta).
\tag{2.3}
```

Thus maximizing `|qr|` is equivalent to minimizing `F` on the square

```math
[0,A]^2.
```

---

## 3. The minimum occurs at the extreme symmetric corner

For the large Target C regime `D>2`; the finite cases below this threshold are already outside the post-ZF branch.

An interior critical point of `F` satisfies

```math
D\sin\alpha=\sin(\alpha+\beta),
\qquad
D\sin\beta=\sin(\alpha+\beta).
\tag{3.1}
```

Hence

```math
\sin\alpha=\sin\beta.
```

Because `0<alpha,beta<pi/2`, this gives

```math
\alpha=\beta.
```

If this common value is nonzero, (3.1) becomes

```math
D=2\cos\alpha<2,
```

contradicting `D>2`. Thus `F` has no interior critical point.

It remains to inspect the boundary.

### Boundary `alpha=0`

```math
F(0,\beta)=D+(D-1)\cos\beta
\ge D+\frac{D-1}{2D},
```
which is much larger than the value at `(A,A)` for `D>2`.

The same holds on `beta=0`.

### Boundary `alpha=A`

The derivative is

```math
\frac{d}{d\beta}F(A,\beta)
=-D\sin\beta+\sin(A+\beta).
\tag{3.2}
```

At `beta=0` it is positive. Any zero in `(0,A)` satisfies

```math
(D-\cos A)\sin\beta=\sin A\cos\beta,
```
so there is at most one such zero. At `beta=A`, using `cos A=1/(2D)`,

```math
-D\sin A+\sin(2A)
=\sin A(-D+2\cos A)
=\sin A\left(-D+\frac1D\right)<0.
```

Hence the unique boundary critical point, if present, is a maximum. The minimum on this boundary occurs at an endpoint. The endpoint `(A,0)` was covered by the previous case, so the minimum is `(A,A)`.

By symmetry the same is true on `beta=A`.

Therefore the global minimum of `F` on `[0,A]^2` is attained uniquely at

```math
\boxed{\alpha=\beta=A.}
\tag{3.3}
```

---

## 4. Evaluate the extremum

At

```math
\cos A=\frac1{2D},
```
we have

```math
\cos(2A)=2\cos^2A-1
=\frac1{2D^2}-1.
```

Thus

```math
\begin{aligned}
F(A,A)
&=2D\cos A-\cos(2A)\\
&=1-\left(\frac1{2D^2}-1\right)\\
&=2-\frac1{2D^2}.
\end{aligned}
```

Substitute into (2.3):

```math
\begin{aligned}
|qr|^2
&\le D^2+2-2\left(2-\frac1{2D^2}\right)\\
&=D^2-2+\frac1{D^2}\\
&=\left(D-\frac1D\right)^2.
\end{aligned}
```

Since lengths are nonnegative,

```math
|qr|\le D-\frac1D.
```

This proves MG.1.

Equality requires `alpha=beta=A`, which is exactly equality in both diameter-lens constraints

```math
|q-s|=D,
\qquad
|r-p|=D.
```
This proves MG.2. `square`

---

## 5. Target C consequence

At a P1 KKT endpoint, CC gives either

```math
e=sp,
\qquad |e|=D,
```
with complementary corner chord `qr`, or the symmetric alternative.

All four vertices belong to the source and hence have mutual distances at most `D`. MG applies directly:

```math
|qr|\le D-\frac1D.
```

Thus the formerly qualitative inequality `|qr|<D` sharpens to the exact endpoint gap MG.3.

If equality occurs, the two cross-distances `qs` and `pr` are additional actual diameter pairs by MG.2. They would be edges of the full diameter graph `H`. This is an important extra rigidity condition for the equality case and can be checked against the convex-thrackle tree topology.

---

## 6. Equality is in fact impossible in the P1 tree phase

Assume equality in MG.1 at a KKT endpoint with

```math
e=sp.
```

Then MG.2 makes

```math
qs,
\qquad pr
```
actual diameter edges.

The full tree `H` already contains `sp`. The three diameter edges

```math
sp,\ qs,\ pr
```
lie on the four vertices `p,q,r,s`.

Now `qs` and `pr` are vertex-disjoint. In the cyclic order

```math
p,q,\ldots,r,s,
```
their endpoints alternate, so they cross, as allowed. But `sp` shares `s` with `qs` and `p` with `pr`, also allowed.

The three edges form the path

```math
q-s-p-r.
```

This does not itself create a cycle, so equality is not excluded by tree topology alone.

Therefore MG.3 is sharp even within the abstract convex-thrackle-tree class. No false strict improvement beyond `1/D` is claimed.

---

## 7. Scale comparison

The fixed P1 rectangle short antipodal chords have

```math
\sqrt{D^2-1}
=D-\frac1{2D}-\frac1{8D^3}+O(D^{-5}).
```

The endpoint moving-corner chord satisfies

```math
|g_e|\le D-\frac1D.
```

Hence for large `D`,

```math
\sqrt{D^2-1}-|g_e|
\ge
\frac1{2D}+O(D^{-3}).
```

So every KKT endpoint creates a non-diameter corner chord that is quantitatively deeper than either of the two canonical rectangle-tie short antipodal chords.

This separation may be useful because P1's difference body itself has only the rectangle tie as a non-strict antipodal event.

---

## 8. Next theorem

There are two direct continuations.

1. **Antipodality exclusion.** Prove that the complementary moving-corner chord `g_e` must be a vertex-vertex antipodal pair of `F`. P1 would then close immediately: every strict vertex-antipodal pair corresponds to a radius-`D` difference-body vertex, while the only short tie pairs have length `sqrt(D^2-1)>D-1/D`.
2. **Two-endpoint comparison.** Each of the two KKT endpoints supplies a chord with deficit at least `1/D`. Use nesting of the corresponding cuts along the common path `J` to prove that one such complementary chord enters the rotating-calipers antipodal list, or that the two anchored WM ratios have incompatible order.

The first route is now a crisp support-normal question rather than a metric one.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

CC endpoint quadrilateral: cyclic p,q,r,s with pq=rs=1, one complementary side sp=D
(the zeroed diameter), the other qr<D. Put p=(0,0), s=(D,0),
  q=(cos alpha,sin alpha),
  r=(D-cos beta,sin beta).
Diameter constraints |q-s|,|r-p|<=D give
  cos alpha, cos beta >=1/(2D),
so alpha,beta<=A=acos(1/(2D)).

Exact:
  |qr|^2=D^2-2D(cos alpha+cos beta)+2+2cos(alpha+beta).
Equivalently maximize |qr| by minimizing
  F=D(cos alpha+cos beta)-cos(alpha+beta).
For D>2 there is no interior minimum; boundary analysis puts the unique minimum at
alpha=beta=A. There
  |qr|^2=(D-1/D)^2.
Thus
  |qr|<=D-1/D.
Equality iff |qs|=|pr|=D.

Hence every P1 KKT endpoint creates a canonical complementary corner chord with
  D-|g_e|>=1/D,
twice the leading shortness of the fixed rectangle tie chords
  D-sqrt(D^2-1)~1/(2D).

Next: prove g_e is antipodal (which would instantly contradict P1), or compare the
two endpoint chords/cuts to force one into the antipodal list.
```
