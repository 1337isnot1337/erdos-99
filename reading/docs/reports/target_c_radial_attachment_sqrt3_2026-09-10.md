> Generated reading edition · [exact source](../../../docs/reports/target_c_radial_attachment_sqrt3_2026-09-10.md) · source SHA-256 `e0aabc05c7199d97a043e75058b3c7ca87ec8024a0f8b77817bc354477324d8b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 9 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-C269D96679B9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — radial attachment geometry pushes the all-phase renormalized surplus past `sqrt(3)/2`

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910` after JS  
**Run type:** full-source radial geometry / attachment-cell sharpening  
**Target:** Target C, all post-ZF survivors  

## LEVEL I STATUS

`STILL OPEN`.

JS proves the explicit all-phase bound `mu_D>=0.857065...`.  Its attachment-cell
estimate still uses the ordinary planar isodiametric inequality, as if a large
attachment cell could be an arbitrary disk of diameter `delta_r`.

It cannot.  Every attachment vertex is a loaded diameter endpoint, and FS places all
such vertices at radius `D/2+o(D)` from one common full-source center.  A component
whose graph diameter is less than `(sqrt(3)/2)D` therefore has all its attachment
vertices in one short circular arc.  Its cell is a circular cap, not a free disk.

This yields:

### Theorem RA

There are absolute constants `epsilon_RA>0` and `D_0<infinity` such that every
post-ZF survivor with `D>=D_0` satisfies

```math
\boxed{
\mu_D
\ge
\frac{\sqrt3}{2}+\epsilon_{RA}.
}
\tag{RA.1}
```

In particular the explicit frontier jumps past

```math
\boxed{\sqrt3/2=0.8660254037844386\ldots .}
```

The positive gap `epsilon_RA` is nonexplicit here; the proof has a fixed area margin
at the limiting threshold.

---

## 1. Attachment-cell metric input

For an unloaded contact component `I_r`, let

```math
\delta_r=\operatorname{diam}_{C[I_r]}I_r
```

and let `A_r` be its distinct loaded attachment set.  If `a,b in A_r`, choose their
contact neighbors in `I_r` and a shortest contact path between those neighbors.  All
contact edges have length one, so

```math
\boxed{
|a-b|\le\delta_r+2.
}
\tag{1.1}
```

Thus

```math
\boxed{\operatorname{diam}(A_r)\le\delta_r+2.}
\tag{1.2}
```

FS.4 supplies one full-source center `o` and a uniform error `L_D=o(D)` such that every
loaded diameter endpoint satisfies

```math
\boxed{
\bigl||b-o|-D/2\bigr|\le L_D.
}
\tag{1.3}
```

Consequently every macroscopic attachment set, after scaling by `D` and taking a
subsequence, lies on the circle of radius `1/2` centered at the origin.

---

## 2. Circular arc lemma below the `120`-degree threshold

### Lemma RA.1

Let `S` be a finite subset of the circle of radius `1/2` centered at the origin and
assume

```math
\operatorname{diam}S\le z<\frac{\sqrt3}{2}.
```

Then `S` is contained in a circular arc of angle

```math
\theta=2\arcsin z<\frac{2\pi}{3}.
```

Hence

```math
\boxed{
\operatorname{area}(\operatorname{conv}S)
\le
B(z):=
\frac{\arcsin z-z\sqrt{1-z^2}}4.
}
\tag{RA.2}
```

### Proof

Suppose first that the origin belonged to `conv(S)`.  By planar Caratheodory, three
points of `S` would have a triangle containing the origin.  List their three cyclic
angular gaps.  A triangle containing the origin has every gap at most `pi`, and the
gaps sum to `2pi`; therefore at least one gap is at least `2pi/3`.  The corresponding
pair of radius-`1/2` points has distance at least

```math
2(1/2)\sin(\pi/3)=\frac{\sqrt3}{2},
```

contrary to the diameter hypothesis.

Thus the origin is outside `conv(S)`.  A line through the origin strictly separates it
from the compact convex polygon `conv(S)`, so all directions in `S` lie in one open
semicircle.  Inside a semicircle, angular separation is monotone with chord length.
The extreme directions therefore differ by at most

```math
2\arcsin z=\theta.
```

The convex hull of the entire radius-`1/2` circular arc of angle `theta` is the
corresponding circular segment.  Its area is

```math
\frac{(1/2)^2}{2}(\theta-\sin\theta)
=
\frac{\arcsin z-z\sqrt{1-z^2}}4.
```

This proves RA.2. `square`

