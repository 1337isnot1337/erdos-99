<!-- theorem-state: {"artifact_id":"ART-DEC31DE08127","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact one-defect difference-body normal form for the cyclic `d_H=1` phase

**Date:** 2026-09-09  
**Repository branch:** PR #118 after AD/UW/R2  
**Run type:** exact finite convex-geometry classification  
**Target:** cyclic primitive phase `d_H=1`  
**Depends on:** AD defect split, Minkowski edge-direction merge, UW/RP ladder notation  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

AD leaves exactly two `d_H=1` cases:

1. `P1`: one parallel pair of primal force-hull sides and no off-circle difference-body vertex pair;
2. `S1`: no parallel primal sides and exactly one antipodal off-circle difference-body vertex pair.

Because every side of `F` has length one, the Minkowski edge lengths of `K=F-F` are also determined: an unmerged direction contributes a unit edge, while a direction in which a side of `F` and a side of `-F` merge contributes an edge of length two.

This makes the complete `d_H=1` difference body explicitly solvable.

Put

\[
\delta:=2\arcsin\frac1{2D},
\qquad
\Delta_2:=2\arcsin\frac1D,
\qquad
q_R:=\frac\pi\delta,
\qquad
s:=q_R-q>0.
\tag{1.1}
\]

### Theorem D1 — exact one-defect family

Every cyclic `d_H=1` survivor falls into exactly one of the following two forms.

### S1: one short antipodal vertex pair

`K=F-F` has `2q` edges, every edge has length one, and all vertices lie on the radius-`D` circle except one antipodal pair `x,-x`.

Let `a,b` be the two circular neighbors of `x` and let `G` be their central angular separation. Then

\[
\boxed{G=(s+2)\delta,}
\tag{D1.1}
\]

\[
\boxed{2\delta<G<\Delta_2,}
\tag{D1.2}
\]

and `x` lies on the outward angular bisector of `a,b` with radius

\[
\boxed{
|x|
=D\cos\frac G2
+
\sqrt{1-D^2\sin^2\frac G2}.}
\tag{D1.3}
\]

Consequently

\[
\boxed{
0<s< s_P(D):=\frac{\Delta_2}{\delta}-2.}
\tag{D1.4}
\]

### P1: one parallel-side pair

`K` has `2q-2` vertices, every vertex lies on the radius-`D` circle, exactly one antipodal pair of edges has length two, and every other edge has length one.

The central-angle sum is exact:

\[
\boxed{(q-2)\delta+\Delta_2=\pi.}
\tag{D1.5}
\]

Equivalently

\[
\boxed{s=s_P(D)=\frac{\Delta_2}{\delta}-2.}
\tag{D1.6}
\]

Thus P1 is precisely the endpoint of the S1 family at which the off-circle vertex reaches the chord joining its two circular neighbors and ceases to be an extreme point.

In particular every `d_H=1` survivor satisfies the sharper second-order bound

\[
\boxed{
0<s\le \frac{\Delta_2}{\delta}-2.}
\tag{D1.7}
\]

Since

\[
\frac{\Delta_2}{\delta}-2
=\frac1{4D^2}+\frac{5}{64D^4}+O(D^{-6}),
\]

we obtain

\[
\boxed{
\limsup D^2(q_R-q)\le\frac14,}
\tag{D1.8}
\]

improving R2's `1/2` constant by a factor of two.

Equivalently

\[
\boxed{
D-D_R(q)
\le
\frac1{4\pi D^2}+o(D^{-2}).}
\tag{D1.9}
\]

---

## 1. Difference-body edge lengths are `1` or `2`

The edge-direction list of

\[
K=F+(-F)
\]

is the cyclic merge of the edge directions of `F` and `-F`.

Every force-hull edge has Euclidean length one.

- If an oriented direction occurs in only one summand, the corresponding Minkowski edge is exactly that one unit edge and has length one.
- If a side of `F` is parallel to an oppositely oriented side of `F`, then in `F+(-F)` the two same-oriented unit edge vectors add. The resulting Minkowski edge has length two.

AD says `d_H=1` has either zero or one parallel-side pair. Therefore:

- S1 has `2q` unit edges;
- P1 has `2q-2` edges, with one antipodal pair of length-two edges and all remaining edges unit.

This is exact, not asymptotic.

---

## 2. S1: only one half-boundary vertex is off the circle

By AD, S1 has exactly one off-circle antipodal pair. Consider one projective half of the centrally symmetric polygon `K`.

There are `q` vertices and `q` unit edges in the half-boundary. Exactly one vertex, `x`, is off the radius-`D` circle. Its two neighbors `a,b` are circular, because there is no second off-circle vertex in the same half.

Every other half-boundary edge joins two radius-`D` circular vertices and has length one. Hence its central angle is exactly

\[
\delta=2\arcsin\frac1{2D}.
\]

There are `q-2` such ordinary edges. Let `G` be the total polar angle from `a` to `b` through `x`. The half-boundary angle sum is `pi`, so

\[
(q-2)\delta+G=\pi.
\]

Using `pi=q_R delta=(q+s)delta` gives

\[
G=(s+2)\delta,
\]

proving D1.1.

Since `s>0` in a genuine one-defect phase,

\[
G>2\delta.
\tag{2.1}
\]

---

## 3. S1: solve the short vertex exactly

The two circular neighbors have equal radius

\[
|a|=|b|=D,
\]

and the adjacent difference-body edges are unit:

\[
|a-x|=|x-b|=1.
\]

Thus `x` lies on the perpendicular bisector of `ab`. Because the origin also lies on that bisector, `x` lies on the angular bisector of the two circular rays.

Write

\[
r:=|x|.
\]

The law of cosines in triangle `0ax` gives

\[
1=D^2+r^2-2Dr\cos(G/2).
\tag{3.1}
\]

Solving the quadratic in `r` gives

\[
r
=D\cos\frac G2
\pm
\sqrt{1-D^2\sin^2\frac G2}.
\tag{3.2}
\]

The boundary of the convex body lies on the side of chord `ab` away from the origin, so `x` is the outward intersection of the two unit circles centered at `a,b`. This selects the plus sign and proves D1.3.

Existence requires

\[
D\sin(G/2)\le1,
\]

or

\[
G\le2\arcsin\frac1D=\Delta_2.
\tag{3.3}
\]

If equality held, the two unit circles would be tangent and `x` would lie on the straight chord segment `ab`. It would not be an extreme vertex of `K`; the two collinear unit edges would merge into one length-two Minkowski edge. That is P1, not S1.

Hence S1 has the strict inequality

\[
G<\Delta_2.
\]

Together with (2.1), this proves D1.2 and D1.4.

---

## 4. P1: the collapsed endpoint

In P1 every vertex of `K` lies on the radius-`D` circle. In one projective half-boundary there are

\[
q-1
\]

edges:

- `q-2` unit edges, each subtending angle `delta`;
- one length-two edge, subtending angle
  \[
  \Delta_2=2\arcsin(1/D).
  \]

The half-circle angle sum is therefore

\[
(q-2)\delta+\Delta_2=\pi,
\]

proving D1.5.

Since `pi=(q+s)delta`, rearrangement gives

\[
s=\frac{\Delta_2}{\delta}-2,
\]

which is D1.6.

Geometrically this is exactly the S1 limit `G -> Delta_2`: the two unit edges from `a` to the off-circle vertex and then to `b` become collinear, the middle point ceases to be extreme, and the Minkowski boundary records one length-two edge.

---

## 5. Sharpen the Reinhardt-ladder defect

Both S1 and P1 give

\[
0<s\le s_P(D)
:=\frac{\Delta_2}{\delta}-2.
\]

Using

\[
\arcsin x=x+\frac{x^3}{6}+\frac{3x^5}{40}+O(x^7),
\]

we get

\[
\Delta_2
=\frac2D+\frac1{3D^3}+\frac{3}{20D^5}+O(D^{-7}),
\]

\[
\delta
=\frac1D+\frac1{24D^3}+\frac{3}{640D^5}+O(D^{-7}).
\]

Division gives

\[
\boxed{
\frac{\Delta_2}{\delta}-2
=\frac1{4D^2}+\frac{5}{64D^4}+O(D^{-6}).}
\tag{5.1}
\]

This proves D1.8.

Since `q_R'(D)=pi+o(1)`, the same mean-value argument as R2 gives D1.9.

---

## 6. Exact short-antipodal length as a function of ladder defect

In S1, combine

\[
G=(s+2)\delta
\]

with D1.3:

\[
\boxed{
|x|
=D\cos\left(\frac{(s+2)\delta}{2}\right)
+
\sqrt{1-D^2\sin^2\left(\frac{(s+2)\delta}{2}\right)}.}
\tag{6.1}
\]

Thus the unique canonical short antipodal pair is not an independent geometric parameter: its Euclidean length is an explicit function of `D` and the single scalar ladder defect `s`.

As `s downarrow0`, `|x|uparrow D`, recovering the zero-defect circular vertex.

As `s uparrow s_P(D)`, the square-root term tends to zero and

\[
|x|\to\sqrt{D^2-1}
=D-\frac1{2D}+O(D^{-3}),
\]

exactly matching UW's sharp `1/(2D)` endpoint scale.

So the complete S1 short-length interval is

\[
\boxed{
\sqrt{D^2-1}<|x|<D.}
\tag{6.2}
\]

---

## 7. P2 all-circular corollary

The same argument gives an exact formula for the `d_H=2`, `r_parallel=2`, `a_short=0` branch P2.

In one half of `K` there are

- `q-4` unit edges of angular size `delta`;
- two length-two edges of angular size `Delta_2`.

Hence

\[
\boxed{(q-4)\delta+2\Delta_2=\pi,}
\tag{7.1}
\]

or

\[
\boxed{
s=2\left(\frac{\Delta_2}{\delta}-2\right).}
\tag{7.2}
\]

Therefore P2 has the exact asymptotic

\[
\boxed{s=\frac1{2D^2}+\frac{5}{32D^4}+O(D^{-6}).}
\tag{7.3}
\]

This is far sharper than the universal R2 `d_H=2` upper constant `2`.

---

## 8. Regression audit

### Power-of-two equilateral near-extremizers

Compatible. The P1 endpoint is exactly the sort of one-defect difference-body geometry that near-Reinhardt even polygons can approach. No shell-only contradiction is claimed.

### S1 off-circle vertex on the inward unit-circle intersection

Rejected by convexity: that intersection lies on the origin side of chord `ab` and cannot be the boundary vertex replacing the outer circular arc.

### P1 transition

At `G=Delta_2`, the off-circle vertex is collinear with its neighbors and is no longer a polygon vertex, so AD correctly switches from `(r_parallel,a_short)=(0,1)` to `(1,0)`.

### Difference-body edge lengths

A merged edge has length exactly two because it is the vector sum of two same-oriented unit primal/Minkowski edges; no unknown scale is introduced.

---

## 9. What this changes

The entire `d_H=1` difference-body geometry is now one scalar family:

```text
0 < s < s_P(D):
    S1, one off-circle antipodal vertex pair,
    all 2q K-edges unit,
    G=(s+2)delta,
    short radius given exactly by D1.3.

s = s_P(D):
    P1, off-circle pair collapses,
    one antipodal pair of K-edges has length 2,
    all K vertices circular.
```

with

\[
s_P(D)=\frac1{4D^2}+O(D^{-4}).
\]

Thus `d_H=1` is twice as close to the Reinhardt ladder as R2 alone proved, and its only canonical geometric defect has an explicit one-parameter formula.

---

## 10. Next theorem

The highest-value `d_H=1` target is now no longer a vague stability statement. It is to insert the explicit D1 geometry into either:

1. the difference-body sign-code/closure equations reconstructing the primal equilateral polygon `F`; or
2. the KKT/WT four-block tree endpoint.

In S1, every difference-body edge is unit and only one antipodal vertex pair leaves the circle. In P1, all vertices are circular and only one antipodal edge pair has length two. Both are finite codimension-one perturbations of the exact Reinhardt difference body.

A complete sign-code classification of this one-defect family would settle the shell geometry of `d_H=1`.

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**

D1 is elementary downstream of AD. No external theorem is imported.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For K=F-F, Minkowski edge lengths are exact:
  unmerged direction -> length 1;
  parallel primal-side merge -> length 2.

d_H=1 has only AD branches S1=(r_parallel=0,a_short=1) and P1=(1,0).
Let delta=2asin(1/(2D)), Delta2=2asin(1/D), q_R=pi/delta, s=q_R-q.

S1:
  K has 2q unit edges and one off-circle antipodal vertex pair x,-x.
  In one half, q-2 ordinary circle-circle unit edges have angle delta.
  If a,x,b is the defect chain and G=angle(a,0,b),
    (q-2)delta+G=pi,
  so G=(s+2)delta.
  Since |a-x|=|x-b|=1 and |a|=|b|=D,
    |x|=D cos(G/2)+sqrt(1-D^2 sin^2(G/2)).
  Extremality gives 2delta<G<Delta2.

P1:
  K has 2q-2 circular vertices; one antipodal edge pair has length 2, rest length1.
  Hence
    (q-2)delta+Delta2=pi,
    s=Delta2/delta-2.

Thus every d_H=1 survivor has
  0<s<=Delta2/delta-2
      =1/(4D^2)+5/(64D^4)+O(D^-6),
sharpening R2's 1/(2D^2) bound by factor 2.
P1 is exactly the endpoint where the S1 defect vertex becomes collinear and merges.
Also P2 satisfies s=2(Delta2/delta-2)=1/(2D^2)+O(D^-4).
```