The function `B` satisfies

```math
\boxed{
B'(z)=\frac{z^2}{2\sqrt{1-z^2}}>0
}
\tag{2.1}
```

and is convex on `(0,1)`.  Since `B(0)=0`, it is superadditive:

```math
B(x)+B(y)\le B(x+y)
\tag{2.2}
```

whenever `x,y>=0` and `x+y<1`.

---

## 3. Endpoint geometry at `z=sqrt(3)/2`

The preceding arc conclusion can fail exactly at

```math
z_0:=\sqrt3/2.
```

There is only one new limiting topology.

### Lemma RA.2

If `S` lies on the radius-`1/2` circle and

```math
\operatorname{diam}S\le\sqrt3/2,
```

then either

1. the origin is outside `conv(S)` and RA.2 holds with `z=z_0`; or
2. `conv(S)` is the equilateral triangle whose three vertices are separated by
   `120` degrees.

In particular

```math
\boxed{
\operatorname{area}(\operatorname{conv}S)
\le\frac{3\sqrt3}{16}.
}
\tag{RA.3}
```

### Proof

If the origin lies in `conv(S)`, the Caratheodory triangle used in Lemma RA.1 has all
three cyclic gaps at most `pi`, summing to `2pi`, while the chord bound forces every
minor angular separation to be at most `2pi/3`.  Hence all three gaps are exactly
`2pi/3`.  The three points form the stated equilateral triangle.

Any additional circle point would be more than `2pi/3` in minor angular distance from
at least one of the three equilateral directions, violating the chord bound.  Thus the
whole set is those three directions.  Its area at circumradius `1/2` is
`3sqrt(3)/16`. `square`

---

## 4. Sum over attachment cells

Let

```math
L_D^{att}:=\sum_r\delta_r.
```

The exact GR/ZK identity gives

```math
\boxed{
\sum_r\delta_r+R_I+s_B=\mu_DD+6,
}
\tag{4.1}
```

so

```math
\boxed{
\sum_r\delta_r\le\mu_DD+6.
}
\tag{4.2}
```

Consider an unbounded sequence with

```math
\mu_D\to\mu\le z_0.
```

Fix `eta>0`.  Components with `delta_r>=eta D` are finite in number, uniformly in
`D`.  After taking a subsequence, write their normalized graph diameters as `z_j`.
Equation (4.2) gives

```math
\sum_jz_j\le\mu.
\tag{4.3}
```

For each such component, (1.2)-(1.3) and Lemma RA.1 apply in the scaled limit whenever
`z_j<z_0`.  If every `z_j<z_0`, then

```math
\limsup\frac1{D^2}
\sum_{\delta_r\ge\eta D}
area(conv A_r)
\le
\sum_jB(z_j)
\le B\left(\sum_jz_j\right)
\le B(\mu).
\tag{4.4}
```

If `mu=z_0` and some `z_j=z_0`, it is the only positive macroscopic diameter in
(4.3); Lemma RA.2 gives instead

```math
\limsup\frac{C_{att}}{D^2}
\le\frac{3\sqrt3}{16}.
\tag{4.5}
```

It remains to dispose of the components with `delta_r<eta D`.  The ordinary
attachment-cell diameter bound and planar isodiametric inequality give

```math
area(conv A_r)\le\frac\pi4(\delta_r+2)^2.
```

Since `sum delta_r=O(D)` and `c_I=O(D)`, their total normalized area is `O(eta)+o(1)`.
Let `eta->0`.

Therefore every limiting state with `mu<=z_0` satisfies the uniform coarse bound

```math
\boxed{
\limsup\frac{C_{att}}{D^2}
\le\frac{3\sqrt3}{16}.
}
\tag{RA.4}
```

For `mu<z_0` the much stronger bound `B(mu)` holds; RA.4 is chosen only because it
also covers the endpoint topology.

---

## 5. Cavity plus attachment area cannot reach the force-hull floor

JS gives, after dropping the nonnegative side cost `C`,

```math
\boxed{
x:=\lim\frac{d_P+Q}{D}
\le\frac{2\mu+\pi}{3}.}
\tag{5.1}
```

RP paired-pocket capacity plus the exceptional-face estimate and ZG give

```math
\boxed{
\limsup\frac G{D^2}
\le\frac{x^2}{4\pi}
\le
\frac{(2\mu+\pi)^2}{36\pi}.
}
\tag{5.2}
```

For `mu<=sqrt(3)/2`, equations RA.4 and (5.2) give

```math
\limsup\frac{area(F)}{D^2}
\le
\frac{3\sqrt3}{16}
+
\frac{(\pi+\sqrt3)^2}{36\pi}.
\tag{5.3}
```

Use the elementary rational bounds

```math
\sqrt3<7/4,
\qquad
3<\pi<22/7.
```

Then

```math
\frac{3\sqrt3}{16}
+
\frac{(\pi+\sqrt3)^2}{36\pi}
<
\frac{21}{64}
+
\frac{11}{126}
+
\frac7{72}
+
\frac1{36}
=
\frac{2179}{4032}.
\tag{5.4}
```

The universal FSDB lower bound has the exact rational estimate already used in RP:

```math
\boxed{
\liminf\frac{area(F)}{D^2}
>
\frac{154451}{250000}.
}
\tag{5.5}
```

The fixed rational margin is

```math
\frac{154451}{250000}-\frac{2179}{4032}
=
\boxed{
\frac{4874777}{63000000}>0.0773.
}
\tag{5.6}
```

This contradicts (5.3).  Hence no subsequential survivor limit can satisfy

```math
\mu\le\sqrt3/2.
```

---

## 6. Uniform positive gap

The preceding contradiction has a fixed area margin at the endpoint.  Suppose there
were no `epsilon_RA>0` in RA.1.  Then one could choose post-ZF survivors with
`D_j->infinity` and

```math
\mu_{D_j}\downarrow\sqrt3/2.
```

The component-diameter measures have uniformly bounded total mass by (4.2).  Extract
the finitely many macroscopic components at each fixed scale and diagonalize.  Their
scaled attachment sets converge, after subsequences, to circle subsets satisfying the
endpoint chord bound of Lemma RA.2.  The small-component estimate remains `O(eta)`.
Thus RA.4 applies to the limiting sequence, and the same fixed margin (5.6)
contradicts FSDB.

Therefore some absolute `epsilon_RA>0` exists, proving RA.1.

---

## 7. Effect on the frontier

The explicit all-phase sequence of lower barriers is now

```math
0.5947
<0.7811
<0.8092
<0.834
<0.857
<\frac{\sqrt3}{2}=0.8660254\ldots,
```

and the `sqrt(3)/2` endpoint itself is excluded.

Unlike the preceding scalar improvements, RA changes the attachment-cell geometry:
the global FS circumcenter prevents the ZK/GU isodiametric disk from being an actual
large-cell extremizer below the `120`-degree wrapping threshold.

## 8. Next target

Extend Lemma RA.2 to a quantitative sharp area envelope for circle subsets with

```math
\sqrt3/2<z<1.
```

The endpoint margin (5.6) is large, so even a fairly coarse wrapped-cell bound beyond
`sqrt(3)/2` should raise the explicit constant again.  The required auxiliary problem
is now purely planar:

> Given a subset of the radius-`1/2` circle with Euclidean diameter at most `z`, bound
> the area of its convex hull as a function of `z`.

Any envelope substantially below the free isodiametric value `pi z^2/4` feeds directly
through (4.2), JS.3, and RP cavity capacity.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For each unloaded component,
  diam(A_r)<=delta_r+2,
and FS puts every loaded attachment at radius D/2+o(D) from one common center.
If delta_r/D->z<sqrt(3)/2, the limiting attachment directions cannot surround the
center: a surrounding triangle has a pair separated by >=120 degrees.  Hence the
attachments lie in an arc of angle 2asin z and
  area(P_r)/D^2 <= B(z)=[asin z-z sqrt(1-z^2)]/4.
B is increasing, convex, and superadditive.
At z=sqrt(3)/2 the only additional wrapping limit is the equilateral triangle,
area 3sqrt(3)/16.
Since sum delta_r<=mu_D D+6, every limit with mu<=sqrt(3)/2 has
  C_att/D^2<=3sqrt(3)/16.
JS gives x=(d_P+Q)/D<=(2mu+pi)/3 and RP gives G/D^2<=x^2/(4pi).
At mu=sqrt(3)/2,
  area(F)/D^2 <=3sqrt(3)/16+(pi+sqrt3)^2/(36pi)
               <2179/4032,
while FSDB gives
  area(F)/D^2>154451/250000.
Exact margin 4874777/63000000>0.
Thus no limit mu<=sqrt(3)/2 exists, and compactness gives
  mu_D>=sqrt(3)/2+epsilon_RA
for all sufficiently large post-ZF survivors.

Next: solve/bound the wrapped circle-subset area problem for z>sqrt(3)/2.
```
